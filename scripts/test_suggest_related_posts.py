#!/usr/bin/env python3
from __future__ import annotations

import unittest

import suggest_related_posts as related


def post(
    title: str,
    *,
    path: str,
    categories: tuple[str, ...] = (),
    tags: tuple[str, ...] = (),
    series: str | None = None,
) -> related.PostMetadata:
    return related.PostMetadata(
        path=path,
        title=title,
        categories=categories,
        tags=tags,
        series=series,
        post_ref=path.rsplit("/", 1)[-1].rsplit(".", 1)[0] if path.startswith("_posts/") else None,
    )


class RelatedCandidateTests(unittest.TestCase):
    def test_clear_metadata_overlap_crosses_threshold(self) -> None:
        source = post(
            "Development Tools",
            path="_drafts/dev-tools.markdown",
            tags=("database", "list", "software", "sql", "tools"),
        )
        candidate = post(
            "Programming Resources",
            path="_posts/2021-12-14-programming-resources.markdown",
            tags=("database", "list", "software", "sql", "tools"),
        )

        results = related.suggest(source, [candidate])
        self.assertEqual(1, len(results))
        self.assertEqual(10, results[0]["score"])
        self.assertEqual("2021-12-14-programming-resources", results[0]["post_ref"])

    def test_superficial_tools_overlap_can_return_zero(self) -> None:
        source = post(
            "Development Tools",
            path="_drafts/dev-tools.markdown",
            categories=("tools",),
            tags=("tools",),
        )
        candidate = post(
            "Pixel Art Editors",
            path="_posts/2022-06-11-pixel-art.markdown",
            categories=("tools",),
            tags=("tools",),
        )

        evidence = related.score_pair(source, candidate)
        self.assertEqual(5, evidence["score"])
        self.assertEqual([], related.suggest(source, [candidate]))

    def test_same_series_is_strong_explicit_signal(self) -> None:
        source = post("Part 2", path="_drafts/part-2.markdown", series="angular-app")
        candidate = post(
            "Part 1",
            path="_posts/2022-01-09-part-1.markdown",
            series="angular-app",
        )

        results = related.suggest(source, [candidate])
        self.assertEqual(8, results[0]["score"])
        self.assertTrue(results[0]["same_series"])

    def test_current_post_is_excluded_and_limit_is_deterministic(self) -> None:
        source = post("Target", path="_posts/2026-08-24-target.markdown", tags=("ai", "agents", "testing"))
        same = source
        beta = post("Beta", path="_posts/2026-01-02-beta.markdown", tags=("ai", "agents", "testing"))
        alpha = post("Alpha", path="_posts/2026-01-01-alpha.markdown", tags=("ai", "agents", "testing"))

        results = related.suggest(source, [same, beta, alpha], limit=1)
        self.assertEqual(["Alpha"], [item["title"] for item in results])


if __name__ == "__main__":
    unittest.main()
