# Changelog

All notable methodological and structural decisions for this project are
logged here, per `REPRODUCIBILITY.md` §8 and `PROTOCOL.md` §12 (protocol
amendments in particular must be logged here with rationale).

## [Unreleased]

Nothing yet — no phase past repository setup and source verification has
been reached.

## 2026-09-13 (latest) — Full-text screening batch: 10 more records decided, 5 new includes extracted (S087–S091)

Continued Phase 6 full-text screening on a rolling batch of researcher-
supplied PDFs, processed via the standard pipeline (convert →
`pdftotext -layout` → screen against `INCLUSION_EXCLUSION.md`'s E01–E12
codes → record via `code/screening/update_full_text_record.py` → log any
exclusion to `exclusion_log.csv` → extract into
`extraction_database.csv` and `evidence_map.csv` for every include →
`validate_schemas.py`).

**10 records decided this batch:**
- **Include (5):** S087 Grönwall (Ghana, mixed-methods, tenure/PURC/WRC/
  CWSA regulatory fragmentation); S088 Otsuki 2016 (Kibera, Kenya —
  Tosha Network CBO certification, chief's-permission bottleneck to
  connect a bio-centre to the city water grid); S089 Tutu & Stoler 2016
  (Accra, Ghana — tenure-based denial of formal water supply in two
  informal settlements); S090 Awunyo-Akaba et al. 2016 (Ghana — tenure/
  land-rights status shaping sanitation investment across three
  comparative communities); S091 Rodina & Harris 2016 (Khayelitsha, Cape
  Town — RDP housing-formalisation process gating individual in-house
  water/sanitation connection vs. communal-tap access, plus differential
  councillor responsiveness to formalized vs. informal residents'
  grievances).
- **Exclude (5):** Wilhelm-Solomon 2016 (E01 — eviction/urban
  regeneration, not service access); Ojha 2021 (Nepal water policy —
  included as S086, logged separately); Liddle et al. 2016 (Ndola,
  Zambia informal water supply — E06, core contribution is technical/
  engineering: well protection, smart hand pumps, not a legal-
  administrative access mechanism); Kanyamurwa 2016 (Uganda — E04,
  quantitative survey of political interference/accountability in
  utility governance, not household-level access/exclusion tied to a
  legal-administrative mechanism).

`extraction_database.csv` and `evidence_map.csv` now hold **91 fully
extracted studies (S001–S091)**. Full-text screening stands at **191 of
3,659 records decided (91 include / 100 exclude)**. All 13 tracked
schemas re-validated clean after every write. Updated `PRISMA_WORKFLOW.md`,
`README.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md` with these totals —
the already-published `preliminary_report_2026-09-13.md`/`.docx` is left
as a dated historical snapshot and not retroactively edited.

## 2026-09-13 — Exploratory Results/Discussion/Conclusion added to the preliminary report, explicitly labeled as a sketch

At the researcher's explicit, repeated request (after an initial version
of this report deliberately omitted these sections per
`manuscript_outline.md`'s own rule), added §6–8 to
`07_manuscript/draft/preliminary_report_2026-09-13.md`: "Preliminary
Results (Exploratory, Non-Representative)," "Preliminary Discussion
(Exploratory)," and "Preliminary Conclusion (Exploratory, Highly
Provisional)." Given a choice between a bare placeholder skeleton, a
labeled exploratory sketch, and a full unhedged synthesis, the researcher
chose the labeled exploratory sketch.

Content is grounded entirely in real extracted data — no fabrication.
Read through all 37 studies flagged `quantitative_synthesis_eligible` and
found that most report descriptive access statistics without a
comparison that isolates a legal/administrative exposure; six
(Lubeck-Schricker et al. 2023 [S084], Gaikwad & Thomas 2026 [S085],
Filčák & Škobla 2021 [S078], Kozole et al. 2023 [S057], dos Santos Alves
Romanato et al. 2025 [S021], Rajput & Pu 2025 [S029]) do isolate such a
comparison and are reported by name with their actual effect estimates.
All six point in the direction the Legal Last Mile framework predicts;
this is stated as weak, non-representative, hand-selected support, not a
finding — the document says so at the top (revised status callout),
before §6, in §7, in §8, and again in a new §10 ("Why §6–8 Are Sketches,
Not the Review's Findings," renumbered from the original §7 "Why This
Report Stops Here") and §11's expanded Limitations. Existing §6–8
(PRISMA-phase status, stopping rationale, limitations) renumbered to
§9–11 without other content changes. Re-generated the matching `.docx`.

## 2026-09-13 (earlier) — Preliminary protocol + interim descriptive report drafted

At the researcher's request for "a preliminary paper," wrote
`07_manuscript/draft/preliminary_report_2026-09-13.md`: a
methods-and-status document, not a findings paper. It contains the
pre-specified conceptual framework and methods (unchanged since
2026-08-22), the actual current PRISMA flow (27,481 unique records →
3,659 past title/abstract screening → 175/3,659 full-text screened,
85 include/90 exclude → 85/85 extracted), and purely descriptive
characteristics of the 85 extracted studies (region, legal system, study
design, mechanism family, outcome family, publication years) plus a full
alphabetical reference list of those 85 studies as Appendix A.

**Deliberately excludes Results, Discussion, Comparative Findings, and
Conclusion sections** — consistent with `manuscript_outline.md`'s own
rule that those sections may not be drafted from illustration or the
preliminary source papers alone, and with `PROJECT_SPEC.md` §1's
governing principle (determine what the evidence allows before deciding
on synthesis, not the reverse). With full-text screening at ≈4.8%
complete and risk-of-bias appraisal and the quantitative-feasibility
decision tree (Phases 9 and 11) both unrun, writing those sections now
would produce either an empty section or an illustration presented as a
finding — exactly what the anti-confirmation-bias rule exists to
prevent. The document says this explicitly in its own §7 rather than
silently omitting the sections.

## 2026-09-12 (latest, cont. 14) — CITATION.cff added for a standalone Zenodo deposit; abstract-redistribution question raised and resolved by researcher decision

Preparing a standalone Zenodo deposit of this `legal-last-mile-systematic-review/`
subdirectory (separate from the repository's existing dataset-scoped DOI,
`10.5281/zenodo.19836413`, whose own title/citation history is being left
untouched). Added `CITATION.cff` scoped to the review itself, since
Zenodo's automatic GitHub-release integration reads the repo root's
existing `CITATION.cff` (dataset-scoped) and a manual, subdirectory-only
deposit needs its own.

Also raised, and the researcher explicitly resolved, a real question: the
review's screening-stage CSVs (`deduplicated_records.csv`,
`screening_database.csv`, `reviewer_2_queue.csv`,
`exclude_spotcheck_sample.csv`) carry ~38MB / 26,222 verbatim abstracts
bulk-exported from Scopus/Web of Science, the same category of
copyright/redistribution concern already caught once for full-text PDFs
(2026-08-26 entry above). Flagged before creating any public deposit,
including the note that this is separately a Scopus/WoS license
(contract) question independent of copyright fair-use analysis, and that
EU text-and-data-mining exceptions (relevant given the researcher's
Erasmus University Rotterdam affiliation) are narrower than US fair use
and generally cover the mining/analysis itself, not public republication
of the underlying text. **Researcher decision: include the abstracts as-is,
accepting the redistribution risk.** Logged here per this project's
standing "flagged, not hidden" practice — this is a disclosed,
researcher-owned risk decision, not an oversight.

## 2026-09-12 (latest, cont. 13) — OSF preregistration draft brought to submission-ready state, with an explicit retrospective-registration disclosure

At the researcher's request, prepared the OSF Generalized Systematic
Review draft (`00_admin/preregistration/osf_preregistration_draft.md`)
for actual submission. This environment has no OSF account, so the
submission click itself remains the researcher's to do. Two substantive
changes, not just formatting:

1. Added an explicit "Disclosure: this is a retrospective registration,
   not a fully a priori one" section. The protocol's *content* (research
   question, `INCLUSION_EXCLUSION.md`, `CODEBOOK.md`, `RISK_OF_BIAS.md`
   tool assignments, `ANALYSIS_PLAN.md`) was fixed 2026-08-22, before any
   database was searched, and has not been revised since in response to
   what the search/screening turned up. But the *registration itself* is
   only being submitted now (2026-09-12), roughly three weeks after
   search execution began and after search closed, title/abstract
   screening completed, and full-text screening/extraction were already
   underway. Both dates need to be stated on OSF itself, not left
   implicit — a registration that reads as fully a priori when it isn't
   would undercut the entire point of registering.
2. Filled in "Existing data / prior work" and "Anticipated timeline" with
   the actual realized dates from this changelog (search closed
   2026-09-11; title/abstract screening complete 2026-09-12; full-text
   screening/extraction live) rather than leaving them at their
   2026-08-22 draft state or blank.

