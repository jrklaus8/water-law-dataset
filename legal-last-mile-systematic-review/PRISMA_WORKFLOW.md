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
| 3 | Database searching | **Started for real, now with abstracts, 17 of 18 planned Scopus batches done.** This environment still cannot reach any database directly (confirmed 2026-08-25). The researcher has working EUR institutional access: `SEARCH_018` (2026-08-26, 500 records, no abstracts) plus all of `scopus_batch_plan_2026-08-26.md` except `SEARCH_026` (17 batches, 2026-09-10, **with** Abstract/Author Keywords/Index Keywords) are executed and ingested. See `CHANGELOG.md` 2026-08-26 and 2026-09-10 (two entries). Still needed: `SEARCH_026`'s export file (run but not yet uploaded — see `scopus_batch_plan_2026-08-26.md` Status), and every other Tier 1/2/legal-repository database. Three earlier rounds of a non-systematic, low-recall **exploratory pilot** were also run via Claude's `WebSearch` tool (`SEARCH_003`–`SEARCH_017`, 2026-08-25, 37 candidate records) — see `SEARCH_PROTOCOL.md` §7; that part still doesn't count toward Phase 3, but every Scopus run does. |
| 4 | Deduplication | **Tooling built and exercised at scale.** `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability) has processed **5,314 unique records** across the WebSearch pilot, the `SOURCES.md` exemplars, and 18 real Scopus exports — 539 duplicates merged in the latest round alone (mostly DOI matches, several backfilling a missing abstract from the merged duplicate), on top of 1 earlier cross-source duplicate (Gaikwad & Thomas exemplar) and 2 likely duplicate-publication pairs flagged manually. The 2026-09-10 batch also surfaced and fixed a real bug: positional `record_id` assignment can collide across ingest rounds as new files shift file-processing order — see `CHANGELOG.md` 2026-09-10 (later) for the fix applied and the note that the underlying scheme is a known follow-up. A schema-validation script (`code/analysis/validate_schemas.py`) checks every project CSV's header against its documented/generated schema — currently all consistent. A **validated** Scopus adapter (`code/search/adapters/scopus_adapter.py`) and an **unvalidated** PubMed adapter exist in `code/search/adapters/`; other per-database adapters remain future work. |
| 5 | Title and abstract screening (two reviewers where feasible) | Tooling ready and exercised — `code/screening/init_screening_db.py` has merged candidates into `02_screening/title_abstract/screening_database.csv`, now **5,314 total records, 5,279 of which have a real abstract**. **No screening decision has been made on any record yet** — `title_abstract_decision` is blank on every row, including the 5,279 with abstracts. A non-binding, title-only triage memo (`06_outputs/supplementary/title_only_triage_memo.md`, still only covering the original 37) exists to help a human reviewer prioritize, but it does not touch the authoritative decision field and has not been extended to the Scopus records. Real title/*abstract* screening against `INCLUSION_EXCLUSION.md` is now technically possible on nearly the whole pool — a human reviewer still needs to actually do it, at this scale a nontrivial undertaking in itself. |
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

**Current phase: 1–2 complete; 3 far along (17 of 18 Scopus batches done,
5,279 records with real abstracts); 4–5 tooling built and exercised at
scale.** Repository/documentation scaffolding is complete, the OSF
preregistration is drafted (not submitted), and the deduplication and
screening-ingest scripts have processed the full raw-export pool (37
`WebSearch`-pilot records — not a Tier 1/2 database search, see
`SEARCH_PROTOCOL.md` §7 — 3 `SOURCES.md` exemplars, `SEARCH_018`'s 500
abstract-less records, and 5,207 records across the 17 completed
`scopus_batch_plan_2026-08-26.md` batches, all with abstracts; 5,747 raw
records total). The 2026-09-10 full re-run of `code/search/deduplicate.py`
found 539 of those to be duplicates; the screening database now holds
**5,314 unique candidate records, 5,279 of which have a real abstract**,
with **no screening decision made on any of them**. None of Phases 3
(fully), 6–16 can proceed at scale without either database access this
environment does not currently have, or the researcher continuing to
supply `SEARCH_026`'s export file and run the other database strategies
in `01_search/database_strategies/`, depositing raw exports in
`01_search/raw_exports/`.

## Screening database schema

`02_screening/title_abstract/screening_database.csv`:

```
record_id, database, title, authors, year, doi, url, abstract, duplicate,
title_abstract_decision, full_text_decision, exclusion_reason,
reviewer_1, reviewer_2, conflict, final_decision
```

(`url` was added 2026-08-25, after the schema's first use, once real
candidate records surfaced sources with no DOI at all — mostly grey
literature. Without a URL such a record cannot be relocated. `abstract`
was added 2026-09-10, once the first export with Abstract selected in the
field picker arrived — optional, blank on anything ingested before that
date. See `CHANGELOG.md` for both amendments.)

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
