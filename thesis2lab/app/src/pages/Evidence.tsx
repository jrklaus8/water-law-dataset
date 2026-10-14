import { useMemo, useState } from 'react'
import { Pill, StatusBadge } from '../components/Badges'
import { claimVerification, claims, experiments, sources, statusOf, thesis } from '../lib/registry'
import { href } from '../lib/router'

const TONE = { reproduced: 'ok', not_reproduced: 'warn', blocked: 'warn', no_experiment: 'neutral' } as const
const TEXT = { reproduced: 'Numerically reproduced', not_reproduced: 'Not (fully) reproduced', blocked: 'Blocked', no_experiment: 'Not tested' } as const

export function EvidencePage({ focus }: { focus?: string }) {
  const [chapter, setChapter] = useState('')
  const [ver, setVer] = useState('')
  const list = useMemo(() => Object.values(claims).filter((c) => (!chapter || (c.chapter_ids ?? []).includes(chapter)) && (!ver || claimVerification(c).state === ver)), [chapter, ver])
  return (
    <>
      <h1 tabIndex={-1}>Evidence explorer</h1>
      <p className="lead">Each claim is traced to the place in a source where it is made. The reproduction label is computed from validation reports, never typed by hand. Researcher review is a separate step and none has happened yet.</p>
      <form className="filters" onSubmit={(e) => e.preventDefault()} aria-label="Filter claims">
        <div className="field"><label htmlFor="c-ch">Chapter</label><select id="c-ch" value={chapter} onChange={(e) => setChapter(e.target.value)}><option value="">All</option>{thesis.chapters.map((c) => <option key={c.id} value={c.id}>{c.title.replace(/\s*\(.*$/, '')}</option>)}</select></div>
        <div className="field"><label htmlFor="c-v">Reproduction</label><select id="c-v" value={ver} onChange={(e) => setVer(e.target.value)}><option value="">All</option>{Object.entries(TEXT).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</select></div>
      </form>
      <h2>Claims ({list.length})</h2>
      {list.map((c) => {
        const v = claimVerification(c)
        return (
          <article key={c.id} id={c.id} className={`claim${focus === c.id ? ' focus' : ''}`}>
            <p className="card-top"><Pill>{c.id}</Pill> <Pill tone={TONE[v.state]}>{TEXT[v.state]}</Pill> <Pill tone="warn">Researcher review: {c.review_status.replace('_', ' ')}</Pill></p>
            <p className="claim-text">{c.text}</p>
            <p className="small"><strong>Where it is made:</strong> {c.location.locator} (<a href={href('evidence', c.location.source_id)}>{sources[c.location.source_id]?.title}</a>)</p>
            <p className="small muted">{v.detail}</p>
            {c.experiment_ids?.length ? <p className="small">Experiments: {c.experiment_ids.map((e) => <span key={e}><a href={href('lab', e)}>{e}</a> <StatusBadge status={statusOf(experiments[e]).status} /> </span>)}</p> : null}
            {c.limitations?.length ? <details><summary>Limitations ({c.limitations.length})</summary><ul>{c.limitations.map((l) => <li key={l}>{l}</li>)}</ul></details> : null}
          </article>
        )
      })}
      <h2>Sources ({Object.keys(sources).length})</h2>
      {Object.values(sources).map((s) => (
        <article key={s.id} id={s.id} className={`claim${focus === s.id ? ' focus' : ''}`}>
          <p className="card-top"><Pill>{s.id}</Pill> <Pill>{s.kind}</Pill> <Pill tone={s.copyright_status === 'unknown' ? 'warn' : 'neutral'}>copyright: {s.copyright_status.replace(/_/g, ' ')}</Pill> <Pill>extraction: {s.extraction_status.replace(/_/g, ' ')}</Pill></p>
          <h3 className="h4">{s.title}</h3>
          <p className="small">{s.location.type === 'url' ? <a href={s.location.ref}>{s.location.ref}</a> : <>{s.location.repository} · <span className="mono">{s.location.ref}</span></>}{s.location.commit ? <> · commit <span className="mono">{s.location.commit.slice(0, 10)}</span></> : null}</p>
          {s.checksum_sha256 && <p className="small muted mono">sha256 {s.checksum_sha256}</p>}
          {s.extraction_notes && <p className="small">{s.extraction_notes}</p>}
        </article>
      ))}
    </>
  )
}