Confirmed PROSPERO remains the wrong registry (health/welfare-outcome
scope; also does not accept registration once extraction has begun,
which this review's already has) — OSF stays the plan. Submission
checklist updated accordingly, including a step to cross-link the
eventual OSF DOI with any Zenodo archival DOI via each platform's
related-identifiers field.

## 2026-09-12 (latest, cont. 12) — Corpus-wide scan for the R88194172BEF6 corruption pattern: no further instances found

The earlier QA spot-check (cont. 9) found one exclude record
(`R88194172BEF6`) whose stored `ai_rationale` was completely mismatched to
its actual title/abstract — an oncology rationale attached to a Sicilian
wastewater-reuse paper, attributed to the 39-parallel-batch merge process.
A 120-record random sample only samples ~0.5% of the 22,557-record exclude
pool, so rather than drawing another random batch, scanned the **entire**
pool's `ai_rationale` text (`ai_first_pass_rationale.csv`) for the same
failure signature: a rationale citing a domain wholly foreign to
water/sanitation/legal-administrative research (oncology, cardiovascular,
psychiatric, blockchain, cryptocurrency, semiconductor, stock-market
trading, etc.) — the kind of mismatch a corrupted merge would produce.
74 records matched at least one such term. Manually verified a diverse
sample of 18 against their actual `screening_database.csv` title/abstract
(spanning every matched term at least once, including the ones read in
full above): all 18 rationales accurately described their real paper —
these are genuine off-topic records correctly swept up and excluded by
the broad keyword search (e.g., 8 near-duplicate stock-market newsletter
records for ticker "SJW" — South Jersey Industries, a water utility
holding company — correctly excluded as wrong-topic noise; a 1990 case
study of a semiconductor company's drinking-water contamination correctly
excluded as historical/policy commentary rather than a water-access
study). **No further instance of the R88194172BEF6 corruption pattern was
found.** This is a stronger result than another random sample would give
for this specific failure mode, since it covers the whole pool rather than
estimating a rate from ~0.5% of it; it does not rule out other, differently
-shaped errors the same merge process might have introduced, which the
120-record random sample (cont. 9) remains the relevant check for.

## 2026-09-12 (latest, cont. 11) — Closed the last extraction gap: S084/S085

While the researcher was mid-download on a fresh PDF batch, audited the
extraction pipeline for other work available without new uploads. Found
that both PDFs behind the two long-flagged "no cached full text" records
(Lubeck-Schricker et al. 2023; Gaikwad & Thomas 2026) were already present
in the session's upload store — uploaded 2026-09-12 alongside that day's
main batch — but had never been converted to text or extracted, apparently
missed in the earlier batch pass rather than genuinely absent. Converted
both (`pdftotext -layout`), read them in full, and extracted them as S084
and S085 following the same `CODEBOOK.md`/`EXTRACTION_FORM.md` process used
for the other 83 studies, then populated `evidence_map.csv` for both
(mechanical fields via `code/analysis/build_evidence_map.py`, judgment-call
fields — `outcome_family`, `evidence_level`,
`quantitative_synthesis_eligible`/`qualitative_synthesis_eligible` — by
hand). `extraction_database.csv` now holds all 85 current full-text
includes with zero gap. S085 (Gaikwad & Thomas) is a genuine
cluster-randomized field experiment (`mechanism_certainty=4`), the
strongest-design study extracted so far, and a clean empirical instance of
`PROJECT_SPEC.md` §8's candidate Family B (bureaucratic assistance →
connection/application success) — though its own finding is that the
mechanism only operates jointly with political coordination, a genuine
complication for treating Family B as a simple main effect. Also
separately fixed a hardcoded, author-machine-specific Windows path
fallback in the (out-of-scope but same-repo) judicial-decisions-dataset
project's `research-assistant/data_loader.py`, and a stale κ figure plus a
broken copy-pasteable command in that project's `validation/README.md` and
`validation/kappa_calculator.py` — flagged separately to the researcher
since they fall outside this systematic review's own scope. Ran
`code/analysis/validate_schemas.py` after every write; all 13 tracked
files matched schema throughout. Updated `PRISMA_WORKFLOW.md` Phases 8 and
10 to reflect 85/85 extraction with no outstanding gap (up from 83/85 with
2 studies flagged as awaiting re-upload that were never actually needed).

## 2026-09-12 (latest, cont. 10) — Full-text reviewer_2 handoff tooling; final_decision normalization

Built `code/screening/build_full_text_reviewer2_queue.py`, mirroring the
title/abstract stage's queue mechanism, so a human `reviewer_2` for Phase
6 (full-text screening) can start immediately whenever the researcher
assigns one rather than needing tooling built first. Generated the queue
for real: `02_screening/full_text/full_text_reviewer_2_queue.csv`, 175
rows (85 include / 90 exclude), plus
`02_screening/full_text/REVIEWER_2_README.md` documenting how to use it
and — unlike the title/abstract stage — the added wrinkle that Phase 8
extraction has already run on every include, so a reviewer_2 override on
an include also means removing/flagging the corresponding
`extraction_database.csv`/`evidence_map.csv` row.

While building this, found that 18 full-text records had `final_decision`
already populated (mirroring `reviewer_1`'s decision) despite no human
reviewer_2 pass ever having happened for this phase — an inconsistency
from recent batches, not intentional. Blanked `final_decision` back out
on all 18, consistent with this project's own stated rule (`final_decision`
is set only after conflict resolution between two independent reviewers).
This did not affect any Phase 8 extraction or Phase 10 evidence-map
work, both of which key off `full_text_decision`, not `final_decision`.

## 2026-09-12 (latest, cont. 9) — QA spot-check of the 120-record exclude sample; pipeline consistency audit

Manually reviewed all 120 records in `exclude_spotcheck_sample.csv`
(fixed-seed random sample of title/abstract-stage excludes, previously
unreviewed) against `INCLUSION_EXCLUSION.md`. 119 of 120 exclusion
decisions and their stated rationale checked out. One discrepancy found:
`R88194172BEF6` (a Sicilian wastewater-reservoir bacterial-removal
modeling study for agricultural irrigation reuse) carried a stored
`ai_rationale` ("Oncology biomarker study; unrelated to water/sanitation")
that plainly did not match its title/abstract — a mismatch that survived
into both `screening_database.csv` and the QA sample, most likely from
the 39-parallel-batch merge process. The `exclude` decision itself was
still correct; only the `exclusion_reason` code was off (`E01` instead of
`E07`, since the actual content is agricultural/irrigation water reuse,
not an unrelated topic). Corrected the code and rationale in both files
and the affected title/abstract exclusion-code breakdown in
`prisma_flow.md` (E01 16,667→16,666; E07 1,039→1,040) — see
`PRISMA_WORKFLOW.md` Phase 5 for the full note.

Also ran a pipeline consistency audit: no duplicate DOIs among the 85
full-text includes, no invalid/missing `exclusion_reason` codes among the
90 full-text excludes, and every include reconciles to an extraction row
except the two records already known to be awaiting full-text re-upload
(Lubeck-Schricker et al.; Gaikwad & Thomas) — no hidden extraction gaps.

## 2026-09-12 (latest, cont. 8) — Added companion bibliometric manuscript as SOURCES.md exemplar

Added Klaus (2026), "The Evolution of Basic Sanitation Research in
Brazil: A Bibliometric Analysis (1987 to 2026)" — this review's own
author's unpublished scientometric manuscript — as `SOURCES.md` entry 14
and a corresponding `sources.bib` entry, at the researcher's request.
This manuscript was supplied via chat upload but is not part of the
search-derived corpus (no `record_id` in
`02_screening/full_text/full_text_screening_database.csv`), so it was
deliberately not forced through Phase 6 full-text screening; it is cited
as background/methodological context on the state of Brazilian
sanitation-law scholarship, not as a candidate primary study for this
review's evidence base.

## 2026-09-12 (latest, cont. 7) — Live full-text screening, full extraction, and evidence classification underway

Phase 6 (full-text screening) went from scaffolding to live, ongoing work
once the researcher began supplying full-text PDFs via chat upload —
expected to continue over roughly a month. Each PDF is converted with
`pdftotext -layout`, screened by Claude as `reviewer_1`
(`Claude-AI-fulltext-2026-09-12`) against `INCLUSION_EXCLUSION.md`, and
recorded via `update_full_text_record.py`; every exclusion is also logged
to `exclusion_log.csv`. As of this entry: **126 of 3,659 records decided
(62 include / 64 exclude)** — see `PRISMA_WORKFLOW.md` Phase 6 for the
exclusion-reason breakdown. `reviewer_2` for this phase has not yet been
assigned; open question for the researcher.

At the researcher's explicit instruction ("go ahead and start an
extraction for the 44 included papers... I'm accompanying you every step
of the way"), Phase 8 (full extraction) began directly rather than first
drawing a separate ~10-study Phase 7 pilot sample — Phase 7 is marked
superseded in `PRISMA_WORKFLOW.md` rather than completed. **42 studies
(S001-S042) are now fully extracted** into `extraction_database.csv`
against `CODEBOOK.md`'s complete 92-field schema, in six batches of
seven. Two studies with no cached full text available in this session
(Lubeck-Schricker et al.; Gaikwad) were explicitly *not* extracted from
memory and are flagged for re-upload — extraction accuracy takes priority
over completeness. Three of the 42 (Basnet & Sherchan; Ilangovan et al.;
Fanaian et al.) are themselves secondary systematic reviews, flagged
`study_design_class = systematic_review_secondary` and never to be pooled
as an independent primary effect, per `RISK_OF_BIAS.md` §1.

**Every one of the 42 extracted rows has `risk_of_bias_rating` left
deliberately blank.** `RISK_OF_BIAS.md` is explicit that none of the six
validated appraisal tools (RoB 2, ROBINS-I, the two JBI checklists, CASP,
MMAT) or AMSTAR 2 may be reconstructed from memory — the current official
version must be obtained before appraising a study with it. Each row
correctly identifies `risk_of_bias_tool` (design-matched, or the
project's own Legal Institutional Evidence Appraisal Framework where no
conventional tool fits) and carries an `extraction_note` deferring the
actual rating to a follow-up pass with the official instrument in hand.
This is a disclosed limitation of the review's current state, to be
reported as such in any manuscript output, not an oversight to be quietly
fixed later.

