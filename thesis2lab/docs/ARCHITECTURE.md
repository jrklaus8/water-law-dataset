# Architecture

Static-first. The public product is HTML, JS, CSS and JSON served from any static host. No backend, no database, no AI call at runtime.

## Data flow
```
research files (read only) -> pipelines/ingest -> research/*.json, data/** (+ checksums)
experiments/EXP-n/manifest.json + data record + references
        |                                   |
        v                                   v
scripts/run-validation.ts  ---->  validation/reports/EXP-n.json  (+ app/src/generated/digests.json)
        |
        v
Vite build: registry.ts globs every record -> pages. status.ts decides what status may be shown.
```

## Boundaries
- `app/src/research/*`: pure TypeScript, no DOM, no React. Runs identically in the browser, Vitest and Node validation scripts. This is the one implementation of every calculation.
- `experiments/*/tests/reference_impl.py`: a second, independent implementation in Python, used only for verification. It must never import the TypeScript code or share logic with it.
- `app/src/lib/registry.ts`: the only module that knows where records live.
- `scripts/`: Node tooling that validates, executes and reports. It writes `validation/` and `app/src/generated/`.

## Execution modes
A: browser (implemented). B: reproducible workflow (documented, not used yet). C: AI assisted (disabled; the schema validator rejects `requires_ai: true`).

## Extension points
- New experiment of an existing type: folder, manifest, dataset record, references. No code change.
- New calculation type: add a runner (`runners.ts`), optional view (`experiments/views.tsx`), an independent `reference_impl.py`.
- New project: replace `project.config.json`, thesis, sources, claims, experiments. See `examples/other-project/`.

## Status computation
`effectiveStatus(manifest, report, currentDigest)` is the single gate. `inputs_digest` hashes the experiment folder, dataset record and file, and every non-test file in `app/src/research/`. Any change makes the report stale and the experiment shows as Unverified until revalidated.

## Static deployment
`vite build` with `base: './'` and hash-based routing, so it works under any sub-path. CI builds it; deployment is a manual workflow. See `DEPLOYMENT.md`.
