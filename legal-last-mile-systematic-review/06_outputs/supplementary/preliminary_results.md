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
  service (334), E04 wrong outcome (255), E03 water-quality-only (65),
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
  **920 of 3,659 records decided (467 include / 453 exclude)** — see
  `PRISMA_WORKFLOW.md` Phase 6 for the exclusion-reason breakdown. A
  human `reviewer_2` for this phase has not yet been assigned — open
  question for the researcher.
- **2026-09-16: Phase 8 (full extraction) is fully caught up with Phase
  6 — no outstanding gap.** At the researcher's explicit instruction to
  extract every full-text include directly rather than drawing a separate
  pilot subsample first (Phase 7 is marked superseded, not completed),
  **all 420 current full-text includes (S001–S422, S227 and S399 documented duplicate-removal gaps) are now fully
  extracted** into `extraction_database.csv` against `CODEBOOK.md`'s
  complete 92-field schema. Nineteen of the 420 (plus S418, a secondary review) are themselves secondary
  systematic reviews, flagged
  `study_design_class = systematic_review_secondary` and never to be
  pooled as an independent primary effect; S356, S364, and S376 are
  documentary/policy/regulatory-audit studies appraised with the project's
  own Legal Institutional Evidence Appraisal Framework rather than AMSTAR
  2, since none documents a formal systematic-review search methodology;
  S102 and S399's underlying record were also appraised with this
  framework and classified by hand as `jurimetric` (see the duplicate-
  merge note in `CHANGELOG.md` 2026-09-16).
- **2026-09-16: Phase 10 (evidence classification) has been run against
  all 420 extracted studies.** `build_evidence_map.py` derived what can
  safely be derived mechanically; the remaining judgment-call fields
  (`outcome_family`, `evidence_level`, `study_design_class` for the
  studies using the project's own Legal Institutional Evidence Appraisal
  Framework, and the two synthesis-eligibility flags) were filled by hand
  per study. **156 of the 420 extracted studies have a genuine,
  study-generated, calculable effect estimate and are judged eligible for
  quantitative synthesis; 354 of 420 are qualitative-synthesis eligible.**
  This is a per-study eligibility judgment, not a corpus-level decision
  that pooling is warranted for any family — that is Phase 11, which has
  not started.
- **2026-09-16 (later the same day): sixteenth full-text screening batch —
  13 researcher-supplied PDFs, 6 new includes (S368–S373).** Full detail in
  `CHANGELOG.md`. Notably, S369 is a companion paper to the already-included
  S357 (same VAPAR rural-South-Africa water-governance programme), and two
  of the six new includes (S370, S372) are secondary reviews whose full text
  allowed a **positively-determined** AMSTAR 2 rating of Critically Low —
  the review authors themselves explicitly state no critical appraisal of
  individual included studies was conducted, a confirmed fact rather than
  an unassessed unknown, distinguishing these from the earlier 17-study
  "Not ratable" AMSTAR 2 batch. A corpus-wide duplicate audit re-run
  afterwards (4 independent methods) came back clean against the resulting
  372-study corpus.
