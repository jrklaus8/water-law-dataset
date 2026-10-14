import type { ComparisonRow } from './compare'
import type { DatasetRecord, ExperimentManifest, Params, RunResult, ValidationReport } from './types'
import type { EffectiveStatus } from './status'

export interface ReproReport {
  schema: 'thesis2lab.run-record/1'
  generated_in_browser_at: string
  experiment: { id: string; version: string; title: string; declared_status: string; shown_status: string; status_reasons: string[]; data_kind?: string }
  datasets: { id: string; version: string; kind: string; checksum_sha256: string; licence: string; path: string }[]
  parameters: Params
  metrics: RunResult['metrics']
  reference_comparison: { scenario: string; rows: ComparisonRow[] }[]
  committed_validation: null | {
    inputs_digest: string; generated_at: string; code_version: ValidationReport['code_version']; summary: ValidationReport['summary']
    independent_review: ValidationReport['independent_review']; remaining_uncertainty: string[]
  }
  limitations: string[]
  notice: string
}

/** Record of one in-browser run. It documents what was run; it is not itself a validation. */
export function buildRunRecord(m: ExperimentManifest, datasets: DatasetRecord[], params: Params, result: RunResult, eff: EffectiveStatus,
  report: ValidationReport | undefined, comparisons: { scenario: string; rows: ComparisonRow[] }[], now = new Date()): ReproReport {
  return {
    schema: 'thesis2lab.run-record/1',
    generated_in_browser_at: now.toISOString(),
    experiment: { id: m.id, version: m.version, title: m.title, declared_status: eff.declared, shown_status: eff.status, status_reasons: eff.reasons, data_kind: m.data_kind },
    datasets: datasets.map((d) => ({ id: d.id, version: d.version, kind: d.kind, checksum_sha256: d.checksum_sha256, licence: d.licence, path: d.path })),
    parameters: params,
    metrics: result.metrics,
    reference_comparison: comparisons,
    committed_validation: report ? {
      inputs_digest: report.inputs_digest, generated_at: report.generated_at, code_version: report.code_version, summary: report.summary,
      independent_review: report.independent_review, remaining_uncertainty: report.remaining_uncertainty,
    } : null,
    limitations: m.limitations,
    notice: 'This record documents one in-browser run with the parameters above. Verification status comes only from the committed validation report. Synthetic or exploratory results are not research findings.',
  }
}
