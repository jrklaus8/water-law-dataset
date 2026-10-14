import { Pill, StatusBadge } from '../components/Badges'
import { claims, config, experimentList, statusOf, thesis } from '../lib/registry'
import { href } from '../lib/router'
import { STATUS_INFO } from '../research/status'
import type { ReproStatus } from '../research/types'

export function HomePage() {
  const counts: Partial<Record<ReproStatus, number>> = {}
  experimentList.forEach((m) => { const s = statusOf(m).status; counts[s] = (counts[s] ?? 0) + 1 })
  return (
    <>
      <div className="callout warn" role="note"><p><strong>An exploration based on partial studies.</strong> The thesis is not written and part of the evidence is missing or synthetic. <a href={href('cover')}>Read this first</a> to see what this is, what AI did and did not do, and how to read the results.</p></div>
      <section className="hero">
        <p className="eyebrow">Interactive research laboratory</p>
        <h1 tabIndex={-1}>{config.project.title}</h1>
        {config.project.subtitle && <p className="lead">{config.project.subtitle}</p>}
        <p>{config.project.summary}</p>
        <p className="actions">
          <a className="btn" href={href('lab')}>Open the laboratory</a>
          <a className="btn secondary" href={href('thesis')}>Explore the thesis</a>
        </p>
      </section>

      <section aria-labelledby="status-h">
        <h2 id="status-h">Where the research stands</h2>
        <dl className="facts">
          <div><dt>Thesis status</dt><dd>{thesis.research_status.replace('_', ' ')} (version {thesis.version})</dd></div>
          <div><dt>Chapters</dt><dd>{thesis.chapters.length} working entries, none final</dd></div>
          <div><dt>Claims on record</dt><dd>{Object.keys(claims).length}, all awaiting researcher review</dd></div>
          <div><dt>Experiments</dt><dd>{experimentList.length}</dd></div>
        </dl>
        <p className="small muted">Experiments by verified status: {(Object.keys(STATUS_INFO) as ReproStatus[]).filter((s) => counts[s]).map((s) => `${counts[s]} ${STATUS_INFO[s].label.toLowerCase()}`).join(', ')}.</p>
      </section>

      <section aria-labelledby="exp-h">
        <h2 id="exp-h">Experiments</h2>
        <div className="cards">
          {experimentList.map((m) => {
            const eff = statusOf(m)
            return (
              <article key={m.id} className="card">
                <p className="card-top"><StatusBadge status={eff.status} /> {m.data_kind === 'synthetic' && <Pill tone="warn">Synthetic data</Pill>} {m.data_kind === 'authentic' && <Pill tone="ok">Authentic data</Pill>}</p>
                <h3><a href={href('lab', m.id)}>{m.title}</a></h3>
                <p>{m.summary}</p>
                <p className="muted small">{m.id} · version {m.version}</p>
              </article>
            )
          })}
        </div>
      </section>

      <section aria-labelledby="start-h">
        <h2 id="start-h">Where to start</h2>
        <ul className="plain">
          <li><a href={href('evidence')}><strong>Evidence explorer</strong></a>: every claim linked to its source location and to the experiment that tried to reproduce it.</li>
          <li><a href={href('compare')}><strong>Comparative governance</strong></a>: the structure for comparing Brazil, Ontario and the Netherlands, filled only with what is supported.</li>
          <li><a href={href('methods')}><strong>Methods and reproducibility</strong></a>: what each status means and how it is earned.</li>
        </ul>
      </section>
    </>
  )
}
