# Editorial content contract

This document defines the durable metadata and taxonomy contract for new and substantially revised JLSunday articles. It is intentionally small enough to enforce in the publishing workflow while leaving older posts valid until they are deliberately modernized.

## Front matter

### Required for new posts

- `layout: post`
- `title`: human-readable article title.
- `date`: publication timestamp.
- `description`: one concise, standalone summary suitable for search/social metadata and article cards. Do not duplicate a second `summary` field with the same purpose.
- `categories`: one or more reader-facing categories from the taxonomy below.
- `tags`: focused discovery terms; prefer a small useful set over exhaustive keyword lists.

### Recommended when applicable

- `last_modified_at`: only when a published article receives a substantive factual or technical revision. Do not change it for typo-only edits.
- `image`: article-specific social/OG image for substantial articles when one exists.
- `featured: true`: editorial selection for prominent surfaces; not a proxy for recency.
- `include_TOC: true`: use for sufficiently long, structured articles where an on-page table of contents improves navigation.
- `series`: stable series identifier when an article is part of a deliberate multi-part series.
- `permalink`: use only when a deliberate stable URL differs from the site's normal post URL convention.

## Primary taxonomy

Categories are broad, reader-facing content areas. Prefer these names rather than creating framework-version or one-off categories:

- `AI & Software Engineering`
- `Software Architecture`
- `Python & Django`
- `C# & .NET`
- `Angular`
- `Building Software`

Use `DevOps & Cloud` or `Developer Tools` only when the body of content warrants a durable topic area rather than a single post.

Tags are narrower facets within those categories: technologies, techniques, products, concepts, or recurring themes. Examples include `agents`, `context-engineering`, `testing`, `jekyll`, `github-actions`, `sql`, and `accessibility`.

## Editorial rules

1. Choose categories for how a reader would browse the site, not merely for every technology mentioned.
2. Use the `description` as a truthful summary of the article, not a keyword list.
3. Keep titles descriptive and specific; do not manufacture SEO titles that misrepresent the article.
4. Preserve existing URLs when modernizing legacy content unless there is a strong reason to migrate them with redirects.
5. Add internal links where they materially help the reader understand a concept or continue into related first-party writing.
6. Automation may propose metadata, categories, tags, links, and images, but publication remains subject to human approval.

## Example

```yaml
---
layout: post
title: "Evidence-Gated Capability Adoption: What We Learned Modernizing JLSunday"
date: 2026-08-23 12:00:00 -0400
description: "A case study in using evidence gates to decide which software and UX capabilities to adopt, adapt, or reject during a real site modernization."
categories:
  - AI & Software Engineering
  - Building Software
tags:
  - agents
  - evidence-gated-adoption
  - jekyll
  - github-actions
featured: true
include_TOC: true
---
```

## Legacy content

Existing posts are not required to satisfy this contract immediately. Modernize them selectively based on value, traffic, relevance, or when they are otherwise being substantially revised. This avoids noisy bulk edits and preserves historical URLs/content until there is evidence that remediation is worthwhile.
