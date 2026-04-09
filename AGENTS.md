# sundayj.github.io Instructions

Scope: applies to the `sundayj.github.io/` repository unless a deeper `AGENTS.md` overrides it.

## Purpose

This is the public website repository for `jlsunday.com`.

Use it for:

- public landing pages
- public product pages
- articles and posts
- longer-form explanations than the catalog repo should carry

## Stack

- Jekyll
- Liquid templates
- static assets
- JavaScript-based frontend behavior

## Content Boundary

- Keep internal planning, pricing strategy, and premium implementation details out of this repo.
- Use `AgentSkillsAndTools` for catalog metadata and teaser listings.
- Use `AgentSkillsHQ` for private planning and launch notes.

## Planning Reference

- For the current site improvement roadmap, publishing sequence, and suggested new post topics, consult `/home/jsunday/GitHub/AgentSkillsWorkspace/jlsunday-site-improvement-plan.md` before making broad structural or editorial changes.

## Working Rules

- Treat this repo as public.
- Prefer editing source files over generated `_site/` output.
- Keep third-party embeds and scripts explicit and reviewable.
- When adding product pages, prefer stable permalinks and concise front matter.

## Security Rules

- Do not commit secrets or tokens intended to stay private.
- Public identifiers such as analytics or publishable search keys are allowed only when they are meant to be public.
- Avoid introducing inline event handlers, unsafe HTML injection, or additional unpinned third-party scripts without a strong reason.
- If security-related behavior depends on headers or edge configuration, note that clearly because those settings may live outside the repo.

## Git Rules

- Do not push unless the user explicitly asks.
- Keep unrelated generated `_site/` churn out of commits unless the workflow genuinely requires it.
