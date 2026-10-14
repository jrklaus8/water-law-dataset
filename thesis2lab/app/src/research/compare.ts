import type { ReferenceCase, RunResult } from './types'

export const tolFor = (tol: Record<string, number>, key: string): number => tol[key] ?? tol.default ?? 0

export function compare(expected: Record<string, number | string>, actual: Record<string, unknown>, tol: Record<string, number>) {
  const diffs: Record<string, unknown> = {}
  let ok = true
  for (const [k, e] of Object.entries(expected)) {
    const a = actual[k]
    if (typeof e === 'number') {
      const d = typeof a === 'number' ? Math.abs(a - e) : Infinity
      if (!(d <= tolFor(tol, k) + 1e-12)) { ok = false; diffs[k] = { expected: e, actual: a ?? null, tolerance: tolFor(tol, k) } }
    } else if (a !== e) { ok = false; diffs[k] = { expected: e, actual: a ?? null } }
  }
  return { ok, diffs }
}

export interface ComparisonRow { metric: string; expected: number | string; actual: number | string | null; tolerance: number | null; difference: number | null; pass: boolean }

/** Row-by-row comparison of one reference scenario with a fresh run. */
export function compareCase(c: ReferenceCase, res: RunResult): ComparisonRow[] {
  return Object.entries(c.expected).map(([metric, expected]) => {
    const a = res.metrics[metric] ?? null
    const num = typeof expected === 'number'
    const tolerance = num ? tolFor(c.tolerance, metric) : null
    const difference = num && typeof a === 'number' ? a - expected : null
    const pass = num ? typeof a === 'number' && Math.abs(a - expected) <= (tolerance ?? 0) + 1e-12 : a === expected
    return { metric, expected, actual: a, tolerance, difference, pass }
  })
}
