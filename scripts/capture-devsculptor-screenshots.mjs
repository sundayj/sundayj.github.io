import { mkdirSync, rmSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const scriptDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(scriptDir, '..');
const outputDir = resolve(
  process.env.JLSUNDAY_PORTFOLIO_SCREENSHOT_DIR ??
    resolve(repoRoot, 'artifacts/devsculptor-portfolio-screenshots'),
);
const baseUrl = process.env.JLSUNDAY_PREVIEW_URL ?? 'http://127.0.0.1:4000';

await assertPreviewReachable(baseUrl);

rmSync(outputDir, { recursive: true, force: true });
mkdirSync(outputDir, { recursive: true });

const npx = process.platform === 'win32' ? 'npx.cmd' : 'npx';
const result = spawnSync(
  npx,
  ['playwright', 'test', 'e2e/devsculptor-portfolio.spec.ts', '--project=chromium', '--workers=1'],
  {
    cwd: repoRoot,
    env: {
      ...process.env,
      JLSUNDAY_PREVIEW_URL: baseUrl,
      JLSUNDAY_PORTFOLIO_SCREENSHOT_DIR: outputDir,
    },
    stdio: 'inherit',
  },
);

if (result.error) {
  throw new Error(`Unable to run Playwright portfolio capture: ${result.error.message}`);
}
if (result.status !== 0) {
  throw new Error(`DevSculptor portfolio screenshot capture failed with status ${result.status}.`);
}

console.log(`\nDevSculptor portfolio screenshots written to:\n  ${outputDir}`);

async function assertPreviewReachable(url) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 5000);

  try {
    const response = await fetch(url, { signal: controller.signal, redirect: 'manual' });
    if (response.status >= 400) {
      throw new Error(`preview returned HTTP ${response.status}`);
    }
  } catch (error) {
    throw new Error(
      `JLSunday preview is not reachable at ${url}. Start it first with "bundle exec jekyll serve --livereload". (${String(error)})`,
    );
  } finally {
    clearTimeout(timeout);
  }
}
