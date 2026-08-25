#!/usr/bin/env python3
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from scripts import validate_blog_posts as validator


VALID_POST = """---
layout: post
title: "Evidence Gates for Blog Automation"
date: 2026-08-24 20:00:00 -0400
description: "A practical test of evidence-gated editorial automation that keeps publication under explicit human control."
categories:
  - AI & Software Engineering
  - Building Software
tags: [agents, testing, jekyll]
featured: false
---

## Why this matters

A useful article body with an [external source](https://example.edu/research).
"""


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.previous_cwd = os.getcwd()
        os.chdir(self.tempdir.name)
        Path("_posts").mkdir()
        Path("_drafts").mkdir()

    def tearDown(self) -> None:
        os.chdir(self.previous_cwd)
        self.tempdir.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = Path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_new_post_matching_current_contract_passes(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST)
        self.assertEqual([], validator.validate(path, status="A"))

    def test_new_post_rejects_duplicate_legacy_summary_fields(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST.replace("featured: false", "summary: duplicate\nfeatured: false"))
        errors = validator.validate(path, status="A")
        self.assertTrue(any("must not set `summary`" in error for error in errors))

    def test_new_post_rejects_body_h1(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST.replace("## Why this matters", "# Duplicate page title"))
        errors = validator.validate(path, status="A")
        self.assertTrue(any("uses an H1" in error for error in errors))

    def test_published_post_rejects_localhost_link(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST.replace("https://example.edu/research", "http://localhost:4000/preview"))
        errors = validator.validate(path, status="A")
        self.assertTrue(any("local-only URL" in error for error in errors))

    def test_featured_post_requires_image(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST.replace("featured: false", "featured: true"))
        errors = validator.validate(path, status="A")
        self.assertTrue(any("featured posts must provide" in error for error in errors))

    def test_modified_legacy_post_does_not_require_current_contract(self) -> None:
        path = "_posts/2021-01-02-Legacy-Title.markdown"
        self.write(
            path,
            """---
layout: post
title: Legacy Title
summary: Old card summary
category: Software Development
tags: [legacy]
---

## Existing section

A small correction to an old post.
""",
        )
        self.assertEqual([], validator.validate(path, status="M"))

    def test_current_categories_must_use_reader_taxonomy(self) -> None:
        path = "_posts/2026-08-24-evidence-gates-for-blog-automation.markdown"
        self.write(path, VALID_POST.replace("Building Software", "Random Framework Version"))
        errors = validator.validate(path, status="A")
        self.assertTrue(any("unknown reader-facing categories" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