- **2026-09-16 (still later the same day): seventeenth full-text screening
  batch — 15 more researcher-supplied PDFs (13 genuinely new), 13 new
  includes (S374–S386).** Full detail in `CHANGELOG.md`. Notable additions:
  Martellet et al. 2024's regulatory-audit-indicator evaluation of Brazil's
  Novo Marco Regulatorio was appraised with the project's own Legal
  Institutional Evidence Appraisal Framework and classified by hand as
  `jurimetric`; Shekhar & Dwivedi 2021 (India) and Ayanlola et al. 2025
  (Nigeria) both contribute real regression coefficients quantifying a
  legal/institutional mechanism's effect on a sanitation-access outcome
  (wealth-index inequality in toilet-technology access; weak sanitation-law
  enforcement's effect on open defecation, beta=0.47, p=0.002); and Rojas
  Rivera 2026 (Colombia) is a genuine natural-institutional-variation
  panel-data study of decentralization's effects on municipal water/
  sewerage coverage, flagged as a strong future `effect_sizes.csv`
  candidate once its full regression-results table is retrieved. A
  corpus-wide duplicate audit re-run afterwards came back clean against the
  resulting 385-study corpus.
- **2026-09-16 (still later the same day): single-record screening
  (S387, S388), a Cowork Scopus-retrieval status merge (no new decisions),
  then an 18-PDF Google Drive batch, 11 new includes (S389–S399).** Full
  detail in `CHANGELOG.md`. Notably: a genuine quasi-experimental
  difference-in-differences study (S398, dos Santos Nascimento Sobrinho &
  da Mota Silveira Neto 2025, Recife's ZEIS zoning-law intervention) was
  added to `effect_sizes.csv`; and the corpus-wide duplicate audit caught
  a genuine duplicate this round — Alvaredo 2025 (Barreiro water-network
  history) had already been extracted as S102 from abstract-only text on
  2026-09-15, and reached the pipeline a second time this round under a
  differently-formatted title. Rather than keep both, the fuller full-text
  extraction obtained this round was merged into S102's row and the
  duplicate record was corrected to exclude/E08, disclosed in full in
  `CHANGELOG.md` alongside a process note about a request-limit PDF-read
  truncation that was caught and corrected before it could affect any
  screening decision.
- **2026-09-16 (still later the same day): single-record screening —
  Carré & Deroubaix 2009 excluded (E04, wrong outcome — utility
  revenue-model/tariff-sustainability focus, not household access/
  exclusion), Tsanga Tabi 2009 included (S400).** Full detail in
  `CHANGELOG.md`. Tsanga Tabi's mixed-methods case study (Vannes municipal
  utility and a Loiret private-concession department) documents France's
  LEMA (2006) article 1 disconnection-prohibition provision, several
  municipal anti-disconnection arretes later annulled by administrative
  tribunals as exceeding municipal competence, and case-study data on
  water-disconnection counts and solidarity-aid-scheme take-up. `S399`
  remains a permanent gap in the `study_id` sequence (like `S227`) — see
  the duplicate-merge note above; S400 continues the sequence from S398
  rather than reusing it.
- **2026-09-17: second Antigravity Drive batch — 34 PDFs, 18 new includes
  (S401–S418), 1 retrieval mismatch flagged.** Full detail in
  `CHANGELOG.md`. Before screening, one delivered PDF (`R81549C4709FC`)
  was found to contain the wrong book chapters entirely (chs.19-20 of a
  Handbook of Climate Justice instead of the requested ch.18) — caught by
  checking the PDF's visible chapter titles against the screening
  database before making any judgment; left open, flagged
  `wrong_file_retrieved`, not screened. Of the 18 new includes, S404
  (Mwaura et al. 2021, Kenya) contributes a genuine quasi-experimental
  effect estimate (WRUA legal-membership status reducing water poverty by
  14-32% across three independent estimators) added to
  `effect_sizes.csv`; S412 (Ranganathan & Balazs 2015) and S416 (Roy 2013)
  are direct empirical instances of the review's core administrative-
  exclusion thesis (municipal-jurisdiction and slum-notification-status
  exclusion from water connection); S418 (Brown et al. 2023, *Lancet
  Global Health*) is a documented-search-strategy secondary review of
  racism/exclusion mechanisms in high-income-country water/sanitation
  access, flagged `study_design_class = systematic_review_secondary`. A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 416-study corpus.
- **2026-09-17 (later the same day): nineteenth full-text screening batch —
  5 researcher-supplied PDFs, 4 new includes (S419–S422).** Full detail in
  `CHANGELOG.md`. Notably, S420 (Helgegren 2020, a Bolivian PhD thesis)
  overlaps with an already-extracted study: its Paper II reports the same
  findings as S410 (a separately-published journal article extracted the
  previous day). Rather than re-extract or duplicate-merge, S420 was
  deliberately restricted to the thesis's genuinely additional findings
  (regime-analysis coverage data and a summary of two other papers),
  explicitly excluding Paper II's content to avoid double-counting — a
  narrower resolution than the earlier S102/S399 duplicate-merge case,
  appropriate here because the two records capture non-overlapping
  evidence rather than the same study reaching the pipeline twice. S421
  (Agade et al. 2022, Kenya) documents WRUA corruption and enforcement
  gaps in the Maasai rangelands via 80 interviews plus a 12-month police
  conflict log; S422 (OECD 2021) is a 48-country cross-national survey
  empirically linking water-governance mechanisms to household/urban
  water-security outcomes. A corpus-wide duplicate audit re-run afterwards
  came back clean against the resulting 420-study corpus.
- **2026-09-17 (later the same day): twentieth full-text screening batch —
  Google Drive Zotero-storage batch 3, 45 new includes (S423–S467), 4
  excluded, 2 flagged `wrong_file_retrieved`.** Full detail in
  `CHANGELOG.md`. Retrieved 51 confirmed record_id/Drive-fileId matches
  plus content-identified 15 further ambiguous-filename Google Docs (13 of
  which turned out to be duplicate Zotero web-snapshots of already-matched
  records, 1 was a blank/unloaded snapshot, and 1 supplied genuine
  substitute full-text content — in Portuguese, via SciELO — for a 156MB
  PDF, S445/`R4B40A3139B39`, that could not otherwise be downloaded).
  Notable includes: S435 (Allaire & Ignacio 2026), a quasi-experimental
  panel study finding California water-district electoral fragmentation
  predicts uncontested board elections (IRR=1.23, p<0.001) which in turn
  predict lower adoption of low-income bill-assistance programs (predicted
  probability 0.31→0.12); S448 (Ribeiro et al. 2026), a panel-regression
  study of Brazilian intermunicipal water/wastewater cooperation with a
  locatable, signed coefficient (-7.253, SE=3.721, p<0.10) on financial
  performance; and S445, a national Brazilian school-census logistic-
  regression study finding regional/indigenous-land/school-size odds
  ratios up to 6.40 (p<0.001) for lacking school water supply. Two records
  were flagged `wrong_file_retrieved` and left open rather than screened:
  `R5725BF04FB9F` (only a 2-page erratum notice was delivered, not the
  substantive article) and `R81549C4709FC` (a *second* wrong-file
  delivery — a different book chapter than the one previously flagged).
  4 studies were added to `effect_sizes.csv` (S434, S435, S445, S448). A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 465-study corpus.
- **2026-09-18: twenty-first full-text screening batch — Google Drive
  Zotero-storage re-sync (batch 5), 2 new includes (S468–S469).** Full
  detail in `CHANGELOG.md`. This Drive folder was a fresh full re-sync of
  the researcher's Zotero library (111 storage-key subfolders, 110 real
  attachments plus one Zotero-master-spreadsheet-only folder), heavily
  overlapping keys already screened in the prior three Drive batches:
  100 of the 110 real attachments matched confidently to already-decided
  records and were skipped without re-processing; a further 8 had
  meaningless Zotero filenames (`pad`, `wp.2025`, `ws.2025`, DOI-suffix
  filenames, etc.) and were content-identified by downloading and reading
  each — all 8 also turned out to be duplicate web-snapshots of
  already-decided records (including a second confirmation, via full-text
  read this time rather than filename alone, that both
  `wrong_file_retrieved`-flagged records — `R81549C4709FC`, `R5725BF04FB9F`
  — are still genuinely wrong on this third attempt). Only 2 records were
  both genuinely open and newly matched: S468 (Santos et al. 2025,
  qualitative case study of institutional fragmentation, tariff
  affordability, and community-led standpipe self-management across 4
  overlapping water/sanitation agencies in Beira, Mozambique) and S469
  (Alam et al. 2025, a 384-household mixed-methods study of administrative
  barriers to sewer connection in Dhaka, Bangladesh, including landlords
  fined by police for unauthorised road-cutting after DWASA took no action
  on a compliant, multi-year-pending connection application). Neither had
  a genuine, non-fabricated single exposure-comparator effect estimate, so
  `effect_sizes.csv` is unchanged at 20 rows. A corpus-wide duplicate audit
  re-run afterwards (4 independent methods) came back clean against the
  resulting 467-study corpus.

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
- Full-text screening itself is far from complete: 920 of the 3,659
  Phase-5 includes have been assessed; 2,739 records have not yet been
  reached, not confirmed unretrievable, since retrieval depends entirely
  on the researcher supplying full-text PDFs.
