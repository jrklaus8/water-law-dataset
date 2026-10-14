import { useState } from 'react'
import { DataTable } from '../charts/Charts'
import { compareCase, type ComparisonRow } from '../research/compare'
import { runExperiment } from '../research/runners'
import type { ExperimentManifest, ReferenceFile, Row } from '../research/types'

export type Comparison = { scenario: string; rows: ComparisonRow[] }

export function ReferencePanel({ m, rows, refs, onResults }: { m: ExperimentManifest; rows: Row[]; refs: ReferenceFile[]; onResults: (c: Comparison[]) => void }) {
  const [results, setResults] = useState<Comparison[] | null>(null)
  const cases = refs.flatMap((r) => r.cases)
  if (!cases.length) return <p>This experiment has no reference outputs, so no comparison is possible.</p>
  const run = () => {
    const out = cases.map((c) => ({ scenario: c.id, rows: compareCase(c, runExperiment(m, rows, c.parameters)) }))
    setResults(out)
    onResults(out)
  }
  return (
    <div>
      <p>Each scenario below re-runs the calculation in your browser with fixed parameters and compares the outputs with a reference. The comparison does not use the controls above.</p>
      <button type="button" className="btn" onClick={run}>{results ? 'Run again' : 'Run all reference comparisons'}</button>
      {results && (
        <div aria-live="polite">
          {cases.map((c, i) => {
            const r = results[i]
            const allPass = r.rows.every((x) => x.pass)
            return (
              <details key={c.id} className="refcase" open={!allPass}>
                <summary>
                  <span className={allPass ? 'res-pass' : 'res-fail'}>{allPass ? 'Matches' : 'Differs'}</span> {c.description}
                  {c.required === false && <span className="pill neutral"> secondary</span>}
                </summary>
                <p className="small muted">Reference: {c.provenance.kind.replace(/_/g, ' ')}. {c.provenance.source}. {c.provenance.note ?? ''}</p>
                <DataTable columns={['metric', 'reference', 'this run', 'allowed difference', 'result']}
                  rows={r.rows.map((x) => [x.metric, x.expected, x.actual, x.tolerance, x.pass ? 'match' : 'DIFFERS'])} />
              </details>
            )
          })}
        </div>
      )}
    </div>
  )
}
