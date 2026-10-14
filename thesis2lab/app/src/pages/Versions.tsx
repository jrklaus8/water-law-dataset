import { experimentList, releases, reports, thesis } from '../lib/registry'

export function VersionsPage() {
  return (
    <>
      <h1 tabIndex={-1}>Versions and releases</h1>
      <p className="lead">A release freezes the thesis version, dataset versions, experiment versions and code commit together, so any published figure can be traced back.</p>
      {releases.length === 0 ? <div className="callout info"><p>No release has been prepared yet. Run <span className="mono">npm run release:prepare</span> to draft one. Releases stay <em>draft</em> until a researcher approves them.</p></div> : releases.map((r) => (
        <article key={r.id} className="claim">
          <h2 className="h3">{r.id} <span className="pill neutral">{r.status}</span></h2>
          <p className="small">Thesis version {r.thesis_version}. Released {r.release_date}. Code commit {r.code_commit?.slice(0, 10) ?? 'not recorded'}. Approved by: {r.approved_by ?? 'nobody yet'}.</p>
          <p className="small">Experiments: {Object.entries(r.experiment_versions).map(([k, v]) => `${k}@${v}`).join(', ')}. Datasets: {Object.entries(r.dataset_versions).map(([k, v]) => `${k}@${v}`).join(', ')}.</p>
          {r.notes?.length ? <ul>{r.notes.map((n) => <li key={n}>{n}</li>)}</ul> : null}
        </article>
      ))}
      <h2>Current versions</h2>
      <ul>
        <li>Thesis record: {thesis.version} ({thesis.research_status})</li>
        {experimentList.map((m) => <li key={m.id}>{m.id} version {m.version}{reports[m.id] ? `, last validated ${reports[m.id].generated_at.slice(0, 10)}` : ', no validation run'}</li>)}
      </ul>
    </>
  )
}
