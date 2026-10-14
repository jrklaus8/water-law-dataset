import { StatusBadge } from '../components/Badges'
import { DataTable } from '../charts/Charts'
import { experimentList, reports, statusOf } from '../lib/registry'
import { href } from '../lib/router'
import { STATUS_INFO } from '../research/status'
import type { ReproStatus } from '../research/types'

export function MethodsPage() {
  return (
    <>
      <h1 tabIndex={-1}>Methods and reproducibility</h1>
      <p className="lead">How experiments are built, run, checked and limited.</p>
      <section aria-labelledby="modes">
        <h2 id="modes">Three execution modes</h2>
        <dl className="defs">
          <dt>Mode A: browser</dt><dd>Deterministic calculations run on your device. No server, no AI, no account. Every experiment in this release uses Mode A.</dd>
          <dt>Mode B: reproducible workflow</dt><dd>For heavy methods: scripts, pinned dependencies and instructions, checked by continuous integration. Not used yet. Visitors cannot trigger jobs.</dd>
          <dt>Mode C: AI-assisted exploration</dt><dd>Disabled and not built. Experiment manifests that request AI are rejected by the build.</dd>
        </dl>
      </section>
      <section aria-labelledby="status">
        <h2 id="status">What each status means</h2>
        <dl className="defs">{(Object.keys(STATUS_INFO) as ReproStatus[]).map((s) => <><dt key={s}><StatusBadge status={s} /></dt><dd key={s + 'd'}>{STATUS_INFO[s].blurb}</dd></>)}</dl>
        <p>A status is displayed only if a current validation report supports it. If inputs or code change after a report was generated, the report is stale and the experiment drops to Unverified until it is validated again. Charts that merely look similar never count as reproduction.</p>
      </section>
      <section aria-labelledby="verify">
        <h2 id="verify">How verification works</h2>
        <ol>
          <li>The data file's checksum must equal the dataset record.</li>
          <li>The implementation runs on fixed reference scenarios, each with its own tolerance (never one universal tolerance).</li>
          <li>Outputs are compared with a reference: an original published or generated value where one exists, plus an independent Python re-implementation.</li>
          <li>Each scenario runs twice to confirm identical output.</li>
          <li>Where the original code is available, the formula is compared with it.</li>
          <li>A machine-readable report records every check, the data checksums, code commit and tool versions.</li>
        </ol>
        <p>Reports distinguish technical execution, numerical agreement, methodological fidelity and independent review. Independent review is always <em>pending</em> until a named person signs off in the report.</p>
      </section>
      <section aria-labelledby="table">
        <h2 id="table">Current validation summary</h2>
        <DataTable columns={['experiment', 'declared', 'shown', 'checks passed', 'technical', 'numerical', 'fidelity', 'repeatability', 'review']}
          rows={experimentList.map((m) => { const r = reports[m.id]; const e = statusOf(m); return [m.id, m.reproducibility_status, e.status, r ? `${r.summary.checks_passed}/${r.summary.checks_total}` : 'n/a', r?.summary.technical_execution ?? 'n/a', r?.summary.numerical_agreement ?? 'n/a', r?.summary.methodological_fidelity ?? 'n/a', r?.summary.repeatability ?? 'n/a', r?.independent_review.status ?? 'n/a'] })} />
        <p className="small muted">Open an experiment from the <a href={href('lab')}>laboratory</a> to see its individual checks.</p>
      </section>
      <section aria-labelledby="integ">
        <h2 id="integ">Scientific integrity rules</h2>
        <ul>
          <li>Source data are never modified. Imports are read-only copies with checksums.</li>
          <li>Synthetic data are labelled on every screen that uses them and can never be Reproducible.</li>
          <li>AI-written text is not verified scholarship. No AI service runs in this site.</li>
          <li>Court case identifiers are replaced by hashes in the public data to limit identification risk.</li>
        </ul>
      </section>
    </>
  )
}
