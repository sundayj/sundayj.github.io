#!/usr/bin/env python3

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import suggest_internal_links as links
from suggest_related_posts import PostMetadata


class InternalLinkSuggestionTests(unittest.TestCase):
    def test_build_suggestions_is_non_mutating_and_requires_human_approval(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target_path = Path(tmp) / "draft.md"
            original = "---\ntitle: Draft\ncategories: [AI]\ntags: [agents, architecture]\n---\nBody\n"
            target_path.write_text(original, encoding="utf-8")
            candidate = PostMetadata(
                path="_posts/2026-01-01-agent-architecture.md",
                title="Agent Architecture",
                categories=("ai",),
                tags=("agents", "architecture"),
                series=None,
                post_ref="2026-01-01-agent-architecture",
            )
            with patch("suggest_internal_links.load_published_posts", return_value=[candidate]):
                result = links.build_suggestions(target_path)

            self.assertFalse(result["mutates_content"])
            self.assertTrue(result["requires_human_approval"])
            self.assertEqual(original, target_path.read_text(encoding="utf-8"))
            self.assertEqual(1, len(result["outbound"]))
            self.assertEqual(1, len(result["inbound"]))
            self.assertIn("{% post_url 2026-01-01-agent-architecture %}", result["outbound"][0]["jekyll_ref"])

    def test_zero_candidates_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target_path = Path(tmp) / "draft.md"
            target_path.write_text("---\ntitle: Draft\ncategories: [AI]\ntags: [agents]\n---\nBody\n", encoding="utf-8")
            unrelated = PostMetadata(
                path="_posts/2022-01-01-pixel-art.md",
                title="Pixel Art",
                categories=("tools",),
                tags=("pixel-art",),
                series=None,
                post_ref="2022-01-01-pixel-art",
            )
            with patch("suggest_internal_links.load_published_posts", return_value=[unrelated]):
                result = links.build_suggestions(target_path)

            self.assertEqual([], result["outbound"])
            self.assertEqual([], result["inbound"])
            rendered = links.render_markdown(result)
            self.assertIn("No candidate cleared", rendered)
            self.assertIn("No Markdown was changed", rendered)


if __name__ == "__main__":
    unittest.main()
