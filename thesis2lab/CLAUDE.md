# Thesis2Lab

Static-first system that turns a thesis into an interactive, verifiable browser laboratory.
First project: "The Legal Last Mile" (sanitation governance, administrative law; Brazil, Ontario, Netherlands).
Use AI to BUILD the lab, never to run it. The public site makes no AI or server calls.

## Session start (do this, in order)
1. Read this file. 2. `git status`. 3. Read `docs/SESSION_STATE.md`. 4. Read only the docs the task needs. 5. Continue from the last validated milestone.
Never re-read whole research sources; use the structured records in `research/` and `data/metadata/`.

## Commands (run from thesis2lab/)
- `npm run dev` start locally. `npm run build` validate everything then build to `app/dist`.
- `npm run validate:schemas` records + cross references. `npm run validate:experiments` run experiments against references, write `validation/reports/`.
- `npm test` vitest. `npm run test:py` pytest. `npm run test:e2e` Playwright (needs a built app: `npx vite build --config app/vite.config.ts`).
- `npm run status` assets and problems. `npm run changes` stale validations and changed sources. `npm run cost` measurable costs. `npm run release:prepare -- X.Y.Z` draft release.
- Python ingest: `python3 pipelines/ingest/register_source.py PATH --title T --kind K`.

## Layout
- `app/src/research/` pure calculation code (csv, descriptive, agreement, status, compare, report). No React here.
- `app/src/{pages,components,charts,experiments,lib}` interface. `lib/registry.ts` discovers all records with `import.meta.glob`.
- `experiments/EXP-nnn/` manifest.json, references/, tests/ (independent Python reference), README.md.
- `research/{thesis,sources,claims,methods,governance,manifests}` JSON records. `data/{public,synthetic,metadata,schemas}`.
- `validation/reports/` generated reports (never hand-edit). `pipelines/` Python ingest and build. `scripts/` TS tooling.

## Scientific integrity (non-negotiable)
- Never invent results, sources, citations, jurisdictional facts or test outcomes. Missing material means BLOCKED or synthetic, labelled.
- A status shows only if a current validation report supports it (`app/src/research/status.ts`). Code that merely runs is not REPRODUCIBLE.
- Reports come from program output only. Independent review stays `pending` until a named human signs.
- Synthetic data must be labelled everywhere and can never be REPRODUCIBLE. Never modify source data; imports are read-only copies with checksums.
- Researcher review is required for scientific and legal conclusions. Claims start `unreviewed`.
- No private or unpublished material in the public repo. Court case ids are hashed in public data.
- Never let visitors run code. `requires_ai` must stay false until Mode C is deliberately built.

## Cost rules
Local scripts first, agents last. One coordinator, one specialist at a time. Cache by digest (`inputs_digest`). No model calls at runtime.
Do not read or summarise the full thesis repeatedly. Bounded retries (3), then document the blocker. Do not invent token or billing numbers.

## Conventions
- New experiment = new folder + valid manifest + data record. Add a runner in `app/src/research/runners.ts` only for a new calculation type.
- Change an analysis file or dataset and the report goes stale; rerun `npm run validate:experiments`.
- Keep the user-facing voice plain. No em dashes in any output text for the user.

## Status
Milestones 1 to 7 implemented for the pilot. See `docs/SESSION_STATE.md` for exact state and next steps.
Docs: `docs/ARCHITECTURE.md`, `ROADMAP.md`, `RESEARCH_CONTEXT.md`, `DECISIONS.md`, `COST_POLICY.md`, `REPRODUCIBILITY_STANDARD.md`, `ADDING_RESEARCH.md`, `DEPLOYMENT.md`.
