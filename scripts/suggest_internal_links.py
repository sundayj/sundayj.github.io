#!/usr/bin/env python3
"""Suggest outbound and inbound internal-link candidates for one editorial target.

This is review infrastructure, not an editor. It never writes Markdown and is
allowed to return zero suggestions. Publication remains a separate human action.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from suggest_related_posts import DEFAULT_LIMIT, DEFAULT_THRESHOLD, load_published_posts, read_metadata, suggest


def build_suggestions(target_path: Path, *, threshold: int = DEFAULT_THRESHOLD, limit: int = DEFAULT_LIMIT) -> dict[str, object]:
    target = read_metadata(target_path)
    candidates = suggest(target, load_published_posts(), threshold=threshold, limit=limit)

    outbound = []
    inbound = []
    for item in candidates:
        evidence = {
            "score": item["score"],
            "shared_categories": item["shared_categories"],
            "shared_tags": item["shared_tags"],
            "same_series": item["same_series"],
            "components": item["components"],
        }
        outbound.append(
            {
                "title": item["title"],
                "source_path": item["path"],
                "jekyll_ref": "{% post_url " + str(item["post_ref"]) + " %}" if item["post_ref"] else None,
                "evidence": evidence,
            }
        )
        inbound.append(
            {
                "title": item["title"],
                "source_path": item["path"],
                "suggestion": "Consider whether this published article should link to the new article after publication.",
                "evidence": evidence,
            }
        )

    return {
        "target": {"path": target.path, "title": target.title},
        "threshold": threshold,
        "limit": limit,
        "mutates_content": False,
        "requires_human_approval": True,
        "outbound": outbound,
        "inbound": inbound,
    }


def render_markdown(result: dict[str, object]) -> str:
    target = result["target"]
    assert isinstance(target, dict)
    lines = [
        "## Editorial internal-link suggestions",
        "",
        f"Target: **{target['title']}** (`{target['path']}`)",
        "",
        "> Suggestions only. No Markdown was changed. A human must approve any link edit or publication action.",
        "",
        "### Outbound candidates",
    ]
    outbound = result["outbound"]
    assert isinstance(outbound, list)
    if not outbound:
        lines.append("- No candidate cleared the relevance threshold.")
    else:
        for item in outbound:
            assert isinstance(item, dict)
            evidence = item["evidence"]
            assert isinstance(evidence, dict)
            lines.append(f"- **{item['title']}** — score {evidence['score']}")
            if item.get("jekyll_ref"):
                lines.append(f"  - Suggested ref: `{item['jekyll_ref']}`")
            lines.append(f"  - Evidence: categories={evidence['shared_categories']}; tags={evidence['shared_tags']}; same_series={evidence['same_series']}")

    lines.extend(["", "### Inbound candidates"])
    inbound = result["inbound"]
    assert isinstance(inbound, list)
    if not inbound:
        lines.append("- No candidate cleared the relevance threshold.")
    else:
        for item in inbound:
            assert isinstance(item, dict)
            evidence = item["evidence"]
            assert isinstance(evidence, dict)
            lines.append(f"- **{item['title']}** — score {evidence['score']}")
            lines.append("  - Review later for a contextually appropriate backlink after the target has an approved publish URL.")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Path to one _drafts/ or _posts/ Markdown file")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_path = Path(args.target)
    if not target_path.is_file():
        raise SystemExit(f"Target does not exist: {target_path}")
    if args.threshold < 0 or args.limit < 1:
        raise SystemExit("--threshold must be >= 0 and --limit must be >= 1")

    result = build_suggestions(target_path, threshold=args.threshold, limit=args.limit)
    print(json.dumps(result, indent=2, sort_keys=True) if args.as_json else render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
