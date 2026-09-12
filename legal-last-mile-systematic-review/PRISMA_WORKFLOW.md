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
| 5 | Title and abstract screening (two reviewers where feasible) | **Real first-pass screening done on the entire closed-search-phase pool, by one AI reviewer.** `02_screening/title_abstract/screening_database.csv` has **27,481 total records, 26,222 of which have a real abstract**; all 26,222 have now been screened against `INCLUSION_EXCLUSION.md` by Claude as `reviewer_1` (`Claude-AI-1stpass-2026-09-10` and `-09-11`), explicitly authorized by the researcher as a methodological choice per `PROJECT_SPEC.md` §14.18 — **3,062 include / 22,557 exclude / 603 unsure**. The 2026-09-11 ProQuest/Sociological Abstracts round (19,085 newly-screened records) came in with a much lower include+unsure rate (~9%) than the earlier Scopus/WoS rounds (~25-30%), driven by real search-strategy noise (broad `noft()` full-text-adjacent matching, thesaurus-term pulls into unrelated sociology-of-bureaucracy literature) rather than a screening quality issue — see `search_log.csv` and `REVIEWER_2_README.md`. This round was run as 39 parallel ~500-record batches, each isolated to its own scratch directory after an earlier flat-shared-directory attempt suffered real cross-agent file corruption (caught via record-for-record validation, not assumed clean — see `CHANGELOG.md`); every batch was independently verified against its source file before merging. **`reviewer_2` (human) pass completed 2026-09-12** via a purpose-built Excel
worksheet handoff (all 3,665 include+unsure records, one-click Yes/blank
decision column) — see `REVIEWER_2_README.md`. Result: 3,659 `include` /
6 `exclude`, **zero recorded conflicts** by the strict definition in
`DATA_DICTIONARY.md` (reviewer_1 `include` vs. reviewer_2 `exclude`) — all
6 reviewer_2 excludes were resolutions of reviewer_1 `unsure` records, not
disagreements with a firm reviewer_1 decision. **Worth flagging plainly**:
a 99.8% agreement rate between two independent reviewers is far higher
than PRISMA second-pass screening typically produces, and the full
worksheet came back in far less time than reading ~3,700 abstracts
individually would take. This was raised directly with the researcher
before merging (not merged silently) — the researcher confirmed proceeding
with the file as delivered. `final_decision` is populated for all 3,665
records on this basis; treat this as the recorded second-reviewer pass,
with the caveat above on the record for anyone assessing this review's
rigor. `exclude_spotcheck_sample.csv` (120-record random QA sample, fixed
seed) has not yet been reviewed and remains available if the researcher
wants an independent check on the exclude population. The 1,259 records
without a real abstract were deliberately left undecided (title-only
triage remains non-binding per `title_only_triage_memo.md`, still only
covering the original 37). |
| 6 | Full-text screening, standardized exclusion reason per record | **In progress, live.** `02_screening/full_text/full_text_screening_database.csv` holds all **3,659** Phase-5 includes. The researcher supplies full-text PDFs via chat upload on a rolling basis (expected to continue for over a month); each is converted (`pdftotext -layout`), screened by Claude as `reviewer_1` (`Claude-AI-fulltext-2026-09-12`) against `INCLUSION_EXCLUSION.md`'s E01–E12 codes, recorded via `code/screening/update_full_text_record.py`, and any exclusion is also logged to `02_screening/exclusion_log/exclusion_log.csv`. As of this update: **156 of 3,659 records decided (77 include / 79 exclude)**; exclusion-reason breakdown so far: E02 (wrong population) 27, E04 (wrong outcome) 15, E01 (wrong topic) 12, E05 (no empirical evidence) 9, E06 (engineering only) 8, E07 (wrong service) 4, E09 (insufficient information) 1, E03 (wrong exposure) 1, E08 (duplicate) 2. `reviewer_2` (human) has not yet been assigned for this phase — open question for the researcher. Retrieval remains researcher-driven (institutional/personal access); this environment has no outbound access to fetch full texts itself. |
| 7 | Pilot extraction (~10 studies) | **Superseded by full extraction (Phase 8) proceeding directly** — the researcher explicitly authorized starting extraction on all full-text includes as they clear Phase 6, rather than waiting to draw a separate ~10-study pilot subsample first (`CHANGELOG.md`). `EXTRACTION_FORM.md` and `CODEBOOK.md` are being applied directly per Phase 8 below. `select_pilot_sample.py` and `PILOT_EXTRACTION.md` remain available if a formal pilot-disagreement check is wanted later. |
| 8 | Full extraction | **In progress, live, essentially caught up with Phase 6.** `03_extraction/extracted_data/extraction_database.csv` holds **75 fully-extracted studies (S001–S075)**, all 92 `CODEBOOK.md` fields populated per study, out of **71** current full-text includes — the only gap is **2 studies flagged with no cached full text available in this session** (Lubeck-Schricker et al.; Gaikwad) that were explicitly *not* extracted from memory, consistent with the standing rule against fabricating data — they await re-upload. Every new full-text include is now extracted in the same session it clears Phase 6, rather than accumulating in a backlog. `reviewer_1` for all 75 is `Claude-AI-fulltext-2026-09-12`; `reviewer_2`/`final_decision` are blank pending a second extraction pass (see Phase 9 note on the same open reviewer_2 question). Four of the 75 (S015, S019, S027, S052) are themselves secondary systematic reviews, flagged `study_design_class = systematic_review_secondary`, never to be pooled as an independent primary effect. |
| 9 | Risk of bias | **Process scaffolding built 2026-09-12; deliberately not yet applied to any of the 75 extracted studies.** `RISK_OF_BIAS.md` is explicit that none of the six validated appraisal tools (RoB 2, ROBINS-I, the two JBI checklists, CASP, MMAT) or AMSTAR 2 may be reconstructed from memory — the current official version of each must be obtained before appraising a study with it. Accordingly, every one of the 62 extracted studies has `risk_of_bias_tool` correctly identified (design-matched per `RISK_OF_BIAS.md` §1, or the project's own Legal Institutional Evidence Appraisal Framework per §2 where no conventional tool fits) but `risk_of_bias_rating` deliberately left **blank**, with an `extraction_note` on each row deferring the actual rating to a follow-up pass conducted with the official instrument in hand. `04_quality/appraisal_forms/APPRAISAL_FORM.md` documents that process; a fully worked fillable form exists for the project-owned Legal Institutional Evidence Appraisal Framework (`legal_institutional_evidence_appraisal_framework_form.md`). This is a real, reportable limitation at this stage of the review, not an oversight — disclose it as such in any manuscript output. |
| 10 | Evidence classification | **Populated 2026-09-12 for all 75 extracted studies, kept current as extraction grows.** `code/analysis/build_evidence_map.py` derived what can safely be derived mechanically (`study_design_class` from `risk_of_bias_tool`, `mechanism_family` from the four top-level mechanism booleans, `legal_context`/`institutional_context` copied from extraction); the remaining judgment-call fields were then filled by hand for all 75 rows: `study_design_class` for the 12 studies using the project's own Legal Institutional Evidence Appraisal Framework (resolved doctrinal vs. jurimetric per study), `outcome_family` mapped to `PROJECT_SPEC.md` §7's hierarchy based on each study's actual central/tested outcome (not a mechanical restatement of the outcome booleans), `evidence_level` written as prose per `DATA_DICTIONARY.md`'s instruction that it is a narrative tier rather than a score, and `quantitative_synthesis_eligible`/`qualitative_synthesis_eligible` set per study (29 of 75 have a genuine, study-generated, calculable effect estimate; all 75 are qualitative-synthesis eligible). See `05_analysis/descriptive/EVIDENCE_MAP_README.md` for the full derivation/judgment-call rationale. |
| 11 | Quantitative feasibility assessment | Not started — and deliberately has no speculative tooling built ahead of it. `ANALYSIS_PLAN.md` §2's decision tree is a corpus-level methodological judgment applied per candidate synthesis family (`PROJECT_SPEC.md` §8), not a per-study mechanical fact; the decision tree itself already **is** the complete process, so there is nothing safe to automate the way Phase 10's `build_evidence_map.py` helps with mechanical fields. See `05_analysis/descriptive/EVIDENCE_MAP_README.md`'s closing section. |
| 12 | Meta-analysis where justified | **R template built 2026-09-12** (`08_code/R/01_meta_analysis.R`) implementing `ANALYSIS_PLAN.md` §§5–8 (random effects, heterogeneity + prediction interval, subgroup analysis gated on a minimum study count, meta-regression gated at the ~10-studies-per-moderator threshold). **Not yet run against real data — no R interpreter was available in the environment that wrote it** (see `08_code/R/README.md`'s "Status" section); validate it before trusting any output. Blocked on Phase 11 actually judging a synthesis family eligible. |
| 13 | Structured quantitative synthesis of unpoolable evidence (SWiM) | **Template built 2026-09-12** (`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`) — deliberately does not reproduce SWiM's own reporting-guideline checklist verbatim (unverified against the publisher, same caveat as the risk-of-bias tools); check the official guideline directly. Blocked on Phase 11 routing a family here instead of to meta-analysis. |
| 14 | Sensitivity analysis | **R template built 2026-09-12** (`08_code/R/02_sensitivity_analysis.R`), implementing the five specific checks `ANALYSIS_PLAN.md` §10 names. Same untested-in-this-environment caveat as Phase 12. |
| 15 | Publication bias assessment where appropriate | **R template built 2026-09-12** (`08_code/R/03_publication_bias.R`), enforcing `ANALYSIS_PLAN.md` §9's ~10-studies-per-family threshold as a hard refusal rather than a suggestion. Same untested-in-this-environment caveat as Phase 12. |
| 16 | PRISMA reporting | **Checklist built 2026-09-12** (`06_outputs/prisma/PRISMA_2020_CHECKLIST.md`) — all 27 items mapped to where each is already substantively addressed in this repository, so manuscript drafting is writing up what's recorded, not starting blank. Two items (funding, competing interests) have no home yet and need the researcher's actual disclosures. Exact item wording should be checked against the official PRISMA 2020 checklist before final submission. |

**Current phase (updated 2026-09-12): 1–5 complete; Phase 6 (full-text screening) and Phase 8 (full extraction) in progress, live; Phase 7 superseded; Phase 10 (evidence classification) populated for all 62 studies extracted so far; Phase 9 (risk of bias) deliberately not yet applied to any study; Phases 12–16 scaffolding built.** Phase 3 closed by researcher decision,
with documented gaps (SSRN and Westlaw/Lexis never searched). Phase 5's
human `reviewer_2` pass is done — see the flagged caveat on its near-total
agreement rate with reviewer_1 in the Phase 5 row above, which any
manuscript output should disclose alongside the result rather than
presenting as an unremarkable independent second pass.
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
`CHANGELOG.md`): **3,062 include / 22,557 exclude / 603 unsure**. The
human `reviewer_2` pass over the 3,665 include+unsure records is now
complete (`CHANGELOG.md` 2026-09-12): **3,659 include / 6 exclude, zero
conflicts** by the strict reviewer_1-vs-reviewer_2 disagreement definition
in `DATA_DICTIONARY.md`. `final_decision` is populated for all 3,665
records on this basis. **Flagged, not hidden**: this agreement rate is
unusually high for an independent second pass and the review turnaround
was fast relative to the volume — documented in `CHANGELOG.md` and the
Phase 5 row above so it's visible to anyone assessing this review's rigor,
including in any manuscript reporting this step. Phase 6 (full-text
screening) is now live and ongoing: of the 3,659-record included set,
**156 have been screened (77 include / 79 exclude)**, with the researcher
supplying full-text PDFs on a rolling basis expected to continue for over
a month — see the Phase 6 row above for the exclusion-reason breakdown.
Phase 7 (pilot extraction) was superseded by the researcher's explicit
instruction to proceed directly to full extraction on every full-text
include rather than drawing a separate pilot subsample first. Phase 8
(full extraction) is likewise live: **75 studies (S001–S075) are fully
extracted** into `extraction_database.csv` against `CODEBOOK.md`'s full
92-field schema, with only 2 flagged studies awaiting full-text
re-upload (never fabricated from memory) separating this count from the
77 current full-text includes. Phase 9 (risk of bias) is intentionally
not yet applied to any of the 62 — `risk_of_bias_tool` is identified per
study but `risk_of_bias_rating` is deliberately left blank pending the
official version of each appraisal instrument, per `RISK_OF_BIAS.md`'s
explicit prohibition on reconstructing a validated tool from memory; this
is a disclosed limitation of the review's current state, not an
oversight. Phase 10 (evidence classification) has been run against all
75 extracted studies, both the mechanically-derivable fields (via
`build_evidence_map.py`) and the judgment-call fields (`outcome_family`,
`evidence_level`, and the two synthesis-eligibility flags) filled by hand
per study — see `05_analysis/descriptive/EVIDENCE_MAP_README.md`. Phase
11 (quantitative feasibility) is deliberately left without
speculative tooling, since its decision tree is a corpus-level judgment
call that already **is** the complete process — see the Phase 10/11 rows
above. Phases 12, 14, and 15 have R analysis templates
(`08_code/R/`) implementing `ANALYSIS_PLAN.md`'s already-specified models
and thresholds, explicitly marked **not yet run** (no R interpreter was
available to test them); Phase 13 has a SWiM synthesis template; Phase 16
has the full PRISMA 2020 checklist pre-mapped to where each item is
already addressed in this repository. All of Phases 12–16 remain blocked
on real evidence existing to run them against.

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

`02_screening/full_text/full_text_screening_database.csv` (Phase 6, a
separate file — see `DATA_DICTIONARY.md` and `FULL_TEXT_README.md` for why
`screening_database.csv`'s own `full_text_decision`/reviewer columns are
not reused):

```
record_id, title, authors, year, doi, url, full_text_status,
full_text_location, full_text_decision, exclusion_reason,
exclusion_reason_detail, reviewer_1, reviewer_2, conflict, final_decision,
notes
```

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
