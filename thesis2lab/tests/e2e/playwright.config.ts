import { defineConfig } from '@playwright/test'
import { existsSync, readdirSync } from 'node:fs'
import { join } from 'node:path'

// Set CHROMIUM_PATH to use a specific Chromium; otherwise Playwright's own installed browser is used.
// In managed sandboxes a Chromium of a different revision may be preinstalled under PLAYWRIGHT_BROWSERS_PATH.
function preinstalled(): string | undefined {
  const base = process.env.PLAYWRIGHT_BROWSERS_PATH
  if (!base || !existsSync(base)) return undefined
  const dir = readdirSync(base).find((d) => /^chromium-\d+$/.test(d))
  const bin = dir && join(base, dir, 'chrome-linux', 'chrome')
  return bin && existsSync(bin) ? bin : undefined
}
const executablePath = process.env.CHROMIUM_PATH ?? preinstalled()

export default defineConfig({
  testDir: '.',
  timeout: 30_000,
  fullyParallel: true,
  reporter: [['list']],
  use: { baseURL: 'http://127.0.0.1:4173', launchOptions: executablePath ? { executablePath } : {} },
  webServer: { command: 'npx vite preview --config app/vite.config.ts --host 127.0.0.1 --port 4173 --strictPort', cwd: '../..', url: 'http://127.0.0.1:4173', reuseExistingServer: !process.env.CI, timeout: 60_000 },
  projects: [
    { name: 'desktop', use: { viewport: { width: 1280, height: 900 } } },
    { name: 'mobile', use: { viewport: { width: 390, height: 800 } } },
  ],
})
