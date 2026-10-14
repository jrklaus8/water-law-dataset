import type { Params, Row, RunResult } from './types'

export interface DescriptiveConfig {
  year_variable: string
  category_variables: string[]
  numeric_variable?: string
}

const asList = (v: unknown): string[] => (Array.isArray(v) ? (v as string[]) : [])

/** Filters: `<variable>` multiselect params (empty = no restriction), plus year_min / year_max. */
export function applyFilters(rows: Row[], params: Params, cfg: DescriptiveConfig): Row[] {
  const yMin = typeof params.year_min === 'number' ? params.year_min : -Infinity
  const yMax = typeof params.year_max === 'number' ? params.year_max : Infinity
  return rows.filter((r) => {
    const y = r[cfg.year_variable] as number
    if (y < yMin || y > yMax) return false
    return cfg.category_variables.every((v) => {
      const allowed = asList(params[v])
      return allowed.length === 0 || allowed.includes(String(r[v]))
    })
  })
}

export function median(xs: number[]): number | null {
  if (!xs.length) return null
  const s = [...xs].sort((a, b) => a - b)
  const m = s.length >> 1
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2
}

/** Ordinary least squares slope of y on x. */
export function olsSlope(xs: number[], ys: number[]): number | null {
  const n = xs.length
  if (n < 2) return null
  const mx = xs.reduce((a, b) => a + b, 0) / n
  const my = ys.reduce((a, b) => a + b, 0) / n
  let sxy = 0
  let sxx = 0
  for (let i = 0; i < n; i++) {
    sxy += (xs[i] - mx) * (ys[i] - my)
    sxx += (xs[i] - mx) ** 2
  }
  return sxx === 0 ? null : sxy / sxx
}

export function runDescriptive(rows: Row[], params: Params, cfg: DescriptiveConfig): RunResult {
  const sel = applyFilters(rows, params, cfg)
  const notes: string[] = []
  if (sel.length === 0) notes.push('No records match the current filters.')

  // counts per year across the full span of the selection (zero-filled so the trend is not biased)
  const years = sel.map((r) => r[cfg.year_variable] as number)
  const yMin = years.length ? Math.min(...years) : null
  const yMax = years.length ? Math.max(...years) : null
  const byYear: [number, number][] = []
  if (yMin !== null && yMax !== null) {
    for (let y = yMin; y <= yMax; y++) byYear.push([y, years.filter((v) => v === y).length])
  }
  const slope = olsSlope(byYear.map((p) => p[0]), byYear.map((p) => p[1]))

  const tables = [
    {
      id: 'by_year', title: 'Records per year', columns: ['year', 'count'],
      rows: byYear.map(([y, c]) => [y, c]),
    },
    ...cfg.category_variables.map((v) => {
      const counts = new Map<string, number>()
      sel.forEach((r) => counts.set(String(r[v]), (counts.get(String(r[v])) ?? 0) + 1))
      const entries = [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
      return {
        id: `by_${v}`, title: `Records by ${v}`, columns: [v, 'count', 'share'],
        rows: entries.map(([k, c]) => [k, c, sel.length ? c / sel.length : 0]),
      }
    }),
  ]

  const metrics: RunResult['metrics'] = {
    n_total: rows.length,
    n_selected: sel.length,
    share_selected: rows.length ? sel.length / rows.length : 0,
    year_min: yMin,
    year_max: yMax,
    yearly_trend_slope: slope,
  }
  for (const v of cfg.category_variables) {
    const t = tables.find((x) => x.id === `by_${v}`)!
    metrics[`n_distinct_${v}`] = t.rows.length
    metrics[`top_${v}`] = t.rows.length ? String(t.rows[0][0]) : null
  }
  if (cfg.numeric_variable) {
    const xs = sel.map((r) => r[cfg.numeric_variable!] as number)
    metrics[`${cfg.numeric_variable}_mean`] = xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null
    metrics[`${cfg.numeric_variable}_median`] = median(xs)
  }
  return { metrics, tables, selectedRows: sel, notes }
}
