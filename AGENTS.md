# JLSunday Blog Agent Guide

This repository is both the source for jlsunday.com and the editorial system for the blog.

## Non-negotiable publication rule

- Never publish a new blog post directly to `master`.
- Never merge a blog-post pull request on the author's behalf unless the author explicitly asks for that specific merge.
- Human editorial approval is required before a post becomes public.
- Work on posts in `_drafts/` first. Move a post to `_posts/` only after the author says it is ready for publication.
- Publication is complete only when the author approves and merges the PR to `master`.

## Repository map

- `_drafts/`: unpublished working drafts.
- `_posts/`: publication-ready or published Jekyll posts.
- `assets/images/posts/`: post imagery and diagrams.
- `.github/blog/editorial-workflow.md`: canonical editorial lifecycle and agent responsibilities.
- `.github/blog/voice-guide.md`: writing voice and style constraints.
- `.github/ISSUE_TEMPLATE/blog-post.yml`: structured intake form for post ideas.
- `.github/pull_request_template.md`: review gate and publication checklist.
- `scripts/validate_blog_posts.py`: mechanical publication checks.
- `.githooks/pre-commit`: optional fast local validation hook.

## Editorial workflow

1. Start from a GitHub issue or an explicit author request.
2. Clarify the thesis, intended reader, why the post matters now, and what evidence could change the conclusion.
3. Research current, credible sources. Prefer primary sources and distinguish evidence from opinion.
4. Research the strongest counterarguments rather than only supporting the initial thesis.
5. Record research and important decisions in the issue when an issue exists.
6. Draft into `_drafts/<slug>.markdown` using existing Jekyll conventions.
7. Run a factual/technical critique, an argument critique, and a voice edit as separate passes.
8. Present uncertain claims, major editorial choices, and unresolved counterarguments to the author.
9. Revise until the author explicitly approves publication.
10. Move the draft to `_posts/YYYY-MM-DD-<slug>.markdown`, complete publication metadata, run validation/build checks, and open a PR to `master`.
11. Stop at the PR. The author owns the final merge decision.

## Research rules

- For fast-moving topics, verify current facts and dates before drafting.
- Prefer original documentation, papers, filings, source code, official statistics, and direct statements over summaries.
- Preserve source URLs or citations in the working issue/draft as appropriate.
- Do not convert uncertain claims into confident prose.
- Identify contrary evidence and edge cases.
- Do not use a source merely because it supports the preferred argument.

## Writing rules

- Read `.github/blog/voice-guide.md` before drafting or materially rewriting a post.
- Preserve the author's substantive position. Do not manufacture stronger opinions than the evidence or author supports.
- Avoid generic AI prose, canned transitions, repetitive conclusions, excessive sectioning, and empty rhetorical flourishes.
- Prefer concrete examples, technical specificity, and explicit tradeoffs.
- Explain jargon when the likely reader may not know it.
- Keep factual editing separate from voice editing; a voice pass must not introduce new factual claims.

## Jekyll conventions

- Use `layout: post`.
- Follow the front-matter patterns in existing `_posts/` files.
- Use descriptive alt text for new images.
- Use `rel="noopener noreferrer"` on new `target="_blank"` links.
- Do not add agent/editorial documentation to site navigation.
- `AGENTS.md`, `.github/`, `.githooks/`, and `scripts/` are repository-only and are explicitly excluded by `_config.yml`.

## Validation

Before declaring a publication PR ready:

- Run `python3 scripts/validate_blog_posts.py`.
- Run `bundle exec jekyll build` when the Ruby environment is available.
- Confirm repository-only files are absent from `_site/` after a build.
- Confirm no draft placeholders such as `TODO`, `TBD`, or `SOURCE NEEDED` remain in a file being moved into `_posts/`.
- Confirm the PR checklist is complete except for the final human approval checkbox.
