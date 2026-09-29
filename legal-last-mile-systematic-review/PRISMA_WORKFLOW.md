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
rigor. **`exclude_spotcheck_sample.csv` (120-record random QA sample,
fixed seed) has now been manually reviewed (2026-09-12)** — 119 of 120
exclusions checked out as correctly reasoned; 1 (`R88194172BEF6`, a
Sicilian wastewater-reservoir bacterial-removal modeling study for
agricultural irrigation reuse) had a stored `ai_rationale` that did not
match its actual title/abstract (it read "Oncology biomarker study;
unrelated to water/sanitation," evidently misaligned during the
39-parallel-batch merge) and an inaccurate `exclusion_reason` (`E01`
instead of `E07`, since the actual content is an irrigation/agricultural
water-reuse study, not an unrelated topic). The `exclude` decision itself
was still correct — corrected the code and rationale in both
`screening_database.csv` and `exclude_spotcheck_sample.csv`, and updated
the title/abstract exclusion-reason breakdown in `prisma_flow.md`
accordingly (E01: 16,667→16,666; E07: 1,039→1,040). No other discrepancy
was found in the 120-record sample. **Follow-up (2026-09-12): scanned the
entire 22,557-record exclude pool's `ai_rationale` text for the same
mismatch signature** (a rationale citing a domain wholly foreign to
water/sanitation/legal-administrative research), rather than relying on
another random sample — 74 records matched; a diverse 18-record manual
check against actual titles/abstracts confirmed all 74 are genuine
off-topic records correctly excluded (e.g., 8 near-duplicate stock-market
newsletter records for ticker "SJW"/South Jersey Industries), not further
instances of the corruption. See `CHANGELOG.md` (cont. 12) for the full
method and result. The 1,259 records without a real abstract were
deliberately left undecided (title-only triage remains
non-binding per `title_only_triage_memo.md`, still only covering the
original 37). |
| 6 | Full-text screening, standardized exclusion reason per record | **Closed 2026-09-28 by researcher decision** (institutional access to further providers exhausted). 2,276 of 3,659 title/abstract includes were assessed (62.2%): **1,159 include / 1,117 exclude**; 1,383 were never assessed (`not_retrievable` or `wrong_file_retrieved`). Every decision was made by the AI reviewer (`reviewer_1`) against `INCLUSION_EXCLUSION.md`'s E01–E12 codes; a human `reviewer_2` has confirmed only the first 100 includes (S001–S100) and no excludes. 73 decided rows carry no reviewer label. Exclusion breakdown: `README.md`; current figures: `00_admin/CURRENT_FIGURES.md`; tooling: `code/screening/`; a prioritised human-review queue: `02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`. Earlier dated status text: `11_archive/PRISMA_WORKFLOW_before_retirement_2026-09-28.md`. |
| 7 | Pilot extraction (~10 studies) | **Superseded by full extraction (Phase 8)** — the researcher authorised extracting all full-text includes directly rather than a separate pilot subsample. `code/extraction/select_pilot_sample.py` and `PILOT_EXTRACTION.md` remain available if a formal pilot-disagreement check is wanted. |
| 8 | Full extraction | **Complete for the closed Phase 6 population.** 1,159 studies extracted by the AI against the 92-field `CODEBOOK.md` (`03_extraction/extracted_data/extraction_database.csv`, plus a 93rd `record_id` column added 2026-09-28); IDs run S001–S1164 with retired gaps (S227, S233, S299, S356, S399). 69 studies were extracted from abstract or metadata only (`05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv`); there is **no second-extractor pass**. Companion reports of one study are linked in `03_extraction/extracted_data/linked_reports_2026-09-28.csv`. Scripts that wrote the data: `code/provenance/`. Earlier dated status text (a 64,860-character accretion): `11_archive/PRISMA_WORKFLOW_before_retirement_2026-09-28.md`. |
| 9 | Risk of bias | **Complete corpus-wide as of 2026-09-28**, by rule-based batch appraisal from the extracted fields (not a signalling-question read of each paper), using the design-matched instruments in `RISK_OF_BIAS.md` (RoB 2, ROBINS-I, JBI, CASP, MMAT, AMSTAR 2) and, for 447 doctrinal/documentary studies, the project's own **non-validated** Legal Institutional Evidence Appraisal Framework. Tool distribution: `00_admin/CURRENT_FIGURES.md`. Method and limits: `RISK_OF_BIAS.md` §4, `04_quality/appraisal_forms/`, `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`. No human has reviewed the ratings. Earlier dated status text: `11_archive/PRISMA_WORKFLOW_before_retirement_2026-09-28.md`. |
| 10 | Evidence classification | **Populated for every extracted study** (`05_analysis/descriptive/evidence_map.csv`; builder `code/analysis/build_evidence_map.py`; guide `EVIDENCE_MAP_README.md`). `study_design_class` normalised to the documented enum on 2026-09-28. `mechanism_family` and `outcome_family` remain free-text labels (236 and 127 distinct values); a draft controlled vocabulary is proposed, not adopted, in `05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`. Eligibility flags: `00_admin/CURRENT_FIGURES.md`. |
| 11 | Quantitative feasibility assessment | **Complete 2026-09-28** (`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`). `ANALYSIS_PLAN.md` §2's decision tree was applied to every `effect_sizes.csv` row. **Verdict: no synthesis family clears the bar for meta-analysis; all three route to Phase 13 (SWiM).** 62 effect-size rows (Family A 20, B 6, C 20, and 16 reasoned non-fits), none pooled. Follow-ups: `phase11_blank_family_resolution_2026-09-28.md`, `phase11_pooling_feasibility_S526_S539_S749.md`, `effect_sizes_remining_2026-09-28.md`. One row (S589) is an unresolved eligibility inconsistency (`00_admin/DECISIONS_AND_OPEN_ITEMS.md` A1). |
| 12 | Meta-analysis where justified | **Not run — nothing to pool.** R template `08_code/R/01_meta_analysis.R` implements `ANALYSIS_PLAN.md` §§5–8 and was test-run 2026-09-28 against the real (correctly refusing) data and synthetic fixtures, which found and fixed a real bug (`08_code/R/README.md`). Blocked only by Phase 11's verdict. |
| 13 | Structured quantitative synthesis of unpoolable evidence (SWiM) | **Complete 2026-09-28:** `06_outputs/supplementary/family_A_swim_synthesis_2026-09-28.md`, `family_B_…`, `family_C_…`, built on `SWIM_SYNTHESIS_TEMPLATE.md` (the template does not reproduce SWiM's checklist wording; check the official guideline). They report direction of association with disclosed judgment calls, corrected on 2026-09-28 for a sign-versus-valence error. Not effect estimates, not GRADE-certainty conclusions. |
| 14 | Sensitivity analysis | **Done for the SWiM syntheses** — `code/analysis/sensitivity_analysis.py` → `05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md` (drops abstract-only extractions, S589, collapses linked reports, drops Family A's coding judgment calls; stated tests). The R template `08_code/R/02_sensitivity_analysis.R` (`ANALYSIS_PLAN.md` §10) has nothing pooled to run against. |
| 15 | Publication bias assessment where appropriate | **Not applicable yet.** `08_code/R/03_publication_bias.R` enforces `ANALYSIS_PLAN.md` §9's ~10-studies-per-family threshold as a hard refusal (test-run 2026-09-28; two crash bugs fixed). No family reaches the threshold with pooled data. |
| 16 | PRISMA reporting | **Checklist built** (`06_outputs/prisma/PRISMA_2020_CHECKLIST.md`): 27 items mapped to where each is addressed in this repository; item wording still to be checked against the official checklist. Items 25 (funding) and 26 (competing interests) await the researcher's disclosures (`00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md`). Generated manuscript pieces: `07_manuscript/draft/GENERATED_MANUSCRIPT_PIECES_2026-09-29.md`. |

**Current status (rewritten 2026-09-28; the previous dated snapshot text is preserved in `11_archive/PRISMA_WORKFLOW_before_retirement_2026-09-28.md`).** Phases 1–5 are complete (search closed 2026-09-11 with disclosed gaps — SSRN and Westlaw/Lexis never searched; 34,594 raw records → 27,481 unique; title/abstract screening double-reviewed, 3,659 include / 6 exclude, with an unusually high 99.8% reviewer agreement that any manuscript must disclose alongside the result). Phase 6 is closed at **1,159 include / 1,117 exclude**; Phases 8–11 and 13 are complete for that corpus; Phase 12 has nothing to pool. The live numbers are generated, not typed: `00_admin/CURRENT_FIGURES.md` (checked by `code/analysis/verify_repository.py`). What is verified by a human and what is not: `AI_USE_STATEMENT.md`.

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

`06_outputs/prisma/prisma_flow.md` is the live flow-diagram source; it carries the real, dated counts for identification, title/abstract screening and full-text screening (closed: 2,276 of 3,659 assessed, **1,159 include / 1,117 exclude**). Read that file for the current diagram.
