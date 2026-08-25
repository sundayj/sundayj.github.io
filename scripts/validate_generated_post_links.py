#!/usr/bin/env python3
"""Validate internal links/assets rendered inside changed post article bodies."""

from __future__ import annotations

import html
import os
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from scripts.validate_blog_posts import parse_front_matter, parse_name_status

SITE_DIR = Path("_site")


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(["git", *args], check=True, capture_output=True, text=True)
    return [line.rstrip() for line in result.stdout.splitlines() if line.strip()]


def changed_posts() -> list[str]:
    base_sha = os.environ.get("BLOG_BASE_SHA")
    if not base_sha:
        return []
    entries = parse_name_status(
        git_lines("diff", "--name-status", "--diff-filter=ACMR", base_sha, "HEAD")
    )
    return [path for _, path in entries if path.startswith("_posts/") and Path(path).exists()]


class PostHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_h1 = False
        self.h1_parts: list[str] = []
        self.article_depth = 0
        self.urls: list[str] = []
        self.ids: set[str] = set()

    @property
    def title(self) -> str:
        return "".join(self.h1_parts).strip()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "h1" and self.article_depth == 0:
            self.in_h1 = True
        if attr.get("id"):
            self.ids.add(str(attr["id"]))
        if tag == "article" and attr.get("id") == "article":
            self.article_depth = 1
            return
        if self.article_depth:
            self.article_depth += 1
            for name in ("href", "src"):
                if attr.get(name):
                    self.urls.append(str(attr[name]))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if attr.get("id"):
            self.ids.add(str(attr["id"]))
        if self.article_depth:
            for name in ("href", "src"):
                if attr.get(name):
                    self.urls.append(str(attr[name]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self.in_h1 = False
        if self.article_depth:
            self.article_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_h1:
            self.h1_parts.append(data)


def parse_html(path: Path) -> PostHTMLParser:
    parser = PostHTMLParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def generated_pages() -> dict[str, tuple[Path, PostHTMLParser]]:
    pages: dict[str, tuple[Path, PostHTMLParser]] = {}
    for path in SITE_DIR.rglob("*.html"):
        parser = parse_html(path)
        if parser.title:
            pages[html.unescape(parser.title)] = (path, parser)
    return pages


def site_url_for(path: Path) -> str:
    relative = path.relative_to(SITE_DIR).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def resolve_target(current: Path, raw_url: str) -> tuple[Path | None, str | None]:
    url = raw_url.strip()
    if not url or "{{" in url or "{%" in url:
        return None, None
    if url.startswith("//"):
        return None, None

    parsed = urlparse(url)
    if parsed.scheme in {"http", "https", "mailto", "tel", "data"}:
        return None, None
    if parsed.scheme:
        return Path("__invalid_scheme__"), None

    current_url = site_url_for(current)
    joined = urlparse(urljoin("https://jlsunday.invalid" + current_url, url))
    path_part = unquote(joined.path)
    fragment = unquote(joined.fragment) or None

    candidate = SITE_DIR / path_part.lstrip("/")
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


def validate_page(path: Path, parser: PostHTMLParser) -> list[str]:
    errors: list[str] = []
    parser_cache: dict[Path, PostHTMLParser] = {path: parser}
    for raw_url in parser.urls:
        target, fragment = resolve_target(path, raw_url)
        if target is None:
            continue
        if target == Path("__invalid_scheme__"):
            errors.append(f"unsupported internal URL scheme: `{raw_url}`")
            continue
        if not target.is_file():
            errors.append(f"internal link/asset does not resolve in generated site: `{raw_url}`")
            continue
        if fragment and target.suffix == ".html":
            target_parser = parser_cache.setdefault(target, parse_html(target))
            if fragment not in target_parser.ids:
                errors.append(f"fragment `#{fragment}` does not exist at `{raw_url.split('#', 1)[0] or site_url_for(path)}`")
    return errors


def main() -> int:
    posts = changed_posts()
    if not posts:
        print("No changed published posts require generated-link validation.")
        return 0

    pages = generated_pages()
    failures = 0
    for source_path in posts:
        front_matter, _, error = parse_front_matter(Path(source_path).read_text(encoding="utf-8"))
        if error:
            print(f"SKIP {source_path}: front matter already failed source validation")
            continue
        title = str(front_matter.get("title", "")).strip()
        generated = pages.get(title)
        if not generated:
            failures += 1
            print(f"FAIL {source_path}")
            print(f"  - could not locate generated HTML page with H1 `{title}`")
            continue
        path, parser = generated
        errors = validate_page(path, parser)
        if errors:
            failures += 1
            print(f"FAIL {source_path} -> {path}")
            for item in errors:
                print(f"  - {item}")
        else:
            print(f"OK   {source_path} -> {path}")

    if failures:
        print(f"\n{failures} generated post page(s) failed link validation.", file=sys.stderr)
        return 1
    print(f"\nValidated generated links for {len(posts)} changed published post(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
