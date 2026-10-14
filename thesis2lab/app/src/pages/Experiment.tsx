import { useEffect, useMemo, useState } from 'react'
import { DataTable } from '../charts/Charts'
import { Pill, StatusExplainer } from '../components/Badges'
import { Controls } from '../components/Controls'
import { ReferencePanel, type Comparison } from '../components/ReferencePanel'
import { ValidationPanel } from '../components/ValidationPanel'
import { viewFor } from '../experiments/views'
import { claimVerification, claims, config, experiments, label, loadDataset, methods, references, reports, sources, statusOf } from '../lib/registry'
import { download } from '../lib/download'
import { href } from '../lib/router'
import { toCsv } from '../research/csv'
import { buildRunRecord } from '../research/report'
import { defaultParams, runExperiment } from '../research/runners'
import type { DatasetRecord, Params, ParamValue, Row, RunResult } from '../research/types'

export function ExperimentPage({ id }: { id: string }) {
  const m = experiments[id]
  const [data, setData] = useState<{ rec: DatasetRecord; rows: Row[] } | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [params, setParams] = useState<Params>(() => (m ? defaultParams(m) : {}))
  const [comparisons, setComparisons] = useState<Comparison[]>([])

  useEffect(() => {
    setData(null); setError(null); setComparisons([])
    if (!m) return
    setParams(defaultParams(m))
    if (!m.dataset_ids.length) return
    loadDataset(m.dataset_ids[0]).then(setData).catch((e) => setError(String(e.message ?? e)))
  }, [id])

  const result = useMemo<{ r?: RunResult; err?: string }>(() => {
    if (!m || !m.runner || !data) return {}
    try { return { r: runExperiment(m, data.rows, params) } } catch (e) { return { err: String((e as Error).message) } }
  }, [m, data, params])

  if (!m) return <section><h1 tabIndex={-1}>Experiment not found</h1><p>No experiment with id "{id}" is registered. <a href={href('lab')}>Back to the laboratory</a></p></section>

  const eff = statusOf(m)
  const report = reports[m.id]
  const method = m.method_id ? methods[m.method_id] : undefined
  const View = viewFor(m.runner)
  const canExportData = data?.rec.permitted_uses.includes('export') && m.exports?.includes('filtered_data') && result.r?.selectedRows
  const yearBad = typeof params.year_min === 'number' && typeof params.year_max === 'number' && params.year_min > params.year_max
  const setParam = (pid: string, v: ParamValue) => setParams((p) => ({ ...p, [pid]: v }))
  const record = () => data && result.r && buildRunRecord(m, [data.rec], params, result.r, eff, report, comparisons)
  const stamp = new Date().toISOString().slice(0, 10)

  return (
    <article>
      <p className="crumbs"><a href={href('lab')}>Laboratory</a> / {m.id}</p>
      <h1 tabIndex={-1}>{m.title}</h1>
      {m.ui_notice && <div className="callout warn banner" role="note"><strong>{m.ui_notice}</strong></div>}
      <StatusExplainer eff={eff} />
      {m.status_rationale && <p><strong>Why this status:</strong> {m.status_rationale}</p>}

      <section aria-labelledby="q-h">
        <h2 id="q-h">Research question</h2>
        <p>{m.research_question}</p>
        <p className="muted small">{m.id} · version {m.version} · {m.execution_mode === 'browser' ? 'Mode A: runs entirely in your browser, no AI, no server' : m.execution_mode} · topics: {(m.topics ?? []).map((t) => label(config.labels.topics, t)).join(', ') || 'none'}</p>
      </section>

      {!m.runner ? (
        <section aria-labelledby="blocked-h">
          <h2 id="blocked-h">Why nothing runs</h2>
          <p>This experiment has no executable method yet. The status above explains what is missing.</p>
          {m.unresolved?.length ? <><h3>What is needed to unblock it</h3><ul>{m.unresolved.map((u) => <li key={u}>{u}</li>)}</ul></> : null}
        </section>
      ) : (
        <>
          <section aria-labelledby="in-h">
            <h2 id="in-h">Inputs</h2>
            {error && <div className="callout warn" role="alert">{error}</div>}
            {!data && !error && <p aria-live="polite">Loading dataset…</p>}
            <div className="workspace">
              <div className="panel">
                <Controls m={m} ds={data?.rec} params={params} onChange={setParam} onReset={() => setParams(defaultParams(m))} />
              </div>
              <div className="results" aria-live="polite">
                <h2 id="out-h">Results</h2>
                {yearBad && <div className="callout warn" role="alert">"From year" is later than "To year", so no records can match.</div>}
                {result.err && <div className="callout warn" role="alert">{result.err}</div>}
                {result.r && (
                  <>
                    {result.r.notes.map((n) => <p key={n} className="callout info small">{n}</p>)}
                    <dl className="facts metrics">
                      {Object.entries(result.r.metrics).filter(([k]) => !/^(tp|fp|fn)_/.test(k)).map(([k, v]) => (
                        <div key={k}><dt>{k.replace(/_/g, ' ')}</dt><dd>{v === null ? 'n/a' : typeof v === 'number' ? (Number.isInteger(v) ? v : v.toFixed(4)) : String(v).replace(/_/g, ' ')}</dd></div>
                      ))}
                    </dl>
                    <View m={m} result={result.r} />
                  </>
                )}
              </div>
            </div>
          </section>

          <section aria-labelledby="ref-h">
            <h2 id="ref-h">Comparison with reference outputs</h2>
            {data ? <ReferencePanel m={m} rows={data.rows} refs={references[m.id] ?? []} onResults={setComparisons} /> : <p>Waiting for data.</p>}
          </section>

          <section aria-labelledby="exp-h">
            <h2 id="exp-h">Export</h2>
            <p className="actions">
              {canExportData && <button type="button" className="btn secondary" onClick={() => download(`${m.id}-filtered-${stamp}.csv`, toCsv(result.r!.selectedRows!, data!.rec.variables.map((v) => v.name)), 'text/csv')}>Filtered data (CSV)</button>}
              {m.exports?.includes('results_json') && result.r && <button type="button" className="btn secondary" onClick={() => download(`${m.id}-results-${stamp}.json`, JSON.stringify({ parameters: params, metrics: result.r!.metrics, tables: result.r!.tables }, null, 2), 'application/json')}>Results (JSON)</button>}
              {m.exports?.includes('reproducibility_report') && result.r && <button type="button" className="btn" onClick={() => download(`${m.id}-run-record-${stamp}.json`, JSON.stringify(record(), null, 2), 'application/json')}>Reproducibility record (JSON)</button>}
            </p>
            <p className="small muted">The reproducibility record lists the experiment version, dataset checksum, your parameters, outputs, reference comparisons you ran, and the committed validation summary. It describes this run; it does not itself verify anything.</p>
          </section>
        </>
      )}

      <section aria-labelledby="val-h">
        <h2 id="val-h">Verification record</h2>
        <ValidationPanel report={report} eff={eff} />
      </section>

      <section aria-labelledby="meth-h">
        <h2 id="meth-h">Method</h2>
        {method ? (<><p><strong>{method.title}.</strong> {method.description}</p><h3>Required inputs</h3><ul>{method.required_inputs.map((x) => <li key={x}>{x}</li>)}</ul><h3>Assumptions</h3><ul>{method.assumptions.map((x) => <li key={x}>{x}</li>)}</ul></>) : <p>No method record is linked.</p>}
        <h3>Limitations</h3>
        <ul>{m.limitations.map((x) => <li key={x}>{x}</li>)}</ul>
        {m.unresolved?.length && m.runner ? (<><h3>Unresolved</h3><ul>{m.unresolved.map((x) => <li key={x}>{x}</li>)}</ul></>) : null}
      </section>

      <section aria-labelledby="prov-h">
        <h2 id="prov-h">Evidence and provenance</h2>
        {m.source_ids.length > 0 && (<><h3>Sources</h3><ul>{m.source_ids.map((s) => <li key={s}><a href={href('evidence', s)}>{sources[s]?.title ?? s}</a> <span className="muted small">({sources[s]?.location.ref})</span></li>)}</ul></>)}
        {(m.claim_ids ?? []).length > 0 && (<><h3>Claims tested</h3><ul>{m.claim_ids!.map((c) => { const v = claimVerification(claims[c]); return <li key={c}><a href={href('evidence', c)}>{claims[c]?.text}</a> <Pill tone={v.state === 'reproduced' ? 'ok' : 'warn'}>{v.state.replace('_', ' ')}</Pill></li> })}</ul></>)}
        {data && (
          <>
            <h3>Dataset</h3>
            <dl className="facts">
              <div><dt>Record</dt><dd>{data.rec.id} v{data.rec.version}</dd></div>
              <div><dt>Kind</dt><dd>{data.rec.kind}</dd></div>
              <div><dt>Rows</dt><dd>{data.rows.length}</dd></div>
              <div><dt>Licence</dt><dd>{data.rec.licence}</dd></div>
              <div><dt>Privacy</dt><dd>{data.rec.privacy_status.replace(/_/g, ' ')}</dd></div>
              <div><dt>SHA-256</dt><dd className="mono">{data.rec.checksum_sha256.slice(0, 16)}…</dd></div>
            </dl>
            {data.rec.privacy_notes && <p className="small muted">{data.rec.privacy_notes}</p>}
            <DataTable caption="Variables" columns={['name', 'type', 'description']} rows={data.rec.variables.map((v) => [v.name, v.type, v.description ?? (v.categories ? v.categories.join(', ') : '')])} />
          </>
        )}
      </section>
    </article>
  )
}
