#!/usr/bin/env python3
"""Validate generated Jekyll SEO/social metadata ownership and image behavior."""

from __future__ import annotations

import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

SEO_MARKER = "<!-- Begin Jekyll SEO tag"
SITE_ORIGIN = "https://jlsunday.com"
DEFAULT_SOCIAL_IMAGE = f"{SITE_ORIGIN}/assets/images/JLSunday-logo/cover2-Logo.png"
PARSER_ARTICLE_SLUG = "your-parser-shouldnt-get-one-shot"
PARSER_ARTICLE_IMAGE = f"{SITE_ORIGIN}/assets/images/posts/undraw/undraw_Design_objectives_re_94pd.png"
REQUIRED_TWITTER_CARD = "summary_large_image"
MAX_SOCIAL_IMAGE_BYTES = 5 * 1024 * 1024
MIN_SOCIAL_IMAGE_WIDTH = 300
MIN_SOCIAL_IMAGE_HEIGHT = 157


class HeadMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_head = False
        self.canonical: list[str] = []
        self.description: list[str] = []
        self.og_title: list[str] = []
        self.og_description: list[str] = []
        self.og_url: list[str] = []
        self.og_image: list[str] = []
        self.twitter_card: list[str] = []
        self.twitter_title: list[str] = []
        self.twitter_description: list[str] = []
        self.twitter_image: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "head":
            self.in_head = True
            return
        if not self.in_head:
            return

        attributes = dict(attrs)
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical.append(attributes.get("href") or "")
        elif tag == "meta":
            content = attributes.get("content") or ""
            name = attributes.get("name")
            property_name = attributes.get("property")

            if name == "description":
                self.description.append(content)
            elif name == "twitter:card":
                self.twitter_card.append(content)
            elif name == "twitter:title":
                self.twitter_title.append(content)
            elif name == "twitter:description":
                self.twitter_description.append(content)
            elif name == "twitter:image":
                self.twitter_image.append(content)

            if property_name == "og:title":
                self.og_title.append(content)
            elif property_name == "og:description":
                self.og_description.append(content)
            elif property_name == "og:url":
                self.og_url.append(content)
            elif property_name == "og:image":
                self.og_image.append(content)

    def handle_endtag(self, tag: str) -> None:
        if tag == "head":
            self.in_head = False


def validate_single(name: str, values: list[str]) -> list[str]:
    errors: list[str] = []
    if len(values) != 1:
        errors.append(f"{name}: expected 1, found {len(values)}")
    elif not values[0].strip():
        errors.append(f"{name}: value is empty")
    return errors


def parse_metadata(html: str) -> HeadMetadataParser:
    parser = HeadMetadataParser()
    parser.feed(html)
    return parser


def validate_https_url(name: str, values: list[str]) -> list[str]:
    if len(values) != 1 or not values[0].strip():
        return []
    parsed = urlparse(values[0])
    if parsed.scheme != "https" or not parsed.netloc:
        return [f"{name} must be an absolute HTTPS URL, found `{values[0]}`"]
    return []


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def jpeg_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        return None

    index = 2
    while index + 9 < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        while index < len(data) and data[index] == 0xFF:
            index += 1
        if index >= len(data):
            break

        marker = data[index]
        index += 1
        if marker in {0xD8, 0xD9}:
            continue
        if index + 2 > len(data):
            break

        segment_length = int.from_bytes(data[index:index + 2], "big")
        if segment_length < 2 or index + segment_length > len(data):
            break

        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            if segment_length < 7:
                return None
            height = int.from_bytes(data[index + 3:index + 5], "big")
            width = int.from_bytes(data[index + 5:index + 7], "big")
            return width, height

        index += segment_length
    return None


def image_dimensions(path: Path) -> tuple[int, int] | None:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return png_dimensions(path)
    if suffix in {".jpg", ".jpeg"}:
        return jpeg_dimensions(path)
    return None


def validate_social_image(site_dir: Path, image_url: str) -> list[str]:
    errors: list[str] = []
    parsed = urlparse(image_url)
    site = urlparse(SITE_ORIGIN)
    if parsed.scheme != "https" or parsed.netloc != site.netloc:
        errors.append(f"social image must resolve to `{SITE_ORIGIN}` over HTTPS, found `{image_url}`")
        return errors

    local_path = site_dir / unquote(parsed.path).lstrip("/")
    if not local_path.is_file():
        errors.append(f"social image does not exist in built site: `{local_path}`")
        return errors

    size = local_path.stat().st_size
    if size == 0:
        errors.append(f"social image is empty: `{local_path}`")
        return errors
    if size > MAX_SOCIAL_IMAGE_BYTES:
        errors.append(
            f"social image exceeds {MAX_SOCIAL_IMAGE_BYTES // (1024 * 1024)} MiB: `{local_path}` is {size} bytes"
        )

    dimensions = image_dimensions(local_path)
    if dimensions is None:
        errors.append(f"social image must be a valid PNG or JPEG with readable dimensions: `{local_path}`")
        return errors

    width, height = dimensions
    if width < MIN_SOCIAL_IMAGE_WIDTH or height < MIN_SOCIAL_IMAGE_HEIGHT:
        errors.append(
            f"social image is too small for a large preview: `{local_path}` is {width}x{height}; "
            f"minimum is {MIN_SOCIAL_IMAGE_WIDTH}x{MIN_SOCIAL_IMAGE_HEIGHT}"
        )
    return errors