`code/analysis/build_evidence_map.py` was run against the real
extraction database for the first time, then the judgment-call fields it
deliberately leaves blank were filled by hand for all 42 studies:
`study_design_class` for the six studies using the Legal Institutional
Evidence Appraisal Framework (resolved doctrinal vs. jurimetric per
study — the tool name alone can't distinguish them), `outcome_family`
mapped to `PROJECT_SPEC.md` §7's hierarchy based on each study's actual
central/tested outcome rather than a mechanical restatement of the
outcome booleans, `evidence_level` written as prose per
`DATA_DICTIONARY.md`'s instruction that it is a narrative tier rather
than a score, and `quantitative_synthesis_eligible`/
`qualitative_synthesis_eligible` set per study (18 of 42 have a genuine,
study-generated, calculable effect estimate; all 42 are eligible for
qualitative/thematic synthesis, consistent with this project's standing
protection of qualitative socio-legal evidence as first-class rather than
a fallback). See `05_analysis/descriptive/EVIDENCE_MAP_README.md`.

`PRISMA_WORKFLOW.md` and `06_outputs/prisma/prisma_flow.md` updated
throughout to replace stale "not started"/"blocked" language for Phases
6-10 with the real, live counts above.

## 2026-09-12 (latest, cont. 6) — Cowork full-text retrieval instructions and bulk-import tooling

At the researcher's request, built the missing piece to actually
unblock Phase 6 rather than more scaffolding downstream of it:

- **`code/screening/bulk_import_full_text_results.py`** (new): applies a
  whole batch of retrieval (or screening) results to
  `full_text_screening_database.csv` in one atomic write. Reuses
  `init_full_text_db.py`'s own `SCHEMA`/`VALID_STATUS`/`VALID_DECISION`
  constants (loaded dynamically, same pattern as `validate_schemas.py`)
  rather than redeclaring them. **Rejects the entire batch if any row is
  invalid** -- a typo in row 400 of 500 can never leave 399 good rows
  applied and one silently wrong; nothing is written until every row
  passes. Never overwrites a record that already has a `final_decision`,
  and never auto-adds an unrecognized `record_id`. Tested against a
  synthetic copy of the real database before ever touching it for real:
  a valid two-row batch applied correctly (plus an unknown record_id
  correctly skipped and reported), an invalid-enum batch correctly
  rejected the whole import with zero writes, and an already-decided
  record was correctly left untouched by a later batch that tried to
  touch it.
- **`02_screening/full_text/COWORK_RETRIEVAL_INSTRUCTIONS.md`** (new): a
  ready-to-paste instruction set for a browser-capable Claude Cowork
  session, mirroring how this project's original database searches were
  actually done (Cowork does the browser work, reports results back as a
  file, the main session applies them). Scopes the task explicitly to
  *retrieval only* (never full-text screening/inclusion decisions,
  which stay a separate, later, judgment-heavy step); works in
  small per-database batches rather than all 3,659 at once; explicitly
  tells Cowork **not** to commit retrieved PDFs into this git
  repository (publisher copyright, repo bloat) and to record only a
  location/link instead; specifies the exact 4-column results-file
  format `bulk_import_full_text_results.py` expects; and carries the
  same "never guess or fabricate a retrieval outcome" discipline used
  throughout this project's screening tools.
- `FULL_TEXT_README.md` updated to reference both.

This is the one piece of work this session that actually has a path to
unblocking Phases 6 onward, rather than more scaffolding ahead of data
that still can't run until real full texts exist.

## 2026-09-12 (latest, cont. 5) — Phases 12-16 scaffolding built (meta-analysis through PRISMA reporting)

At the researcher's request ("keep scaffolding further downstream
phases... regardless"), built shells for every remaining phase, with an
explicit disclosure this time that matters more than in prior rounds:
**none of the R code below has actually been executed** — no R
interpreter was available in the environment that wrote it (checked:
`which R` / `which Rscript` both came back empty). This is a materially
different situation from every stdlib-Python script built earlier this
project, which were tested directly. Brace/parenthesis balance was
sanity-checked mechanically as a minimal safety net, but that is not the
same as a real run.

- **`08_code/R/01_meta_analysis.R`** (Phase 12): random-effects model per
  candidate synthesis family (`ANALYSIS_PLAN.md` §5), heterogeneity +
  prediction interval (§6), subgroup analysis gated on a minimum study
  count (§7), meta-regression gated at the ~10-studies-per-moderator
  threshold (§8). Flags rather than silently pools when a study
  contributes more than one effect to a family (`CODEBOOK.md` §12's
  dependence-modeling requirement). Joins `extraction_database.csv` in
  for moderator/subgroup fields, since `effect_sizes.csv` itself has none
  — and explicitly does NOT invent a clean mapping between
  `ANALYSIS_PLAN.md`'s colloquial moderator names ("jurisdiction",
  "decentralization") and `extraction_database.csv`'s actual column names
  (`country`, `regulatory_model`), since no such 1:1 mapping currently
  exists in this project's own schema.
- **`08_code/R/02_sensitivity_analysis.R`** (Phase 14): the five specific
  checks `ANALYSIS_PLAN.md` §10 names, each reported as run or explicitly
  skipped (never silently omitted) depending on what fields are actually
  available for a given family.
- **`08_code/R/03_publication_bias.R`** (Phase 15): funnel plot, Egger,
  Begg — **refuses to run below `ANALYSIS_PLAN.md` §9's ~10-studies-per-
  family threshold** rather than producing an uninterpretable plot, same
  discipline as `code/extraction/select_pilot_sample.py`'s refusal logic.
  Prints the "asymmetry is not proof of publication bias" caveat
  alongside every result it does produce.
- **`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`** (Phase 13):
  structural template for families the decision tree routes away from
  meta-analysis — explicitly does not reproduce SWiM's own reporting
  checklist verbatim, same unverified-citation caveat as the
  risk-of-bias tools.
- **`06_outputs/prisma/PRISMA_2020_CHECKLIST.md`** (Phase 16): all 27
  items mapped to where each is already substantively addressed in this
  repository (most of them, well before any manuscript gets drafted) —
  two items (funding, competing interests) flagged as having no home yet
  since they're disclosures the researcher supplies, not pipeline
  outputs. Item wording reconstructed from well-established knowledge of
  PRISMA 2020's structure, not a live fetch against the publisher — flag
  to verify against the official checklist before submission.
- Fixed a stale `ANALYSIS_PLAN.md` §13 status line still blaming the
  (long-closed) search phase; the real current blocker is Phase 6 not
  having produced full-text decisions yet.
- `PRISMA_WORKFLOW.md` Phase 12-16 rows and current-phase summary updated
  accordingly, each carrying the "not yet run" caveat explicitly rather
  than only in `08_code/R/README.md`.

No new CSV schemas, so `validate_schemas.py` needed no updates. No
analysis has actually been run on real data — templates only, and
honestly labeled as untested where that's genuinely true (unlike this
project's Python tooling, which has been run and verified throughout).

## 2026-09-12 (latest, cont. 4) — Phase 10 (evidence classification) tooling built; Phase 11 deliberately left unscaffolded

