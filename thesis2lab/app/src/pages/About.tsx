import { config } from '../lib/registry'

export function AboutPage() {
  const p = config.project
  return (
    <>
      <h1 tabIndex={-1}>About</h1>
      <section>
        <h2>The project</h2>
        <p>{p.summary}</p>
        <p><strong>Researcher:</strong> {p.researcher}. <strong>Institution:</strong> {p.institution}.</p>
      </section>
      <section>
        <h2>How to cite</h2>
        <p>{p.citation}</p>
        <p className="small muted">Individual figures should cite the experiment id, version and the dataset checksum shown in its reproducibility record.</p>
      </section>
      <section>
        <h2>Open source</h2>
        <p>Thesis2Lab is MIT licensed. Source and documentation: {p.repository_url ? <a href={p.repository_url}>{p.repository_url}</a> : 'in the repository'}. The framework avoids project-specific names so other researchers can adopt it through configuration and experiment manifests.</p>
      </section>
      <section>
        <h2>Disclaimers</h2>
        <p>{p.disclaimer}</p>
        <p>Court-decision data come from public sources and were collected by the researcher. They may include errors, and automated coding is imperfect. Do not cite a number from this site without checking the status label beside it.</p>
      </section>
    </>
  )
}
