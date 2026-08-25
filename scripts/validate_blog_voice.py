#!/usr/bin/env python3
"""Validate mechanical JLSunday voice rules for changed drafts/current posts.

Subjective voice review remains a human/agent editorial pass. This script only enforces
rules that are safe to make mechanical. At present, that means Justin's explicit rule
that authored blog prose does not use em dashes.
"""

from __future__ import annotations

import sys
from pathlib import Path

import validate_blog_posts as publication

EM_DASH = "—"


def validate(path_str: str, status: str = "M") -> list[str]:
    path = Path(path_str)
    if not path.exists() or not path_str.startswith(("_drafts/", "_posts/")):
        return []

    text = path.read_text(encoding="utf-8")
    front_matter, body, parse_error = publication.parse_front_matter(text)
    if parse_error:
        return []  # The publication validator owns YAML/front-matter errors.

    is_draft = path_str.startswith("_drafts/")
    current_post = path_str.startswith("_posts/") and (
        status == "A" or "categories" in front_matter
    )
    if not (is_draft or current_post):
        return []

    errors: list[str] = []

    for field in ("title", "description"):
        value = str(front_matter.get(field, ""))
        if EM_DASH in value:
            errors.append(
                f"`{field}` contains an em dash; rewrite it because JLSunday authored prose does not use em dashes"
            )

    visible_lines = publication.visible_body_lines(body)
    for line_no, line in enumerate(visible_lines, start=1):
        if EM_DASH in line:
            errors.append(
                f"body line {line_no} contains an em dash; rewrite the sentence with other punctuation or structure"
            )

    return errors


def main() -> int:
    entries = publication.candidate_entries(sys.argv[1:])
    blog_entries = [
        (status, path)
        for status, path in entries
        if path.startswith(("_posts/", "_drafts/"))
    ]

    if not blog_entries:
        print("No changed blog posts or drafts to voice-check.")
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
        print(f"\n{failures} blog file(s) failed mechanical voice validation.", file=sys.stderr)
        return 1

    print(f"\nVoice-checked {len(blog_entries)} changed blog file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
