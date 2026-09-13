# Preliminary Results

**There are still no review findings.** This file is updated only when a
phase of `PRISMA_WORKFLOW.md` actually produces a result — never pre-filled
with an anticipated or illustrative finding. A pool of unscreened candidate
records is not a finding; it is listed below for transparency, not as
evidence of anything.

## What has actually been done

- Repository and documentation scaffold complete (`PRISMA_WORKFLOW.md`
  Phase 1).
- Eight preliminary methodological/exemplar sources checked against
  independent web sources (`SOURCES.md`) — this is source verification, not
  a review finding, and none of these eight sources have been screened or
  extracted as part of the review itself.
- Three rounds of an explicitly non-systematic exploratory pilot (Claude
  `WebSearch` tool, not any Tier 1/2 or legal-repository database's native
  search — see `SEARCH_PROTOCOL.md` §7) surfaced **37 candidate records**,
  now sitting in `02_screening/title_abstract/screening_database.csv` —
  including 3 of the 4 substantive `SOURCES.md` exemplars, which had
  previously been cited as methodological context but never actually
  entered the screening pipeline (fixed 2026-08-25). This is raw,
  unscreened input, not a result: none of these 37 records have a
  title/abstract decision, none have been read in full text, none have been
  extracted, and none have been risk-of-bias-appraised. A non-binding,
  title-only triage read (`06_outputs/supplementary/title_only_triage_memo.md`)
  flagged over a third as uncertain — several law-review articles among
  them may turn out to be doctrinal commentary rather than empirical
  studies once actually read; two Dutch-language queries in a row (under
  `SEARCH_006` and `SEARCH_015`) surfaced only primary legal sources, not
  studies, and contributed nothing to the screening database; and 2 pairs
  of records were flagged as likely duplicate publications for a human to
  resolve at full-text stage.
- A schema-validation script (`code/analysis/validate_schemas.py`) confirms
  every project CSV's header currently matches its documented schema.
- **2026-08-26: the pilot Scopus string was run for real**, via the
  researcher's EUR institutional access, and 500 of the ~5,443 total
  matching records were exported and ingested (`SEARCH_018` — see
  `CHANGELOG.md`). This is still not screening, extraction, or a review
  finding — it's 500 more unscreened title/author/year/DOI records, with
  the same limitations as the WebSearch pilot (no abstracts in this
  export) plus new ones of its own (only ~9% of the matching set exported
  so far). Deduplication against the existing 37 caught 1 real duplicate
  (the Gaikwad & Thomas 2026 exemplar). Total unscreened pool at that
  point: 536 records. The title-only triage memo has not yet been
  extended to cover these 500 — it still only covers the original 37.
- **2026-09-10: the first batch of `scopus_batch_plan_2026-08-26.md` was
  run — `SEARCH_021b`, 106 records — and it includes real abstracts.**
  This is the first time abstract text has entered this project. The
  schema was amended project-wide to carry it through (see
  `CHANGELOG.md`), including migrating the 536 pre-existing screening-
  database rows and fixing a dedup bug the change surfaced (a duplicate's
  abstract could have been silently discarded depending on file-processing
  order — fixed and verified with a synthetic test). Total unscreened
  pool: **642 records, of which 106 now have a real abstract**. This is
  still not screening: `title_abstract_decision` remains blank on all 642,
  including the 106 with abstracts — nothing has been screened yet, only
  the precondition for real screening (an actual abstract to read) now
  exists for a subset.
