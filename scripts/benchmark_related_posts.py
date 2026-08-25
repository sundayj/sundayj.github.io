#!/usr/bin/env python3
"""Benchmark deterministic related-post scoring over the published JLSunday corpus.

This is an evidence harness, not a production recommendation engine. It intentionally
allows zero recommendations when no candidate clears the relevance threshold.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

from validate_blog_posts import as_list, parse_front_matter

POSTS_DIR = Path("_posts")
CATEGORY_WEIGHT = 3
TAG_WEIGHT = 2
SERIES_WEIGHT = 8
MIN_SCORE = 6
MAX_RESULTS = 3


@dataclass(frozen=True)
class Post:
    path: str
    title: str
    categories: tuple[str, ...]
    tags: tuple[str, ...]
    series: str | None


def normalize(value: str) -> str:
    return " ".join(value.strip().lower().replace("_", "-").split())


def load_posts() -> list[Post]:
    posts: list[Post] = []
    for path in sorted(POSTS_DIR.glob("*.md")) + sorted(POSTS_DIR.glob("*.markdown")):
        front_matter, _, error = parse_front_matter(path.read_text(encoding="utf-8"))
        if error:
            raise ValueError(f"{path}: {error}")

        categories = as_list(front_matter.get("categories"))
        if not categories:
            categories = as_list(front_matter.get("category"))

        posts.append(
            Post(
                path=path.as_posix(),
                title=str(front_matter.get("title", path.stem)).strip(),
                categories=tuple(sorted({normalize(item) for item in categories if item.strip()})),
                tags=tuple(sorted({normalize(item) for item in as_list(front_matter.get("tags")) if item.strip()})),
                series=(normalize(str(front_matter["series"])) if front_matter.get("series") else None),
            )
        )
    return posts


def score_pair(source: Post, candidate: Post) -> dict[str, object]:
    shared_categories = sorted(set(source.categories) & set(candidate.categories))
    shared_tags = sorted(set(source.tags) & set(candidate.tags))
    same_series = bool(source.series and source.series == candidate.series)

    category_score = len(shared_categories) * CATEGORY_WEIGHT
    tag_score = len(shared_tags) * TAG_WEIGHT
    series_score = SERIES_WEIGHT if same_series else 0
    score = category_score + tag_score + series_score

    return {
        "score": score,
        "shared_categories": shared_categories,
        "shared_tags": shared_tags,
        "same_series": same_series,
        "components": {
            "category": category_score,
            "tags": tag_score,
            "series": series_score,
        },
    }


def recommendations(source: Post, posts: list[Post]) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for candidate in posts:
        if candidate.path == source.path:
            continue
        evidence = score_pair(source, candidate)
        if int(evidence["score"]) < MIN_SCORE:
            continue
        candidates.append(
            {
                "path": candidate.path,
                "title": candidate.title,
                **evidence,
            }
        )

    candidates.sort(key=lambda item: (-int(item["score"]), str(item["title"]).lower(), str(item["path"])))
    return candidates[:MAX_RESULTS]


def build_report(posts: list[Post]) -> dict[str, object]:
    return {
        "weights": {
            "shared_category": CATEGORY_WEIGHT,
            "shared_tag": TAG_WEIGHT,
            "same_series": SERIES_WEIGHT,
            "minimum_score": MIN_SCORE,
            "max_results": MAX_RESULTS,
        },
        "corpus_size": len(posts),
        "posts": [
            {
                "path": post.path,
                "title": post.title,
                "categories": list(post.categories),
                "tags": list(post.tags),
                "series": post.series,
                "recommendations": recommendations(post, posts),
            }
            for post in posts
        ],
    }


def render_text(report: dict[str, object]) -> str:
    lines = [
        f"JE-003 related-content benchmark: {report['corpus_size']} published posts",
        f"threshold={report['weights']['minimum_score']} max_results={report['weights']['max_results']}",
        "",
    ]
    for post in report["posts"]:
        lines.append(f"{post['title']} [{post['path']}]")
        recs = post["recommendations"]
        if not recs:
            lines.append("  -> no recommendation above threshold")
        for rec in recs:
            reasons: list[str] = []
            if rec["shared_categories"]:
                reasons.append("categories=" + ", ".join(rec["shared_categories"]))
            if rec["shared_tags"]:
                reasons.append("tags=" + ", ".join(rec["shared_tags"]))
            if rec["same_series"]:
                reasons.append("same-series")
            lines.append(f"  -> {rec['title']} score={rec['score']} ({'; '.join(reasons)})")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> int:
    posts = load_posts()
    if not posts:
        print("No published posts found.", file=sys.stderr)
        return 2

    report = build_report(posts)
    if "--json" in sys.argv:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
