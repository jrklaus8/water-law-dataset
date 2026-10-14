/**
 * Lightweight cost report built only from facts this repository can measure.
 * It never estimates tokens or invoices: AI-assisted development usage and any API spend are
 * recorded as "not measured" unless a human adds them to docs/cost-ledger.json.
 */
import { existsSync, readdirSync, statSync, writeFileSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
import { inputsDigest, loadProject, loadReport, p, readJson } from './lib/project'

const { manifests, datasets } = loadProject()
const du = (dir: string): number => (existsSync(dir) ? readdirSync(dir).reduce((n, f) => { const fp = join(dir, f); return n + (statSync(fp).isDirectory() ? du(fp) : statSync(fp).size) }, 0) : 0)
const pkg = readJson<{ dependencies: Record<string, string>; devDependencies: Record<string, string> }>(p('package.json'))
const ledgerPath = p('docs/cost-ledger.json')
const ledger = existsSync(ledgerPath) ? readJson<{ entries: unknown[] }>(ledgerPath).entries : []
const runnable = manifests.filter((m) => m.runner)
const reused = runnable.filter((m) => loadReport(m.id)?.inputs_digest === inputsDigest(m, datasets)).map((m) => m.id)
const report = {
  public_runtime: { ai_api_calls_per_visit: 0, servers: 0, experiments_requiring_ai: manifests.filter((m) => m.requires_ai).map((m) => m.id) },
  ai_assisted_development: { measured: false, note: 'Not measured by this repository. Add entries to docs/cost-ledger.json from your own billing or usage views.', ledger_entries: ledger.length },
  api_expenditure: { measured: false, amount: null },
  infrastructure: ['GitHub repository (free tier)', 'GitHub Actions (free tier minutes)', 'GitHub Pages (free tier, not enabled by this project)'],
  runtime_dependencies: Object.keys(pkg.dependencies),
  build_dependencies: Object.keys(pkg.devDependencies).length,
  static_site_bytes: du(p('app/dist')) || null,
  validation_reuse: { current_reports_reusable: reused, needing_recomputation: runnable.map((m) => m.id).filter((id) => !reused.includes(id)) },
}
console.log(JSON.stringify(report, null, 2))
if (process.argv.includes('--write')) { mkdirSync(p('validation/provenance'), { recursive: true }); writeFileSync(p('validation/provenance/cost-report.json'), JSON.stringify(report, null, 2) + '\n') }
