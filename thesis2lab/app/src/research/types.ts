export type ReproStatus = 'REPRODUCIBLE' | 'PARTIAL' | 'AUDITABLE' | 'EXPLORATORY' | 'BLOCKED' | 'UNVERIFIED'

export type Row = Record<string, string | number>
export type ParamValue = string | number | boolean | string[]
export type Params = Record<string, ParamValue>

export interface ParamDef {
  id: string
  label: string
  type: 'range' | 'select' | 'multiselect' | 'toggle'
  help?: string
  variable?: string
  min?: number
  max?: number
  step?: number
  options?: { value: string; label: string }[]
  options_from_variable?: string
  default?: ParamValue
}

export interface DatasetVariable {
  name: string
  type: 'string' | 'integer' | 'number' | 'category' | 'boolean'
  description?: string
  categories?: string[]
}

export interface DatasetRecord {
  id: string
  title: string
  version: string
  kind: 'authentic' | 'synthetic'
  checksum_sha256: string
  path: string
  row_count?: number
  licence: string
  privacy_status: string
  privacy_notes?: string
  permitted_uses: string[]
  variables: DatasetVariable[]
  provenance: Record<string, unknown>
}

export interface ExperimentManifest {
  id: string
  title: string
  version: string
  summary?: string
  research_question: string
  source_ids: string[]
  method_id: string | null
  dataset_ids: string[]
  runner: string | null
  runner_config?: Record<string, unknown>
  execution_mode: 'browser' | 'workflow' | 'ai_assisted'
  reproducibility_status: ReproStatus
  status_rationale?: string
  data_kind?: 'authentic' | 'synthetic' | 'none'
  chapter_ids?: string[]
  claim_ids?: string[]
  topics?: string[]
  jurisdictions?: string[]
  method_tags?: string[]
  parameters: ParamDef[]
  reference_outputs: string[]
  validation_rules: { id: string; kind: string; description: string; tolerance?: Record<string, unknown> }[]
  limitations: string[]
  unresolved?: string[]
  requires_ai: boolean
  exports?: ('filtered_data' | 'results_json' | 'reproducibility_report')[]
  ui_notice?: string
}

export interface TableResult {
  id: string
  title: string
  columns: string[]
  rows: (string | number | null)[][]
}

export interface RunResult {
  /** Scalar outputs compared against reference outputs. */
  metrics: Record<string, number | string | null>
  /** Tables shown to the reader and exported. */
  tables: TableResult[]
  /** Rows retained by the filters (for export). */
  selectedRows?: Row[]
  notes: string[]
}

export interface ReferenceCase {
  id: string
  description: string
  parameters: Params
  expected: Record<string, number | string>
  tolerance: Record<string, number> & { default?: number }
  required?: boolean
  claim_id?: string
  provenance: { kind: 'original' | 'original_published' | 'independent_reimplementation'; source: string; note?: string }
}

export interface ReferenceFile {
  experiment_id: string
  cases: ReferenceCase[]
}

export interface ValidationCheck {
  id: string
  kind: 'technical' | 'numerical' | 'methodological' | 'repeatability' | 'sanity'
  description: string
  pass: boolean
  required?: boolean
  reference_kind?: string
  claim_id?: string
  expected?: unknown
  actual?: unknown
  tolerance?: unknown
  difference?: unknown
}

export interface ValidationReport {
  schema_version: '1.0'
  experiment_id: string
  experiment_version: string
  declared_status: ReproStatus
  inputs_digest: string
  code_version: { git_commit: string | null; working_tree_dirty?: boolean; note?: string }
  dependency_versions: Record<string, string>
  dataset_checksums: Record<string, string>
  checks: ValidationCheck[]
  summary: {
    technical_execution: 'pass' | 'fail' | 'not_applicable'
    numerical_agreement: 'pass' | 'fail' | 'not_applicable'
    methodological_fidelity: 'pass' | 'fail' | 'not_assessed' | 'not_applicable'
    repeatability: 'pass' | 'fail' | 'not_applicable'
    checks_total: number
    checks_passed: number
    overall: 'pass' | 'fail' | 'not_applicable'
  }
  independent_review: { status: 'pending' | 'completed'; reviewer?: string; date?: string; note?: string }
  remaining_uncertainty: string[]
  generated_at: string
}
