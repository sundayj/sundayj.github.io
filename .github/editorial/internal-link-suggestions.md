# Editorial internal-link suggestions

CI-014 turns the JE-003/CI-013 relevance scorer into review-only workflow assistance.

For same-repository pull requests whose branch starts with `blog/` and that change files under `_drafts/`, GitHub Actions posts or refreshes one PR comment containing:

- outbound candidates the draft may link to;
- inbound candidates that may deserve a backlink after the new article has an approved publish URL;
- the score and metadata overlap that caused each suggestion.

The workflow does **not** edit Markdown. Zero suggestions is valid.

## Publication boundary

Automated editorial work stays in `_drafts`. Jekyll does not publish `_drafts` in the normal production build. Moving an approved article into `_posts` is a separate publication step and is not performed by the suggestion workflow.

This separation is intentional for JE-006: a dry-run editorial PR can be merged without making the article live, while actual publication still requires an explicit human-approved promotion.
