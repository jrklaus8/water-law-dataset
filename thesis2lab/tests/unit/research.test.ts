import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'
import { bootstrapCi, cohenKappa, mulberry32, runAgreement } from '../../app/src/research/agreement'
import { loadRows, parseCsv, toCsv } from '../../app/src/research/csv'
import { applyFilters, median, olsSlope, runDescriptive } from '../../app/src/research/descriptive'
import { runExperiment } from '../../app/src/research/runners'
import { loadProject, p } from '../../scripts/lib/project'

describe('csv', () => {
  it('parses quotes, escaped quotes, CRLF and BOM', () => {
    expect(parseCsv('﻿a,b\r\n"x,1","he said ""hi"""\n')).toEqual([['a', 'b'], ['x,1', 'he said "hi"']])
  })
  it('rejects a file whose columns differ from the dataset record', () => {
    expect(() => loadRows('a,b\n1,2\n', [{ name: 'a', type: 'integer' }, { name: 'c', type: 'integer' }])).toThrow(/do not match/)
  })
  it('rejects non-numeric values in numeric columns', () => {
    expect(() => loadRows('a\nx\n', [{ name: 'a', type: 'integer' }])).toThrow(/not numeric/)
  })
  it('round-trips through toCsv', () => {
    const rows = [{ a: 'x,y', b: 2 }]
    expect(parseCsv(toCsv(rows, ['a', 'b']))).toEqual([['a', 'b'], ['x,y', '2']])
  })
})

describe('descriptive statistics', () => {
  it('median handles odd, even and empty', () => {
    expect([median([3, 1, 2]), median([4, 1, 2, 3]), median([])]).toEqual([2, 2.5, null])
  })
  it('olsSlope matches a hand computed line', () => {
    expect(olsSlope([1, 2, 3], [2, 4, 6])).toBeCloseTo(2, 12)
    expect(olsSlope([1], [1])).toBeNull()
  })
  const cfg = { year_variable: 'y', category_variables: ['c'] }
  const rows = [{ y: 2000, c: 'a' }, { y: 2000, c: 'b' }, { y: 2002, c: 'a' }]
  it('filters by year range and category (empty selection means all)', () => {
    expect(applyFilters(rows, { year_min: 2001 }, cfg)).toHaveLength(1)
    expect(applyFilters(rows, { c: ['a'] }, cfg)).toHaveLength(2)
    expect(applyFilters(rows, { c: [] }, cfg)).toHaveLength(3)
  })
  it('zero-fills missing years before fitting the trend', () => {
    const r = runDescriptive(rows, {}, cfg)
    expect(r.tables[0].rows).toEqual([[2000, 2], [2001, 0], [2002, 1]])
    expect(r.metrics.yearly_trend_slope).toBeCloseTo(-0.5, 12)
  })
  it('reports an empty selection explicitly', () => {
    const r = runDescriptive(rows, { c: ['zzz'] }, cfg)
    expect(r.metrics.n_selected).toBe(0)
    expect(r.notes[0]).toMatch(/No records/)
  })
})

describe('agreement', () => {
  it('kappa equals a hand computed value', () => {
    expect(cohenKappa(['A', 'A', 'B', 'B'], ['A', 'B', 'B', 'B'])).toBeCloseTo(0.5, 12)
  })
  it('perfect agreement gives 1 and chance-level gives 0', () => {
    expect(cohenKappa(['A', 'B'], ['A', 'B'])).toBe(1)
    expect(cohenKappa(['A', 'A', 'B', 'B'], ['A', 'B', 'A', 'B'])).toBeCloseTo(0, 12)
  })
  it('seeded PRNG and bootstrap are deterministic and bracket the estimate', () => {
    expect(mulberry32(1)()).toBe(mulberry32(1)())
    const y1 = ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B']
    const y2 = ['A', 'A', 'B', 'A', 'A', 'B', 'B', 'B']
    const ci = bootstrapCi(y1, y2, 500, 7)!
    expect(bootstrapCi(y1, y2, 500, 7)).toEqual(ci)
    expect(ci[0]).toBeLessThanOrEqual(cohenKappa(y1, y2)!)
    expect(ci[1]).toBeGreaterThanOrEqual(cohenKappa(y1, y2)!)
  })
  it('rejects unknown specifications instead of guessing', () => {
    expect(() => runAgreement([], { specification: 'nope' }, {} as never)).toThrow(/Unknown specification/)
  })
})

describe('registered experiments (end to end, real data)', () => {
  const { manifests, datasets } = loadProject()
  const load = (id: string) => {
    const m = manifests.find((x) => x.id === id)!
    const ds = datasets[m.dataset_ids[0]]
    return { m, rows: loadRows(readFileSync(p(ds.path), 'utf8'), ds.variables) }
  }
  it('EXP-001 controls change the calculated output', () => {
    const { m, rows } = load('EXP-001')
    const all = runExperiment(m, rows, { year_min: 2000, year_max: 2025 })
    const some = runExperiment(m, rows, { year_min: 2010, year_max: 2020, country: ['Brazil'] })
    expect(all.metrics.n_selected).toBe(600)
    expect(some.metrics.n_selected).toBeLessThan(all.metrics.n_selected as number)
    expect(some.metrics.top_country).toBe('Brazil')
  })
  it('EXP-002 recomputes the published kappa under each specification', () => {
    const { m, rows } = load('EXP-002')
    const k = (specification: string) => runExperiment(m, rows, { specification }).metrics
    expect(k('three_label_baseline')).toMatchObject({ n: 91 })
    expect(k('three_label_baseline').cohen_kappa).toBeCloseTo(0.5684, 4)
    expect(k('mananciais_rule').cohen_kappa).toBeCloseTo(0.832, 3)
    expect(k('binary_exclude_uncertain')).toMatchObject({ n: 59 })
    expect(k('binary_exclude_uncertain').cohen_kappa).toBeCloseTo(0.932, 3)
    expect(k('coder1_confident')).toMatchObject({ n: 63 })
  })
})
