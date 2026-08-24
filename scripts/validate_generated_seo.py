#!/usr/bin/env python3
"""Validate generated Jekyll page metadata used by the JE-001 evidence gate."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

SEO_MARKER = "<!-- Begin Jekyll SEO tag"


class HeadMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_head = False
        self.canonical_count = 0
        self.description_count = 0
        self.twitter_description_count = 0
        self.og_description_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "head":
            self.in_head = True
            return
        if not self.in_head:
            return

        attributes = dict(attrs)
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical_count += 1
        elif tag == "meta":
            if attributes.get("name") == "description":
                self.description_count += 1
            if attributes.get("name") == "twitter:description":
                self.twitter_description_count += 1
            if attributes.get("property") == "og:description":
                self.og_description_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "head":
            self.in_head = False


def validate_html(path: Path, html: str) -> list[str]:
    parser = HeadMetadataParser()
    parser.feed(html)

    errors: list[str] = []
    expected_counts = {
        "canonical": parser.canonical_count,
        "description": parser.description_count,
        "twitter:description": parser.twitter_description_count,
        "og:description": parser.og_description_count,
    }
    for name, count in expected_counts.items():
        if count != 1:
            errors.append(f"{name}: expected 1, found {count}")
    return errors


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
    validated = 0
    for path in html_files:
        html = path.read_text(encoding="utf-8")
        # Raw verification files and vendored/demo HTML assets do not use the
        # Jekyll layout or SEO tag and are intentionally outside this gate.
        if SEO_MARKER not in html:
            continue
        validated += 1
        errors = validate_html(path, html)
        failures.extend(f"{path}: {error}" for error in errors)

    if validated == 0:
        print("No Jekyll-rendered HTML pages containing the SEO tag were found", file=sys.stderr)
        return 2

    if failures:
        print("Generated SEO metadata validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Validated SEO metadata ownership across {validated} Jekyll-rendered HTML pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
