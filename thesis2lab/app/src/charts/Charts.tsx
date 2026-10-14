import { useId, useState } from 'react'

const fmt = (v: number) => (Number.isInteger(v) ? String(v) : v.toFixed(3))

export interface Point { label: string; value: number }

/** Accessible column chart: SVG with a text description and a data-table alternative. */
export function ColumnChart({ title, points, xLabel, yLabel }: { title: string; points: Point[]; xLabel: string; yLabel: string }) {
  const id = useId()
  const [asTable, setAsTable] = useState(false)
  if (!points.length) return <p className="muted">Nothing to chart for the current selection.</p>
  const W = 640, H = 240, L = 44, B = 34, T = 10, R = 8
  const max = Math.max(...points.map((p) => p.value), 1)
  const bw = (W - L - R) / points.length
  const every = Math.ceil(points.length / 12)
  const ticks = [0, Math.round(max / 2), max]
  const summary = `${title}. ${points.length} ${xLabel} values from ${points[0].label} to ${points[points.length - 1].label}. Highest ${yLabel}: ${max}.`
  return (
    <figure className="chart">
      <figcaption id={`${id}-t`}>{title}</figcaption>
      {asTable ? <DataTable columns={[xLabel, yLabel]} rows={points.map((p) => [p.label, p.value])} /> : (
        <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-labelledby={`${id}-t ${id}-d`}>
          <desc id={`${id}-d`}>{summary}</desc>
          {ticks.map((t) => {
            const y = T + (H - T - B) * (1 - t / max)
            return <g key={t}><line x1={L} x2={W - R} y1={y} y2={y} className="grid" /><text x={L - 6} y={y + 4} textAnchor="end" className="tick">{t}</text></g>
          })}
          {points.map((p, i) => {
            const h = (H - T - B) * (p.value / max)
            return (
              <g key={p.label}>
                <rect x={L + i * bw + 1} y={H - B - h} width={Math.max(bw - 2, 1)} height={h} className="bar"><title>{`${p.label}: ${p.value}`}</title></rect>
                {i % every === 0 && <text x={L + i * bw + bw / 2} y={H - B + 16} textAnchor="middle" className="tick">{p.label}</text>}
              </g>
            )
          })}
          <text x={W / 2} y={H - 2} textAnchor="middle" className="axis">{xLabel}</text>
        </svg>
      )}
      <button type="button" className="link-button" onClick={() => setAsTable(!asTable)} aria-pressed={asTable}>{asTable ? 'Show chart' : 'View as table'}</button>
    </figure>
  )
}

/** Horizontal bars with the value written next to each bar (no information carried by colour alone). */
export function BarList({ title, points, total }: { title: string; points: Point[]; total?: number }) {
  const max = Math.max(...points.map((p) => p.value), 1)
  return (
    <figure className="chart">
      <figcaption>{title}</figcaption>
      {points.length === 0 ? <p className="muted">No records.</p> : (
        <ul className="barlist">
          {points.map((p) => (
            <li key={p.label}>
              <span className="barlist-label">{p.label.replace(/_/g, ' ')}</span>
              <span className="barlist-track" aria-hidden="true"><span style={{ width: `${(p.value / max) * 100}%` }} /></span>
              <span className="barlist-value">{p.value}{total ? ` (${((p.value / total) * 100).toFixed(1)}%)` : ''}</span>
            </li>
          ))}
        </ul>
      )}
    </figure>
  )
}

/** A value on a 0 to 1 scale with an optional interval. */
export function IntervalPlot({ title, value, low, high, min = -0.2, max = 1 }: { title: string; value: number | null; low: number | null; high: number | null; min?: number; max?: number }) {
  const id = useId()
  if (value === null) return <p className="muted">Not defined for this selection.</p>
  const W = 640, H = 80, L = 20, R = 20
  const x = (v: number) => L + ((v - min) / (max - min)) * (W - L - R)
  const desc = `${title}: estimate ${fmt(value)}${low !== null && high !== null ? `, 95% bootstrap interval ${fmt(low)} to ${fmt(high)}` : ', no interval computed'}.`
  const ticks = [0, 0.2, 0.4, 0.6, 0.8, 1]
  return (
    <figure className="chart">
      <figcaption id={`${id}-t`}>{title}</figcaption>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-labelledby={`${id}-t ${id}-d`}>
        <desc id={`${id}-d`}>{desc}</desc>
        <line x1={x(min)} x2={x(max)} y1={36} y2={36} className="axisline" />
        {ticks.map((t) => <g key={t}><line x1={x(t)} x2={x(t)} y1={32} y2={40} className="axisline" /><text x={x(t)} y={58} textAnchor="middle" className="tick">{t}</text></g>)}
        {low !== null && high !== null && <rect x={x(low)} y={30} width={Math.max(x(high) - x(low), 1)} height={12} className="ci"><title>{`95% interval ${fmt(low)} to ${fmt(high)}`}</title></rect>}
        <circle cx={x(value)} cy={36} r={7} className="point"><title>{`estimate ${fmt(value)}`}</title></circle>
        <text x={x(value)} y={20} textAnchor="middle" className="axis">{fmt(value)}</text>
      </svg>
    </figure>
  )
}

export function DataTable({ columns, rows, caption }: { columns: string[]; rows: (string | number | null)[][]; caption?: string }) {
  return (
    <div className="table-wrap" tabIndex={0} role="region" aria-label={caption ?? 'Data table'}>
      <table>
        {caption && <caption>{caption}</caption>}
        <thead><tr>{columns.map((c) => <th key={c} scope="col">{c.replace(/_/g, ' ')}</th>)}</tr></thead>
        <tbody>{rows.map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j} className={typeof c === 'number' ? 'num' : undefined}>{c === null ? 'n/a' : typeof c === 'number' ? fmt(c) : String(c).replace(/_/g, ' ')}</td>)}</tr>)}</tbody>
      </table>
    </div>
  )
}
