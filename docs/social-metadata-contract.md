# Social metadata contract

JLSunday delegates Open Graph, Twitter Card, canonical, and structured SEO metadata to `jekyll-seo-tag`. Theme/site code should not duplicate tags already owned by the plugin.

## Description ownership

GitHub Pages currently supplies `jekyll-seo-tag` 2.8.x, which does not emit `twitter:description`. DevSculptor therefore provides that one compatibility tag and resolves its value in this order:

1. `page.description` — current editorial contract.
2. `page.summary` — legacy post fallback.
3. `site.description` — final site fallback.

When the GitHub Pages plugin line provides native `twitter:description`, re-evaluate and remove the compatibility tag rather than keeping two owners.

## Social image ownership

`jekyll-seo-tag` owns `og:image` and Twitter image behavior.

JLSunday defines a site-wide Front Matter default image in `_config.yml`:

`/assets/images/JLSunday-logo/cover2-Logo.png`

Pages and posts may override the fallback with front-matter `image`. New local images use root-relative `/assets/...` paths or HTTPS URLs. Featured posts require an explicit article image rather than relying on the generic fallback.

Do not add hand-written `og:image` or `twitter:image` tags to DevSculptor or JLSunday unless a future evidence gate demonstrates that the plugin cannot satisfy a concrete requirement.

## Validation

`scripts/validate_generated_seo.py` runs after the Jekyll build and verifies:

- a single non-empty canonical URL and description owner;
- a single custom/native `twitter:description` and plugin-owned `og:description`;
- one non-empty absolute HTTPS `og:image` on Jekyll-rendered pages;
- a Twitter card declaration;
- the homepage receives the branded fallback image;
- a representative post with explicit `image` front matter overrides the fallback;
- the representative post's Twitter description reflects its page description rather than falling back to the site description.

The validation intentionally inspects generated HTML instead of duplicating the plugin's Liquid implementation in application code.
