import type { DatasetRecord, ExperimentManifest, ParamDef, Params, ParamValue } from '../research/types'

function optionsFor(d: ParamDef, ds?: DatasetRecord) {
  if (d.options) return d.options
  const v = ds?.variables.find((x) => x.name === d.options_from_variable)
  return (v?.categories ?? []).map((c) => ({ value: c, label: c.replace(/_/g, ' ') }))
}

export function Controls({ m, ds, params, onChange, onReset }: { m: ExperimentManifest; ds?: DatasetRecord; params: Params; onChange: (id: string, v: ParamValue) => void; onReset: () => void }) {
  return (
    <form className="controls" onSubmit={(e) => e.preventDefault()} aria-label="Experiment parameters">
      {m.parameters.map((d) => {
        const fid = `${m.id}-${d.id}`
        const help = d.help ? <p className="help" id={`${fid}-h`}>{d.help}</p> : null
        const describedBy = d.help ? `${fid}-h` : undefined
        if (d.type === 'range') {
          return (
            <div className="field" key={d.id}>
              <label htmlFor={fid}>{d.label}: <output htmlFor={fid}>{String(params[d.id])}</output></label>
              <input id={fid} type="range" min={d.min} max={d.max} step={d.step ?? 1} value={Number(params[d.id])} aria-describedby={describedBy} onChange={(e) => onChange(d.id, Number(e.target.value))} />
              {help}
            </div>
          )
        }
        if (d.type === 'select') {
          return (
            <div className="field" key={d.id}>
              <label htmlFor={fid}>{d.label}</label>
              <select id={fid} value={String(params[d.id])} aria-describedby={describedBy} onChange={(e) => onChange(d.id, e.target.value)}>
                {optionsFor(d, ds).map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}
              </select>
              {help}
            </div>
          )
        }
        if (d.type === 'toggle') {
          return (
            <div className="field check" key={d.id}>
              <label><input type="checkbox" checked={Boolean(params[d.id])} onChange={(e) => onChange(d.id, e.target.checked)} /> {d.label}</label>
              {help}
            </div>
          )
        }
        const selected = (params[d.id] as string[]) ?? []
        return (
          <fieldset className="field" key={d.id} aria-describedby={describedBy}>
            <legend>{d.label}{selected.length === 0 ? <span className="muted"> (all)</span> : null}</legend>
            <div className="checks">
              {optionsFor(d, ds).map((o) => (
                <label key={o.value} className="check">
                  <input type="checkbox" checked={selected.includes(o.value)} onChange={(e) => onChange(d.id, e.target.checked ? [...selected, o.value] : selected.filter((x) => x !== o.value))} /> {o.label}
                </label>
              ))}
            </div>
            {help}
          </fieldset>
        )
      })}
      <button type="button" className="btn secondary" onClick={onReset}>Reset to defaults</button>
    </form>
  )
}
