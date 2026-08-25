#!/usr/bin/env python3
"""Validate changed Jekyll posts/drafts against the current editorial contract.

New posts are held to the current contract. Untouched or lightly edited legacy posts
remain valid unless they opt into the current plural `categories` metadata shape.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

POST_RE = re.compile(
    r"^_posts/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\.(?:md|markdown)$",
    re.IGNORECASE,
)
DRAFT_RE = re.compile(r"^_drafts/.+\.(?:md|markdown)$", re.IGNORECASE)
CURRENT_REQUIRED = {"layout", "title", "date", "description", "categories", "tags"}
LEGACY_REQUIRED = {"layout", "title"}
DRAFT_REQUIRED = {"layout", "title"}
DEPRECATED_CURRENT_FIELDS = {
    "summary": "use `description` as the single card/search/social summary",
    "excerpt": "let Jekyll derive the excerpt unless the article has a specific editorial need",
    "canonical_url": "let jekyll-seo-tag derive the canonical URL from the generated post URL",
    "category": "use plural `categories` from the reader-facing taxonomy",
}
ALLOWED_CATEGORIES = {
    "AI & Software Engineering",
    "Software Architecture",
    "Python & Django",
    "C# & .NET",
    "Angular",
    "Building Software",
    "DevOps & Cloud",
    "Developer Tools",
}
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|SOURCE NEEDED|CITATION NEEDED|FIXME)\b", re.IGNORECASE)
EMPTY_YAML_VALUES = {"", "''", '""', "[]", "{}", "null", "~"}
BLOCK_SCALAR_MARKERS = {">", ">-", ">+", "|", "|-", "|+"}
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
HTML_URL_RE = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(["git", *args], check=True, capture_output=True, text=True)
    return [line.rstrip() for line in result.stdout.splitlines() if line.strip()]


def parse_name_status(lines: list[str]) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for line in lines:
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0][0]
        path = parts[-1]
        entries.append((status, path))
    return entries


def candidate_entries(argv: list[str]) -> list[tuple[str, str]]:
    if argv:
        return [("M", path) for path in argv]

    base_sha = os.environ.get("BLOG_BASE_SHA")
    if base_sha:
        return parse_name_status(
            git_lines("diff", "--name-status", "--diff-filter=ACMR", base_sha, "HEAD")
        )

    staged = parse_name_status(git_lines("diff", "--cached", "--name-status", "--diff-filter=ACMR"))
    if staged:
        return staged

    return parse_name_status(git_lines("diff", "--name-status", "--diff-filter=ACMR"))


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str] | None:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [unquote(item.strip()) for item in inner.split(",") if item.strip()]


def parse_front_matter(text: str) -> tuple[dict[str, object], str, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, "missing opening YAML front-matter delimiter"

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, text, "missing closing YAML front-matter delimiter"

    values: dict[str, object] = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or line[0].isspace() or ":" not in line:
            i += 1
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()

        if value in BLOCK_SCALAR_MARKERS:
            block_lines: list[str] = []
            i += 1
            while i < end and (not lines[i].strip() or lines[i][0].isspace()):
                block_lines.append(lines[i].strip())
                i += 1
            values[key] = "\n".join(part for part in block_lines if part).strip()
            continue

        if value == "":
            items: list[str] = []
            i += 1
            while i < end and (not lines[i].strip() or lines[i][0].isspace()):
                stripped = lines[i].strip()
                if stripped.startswith("- "):
                    items.append(unquote(stripped[2:].strip()))
                i += 1
            values[key] = items if items else ""
            continue

        inline_list = parse_inline_list(value)
        values[key] = inline_list if inline_list is not None else unquote(value)
        i += 1

    return values, "\n".join(lines[end + 1 :]), None


def has_value(value: object | None) -> bool:
    if value is None:
        return False
    if isinstance(value, list):
        return bool(value)
    return str(value).strip().lower() not in EMPTY_YAML_VALUES


def as_list(value: object | None) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if not has_value(value):
        return []
    return [str(value).strip()]


def as_bool(value: object | None) -> bool:
    return str(value).strip().lower() == "true"


def visible_body_lines(body: str) -> list[str]:
    output: list[str] = []
    fence: str | None = None
    for line in body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            output.append(line)
    return output


def validate_headings(body: str) -> list[str]:
    errors: list[str] = []
    for line_no, line in enumerate(visible_body_lines(body), start=1):
        if re.match(r"^\s*#\s+\S", line):
            errors.append(
                f"body line {line_no} uses an H1; the post layout already renders the article title, so body headings must start at H2"
            )
        if re.match(r"^\s*#{2,6}\s*$", line):
            errors.append(f"body line {line_no} contains an empty heading")
    return errors


def iter_urls(body: str) -> list[str]:
    return MARKDOWN_LINK_RE.findall(body) + HTML_URL_RE.findall(body)


def validate_url_conventions(body: str) -> list[str]:
    errors: list[str] = []
    for raw_url in iter_urls(body):
        url = raw_url.strip()
        if not url or "{{" in url or "{%" in url or url.startswith("#"):
            continue
        lowered = url.lower()
        if lowered.startswith(("javascript:", "file:")):
            errors.append(f"unsafe link scheme in `{url}`")
            continue
        parsed = urlparse(url)
        if parsed.hostname in {"localhost", "127.0.0.1", "0.0.0.0"}:
            errors.append(f"local-only URL must not be published: `{url}`")
        if "example.com" in lowered or "example.org" in lowered or "example.net" in lowered:
            errors.append(f"placeholder example URL must not be published: `{url}`")
    return errors


def validate_image(front_matter: dict[str, object]) -> list[str]:
    errors: list[str] = []
    image = front_matter.get("image")
    if as_bool(front_matter.get("featured")) and not has_value(image):
        errors.append("featured posts must provide an `image` for card/social presentation")
    if not has_value(image):
        return errors

    image_url = str(image).strip()
    if image_url.startswith("https://"):
        return errors
    if image_url.startswith("http://"):
        errors.append("`image` must use HTTPS or a root-relative `/assets/...` path")
        return errors
    if not image_url.startswith("/assets/"):
        errors.append("local `image` must be root-relative under `/assets/`")
        return errors

    local_path = Path(image_url.split("?", 1)[0].split("#", 1)[0].lstrip("/"))
    if not local_path.exists():
        errors.append(f"local `image` does not exist: `{image_url}`")
    return errors


def validate(path_str: str, status: str = "M") -> list[str]:
    errors: list[str] = []
    is_post = path_str.startswith("_posts/")
    is_draft = path_str.startswith("_drafts/")
    if not (is_post or is_draft):
        return errors

    path = Path(path_str)
    if not path.exists():
        return errors

    match = POST_RE.match(path_str) if is_post else None
    if is_post and status == "A" and not match:
        errors.append("new published post filename must be lowercase `_posts/YYYY-MM-DD-kebab-case-slug.md` or `.markdown`")
    if is_draft and not DRAFT_RE.match(path_str):
        errors.append("draft must be a Markdown file under `_drafts/`")

    text = path.read_text(encoding="utf-8")
    front_matter, body, parse_error = parse_front_matter(text)
    if parse_error:
        errors.append(parse_error)
        return errors

    current_contract = is_post and (status == "A" or "categories" in front_matter)
    required = CURRENT_REQUIRED if current_contract else (DRAFT_REQUIRED if is_draft else LEGACY_REQUIRED)
    missing = sorted(key for key in required if not has_value(front_matter.get(key)))
    if missing:
        errors.append("missing or empty required front matter: " + ", ".join(missing))

    if has_value(front_matter.get("layout")) and str(front_matter["layout"]).strip() != "post":
        errors.append("`layout` must be `post`")

    if current_contract:
        for field, guidance in DEPRECATED_CURRENT_FIELDS.items():
            if has_value(front_matter.get(field)):
                errors.append(f"current-contract posts must not set `{field}`; {guidance}")

        description = str(front_matter.get("description", "")).strip()
        if description and not 40 <= len(description) <= 220:
            errors.append("`description` should be 40-220 characters and stand alone as the article summary")

        categories = as_list(front_matter.get("categories"))
        unknown_categories = [category for category in categories if category not in ALLOWED_CATEGORIES]
        if unknown_categories:
            errors.append("unknown reader-facing categories: " + ", ".join(unknown_categories))

        tags = as_list(front_matter.get("tags"))
        if len(tags) > 10:
            errors.append("use at most 10 focused tags; prefer a small useful set over keyword stuffing")

        errors.extend(validate_image(front_matter))

    if is_post:
        placeholders = sorted({match.group(0).upper() for match in PLACEHOLDER_RE.finditer(text)})
        if placeholders:
            errors.append("published post contains draft placeholder(s): " + ", ".join(placeholders))
        errors.extend(validate_url_conventions(body))

    errors.extend(validate_headings(body))
    return errors


def main() -> int:
    entries = candidate_entries(sys.argv[1:])
    blog_entries = [(status, path) for status, path in entries if path.startswith(("_posts/", "_drafts/"))]

    if not blog_entries:
        print("No changed blog posts or drafts to validate.")
        return 0

    failures = 0
    for status, path in blog_entries:
        errors = validate(path, status=status)
        if errors:
            failures += 1
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path}")

    if failures:
        print(f"\n{failures} blog file(s) failed validation.", file=sys.stderr)
        return 1

    print(f"\nValidated {len(blog_entries)} changed blog file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
