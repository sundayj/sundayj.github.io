#!/usr/bin/env python3
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

import validate_blog_voice as voice


DRAFT = """---
layout: post
title: "Software Engineering After Coding Agents"
description: "A concrete argument about what becomes valuable when implementation gets cheaper."
categories: ["AI & Software Engineering"]
tags: [AI, agents]
---

## The actual shift

Implementation is cheaper. Accountability is not.
"""


class VoiceValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.previous_cwd = os.getcwd()
        os.chdir(self.tempdir.name)
        Path("_drafts").mkdir()
        Path("_posts").mkdir()

    def tearDown(self) -> None:
        os.chdir(self.previous_cwd)
        self.tempdir.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = Path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_draft_without_em_dash_passes(self) -> None:
        path = "_drafts/software-engineering-after-coding-agents.md"
        self.write(path, DRAFT)
        self.assertEqual([], voice.validate(path, status="A"))

    def test_draft_rejects_em_dash_in_body(self) -> None:
        path = "_drafts/software-engineering-after-coding-agents.md"
        self.write(path, DRAFT.replace("Implementation is cheaper. Accountability is not.", "Implementation is cheaper—accountability is not."))
        errors = voice.validate(path, status="A")
        self.assertTrue(any("body line" in error and "em dash" in error for error in errors))

    def test_draft_rejects_em_dash_in_description(self) -> None:
        path = "_drafts/software-engineering-after-coding-agents.md"
        self.write(path, DRAFT.replace("A concrete argument about", "A concrete argument—about"))
        errors = voice.validate(path, status="A")
        self.assertTrue(any("`description`" in error for error in errors))

    def test_em_dash_inside_fenced_code_is_ignored(self) -> None:
        path = "_drafts/software-engineering-after-coding-agents.md"
        self.write(path, DRAFT + "\n```text\nexample—literal\n```\n")
        self.assertEqual([], voice.validate(path, status="A"))

    def test_modified_legacy_post_is_not_retroactively_enforced(self) -> None:
        path = "_posts/2021-01-01-Legacy-Post.markdown"
        self.write(
            path,
            """---
layout: post
title: Legacy Post
category: Software Development
---

Old prose—with historical punctuation.
""",
        )
        self.assertEqual([], voice.validate(path, status="M"))


if __name__ == "__main__":
    unittest.main()
