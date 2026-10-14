import type { Params, Row, RunResult } from './types'

export interface AgreementConfig {
  coder1_variable: string
  coder2_variable: string
  group_variable: string
  /** Value of group_variable the calibration rule applies to. */
  rule_group: string
  rule_from: string
  rule_to: string
  uncertain_label: string
}

export type SpecId = 'three_label_baseline' | 'mananciais_rule' | 'binary_exclude_uncertain' | 'coder1_confident'

export const SPEC_LABELS: Record<SpecId, string> = {
  three_label_baseline: 'Three labels, no rule (pre-calibration baseline)',
  mananciais_rule: 'Three labels, calibration rule applied (coder 1 UNCERTAIN recoded for one group)',
  binary_exclude_uncertain: 'Binary: exclude pairs where either coder said UNCERTAIN',
  coder1_confident: 'Only pairs where coder 1 gave a confident (non-UNCERTAIN) label',
}

/** Seeded PRNG (mulberry32) so interface and tests give identical intervals. */
export function mulberry32(seed: number): () => number {
  let a = seed >>> 0
  return () => {
    a = (a + 0x6d2b79f5) >>> 0
    let t = a
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export function observedAgreement(y1: string[], y2: string[]): number {
  return y1.filter((v, i) => v === y2[i]).length / y1.length
}

export function cohenKappa(y1: string[], y2: string[]): number | null {
  const n = y1.length
  if (n === 0) return null
  const po = observedAgreement(y1, y2)
  const c1 = new Map<string, number>()
  const c2 = new Map<string, number>()
  y1.forEach((v) => c1.set(v, (c1.get(v) ?? 0) + 1))
  y2.forEach((v) => c2.set(v, (c2.get(v) ?? 0) + 1))
  let pe = 0
  new Set([...c1.keys(), ...c2.keys()]).forEach((k) => { pe += ((c1.get(k) ?? 0) / n) * ((c2.get(k) ?? 0) / n) })
  return pe === 1 ? 1 : (po - pe) / (1 - pe)
}

export function bootstrapCi(y1: string[], y2: string[], nBoot: number, seed: number): [number, number] | null {
  const n = y1.length
  if (n < 2) return null
  const rnd = mulberry32(seed)
  const ks: number[] = []
  for (let b = 0; b < nBoot; b++) {
    const s1: string[] = []
    const s2: string[] = []
    for (let i = 0; i < n; i++) { const j = Math.floor(rnd() * n); s1.push(y1[j]); s2.push(y2[j]) }
    ks.push(cohenKappa(s1, s2) as number)
  }
  ks.sort((a, b) => a - b)
  return [ks[Math.floor(0.025 * nBoot)], ks[Math.floor(0.975 * nBoot)]]
}

export function perCategory(y1: string[], y2: string[]) {
  return [...new Set([...y1, ...y2])].sort().map((cat) => {
    let tp = 0, fp = 0, fn = 0
    y1.forEach((a, i) => {
      const b = y2[i]
      if (a === cat && b === cat) tp++
      else if (a !== cat && b === cat) fp++
      else if (a === cat && b !== cat) fn++
    })
    return { cat, tp, fp, fn, precision: tp + fp ? tp / (tp + fp) : null, recall: tp + fn ? tp / (tp + fn) : null }
  })
}

export function runAgreement(rows: Row[], params: Params, cfg: AgreementConfig): RunResult {
  const spec = (params.specification ?? 'three_label_baseline') as SpecId
  if (!(spec in SPEC_LABELS)) throw new Error(`Unknown specification: ${String(spec)}`)
  const nBoot = typeof params.bootstrap_iterations === 'number' ? params.bootstrap_iterations : 0
  const seed = typeof params.bootstrap_seed === 'number' ? params.bootstrap_seed : 42
  const notes: string[] = []

  let used = rows.map((r) => ({
    a: String(r[cfg.coder1_variable]), b: String(r[cfg.coder2_variable]), g: String(r[cfg.group_variable]),
  }))
  if (spec === 'mananciais_rule') {
    const before = used.filter((u) => u.g === cfg.rule_group && u.a === cfg.rule_from).length
    used = used.map((u) => (u.g === cfg.rule_group && u.a === cfg.rule_from ? { ...u, a: cfg.rule_to } : u))
    notes.push(`Rule recoded ${before} coder-1 labels (${cfg.rule_from} to ${cfg.rule_to}) for group "${cfg.rule_group}". The dataset has no per-case topic flag, so the rule is applied to the whole group.`)
  } else if (spec === 'binary_exclude_uncertain') {
    used = used.filter((u) => u.a !== cfg.uncertain_label && u.b !== cfg.uncertain_label)
  } else if (spec === 'coder1_confident') {
    used = used.filter((u) => u.a !== cfg.uncertain_label)
  }
  const y1 = used.map((u) => u.a)
  const y2 = used.map((u) => u.b)
  const kappa = cohenKappa(y1, y2)
  const ci = nBoot > 0 ? bootstrapCi(y1, y2, nBoot, seed) : null
  const pc = perCategory(y1, y2)
  const cats = [...new Set([...y1, ...y2])].sort()

  const metrics: RunResult['metrics'] = {
    n: used.length,
    observed_agreement: used.length ? observedAgreement(y1, y2) : null,
    cohen_kappa: kappa,
    ci_low: ci ? ci[0] : null,
    ci_high: ci ? ci[1] : null,
  }
  pc.forEach((p) => { metrics[`tp_${p.cat}`] = p.tp; metrics[`fp_${p.cat}`] = p.fp; metrics[`fn_${p.cat}`] = p.fn })

  return {
    metrics,
    tables: [
      {
        id: 'per_category', title: 'Per-category agreement (coder 2 treated as the prediction)',
        columns: ['label', 'tp', 'fp', 'fn', 'precision', 'recall'],
        rows: pc.map((p) => [p.cat, p.tp, p.fp, p.fn, p.precision, p.recall]),
      },
      {
        id: 'confusion', title: 'Confusion matrix (rows: coder 1, columns: coder 2)',
        columns: ['coder 1 \\ coder 2', ...cats],
        rows: cats.map((a) => [a, ...cats.map((b) => y1.filter((v, i) => v === a && y2[i] === b).length)]),
      },
    ],
    notes,
  }
}