- **2026-09-10 (later): 16 more batches of `scopus_batch_plan_2026-08-26.md`
  were run and ingested — 17 of 18 planned batches now done, all with real
  abstracts.** This includes `SEARCH_021a` (2025 articles+reviews, 477
  records — the substantive sibling `SEARCH_021b` didn't cover) plus every
  other year/year-range from 2027 back to 1928. Confirmed there is no hard
  500-record Scopus export ceiling when signed in: both oversized DOCTYPE
  halves (`SEARCH_020a`, 556 records; `SEARCH_021a`, 477 records) exported
  whole. Every batch's exported-record count was cross-checked against the
  researcher's own authoritative run log
  (`scopus_batch_run_log_20260910.csv`) and an independent row count of
  each raw file — all matching exactly, no truncation or data loss. The
  full corpus (5,747 raw records across 18 Scopus exports plus the earlier
  WebSearch pilot and exemplars) was re-deduplicated as one pool: 539
  duplicates merged. Total pool at that point: **5,314 records, of
  which 5,279 have a real abstract** — still zero screening decisions
  made on any of them. Processing this round also surfaced a latent bug
  in how `deduplicate.py` assigns record IDs (positional, so vulnerable
  to collision as new files are added across rounds); 13 affected records
  were recovered under fresh IDs rather than lost. `SEARCH_026` (2020,
  ~274 records per the run log) was run by the researcher but its export
  file has not been uploaded to this project yet — the one remaining gap
  in the 18-batch plan.
- **2026-09-10 (later still): the record_id bug above was actually fixed**,
  not just patched around — `record_id` is now a stable content hash
  (normalized DOI, or title+year) rather than a positional index, so it
  can never again collide just because new files shifted the sort order.
  Regenerating everything under the new scheme (from the same raw data,
  verified zero data loss against the previous 5,314-row state) landed on
  **5,208 unique records, 5,173 with a real abstract** — the 106-record
  drop is genuine duplicates the old positional-ID incremental matching
  had missed across earlier rounds, not lost data. Also added an
  unvalidated Web of Science adapter (`code/search/adapters/wos_adapter.py`)
  so that search is ready to ingest instantly once run.
- **2026-09-10 (final): real title/abstract screening has now actually
  happened, for the first time in this project.** All 5,173 abstract-bearing
  records were screened against `INCLUSION_EXCLUSION.md` by Claude, acting
  as a first-pass AI reviewer — the researcher was explicitly asked
  whether an AI first pass should count toward this project's two-reviewer
  process, per `PROJECT_SPEC.md` §14.18, and authorized it. Screening ran
  as 15 independently-validated batches (~350 records each): every
  batch's output was checked for exact record coverage/order, valid
  decision values, and a code on every exclusion before being merged — no
  already-decided record was ever at risk of being overwritten.
  **Result: 1,436 include, 3,565 exclude, 172 unsure** (35 records
  without a real abstract were left undecided, consistent with this
  project's non-binding-triage convention for title-only records).
  Exclusion codes, most to least common: E01 wrong topic (1,555), E06
  engineering only (780), E05 no empirical evidence (487), E07 wrong
  service (320), E04 wrong outcome (255), E03 water-quality-only (65),
  E09 insufficient information (63), E02 wrong population (21), E08
  duplicate (18), E11 wrong jurisdiction/context (1) — consistent with
  this being a deliberately broad, high-recall Boolean search expected to
  surface a lot of engineering/hydrology noise. **This is not a final
  decision on any record.** No human `reviewer_2` pass or conflict
  resolution has happened; `unsure` records should be treated the same as
  `include` for full-text-screening purposes (a first-pass reviewer's
  genuine uncertainty, not a rejection). Full-text screening (Phase 6) is
  not yet possible at scale on this pool until a human second reviewer's
  pass exists to reconcile against this one.
- **2026-09-10 (final)/2026-09-11: built a reviewer_2 handoff, populated
  the PRISMA flow diagram, added a shared RIS adapter, and closed the
  last gap in the Scopus plan.** `reviewer_2_queue.csv` and
  `exclude_spotcheck_sample.csv` give a human second reviewer a ready
  starting point instead of filtering the full screening database by
  hand (`REVIEWER_2_README.md`). `06_outputs/prisma/prisma_flow.md`,
  previously an all-placeholder stub, now carries real, explicitly
  provisional counts through the title/abstract stage.
  `code/search/adapters/ris_adapter.py` (unvalidated) covers HeinOnline/
  ProQuest/Sociological Abstracts/JSTOR/SSRN via the shared RIS export
  format; Westlaw/Lexis and the doctrinal/jurimetric-strand databases
  (CanLII, Rechtspraak.nl, Brazilian courts, ANA/SNIS) were deliberately
  left uncovered, with each `database_strategies/*.md` file now
  explaining why. `SEARCH_026` (2020, 274 records) — the one remaining
  gap in `scopus_batch_plan_2026-08-26.md` — arrived and was ingested on
  2026-09-11: **all 18 planned Scopus batches are now done**, Scopus is
  fully searched per this plan's design, and its 274 records went
  through the same first-pass screening as everything else. **Cumulative
  totals: 5,480 unique records, 5,445 with a real abstract, all 5,445
  screened — 1,509 include, 3,747 exclude, 189 unsure.** Still a
  provisional first pass only; still no human `reviewer_2`.
- **2026-09-11 (later): Web of Science — the second Tier 1 database —
  searched for real.** `SEARCH_035` (4,058 records, with abstracts)
  arrived as 5 sequential export batches (Web of Science's native
  1,000-record export cap), zero overlap between batches verified.
  Processing it surfaced and fixed two real bugs in the previously-
  speculative `wos_adapter.py`: it only handled single CSV files
  (fixed — now merges multiple tab-delimited files in one call), and a
  genuine data-corruption bug where WoS's unescaped tab-delimited format
  confused Python's default CSV quote-handling whenever an abstract
  contained a literal double-quote, silently merging or corrupting
  records (caught by comparing raw physical line counts against parsed
  row counts, fixed by disabling quote interpretation entirely — correct
  for this format). The adapter is now validated against a real export,
  not just written speculatively. Full re-dedup across the combined
  10,079-record raw pool found **3,475 duplicates — 2,934 of them from
  heavy Scopus/Web-of-Science overlap alone**, exactly the kind of
  cross-database redundancy a working dedup pipeline should catch,
  leaving **7,145 unique records, 7,109 with a real abstract**. The
  1,664 newly-unique records were screened the same way as every prior
  batch: **201 include, 1,404 exclude, 59 unsure** — a notably lower
  yield (~13%) than Scopus's ~25-30%, expected since this batch is only
  the WoS-unique residue left after cross-database dedup already removed
  everything WoS shared with Scopus. **Cumulative totals: 7,145 unique
  records, 7,109 with a real abstract, all 7,109 screened — 1,710
  include, 5,151 exclude, 248 unsure.** Still a provisional first pass
  only; still no human `reviewer_2`.

- **2026-09-11 (later still)/2026-09-12: the search phase closed, by
  researcher decision, with documented gaps.** Beyond Scopus (fully
  searched) and Web of Science (`SEARCH_035`, 4,058 records), the
  researcher's institutional access also reached HeinOnline
  (`SEARCH_036`–`SEARCH_038`) but with a mostly-lost real yield:
  `SEARCH_036` found 71,226 hits with no bulk-export mechanism at that
  volume (count-only, 0 ingested), `SEARCH_037` yielded exactly 1
  ingested record, and `SEARCH_038`'s 3 records were reported but their
  export file never reached this pipeline. ProQuest (`SEARCH_039`,
  7,728 records via a full account-based export) and ProQuest/
  Sociological Abstracts (`SEARCH_040`, 16,736 records) were both
  searched in full. JSTOR (`SEARCH_041`) identified 356 records but only
  a partial export of 50 was ever produced before the search phase
  closed. **SSRN and Westlaw/Lexis were never searched at all** — the
  phase was closed, by explicit researcher decision, before either was
  reached (the candidate pool was judged large enough to move to
  screening); this is a real, disclosed limitation of this review's
  search strategy, not an oversight, and must be reported as such in any
  manuscript output (`SEARCH_PROTOCOL.md` §7). Final deduplication
  across every source run against this closed pool (WebSearch pilot,
  `SOURCES.md` exemplars, all 18 Scopus batches, Web of Science,
  HeinOnline, ProQuest, ProQuest/Sociological Abstracts, JSTOR) landed
  on **27,481 unique records, 7,113 duplicates merged** — heavy
  Scopus/WoS/ProQuest cross-database journal overlap, as expected.
- **2026-09-10/2026-09-11: first-pass AI title/abstract screening
  completed on the full closed-search-phase pool.** Of the 27,481 unique
  records, 26,222 have a real abstract; all 26,222 were screened by
  Claude as `reviewer_1` against `INCLUSION_EXCLUSION.md`, explicitly
  authorized by the researcher per `PROJECT_SPEC.md` §14.18 — **3,062
  include / 22,557 exclude / 603 unsure**. The 1,259 records without a
  real abstract were deliberately left undecided (non-binding title-only
  triage only, per `title_only_triage_memo.md`).
- **2026-09-12: a human `reviewer_2` pass was completed** on all 3,665
  reviewer_1 include+unsure records, via a purpose-built Excel worksheet
  handoff (`REVIEWER_2_README.md`) — **3,659 `include` / 6 `exclude`,
  zero recorded conflicts** by the strict reviewer_1-vs-reviewer_2
  disagreement definition in `DATA_DICTIONARY.md` (all 6 reviewer_2
  excludes resolved a reviewer_1 `unsure`, none overturned a firm
  reviewer_1 `include`). **Flagged plainly, not treated as routine:** a
  99.8% agreement rate between two independent reviewers is unusually
  high for genuine independent screening, and the full worksheet came
  back faster than reading ~3,700 abstracts individually would take —
  this was raised directly with the researcher before merging, who
  confirmed proceeding with the file as delivered; this caveat should
  travel with the number in any manuscript reporting it. `final_decision`
  is now populated for all 3,665 records on this basis. The 120-record
  `exclude_spotcheck_sample.csv` QA sample remains unreviewed and
  available if an independent check on the exclude population is wanted.
- **2026-09-12: Phase 6 (full-text screening) went live and is ongoing.**
  `02_screening/full_text/full_text_screening_database.csv` was seeded
  with all 3,659 Phase-5 includes. The researcher supplies full-text
  PDFs via chat upload on a rolling basis, expected to continue for
  roughly a month; each is converted (`pdftotext -layout`), screened by
  Claude as `reviewer_1` against `INCLUSION_EXCLUSION.md`'s E01–E12
  codes, and recorded via `update_full_text_record.py`, with every
  exclusion also logged to `exclusion_log.csv`. As of this entry:
  **191 of 3,659 records decided (91 include / 100 exclude)** — see
  `PRISMA_WORKFLOW.md` Phase 6 for the exclusion-reason breakdown. A
  human `reviewer_2` for this phase has not yet been assigned — open
  question for the researcher.
- **2026-09-13: Phase 8 (full extraction) is fully caught up with Phase
  6 — no outstanding gap.** At the researcher's explicit instruction to
  extract every full-text include directly rather than drawing a separate
  pilot subsample first (Phase 7 is marked superseded, not completed),
  **all 91 current full-text includes (S001–S091) are now fully
  extracted** into `extraction_database.csv` against `CODEBOOK.md`'s
  complete 92-field schema. Five of the 91 are themselves secondary
  reviews (four systematic, one focused/narrative), flagged
  `study_design_class = systematic_review_secondary` and never to be
  pooled as an independent primary effect.
- **2026-09-13: Phase 10 (evidence classification) has been run against
  all 91 extracted studies.** `build_evidence_map.py` derived what can
  safely be derived mechanically; the remaining judgment-call fields
  (`outcome_family`, `evidence_level`, `study_design_class` for the
  studies using the project's own Legal Institutional Evidence Appraisal
  Framework, and the two synthesis-eligibility flags) were filled by hand
  per study. **38 of the 91 extracted studies have a genuine,
  study-generated, calculable effect estimate and are judged eligible for
  quantitative synthesis; all 91 are qualitative-synthesis eligible.**
  This is a per-study eligibility judgment, not a corpus-level decision
  that pooling is warranted for any family — that is Phase 11, which has
  not started.

## What has not been done

- **Only five of the databases named in `SEARCH_PROTOCOL.md` were
  searched, and two planned searches never ran at all.** Scopus (fully
  searched, 18/18 planned batches) and Web of Science (`SEARCH_035`) are
  the two Tier 1 databases actually covered; HeinOnline, ProQuest,
  ProQuest/Sociological Abstracts, and JSTOR were also reached but with
  real, disclosed gaps in each (see above). **SSRN and Westlaw/Lexis were
  never searched at all** — the search phase was closed by researcher
  decision before either was reached. CanLII, Rechtspraak.nl, and
  Brazilian court/regulatory portals (feeding the doctrinal/jurimetric
  strand rather than this empirical-evidence pipeline) also remain
  untouched. This is the review's single largest disclosed limitation and
  must be reported as such in any manuscript output.
- A human `reviewer_2` pass for full-text screening (Phase 6) has not yet
  been assigned — open question for the researcher, distinct from the
  title/abstract `reviewer_2` pass, which is complete.
- Full-text screening itself is far from complete: 191 of the 3,659
  Phase-5 includes have been assessed; 3,468 records have not yet been
  reached, not confirmed unretrievable, since retrieval depends entirely
  on the researcher supplying full-text PDFs.
- Extraction (Phase 8) is caught up with screening completely — all 91
  current full-text includes are extracted, no outstanding gap.
- **No risk-of-bias rating has been performed on any of the 91 extracted
  studies** — `risk_of_bias_tool` is identified per study, but
  `risk_of_bias_rating` is deliberately left blank pending the official
  version of each appraisal instrument (`RISK_OF_BIAS.md`'s explicit
  prohibition on reconstructing a validated tool from memory). This is a
  real, reportable limitation at this stage, not an oversight.
- **No quantitative-feasibility determination (Phase 11) has been made
  for any candidate synthesis family** — 38 studies being individually
  eligible for quantitative synthesis is not the same as any family
  clearing `ANALYSIS_PLAN.md` §2's full decision tree (empirical basis →
  substantively comparable estimand → enough independent, non-secondary
  studies). That corpus-level judgment has not been made for any family.
- No effect size, pooled or otherwise, exists in this project. Phases
  12–16 (meta-analysis, SWiM synthesis, sensitivity analysis, publication
  bias, PRISMA reporting) have R-script/template scaffolding built but
  are all blocked on Phase 11 and have not been run against real data.

## Why this file is still preliminary, not a results section

`PROJECT_SPEC.md` §14 (operating instructions) prohibits inventing
literature, results, sample sizes, effect sizes, or confidence intervals,
and prohibits claiming an exhaustive search that was not actually
performed, or a synthesis judgment that has not actually been made. This
file now reports real screening and extraction progress — because that
progress is real, logged, and reproducible from the CSVs it cites — but it
still contains **no finding about any legal/administrative mechanism's
relationship to any household-level water/sanitation outcome**, because no
such finding has been produced yet: Phase 9 (risk of bias) and Phase 11
(quantitative feasibility) both remain undone, and nothing in
`05_analysis/` or `08_code/R/` has been run against this project's real
data. The next entry in this file that reports an actual finding should be
written only once a synthesis family has cleared Phase 11's decision tree
and a corresponding Phase 12/13 output exists.
