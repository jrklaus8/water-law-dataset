/** Prints available research assets, experiment status and outstanding problems. Local files only; no network, no AI. */
import { existsSync } from 'node:fs'
import { effectiveStatus } from '../app/src/research/status'
import { inputsDigest, listFiles, loadProject, loadReport, p, readJson } from './lib/project'

const { manifests, datasets } = loadProject()
const count = (d: string) => listFiles(p(d)).length
console.log('THESIS2LAB STATUS')
console.log(`  sources ${count('research/sources')} | claims ${count('research/claims')} | methods ${count('research/methods')} | governance records ${count('research/governance')} | datasets ${count('data/metadata')} | releases ${count('research/manifests')}`)
const problems: string[] = []
console.log('\nEXPERIMENTS')
for (const m of manifests) {
  const report = loadReport(m.id)
  const digest = m.dataset_ids.length ? inputsDigest(m, datasets) : undefined
  const eff = effectiveStatus(m, report, digest)
  const fresh = !m.runner || (report && report.inputs_digest === digest)
  console.log(`  ${m.id}  declared ${m.reproducibility_status.padEnd(11)} shown ${eff.status.padEnd(11)} ${m.runner ? (fresh ? 'report current' : 'REPORT STALE') : 'not runnable'}  ${m.title}`)
  if (m.runner && !fresh) problems.push(`${m.id}: validation report is stale or missing. Run npm run validate:experiments.`)
  if (eff.downgraded) problems.push(`${m.id}: ${eff.reasons.join(' ')}`)
  ;(m.unresolved ?? []).forEach((u) => problems.push(`${m.id} unresolved: ${u}`))
}
const claims = listFiles(p('research/claims')).map((f) => readJson<{ id: string; review_status: string }>(f))
const unreviewed = claims.filter((c) => c.review_status === 'unreviewed').length
if (unreviewed) problems.push(`${unreviewed} of ${claims.length} claims have not been reviewed by the researcher.`)
const sources = listFiles(p('research/sources')).map((f) => readJson<{ id: string; copyright_status: string; extraction_status: string }>(f))
sources.filter((s) => s.copyright_status === 'unknown').forEach((s) => problems.push(`${s.id}: copyright status unknown. Confirm before any redistribution.`))
sources.filter((s) => s.extraction_status === 'registered').forEach((s) => problems.push(`${s.id}: registered but not yet extracted.`))
if (!existsSync(p('research/manifests')) || count('research/manifests') === 0) problems.push('No release prepared (npm run release:prepare).')
console.log('\nOUTSTANDING')
problems.forEach((x) => console.log('  - ' + x))
