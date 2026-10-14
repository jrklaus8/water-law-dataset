import { Pill } from '../components/Badges'
import { claims, config, experiments, sources, statusOf, thesis } from '../lib/registry'
import { href } from '../lib/router'
import { StatusBadge } from '../components/Badges'

export function ThesisPage({ focus }: { focus?: string }) {
  return (
    <>
      <h1 tabIndex={-1}>Explore the thesis</h1>
      <p className="lead">{thesis.title}</p>
      <div className="callout info">
        <p>{thesis.notes}</p>
        <p className="small">Researcher: {thesis.authors.join(', ')}. Institution: {config.project.institution}. Status: <strong>{thesis.research_status.replace('_', ' ')}</strong>.</p>
      </div>
      {thesis.chapters.map((c) => (
        <section key={c.id} className={`chapter${focus === c.id ? ' focus' : ''}`} id={c.id} aria-labelledby={`${c.id}-h`}>
          <h2 id={`${c.id}-h`}>{c.title} <Pill tone={c.status === 'planned' ? 'neutral' : 'info'}>{c.status.replace('_', ' ')}</Pill></h2>
          {c.research_questions?.length ? (<><h3>Research questions</h3><ul>{c.research_questions.map((q) => <li key={q}>{q}</li>)}</ul></>) : <p className="muted">No research questions recorded yet.</p>}
          {c.experiment_ids?.length ? (<><h3>Experiments</h3><ul>{c.experiment_ids.map((id) => { const m = experiments[id]; return m ? <li key={id}><a href={href('lab', id)}>{m.title}</a> <StatusBadge status={statusOf(m).status} /></li> : null })}</ul></>) : null}
          {c.claim_ids?.length ? (<><h3>Claims</h3><ul>{c.claim_ids.map((id) => <li key={id}><a href={href('evidence', id)}>{claims[id]?.text ?? id}</a></li>)}</ul></>) : null}
          {c.source_ids?.length ? (<><h3>Sources</h3><ul>{c.source_ids.map((id) => <li key={id}><a href={href('evidence', id)}>{sources[id]?.title ?? id}</a></li>)}</ul></>) : null}
        </section>
      ))}
    </>
  )
}
