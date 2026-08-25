#!/usr/bin/env python3
"""Enforce reproducible DevSculptor consumption for JLSunday builds."""

from __future__ import annotations

import re
from pathlib import Path

CONFIG_PATH = Path("_config.yml")
GEMFILE_PATH = Path("Gemfile")
REMOTE_THEME_RE = re.compile(
    r"^remote_theme:\s*sundayj/DevSculptor@(?P<sha>[0-9a-f]{40})\s*$",
    re.MULTILINE,
)
DEVSculptor_GEM_RE = re.compile(
    r"^\s*gem\s+[\"']DevSculptor[\"'](?:\s*,.*)?$",
    re.MULTILINE,
)


def main() -> int:
    config = CONFIG_PATH.read_text(encoding="utf-8")
    gemfile = GEMFILE_PATH.read_text(encoding="utf-8")
    failures: list[str] = []

    match = REMOTE_THEME_RE.search(config)
    if not match:
        failures.append(
            "_config.yml must pin remote_theme to sundayj/DevSculptor@<40-character commit SHA>."
        )

    if DEVSculptor_GEM_RE.search(gemfile):
        failures.append(
            'Gemfile must not declare gem "DevSculptor"; the site consumes the theme only through jekyll-remote-theme.'
        )

    if 'gem "jekyll-remote-theme"' not in gemfile and "gem 'jekyll-remote-theme'" not in gemfile:
        failures.append("Gemfile must include jekyll-remote-theme.")

    if "jekyll-remote-theme" not in config:
        failures.append("_config.yml plugins must include jekyll-remote-theme.")

    if failures:
        print("Theme distribution validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated immutable DevSculptor theme pin: {match.group('sha')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
