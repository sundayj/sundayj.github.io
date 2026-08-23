# Editorial Workflow

This file is the durable workflow for producing JLSunday blog posts with AI assistance while preserving human editorial control.

## State model

`idea -> researching -> outlining -> drafting -> review -> ready -> publication PR -> published`

A post may move backward at any time. `published` requires an author-approved merge to `master`.

## 1. Idea intake

Capture the idea in a GitHub issue using the Blog Post issue form when possible. The issue is the durable record for:

- working title
- core thesis or question
- intended reader
- why the topic matters now
- author's initial position
- research notes
- counterarguments
- decisions and revisions
- publication PR link

A sparse issue is acceptable. Agents should fill gaps through research rather than forcing the author to complete every field.

## 2. Research

Research should answer both "what supports this thesis?" and "what would make it wrong?"

Expected output:

- primary/authoritative sources
- dates and freshness notes for time-sensitive claims
- strongest supporting evidence
- strongest counterarguments
- conflicting evidence
- edge cases
- claims that remain uncertain
- proposed thesis adjustments, if evidence warrants them

Do not draft around a conclusion that the evidence no longer supports.

## 3. Outline

Produce an outline that states the argument each section advances. Avoid sections that merely restate the topic.

The outline should include:

- opening problem/question
- thesis
- evidence sequence
- counterargument treatment
- practical implications
- conclusion that adds synthesis rather than repeating the introduction

## 4. Draft

Create the initial post at `_drafts/<slug>.markdown`.

Use the site's established Jekyll front matter, but drafts may omit final publication-only values such as canonical URL and final date.

Read `.github/blog/voice-guide.md` before drafting.

## 5. Independent review passes

Treat these as separate passes even if the same model performs them.

### Fact/technical review

- Verify factual claims against sources.
- Check technical examples for correctness.
- Flag stale or weak evidence.
- Do not rewrite merely for style.

### Argument review

- Identify unsupported leaps.
- Test causal claims.
- Surface omitted stakeholders and edge cases.
- Steelman the opposing position.
- Flag where opinion is being presented as fact.

### Voice review

- Apply the voice guide.
- Remove generic AI phrasing and unnecessary throat-clearing.
- Preserve technical nuance and the author's actual position.
- Do not introduce new factual claims during this pass.

## 6. Human editorial review

Before publication, present the author with:

- a concise thesis summary
- the complete draft
- the most contestable claims
- important sources
- unresolved uncertainties
- major editorial choices the agent made

The author may request revisions in prose, GitHub comments, or chat. Continue revising until the author explicitly says the post is ready for publication.

## 7. Publication preparation

After explicit approval to prepare publication:

1. Move/rename the draft to `_posts/YYYY-MM-DD-<slug>.markdown`.
2. Complete front matter: title, summary, excerpt, description, category, tags, date, canonical URL, author, and other established fields.
3. Add or verify imagery and alt text.
4. Run `python3 scripts/validate_blog_posts.py`.
5. Run the Jekyll build when available.
6. Create a dedicated `blog/<slug>` branch if one does not already exist.
7. Open a PR to `master`.
8. Leave the final human-approval checklist item unchecked.

## 8. Publication

The author reviews the PR and CI results and decides whether to merge.

Agents must not enable auto-merge or merge a blog-post PR without an explicit request to merge that specific PR.

Merging to `master` is the publication action. GitHub Pages then deploys the site.

## Suggested labels

Create these repository labels manually once:

- `blog:idea`
- `blog:researching`
- `blog:drafting`
- `blog:review`
- `blog:ready`
- `blog:published`
- `topic:ai`
- `topic:software-engineering`
- `topic:career`
- `topic:python`
- `topic:angular`

Labels are organizational aids, not publication authority.
