# JE-003 — Related-content scoring benchmark

## Question

Can a deterministic metadata-only scorer produce genuinely useful related-post recommendations on JLSunday without embeddings, vector infrastructure, or forced top-N results?

## Current corpus

The published corpus currently contains seven posts. Most of the older posts predate the current taxonomy contract and use legacy singular `category` plus heterogeneous tags. The two 2026 posts use substantially newer topics/metadata and do not have strong direct neighbors in the older corpus.

The seventh post, `Make Your Coding Agent Earn the Architecture`, was published after the initial experiment inventory. The first benchmark run intentionally failed because the human-judgment fixture did not silently accept an unreviewed corpus member. After review, it is classified as no automatic recommendation: it shares broad AI/architecture themes with the parser article, but not enough direct topical overlap to justify an always-visible related-post card.

Because the corpus is sparse, the experiment treats **no recommendation** as a valid and often preferable result.

## Scoring prototype

The bounded scorer uses only explicit post metadata:

- shared category: +3 per category
- shared tag: +2 per tag
- same explicit `series`: +8
- recommendation threshold: 6
- maximum results: 3
- deterministic title/path tie-breaking

The scorer emits the score components and overlapping metadata for every returned recommendation. It does not inspect article prose and does not use semantic embeddings.

## Human relevance judgments

For the current seven-post corpus, the conservative expected relationship is:

- `5 Great Free Software Development Tools` ↔ `40 Awesome Programming Resources`
- `Site Updates` → none
- `Building an App with Angular, Part 1: Introduction` → none
- `Comparing Pixel Art Editors` → none
- `Your Parser Shouldn't Get One Shot` → none
- `Make Your Coding Agent Earn the Architecture` → none

The key negative cases are:

- Pixel Art Editors shares legacy `category: Tools` and tag `tools` with the development-tools article, but that superficial overlap should remain below threshold.
- The parser and coding-agent articles share `ai`, but broad AI/architecture affinity alone should not force a recommendation.

## Evidence commands

```bash
python3 scripts/benchmark_related_posts.py
python3 scripts/test_related_content_benchmark.py
```

The experiment PR temporarily runs these commands in CI so the observed output is durable in the workflow log.

## Decision criteria

**Adopt** if the simple scorer matches the conservative human judgments, remains deterministic/explainable, and does not manufacture cross-topic recommendations.

**Adapt** if useful relationships are present but weights, taxonomy normalization, explicit series metadata, or editorial overrides are needed before implementation.

**Reject** if metadata is too sparse/noisy for useful recommendations and semantic/content-based scoring would be required.

Even an Adopt decision does **not** imply immediately adding a related-post UI. The next implementation step would be to use the scorer first as an editorial suggestion mechanism for CI-014, where humans can accept or reject proposed internal links.