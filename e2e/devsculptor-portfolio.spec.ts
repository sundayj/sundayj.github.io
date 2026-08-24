import { expect, test, type Page } from '@playwright/test';
import { resolve } from 'node:path';

const outputDir = resolve(
  process.env.JLSUNDAY_PORTFOLIO_SCREENSHOT_DIR ??
    'artifacts/devsculptor-portfolio-screenshots',
);

const articlePath = '/software-development/2026/08/23/your-parser-shouldnt-get-one-shot.html';

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
  await page.goto(articlePath);
  await expect(page.getByRole('heading', { name: "Your Parser Shouldn't Get One Shot", level: 1 })).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-article-desktop-dark.png');
});

test('capture projects desktop light', async ({ page }) => {
  await prepare(page, 'light', { width: 1440, height: 1000 });
  await page.goto('/projects/');
  await expect(page.getByRole('heading', { name: /projects/i, level: 1 })).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-projects-desktop-light.png');
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
  await page.goto(articlePath);
  await expect(page.getByRole('heading', { name: "Your Parser Shouldn't Get One Shot", level: 1 })).toBeVisible();
  await settle(page);
  await capture(page, 'devsculptor-article-mobile-light.png');
});

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
