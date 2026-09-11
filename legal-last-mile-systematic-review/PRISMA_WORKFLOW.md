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
| 3 | Database searching | **Closed 2026-09-11, by researcher decision — candidate pool already large enough to move to screening.** This environment still cannot reach any database directly (confirmed 2026-08-25); all searching was done by the researcher via EUR institutional access, largely relayed through Claude Cowork. Databases actually searched: Scopus (18/18 planned batches), Web of Science (`SEARCH_035`, 4,058 records), HeinOnline (`SEARCH_036`–`SEARCH_038`, minimal real yield — see below), ProQuest (`SEARCH_039`, 7,728 records via a full account-based export) and ProQuest/Sociological Abstracts (`SEARCH_040`, 16,736 records), and JSTOR (`SEARCH_041`, 356 identified, only a partial export ever produced). **SSRN and Westlaw/Lexis were never searched at all** — the phase was closed before either was reached; documented as an intentional gap in `SEARCH_PROTOCOL.md` §7 and `search_log.csv`'s `SEARCH_042`/`SEARCH_043` stub rows, to be reported honestly in any manuscript output rather than omitted. HeinOnline's real yield was small and mostly lost to file-delivery failures: `SEARCH_036` found 71,226 hits with no bulk-export mechanism at that volume (count-only, 0 ingested); `SEARCH_037` yielded 1 ingested record; `SEARCH_038`'s 3 records and most of `SEARCH_041`'s JSTOR batch were reported by Cowork but the export files themselves never reached this pipeline, and recovery was abandoned when the search phase closed. Three earlier rounds of a non-systematic, low-recall **exploratory pilot** were also run via Claude's `WebSearch` tool (`SEARCH_003`–`SEARCH_017`, 2026-08-25, 37 candidate records) — see `SEARCH_PROTOCOL.md` §7; that part never counted toward Phase 3. |
| 4 | Deduplication | **Complete for the closed search phase.** `code/search/deduplicate.py` (DOI-match + title/year-similarity match, full merge log for auditability) has processed **27,481 unique records** across the WebSearch pilot, the `SOURCES.md` exemplars, all 18 Scopus exports, Web of Science, HeinOnline, ProQuest, ProQuest/Sociological Abstracts, and JSTOR — **7,113 duplicates merged** in total (heavy Scopus/WoS/ProQuest cross-database journal overlap, exactly as expected). `record_id` is a stable content hash (DOI, or title+year) rather than positional. A schema-validation script (`code/analysis/validate_schemas.py`) checks every project CSV's header against its documented/generated schema — currently all consistent (11 files). Validated adapters: Scopus, Web of Science (`wos_adapter.py` — found and fixed two real bugs, including a data-corrupting quote-escaping issue), and the shared RIS adapter (`ris_adapter.py`, validated against real HeinOnline/ProQuest/Sociological Abstracts/JSTOR exports this round — also found and fixed a genuine bug: ProQuest conference-abstract-supplement records can carry a single abstract field past Python's default csv module field-size limit, now raised in every downstream script). Deliberately not covered: Westlaw/Lexis (never searched, no standard bulk export to build against) and CanLII/Rechtspraak.nl/Brazilian court portals/ANA-SNIS (feed the doctrinal/jurimetric strand, not this pipeline — see each `database_strategies/*.md`). |
| 5 | Title and abstract screening (two reviewers where feasible) | **Real first-pass screening done on the entire closed-search-phase pool, by one AI reviewer.** `02_screening/title_abstract/screening_database.csv` has **27,481 total records, 26,222 of which have a real abstract**; all 26,222 have now been screened against `INCLUSION_EXCLUSION.md` by Claude as `reviewer_1` (`Claude-AI-1stpass-2026-09-10` and `-09-11`), explicitly authorized by the researcher as a methodological choice per `PROJECT_SPEC.md` §14.18 — **3,062 include / 22,557 exclude / 603 unsure**. The 2026-09-11 ProQuest/Sociological Abstracts round (19,085 newly-screened records) came in with a much lower include+unsure rate (~9%) than the earlier Scopus/WoS rounds (~25-30%), driven by real search-strategy noise (broad `noft()` full-text-adjacent matching, thesaurus-term pulls into unrelated sociology-of-bureaucracy literature) rather than a screening quality issue — see `search_log.csv` and `REVIEWER_2_README.md`. This round was run as 39 parallel ~500-record batches, each isolated to its own scratch directory after an earlier flat-shared-directory attempt suffered real cross-agent file corruption (caught via record-for-record validation, not assumed clean — see `CHANGELOG.md`); every batch was independently verified against its source file before merging. A ready-to-use handoff for a human `reviewer_2` exists: `02_screening/title_abstract/reviewer_2_queue.csv` (3,665 include+unsure records) and `exclude_spotcheck_sample.csv` (120-record random QA sample, fixed seed), see `REVIEWER_2_README.md`. **This is a first pass only — `reviewer_2` (human) and conflict resolution have not happened**, so no record's inclusion is final yet; treat `unsure` the same as `include` for full-text-stage purposes. The 1,259 records without a real abstract were deliberately left undecided (title-only triage remains non-binding per `title_only_triage_memo.md`, still only covering the original 37). |
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

**Current phase: 1–2 complete; 3 closed (by researcher decision, with
documented gaps — SSRN and Westlaw/Lexis never searched); 4–5 done for a
first AI reviewer pass, awaiting a human second reviewer.**
Repository/documentation scaffolding is complete, the OSF preregistration
is drafted (not submitted), and the deduplication and screening-ingest
scripts have processed the full raw-export pool: 37 `WebSearch`-pilot
records (not a Tier 1/2 database search, see `SEARCH_PROTOCOL.md` §7), 3
`SOURCES.md` exemplars, `SEARCH_018`'s 500 abstract-less records, 5,484
records across all 18 Scopus batches, 4,058 from Web of Science, 1 from
HeinOnline, 7,728 from ProQuest's full account-based export, 16,736 from
ProQuest/Sociological Abstracts, and 50 from JSTOR — **34,594 raw records
total**. The final 2026-09-11 re-run of `code/search/deduplicate.py`
found 7,113 of those to be duplicates (heavy cross-database journal
overlap, as expected); the screening database now holds **27,481 unique
candidate records, 26,222 of which have a real abstract**. All 26,222
have now been screened against `INCLUSION_EXCLUSION.md` by Claude as a
first-pass AI reviewer (explicitly authorized by the researcher —
`CHANGELOG.md`): **3,062 include / 22,557 exclude / 603 unsure**.
**This is provisional, not final** — a human `reviewer_2` pass and
conflict resolution are still needed before any record's inclusion is
settled; a ready-to-use handoff exists (`REVIEWER_2_README.md`, 3,665
include+unsure records). Phases 6–16 cannot proceed at scale until the
researcher (or a delegate) completes the human second-reviewer pass this
phase still needs — that is now the project's real bottleneck, not
further searching.

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
