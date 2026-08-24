#!/usr/bin/env python3
"""Validate generated author/About links without depending on external availability."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

SITE_DIR = Path("_site")


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        self.anchors.append({key: value or "" for key, value in attrs})


def extract_section(html: str, marker: str, closing_tag: str) -> str | None:
    marker_index = html.find(marker)
    if marker_index < 0:
        return None
    end_index = html.find(closing_tag, marker_index)
    if end_index < 0:
        return None
    return html[marker_index : end_index + len(closing_tag)]


def internal_target_exists(href: str) -> bool:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return True

    path = parsed.path
    if not path or path == "/":
        return (SITE_DIR / "index.html").exists()

    relative = path.lstrip("/")
    candidates: list[Path]
    if path.endswith("/"):
        candidates = [SITE_DIR / relative / "index.html", SITE_DIR / relative]
    else:
        candidates = [
            SITE_DIR / relative,
            SITE_DIR / f"{relative}.html",
            SITE_DIR / relative / "index.html",
        ]
    return any(candidate.exists() for candidate in candidates)


def main() -> int:
    if not SITE_DIR.exists():
        raise SystemExit("Generated site directory _site does not exist. Run Jekyll first.")

    failures: list[str] = []
    author_cards = 0
    social_links = 0
    about_link_sections = 0

    for html_file in SITE_DIR.rglob("*.html"):
        html = html_file.read_text(encoding="utf-8", errors="replace")

        card = extract_section(html, 'class="author-card', "</aside>")
        if card:
            author_cards += 1
            parser = AnchorParser()
            parser.feed(card)
            for anchor in parser.anchors:
                href = anchor.get("href", "").strip()
                if not href:
                    failures.append(f"{html_file}: author-card link has an empty href")
                    continue

                parsed = urlsplit(href)
                if parsed.scheme in {"http", "https"}:
                    social_links += 1
                    if parsed.scheme != "https":
                        failures.append(f"{html_file}: social link must use HTTPS: {href}")
                    if anchor.get("target") != "_blank":
                        failures.append(f"{html_file}: external author link must use target=_blank: {href}")
                    rel_tokens = set(anchor.get("rel", "").split())
                    for required in {"noopener", "noreferrer", "me"}:
                        if required not in rel_tokens:
                            failures.append(f"{html_file}: external author link missing rel={required}: {href}")
                    if not anchor.get("aria-label"):
                        failures.append(f"{html_file}: external author link missing aria-label: {href}")
                    if not anchor.get("title"):
                        failures.append(f"{html_file}: external author link missing title: {href}")
                elif not internal_target_exists(href):
                    failures.append(f"{html_file}: internal author link does not resolve in _site: {href}")

        about_links = extract_section(html, 'class="about-links', "</section>")
        if about_links:
            about_link_sections += 1
            parser = AnchorParser()
            parser.feed(about_links)
            for anchor in parser.anchors:
                href = anchor.get("href", "").strip()
                if not href:
                    failures.append(f"{html_file}: About link has an empty href")
                elif not internal_target_exists(href):
                    failures.append(f"{html_file}: About internal link does not resolve in _site: {href}")

    if author_cards == 0:
        failures.append("No generated author-card markup was found.")
    if about_link_sections == 0:
        failures.append("No generated About links section was found.")
    if social_links == 0:
        failures.append("No external social links were found in generated author cards.")

    if failures:
        print("Generated author-link validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Validated {author_cards} author card(s), {about_link_sections} About link section(s), "
        f"and {social_links} external author/social link occurrence(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
