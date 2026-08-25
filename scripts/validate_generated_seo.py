#!/usr/bin/env python3
"""Validate generated Jekyll SEO/social metadata ownership and image behavior."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

SEO_MARKER = "<!-- Begin Jekyll SEO tag"
DEFAULT_SOCIAL_IMAGE = "https://jlsunday.com/assets/images/JLSunday-logo/cover2-Logo.png"
PARSER_ARTICLE_SLUG = "your-parser-shouldnt-get-one-shot"
PARSER_ARTICLE_IMAGE = "https://jlsunday.com/assets/images/posts/undraw/undraw_Design_objectives_re_94pd.png"


class HeadMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_head = False
        self.canonical: list[str] = []
        self.description: list[str] = []
        self.twitter_description: list[str] = []
        self.og_description: list[str] = []
        self.og_image: list[str] = []
        self.twitter_card: list[str] = []

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
            if attributes.get("name") == "description":
                self.description.append(content)
            if attributes.get("name") == "twitter:description":
                self.twitter_description.append(content)
            if attributes.get("name") == "twitter:card":
                self.twitter_card.append(content)
            if attributes.get("property") == "og:description":
                self.og_description.append(content)
            if attributes.get("property") == "og:image":
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


def validate_html(path: Path, html: str) -> tuple[list[str], HeadMetadataParser]:
    parser = parse_metadata(html)

    errors: list[str] = []
    for name, values in {
        "canonical": parser.canonical,
        "description": parser.description,
        "twitter:description": parser.twitter_description,
        "og:description": parser.og_description,
        "og:image": parser.og_image,
        "twitter:card": parser.twitter_card,
    }.items():
        errors.extend(validate_single(name, values))

    if parser.og_image and not parser.og_image[0].startswith("https://"):
        errors.append(f"og:image must resolve to an absolute HTTPS URL, found `{parser.og_image[0]}`")

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
    for path in html_files:
        html = path.read_text(encoding="utf-8")
        if SEO_MARKER not in html:
            continue
        validated += 1
        errors, parser = validate_html(path, html)
        metadata_by_path[path] = parser
        failures.extend(f"{path}: {error}" for error in errors)

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
        f"Validated SEO/social metadata across {validated} Jekyll-rendered HTML pages, including default and per-post image behavior."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
