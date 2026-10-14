# Session state

Last updated: 2026-10-14. Version 0.1.0. Branch `claude/thesis2lab-architecture-build-o3nfgr` (inside jrklaus8/water-law-dataset, folder `thesis2lab/`).

## Current milestone
M1 to M7 implemented for the pilot and validated locally (results in the final report of the build session). Not deployed. No release approved.

## What exists
- App: Home, Thesis, Laboratory (filters), Experiment workspace, Evidence explorer, Compare (governance matrix), Methods, Versions, About.
- EXP-001 EXPLORATORY (synthetic), EXP-002 PARTIAL (authentic labels, kappa audit), EXP-003 BLOCKED.
- 8 claims (all unreviewed), 7 sources, 3 methods, 4 governance records (hypotheses and one reported finding, none verified legal sources).
- Tooling: validate, status, changes, cost, release:prepare, check:links. CI and manual Pages workflows at the repo root.

## Outstanding issues
- Researcher input needed: see `docs/RESEARCH_CONTEXT.md` (unresolved questions).
- EXP-002: bootstrap CI endpoints do not reproduce; README headline 0.832 has no committed output file; calibration rule defined in-sample.
- The preliminary PDF is registered but not extracted (no PDF parser in the build).
- CI workflows have not run on GitHub yet; they were checked for YAML syntax only.
- Deploying Pages from this repo would replace the existing dashboard site. Do not enable until the researcher decides.

## Next steps (in order)
1. Researcher reviews claims and EXP-002 limitations; a named reviewer signs `validation/reviews/EXP-002.json` if satisfied.
2. Supply authentic data (raw corpus subset for EXP-003; real bibliographic records for EXP-001) with redistribution terms.
3. Add a PDF text extractor to `pipelines/ingest` (preserving page numbers) and map claims from the preliminary PDF.
4. Wrap `utils/jurimetric_coding.py` as a Mode B workflow with pinned dependencies and CI.
5. Populate `research/governance/` from verified legal sources only.
6. Confirm the first CI run on GitHub; decide hosting; then `npm run release:prepare`.
