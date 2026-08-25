#!/usr/bin/env python3
from __future__ import annotations

import os
import struct
import tempfile
import unittest
from pathlib import Path

import validate_generated_seo as validator


VALID_HTML = """<!doctype html>
<html>
<head>
<!-- Begin Jekyll SEO tag v2.8.0 -->
<link rel="canonical" href="https://jlsunday.com/posts/example.html">
<meta name="description" content="Example description for a generated blog post.">
<meta property="og:title" content="Example post">
<meta property="og:description" content="Example description for a generated blog post.">
<meta property="og:url" content="https://jlsunday.com/posts/example.html">
<meta property="og:image" content="https://jlsunday.com/assets/images/posts/example.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:description" content="Example description for a generated blog post.">
<!-- End Jekyll SEO tag -->
</head>
<body></body>
</html>
"""

EXPLICIT_TWITTER_TAGS = """<meta name="twitter:title" content="Example post">
<meta name="twitter:image" content="https://jlsunday.com/assets/images/posts/example.png">
"""


def png_bytes(width: int, height: int) -> bytes:
    return (
        b"\x89PNG\r\n\x1a\n"
        + struct.pack(">I", 13)
        + b"IHDR"
        + struct.pack(">II", width, height)
        + b"\x08\x06\x00\x00\x00"
    )


class GeneratedSeoValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.previous_cwd = os.getcwd()
        os.chdir(self.tempdir.name)
        self.site_dir = Path("_site")
        (self.site_dir / "assets/images/posts").mkdir(parents=True)

    def tearDown(self) -> None:
        os.chdir(self.previous_cwd)
        self.tempdir.cleanup()

    def write_image(self, relative: str, content: bytes) -> Path:
        path = self.site_dir / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def validate_contract(self, html: str) -> list[str]:
        errors, _ = validator.validate_html(
            Path("example.html"),
            html,
            require_social_card_contract=True,
        )
        return errors

    def test_open_graph_fallback_is_valid_for_x_card(self) -> None:
        self.assertEqual([], self.validate_contract(VALID_HTML))

    def test_explicit_twitter_title_and_image_are_valid(self) -> None:
        html = VALID_HTML.replace(
            '<meta name="twitter:description"',
            EXPLICIT_TWITTER_TAGS + '<meta name="twitter:description"',
        )
        self.assertEqual([], self.validate_contract(html))

    def test_twitter_card_must_be_large_image(self) -> None:
        errors = self.validate_contract(VALID_HTML.replace("summary_large_image", "summary"))
        self.assertTrue(any("twitter:card must be `summary_large_image`" in error for error in errors))

    def test_explicit_twitter_image_must_match_open_graph_image(self) -> None:
        explicit = EXPLICIT_TWITTER_TAGS.replace(
            "https://jlsunday.com/assets/images/posts/example.png",
            "https://jlsunday.com/assets/images/posts/other.png",
        )
        html = VALID_HTML.replace(
            '<meta name="twitter:description"',
            explicit + '<meta name="twitter:description"',
        )
        errors = self.validate_contract(html)
        self.assertTrue(any("twitter:image must match og:image" in error for error in errors))

    def test_social_image_url_must_be_absolute_https(self) -> None:
        html = VALID_HTML.replace(
            "https://jlsunday.com/assets/images/posts/example.png",
            "/assets/images/posts/example.png",
        )
        errors = self.validate_contract(html)
        self.assertTrue(any("og:image must be an absolute HTTPS URL" in error for error in errors))

    def test_built_social_image_must_exist(self) -> None:
        errors = validator.validate_social_image(
            self.site_dir,
            "https://jlsunday.com/assets/images/posts/missing.png",
        )
        self.assertTrue(any("does not exist in built site" in error for error in errors))

    def test_built_social_image_rejects_small_dimensions(self) -> None:
        self.write_image("assets/images/posts/example.png", png_bytes(200, 100))
        errors = validator.validate_social_image(
            self.site_dir,
            "https://jlsunday.com/assets/images/posts/example.png",
        )
        self.assertTrue(any("too small for a large preview" in error for error in errors))

    def test_built_social_image_accepts_reasonable_png(self) -> None:
        self.write_image("assets/images/posts/example.png", png_bytes(1536, 1024))
        errors = validator.validate_social_image(
            self.site_dir,
            "https://jlsunday.com/assets/images/posts/example.png",
        )
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
