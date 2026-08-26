#!/usr/bin/env python3
"""Validate internal links and assets across the complete generated Jekyll site."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

SITE_DIR = Path("_site")
SKIPPED_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class SiteHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.urls: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def _collect(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if attr.get("id"):
            self.ids.add(str(attr["id"]))
        if attr.get("name") and tag == "a":
            self.ids.add(str(attr["name"]))
        for name in ("href", "src"):
            if attr.get(name):
                self.urls.append((name, str(attr[name])))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._collect(tag, attrs)


def parse_html(path: Path) -> SiteHTMLParser:
    parser = SiteHTMLParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def generated_html_pages(site_dir: Path = SITE_DIR) -> list[Path]:
    return sorted(site_dir.rglob("*.html"))


def site_url_for(path: Path, site_dir: Path = SITE_DIR) -> str:
    relative = path.relative_to(site_dir).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def resolve_target(
    current: Path,
    raw_url: str,
    site_dir: Path = SITE_DIR,
) -> tuple[Path | None, str | None]:
    url = raw_url.strip()
    if not url or "{{" in url or "{%" in url or url.startswith("//"):
        return None, None

    parsed = urlparse(url)
    if parsed.scheme in SKIPPED_SCHEMES:
        return None, None
    if parsed.scheme:
        return None, None

    current_url = site_url_for(current, site_dir)
    joined = urlparse(urljoin("https://jlsunday.invalid" + current_url, url))
    path_part = unquote(joined.path)
    fragment = unquote(joined.fragment) or None

    candidate = site_dir / path_part.lstrip("/")
    possibilities: list[Path] = []
    if path_part.endswith("/"):
        possibilities.append(candidate / "index.html")
    else:
        possibilities.append(candidate)
        if not candidate.suffix:
            possibilities.extend([Path(str(candidate) + ".html"), candidate / "index.html"])

    for possibility in possibilities:
        if possibility.is_file():
            return possibility, fragment
    return possibilities[0] if possibilities else candidate, fragment


def validate_page(
    path: Path,
    parser: SiteHTMLParser,
    site_dir: Path = SITE_DIR,
    parser_cache: dict[Path, SiteHTMLParser] | None = None,
) -> list[str]:
    errors: list[str] = []
    cache = parser_cache if parser_cache is not None else {path: parser}

    for attribute, raw_url in parser.urls:
        target, fragment = resolve_target(path, raw_url, site_dir)
        if target is None:
            continue
        if not target.is_file():
            errors.append(f"{attribute} does not resolve in generated site: `{raw_url}`")
            continue
        if fragment and target.suffix == ".html":
            target_parser = cache.setdefault(target, parse_html(target))
            if fragment not in target_parser.ids:
                errors.append(
                    f"fragment `#{fragment}` does not exist at "
                    f"`{raw_url.split('#', 1)[0] or site_url_for(path, site_dir)}`"
                )
    return errors


def validate_site(site_dir: Path = SITE_DIR) -> dict[Path, list[str]]:
    pages = generated_html_pages(site_dir)
    parser_cache = {path: parse_html(path) for path in pages}
    failures: dict[Path, list[str]] = {}

    for path, parser in parser_cache.items():
        errors = validate_page(path, parser, site_dir, parser_cache)
        if errors:
            failures[path] = errors
    return failures


def main() -> int:
    if not SITE_DIR.is_dir():
        print(f"Generated site directory does not exist: {SITE_DIR}", file=sys.stderr)
        return 1

    pages = generated_html_pages()
    failures = validate_site()

    if failures:
        for path, errors in failures.items():
            print(f"FAIL {path}")
            for item in errors:
                print(f"  - {item}")
        print(
            f"\n{len(failures)} generated page(s) contain broken internal links or assets.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Validated internal href/src targets and fragments across "
        f"{len(pages)} generated HTML page(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
