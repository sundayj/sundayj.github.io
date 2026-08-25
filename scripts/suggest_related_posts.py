#!/usr/bin/env python3
"""Suggest high-confidence related published posts for one editorial target.

The scorer implements the adapted JE-003 decision: it is conservative,
explainable, deterministic, and allowed to return zero candidates. It does not
edit content and does not publish anything.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from validate_blog_posts import as_list, parse_front_matter

POSTS_DIR = Path("_posts")
CATEGORY_WEIGHT = 3
TAG_WEIGHT = 2
SERIES_WEIGHT = 8
DEFAULT_THRESHOLD = 6
DEFAULT_LIMIT = 3


@dataclass(frozen=True)
class PostMetadata:
    path: str
    title: str
    categories: tuple[str, ...]
    tags: tuple[str, ...]
    series: str | None
    post_ref: str | None


def normalize(value: str) -> str:
    return " ".join(value.strip().lower().replace("_", "-").split())


def read_metadata(path: Path) -> PostMetadata:
    front_matter, _, error = parse_front_matter(path.read_text(encoding="utf-8"))
    if error:
        raise ValueError(f"{path}: {error}")

    categories = as_list(front_matter.get("categories"))
    if not categories:
        categories = as_list(front_matter.get("category"))

    is_post = path.parent.name == "_posts"
    return PostMetadata(
        path=path.as_posix(),
        title=str(front_matter.get("title", path.stem)).strip(),
        categories=tuple(sorted({normalize(item) for item in categories if item.strip()})),
        tags=tuple(sorted({normalize(item) for item in as_list(front_matter.get("tags")) if item.strip()})),
        series=(normalize(str(front_matter["series"])) if front_matter.get("series") else None),
        post_ref=path.stem if is_post else None,
    )


def load_published_posts(posts_dir: Path = POSTS_DIR) -> list[PostMetadata]:
    paths = sorted(posts_dir.glob("*.md")) + sorted(posts_dir.glob("*.markdown"))
    return [read_metadata(path) for path in paths]


def score_pair(source: PostMetadata, candidate: PostMetadata) -> dict[str, object]:
    shared_categories = sorted(set(source.categories) & set(candidate.categories))
    shared_tags = sorted(set(source.tags) & set(candidate.tags))
    same_series = bool(source.series and source.series == candidate.series)

    category_score = len(shared_categories) * CATEGORY_WEIGHT
    tag_score = len(shared_tags) * TAG_WEIGHT
    series_score = SERIES_WEIGHT if same_series else 0

    return {
        "score": category_score + tag_score + series_score,
        "shared_categories": shared_categories,
        "shared_tags": shared_tags,
        "same_series": same_series,
        "components": {
            "category": category_score,
            "tags": tag_score,
            "series": series_score,
        },
    }


def suggest(
    target: PostMetadata,
    candidates: list[PostMetadata],
    *,
    threshold: int = DEFAULT_THRESHOLD,
    limit: int = DEFAULT_LIMIT,
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for candidate in candidates:
        if candidate.path == target.path:
            continue
        evidence = score_pair(target, candidate)
        if int(evidence["score"]) < threshold:
            continue
        results.append(
            {
                "path": candidate.path,
                "title": candidate.title,
                "post_ref": candidate.post_ref,
                **evidence,
            }
        )

    results.sort(key=lambda item: (-int(item["score"]), str(item["title"]).lower(), str(item["path"])))
    return results[:limit]


def render_text(target: PostMetadata, results: list[dict[str, object]], threshold: int) -> str:
    lines = [f"Related-content candidates for: {target.title}", f"threshold={threshold}", ""]
    if not results:
        lines.append("No candidate cleared the relevance threshold.")
        return "\n".join(lines)

    for item in results:
        reasons: list[str] = []
        if item["shared_categories"]:
            reasons.append("categories=" + ", ".join(item["shared_categories"]))
        if item["shared_tags"]:
            reasons.append("tags=" + ", ".join(item["shared_tags"]))
        if item["same_series"]:
            reasons.append("same-series")
        lines.append(f"- {item['title']} (score {item['score']})")
        lines.append(f"  source: {item['path']}")
        if item["post_ref"]:
            lines.append("  Jekyll ref: {% post_url " + str(item["post_ref"]) + " %}")
        lines.append("  evidence: " + ("; ".join(reasons) if reasons else "none"))
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

    target = read_metadata(target_path)
    results = suggest(target, load_published_posts(), threshold=args.threshold, limit=args.limit)
    if args.as_json:
        print(
            json.dumps(
                {
                    "target": {"path": target.path, "title": target.title},
                    "threshold": args.threshold,
                    "limit": args.limit,
                    "candidates": results,
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print(render_text(target, results, args.threshold))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