- Extraction (Phase 8) is caught up with screening completely — all 467
  current full-text includes are extracted, no outstanding gap.
- **No risk-of-bias rating has been performed on the great majority of the
  467 extracted studies** (a first 12-study partial pilot batch was
  appraised 2026-09-16, plus 2 further studies -- S370, S372 -- with a
  positively-determined AMSTAR 2 rating, see `PRISMA_WORKFLOW.md` Phase 9) —
  `risk_of_bias_tool` is identified per study, but
  `risk_of_bias_rating` is deliberately left blank for the rest pending the official
  version of each appraisal instrument (`RISK_OF_BIAS.md`'s explicit
  prohibition on reconstructing a validated tool from memory). This is a
  real, reportable limitation at this stage, not an oversight.
- **No quantitative-feasibility determination (Phase 11) has been made
  for any candidate synthesis family** — 178 studies being individually
  eligible for quantitative synthesis is not the same as any family
  clearing `ANALYSIS_PLAN.md` §2's full decision tree (empirical basis →
  substantively comparable estimand → enough independent, non-secondary
  studies). That corpus-level judgment has not been made for any family.
  **2026-09-16: a stricter first pass through `05_analysis/effect_sizes/
  effect_sizes.csv` found only 11 of those 124 studies have a genuine,
  non-fabricated exposure-vs-comparator contrast and a locatable effect
  estimate** (8 fit `PROJECT_SPEC.md` §8's Families A/B/C; 3 do not match
  any existing family's exposure/outcome definitions). **Extended the same
  day with 2 more studies (S353, S358) from a later PDF batch, then 1
  more the same day (S388, Li/McManus/Cronk 2025, Liberia water-point
  functionality -- a genuine institutional-management exposure/comparator
  with a real adjusted OR, but left without a synthesis_family assignment
  since it does not cleanly fit Family A/B/C), bringing
  the total to 14 (9 fit Families A/B/C, 5 do not), then 1 more (S398,
  dos Santos Nascimento Sobrinho & da Mota Silveira Neto 2025, a genuine
  quasi-experimental difference-in-differences evaluation of Recife's
  ZEIS zoning-law intervention, Family A), bringing the total to 15 (10
  fit Families A/B/C, 5 do not), then 1 more (S404, Mwaura et al. 2021, a
  genuine quasi-experimental estimate of WRUA legal-membership status'
  effect on water poverty, Family A), bringing the total to 16 (11 fit
  Families A/B/C, 5 do not), then 4 more from Google Drive batch 3 (S434
  mining-proximity/water-security IV estimate; S435 water-board-election
  competitiveness/bill-assistance-adoption marginal effect; S445 school-
  census regional funding-formula-disadvantage odds ratios; S448
  intermunicipal-cooperation/financial-performance panel coefficient; none
  fit Families A/B/C), bringing the total to 20 (11 fit Families A/B/C, 9
  do not).** Every row has
  `included_in_pooled_estimate = FALSE` — no pooling decision has been
  made for any family, and no family yet has more than one study sharing
  a genuinely comparable exposure-comparator definition, so none is close
  to clearing the decision tree yet. See `CHANGELOG.md` 2026-09-17 for the
  full list and exclusion rationale.
- Effect sizes now exist for 20 studies in `effect_sizes.csv` (added
  2026-09-16, extended 2026-09-17), but none is pooled, and no family-level meta-analysis has
  been run. Phases 12–16 (meta-analysis, SWiM synthesis, sensitivity
  analysis, publication bias, PRISMA reporting) have R-script/template
  scaffolding built but are all blocked on Phase 11 and have not been run
  against real data.

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
