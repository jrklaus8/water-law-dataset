import { useMemo, useState } from 'react'
import { Pill, StatusBadge } from '../components/Badges'
import { config, experimentList, label, methods, statusOf, thesis } from '../lib/registry'
import { href } from '../lib/router'
import { STATUS_INFO } from '../research/status'
import type { ReproStatus } from '../research/types'

type Filters = { status: string; method: string; chapter: string; topic: string; jurisdiction: string }

export function LabPage() {
  const [f, setF] = useState<Filters>({ status: '', method: '', chapter: '', topic: '', jurisdiction: '' })
  const upd = (k: keyof Filters) => (e: React.ChangeEvent<HTMLSelectElement>) => setF({ ...f, [k]: e.target.value })
  const shown = useMemo(() => experimentList.filter((m) =>
    (!f.status || statusOf(m).status === f.status) &&
    (!f.method || (m.method_tags ?? []).includes(f.method)) &&
    (!f.chapter || (m.chapter_ids ?? []).includes(f.chapter)) &&
    (!f.topic || (m.topics ?? []).includes(f.topic)) &&
    (!f.jurisdiction || (m.jurisdictions ?? []).includes(f.jurisdiction))), [f])
  const uniq = (g: (m: (typeof experimentList)[number]) => string[]) => [...new Set(experimentList.flatMap(g))].sort()
  const Sel = ({ k, name, opts }: { k: keyof Filters; name: string; opts: { value: string; label: string }[] }) => (
    <div className="field"><label htmlFor={`f-${k}`}>{name}</label>
      <select id={`f-${k}`} value={f[k]} onChange={upd(k)}><option value="">All</option>{opts.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select></div>
  )
  return (
    <>
      <h1 tabIndex={-1}>Research laboratory</h1>
      <p className="lead">Every experiment found in the repository, with the status the evidence currently supports.</p>
      <form className="filters" aria-label="Filter experiments" onSubmit={(e) => e.preventDefault()}>
        <Sel k="status" name="Status" opts={(Object.keys(STATUS_INFO) as ReproStatus[]).map((s) => ({ value: s, label: STATUS_INFO[s].label }))} />
        <Sel k="method" name="Method" opts={uniq((m) => m.method_tags ?? []).map((v) => ({ value: v, label: v }))} />
        <Sel k="chapter" name="Chapter" opts={thesis.chapters.map((c) => ({ value: c.id, label: c.title.replace(/\s*\(.*$/, '') }))} />
        <Sel k="topic" name="Topic" opts={uniq((m) => m.topics ?? []).map((v) => ({ value: v, label: label(config.labels.topics, v) }))} />
        <Sel k="jurisdiction" name="Jurisdiction" opts={uniq((m) => m.jurisdictions ?? []).map((v) => ({ value: v, label: label(config.labels.jurisdictions, v) }))} />
      </form>
      <p aria-live="polite" className="muted">{shown.length} of {experimentList.length} experiments shown.</p>
      <div className="cards">
        {shown.map((m) => {
          const eff = statusOf(m)
          return (
            <article key={m.id} className="card">
              <p className="card-top"><StatusBadge status={eff.status} /> {m.data_kind === 'synthetic' && <Pill tone="warn">Synthetic data</Pill>} {m.data_kind === 'authentic' && <Pill tone="ok">Authentic data</Pill>} <Pill>{m.execution_mode === 'browser' ? 'Runs in browser' : m.execution_mode}</Pill></p>
              <h2 className="h3"><a href={href('lab', m.id)}>{m.title}</a></h2>
              <p>{m.research_question}</p>
              <p className="muted small">{m.id} · {m.method_id ? methods[m.method_id]?.title : 'no method record'}</p>
            </article>
          )
        })}
      </div>
    </>
  )
}
