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
| 4 | Deduplication | **Tooling built and exercised at scale.** `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability) has processed **5,208 unique records** across the WebSearch pilot, the `SOURCES.md` exemplars, and 18 real Scopus exports — 539 duplicates merged in the 2026-09-10 round (mostly DOI matches, several backfilling a missing abstract from the merged duplicate), on top of 1 earlier cross-source duplicate (Gaikwad & Thomas exemplar). `record_id` now a stable content hash (DOI, or title+year) rather than positional — the collision risk flagged earlier the same day is fixed, not just noted as a follow-up; see `CHANGELOG.md` 2026-09-10 (later still). A schema-validation script (`code/analysis/validate_schemas.py`) checks every project CSV's header against its documented/generated schema — currently all consistent. A **validated** Scopus adapter (`code/search/adapters/scopus_adapter.py`); **unvalidated** PubMed and Web of Science adapters (`pubmed_adapter.py`, `wos_adapter.py`); and an **unvalidated** shared RIS-format adapter (`ris_adapter.py`, covering HeinOnline/ProQuest/Sociological Abstracts/JSTOR/SSRN, all of which export RIS — grounded in the RIS standard itself rather than a guessed platform-specific format) exist in `code/search/adapters/`. Deliberately not covered: Westlaw/Lexis (no standard bulk export to build against) and CanLII/Rechtspraak.nl/Brazilian court portals/ANA-SNIS (feed the doctrinal/jurimetric strand, not this pipeline — see each `database_strategies/*.md`). |
| 5 | Title and abstract screening (two reviewers where feasible) | **Real first-pass screening done, by one AI reviewer.** `02_screening/title_abstract/screening_database.csv` has **5,208 total records, 5,173 of which have a real abstract**; all 5,173 have now been screened against `INCLUSION_EXCLUSION.md` by Claude as `reviewer_1` (`Claude-AI-1stpass-2026-09-10`), explicitly authorized by the researcher as a methodological choice per `PROJECT_SPEC.md` §14.18 — **1,436 include / 3,565 exclude / 172 unsure**. See `CHANGELOG.md` 2026-09-10 (final) for the exclusion-code breakdown and the batch-validation method. **This is a first pass only — `reviewer_2` (human) and conflict resolution have not happened**, so no record's inclusion is final yet; treat `unsure` the same as `include` for full-text-stage purposes. The 35 records without a real abstract were deliberately left undecided (title-only triage remains non-binding per `title_only_triage_memo.md`, still only covering the original 37). |
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
5,173 records with real abstracts); 4–5 done for a first AI reviewer pass,
awaiting a human second reviewer.** Repository/documentation scaffolding
is complete, the OSF preregistration is drafted (not submitted), and the
deduplication and screening-ingest scripts have processed the full
raw-export pool (37 `WebSearch`-pilot records — not a Tier 1/2 database
search, see `SEARCH_PROTOCOL.md` §7 — 3 `SOURCES.md` exemplars,
`SEARCH_018`'s 500 abstract-less records, and 5,207 records across the 17
completed `scopus_batch_plan_2026-08-26.md` batches, all with abstracts;
5,747 raw records total). The 2026-09-10 full re-run of
`code/search/deduplicate.py` found 539 of those to be duplicates; the
screening database now holds **5,208 unique candidate records, 5,173 of
which have a real abstract**. All 5,173 have now been screened against
`INCLUSION_EXCLUSION.md` by Claude as a first-pass AI reviewer (explicitly
authorized by the researcher — `CHANGELOG.md` 2026-09-10 (final)):
**1,436 include / 3,565 exclude / 172 unsure**. **This is provisional,
not final** — a human `reviewer_2` pass and conflict resolution are still
needed before any record's inclusion is settled. None of Phases 3 (fully),
6–16 can proceed at scale without either database access this environment
does not currently have, or the researcher continuing to supply
`SEARCH_026`'s export file, running the other database strategies in
`01_search/database_strategies/`, and providing (or delegating) the human
second-reviewer pass this phase still needs.

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
