/**
 * Change detection. Compares what each validation report was built from with what is on disk now,
 * and checks registered sources against their recorded checksums. Reports only; changes nothing
 * unless --write is passed (then writes validation/provenance/change-report.json).
 * Dependency chain: source -> claim -> experiment, dataset -> experiment, code -> every experiment.
 */
import { existsSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
import { inputsDigest, listFiles, loadProject, loadReport, p, readJson, sha256 } from './lib/project'

const { manifests, datasets } = loadProject()
const stale: { experiment: string; reason: string }[] = []
for (const m of manifests.filter((x) => x.runner)) {
  const r = loadReport(m.id)
  if (!r) stale.push({ experiment: m.id, reason: 'no validation report' })
  else if (r.inputs_digest !== inputsDigest(m, datasets)) stale.push({ experiment: m.id, reason: 'experiment files, dataset or analysis code changed since the last validation' })
}

const sourceChanges: { source: string; status: string; affected_experiments: string[] }[] = []
const parentRepo = join(p('..'))
for (const f of listFiles(p('research/sources'))) {
  const s = readJson<{ id: string; checksum_sha256: string | null; location: { type: string; ref: string } }>(f)
  if (!s.checksum_sha256 || s.location.type !== 'repository_path') continue
  const file = join(parentRepo, s.location.ref.split('#')[0])
  const status = !existsSync(file) ? 'not found next to this project (cannot check)' : sha256(readFileSync(file)) === s.checksum_sha256 ? 'unchanged' : 'CHANGED since registration'
  const claims = listFiles(p('research/claims')).map((c) => readJson<{ source_ids: string[]; experiment_ids?: string[] }>(c)).filter((c) => c.source_ids.includes(s.id))
  const affected = [...new Set([...claims.flatMap((c) => c.experiment_ids ?? []), ...manifests.filter((m) => m.source_ids.includes(s.id)).map((m) => m.id)])]
  sourceChanges.push({ source: s.id, status, affected_experiments: affected })
}
const report = { stale_validations: stale, sources: sourceChanges }
console.log('Experiments needing revalidation:', stale.length ? '' : 'none')
stale.forEach((s) => console.log(`  - ${s.experiment}: ${s.reason}`))
console.log('Registered sources:')
sourceChanges.forEach((s) => console.log(`  - ${s.source}: ${s.status}${s.status.startsWith('CHANGED') ? `; revalidate ${s.affected_experiments.join(', ') || '(no experiment linked)'}` : ''}`))
if (process.argv.includes('--write')) { mkdirSync(p('validation/provenance'), { recursive: true }); writeFileSync(p('validation/provenance/change-report.json'), JSON.stringify(report, null, 2) + '\n') }
if (process.argv.includes('--fail-on-stale') && (stale.length || sourceChanges.some((s) => s.status.startsWith('CHANGED')))) process.exit(1)
