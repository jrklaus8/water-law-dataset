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
| 3 | Database searching | **Blocked for every Tier 1/2 and legal-repository database** — strings ready in `01_search/database_strategies/`, but this environment cannot reach any of them (no credentials for the subscription platforms; direct network egress to the open web, including the free ones like PubMed/Scholar/CanLII/Rechtspraak.nl, is blocked by policy — confirmed 2026-08-25). Requires a human researcher (or a tool run with the appropriate access) to execute the real searches and deposit raw exports in `01_search/raw_exports/`. Two rounds of a non-systematic, low-recall **exploratory pilot** were run instead via Claude's `WebSearch` tool (`SEARCH_003`–`SEARCH_013`, 2026-08-25 — keyword searches plus an approximated backward-citation search on the 4 exemplar papers and a grey-literature pass, 31 candidate records total) — see `SEARCH_PROTOCOL.md` §7; **none of this counts toward Phase 3.** |
| 4 | Deduplication | **Tooling built and now exercised on real (pilot) data** — `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability) ran on 31 WebSearch-pilot candidates across two batches, 0 duplicates found, output in `01_search/deduplicated/`. A schema-validation script (`code/analysis/validate_schemas.py`) now checks every project CSV's header against its documented/generated schema — currently all consistent. Still untested against a real Tier 1 export, since none exist; per-database raw-export adapters remain future work. |
| 5 | Title and abstract screening (two reviewers where feasible) | Tooling ready and exercised — `code/screening/init_screening_db.py` merged 31 pilot candidates into `02_screening/title_abstract/screening_database.csv`. **No screening decision has been made on any of them** — `title_abstract_decision` is blank on every row. A non-binding, title-only triage memo (`06_outputs/supplementary/title_only_triage_memo.md`) exists to help a human reviewer prioritize, but it does not touch the authoritative decision field. A human reviewer (or a properly scoped screening pass with actual abstract access) still needs to decide include/exclude/unsure per `INCLUSION_EXCLUSION.md`. |
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

**Current phase: 1–2 complete; 4–5 tooling built and now exercised on a
real (but explicitly non-systematic) pilot batch; 3 is the hard blocker
for the actual protocol.** Repository/documentation scaffolding is
complete, the OSF preregistration is drafted (not submitted), and the
deduplication and screening-ingest scripts have processed 25 real
candidate records surfaced by an exploratory `WebSearch` pilot (not a
Tier 1/2 database search — see `SEARCH_PROTOCOL.md` §7). Those 25 records
are sitting in the screening database with **no screening decision made**.
None of Phases 3 (as actually specified), 6–16 can begin in earnest
without either database access this environment does not currently have,
or a human researcher running the searches in
`01_search/database_strategies/` and depositing raw exports in
`01_search/raw_exports/`.

## Screening database schema

`02_screening/title_abstract/screening_database.csv`:

```
record_id, database, title, authors, year, doi, url, duplicate,
title_abstract_decision, full_text_decision, exclusion_reason,
reviewer_1, reviewer_2, conflict, final_decision
```

(`url` was added 2026-08-25, after the schema's first use, once real
candidate records surfaced sources with no DOI at all — mostly grey
literature. Without a URL such a record cannot be relocated. See
`CHANGELOG.md` for the amendment.)

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
