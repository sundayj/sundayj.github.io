#!/usr/bin/env python3
"""Regression tests for generated-site link and image integrity validation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import validate_generated_post_links as validator


class GeneratedSiteIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.site = Path(self.temp_dir.name) / "_site"
        self.site.mkdir()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, relative: str, content: str = "") -> Path:
        path = self.site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_internal_links_images_and_fragments_pass(self) -> None:
        self.write("assets/hero.png", "not-real-image-bytes")
        self.write(
            "about/index.html",
            '<html><body><h1 id="team">Team</h1></body></html>',
        )
        self.write(
            "index.html",
            '<html><body>'
            '<a href="/about/#team">About</a>'
            '<img src="/assets/hero.png" alt="Hero">'
            '</body></html>',
        )

        self.assertEqual({}, validator.validate_site(self.site))

    def test_missing_image_is_reported(self) -> None:
        page = self.write(
            "index.html",
            '<html><body><img src="/assets/missing.png" alt="Missing"></body></html>',
        )

        failures = validator.validate_site(self.site)

        self.assertIn(page, failures)
        self.assertTrue(any("/assets/missing.png" in error for error in failures[page]))

    def test_missing_internal_page_is_reported(self) -> None:
        page = self.write(
            "index.html",
            '<html><body><a href="/does-not-exist/">Missing</a></body></html>',
        )

        failures = validator.validate_site(self.site)

        self.assertIn(page, failures)
        self.assertTrue(any("/does-not-exist/" in error for error in failures[page]))

    def test_missing_fragment_is_reported(self) -> None:
        page = self.write(
            "index.html",
            '<html><body><a href="/about/#missing">Broken fragment</a></body></html>',
        )
        self.write(
            "about/index.html",
            '<html><body><h1 id="team">Team</h1></body></html>',
        )

        failures = validator.validate_site(self.site)

        self.assertIn(page, failures)
        self.assertTrue(any("#missing" in error for error in failures[page]))

    def test_external_and_non_http_targets_are_out_of_scope(self) -> None:
        self.write(
            "index.html",
            '<html><body>'
            '<a href="https://example.com/no-check">External</a>'
            '<a href="mailto:test@example.com">Email</a>'
            '<a href="javascript:void(0)">JS</a>'
            '<img src="data:image/png;base64,AAAA" alt="Inline">'
            '</body></html>',
        )

        self.assertEqual({}, validator.validate_site(self.site))


if __name__ == "__main__":
    unittest.main()
