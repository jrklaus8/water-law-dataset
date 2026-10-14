import { runAgreement, type AgreementConfig } from './agreement'
import { runDescriptive, type DescriptiveConfig } from './descriptive'
import type { ExperimentManifest, Params, Row, RunResult } from './types'

/** Computation runners. A new experiment of an existing type needs only a manifest and data. */
export const RUNNERS: Record<string, (rows: Row[], params: Params, cfg: Record<string, unknown>) => RunResult> = {
  descriptive_table: (rows, params, cfg) => runDescriptive(rows, params, cfg as unknown as DescriptiveConfig),
  coder_agreement: (rows, params, cfg) => runAgreement(rows, params, cfg as unknown as AgreementConfig),
}

export function runExperiment(m: ExperimentManifest, rows: Row[], params: Params): RunResult {
  if (!m.runner) throw new Error(`${m.id} has no runner (status ${m.reproducibility_status})`)
  const fn = RUNNERS[m.runner]
  if (!fn) throw new Error(`Unknown runner "${m.runner}" in ${m.id}`)
  return fn(rows, params, m.runner_config ?? {})
}

export function defaultParams(m: ExperimentManifest): Params {
  const p: Params = {}
  for (const d of m.parameters) if (d.default !== undefined) p[d.id] = d.default
  return p
}
