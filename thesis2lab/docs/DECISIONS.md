# Decisions

| ID | Decision | Why |
|---|---|---|
| D-001 | Project lives in `thesis2lab/` inside the water-law-dataset repo, as an independent project. No existing file is modified. | Only that repository was in scope. The folder can be split out later with `git subtree split`. |
| D-002 | React + TypeScript + Vite; hash routing; relative base. | Works on GitHub Pages sub-paths with no server rewrite rules. |
| D-003 | Hand-written accessible SVG charts instead of Plotly. | Plotly adds roughly 1 MB or more. The charts needed (columns, bars, interval) are small, and every chart has a table alternative. Revisit if richer charts are needed. |
| D-004 | Pyodide not used. Calculations are TypeScript. | Not needed for the pilot; avoids a ~10 MB runtime. Python is used for independent verification only. Revisit for methods that need SciPy. |
| D-005 | Two implementations per experiment: TypeScript (product) and Python (reference). | A reference written separately catches transcription errors that a single implementation cannot. |
| D-006 | Status is derived, not trusted. Manifest holds the declared status; the interface shows the status the latest report supports. | Satisfies "the interface cannot report success without passing tests". |
| D-007 | `inputs_digest` change detection. | Cheap, deterministic invalidation without rerunning everything. |
| D-008 | Public inter-coder data replaces case identifiers with hashes. | Brazilian process numbers can identify parties. Traceability remains for the researcher through the hash. Researcher should confirm. |
| D-009 | The mananciais calibration rule is applied to all Brazilian coder-1 UNCERTAIN labels. | The sample has no topic flag, and this reproduces the published 0.832 within rounding. Documented as a limitation. |
| D-010 | EXP-002 is PARTIAL, not REPRODUCIBLE. | Point values reproduce; bootstrap intervals do not, and published intervals disagree with each other. |
| D-011 | Claims carry no stored verification flag. | Verification is computed from reports to avoid stale hand-typed flags. |
| D-012 | Workflows live at the repository root (`.github/workflows/thesis2lab-*.yml`), path-filtered. | GitHub only runs workflows from the root. They are new files; no existing workflow was edited. |
| D-013 | Deployment is manual (`workflow_dispatch`). | No automatic publication of unreviewed science. The existing repo already uses Pages for `docs/`; switching the Pages source would replace it. |
| D-014 | Researcher name "Junior Klaus" taken from CITATION.cff. RESEARCH_CONTEXT.md says "Claudio Klaus". | Needs researcher confirmation. |
| D-015 | Institution shown as "doctoral application in progress". | The brief names Erasmus University Rotterdam but admission is not confirmed. Do not assert affiliation. |
