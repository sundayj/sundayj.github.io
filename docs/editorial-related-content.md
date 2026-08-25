# Editorial related-content candidates

JLSunday uses a conservative, metadata-based candidate scorer to help editorial workflows find potentially useful first-party links. It is intentionally **not** an automatic related-post UI and it never edits or publishes content.

## Usage

Run the scorer against one draft or published post:

```bash
python3 scripts/suggest_related_posts.py _drafts/my-article.markdown
```

For structured agent/tooling consumption:

```bash
python3 scripts/suggest_related_posts.py _drafts/my-article.markdown --json
```

The command compares the target with published posts and may return zero candidates.

## Scoring contract

The current weights come directly from JE-003 / decision JD-005:

- shared category: +3 per category
- shared tag: +2 per tag
- same explicit `series`: +8
- default threshold: 6
- default maximum candidates: 3

Each result includes the score components, shared metadata, source path, and stable Jekyll post reference. Tie-breaking is deterministic.

Legacy singular `category` remains readable for older posts, while current posts use plural `categories`.

## Editorial boundary

A score means **candidate for human/editorial consideration**, not “insert this link.” A later editorial pass should decide:

- whether the relationship is actually useful in the target article;
- where a link would help the reader rather than interrupt the argument;
- whether the link should be outbound from the new article, or whether an older article merits a separate inbound-link update;
- whether no link is preferable.

The scorer must not modify Markdown, create publication commits, or cross the human publication boundary.

## Why there is no automatic Related Posts UI

JE-003 found the current corpus too sparse and taxonomically uneven to justify an always-visible related-post surface. The scorer produced one clear reciprocal relationship and correctly returned no recommendation for the remaining topics. The adapted decision is therefore to use the high-precision signal inside the editorial workflow first and revisit presentation after the corpus/current taxonomy becomes materially denser.