def validate_html(path: Path, html: str) -> tuple[list[str], HeadMetadataParser]:
    parser = parse_metadata(html)

    errors: list[str] = []
    metadata = {
        "canonical": parser.canonical,
        "description": parser.description,
        "og:title": parser.og_title,
        "og:description": parser.og_description,
        "og:url": parser.og_url,
        "og:image": parser.og_image,
        "twitter:card": parser.twitter_card,
        "twitter:title": parser.twitter_title,
        "twitter:description": parser.twitter_description,
        "twitter:image": parser.twitter_image,
    }
    for name, values in metadata.items():
        errors.extend(validate_single(name, values))

    for name, values in {
        "canonical": parser.canonical,
        "og:url": parser.og_url,
        "og:image": parser.og_image,
        "twitter:image": parser.twitter_image,
    }.items():
        errors.extend(validate_https_url(name, values))

    if parser.twitter_card and parser.twitter_card[0] != REQUIRED_TWITTER_CARD:
        errors.append(
            f"twitter:card must be `{REQUIRED_TWITTER_CARD}`, found `{parser.twitter_card[0]}`"
        )
    if parser.og_image and parser.twitter_image and parser.og_image[0] != parser.twitter_image[0]:
        errors.append(
            f"twitter:image must match og:image; found `{parser.twitter_image[0]}` vs `{parser.og_image[0]}`"
        )
    if parser.canonical and parser.og_url and parser.canonical[0] != parser.og_url[0]:
        errors.append(
            f"og:url must match canonical URL; found `{parser.og_url[0]}` vs `{parser.canonical[0]}`"
        )

    return errors, parser


def main() -> int:
    site_dir = Path("_site")
    if not site_dir.is_dir():
        print("_site does not exist; run the Jekyll build first", file=sys.stderr)
        return 2

    html_files = sorted(site_dir.rglob("*.html"))
    if not html_files:
        print("No generated HTML files found in _site", file=sys.stderr)
        return 2

    failures: list[str] = []
    metadata_by_path: dict[Path, HeadMetadataParser] = {}
    validated = 0
    validated_images: set[str] = set()
    for path in html_files:
        html = path.read_text(encoding="utf-8")
        if SEO_MARKER not in html:
            continue
        validated += 1
        errors, parser = validate_html(path, html)
        metadata_by_path[path] = parser
        failures.extend(f"{path}: {error}" for error in errors)

        if len(parser.og_image) == 1 and parser.og_image[0] not in validated_images:
            validated_images.add(parser.og_image[0])
            failures.extend(
                f"{path}: {error}" for error in validate_social_image(site_dir, parser.og_image[0])
            )

    if validated == 0:
        print("No Jekyll-rendered HTML pages containing the SEO tag were found", file=sys.stderr)
        return 2

    homepage = metadata_by_path.get(site_dir / "index.html")
    if homepage is None:
        failures.append("_site/index.html: homepage metadata fixture not found")
    elif homepage.og_image != [DEFAULT_SOCIAL_IMAGE]:
        failures.append(
            f"_site/index.html: expected default social image `{DEFAULT_SOCIAL_IMAGE}`, found {homepage.og_image}"
        )

    parser_fixture = next(
        (
            (path, metadata)
            for path, metadata in metadata_by_path.items()
            if metadata.canonical and PARSER_ARTICLE_SLUG in metadata.canonical[0]
        ),
        None,
    )
    if parser_fixture is None:
        failures.append(f"expected parser article canonical containing `{PARSER_ARTICLE_SLUG}` was not generated")
    else:
        path, metadata = parser_fixture
        if metadata.og_image != [PARSER_ARTICLE_IMAGE]:
            failures.append(
                f"{path}: explicit post image should override the default; expected `{PARSER_ARTICLE_IMAGE}`, found {metadata.og_image}"
            )
        if metadata.description and metadata.twitter_description:
            expected = metadata.description[0][:159]
            if not metadata.twitter_description[0].startswith(expected[:120]):
                failures.append(
                    f"{path}: twitter:description does not reflect the page description; found `{metadata.twitter_description[0]}`"
                )

    if failures:
        print("Generated SEO metadata validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Validated SEO/social metadata across {validated} Jekyll-rendered HTML pages and "
        f"{len(validated_images)} distinct social images."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
