# DevSculptor portfolio screenshots

JLSunday can generate a repeatable screenshot set that demonstrates the DevSculptor theme through its real consuming site.

## Prerequisites

Start the local Jekyll preview from the repository root:

```bash
rbenv shell 3.1.7
bundle exec jekyll serve --livereload
```

In another terminal, install the Node dependencies and Chromium once:

```bash
npm install
npx playwright install chromium
```

## Capture the screenshot set

```bash
npm run portfolio:screenshots
```

The runner verifies the local preview is reachable at `http://127.0.0.1:4000` before Playwright starts. It captures fixed viewport images with explicit light/dark state, reduced motion, animations disabled, fonts/images settled, and no full-page expansion.

Generated files:

- `devsculptor-home-desktop-dark.png`
- `devsculptor-home-desktop-light.png`
- `devsculptor-article-desktop-dark.png`
- `devsculptor-projects-desktop-light.png`
- `devsculptor-home-mobile-dark.png`
- `devsculptor-article-mobile-light.png`

They are written to `artifacts/devsculptor-portfolio-screenshots/`, which is ignored by Git. Review the captures before copying selected files into `assets/images/projects/devsculptor/` for publication.

## Overrides

```bash
JLSUNDAY_PREVIEW_URL=http://127.0.0.1:4000 \
JLSUNDAY_PORTFOLIO_SCREENSHOT_DIR=/tmp/devsculptor-screenshots \
npm run portfolio:screenshots
```

The representative article is intentionally a stable current post in the repository so the workflow exercises modern article typography and navigation in addition to the homepage and Projects page.
