# 00_admin — decisions, audits and the running record

**Start with:** `DECISIONS_AND_OPEN_ITEMS.md`. It is the single place to see what is still undecided and who decides (table A), the judgment calls already made and where each is documented, what has not been verified, and a backlog. Items are numbered `A1`, `A2`, … (see `../GLOSSARY.md`); each is marked OPEN or CLOSED with a date and, for rulings, the reviewer initials `CK`.

| File or folder | What it is |
|---|---|
| `CURRENT_FIGURES.md`, `current_figures.json` | Every headline figure, **generated** from the CSV databases by `code/analysis/current_figures.py`. If any document disagrees with this file, this file is right |
| `DECISIONS_AND_OPEN_ITEMS.md` | The decision log described above |
| `WEAKNESSES.md`, `WEAKNESS_REGISTER.csv` | **The frank list of the review's weak points**, each with evidence, a way to test or break it and what would resolve it (generated from `code/analysis/weakness_register_source.csv`) |
| `STUDY_AUDIT_TRAIL.csv`, `.md` | One row per included study: who decided inclusion, extraction depth, risk-of-bias depth, synthesis status (generated) |
| `AI_USE_LEDGER.csv`, `.md` | Which AI did what at each stage, and what is not archived (generated) |
| `DEVIATIONS_REGISTER.csv`, `ERRORS_FOUND_REGISTER.csv`, `DEVIATIONS_AND_ERRORS.md` | Every departure from the protocol and every error the project found in itself (hand-maintained data; the page is rendered from them) |
| `audits/2026-09-28_repository_audit.md` | The project's audit of itself: 16 findings, what was wrong, what was fixed, what stayed open |
| `RELEASE_0.2.0-interim_2026-10-14.md` | What the interim release contains and what it does not |
| `preregistration/osf_preregistration_draft.md` | Retrospective registration, prepared and **not yet submitted**; separates what was fixed in writing before searching from the dated changes afterwards |
| `disclosures/` | Funding and competing-interests statements |
| `RESEARCHER_DECISION_BRIEF_*`, `SESSION_HANDOFF_*`, `*_LOG_*`, `PDF_RETRIEVAL_*`, `A9_INSTRUMENT_VERIFICATION_*`, `VERIFIER_MUTATION_MAP_*`, `LEGAL_DATA_HUNTER_SOURCE_REQUESTS_*` | Dated working notes: briefs to the researcher, retrieval logs, the check of appraisal-instrument wording against the publishers' sources, and the test of whether the verifier catches deliberately introduced errors. Snapshots, not current status |
| `protocol/`, `ethics/`, `correspondence/` | Empty placeholders from the project template (the protocol itself is `../PROTOCOL.md`) |

**Who checked it:** the figures are re-derived on every run of `python3 code/analysis/verify_repository.py`; rulings under `CK` were made by the principal investigator; everything else is the AI's record of its own work.
