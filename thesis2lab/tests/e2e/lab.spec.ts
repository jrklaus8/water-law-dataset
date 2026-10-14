import { expect, test } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'
import { readFileSync } from 'node:fs'

const metric = (page: import('@playwright/test').Page, name: string) =>
  page.locator('.metrics > div', { has: page.locator('dt', { hasText: new RegExp(`^${name}$`) }) }).locator('dd')

test('home page lists every experiment with its verified status', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByRole('heading', { level: 1, name: 'The Legal Last Mile' })).toBeVisible()
  await expect(page.getByText('Research in progress. The thesis is not written yet')).toBeVisible()
  await page.getByRole('navigation', { name: 'Main' }).getByRole('link', { name: 'Laboratory' }).click()
  await expect(page.getByText('3 of 3 experiments shown.')).toBeVisible()
  await expect(page.locator('article', { hasText: 'Bibliometric explorer' }).getByText('Exploratory')).toBeVisible()
  await expect(page.locator('article', { hasText: 'Reproducing the coding-agreement audit' }).getByText('Partially reproduced')).toBeVisible()
  await expect(page.locator('article', { hasText: 'Theme shares' }).getByText('Blocked')).toBeVisible()
})

test('status filter narrows the catalogue', async ({ page }) => {
  await page.goto('/#/lab')
  await page.getByLabel('Status').selectOption('BLOCKED')
  await expect(page.getByText('1 of 3 experiments shown.')).toBeVisible()
})

test('EXP-001: controls change calculated output and synthetic data is labelled', async ({ page }) => {
  await page.goto('/#/lab/EXP-001')
  await expect(page.getByText('SYNTHETIC DATA.').first()).toBeVisible()
  await expect(metric(page, 'n selected')).toHaveText('600')
  await page.getByLabel('Brazil').check()
  const brazil = Number(await metric(page, 'n selected').textContent())
  expect(brazil).toBe(264)
  await page.getByLabel('From year').fill('2010')
  await expect.poll(async () => Number(await metric(page, 'n selected').textContent())).toBeLessThan(brazil)
  await page.getByRole('button', { name: 'Reset to defaults' }).click()
  await expect(metric(page, 'n selected')).toHaveText('600')
})

test('EXP-001: invalid year range is explained', async ({ page }) => {
  await page.goto('/#/lab/EXP-001')
  await page.getByLabel('From year').fill('2024')
  await page.getByLabel('To year').fill('2005')
  await expect(page.getByRole('alert').filter({ hasText: 'later than' })).toBeVisible()
  await expect(metric(page, 'n selected')).toHaveText('0')
})

test('EXP-002: reproduces the published kappa, exposes the discrepancy, exports a record', async ({ page }) => {
  await page.goto('/#/lab/EXP-002')
  await expect(page.getByText('Partially reproduced').first()).toBeVisible()
  await expect(metric(page, 'cohen kappa')).toHaveText('0.5684')
  await page.getByLabel('Specification').selectOption('mananciais_rule')
  await expect(metric(page, 'cohen kappa')).toHaveText('0.8318')
  await page.getByLabel('Specification').selectOption('binary_exclude_uncertain')
  await expect(metric(page, 'n')).toHaveText('59')

  await page.getByRole('button', { name: 'Run all reference comparisons' }).click()
  await expect(page.getByText('Matches').first()).toBeVisible()
  await expect(page.locator('summary', { hasText: 'Differs' }).first()).toBeVisible() // secondary CI comparisons honestly differ

  const [dl] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Reproducibility record (JSON)' }).click()])
  const rec = JSON.parse(readFileSync((await dl.path())!, 'utf8'))
  expect(rec.experiment.id).toBe('EXP-002')
  expect(rec.parameters.specification).toBe('binary_exclude_uncertain')
  expect(rec.datasets[0].checksum_sha256).toMatch(/^[a-f0-9]{64}$/)
  expect(rec.reference_comparison.length).toBeGreaterThan(3)
  expect(rec.committed_validation.independent_review.status).toBe('pending')
})

