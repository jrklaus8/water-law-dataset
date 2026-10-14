/**
 * Executes every runnable experiment against its reference outputs and writes
 * machine-readable validation reports (validation/reports/EXP-xxx.json) plus the
 * build-time digest table the interface uses to detect stale reports.
 * Reports are produced from program output only; nothing is hand-written.
 */
import { execSync, spawnSync } from 'node:child_process'
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { loadRows } from '../app/src/research/csv'
import { compare } from '../app/src/research/compare'
import { runExperiment } from '../app/src/research/runners'
import { effectiveStatus } from '../app/src/research/status'
import type { ExperimentManifest, Params, RunResult, ValidationCheck, ValidationReport } from '../app/src/research/types'
import { inputsDigest, loadProject, loadReferences, loadReport, p, sha256 } from './lib/project'

const { manifests, datasets } = loadProject()
const digests: Record<string, string> = {}
let failed = 0

function python(m: ExperimentManifest, dsPath: string, params: Params): { metrics: Record<string, unknown>; original_function_kappa?: number | null } | null {
  const script = p('experiments', m.id, 'tests/reference_impl.py')
  if (!existsSync(script)) return null
  const r = spawnSync('python3', ['-I', script, '--dataset', dsPath, '--params', JSON.stringify(params)], { encoding: 'utf8' })
  if (r.status !== 0) throw new Error(`python reference failed for ${m.id}: ${r.stderr.slice(0, 500)}`)
  return JSON.parse(r.stdout)
}

function gitInfo() {
  try {
    const commit = execSync('git rev-parse HEAD', { cwd: p('.'), encoding: 'utf8' }).trim()
    const dirty = execSync('git status --porcelain -- .', { cwd: p('.'), encoding: 'utf8' }).trim().length > 0
    return { git_commit: commit, working_tree_dirty: dirty }
  } catch { return { git_commit: null, note: 'git not available' } }
}

function validate(m: ExperimentManifest): ValidationReport {
  const checks: ValidationCheck[] = []
  const add = (c: ValidationCheck) => checks.push(c)
  const ds = datasets[m.dataset_ids[0]]
  const dsPath = p(ds.path)
  const text = readFileSync(dsPath, 'utf8')
  const checksums: Record<string, string> = {}

  for (const id of m.dataset_ids) {
    const rec = datasets[id]
    checksums[id] = sha256(readFileSync(p(rec.path)))
    add({ id: `tech:checksum:${id}`, kind: 'technical', description: `Dataset ${id} file checksum equals its record`, pass: checksums[id] === rec.checksum_sha256, required: true, expected: rec.checksum_sha256, actual: checksums[id] })
  }
  let rows
  try {
    rows = loadRows(text, ds.variables)
    add({ id: 'tech:parse', kind: 'technical', description: 'CSV parses and matches the declared columns and types', pass: true, required: true })
  } catch (e) {
    add({ id: 'tech:parse', kind: 'technical', description: 'CSV parses and matches the declared columns and types', pass: false, required: true, actual: String(e) })
    return finish(m, checks, checksums)
  }
  add({ id: 'tech:rows', kind: 'technical', description: 'Row count equals the dataset record', pass: rows.length === ds.row_count, required: true, expected: ds.row_count, actual: rows.length })
  const badCats = ds.variables.filter((v) => v.type === 'category' && v.categories).flatMap((v) => rows!.filter((r) => !v.categories!.includes(String(r[v.name]))).map(() => v.name))
  add({ id: 'tech:categories', kind: 'technical', description: 'Every categorical value belongs to its declared category list', pass: badCats.length === 0, required: true, actual: badCats.length })

  for (const file of loadReferences(m)) {
    for (const c of file.cases) {
      const required = c.required !== false
      let res: RunResult | undefined
      try { res = runExperiment(m, rows, c.parameters); add({ id: `tech:run:${c.id}`, kind: 'technical', description: `Runner executes for scenario "${c.id}"`, pass: true, required: true }) }
      catch (e) { add({ id: `tech:run:${c.id}`, kind: 'technical', description: `Runner executes for scenario "${c.id}"`, pass: false, required: true, actual: String(e) }); continue }

      const { ok, diffs } = compare(c.expected, res.metrics, c.tolerance)
      add({ id: `ref:${c.id}`, kind: 'numerical', description: `${c.description} (vs ${c.provenance.source})`, pass: ok, required, reference_kind: c.provenance.kind, claim_id: c.claim_id, expected: c.expected, actual: Object.fromEntries(Object.keys(c.expected).map((k) => [k, res!.metrics[k] ?? null])), tolerance: c.tolerance, difference: ok ? undefined : diffs })

      const again = runExperiment(m, rows, c.parameters)
      add({ id: `rep:${c.id}`, kind: 'repeatability', description: `Two executions of "${c.id}" give identical output`, pass: JSON.stringify(again.metrics) === JSON.stringify(res.metrics) && JSON.stringify(again.tables) === JSON.stringify(res.tables), required: true })

      if (required) {
        const py = python(m, dsPath, c.parameters)
        if (py) {
          const keys = new Set([...Object.keys(py.metrics), ...Object.keys(res.metrics).filter((k) => !k.startsWith('ci_'))])
          const expectedAll = Object.fromEntries([...keys].map((k) => [k, (py.metrics[k] ?? null) as number | string]))
          const cmp = compare(Object.fromEntries(Object.entries(expectedAll).filter(([, v]) => v !== null)), res.metrics, { default: 1e-9 })
          const nullMismatch = [...keys].filter((k) => expectedAll[k] === null && res!.metrics[k] !== null && res!.metrics[k] !== undefined)
          add({ id: `py:${c.id}`, kind: 'numerical', description: `Independent Python implementation agrees on "${c.id}" (all ${keys.size} metrics)`, pass: cmp.ok && nullMismatch.length === 0, required: true, reference_kind: 'independent_reimplementation', difference: cmp.ok && !nullMismatch.length ? undefined : { ...cmp.diffs, nullMismatch } })
          if (py.original_function_kappa !== undefined && py.original_function_kappa !== null) {
            const k = res.metrics.cohen_kappa as number
            add({ id: `fid:${c.id}`, kind: 'methodological', description: `Kappa equals the original validation/kappa_calculator.py function on "${c.id}"`, pass: Math.abs(k - py.original_function_kappa) < 1e-12, required: true, expected: py.original_function_kappa, actual: k })
          }
        }
      }
    }
  }
  return finish(m, checks, checksums)
}

