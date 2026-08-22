# PRISMA Workflow

Reporting follows PRISMA 2020 (`SOURCES.md`), applicable to systematic
reviews with or without meta-analysis and usable beyond conventional health
intervention questions. PRISMA is a reporting guideline, not a complete
conduct manual — the conduct steps below are this project's own procedure.

## 16-phase workflow

| Phase | Task | Status |
|---|---|---|
| 1 | Develop protocol | **Done** — `PROTOCOL.md` |
| 2 | Preregister (OSF Generalized Systematic Review — see `PROTOCOL.md` §11) | Draft ready — `00_admin/preregistration/osf_preregistration_draft.md`; not yet submitted (no OSF account access from this environment) |
| 3 | Database searching | **Blocked** — strings ready in `01_search/database_strategies/`, but this environment has no credentials for Scopus, Web of Science, HeinOnline, Westlaw, Lexis, ProQuest, Sociological Abstracts, CanLII, or Rechtspraak.nl. Requires a human researcher (or a tool run with the appropriate access) to execute the searches and deposit raw exports in `01_search/raw_exports/`. |
| 4 | Deduplication | Tooling ready — `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability), tested against synthetic data, not yet run on real exports since none exist. Expects input normalized to a common schema (see the script's docstring); per-database raw-export adapters are still future work, to be written once real exports exist to develop against. |
| 5 | Title and abstract screening (two reviewers where feasible) | Tooling ready — `code/screening/init_screening_db.py` merges deduplicated records into the persistent screening database without ever overwriting an existing reviewer decision; tested and idempotent. Actual screening not started (no records to screen yet). |
| 6 | Full-text screening, standardized exclusion reason per record | Not started |
| 7 | Pilot extraction (~10 studies) | Not started |
| 8 | Full extraction | Not started |
| 9 | Risk of bias | Not started |
| 10 | Evidence classification | Not started |
| 11 | Quantitative feasibility assessment | Not started |
| 12 | Meta-analysis where justified | Not started |
| 13 | Structured quantitative synthesis of unpoolable evidence (SWiM) | Not started |
| 14 | Sensitivity analysis | Not started |
| 15 | Publication bias assessment where appropriate | Not started |
| 16 | PRISMA reporting | Not started |

**Current phase: 1–2 complete; 4–5 tooling built ahead of need; 3 is the
hard blocker.** Repository/documentation scaffolding is complete, the OSF
preregistration is drafted (not submitted), and the deduplication and
screening-ingest scripts are written and tested against synthetic data.
None of Phases 3, 6–16 can begin without either database access this
environment does not currently have, or a human researcher running the
searches in `01_search/database_strategies/` and depositing raw exports in
`01_search/raw_exports/`. Building tooling ahead of Phase 3 is deliberate —
it means the moment real exports exist, deduplication and screening can
start immediately — but it does not substitute for the search itself.

## Screening database schema

`02_screening/title_abstract/screening_database.csv`:

```
record_id, database, title, authors, year, doi, duplicate,
title_abstract_decision, full_text_decision, exclusion_reason,
reviewer_1, reviewer_2, conflict, final_decision
```

Standardized exclusion codes: `INCLUSION_EXCLUSION.md` §"Standardized
exclusion codes" (E01–E12).

## Evidence classification matrix

Every included study receives, in `05_analysis/descriptive/evidence_map.csv`:

```
study_id, study_design_class, evidence_level, mechanism_family,
outcome_family, quantitative_synthesis_eligible, qualitative_synthesis_eligible,
legal_context, institutional_context
```

Worked example (illustrative only — not real extracted data):

| Study type | Design | Mechanism | Outcome | Meta-eligible |
|---|---|---|---|---|
| Legal-recognition observational study | Observational | Eligibility | Water access | Potentially |
| Bureaucratic-assistance field experiment | Experimental | Burden/facilitation | Formal connection | Potentially |
| Doctrinal article | Doctrinal | Eligibility | Normative | No |
| Interview study | Qualitative | Discretion | Administrative experience | No, but mechanism-synthesis eligible |
| Judicial decisions dataset | Jurimetric | Litigation | Judicial outcome | Never — separate study (`PROJECT_SPEC.md` §9) |

## PRISMA flow diagram

`06_outputs/prisma/prisma_flow.md` is the live flow-diagram source. It is
currently a stub with all counts at zero, updated only as each phase above
actually produces a count — never pre-filled with placeholder or estimated
numbers.
