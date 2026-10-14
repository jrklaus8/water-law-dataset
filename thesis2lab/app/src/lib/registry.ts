/**
 * Discovers every research object from the repository files at build time.
 * Nothing about experiments, chapters or jurisdictions is hardcoded here:
 * adding a folder under experiments/ with a valid manifest adds it to the site.
 */
import { loadRows } from '../research/csv'
import type { DatasetRecord, ExperimentManifest, ReferenceFile, Row, ValidationReport } from '../research/types'
import { effectiveStatus, type EffectiveStatus } from '../research/status'
import digests from '../generated/digests.json'

const eager = <T,>(g: Record<string, unknown>): T[] => Object.values(g) as T[]
const byId = <T extends { id: string }>(xs: T[]) => Object.fromEntries(xs.map((x) => [x.id, x])) as Record<string, T>

export interface ProjectConfig {
  project: { id: string; title: string; subtitle?: string; researcher: string; institution: string; status: string; summary?: string; repository_url?: string; citation?: string; disclaimer?: string }
  labels: { jurisdictions: Record<string, string>; topics: Record<string, string>; governance_categories?: Record<string, string> }
}
export interface Chapter { id: string; title: string; status: string; research_questions?: string[]; claim_ids?: string[]; experiment_ids?: string[]; source_ids?: string[] }
export interface Thesis { id: string; title: string; institution: string; research_status: string; version: string; authors: string[]; notes?: string; chapters: Chapter[]; source_ids?: string[] }
export interface Source { id: string; title: string; kind: string; location: { type: string; ref: string; repository?: string; commit?: string }; copyright_status: string; licence?: string; checksum_sha256: string | null; extraction_status: string; extraction_notes?: string; format?: string }
export interface Claim { id: string; text: string; claim_type: string; source_ids: string[]; location: { source_id: string; locator: string }; chapter_ids?: string[]; experiment_ids?: string[]; review_status: string; limitations?: string[]; notes?: string }
export interface Method { id: string; title: string; description: string; required_inputs: string[]; assumptions: string[]; execution_environment: string; associated_outputs?: string[] }
export interface GovEvidence { id: string; jurisdiction: string; category: string; statement: string; evidence_type: string; source_id: string; locator: string; review_status: string; caveat?: string }
export interface Release { id: string; thesis_version: string; dataset_versions: Record<string, string>; experiment_versions: Record<string, string>; code_commit: string | null; release_date: string; status: string; notes?: string[]; approved_by?: string | null }

const one = <T,>(g: Record<string, unknown>): T => Object.values(g)[0] as T

export const config = one<ProjectConfig>(import.meta.glob('../../../project.config.json', { eager: true, import: 'default' }))
export const thesis = one<Thesis>(import.meta.glob('../../../research/thesis/thesis.json', { eager: true, import: 'default' }))
export const sources = byId(eager<Source>(import.meta.glob('../../../research/sources/*.json', { eager: true, import: 'default' })))
export const claims = byId(eager<Claim>(import.meta.glob('../../../research/claims/*.json', { eager: true, import: 'default' })))
export const methods = byId(eager<Method>(import.meta.glob('../../../research/methods/*.json', { eager: true, import: 'default' })))
export const governance = eager<GovEvidence>(import.meta.glob('../../../research/governance/*.json', { eager: true, import: 'default' }))
export const releases = eager<Release>(import.meta.glob('../../../research/manifests/*.json', { eager: true, import: 'default' }))
export const datasets = byId(eager<DatasetRecord>(import.meta.glob('../../../data/metadata/*.json', { eager: true, import: 'default' })))
export const experiments = byId(eager<ExperimentManifest>(import.meta.glob('../../../experiments/*/manifest.json', { eager: true, import: 'default' })))
const reportList = eager<ValidationReport & { id: string }>(Object.fromEntries(Object.entries(import.meta.glob('../../../validation/reports/*.json', { eager: true, import: 'default' })).map(([k, v]) => [k, { ...(v as object), id: (v as ValidationReport).experiment_id }])))
export const reports = byId(reportList) as Record<string, ValidationReport>
const refList = Object.entries(import.meta.glob('../../../experiments/*/references/*.json', { eager: true, import: 'default' })).map(([, v]) => v as ReferenceFile & { id: string })
export const references: Record<string, ReferenceFile[]> = {}
refList.forEach((r) => { (references[r.experiment_id] ??= []).push(r) })

const csvFiles = import.meta.glob('../../../data/{public,synthetic}/*.csv', { query: '?raw', import: 'default' }) as Record<string, () => Promise<string>>

export async function loadDataset(id: string): Promise<{ rec: DatasetRecord; rows: Row[] }> {
  const rec = datasets[id]
  if (!rec) throw new Error(`Unknown dataset ${id}`)
  const loader = csvFiles['../../../' + rec.path]
  if (!loader) throw new Error(`Data file for ${id} is not bundled (${rec.path})`)
  return { rec, rows: loadRows(await loader(), rec.variables) }
}

export const experimentList = Object.values(experiments).sort((a, b) => a.id.localeCompare(b.id))
export const statusOf = (m: ExperimentManifest): EffectiveStatus => effectiveStatus(m, reports[m.id], (digests as Record<string, string>)[m.id])

export const label = (map: Record<string, string> | undefined, key: string) => map?.[key] ?? key

/** Verification of a claim derived from the experiment reports, never from hand-written flags. */
export function claimVerification(c: Claim): { state: 'reproduced' | 'not_reproduced' | 'blocked' | 'no_experiment'; detail: string } {
  const exps = (c.experiment_ids ?? []).map((id) => experiments[id]).filter(Boolean)
  if (!exps.length) return { state: 'no_experiment', detail: 'No experiment is linked to this claim.' }
  const checks = exps.flatMap((m) => (reports[m.id]?.checks ?? []).filter((k) => k.claim_id === c.id).map((k) => ({ ...k, status: statusOf(m) })))
  if (!checks.length) return exps.every((m) => m.reproducibility_status === 'BLOCKED')
    ? { state: 'blocked', detail: 'The linked experiment is blocked, so this claim could not be recomputed.' }
    : { state: 'no_experiment', detail: 'No validation check refers to this claim yet.' }
  const trusted = checks.every((k) => k.status.status !== 'UNVERIFIED')
  const required = checks.filter((k) => k.required !== false)
  const optional = checks.filter((k) => k.required === false)
  const reqOk = required.length > 0 && required.every((k) => k.pass)
  const optBad = optional.filter((k) => !k.pass)
  if (trusted && reqOk && optBad.length === 0 && required.length === checks.length) return { state: 'reproduced', detail: `${checks.length} comparison(s) with the published value passed.` }
  if (required.length === 0) return { state: 'not_reproduced', detail: 'Only secondary comparisons exist for this claim and they did not match within tolerance. See the validation report.' }
  if (trusted && reqOk) return { state: 'reproduced', detail: `Point values reproduced (${required.length} comparison(s)); ${optBad.length} secondary comparison(s) did not match: see the validation report.` }
  return { state: 'not_reproduced', detail: 'A required comparison failed or the report is not current.' }
}
