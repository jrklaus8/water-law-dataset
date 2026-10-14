import { config } from '../lib/registry'
import { href } from '../lib/router'

export function CoverPage() {
  const c = config.cover
  if (!c) return <section><h1 tabIndex={-1}>Read first</h1><p>No cover text is configured. Add a <span className="mono">cover</span> block to project.config.json.</p></section>
  return (
    <article className="cover">
      <p className="eyebrow">{config.project.title} · Thesis2Lab</p>
      <h1 tabIndex={-1}>{c.title}</h1>
      <p className="lead">{c.lead}</p>
      {c.sections.map((s) => (
        <section key={s.heading} aria-labelledby={`cv-${s.heading.replace(/\W+/g, '-')}`}>
          <h2 id={`cv-${s.heading.replace(/\W+/g, '-')}`}>{s.heading}</h2>
          {s.body.map((t) => <p key={t}>{t}</p>)}
          {s.bullets?.length ? <ul>{s.bullets.map((b) => <li key={b}>{b}</li>)}</ul> : null}
        </section>
      ))}
      {c.disclosure && <p className="callout info small">{c.disclosure}</p>}
      <p className="actions">
        <a className="btn" href={href('lab')}>Open the laboratory</a>
        <a className="btn secondary" href={href('methods')}>How verification works</a>
        <button type="button" className="btn secondary" onClick={() => window.print()}>Print this page</button>
      </p>
    </article>
  )
}