function finish(m: ExperimentManifest, checks: ValidationCheck[], dataset_checksums: Record<string, string>): ValidationReport {
  const req = checks.filter((c) => c.required !== false)
  const kind = (k: ValidationCheck['kind']) => req.filter((c) => c.kind === k)
  const st = (cs: ValidationCheck[], na: 'not_applicable' | 'not_assessed' = 'not_applicable') => (cs.length === 0 ? na : cs.every((c) => c.pass) ? 'pass' : 'fail')
  const summary = {
    technical_execution: st(kind('technical')) as 'pass' | 'fail' | 'not_applicable',
    numerical_agreement: st(kind('numerical')) as 'pass' | 'fail' | 'not_applicable',
    methodological_fidelity: st(kind('methodological'), 'not_assessed') as 'pass' | 'fail' | 'not_assessed',
    repeatability: st(kind('repeatability')) as 'pass' | 'fail' | 'not_applicable',
    checks_total: checks.length,
    checks_passed: checks.filter((c) => c.pass).length,
    overall: (req.length > 0 && req.every((c) => c.pass) ? 'pass' : 'fail') as 'pass' | 'fail',
  }
  const uncertainty = [...(m.unresolved ?? [])]
  const optionalFailed = checks.filter((c) => c.required === false && !c.pass)
  if (optionalFailed.length) uncertainty.unshift(`Non-required checks did not pass: ${optionalFailed.map((c) => c.id).join(', ')}.`)
  // A human review counts only if it was signed against exactly these inputs (same digest).
  const reviewFile = p('validation/reviews', `${m.id}.json`)
  const review = existsSync(reviewFile) ? (JSON.parse(readFileSync(reviewFile, 'utf8')) as { inputs_digest: string; reviewer: string; date: string; note?: string }) : undefined
  const signed = review && review.inputs_digest === digests[m.id] && review.reviewer
  if (review && !signed) uncertainty.push('A review file exists but was signed for different inputs, so it no longer applies.')
  if (!signed) uncertainty.push('Independent human review of this validation has not been recorded.')
  return {
    schema_version: '1.0', experiment_id: m.id, experiment_version: m.version, declared_status: m.reproducibility_status,
    inputs_digest: digests[m.id], code_version: gitInfo(),
    dependency_versions: { node: process.version, python: spawnSync('python3', ['--version'], { encoding: 'utf8' }).stdout.trim(), thesis2lab: '0.1.0' },
    dataset_checksums, checks, summary,
    independent_review: signed ? { status: 'completed', reviewer: review!.reviewer, date: review!.date, ...(review!.note ? { note: review!.note } : {}) } : { status: 'pending', note: 'No reviewer has signed off. Reports are generated by program execution only.' },
    remaining_uncertainty: uncertainty, generated_at: new Date().toISOString(),
  }
}

mkdirSync(p('validation/reports'), { recursive: true })
const strip = (r: ValidationReport | undefined) => r && JSON.stringify({ ...r, generated_at: 0, code_version: 0, dependency_versions: 0 })
for (const m of manifests) {
  digests[m.id] = m.dataset_ids.length ? inputsDigest(m, datasets) : sha256(JSON.stringify(m))
  if (!m.runner) { console.log(`${m.id}  ${m.reproducibility_status.padEnd(11)} no computation to validate`); continue }
  const report = validate(m)
  const old = loadReport(m.id)
  if (strip(old) !== strip(report)) writeFileSync(p('validation/reports', `${m.id}.json`), JSON.stringify(report, null, 2) + '\n')
  const eff = effectiveStatus(m, report, digests[m.id])
  const s = report.summary
  console.log(`${m.id}  declared ${m.reproducibility_status.padEnd(11)} shown ${eff.status.padEnd(11)} checks ${s.checks_passed}/${s.checks_total}  tech:${s.technical_execution} num:${s.numerical_agreement} fid:${s.methodological_fidelity} rep:${s.repeatability}`)
  for (const c of report.checks.filter((c) => !c.pass)) console.log(`    ${c.required === false ? 'note' : 'FAIL'} ${c.id}: ${JSON.stringify(c.difference ?? c.actual)}`)
  eff.reasons.forEach((r) => console.log('    downgrade reason: ' + r))
  if (s.overall !== 'pass' || eff.downgraded) failed++
}
mkdirSync(p('app/src/generated'), { recursive: true })
writeFileSync(p('app/src/generated/digests.json'), JSON.stringify(digests, null, 2) + '\n')
if (failed) { console.error(`\n${failed} experiment(s) failed validation or were downgraded.`); process.exit(1) }
console.log('\nAll declared statuses are supported by current validation reports.')
