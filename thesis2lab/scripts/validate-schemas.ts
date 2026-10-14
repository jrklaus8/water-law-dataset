/** Validate every research record against its JSON Schema and check cross-references. */
import { existsSync } from 'node:fs'
import { ROOT, listFiles, loadProject, p, readJson, sha256, validateAgainst } from './lib/project'
import { readFileSync } from 'node:fs'

const errors: string[] = []
const fail = (where: string, msg: string) => errors.push(`${where}: ${msg}`)
const ids: Record<string, Set<string>> = { SRC: new Set(), DS: new Set(), CLM: new Set(), MTH: new Set(), EXP: new Set(), CH: new Set() }
let count = 0

function check(schema: string, file: string, prefix?: string) {
  const data = readJson<{ id?: string }>(file)
  count++
  validateAgainst(schema, data).forEach((e) => fail(file.replace(ROOT + '/', ''), e))
  if (prefix && data.id) {
    if (ids[prefix].has(data.id)) fail(file, `duplicate id ${data.id}`)
    ids[prefix].add(data.id)
  }
  return data
}

check('project-config', p('project.config.json'))
check('project-config', p('examples/other-project/project.config.json'))
const thesis = check('thesis', p('research/thesis/thesis.json')) as { chapters: { id: string; claim_ids?: string[]; experiment_ids?: string[]; source_ids?: string[] }[]; source_ids?: string[] }
thesis.chapters.forEach((c) => ids.CH.add(c.id))
listFiles(p('research/sources')).forEach((f) => check('source', f, 'SRC'))
const datasets = listFiles(p('data/metadata')).map((f) => check('dataset', f, 'DS')) as { id: string; path: string; checksum_sha256: string; source_ids?: string[] }[]
const claims = listFiles(p('research/claims')).map((f) => check('claim', f, 'CLM')) as { id: string; source_ids: string[]; chapter_ids?: string[]; experiment_ids?: string[] }[]
listFiles(p('research/methods')).forEach((f) => check('method', f, 'MTH'))
const gov = listFiles(p('research/governance')).map((f) => check('governance-evidence', f)) as { source_id: string; jurisdiction: string; category: string }[]
const { manifests } = loadProject()
manifests.forEach((m) => { count++; validateAgainst('experiment', m).forEach((e) => fail(`experiments/${m.id}/manifest.json`, e)); ids.EXP.add(m.id) })
listFiles(p('validation/reports')).forEach((f) => { count++; validateAgainst('validation-report', readJson(f)).forEach((e) => fail(f.replace(ROOT + '/', ''), e)) })
listFiles(p('research/manifests')).forEach((f) => check('release', f))

// cross references
const need = (kind: keyof typeof ids, id: string, where: string) => { if (!ids[kind].has(id)) fail(where, `unknown ${kind} reference ${id}`) }
thesis.source_ids?.forEach((s) => need('SRC', s, 'thesis'))
thesis.chapters.forEach((c) => {
  c.claim_ids?.forEach((x) => need('CLM', x, c.id)); c.experiment_ids?.forEach((x) => need('EXP', x, c.id)); c.source_ids?.forEach((x) => need('SRC', x, c.id))
})
claims.forEach((c) => { c.source_ids.forEach((x) => need('SRC', x, c.id)); c.chapter_ids?.forEach((x) => need('CH', x, c.id)); c.experiment_ids?.forEach((x) => need('EXP', x, c.id)) })
gov.forEach((g) => need('SRC', g.source_id, 'governance evidence'))
datasets.forEach((d) => {
  d.source_ids?.forEach((x) => need('SRC', x, d.id))
  if (!existsSync(p(d.path))) fail(d.id, `data file missing: ${d.path}`)
  else if (sha256(readFileSync(p(d.path))) !== d.checksum_sha256) fail(d.id, 'checksum mismatch with data file')
})
manifests.forEach((m) => {
  m.source_ids.forEach((x) => need('SRC', x, m.id)); m.dataset_ids.forEach((x) => need('DS', x, m.id)); m.chapter_ids?.forEach((x) => need('CH', x, m.id)); m.claim_ids?.forEach((x) => need('CLM', x, m.id))
  if (m.method_id) need('MTH', m.method_id, m.id)
  m.reference_outputs.forEach((r) => { if (!existsSync(p('experiments', m.id, r))) fail(m.id, `missing reference file ${r}`) })
  if (m.reproducibility_status === 'REPRODUCIBLE' && m.reference_outputs.length === 0) fail(m.id, 'REPRODUCIBLE requires reference outputs')
  if (m.runner === null && !['BLOCKED', 'AUDITABLE'].includes(m.reproducibility_status)) fail(m.id, 'experiments without a runner must be BLOCKED or AUDITABLE')
  if (m.requires_ai) fail(m.id, 'requires_ai must be false in the initial release (Mode C is disabled)')
  if (m.data_kind === 'synthetic' && !m.ui_notice) fail(m.id, 'synthetic experiments need a ui_notice')
  if (m.data_kind === 'synthetic' && m.reproducibility_status === 'REPRODUCIBLE') fail(m.id, 'synthetic data can never be REPRODUCIBLE')
  m.dataset_ids.forEach((d) => { const rec = datasets.find((x) => x.id === d) as { kind?: string } | undefined; if (rec?.kind === 'synthetic' && m.data_kind !== 'synthetic') fail(m.id, `uses synthetic dataset ${d} but data_kind is ${m.data_kind}`) })
})

if (errors.length) { console.error(errors.map((e) => '  - ' + e).join('\n')); console.error(`\nSchema validation FAILED (${errors.length} problems in ${count} records)`); process.exit(1) }
console.log(`Schema validation passed: ${count} records, cross-references consistent.`)
