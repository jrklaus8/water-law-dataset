# Roadmap

## Done (version 0.1.0)
- M1 Foundation: Vite + React + TypeScript app, schemas, tests, docs.
- M2 Data model: ten JSON Schemas, validator with cross-reference checks, read-only ingest scripts, synthetic fixture.
- M3 First experiment: EXP-001 bibliometric explorer (synthetic, EXPLORATORY) with filters, charts, exports.
- M4 Verification: independent Python references, repeatability, stale-report detection, derived statuses. EXP-002 reproduces published kappa values (PARTIAL).
- M5 Navigation: thesis, evidence explorer, comparative governance matrix.
- M6 Publication: CI workflow, accessibility checks (axe), manual Pages workflow, draft release tooling. Not deployed.
- M7 Expansion: `register_source.py`, change report, project skills, example project, documentation for adding material.

## Next (priority order)
1. Researcher review of the eight claims and of the EXP-002 limitations. Record sign-off in the validation report process.
2. Obtain authentic data: the raw decision corpus (or a licence-cleared subset) to unblock EXP-003; real bibliographic records to replace EXP-001's synthetic data.
3. Wrap `utils/jurimetric_coding.py` as a Mode B workflow with pinned dependencies and CI verification.
4. Extract text and page references from the preliminary PDF (add a PDF parser to the ingest pipeline), then map claims.
5. Populate the governance matrix from verified legal sources only.
6. Decide on hosting (own repository recommended) and enable Pages.

## Later
Pyodide for methods that need SciPy; optional FastAPI for heavy methods; Zenodo archiving of approved releases; optional, authenticated, budget-capped Mode C.
