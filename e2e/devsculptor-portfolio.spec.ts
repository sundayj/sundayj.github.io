import { expect, test, type Locator, type Page } from '@playwright/test';
import { resolve } from 'node:path';

const outputDir = resolve(
  process.env.JLSUNDAY_PORTFOLIO_SCREENSHOT_DIR ??
    'artifacts/devsculptor-portfolio-screenshots',
);

const articleTitle = "Your Parser Shouldn't Get One Shot";

test.describe.configure({ mode: 'serial' });

test('capture home desktop dark', async ({ page }) => {
  await prepare(page, 'dark', { width: 1440, height: 1000 });
  await page.goto('/');
  await expect(page.locator('#site-logo')).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-home-desktop-dark.png');
});

test('capture home desktop light', async ({ page }) => {
  await prepare(page, 'light', { width: 1440, height: 1000 });
  await page.goto('/');
  await expect(page.locator('#site-logo')).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-home-desktop-light.png');
});

test('capture article desktop dark', async ({ page }) => {
  await prepare(page, 'dark', { width: 1440, height: 1000 });
  await gotoRepresentativeArticle(page);
  await expect(page.getByRole('heading', { name: articleTitle, level: 1 })).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-article-desktop-dark.png');
});

test('capture projects desktop light', async ({ page }) => {
  await prepare(page, 'light', { width: 1440, height: 1000 });
  await page.goto('/projects/');
  await expect(page.getByRole('heading', { name: /projects/i, level: 1 })).toBeVisible();
  const firstProjectActions = page.locator('.project-actions').first();
  await expect(firstProjectActions).toBeVisible();
  await settle(page);
  await captureThrough(page, firstProjectActions, 'devsculptor-projects-desktop-light.png');
});

test('capture home mobile dark', async ({ page }) => {
  await prepare(page, 'dark', { width: 430, height: 932 });
  await page.goto('/');
  await expect(page.locator('#site-logo')).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-home-mobile-dark.png');
});

test('capture article mobile light', async ({ page }) => {
  await prepare(page, 'light', { width: 430, height: 932 });
  await gotoRepresentativeArticle(page);
  await expect(page.getByRole('heading', { name: articleTitle, level: 1 })).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-article-mobile-light.png');
});

async function gotoRepresentativeArticle(page: Page): Promise<void> {
  await page.goto('/');
  const articleLink = page.getByRole('link', { name: articleTitle }).first();
  await expect(articleLink).toBeVisible();
  const href = await articleLink.getAttribute('href');
  if (!href) {
    throw new Error(`Could not resolve a local URL for representative article: ${articleTitle}`);
  }
  await page.goto(href);
}

async function prepare(
  page: Page,
  theme: 'light' | 'dark',
  viewport: { width: number; height: number },
): Promise<void> {
  await page.setViewportSize(viewport);
  await page.emulateMedia({ colorScheme: theme, reducedMotion: 'reduce' });
  await page.addInitScript((selectedTheme) => {
    localStorage.setItem('theme', selectedTheme);
  }, theme);
}

async function settle(page: Page): Promise<void> {
  await expect(page.locator('html')).toHaveAttribute('data-bs-theme', /^(light|dark)$/);
  await page.waitForLoadState('domcontentloaded');
  await page.waitForLoadState('networkidle', { timeout: 5000 }).catch(() => undefined);
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all(
      Array.from(document.images).map((image) =>
        image.complete ? Promise.resolve() : image.decode().catch(() => undefined),
      ),
    );
  });
  await page.waitForTimeout(250);
}

async function capture(page: Page, filename: string): Promise<void> {
  await page.screenshot({
    path: resolve(outputDir, filename),
    fullPage: false,
    animations: 'disabled',
    caret: 'hide',
  });
}

async function captureThrough(page: Page, locator: Locator, filename: string): Promise<void> {
  const box = await locator.boundingBox();
  const viewport = page.viewportSize();
  if (!box || !viewport) {
    throw new Error(`Could not calculate deterministic crop for ${filename}.`);
  }

  const bottomPadding = 12;
  const captureHeight = Math.min(
    viewport.height,
    Math.ceil(box.y + box.height + bottomPadding),
  );

  await page.screenshot({
    path: resolve(outputDir, filename),
    clip: {
      x: 0,
      y: 0,
      width: viewport.width,
      height: captureHeight,
    },
    animations: 'disabled',
    caret: 'hide',
  });
}
