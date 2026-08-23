#!/usr/bin/env python3
"""Validate changed Jekyll blog posts without imposing new rules on untouched legacy posts."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

POST_RE = re.compile(r"^_posts/\d{4}-\d{2}-\d{2}-.+\.(?:md|markdown)$", re.IGNORECASE)
DRAFT_RE = re.compile(r"^_drafts/.+\.(?:md|markdown)$", re.IGNORECASE)
PUBLISHED_REQUIRED = {
    "layout",
    "title",
    "summary",
    "excerpt",
    "description",
    "canonical_url",
    "category",
    "tags",
    "date",
    "author",
}
DRAFT_REQUIRED = {"layout", "title"}
PLACEHOLDERS = (
    "TODO",
    "TBD",
    "SOURCE NEEDED",
    "CITATION NEEDED",
    "FIXME",
)
EMPTY_YAML_VALUES = {"", "''", '""', "[]", "{}", "null", "~"}
BLOCK_SCALAR_MARKERS = {">", ">-", ">+", "|", "|-", "|+"}


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def candidate_paths(argv: list[str]) -> list[str]:
    if argv:
        return argv

    base_sha = os.environ.get("BLOG_BASE_SHA")
    if base_sha:
        return git_lines("diff", "--name-only", "--diff-filter=ACMR", base_sha, "HEAD")

    staged = git_lines("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    if staged:
        return staged

    changed = git_lines("diff", "--name-only", "--diff-filter=ACMR")
    return changed


def parse_front_matter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "missing opening YAML front-matter delimiter"

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, "missing closing YAML front-matter delimiter"

    values: dict[str, str] = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line or line[0].isspace() or line.lstrip().startswith("#") or ":" not in line:
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

        values[key] = value
        i += 1

    return values, None


def has_value(value: str | None) -> bool:
    if value is None:
        return False
    normalized = value.strip()
    return normalized.lower() not in EMPTY_YAML_VALUES


def validate(path_str: str) -> list[str]:
    errors: list[str] = []
    is_post = path_str.startswith("_posts/")
    is_draft = path_str.startswith("_drafts/")
    if not (is_post or is_draft):
        return errors

    path = Path(path_str)
    if not path.exists():
        return errors

    if is_post and not POST_RE.match(path_str):
        errors.append("published post filename must be `_posts/YYYY-MM-DD-slug.md` or `.markdown`")
    if is_draft and not DRAFT_RE.match(path_str):
        errors.append("draft must be a Markdown file directly under `_drafts/` or its subdirectories")

    text = path.read_text(encoding="utf-8")
    front_matter, parse_error = parse_front_matter(text)
    if parse_error:
        errors.append(parse_error)
        return errors

    required = PUBLISHED_REQUIRED if is_post else DRAFT_REQUIRED
    missing = sorted(key for key in required if not has_value(front_matter.get(key)))
    if missing:
        errors.append("missing or empty required front matter: " + ", ".join(missing))

    if has_value(front_matter.get("layout")) and front_matter["layout"].strip("'\"") != "post":
        errors.append("`layout` must be `post`")

    if is_post:
        upper_text = text.upper()
        found = [token for token in PLACEHOLDERS if token in upper_text]
        if found:
            errors.append("published post contains draft placeholder(s): " + ", ".join(found))

    return errors


def main() -> int:
    paths = candidate_paths(sys.argv[1:])
    blog_paths = [p for p in paths if p.startswith(("_posts/", "_drafts/"))]

    if not blog_paths:
        print("No changed blog posts or drafts to validate.")
        return 0

    failures = 0
    for path in blog_paths:
        errors = validate(path)
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

    print(f"\nValidated {len(blog_paths)} changed blog file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
