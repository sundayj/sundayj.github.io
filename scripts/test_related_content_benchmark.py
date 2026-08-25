#!/usr/bin/env python3
"""Human-judgment benchmark for JE-003's current six-post corpus."""

from __future__ import annotations

import unittest

import benchmark_related_posts as benchmark

# These expectations are deliberately conservative. A missing recommendation is
# preferable to a superficially similar false positive in this small corpus.
EXPECTED_RELATED = {
    "5 Great Free Software Development Tools": ["40 Awesome Programming Resources"],
    "40 Awesome Programming Resources": ["5 Great Free Software Development Tools"],
    "Site Updates": [],
    "Building an App with Angular, Part 1: Introduction": [],
    "Comparing Pixel Art Editors": [],
    "Your Parser Shouldn't Get One Shot": [],
}


class RelatedContentBenchmarkTests(unittest.TestCase):
    def test_current_corpus_matches_human_relevance_judgments(self) -> None:
        posts = benchmark.load_posts()
        self.assertEqual(set(EXPECTED_RELATED), {post.title for post in posts})

        actual = {
            post.title: [item["title"] for item in benchmark.recommendations(post, posts)]
            for post in posts
        }
        self.assertEqual(EXPECTED_RELATED, actual)

    def test_score_is_symmetric_and_explainable(self) -> None:
        posts = benchmark.load_posts()
        by_title = {post.title: post for post in posts}
        left = by_title["5 Great Free Software Development Tools"]
        right = by_title["40 Awesome Programming Resources"]

        forward = benchmark.score_pair(left, right)
        reverse = benchmark.score_pair(right, left)
        self.assertEqual(forward, reverse)
        self.assertGreaterEqual(forward["score"], benchmark.MIN_SCORE)
        self.assertIn("tools", forward["shared_tags"])
        self.assertGreater(len(forward["shared_tags"]), 1)

    def test_generic_tools_overlap_does_not_force_pixel_art_recommendation(self) -> None:
        posts = benchmark.load_posts()
        by_title = {post.title: post for post in posts}
        dev_tools = by_title["5 Great Free Software Development Tools"]
        pixel_art = by_title["Comparing Pixel Art Editors"]

        evidence = benchmark.score_pair(dev_tools, pixel_art)
        self.assertLess(evidence["score"], benchmark.MIN_SCORE)


if __name__ == "__main__":
    unittest.main()
