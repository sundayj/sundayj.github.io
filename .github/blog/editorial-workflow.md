# Editorial Workflow

This file is the durable workflow for producing JLSunday blog posts with AI assistance while preserving human editorial control.

## State model

`idea -> researching -> outlining -> drafting -> review -> ready -> publication PR -> published`

A post may move backward at any time. `published` requires an author-approved merge to `master`.

## Artifact chain

For posts with an editorial issue, keep one explicit chain of durable artifacts:

`issue #N -> blog/N-<slug> working branch -> _drafts/<slug>.markdown -> publication PR (Closes #N) -> merge`

The issue is the editorial record, the branch is the working artifact, the draft is the prose artifact, and the PR is the publication gate. The repository remains the source of truth for code/content that actually exists.

For new posts, create the working branch when the issue enters `blog:drafting`. Use `blog/<issue-number>-<slug>` so the relationship is visible even outside GitHub's UI. If GitHub's native Development relationship can be created, use it. If the available agent/tooling cannot create that relationship, add a concise issue comment recording the branch. Do not create a duplicate branch solely to retrofit this naming convention onto an existing draft.

## 1. Idea intake

Capture the idea in a GitHub issue using the Blog Post issue form when possible. The issue is the durable record for:

- working title
- core thesis or question
- intended reader
- why the topic matters now
- author's initial position
- research notes and research ledger
- counterarguments
- decisions and revisions
- working draft branch
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

### Durable research ledger

For research-heavy posts, maintain a compact research ledger in the editorial issue alongside synthesis and conclusion notes. The ledger exists to preserve research coverage and provenance, including sources that ultimately do not appear in the article.

Record every materially evaluated source, project, methodology, tool, competing approach, or adjacent system. Do not limit the ledger to sources selected for citation.

Each entry should record at minimum:

- **Name / source**
- **Date investigated**
- **Canonical URL or repository**, when available
- **Why it is relevant**
- **Key finding / relationship to the thesis**
- **Disposition**, such as `foundational lineage`, `related work`, `competing approach`, `supporting evidence`, `counterevidence`, `rejected/irrelevant`, or `revisit`

Keep entries concise. Full research synthesis may live in separate issue comments; the ledger answers the narrower questions "Did we investigate this?", "Why?", "What did we conclude?", and "Where did it come from?"

When later evidence introduces a materially relevant source that was missed or cannot be confirmed in the existing ledger, add it explicitly and mark it as post-publication or late-stage research rather than implying it was part of the original research pass.

Before moving from research to outlining, review the ledger for obvious gaps in competing approaches, intellectual lineage, counterevidence, and primary sources. For claims of novelty or methodological distinctiveness, perform an adversarial related-work pass and record the closest alternatives even when the conclusion is that they differ materially.

The research ledger is durable editorial state, not a citation requirement. The final article should cite only sources that materially support the published argument.

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

When the editorial issue enters `blog:drafting`:

1. Create or identify its dedicated working branch. For new work, use `blog/<issue-number>-<slug>`.
2. Link the branch through GitHub's Development UI when supported by the available tooling; otherwise record the branch on the issue.
3. Create the initial post at `_drafts/<slug>.markdown` on that branch.

Drafts require only `layout: post` and a working `title`; publication metadata may remain incomplete until the article is approved for publication. When adding metadata early, follow `docs/editorial-content-contract.md` rather than the legacy front matter found in older posts.

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

### Final anti-slop review

This is the final automated editorial step before the draft is presented for human approval. Run it only after fact, technical, argument, and normal voice review are complete.

Apply the full checklist in `.github/blog/voice-guide.md`, including these non-negotiable requirements:

- Remove every em dash (`—`) from authored prose. Justin does not use them in his own writing.
- Remove generic throat-clearing and canned AI transitions.
- Prefer concrete engineering experience, named tools, traceable evidence, and falsifiable specificity over generic claims.
- Preserve real opinions, disagreement, counterarguments, and uncertainty rather than smoothing the article into artificial consensus.
- Reduce unnecessary headings, repeated summaries, listicle structure, and overly symmetrical organization.
- Vary sentence rhythm and remove repetitive rhetorical patterns.
- Scrutinize stock AI vocabulary, inflated language, and fake profundity.
- Never manufacture personal anecdotes or first-person experiences.
- Flag paragraphs that could be pasted unchanged into an unrelated AI-generated article.

This pass is allowed to revise style, structure, rhythm, and emphasis. It must not introduce new factual claims, citations, statistics, technical claims, or personal anecdotes. Any factual addition goes back through fact review. Any personal experience must come from information the author actually supplied.

The purpose of this gate is not to conceal AI assistance. It is to ensure the draft reaches the author as specific, evidence-based writing that reflects Justin's actual voice and engineering judgment rather than default model prose.

## 6. Human editorial review

Before publication, present the author with:

- a concise thesis summary
- the complete draft
- the most contestable claims
- important sources
- unresolved uncertainties
- major editorial choices the agent made
- confirmation that the final anti-slop pass completed and no em dashes remain in authored prose

The author may request revisions in prose, GitHub comments, or chat. Continue revising until the author explicitly says the post is ready for publication.

## 7. Publication preparation

After explicit approval to prepare publication:

1. Stay on the issue's existing working branch; do not create a second publication branch unless there is a concrete reason.
2. Move/rename the draft to `_posts/YYYY-MM-DD-kebab-case-slug.markdown`.
3. Complete the current front-matter contract from `docs/editorial-content-contract.md`: `layout`, `title`, `date`, one canonical `description`, plural `categories`, and focused `tags`, plus optional fields only when they add real value.
4. Do not add legacy duplicate `summary`, `excerpt`, `canonical_url`, or singular `category` fields to a new/current-contract post.
5. Add or verify imagery and alt text. Substantial authored hero illustrations should follow `.github/blog/voice-guide.md`; use PNG for the current editorial-illustration style. A featured post must have a valid image.
6. Verify body headings start at H2 and remove draft placeholders/local-only URLs.
7. Run `python3 scripts/test_validate_blog_posts.py`.
8. Run `python3 scripts/validate_blog_posts.py`.
9. Run the Jekyll build when available; CI will also validate generated internal links/assets in the changed article body.
10. Open a PR to `master` from the working branch.
11. Include `Closes #<issue-number>` in the PR body. Do not rely only on a bare URL or `Refs`; the closing keyword is part of the editorial-state automation contract.
12. Leave the final human-approval checklist item unchecked.

## 8. Publication

The author reviews the PR and CI results and decides whether to merge.

Agents must not enable auto-merge or merge a blog-post PR without an explicit request to merge that specific PR.

Merging to `master` is the publication action. GitHub Pages then deploys the site, and the linked editorial issue can transition to `blog:published`.

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
