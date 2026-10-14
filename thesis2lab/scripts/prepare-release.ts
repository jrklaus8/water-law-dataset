/**
 * Drafts a ResearchRelease record from the current state. Releases are always created as 'draft':
 * a researcher must approve (set status 'approved' and approved_by) before anything is published.
 * Usage: npm run release:prepare -- 0.1.0
 */
import { execSync } from 'node:child_process'
import { existsSync, writeFileSync, mkdirSync } from 'node:fs'
import { effectiveStatus } from '../app/src/research/status'
import { inputsDigest, loadProject, loadReport, p, readJson, validateAgainst } from './lib/project'

const version = process.argv[2]
if (!version || !/^\d+\.\d+\.\d+$/.test(version)) { console.error('Usage: npm run release:prepare -- <major.minor.patch>'); process.exit(2) }
const out = p('research/manifests', `REL-${version}.json`)
if (existsSync(out)) { console.error(`${out} already exists. Releases are immutable; choose a new version.`); process.exit(2) }
const { manifests, datasets } = loadProject()
const thesis = readJson<{ version: string }>(p('research/thesis/thesis.json'))
let commit: string | null = null
try { commit = execSync('git rev-parse HEAD', { cwd: p('.'), encoding: 'utf8' }).trim() } catch { /* no git */ }
const notes = manifests.map((m) => {
  const eff = effectiveStatus(m, loadReport(m.id), m.dataset_ids.length ? inputsDigest(m, datasets) : undefined)
  return `${m.id} ${m.title}: shown as ${eff.status}${eff.downgraded ? ` (declared ${eff.declared})` : ''}`
})
notes.push('Draft only. No researcher has approved this release.')
const rel = {
  schema_version: '1.0', id: `REL-${version}`, thesis_version: thesis.version,
  dataset_versions: Object.fromEntries(Object.values(datasets).map((d) => [d.id, d.version])),
  experiment_versions: Object.fromEntries(manifests.map((m) => [m.id, m.version])),
  code_commit: commit, release_date: new Date().toISOString().slice(0, 10), status: 'draft', notes, archived_references: [], approved_by: null,
}
const errs = validateAgainst('release', rel)
if (errs.length) { console.error(errs.join('\n')); process.exit(1) }
mkdirSync(p('research/manifests'), { recursive: true })
writeFileSync(out, JSON.stringify(rel, null, 2) + '\n')
console.log(`Wrote ${out}. Status: draft.`)
