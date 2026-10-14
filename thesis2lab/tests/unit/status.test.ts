import { describe, expect, it } from 'vitest'
import { effectiveStatus } from '../../app/src/research/status'
import type { ExperimentManifest, ReproStatus, ValidationCheck, ValidationReport } from '../../app/src/research/types'

const manifest = (status: ReproStatus): ExperimentManifest => ({
  id: 'EXP-900', title: 't', version: '1.0.0', research_question: 'q', source_ids: [], method_id: null, dataset_ids: [], runner: 'x',
  execution_mode: 'browser', reproducibility_status: status, parameters: [], reference_outputs: [], validation_rules: [], limitations: [], requires_ai: false,
})
const check = (over: Partial<ValidationCheck> = {}): ValidationCheck => ({ id: 'c', kind: 'numerical', description: 'd', pass: true, required: true, reference_kind: 'original', ...over })
const report = (status: ReproStatus, over: Partial<ValidationReport> = {}, checks: ValidationCheck[] = [check()]): ValidationReport => ({
  schema_version: '1.0', experiment_id: 'EXP-900', experiment_version: '1.0.0', declared_status: status, inputs_digest: 'd1', code_version: { git_commit: null },
  dependency_versions: {}, dataset_checksums: {}, checks,
  summary: { technical_execution: 'pass', numerical_agreement: 'pass', methodological_fidelity: 'pass', repeatability: 'pass', checks_total: checks.length, checks_passed: checks.length, overall: 'pass' },
  independent_review: { status: 'pending' }, remaining_uncertainty: [], generated_at: 'now', ...over,
})

describe('effectiveStatus: the interface never claims more than the evidence', () => {
  it('REPRODUCIBLE with a full passing original comparison is shown', () => {
    expect(effectiveStatus(manifest('REPRODUCIBLE'), report('REPRODUCIBLE'), 'd1').status).toBe('REPRODUCIBLE')
  })
  it('REPRODUCIBLE without a report is downgraded', () => {
    const e = effectiveStatus(manifest('REPRODUCIBLE'), undefined, 'd1')
    expect(e.status).toBe('UNVERIFIED')
    expect(e.downgraded).toBe(true)
  })
  it('a stale report (inputs changed) downgrades', () => {
    expect(effectiveStatus(manifest('REPRODUCIBLE'), report('REPRODUCIBLE'), 'other').status).toBe('UNVERIFIED')
  })
  it('a failed required check downgrades', () => {
    const bad = report('REPRODUCIBLE', { summary: { ...report('REPRODUCIBLE').summary, overall: 'fail', numerical_agreement: 'fail' } })
    expect(effectiveStatus(manifest('REPRODUCIBLE'), bad, 'd1').status).toBe('UNVERIFIED')
  })
  it('running without error is not reproduction: only independent re-implementation does not qualify', () => {
    const r = report('REPRODUCIBLE', {}, [check({ reference_kind: 'independent_reimplementation' })])
    expect(effectiveStatus(manifest('REPRODUCIBLE'), r, 'd1').status).toBe('UNVERIFIED')
  })
  it('REPRODUCIBLE needs methodological fidelity', () => {
    const r = report('REPRODUCIBLE', { summary: { ...report('REPRODUCIBLE').summary, methodological_fidelity: 'not_assessed' } })
    expect(effectiveStatus(manifest('REPRODUCIBLE'), r, 'd1').status).toBe('UNVERIFIED')
  })
  it('PARTIAL needs at least one original output reproduced', () => {
    expect(effectiveStatus(manifest('PARTIAL'), report('PARTIAL'), 'd1').status).toBe('PARTIAL')
    expect(effectiveStatus(manifest('PARTIAL'), report('PARTIAL', {}, [check({ reference_kind: 'independent_reimplementation' })]), 'd1').status).toBe('UNVERIFIED')
  })
  it('EXPLORATORY is shown only with a passing report', () => {
    expect(effectiveStatus(manifest('EXPLORATORY'), report('EXPLORATORY', {}, [check({ reference_kind: 'independent_reimplementation' })]), 'd1').status).toBe('EXPLORATORY')
    expect(effectiveStatus(manifest('EXPLORATORY'), undefined, 'd1').status).toBe('UNVERIFIED')
  })
  it('BLOCKED and AUDITABLE need no computation and are shown as declared', () => {
    expect(effectiveStatus(manifest('BLOCKED'), undefined, undefined).status).toBe('BLOCKED')
    expect(effectiveStatus(manifest('AUDITABLE'), undefined, undefined).status).toBe('AUDITABLE')
  })
})
