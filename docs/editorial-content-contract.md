# Editorial content contract

This document is the authoritative metadata and publication contract for new JLSunday articles and legacy articles that are deliberately modernized to the current schema. `scripts/validate_blog_posts.py`, the editorial workflow, and the publication PR checklist should agree with this document.

Untouched or lightly edited legacy posts remain valid until they are deliberately modernized. The validator does not infer whether a prose edit is “substantial”; adding the current plural `categories` field opts an existing post into the current contract.

## Front matter

### Required for new/current-contract posts

- `layout: post`
- `title`: human-readable article title.
- `date`: publication timestamp.
- `description`: one concise, standalone summary suitable for search/social metadata and article cards. Keep it roughly 40–220 characters.
- `categories`: one or more reader-facing categories from the taxonomy below.
- `tags`: focused discovery terms; prefer a small useful set over exhaustive keyword lists.

### Do not duplicate these legacy fields in current-contract posts

- `summary`: `description` is now the single summary field. DevSculptor uses `description` for current cards and keeps `summary` only as a legacy fallback.
- `excerpt`: let Jekyll derive excerpts unless a future editorial requirement explicitly justifies an override.
- `canonical_url`: `jekyll-seo-tag` derives canonical URLs from the generated post URL.
- singular `category`: use plural `categories`.

The site-level author configuration supplies the default author identity; a post-specific `author` is only needed if a future article genuinely has a different author.

### Recommended when applicable

- `last_modified_at`: only when a published article receives a substantive factual or technical revision. Do not change it for typo-only edits.
- `image`: article-specific social/OG image for substantial articles when one exists. Use HTTPS or a root-relative path under `/assets/`. A `featured: true` post must provide an image.
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

`DevOps & Cloud` and `Developer Tools` are also accepted when the body of content warrants a durable topic area rather than a one-off mention.

Tags are narrower facets within those categories: technologies, techniques, products, concepts, or recurring themes. Examples include `agents`, `context-engineering`, `testing`, `jekyll`, `github-actions`, `sql`, and `accessibility`. Keep the list focused; current validation caps it at 10.

## Content and link conventions

1. New published filenames use `_posts/YYYY-MM-DD-kebab-case-slug.md` or `.markdown`. Existing legacy filenames are preserved during minor edits so historical URLs do not churn.
2. The post layout renders the page H1 from `title`; article-body Markdown headings therefore start at H2.
3. Published content must not contain `TODO`, `TBD`, `SOURCE NEEDED`, `CITATION NEEDED`, or `FIXME` markers.
4. Do not publish `localhost`, loopback, `file:`, `javascript:`, or placeholder example-domain links.
5. CI builds the site and validates internal links/assets rendered inside changed post article bodies. External sites are not network-probed during CI because availability checks would be flaky; source/fact review remains responsible for external-link quality.
6. New local post images referenced through front matter must resolve under `/assets/`.

## Editorial rules

1. Choose categories for how a reader would browse the site, not merely for every technology mentioned.
2. Use `description` as a truthful summary of the article, not a keyword list.
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
image: /assets/images/posts/evidence-gated-capability-adoption.png
include_TOC: true
---
```

## Validation

For a publication branch:

```bash
python3 scripts/test_validate_blog_posts.py
python3 scripts/validate_blog_posts.py
bundle exec jekyll build --trace
```

CI additionally runs `scripts/validate_generated_post_links.py` for changed published posts after the Jekyll build.

## Legacy content

Existing posts are not required to satisfy this contract immediately. Minor fixes keep their historical front matter and filenames valid. When intentionally modernizing an older article, migrate it to `description`, plural `categories`, and the current rules above; the presence of `categories` opts the post into strict current-contract validation.