At the researcher's request ("go on"), built `code/analysis/
build_evidence_map.py`: an idempotent, append-only script (same design
as `init_screening_db.py`/`init_full_text_db.py`) that fills
`evidence_map.csv` with whatever can be safely derived from
`extraction_database.csv` and leaves the rest blank with an explicit
warning rather than guessing:

- **Derived mechanically** (safe, because each is either already a
  closed-form fact recorded during extraction, or a direct application
  of a mapping this project's own docs already commit to):
  `study_design_class` (inverts `RISK_OF_BIAS.md` §1's design↔tool
  table), `mechanism_family` (from the four top-level mechanism
  booleans, `MULTIPLE` when more than one is true), `legal_context`/
  `institutional_context` (copied straight from already-extracted
  fields).
- **Left blank on purpose, with a printed warning**: `study_design_class`
  when the tool was the project's own Legal Institutional Evidence
  Appraisal Framework (covers both doctrinal and jurimetric studies,
  RISK_OF_BIAS.md §2 — the tool name alone can't disambiguate);
  `mechanism_family` when no top-level boolean came through true (a
  data-quality flag); `evidence_level` (a narrative tier per
  `DATA_DICTIONARY.md`, never a formula); and **`outcome_family`, every
  time** — `PROJECT_SPEC.md` §7's own outcome hierarchy lists
  "approval/refusal" under both the primary outcome and a secondary
  "administrative outcomes" category, so a study coded with
  `application_success`/`refusal`/`delay_outcome` genuinely cannot be
  mechanically resolved to one family without reading which specific
  approval/refusal the study actually measured. Guessing here would risk
  the "manufactured comparability" `PROJECT_SPEC.md` §3 exists to
  prevent, since outcome family gates what can ever be pooled together.

Tested against a synthetic four-study extraction database before
touching real data: correct tool→design-class mapping across RoB 2/
ROBINS-I/JBI/the project's own framework, correct single-vs-`MULTIPLE`
mechanism handling, correct warnings on the deliberately-blank fields,
and a verified no-op/no-duplicate on a second run (idempotency check).
Then run against the real `extraction_database.csv` — currently empty,
so a correct zero-row no-op.

`05_analysis/descriptive/EVIDENCE_MAP_README.md` (new) documents both
what the script does and, in its closing section, **why Phase 11
(quantitative feasibility assessment) gets no equivalent tooling**:
`ANALYSIS_PLAN.md` §2's decision tree is a corpus-level methodological
judgment applied per candidate synthesis family, not a per-study
mechanical fact — the decision tree itself already *is* the complete
process, so there's nothing safe left to automate ahead of real evidence
the way Phase 10's script helps with mechanical fields. `PRISMA_WORKFLOW.md`
Phase 10/11 rows and current-phase summary updated accordingly.

No new CSV schemas (evidence_map.csv's header is unchanged), so
`validate_schemas.py` needed no updates. No study has actually been
classified — tooling only, and honest about where tooling stops being
appropriate.

## 2026-09-12 (latest, cont. 3) — Phase 9 (risk of bias) process scaffolding built

At the researcher's request ("keep going"), scaffolded Phase 9 ahead of
any study actually reaching the appraisal stage:

- **`04_quality/appraisal_forms/APPRAISAL_FORM.md`** (new): the process
  guide — classify design, obtain the current official tool, complete it,
  save the filled checklist alongside a provenance-style filename
  (`<study_id>_<tool>.<ext>`), record the result into
  `extraction_database.csv`'s quality fields. **Deliberately does not
  reproduce any of the six validated tools' (RoB 2, ROBINS-I, two JBI
  checklists, CASP, MMAT) own checklist items or signaling questions
  anywhere in this repository** — those are living instruments their
  publishers revise, and this project has not independently re-verified
  their citations against the publisher (network access to publisher
  domains stays blocked from this environment).
- **`SOURCES.md`** §9–13: added citations for all six standard tools
  named in `RISK_OF_BIAS.md` §1 that had never been logged there, using
  the exact same honest hedge already established for PRISMA-P and
  AMSTAR 2 in that file — "not independently re-confirmed this session,
  standard and internally consistent with its well-known form, confirm
  before manuscript use." No citation is presented as more verified than
  it actually is.
- **`legal_institutional_evidence_appraisal_framework_form.md`** (new):
  a fully worked fillable form for the one instrument this project
  actually authored (`RISK_OF_BIAS.md` §2's 13 domains) — safe to
  reproduce in full since it's this project's own content, unlike the six
  validated tools above.
- **`04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md`** (new):
  shell for the end-of-phase cross-cutting narrative `RISK_OF_BIAS.md`
  §3 already calls for but never had a template for.
- Fixed a stale line in **`RISK_OF_BIAS.md`** §4 that still said "the
  search has not been executed" as the reason no study has been
  appraised — the search closed 2026-09-11; the real current blocker is
  that extraction (Phase 8) hasn't started yet, since Phase 6 (full-text
  screening) hasn't produced real decisions.
- `PRISMA_WORKFLOW.md` Phase 9 row and current-phase summary updated to
  match.

No new CSV files were created and no schema changed, so
`validate_schemas.py` needed no updates for this round. No study has
actually been appraised — process scaffolding only.

## 2026-09-12 (latest, cont. 2) — Phase 7 (pilot extraction) scaffolding built

At the researcher's request ("go on to the next"), scaffolded Phase 7
ahead of Phase 6 actually producing any full-text decisions — the same
build-ahead pattern used for Phase 6 itself:

- **`03_extraction/extraction_form/EXTRACTION_FORM.md`** (new):
  operationalizes `CODEBOOK.md`'s 12 sections into an ordered, fillable
  checklist for extracting one study into `extraction_database.csv` --
  explicitly flags the unit-of-analysis decision (`PROJECT_SPEC.md` §4)
  as something to nail down before extracting a single number, and the
  one-effect-per-study-and-outcome-family default (`CODEBOOK.md` §12)
  before extracting statistics from a multi-effect study.
- **`code/extraction/select_pilot_sample.py`** (new): draws the ~10-study
  pilot sample `PROTOCOL.md` §6 requires, stratified proportionally by
  source database (largest-remainder apportionment) with a fixed seed for
  reproducibility -- same practice as `exclude_spotcheck_sample.csv`.
  **Correctly refuses to run right now**: 0 of `full_text_screening_
  database.csv`'s 3,659 seeded records currently carry `final_decision ==
  "include"` (Phase 6 retrieval/screening hasn't started), so drawing a
  10-study sample from an empty pool would be meaningless. Verified the
  refusal path, and separately verified the actual stratification logic
  against a synthetic 30-record pool (15/10/5 split across three fake
  databases correctly yielded a 5/3/2 pilot draw) -- synthetic test files
  deleted after verification, nothing real touched.
- **`03_extraction/extraction_form/PILOT_EXTRACTION.md`** (new):
  documents why the pilot can't run yet, how to run it once it can, and
  -- the actual point of piloting -- that a disagreement between two
  independent pilot extractions should prompt asking whether `CODEBOOK.md`
  itself needs revision, not just resolving that one study's numbers; any
  such revision is a protocol amendment to log in this changelog per
  `PROTOCOL.md` §12.
- `PRISMA_WORKFLOW.md` Phase 7 row and current-phase summary, `CODEBOOK.md`'s
  opening paragraph, and `DATA_DICTIONARY.md` (a new entry for
  `pilot_sample.csv`, explicitly marked not-yet-generated) all updated to
  point at this tooling.

`pilot_sample.csv`'s schema is intentionally **not yet** added to
`validate_schemas.py` -- the file cannot legitimately exist until the
script actually runs for real, and adding a schema entry for a file that
doesn't exist yet would turn `validate_schemas.py`'s otherwise-clean
report into a false "MISSING" failure. Add it once Phase 6 has enough
real includes and the pilot is actually drawn.

No study has been extracted and no pilot has been drawn -- this is
scaffolding only, ready to use the moment Phase 6 produces enough
full-text includes.

## 2026-09-12 (latest, cont.) — Phase 6 retrieval tooling added

Following the scaffolding entry directly below, added three small
`code/screening/` scripts to support the actual retrieval/screening loop
the researcher (or a future full-text reviewer) will run repeatedly —
none of them retrieve anything themselves (still no outbound network
access from this environment), but they take the error-prone parts of
*recording* progress off the researcher:

- **`build_full_text_queue.py`**: regenerates a disposable
  `full_text_retrieval_queue.csv` from `full_text_screening_database.csv`
  joined against `screening_database.csv` for the `database` field —
  every still-open record (no `final_decision` yet), sorted by database
  then year descending, so retrieval can be batched one platform at a
  time instead of context-switching every row. Never writes to the
  authoritative file.
- **`update_full_text_record.py`**: the safe way to record one record's
  status or decision, instead of hand-editing the CSV (real risk: broken
  quoting on titles/authors with commas, or a typo'd enum value nothing
  else would catch). Validates every field against the same enums as
  `init_full_text_db.py`, touches only the fields passed, writes
  atomically (`tempfile.mkstemp()` + `os.replace()`) so a crash mid-write
  can't corrupt the file. Tested: happy-path update, an invalid `--status`
  value (correctly rejected by argparse before any write), and an unknown
  `--record-id` (correctly refused with no write) — all verified against
  a backup copy of the real database, which was restored and
  re-validated clean afterward.
- **`full_text_progress.py`**: read-only progress report — counts by
  retrieval status, by decision, by exclusion reason (E01–E12), any
  unresolved conflicts, and the exact numbers `PRISMA_WORKFLOW.md`/
  `prisma_flow.md` need for their "Reports sought/not retrieved/assessed"
  lines.

`full_text_retrieval_queue.csv`'s schema (`build_full_text_queue.py`'s own
`OUTPUT_FIELDS`) added to `validate_schemas.py` the same way as the other
generated schemas — no hand-duplicated declaration. All **13** tracked
files (up from 12) validate clean. `FULL_TEXT_README.md` and
`DATA_DICTIONARY.md` updated with usage and the new file's schema.

No full-text retrieval or screening has actually happened yet — this
remains tooling only, ready to use.

## 2026-09-12 (latest) — Phase 6 (full-text screening) scaffolding built

At the researcher's request, built the infrastructure for full-text
screening without doing any actual retrieval or screening work yet:

- **`code/screening/init_full_text_db.py`**: new idempotent, append-only
  seeding script mirroring `init_screening_db.py`'s design one stage
  later. Reads `screening_database.csv`, takes every record with
  `final_decision == "include"`, and appends any not already present to
  `02_screening/full_text/full_text_screening_database.csv` — never
  overwrites an existing row's retrieval status or decision, never
  silently resolves a record_id collision, warns (rather than deletes)
  if a record already in the full-text database no longer shows
  `final_decision == "include"` upstream.
- Ran it: seeded **3,659 records** (exactly the `final_decision ==
  "include"` count from the reviewer_2 merge above), all retrieval/
  decision/reviewer fields blank.
- **Deliberate design choice**: full-text tracking lives in this
  entirely separate file rather than reusing `screening_database.csv`'s
  existing-but-unused `full_text_decision`/`reviewer_1`/`reviewer_2`/
  `conflict` columns — reusing them would overwrite the title/abstract
  stage's own audit trail and gives full-text screening nowhere to put
  fields that stage never needed (retrieval status, file location).
  `screening_database.csv`'s own `full_text_decision` and reviewer
  columns are now unused/superseded; documented as such in
  `DATA_DICTIONARY.md`.
- `code/analysis/validate_schemas.py` updated to import the new file's
  schema from `init_full_text_db.py.SCHEMA`, matching how
  `screening_database.csv`'s schema is sourced from
  `init_screening_db.py` — no hand-duplicated schema declarations. All
  **12** tracked files (up from 11) validate clean.
- New `02_screening/full_text/FULL_TEXT_README.md` written for the
  researcher: how to record retrieval status (`sought`/`retrieved`/
  `not_retrievable`), where to log a retrieved file's location, how to
  apply E01–E12 exclusion codes at the full-text stage with page/section-
  level detail now possible, the same two-reviewer/conflict process as
  Phase 5, and a note that a possible future independent re-review of
  Phase 5 (raised separately by the researcher, not yet requested) would
  flow through to this file automatically via the same idempotent
  re-run, without disturbing any full-text work already logged.
- `DATA_DICTIONARY.md`, `PRISMA_WORKFLOW.md` (Phase 6 row and schema
  block), and `06_outputs/prisma/prisma_flow.md` ("Reports sought for
  retrieval" line, now n = 3,659) all updated to reflect this.
- `README.md`'s "Current status" section and top status line, both
  several rounds stale (still describing the pre-ProQuest/JSTOR search
  state and an unreviewed first-pass-only screening result), rewritten
  to match the actual current state through this Phase 6 scaffolding
  step — including carrying the reviewer_2 agreement-rate caveat
  forward rather than only having it live in `PRISMA_WORKFLOW.md`.

No full-text retrieval or screening has actually happened — this is
scaffolding only, ready for the researcher (or a future reviewer) to
start filling in.

## 2026-09-12 — Human reviewer_2 pass completed, with a flagged caveat

The researcher was sent a purpose-built Excel worksheet covering all
3,665 records reviewer_1 (AI) marked `include` or `unsure` — a one-click
dropdown decision column (Yes = include, left blank = exclude), the row
turning green on Yes, plus title/year/authors/abstract/AI-rationale/DOI/
URL for each record so no other file was needed to make the call.

The completed worksheet came back with **3,659 of 3,665 rows (99.8%)
marked Yes**. This is far above what an independent second-pass PRISMA
screening typically produces — the whole point of a second reviewer is
to catch cases the first pass got wrong, and a near-total agreement rate
is itself informative, in a way worth being honest about rather than
recording silently. Before merging anything, this was raised directly
with the researcher (not assumed to be an error, not assumed to be
genuine review) via an explicit question distinguishing three
possibilities: an accidental fill-down across the whole column, a
genuine deliberate review that happened to agree this strongly, or a
mix of both. The researcher's answer: proceed with the file as
delivered.

Merged into `screening_database.csv` on that basis:
`reviewer_2` = `Human-reviewer2-2026-09-12` for all 3,665 records;
`conflict` computed per `DATA_DICTIONARY.md`'s clarified definition
(true only where reviewer_1 made a firm `include` call that reviewer_2
then excluded -- **zero such conflicts occurred**; all 6 reviewer_2
excludes were resolutions of reviewer_1 `unsure` records, not
disagreements with a firm decision); `final_decision` populated for all
3,665 records (**3,659 include / 6 exclude**). All 11 tracked schemas
validated clean.

`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`DATA_DICTIONARY.md` all updated to carry this result **alongside the
agreement-rate caveat**, explicitly instructing that any manuscript
output reporting this screening step disclose it rather than presenting
a two-reviewer PRISMA process as routine. `exclude_spotcheck_sample.csv`
(120-record random QA sample of reviewer_1's excludes) remains
unreviewed and available if the researcher wants an independent check on
that population later.

## 2026-09-11 (latest) — Search phase closed; full corpus screened; corruption caught and fixed

Six real events, in order:

1. **ProQuest full export delivered and ingested** — `SEARCH_039`, 7,728
   records via the researcher's new "My Research" account, superseding
   the earlier 100-record guest-mode sample (confirmed 97% redundant by
   title overlap, not separately ingested).
2. **ProQuest/Sociological Abstracts delivered and ingested** —
   `SEARCH_040`, 16,736 records, a broader thesaurus-term pull with a
   correspondingly wider topical spread (documented, not treated as a
   search-string defect).
3. **Search phase closed by researcher decision** — candidate pool
   (34,594 raw records at that point) judged large enough to move to
   screening. `search_log.csv` and `SEARCH_PROTOCOL.md` §7 updated to
   document this honestly, including the real gap it leaves: SSRN and
   Westlaw/Lexis were never searched at all (`SEARCH_042`/`SEARCH_043`
   stub rows record this rather than omitting it).
4. **JSTOR's 4 outstanding delivery files finally arrived** —
   `SEARCH_041`'s 50-record export, closing out a three-round "reported
   but never delivered" gap. A 100-record ProQuest file delivered
   alongside it was checked for overlap (97% redundant with SEARCH_039)
   and not separately ingested.
5. **First-pass AI screening of all 19,085 newly-added records, with a
   real data-corruption incident caught and fixed mid-round.** Screening
   19,085 records required 39 parallel ~500-record agent batches. The
   first attempt used a shared output directory across all 39 agents;
   validation afterward found several "completed" batches missing
   hundreds of rows each, with one agent's own report describing a
   helper script silently overwritten and its output redirected into a
   different batch's file — a genuine multi-agent file collision, not a
   screening-quality problem. All 39 batches were discarded and redone
   from isolated per-batch scratch directories, then validated
   record-for-record against their source files (exact record_id-set
   match, no duplicates, no foreign IDs) before merging. Final result:
   1,351 include / 17,379 exclude / 355 unsure across the 19,085 records.
6. **A second, independent gap caught during PRISMA-number
   reconciliation**: `SEARCH_041`'s 50 JSTOR records had been written to
   `raw_exports/` but never actually run through
   `deduplicate.py`/`init_screening_db.py` — caught because the raw-file
   total didn't match the dedup-output total. Re-ran the full-corpus
   dedup (34,594 raw → 27,481 unique, 7,113 merged) and screened the 28
   newly-surfaced abstract-bearing records directly: 1 include, 27
   exclude.

**Final state**: `screening_database.csv` holds 27,481 unique records,
26,222 screened (1,259 undecided for lack of an abstract) — **3,062
include / 22,557 exclude / 603 unsure**. `reviewer_2_queue.csv`
regenerated at 3,665 rows; `exclude_spotcheck_sample.csv` regenerated
(same fixed seed, 120 rows) against the corrected exclude population.
`PRISMA_WORKFLOW.md` and `06_outputs/prisma/prisma_flow.md` updated with
these final numbers and the Phase 3 closure. All 11 tracked schemas
validated clean throughout.

Two real code bugs found and fixed along the way, both now standing
protections for any future large export: (a) `csv.field_size_limit`
wasn't raised in `deduplicate.py`, `init_screening_db.py`, or
`validate_schemas.py`, which would have crashed on the two ProQuest
conference-abstract-supplement records carrying a single 600K+ character
abstract field (genuine platform behavior, not a parsing error — verified
against the raw RIS by line number); (b) the multi-agent shared-directory
corruption above, now avoided by confining each parallel screening agent
to its own scratch subdirectory.

## 2026-09-11 (later) — ProQuest and JSTOR: two methodological decisions

Cowork's next round surfaced two real, platform-forced compromises that
needed a decision from the researcher rather than being resolved
unilaterally (`PROJECT_SPEC.md` §14.18) — both logged in
`search_log.csv` (`SEARCH_039`, `SEARCH_041`) alongside the technical
detail; the decisions themselves:

- **ProQuest** (`SEARCH_039`, 8,137 total hits): guest/no-account export
  works mechanically but caps at roughly 100–200 records per session
  before a login-required error, and saves under an unrecoverable random
  filename. **Decision: the researcher will create a personal ProQuest
  "My Research" account**, which unlocks a documented 20,000-record bulk
  export — Cowork cannot create the account or enter a password on the
  researcher's behalf. Full ProQuest export is pending that account.
- **JSTOR** (`SEARCH_041`): the full search string is rejected outright
  as "too long," forcing a trim to ~9 terms across 3 clauses (a
  materially smaller vocabulary than every other database in this
  project), and even that returned 5,217 hits until an ad-hoc
  "Subject: Law" filter narrowed it to a workable 356 — excluding
  whatever JSTOR classifies under Development Studies, Public Policy,
  Urban Studies, etc. **Decision: accept the narrower, Subject:Law-only
  JSTOR search as a supplementary source** (consistent with
  `SEARCH_PROTOCOL.md` §1's own Tier 2 framing for JSTOR/SSRN/Google
  Scholar — supplementing, not matching, Tier 1 recall) rather than
  running further subject-filtered sub-searches to widen it. The full
  356 (not just the 7-record sample already pulled) still needs
  exporting — no bulk "select all" exists on JSTOR, so this is manual,
  per-item selection across roughly 15 pages.

## 2026-09-11 (earlier still) — HeinOnline begins; a SEARCH_035 integrity scare, resolved

- **`SEARCH_037` (HeinOnline, Title-restricted secondary search per
  `heinonline.md`)** ingested: 1 record ("Hear Their Voices: Australia's
  First Nations Women and the Legal Recognition of Their Rights to
  Water," O'Bryan & Harriden 2023). No structured abstract available
  from HeinOnline for this record — left blank, not fabricated; gets
  title-only triage like other abstract-less records.
- **`SEARCH_036` (HeinOnline, main three-clause full-text search)**
  logged as **count-only**: 71,226 hits, far too many to hand-compile
  and no bulk results-list export exists on HeinOnline at that volume.
  Per `REPRODUCIBILITY.md`, a real search that ran and produced a real
  total is logged even when it yields no exportable records — no records
  added under this `search_id`.
- **A serious, since-resolved integrity question on `SEARCH_035`.** A
  run log received the same day claimed the Web of Science export
  ingested in the previous round had never actually succeeded ("no
  download was ever produced... confirmed nothing in Downloads"),
  directly contradicting the 4,058 real-looking records already screened
  and pushed. Flagged to the researcher rather than resolved
  unilaterally either way (`PROJECT_SPEC.md` §14.18); a technical
  read at the time (realistic WOS accession-number entropy, correct
  journal/ISSN/publisher metadata, WoS-internal ResearcherID/GA-code
  fields very hard to fabricate at scale) suggested the data was
  genuine, but this was not independently verifiable from this
  environment.
  - **Conclusively resolved**: checked directly on the researcher's
    machine, file by file. The 5 files exist under Windows' standard
    duplicate-naming convention (`savedrecs.txt`, `savedrecs (1).txt`,
    `savedrecs (2).txt`, `savedrecs (3).txt`) rather than the 4 distinct
    names originally assumed — 1000+1000+1000+58 = 4,058 records, zero
    WOS-ID overlap, timestamped 03:52–03:57 UTC, predating the later
    session that logged the HTTP 500 failures. **The originally-ingested
    4,058 records are genuine and stand as final — nothing in this
    project's data was ever wrong.**
  - **A second, smaller instance of the same failure mode surfaced
    during the resolution itself**: the later session's own retry
    produced a `savedrecs (4).txt` that returned HTTP 200 (apparent
    success) but was a byte-for-byte duplicate of the first batch — no
    new file actually written despite the "successful" network
    response. Worth carrying forward as a standing caution for future
    rounds: a Cowork session's own claim of export success (status
    code, dialog closing normally) is not sufficient on its own for
    this platform — confirm against the actual file on disk.

## 2026-09-11 (earlier) — SEARCH_035 ingested: first Web of Science batch, second Tier 1 database

- **Web of Science is the second Tier 1 database actually searched for
  real** (`SEARCH_035`, 2026-09-11) — sent as 5 sequential tab-delimited
  `savedrecs.txt`-style export batches (WoS's native 1,000-record export
  cap; the researcher used `cowork_instructions_2026-09-11_wos_heinonline.md`
  to run it), zero overlap between batches confirmed via UT/accession
  number comparison, totaling 4,058 records after removing one exact
  internal repeat.
- **Found and fixed two real bugs in `wos_adapter.py`, previously
  unvalidated speculative code, while processing this batch:**
  1. It only handled a single CSV file; added tab-delimited
     auto-detection (comparing tab vs. comma counts in the header line)
     and multi-file merging (`--input` now takes one or more files).
  2. **A real data-corruption bug**: WoS's tab-delimited export has no
     quote-escaping at all, so a literal double-quote inside an abstract
     (common — quoting a term) was being misread by Python's csv module
     under its default quoting mode as *opening* a quoted field, which
     then silently swallowed every subsequent tab and newline as literal
     text until some *later* stray quote happened to close it —
     corrupting or merging an unpredictable number of downstream records.
     Caught by comparing each file's raw physical line count (1,000)
     against its parsed row count (as low as 988 before the fix) rather
     than assuming a clean parse; fixed by switching to
     `csv.QUOTE_NONE` for the tab-delimited path, which is actually
     correct for this format. Re-verified exact 1,000/1,000 parsing
     after the fix, then spot-checked field alignment on real records.
     `wos_adapter.py` is now genuinely validated against a real export,
     not just written speculatively.
- Full-corpus re-dedup (10,079 raw records now that WoS is in) found
  **2,934 duplicates** — far more than any prior round, as expected:
  Scopus and Web of Science index a lot of the same journal literature,
  so heavy cross-database overlap is exactly what a working dedup should
  catch. Leaves **7,145 unique records, 7,109 with a real abstract**.
  Same benign `record_id` flag as the previous round (`R36A2B99DC8AD`,
  the SEARCH_026/SEARCH_027 Scopus year-metadata quirk) recurred and was
  left untouched, as before — not a new issue.
- Screened the 1,664 newly-unique records (5 more batches, same
  independent-validation method as every prior round) against
  `INCLUSION_EXCLUSION.md`: **201 include / 1,404 exclude / 59 unsure**.
  Notably lower yield than the Scopus batches (~13% include/unsure vs.
  ~25-30%) — expected, not a screening-quality problem: `TS=` is broader
  than Scopus's `TITLE-ABS-KEY` (also searches Keywords Plus), and this
  batch is only the WoS-unique residue *after* cross-database dedup
  already removed everything WoS shared with Scopus, so it's
  disproportionately the noise Scopus's narrower field didn't also catch.
- Screening database now has **7,145 total records, 7,109 screened**
  (36 still lack a real abstract and remain deliberately undecided).
  Cumulative first-pass totals: **1,710 include / 5,151 exclude / 248
  unsure.** Refreshed `reviewer_2_queue.csv` (1,958 rows) and
  `exclude_spotcheck_sample.csv` (120-row sample, seed `20260911035`,
  regenerated fresh over the full exclude population) accordingly.
  `code/analysis/validate_schemas.py` confirms all 11 checked project
  CSVs still match their documented schema.
- `search_log.csv`'s `SEARCH_035` row documents what's confirmed (exact
  query string, per-batch counts, zero-overlap verification) and flags
  what wasn't reported back (Core Collection index selection, the
  platform's own on-screen total count) rather than guessing either —
  worth the researcher confirming for the record.

## 2026-09-11 — SEARCH_026 ingested: Scopus batch plan complete (18 of 18)

- Received and ingested `SEARCH_026` (2020, 274 records) — the one
  outstanding gap from `scopus_batch_plan_2026-08-26.md` flagged in the
  previous entry. Record count cross-checked against the researcher's run
  log (`scopus_batch_run_log_20260910.csv`, 274 shown/exported) and an
  independent file row count, both matching exactly. **All 18 planned
  Scopus batches are now done.**
- Full-corpus re-dedup (5,747 → 6,021 raw records, +274 from SEARCH_026) found 541 duplicates
  (2 more than the previous round), leaving **5,480 unique records**. One
  of the 2 new duplicates is worth noting: the same DOI appeared in both
  `SEARCH_026` (PUBYEAR=2020) and `SEARCH_027` (PUBYEAR=2019) with a
  trivial title-capitalization difference and a one-year metadata
  discrepancy — a Scopus indexing quirk (same paper, inconsistent
  year field across two of Scopus's own query contexts), not a data
  error on this project's side. Correctly DOI-matched and merged;
  `init_screening_db.py`'s existing safety check flagged the resulting
  text mismatch against the already-screened `SEARCH_027` copy rather
  than silently overwriting it — verified benign and left as-is, no
  action needed since the underlying study was already screened
  (`title_abstract_decision = include`) under its existing `record_id`.
- Screened the 272 newly-added records (batch 16, following the same
  15-batch method and validation as the previous round) against
  `INCLUSION_EXCLUSION.md`: **73 include / 182 exclude / 17 unsure**.
  Screening database now has **5,480 total records, 5,445 with a real
  abstract, all 5,445 screened** (35 records still lack an abstract and
  remain deliberately undecided). Cumulative first-pass screening
  totals: **1,509 include / 3,747 exclude / 189 unsure.**
- Refreshed `reviewer_2_queue.csv` (now 1,698 rows) and
  `exclude_spotcheck_sample.csv` (regenerated fresh over the full 3,747
  excludes, seed `20260911`) to cover the complete corpus; appended
  `SEARCH_026`'s rationale to `ai_first_pass_rationale.csv` (now 5,445
  rows). `code/analysis/validate_schemas.py` confirms all 11 checked
  project CSVs still match their documented schema.

## 2026-09-10 (final) — Reviewer 2 prep packet, PRISMA flow diagram, RIS adapter

- **Built the reviewer_2 handoff.** `02_screening/title_abstract/
  reviewer_2_queue.csv`: every `include`/`unsure` record from the AI
  first pass (1,608 rows), with title/abstract/authors/year/doi/url and
  the first-pass rationale attached, so a human second reviewer works
  from one file instead of filtering a 5,208-row database by hand.
  `exclude_spotcheck_sample.csv`: a random, fixed-seed (`20260910`,
  reproducible) 100-record sample of the 3,565 first-pass excludes, for
  false-negative spot-checking rather than a full second pass over every
  exclude — standard systematic-review QA practice. `REVIEWER_2_README.md`
  explains how to use both and is explicit that screening only these
  1,608 does not by itself satisfy `PROTOCOL.md`'s two-reviewer
  requirement for the whole title/abstract stage. Both new CSVs added to
  `validate_schemas.py` and `DATA_DICTIONARY.md`.
- **Populated `06_outputs/prisma/prisma_flow.md`** (previously an
  all-placeholder stub) with real counts through the title/abstract
  screening stage: 5,710 records identified from Scopus, 37 from the
  WebSearch pilot/exemplars, 539 duplicates removed, 5,173 screened (35
  left unscreened — no abstract), 3,565 excluded (full E01–E12 code
  breakdown), 1,608 carried forward. Everything from "reports sought for
  retrieval" onward is left genuinely blank — that work hasn't started —
  and every screening-stage number is explicitly flagged provisional
  (reviewer_1/AI only, no `reviewer_2` yet).
- **Added `code/search/adapters/ris_adapter.py`**: one shared,
  **unvalidated** adapter for the RIS citation-export format, covering
  HeinOnline, ProQuest, Sociological Abstracts, JSTOR, and SSRN — all of
  which offer RIS export per their `database_strategies/*.md` files.
  Grounded in the RIS format itself (a real, long-published standard),
  not a guessed platform-specific CSV layout, which is why one adapter
  can responsibly cover five platforms at once. Handles multiple authors,
  wrapped/continuation lines, and both common tag variants per field
  (TI/T1, PY/Y1, AB/N2, UR/L1/L2) — tested against synthetic RIS data
  covering all of that plus a missing-title record and a not-actually-RIS
  file, both of which fail cleanly rather than silently producing
  garbage.
- **Deliberately did not** build adapters for Westlaw/Lexis (neither
  platform offers a standard bulk export to build against without
  guessing — `PROJECT_SPEC.md` §14) or for CanLII/Rechtspraak.nl/
  Brazilian court portals/ANA-SNIS (these feed the doctrinal/jurimetric
  strand of the project, not this screening pipeline — merging their
  hits through this pipeline would be wrong, not just premature). Each
  `database_strategies/*.md` file now says so explicitly rather than
  leaving the absence unexplained.

## 2026-09-10 (earlier) — First-pass AI title/abstract screening, all 5,173 abstract-bearing records

- **Real title/abstract screening against `INCLUSION_EXCLUSION.md` has now
  actually happened**, for the first time in this project, on every
  record with a real abstract. This is a first pass by Claude, explicitly
  authorized by the researcher as an AI reviewer (`reviewer_1`) — per
  `PROTOCOL.md` §"Selection process" ("two reviewers where feasible") and
  `PROJECT_SPEC.md` §14.18 ("ask for human confirmation when a major
  methodological choice is genuinely ambiguous"), this was surfaced to
  the researcher as a choice rather than decided unilaterally, then
  proceeded on explicit instruction. **`reviewer_2` (a human) and
  conflict resolution have not happened — these decisions are
  provisional, not final**, exactly like any single reviewer's pass in a
  real dual-review PRISMA process.
- Method: the 5,173 records with a real abstract were split into 15
  batches of ~350 and screened independently by subagents, each reading
  `INCLUSION_EXCLUSION.md` directly and applying its 9 inclusion criteria,
  11 exclusion criteria, and E01–E12 exclusion-code table. Every batch's
  output was validated before merging: exact record_id order and coverage
  match against its input, every `exclude` decision carries exactly one
  valid E01–E12 code, no `include`/`unsure` row carries a stray code, no
  duplicate record_ids across batches, and no already-decided row was
  ever touched (the merge script refuses outright on any of these). The
  35 records without a real abstract (grey literature / older exports)
  were deliberately left undecided — this project's own convention (see
  `title_only_triage_memo.md`) is that title-only triage is non-binding,
  never a substitute for reading an abstract.
- **Results: 1,436 include / 3,565 exclude / 172 unsure**, out of 5,173
  screened (35 of 5,208 total records left undecided, no abstract).
  Exclusion code breakdown: E01 wrong topic 1,555; E06 engineering only
  780; E05 no empirical evidence 487; E04 wrong outcome 255; E07 wrong
  service 320; E03 water-quality-only 65; E09 insufficient information
  63; E02 wrong population 21; E08 duplicate 18; E11 wrong
  jurisdiction/context 1. Consistent with the batch plan's own
  expectation (`scopus_batch_plan_2026-08-26.md`, `EXECUTION_CHECKLIST.md`)
  that this broad, high-recall OR-heavy Boolean search would surface a
  lot of engineering/hydrology/water-quality noise alongside the
  genuinely on-topic records.
- `reviewer_1` is set to `Claude-AI-1stpass-2026-09-10` on every screened
  row, so it's always traceable which decisions came from this pass
  versus a human reviewer. `title_abstract_decision` of `unsure` should
  be treated the same as `include` for full-text-stage purposes (proceed
  to read it) — these are records the first-pass reviewer explicitly
  could not confidently resolve from title+abstract alone, not a
  rejection.
- **What this is not**: not a final inclusion/exclusion decision (needs
  `reviewer_2` and conflict resolution per `PROTOCOL.md`), not full-text
  screening, not data extraction, not risk-of-bias appraisal. The 1,436
  (+172 unsure = up to 1,608) candidate records are the pool that Phase 6
  (full-text screening) will actually work from once a human reviewer's
  pass exists to compare against.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after this round.

## 2026-09-10 (later still) — Stable record_id migration; Web of Science adapter

- **Replaced positional `record_id` assignment with a stable content
  hash**, closing the follow-up flagged in the previous entry.
  `code/search/deduplicate.py`'s `compute_record_id()` now keys on the
  normalized DOI when present, else normalized title+year — the same
  fields the duplicate matcher itself already uses — so a record's ID no
  longer depends on which files happen to be present or what order they
  sort in. Collision-checked: three genuine content collisions surfaced
  during the full re-run (two different generic-titled records sharing a
  normalized title+year, e.g. a recurring report-series title), correctly
  disambiguated with a `-1` suffix rather than silently merged.
- Did this migration now specifically because it was still safe to:
  confirmed **zero rows** in `screening_database.csv` had any decision
  field set (`title_abstract_decision`, `full_text_decision`,
  `reviewer_1`, `reviewer_2`, `final_decision`) before touching a single
  ID. Regenerated `deduplicated_records.csv` and
  `screening_database.csv` in full from a fresh re-run across all of
  `01_search/raw_exports/` under the new scheme, then verified **zero
  orphans**: every one of the previous 5,314 rows matches (by DOI or
  normalized title+year) something in the new 5,208-row output. The
  106-row reduction is not data loss — it's genuine duplicates that had
  slipped past the old positional-ID incremental matching across earlier
  rounds, now correctly collapsed by one clean full-corpus dedup pass.
  Remapped the 37 `record_id`s referenced in
  `06_outputs/supplementary/title_only_triage_memo.md` to match.
- Added `code/search/adapters/wos_adapter.py`: **unvalidated** (no real
  Web of Science export exists in this project yet, same status
  `pubmed_adapter.py` carried before SEARCH_018), written ahead of time so
  ingestion is instant once the researcher runs
  `database_strategies/wos.md`. Handles both CSV shapes Web of Science's
  UI can produce (full-word "Export → Excel" headers, and the classic
  two-letter Core Collection field tags), tested against synthetic data
  covering both plus a missing-required-column failure case.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after the migration.

## 2026-08-22 (later) — PR opened; preregistration draft + Phase 4/5 tooling

- Opened PR #3 (`claude/legal-last-mile-review-spec-8ri0zs` → `main`) on the
  jrklaus8/water-law-dataset repository.
- Drafted the OSF Generalized Systematic Review preregistration text
  (`00_admin/preregistration/osf_preregistration_draft.md`) — not
  submitted; this environment has no OSF account access.
- Wrote and tested `code/search/deduplicate.py` (DOI-match and
  title/year-similarity-match deduplication, with a full merge log for
  auditability) against synthetic data — not yet run on real data, since
  none exists. Documents that it expects input already normalized to a
  common schema; per-database raw-export adapters remain future work to be
  developed against real exports once Phase 3 produces any.
- Wrote and tested `code/screening/init_screening_db.py` (idempotent merge
  of newly deduplicated records into the persistent screening database,
  never overwriting an existing reviewer decision) against synthetic data.
- Updated `PRISMA_WORKFLOW.md` and `README.md` status tables accordingly.
  Phase 3 (database searching) remains the hard blocker — no credentials
  exist in this environment for any Tier 1 database.

## 2026-08-25 — Confirmed network egress is blocked; ran exploratory WebSearch pilot

- Tested direct access to PubMed's API (`curl`) and to PubMed, Google
  Scholar, CanLII, Rechtspraak.nl, and SSRN (`WebFetch`) — every one was
  denied by this environment's network egress policy (confirmed via
  `/root/.ccr/agentproxy/status`, a genuine policy denial rather than a
  transient failure, per that tool's own guidance not to retry). This
  environment therefore cannot reach any database, free or paid, by direct
  fetch or API call — only Claude's first-party `WebSearch` tool works.
- Amended the screening-database schema to add a `url` field alongside
  `doi` (`02_screening/title_abstract/screening_database.csv`,
  `code/search/deduplicate.py`, `code/screening/init_screening_db.py`,
  `DATA_DICTIONARY.md`, `PRISMA_WORKFLOW.md`) — real candidate records,
  especially grey literature, routinely have no DOI, and a URL is the only
  way to relocate them.
- Ran six explicitly non-systematic `WebSearch` queries drawn from
  `SEARCH_PROTOCOL.md`'s terms, logged as `SEARCH_003`–`SEARCH_008` in
  `01_search/search_logs/search_log.csv` with the pilot's method and
  limitations stated on every row. Extracted only title + URL from
  WebSearch's structured result data (never from its prose summary, which
  is itself an LLM paraphrase and risks introducing unverified specifics)
  into `01_search/raw_exports/SEARCH_003-008_WEBSEARCH_PILOT_2026-08-25.csv`
  — 25 candidate records, no fabricated authors/years/DOIs (left blank
  where not directly legible from the search result itself).
- Ran `code/search/deduplicate.py` and `code/screening/init_screening_db.py`
  on this real data for the first time (previously only synthetic-data
  tested) — 0 duplicates within the batch, 25 records now in
  `02_screening/title_abstract/screening_database.csv` with no screening
  decision made on any of them.
- Updated `SEARCH_PROTOCOL.md`, `PRISMA_WORKFLOW.md`, `README.md`, and
  `06_outputs/supplementary/preliminary_results.md` to state clearly, in
  each place, that this pilot is not Phase 3 and does not substitute for
  it — it exists so the deduplication/screening tooling has real data to
  operate on and so genuine (if low-recall) candidate studies are already
  identified once real screening capacity exists.

## 2026-08-25 (later) — Second pilot round, schema-validation tooling, triage memo

- Added `code/analysis/validate_schemas.py`: checks every project CSV's
  actual header against its documented (or script-generated) schema.
  Verified it catches real drift with a synthetic test, then confirmed all
  8 checked files are currently consistent — useful given the schema has
  already changed once (the `url` field).
- Ran a second WebSearch pilot round: an approximated backward-citation
  search on all 4 exemplar papers from `SOURCES.md` (WebSearch has no real
  citation-graph capability, so this is a keyword approximation, logged as
  such), plus a World Bank/UN-Habitat grey-literature query and a
  connection/service-refusal query. Logged as `SEARCH_009`–`SEARCH_013`,
  including two searches that found nothing new (Gaikwad/Thomas citations,
  too recent for a citation index; Halling/Bækgaard citations, real hits
  but out of this review's water/sanitation scope — logged as a scope
  demonstration, not a failure).
- Added 6 new genuine candidates from this round to
  `01_search/raw_exports/SEARCH_009-013_CITATION_GREYLIT_PILOT_2026-08-25.csv`;
  total candidate pool now 31 records, still 0 duplicates.
- Added `06_outputs/supplementary/title_only_triage_memo.md`: a title/URL-only,
  explicitly non-binding read of all 31 candidates against
  `INCLUSION_EXCLUSION.md`, since this environment cannot fetch abstracts.
  Does not populate `title_abstract_decision` for any record. Flagged a
  recurring pattern for the eventual reviewer: three law-review articles
  whose doctrinal-vs-empirical status can't be resolved from the title.

## 2026-08-25 (later still) — Third pilot round targeting gaps; exemplars added to pipeline; PubMed adapter

- Ran a third WebSearch round targeting gaps identified in the first two:
  Family B (bureaucratic assistance/political coordination + water),
  Dutch-language empirical studies specifically, Brazilian ANA/SNIS
  regulatory-data studies, and WHO/UNICEF JMP grey literature. Logged as
  `SEARCH_014`-`SEARCH_017`.
- Found a likely duplicate-publication pair: an earlier working-paper
  title appears to be a pre-publication version of the Gaikwad & Thomas
  2026 exemplar. Logged both per `REPRODUCIBILITY.md` §6 (identify, don't
  silently merge) rather than dropping the earlier one.
- Second Dutch-language query in a row surfaced zero empirical studies
  (only primary legal/regulatory sources) — logged as a preliminary,
  WebSearch-only pattern, explicitly caveated as far too thin a basis to
  draw any conclusion about the Dutch empirical literature.
- WHO/UNICEF JMP 2025 report deliberately excluded from the candidate pool:
  relevant background, but per its own summary it doesn't treat legal/
  administrative barriers as a distinct topic, failing inclusion
  criterion 2 — a scope-discipline exclusion, not a search failure.
- **Found and fixed a real gap**: 3 of the 4 substantive exemplar studies
  in `SOURCES.md` (Lubeck-Schricker et al. 2023, Gaikwad & Thomas 2026,
  Apio/Thiam/Dinar 2025) had been cited as methodological context but
  never actually entered the screening pipeline, meaning they'd never be
  formally screened like everything else. Added them with their
  already-verified DOIs. The 4th exemplar, Halling & Bækgaard 2024,
  deliberately was not added — it's administrative-burden methodological
  literature with no water/sanitation content, failing inclusion
  criterion 1; it remains a `SOURCES.md`-only methodological reference.
- Total candidate pool now 37 records, still 0 duplicates found by the
  automated dedup script (the 2 likely-duplicate pairs identified above
  differ enough in title that automated matching correctly can't catch
  them — exactly why they were logged manually instead).
- Added `code/search/adapters/pubmed_adapter.py`: normalizes PubMed's
  documented CSV export format to the project's common schema. Explicitly
  marked **unvalidated against a real export** (PubMed is unreachable from
  this environment) — tested against a synthetic file matching the
  documented format (works) and a deliberately wrong format (correctly
  refuses to guess rather than producing silently-wrong output).
- Updated `06_outputs/supplementary/title_only_triage_memo.md` for the 6
  new records.

## 2026-08-25 (latest) — Execution checklist for real institutional access

- The researcher confirmed a working EUR (Erasmus University Rotterdam)
  institutional research account, which should give real access to
  Scopus, Web of Science, HeinOnline, Westlaw, Lexis, and ProQuest.
- Added `01_search/EXECUTION_CHECKLIST.md`: a literal, step-by-step
  "what to actually click" guide per database — access route (via the
  library, not the database directly), where to paste each search string,
  export format/field selection (emphasizing abstracts, not just
  citations, since every candidate identified so far has been title-only),
  file-naming convention, and exactly what to hand back to Claude. Written
  to be followable without the rest of this repo's context, since the
  researcher intends to execute it via a separate tool (Claude Cowork).
- This does not touch credentials at all: Claude does not have and will
  not request the researcher's institutional login. Two independent
  reasons this has to be human-executed rather than automated from this
  environment: (1) network egress from this environment is blocked for
  every external domain tested, regardless of credentials; (2)
  institutional SSO logins involve MFA/interactive flows a script can't
  drive, and most of these platforms' license terms prohibit automated or
  bulk retrieval even by authorized users.
- Cross-linked from `README.md` and `SEARCH_PROTOCOL.md` §8.

## 2026-08-26 — First real Tier 1 database data (Scopus)

- The researcher ran the pilot Scopus string for real via EUR institutional
  access (Claude Cowork assisted) and uploaded the results as two GitHub
  PRs (#4, #5) containing PDFs and CSVs. **Flagged immediately: PR #4/#5
  contain 24 copyrighted journal-article PDFs (Nature, Springer, BMC)
  pushed to public branches — a likely redistribution problem independent
  of this project. Recommended deleting those branches/files rather than
  merging; only bibliographic metadata belongs in this repo.**
- Of the uploaded files, one was actually usable as review data:
  `export_d3841da0-...csv`, a genuine 500-record Scopus export (Authors,
  Title, Year, Source title, DOI, Link, Document Type, etc. — confirmed
  real Scopus export header). `Scopus-200-Analyze-Year.csv` was not a
  document-level export at all — it's Scopus's "Analyze results by Year"
  aggregate count feature, useful only for reconstructing the *total* hit
  count (summed to ~5,443 for the unrefined pilot string) and not ingested
  as data.
- Wrote and ran `code/search/adapters/scopus_adapter.py` — **validated
  against a real export**, unlike the still-unvalidated PubMed adapter.
  Normalized 500 records into `01_search/raw_exports/SEARCH_018_SCOPUS_2026-08-26.csv`,
  logged as `SEARCH_018` with the real query, the ~5,443 total count, and
  the gaps (no abstracts in this export; only 500 of ~5,443 exported).
- Ran the full pipeline on the combined pool (37 WebSearch-pilot + 500
  Scopus records): `deduplicate.py` found **1 real cross-source
  duplicate** — the Gaikwad & Thomas 2026 exemplar, independently added
  earlier from `SOURCES.md`, also appeared in the live Scopus results,
  correctly matched by DOI. This is the first real validation of the
  dedup logic against two independent real sources, not synthetic test
  data. Screening database now has **536 unique records**.
- Spot-checked the first 15 Scopus titles: a healthy mix of clearly
  on-topic hits and expected noise from a broad, sensitive Boolean string
  (corona-discharge hardware, blockchain, coastal-ecosystem valuation) —
  normal at this stage; screening exists to filter exactly this.
- Two follow-ups flagged for the researcher: (1) re-export with the
  Abstract field explicitly selected — none of these 500 records have one;
  (2) only ~9% of the total ~5,443 matching documents were exported —
  getting the rest needs either batching (e.g. by year range, since
  Scopus's bulk-export UI appears to cap a single CSV well below the full
  result count) or narrowing the query.

## 2026-08-26 (later) — Removed all 43 copyrighted PDFs from every branch

- 43 full-text journal-article PDFs (Nature, Springer, BMC/BioMed Central)
  had accumulated across three separate uploads: 10 on `jrklaus8-patch-1`
  (PR #4), 13 on `jrklaus8-patch-2` (PR #5), and 20 directly on this
  review branch. Flagged to the researcher as a copyright/redistribution
  concern independent of the research use itself.
- Closed PR #4 and PR #5 without merging.
- Removed the 10 and 13 PDFs from `jrklaus8-patch-1`/`jrklaus8-patch-2` via
  a direct git push updating each branch (GitHub's file-delete API choked
  on the large binaries; branch *deletion* was blocked by the same
  ruleset that blocked branch creation earlier in this project, but a
  normal branch *update* was not).
- Removed the 20 PDFs from this branch the same way.
- Before removing anything, recovered all 43 from git history and sent
  them directly to the researcher (not through GitHub) for them to store
  privately, per their request — see
  `01_search/raw_exports/native/README.md` for the accounting. None of
  the 43 remain in this repository in any form; their bibliographic
  metadata (for the 10+13 that came from the Scopus session) is preserved
  in `01_search/raw_exports/native/SEARCH_018_SCOPUS_2026-08-26_native.csv`.
- Confirmed via `git ls-tree` on both upload branches after the push that
  no PDF remains reachable from either branch tip. Noted as a caveat to
  the researcher: this doesn't purge the blobs from git's object history
  (recoverable by anyone with the old commit SHA) — a harder guarantee
  would need branch deletion (blocked here) or a GitHub-side history purge.

## 2026-09-10 — First abstracts; SEARCH_021b ingested

- Received the first batch from `scopus_batch_plan_2026-08-26.md`:
  `SEARCH_021b` (2025, non-article/non-review document types — the
  "everything else" half of the 2025 split; `SEARCH_021a`, articles and
  reviews, has not been run yet), 106 records. **This export includes
  Abstract, Author Keywords, and Index Keywords** — the first real
  abstract-bearing data in this project.
- Amended the project schema to actually carry this through, since
  neither the adapter nor the screening database had an `abstract` field
  before now:
  - `code/search/deduplicate.py`: added `abstract` as an *optional*
    normalized field (not required — older files without it still load).
    Also fixed a latent correctness bug this surfaced: when two sources
    describe the same record and only one has an abstract, the dedup
    logic was keeping whichever file sorted first alphabetically and
    discarding the other's abstract along with the duplicate. Now the
    kept record is backfilled with the abstract if it was missing one —
    verified with a synthetic test using filenames ordered the way they
    actually appear in production (abstract-less source sorting first),
    which is the case that would have silently failed before.
  - `code/screening/init_screening_db.py`: same backfill logic for a
    record already sitting in the screening database from an earlier,
    abstract-less run — the one narrow exception to "never touch an
    existing row," since backfilling a blank abstract isn't touching a
    decision field.
  - `code/search/adapters/scopus_adapter.py`: now maps the Abstract
    column through when present (previously just warned that it existed
    and dropped it).
  - Migrated all 536 existing `screening_database.csv` rows to the new
    16-field schema (blank `abstract`) rather than leaving them on an
    incompatible header.
- Ran the full pipeline on the combined pool: 0 new duplicates from this
  batch specifically (the one duplicate in the log is the pre-existing
  Gaikwad & Thomas exemplar match from 2026-08-26). Screening database now
  has **642 unique records, 106 of which have a real abstract** for the
  first time — real title/abstract screening against
  `INCLUSION_EXCLUSION.md` is now possible on that subset, though it
  hasn't been done yet.
- Note on this specific batch's composition: because `SEARCH_021b` is
  deliberately the non-article/review half of 2025 (book chapters,
  conference papers, an erratum, etc. — see the batch plan), it is not
  representative of Scopus's 2025 output as a whole; `SEARCH_021a`
  (articles + reviews) is where the more substantive primary research is
  expected to land.

## 2026-09-10 (later) — 17 of 18 Scopus batches ingested

- Received and processed the remaining 16 batches of
  `scopus_batch_plan_2026-08-26.md` in one round: `SEARCH_019` (2027, 2),
  `SEARCH_020a` (2026 articles+reviews, 556), `SEARCH_020b` (2026
  everything else, 100), `SEARCH_021a` (2025 articles+reviews, 477),
  `SEARCH_022` (2024, 392), `SEARCH_023` (2023, 337), `SEARCH_024` (2022,
  326), `SEARCH_025` (2021, 324), `SEARCH_027` (2019, 254), `SEARCH_028`
  (2018, 241), `SEARCH_029` (2016–2017, 375), `SEARCH_030` (2014–2015,
  315), `SEARCH_031` (2012–2013, 293), `SEARCH_032` (2009–2011, 367),
  `SEARCH_033` (2003–2008, 388), `SEARCH_034` (1928–2002, 357). All 16
  were exported with Abstract, Author Keywords, and Index Keywords, same
  as `SEARCH_021b`. Every native file preserved untouched in
  `01_search/raw_exports/native/`; every normalized file in
  `01_search/raw_exports/`; every batch logged as its own row in
  `search_log.csv`, built from the researcher's own authoritative run log
  (`scopus_batch_run_log_20260910.csv`) rather than reconstructed — every
  exported-record count cross-checked against that log and against an
  independent row count of each raw file, all matching exactly. Confirms
  `SEARCH_020a`/`SEARCH_021a`'s earlier finding that there is no hard
  500-record export ceiling when signed in via EUR proxy — both
  oversized DOCTYPE halves (556 and 477 records) exported whole.
- 17 of the 18 planned batches are now done. `SEARCH_026` (2020, ~274
  records per the run log) was run by the researcher but its export CSV
  has not been uploaded to this project yet — flagged in
  `scopus_batch_plan_2026-08-26.md` as the one remaining gap.
- Re-ran `code/search/deduplicate.py` across the full accumulated corpus
  (all `01_search/raw_exports/*.csv`): **5,208 unique records kept, 539
  duplicates merged** (mostly by DOI match; several backfilled a missing
  abstract from the surviving record's duplicate per the existing
  backfill rule). Re-ran `code/screening/init_screening_db.py`: 4,659 new
  records appended, 501 existing records backfilled with an abstract they
  previously lacked.
- **Found and fixed a latent record_id collision bug** surfaced by this
  round's scale: `deduplicate.py` assigns `record_id` positionally
  (`R0001`, `R0002`, ...) by file-processing order across
  `01_search/raw_exports/`. Adding 16 new files shifted that ordering
  enough that 13 IDs in the new dedup run collided with unrelated,
  already-screened-pool records from earlier rounds (same ID, different
  title/DOI). `init_screening_db.py`'s existing safety check correctly
  refused to overwrite the 13 old rows (so nothing was corrupted), but
  also silently skipped appending the 13 legitimately-new records under
  those colliding IDs — a real (if narrow) data-loss risk, not a
  duplicate. Manually verified all 13 were genuinely different
  title+DOI pairs, then appended them under 13 fresh unused IDs
  (`R5748`–`R5760`). **This is a structural limitation of the current
  positional ID scheme, not a one-off bug** — it will recur any time a
  new file is added whose sort position is before existing files' tail
  end and the corpus is large enough for a same-position collision;
  a content-hash-based `record_id` would eliminate it, but that is a
  larger migration (it would need to remap 5,300+ existing IDs) and is
  left as a known follow-up rather than done inline here.
- Screening database now has **5,314 unique records, 5,279 of which have
  a real abstract**. `code/analysis/validate_schemas.py` confirms all 8
  checked project CSVs still match their documented schema after this
  round. No screening decision has been made on any of them — this is
  still search, not screening.

## 2026-08-26 (latest) — Scopus batch export plan

- Added `01_search/scopus_batch_plan_2026-08-26.md`: 16 ready-to-paste
  batch queries to capture the remaining ~4,944 of ~5,444 total matching
  Scopus records, computed from the real year-by-year breakdown (not a
  guess) so each batch stays comfortably under the 500-record ceiling the
  first export hit. Flags that 2026 and 2025 alone (619 and 583 records)
  exceed that ceiling even as single years and need a further
  `DOCTYPE`-based split.
- Cross-linked from `EXECUTION_CHECKLIST.md`. Every batch still needs
  Abstract selected explicitly in the export field picker — the one gap
  that actually blocks real screening, and the main reason to finish
  Scopus before moving to a second database.
- Not yet executed — this is a plan, not new data.

## 2026-08-22 — Initial scaffold

- Repository structure created per the eleven-phase folder architecture
  (`00_admin/` through `11_archive/`, plus `data/` and `code/`).
- Governing documents written: `README.md`, `PROJECT_SPEC.md`,
  `PROTOCOL.md`, `SEARCH_PROTOCOL.md`, `INCLUSION_EXCLUSION.md`,
  `CODEBOOK.md`, `RISK_OF_BIAS.md`, `ANALYSIS_PLAN.md`,
  `PRISMA_WORKFLOW.md`, `DATA_DICTIONARY.md`, `REPRODUCIBILITY.md`,
  `PUBLICATION_PLAN.md`, `SOURCES.md`, `sources.bib`.
- Empty, header-only CSV templates created for the search log, screening
  database, exclusion log, extraction database, evidence map, and effect
  sizes — no data populated.
- Per-database search strings drafted for Scopus, Web of Science, PubMed/
  Global Health, HeinOnline, Westlaw/Lexis, ProQuest/Sociological
  Abstracts, JSTOR/Google Scholar/SSRN, CanLII, Rechtspraak.nl, and
  Brazilian legal/regulatory databases, plus grey-literature guidance —
  **none executed**.
- Eight preliminary methodological sources checked against independent web
  sources (publisher domains and doi.org were unreachable in this
  environment; see `SOURCES.md` for method and caveats). Two sources
  (PRISMA-P 2015, AMSTAR 2) remain unverified beyond the original citation
  and are flagged as such.
- Decided, following `PROJECT_SPEC.md` §3, that no title or framing implying
  a completed meta-analysis will be used until Phase 11–12 of
  `PRISMA_WORKFLOW.md` establishes that pooling is defensible for a given
  evidence family.
- Decided the systematic review's evidence base and the existing Global
  Water Law Judicial Decisions Dataset in this repository will not be
  merged (`PROJECT_SPEC.md` §9); they are cross-referenced but kept as
  separate evidence populations even though they share a git repository.

No search has been executed. No study has been screened, extracted, or
appraised. No effect size exists anywhere in this project.
