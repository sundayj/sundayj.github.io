## Summary

<!-- What does this PR change? For blog posts, summarize the thesis and intended audience. -->

## Blog publication checklist

<!-- Leave non-blog items marked N/A where appropriate. -->

- [ ] N/A or this PR does not publish a blog post
- [ ] Post began as a draft or otherwise received author review before being placed in `_posts/`
- [ ] This publication PR explicitly closes its editorial issue with `Closes #N`
- [ ] Facts and technical claims were checked against current sources
- [ ] Meaningful counterarguments/edge cases were considered
- [ ] Voice review completed against `.github/blog/voice-guide.md`
- [ ] Front matter, title, description, tags, category, dates, and canonical URL are correct
- [ ] New images have useful alt text and appropriate attribution
- [ ] No `TODO`, `TBD`, `SOURCE NEEDED`, or similar draft markers remain
- [ ] `python3 scripts/validate_blog_posts.py` passes
- [ ] Jekyll build/CI passes
- [ ] **Justin explicitly approved this post for publication**

## Editorial notes

<!-- For a blog PR, call out contestable claims, unresolved uncertainty, and major editorial choices. -->

## Sources / related issue

<!-- REQUIRED for blog publication PRs: use `Closes #N` for the editorial issue so merge closes the issue and drives publication-state automation. -->

Closes #

## Publication rule

A blog-post PR must not be auto-merged. The final checkbox above represents human editorial approval; merge to `master` is the publication action.
