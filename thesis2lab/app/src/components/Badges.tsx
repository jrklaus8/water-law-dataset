import { STATUS_INFO, type EffectiveStatus } from '../research/status'
import type { ReproStatus } from '../research/types'

const GLYPH: Record<ReproStatus, string> = { REPRODUCIBLE: '✓', PARTIAL: '◐', AUDITABLE: '◇', EXPLORATORY: '△', BLOCKED: '■', UNVERIFIED: '?' }

export function StatusBadge({ status, large }: { status: ReproStatus; large?: boolean }) {
  return (
    <span className={`badge status-${status.toLowerCase()}${large ? ' large' : ''}`} title={STATUS_INFO[status].blurb}>
      <span aria-hidden="true">{GLYPH[status]}</span> {STATUS_INFO[status].label}
    </span>
  )
}

export function StatusExplainer({ eff }: { eff: EffectiveStatus }) {
  return (
    <div className="status-box">
      <StatusBadge status={eff.status} large />
      <p>{STATUS_INFO[eff.status].blurb}</p>
      {eff.downgraded && (
        <div className="callout warn" role="alert">
          <strong>Shown as {STATUS_INFO[eff.status].label} although the manifest declares {STATUS_INFO[eff.declared].label}.</strong>
          <ul>{eff.reasons.map((r) => <li key={r}>{r}</li>)}</ul>
        </div>
      )}
    </div>
  )
}

export function Pill({ children, tone = 'neutral' }: { children: React.ReactNode; tone?: 'neutral' | 'warn' | 'ok' | 'info' }) {
  return <span className={`pill ${tone}`}>{children}</span>
}