test('EXP-001 exports filtered data as CSV', async ({ page }) => {
  await page.goto('/#/lab/EXP-001')
  await page.getByLabel('Canada').check()
  const [dl] = await Promise.all([page.waitForEvent('download'), page.getByRole('button', { name: 'Filtered data (CSV)' }).click()])
  const lines = readFileSync((await dl.path())!, 'utf8').trim().split('\n')
  expect(lines[0]).toBe('record_id,year,country,theme,method,institution,citations')
  expect(lines.slice(1).every((l) => l.split(',')[2] === 'Canada')).toBe(true)
})

test('EXP-003: blocked experiment runs nothing and says why', async ({ page }) => {
  await page.goto('/#/lab/EXP-003')
  await expect(page.getByText('Blocked').first()).toBeVisible()
  await expect(page.getByRole('heading', { name: 'Why nothing runs' })).toBeVisible()
  await expect(page.getByRole('button', { name: /Reproducibility record/ })).toHaveCount(0)
})

test('evidence explorer derives reproduction labels from reports', async ({ page }) => {
  await page.goto('/#/evidence')
  const c2 = page.locator('#CLM-IC-002')
  await expect(c2.getByText('Numerically reproduced')).toBeVisible()
  await expect(c2.getByText('Researcher review: unreviewed')).toBeVisible()
  await expect(page.locator('#CLM-IC-005').getByText('Not (fully) reproduced')).toBeVisible()
  await expect(page.locator('#CLM-DS-001').getByText('Blocked', { exact: true })).toBeVisible()
})

test('comparative governance shows only recorded evidence', async ({ page }) => {
  await page.goto('/#/compare')
  await expect(page.getByText('No verified evidence yet').first()).toBeVisible()
  await expect(page.getByText('Researcher hypothesis').first()).toBeVisible()
})

test('unknown experiment id fails gracefully', async ({ page }) => {
  await page.goto('/#/lab/EXP-999')
  await expect(page.getByRole('heading', { name: 'Experiment not found' })).toBeVisible()
})

for (const route of ['', 'cover', 'thesis', 'lab', 'lab/EXP-001', 'lab/EXP-002', 'lab/EXP-003', 'evidence', 'compare', 'methods', 'versions', 'about']) {
  test(`accessibility (axe, WCAG 2 A/AA): /${route}`, async ({ page }) => {
    await page.goto(`/#/${route}`)
    await page.waitForLoadState('networkidle')
    if (route.startsWith('lab/EXP-00') && route !== 'lab/EXP-003') await expect(page.locator('.metrics')).toBeVisible()
    const r = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze()
    expect(r.violations.map((v) => `${v.id}: ${v.nodes.map((n) => n.target.join(' ')).join(' | ')}`)).toEqual([])
  })
}

test('keyboard: skip link moves focus to main content', async ({ page }) => {
  await page.goto('/')
  await page.keyboard.press('Tab')
  await expect(page.getByRole('link', { name: 'Skip to content' })).toBeFocused()
  await page.keyboard.press('Enter')
  await expect(page.locator('#main')).toBeFocused()
})

for (const route of ['', 'lab/EXP-002', 'evidence']) {
  test(`accessibility in dark colour scheme: /${route}`, async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'dark' })
    await page.goto(`/#/${route}`)
    await page.waitForLoadState('networkidle')
    if (route === 'lab/EXP-002') await expect(page.locator('.metrics')).toBeVisible()
    const r = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa']).analyze()
    expect(r.violations.map((v) => `${v.id}: ${v.nodes.map((n) => n.target.join(' ')).join(' | ')}`)).toEqual([])
  })
}

test('cover page explains partial basis and AI role, and home links to it', async ({ page }) => {
  await page.goto('/')
  await page.getByRole('link', { name: 'Read this first' }).first().click()
  await expect(page.getByRole('heading', { level: 1, name: 'Read this first' })).toBeVisible()
  await expect(page.getByRole('heading', { name: 'It is based on partial studies' })).toBeVisible()
  await expect(page.getByRole('heading', { name: 'What AI was used for' })).toBeVisible()
  await expect(page.getByText('does not call any AI service')).toBeVisible()
})
