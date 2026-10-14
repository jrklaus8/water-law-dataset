import { useState } from 'react'
import { Pill } from '../components/Badges'
import { config, governance, sources } from '../lib/registry'
import { href } from '../lib/router'

const TYPE = { verified_legal_source: 'Verified legal source', empirical_finding: 'Empirical finding (unreplicated)', researcher_hypothesis: 'Researcher hypothesis' } as const

export function ComparePage() {
  const jur = Object.entries(config.labels.jurisdictions).filter(([k]) => k !== 'ALL')
  const cats = Object.entries(config.labels.governance_categories ?? {})
  const [cat, setCat] = useState('')
  const shownCats = cats.filter(([k]) => !cat || k === cat)
  const count = governance.length
  return (
    <>
      <h1 tabIndex={-1}>Comparative governance explorer</h1>
      <p className="lead">A structure for comparing {jur.map(([, v]) => v).join(', ')} category by category. Every cell holds structured evidence records. Empty cells are deliberately empty.</p>
      <div className="callout info">
        <p><strong>{count} evidence records so far, none of them verified legal sources.</strong> They are the researcher's own theoretical model and one reported search result, recorded with their locations. This is a qualitative comparison, not a computational experiment, and it has no reproducibility status.</p>
      </div>
      <div className="field"><label htmlFor="g-cat">Category</label>
        <select id="g-cat" value={cat} onChange={(e) => setCat(e.target.value)}><option value="">All categories</option>{cats.map(([k, v]) => <option key={k} value={k}>{v}</option>)}</select></div>
      <div className="table-wrap" tabIndex={0} role="region" aria-label="Comparison matrix">
        <table className="matrix">
          <caption className="sr-only">Evidence by governance category and jurisdiction</caption>
          <thead><tr><th scope="col">Category</th>{jur.map(([k, v]) => <th key={k} scope="col">{v}</th>)}</tr></thead>
          <tbody>
            {shownCats.map(([ck, cv]) => (
              <tr key={ck}>
                <th scope="row">{cv}</th>
                {jur.map(([jk]) => {
                  const items = governance.filter((g) => g.category === ck && g.jurisdiction === jk)
                  return (
                    <td key={jk}>
                      {items.length === 0 ? <span className="muted">No verified evidence yet</span> : items.map((g) => (
                        <div key={g.id} className="gov">
                          <p><Pill tone="warn">{TYPE[g.evidence_type as keyof typeof TYPE]}</Pill></p>
                          <p>{g.statement}</p>
                          <p className="small muted">{g.locator}. <a href={href('evidence', g.source_id)}>{sources[g.source_id]?.title}</a>. Review: {g.review_status}. {g.caveat}</p>
                        </div>
                      ))}
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2>How to add evidence</h2>
      <p>Add a JSON file under <span className="mono">research/governance/</span> that follows <span className="mono">governance-evidence.schema.json</span>: jurisdiction, category, the statement, its type, a registered source and the exact location in it. The build refuses records that point to unknown sources.</p>
    </>
  )
}
