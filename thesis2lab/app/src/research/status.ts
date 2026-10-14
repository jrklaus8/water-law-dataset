import type { ExperimentManifest, ReproStatus, ValidationReport } from './types'

export const STATUS_INFO: Record<ReproStatus, { label: string; blurb: string }> = {
  REPRODUCIBLE: { label: 'Reproducible', blurb: 'The original computational result was reproduced within documented acceptance criteria.' },
  PARTIAL: { label: 'Partially reproduced', blurb: 'Some original outputs were reproduced, but important elements remain unresolved.' },
  AUDITABLE: { label: 'Auditable', blurb: 'Evidence and procedures can be inspected, but full computational reproduction is unavailable.' },
  EXPLORATORY: { label: 'Exploratory', blurb: 'An independent simulation or scenario explorer. It is not a reproduction of original findings.' },
  BLOCKED: { label: 'Blocked', blurb: 'Required evidence, permissions, data, code or methodological detail is missing.' },
  UNVERIFIED: { label: 'Unverified', blurb: 'An implementation exists but verification has not been completed (or no longer holds).' },
}

export interface EffectiveStatus {
  /** What the interface is allowed to display. Never stronger than the evidence. */
  status: ReproStatus
  declared: ReproStatus
  downgraded: boolean
  reasons: string[]
}

const requiredChecks = (r: ValidationReport) => r.checks.filter((c) => c.required !== false)

/**
 * The only place the interface decides which status to show. A declared status that needs
 * computational evidence (REPRODUCIBLE, PARTIAL, EXPLORATORY) is shown only when a current,
 * passing validation report supports it. Otherwise it is downgraded to UNVERIFIED.
 */
export function effectiveStatus(m: ExperimentManifest, report: ValidationReport | undefined, currentDigest: string | undefined): EffectiveStatus {
  const declared = m.reproducibility_status
  const out = (status: ReproStatus, reasons: string[] = []): EffectiveStatus => ({ status, declared, downgraded: status !== declared, reasons })

  if (declared === 'BLOCKED' || declared === 'AUDITABLE') return out(declared)
  if (declared === 'UNVERIFIED') return out('UNVERIFIED', report ? [] : ['No validation report exists.'])

  const reasons: string[] = []
  if (!report) reasons.push('No validation report exists for this experiment.')
  else {
    if (report.experiment_id !== m.id || report.experiment_version !== m.version) reasons.push('The validation report is for a different experiment version.')
    if (!currentDigest || report.inputs_digest !== currentDigest) reasons.push('Inputs or code changed since the validation report was generated (stale report).')
    if (report.declared_status !== declared) reasons.push('The report was generated for a different declared status.')
    if (report.summary.overall !== 'pass') reasons.push('One or more required validation checks failed.')
    if (report.summary.technical_execution !== 'pass') reasons.push('Technical execution did not pass.')
    if (report.summary.repeatability !== 'pass') reasons.push('Repeatability did not pass.')

    const originalNumeric = requiredChecks(report).filter((c) => c.kind === 'numerical' && c.reference_kind?.startsWith('original'))
    if (declared === 'REPRODUCIBLE') {
      if (originalNumeric.length === 0) reasons.push('No numerical comparison against an original reference output exists.')
      if (report.summary.numerical_agreement !== 'pass') reasons.push('Numerical agreement with the reference did not pass.')
      if (report.summary.methodological_fidelity !== 'pass') reasons.push('Methodological fidelity has not been confirmed.')
    }
    if (declared === 'PARTIAL' && !originalNumeric.some((c) => c.pass)) reasons.push('No original output was numerically reproduced.')
  }
  return reasons.length ? out('UNVERIFIED', reasons) : out(declared)
}
