import { createHash } from 'node:crypto'
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs'
import { dirname, join, relative, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import Ajv from 'ajv'
import addFormats from 'ajv-formats'
import type { DatasetRecord, ExperimentManifest, ReferenceFile, ValidationReport } from '../../app/src/research/types'

export const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..')
export const p = (...parts: string[]) => join(ROOT, ...parts)
export const readJson = <T = unknown>(path: string): T => JSON.parse(readFileSync(path, 'utf8')) as T
export const sha256 = (data: string | Buffer) => createHash('sha256').update(data).digest('hex')

export function listFiles(dir: string, ext = '.json'): string[] {
  if (!existsSync(dir)) return []
  return readdirSync(dir).filter((f) => f.endsWith(ext)).sort().map((f) => join(dir, f))
}

function walk(dir: string): string[] {
  if (!existsSync(dir)) return []
  return readdirSync(dir).sort().flatMap((n) => {
    if (n === '__pycache__' || n === 'node_modules') return []
    const full = join(dir, n)
    return statSync(full).isDirectory() ? walk(full) : [full]
  })
}

const ajv = new Ajv({ allErrors: true, strict: false })
addFormats(ajv)
const validators = new Map<string, ReturnType<typeof ajv.compile>>()

export function validateAgainst(schemaName: string, data: unknown): string[] {
  let v = validators.get(schemaName)
  if (!v) { v = ajv.compile(readJson(p('data/schemas', `${schemaName}.schema.json`))); validators.set(schemaName, v) }
  return v(data) ? [] : (v.errors ?? []).map((e) => `${e.instancePath || '/'} ${e.message}`)
}

export interface Loaded {
  manifests: ExperimentManifest[]
  datasets: Record<string, DatasetRecord>
}

export function loadProject(): Loaded {
  const manifests = readdirSync(p('experiments')).sort()
    .map((d) => p('experiments', d, 'manifest.json')).filter(existsSync)
    .map((f) => readJson<ExperimentManifest>(f))
  const datasets = Object.fromEntries(listFiles(p('data/metadata')).map((f) => readJson<DatasetRecord>(f)).map((d) => [d.id, d]))
  return { manifests, datasets }
}

export const loadReferences = (m: ExperimentManifest): ReferenceFile[] =>
  m.reference_outputs.map((r) => readJson<ReferenceFile>(p('experiments', m.id, r)))

export const loadReport = (id: string): ValidationReport | undefined => {
  const f = p('validation/reports', `${id}.json`)
  return existsSync(f) ? readJson<ValidationReport>(f) : undefined
}

/** Digest of everything a validation result depends on. Any change makes old reports stale. */
export function inputsDigest(m: ExperimentManifest, datasets: Record<string, DatasetRecord>): string {
  const files = new Set<string>(walk(p('experiments', m.id)).filter((f) => !f.endsWith('README.md')))
  for (const id of m.dataset_ids) {
    files.add(p('data/metadata', `${id}.json`))
    files.add(p(datasets[id].path))
  }
  walk(p('app/src/research')).filter((f) => f.endsWith('.ts') && !f.endsWith('.test.ts')).forEach((f) => files.add(f))
  const lines = [...files].sort().map((f) => `${relative(ROOT, f)}\0${sha256(readFileSync(f))}`)
  return sha256(lines.join('\n'))
}
