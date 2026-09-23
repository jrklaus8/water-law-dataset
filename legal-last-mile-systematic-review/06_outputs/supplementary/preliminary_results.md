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
  **1,011 of 3,659 records decided (508 include / 503 exclude)** — see
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
- **2026-09-18 (later the same day): twenty-second full-text screening
  batch — 4 researcher-supplied PDFs, 2 excluded, 2 new includes
  (S470–S471).** Full detail in `CHANGELOG.md`. Excludes: Garrett et al.
  2025's PFAS-contamination community-response case study (E03, wrong
  exposure — water-quality-only) and Kwame et al. 2025's Yendi Hospital
  water-inaccessibility ethnography (E02, wrong population — institutional
  healthcare-facility WASH provision, not household/community access,
  directly analogous to the earlier Ayalew et al. 2025 E02 exclusion).
  Includes: S470 (Amorim, Resende, Miranda & Freistadt 2025), a
  quasi-experimental panel study of 572 Minas Gerais municipalities finding
  a ~19-percentage-point increase in social-tariff implementation
  associated with a 2021 regulatory-enforcement intervention by Brazil's
  Arsae-MG regulator (p<0.01, corroborated by Wilcoxon signed-rank tests
  significant in all 11 macro-regions); and S471 (Hughes, Kirchhoff, Lee &
  Switzer 2025), a national US cross-sectional study of 2,119 municipal
  drinking-water utilities finding mayor-led governments charge $1.58/month
  less for basic water service than manager/council-led governments
  (p<0.05, organizational-structure model). Both new includes were added to
  `effect_sizes.csv` (20→22 rows). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 469-study corpus.
- **2026-09-18 (later the same day): twenty-third full-text screening
  batch — 3 researcher-supplied PDFs, 1 duplicate re-upload, 1 excluded,
  1 new include (S472).** Full detail in `CHANGELOG.md`. One PDF
  (Frempong et al. 2025, mining and water security in Ghana) was a
  redundant re-upload of a record already screened, included, and
  extracted as S434 in an earlier batch — verified and skipped without
  reprocessing. Excluded: Vij & Narain 2025's systematic review of
  peri-urban climate-change adaptation and water (in)security in Asia/
  Africa (E01, wrong topic — a climate-vulnerability/adaptation review,
  not a household/community water-or-sanitation-service-access study).
  Included: S472 (Lopez, Ofori, Mdee & Llaxacondor 2025), a qualitative
  case study of container-based sanitation (CBS) in Pamplona Alta, an
  informal settlement in Lima, Peru, where 92% of ~12,300 households lack
  a sewer connection. Finds that Lima's fragmented sanitation regime and a
  legal prohibition (Legislative Decree No. 1280) barring ecological-
  sanitation providers from delivering sewerage/wastewater services blocks
  scaling CBS despite high social acceptability, while state service
  delivery remains formally conditioned on legal land title, structurally
  excluding informal residents. Not eligible for `effect_sizes.csv`
  (qualitative design, no statistical effect estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the resulting
  470-study corpus.
- **2026-09-18 (later the same day): twenty-fourth full-text screening
  batch — 4 researcher-supplied PDFs, 2 excludes + 2 new includes
  (S473–S474).** Full detail in `CHANGELOG.md`. Excludes: Bolatova et al.
  2025's Kazakhstan rural household water-quality-satisfaction survey (E03,
  wrong exposure — water-quality/satisfaction-only, no legal/administrative
  connection-mechanism content) and Omalanga & Onyari 2025's broad
  systematic review of Water Resources Management in South Africa (E01,
  wrong topic — general resource-management review, not focused on
  household/community service-access mechanisms). Includes: S473 (Nyambwe
  et al. 2025), a 655-household Bukavu (DR Congo) survey finding distance
  from city center significantly predicts drinking-water coverage
  (r=-0.42, p<0.05) and land tenure insecurity (29.74% of households
  lacking formal titles) concentrates poor REGIDESO connection in informal
  peripheral neighborhoods; and S474 (Kehinde et al. 2025), a mixed-methods
  study finding Canada's federal government invested CA$598 million across
  149 First Nations drinking-water infrastructure projects (2016-2022) yet
  38 Long-Term Drinking Water Advisories remained active in 30 communities
  as of July 2025, with under 0.1% of funding combined going to operator
  training and source-water protection. Neither new include was added to
  `effect_sizes.csv` (S473's findings are geographic/correlational rather
  than a legal-mechanism exposure-comparator; S474 is descriptive
  government-expenditure data with no inferential test). A corpus-wide
  duplicate audit re-run afterwards came back clean against the resulting
  472-study corpus.
- **2026-09-18 (later the same day): twenty-fifth full-text screening
  batch — 1 researcher-supplied PDF, 1 new include (S475).** Full detail
  in `CHANGELOG.md`. Included: Murebwayire, Nilsson, Nhapi & Wali (2025), a
  PRISMA 2020 systematic review of 73 publications (36 scientific studies +
  32 government/policy documents) on household fecal sludge management in
  Kigali, Rwanda, directly reviewing 23 government laws/strategies/
  regulations/policies/standards/guidelines and documenting institutional
  fragmentation across overlapping mandates, seldom-enforced building-law
  approval requirements for on-site sanitation, authorities prioritizing
  sanctions over supportive regulatory mechanisms, and recurring
  tenant-landlord disputes over pit-latrine maintenance responsibility,
  against a USD 316 million annual WASH-sector funding gap. Not eligible
  for `effect_sizes.csv` (thematic/narrative secondary synthesis across
  heterogeneous sources, not a single quantitative exposure-comparator
  estimate). A corpus-wide duplicate audit re-run afterwards came back
  clean against the resulting 473-study corpus.
- **2026-09-18 (later the same day): twenty-sixth full-text screening
  batch — 9 researcher-supplied items (8 PDFs + 1 Google Drive share), 7
  excludes + 2 new includes (S476-S477).** Full detail in `CHANGELOG.md`.
  Two items were duplicate re-uploads of already-decided/extracted records
  (Beker & Kansal 2023 Ethiopia, already S449; Araújo et al. 2024 Federal
  District of Brazil, already S462) and were skipped without reprocessing.
  Excludes: an Aba, Nigeria drinking-water quality/health-risk assessment
  (E03); a Visakhapatnam, India trust-in-government/participation survey
  (E01); a Kyrgyz Republic water-sector workforce-training proposal (E01);
  a Cameroon non-revenue-water engineering assessment (E06); a cross-country
  macro-econometric water-poverty-cycle study (E01); a Canadian Indigenous
  water-insecurity review explicitly restricted by its own authors to
  microbiological/technical issues (E03); and a Blue Pacific WASH/climate/
  gender civil-society-coalition scoping review (E01). Includes: S476 (Khan
  & Fenner 2024), a Bangladesh household survey finding a private operator's
  5,000 BDT upfront connection fee and shutdown of nearby community tap
  points drove low-income households toward unsafe water sources; and S477
  (Ouma, Njoroge & Weru, in Di Giovanni & Bercovich eds. 2025, *Legal
  Empowerment in Informal Settlements*), a Mukuru, Nairobi case study of a
  Special Planning Area co-producing simplified-sewer/prepaid-water
  infrastructure after documenting a "poverty penalty" of 172% higher
  per-m³ water costs, with a KES 5,000 connection fee found prohibitive
  enough to require a dedicated micro-loan facility. Neither new include
  was added to `effect_sizes.csv` (S476's reported statistic is a bare
  p-value with no effect-size magnitude; S477 is a qualitative case study
  with descriptive counts only). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 475-study corpus.
- **2026-09-18 (later the same day): twenty-seventh full-text screening
  batch — 7 researcher-supplied PDFs, 2 excludes + 2 new includes
  (S478-S479).** Full detail in `CHANGELOG.md`. Three items were skipped
  without reprocessing: two duplicate re-uploads of already-decided
  records (D'Odorico et al.'s water-grabbing paper, already excluded E01;
  Sisay et al.'s Addis Ababa FSM/sanitation-safety study, already S463),
  and a third failed retrieval of the wrong chapter for the still-open
  Singh & Singh Kathmandu record. Excludes: a conceptual dynamical-systems
  model of utility-level institutional friction in stylized Phoenix Metro
  cities (E01), and a bottled-water-consumption/tap-water-trust review
  whose affordability content is a boxed aside rather than its own focal
  contribution (E04). Includes: S478 (Albright, Coleman Flowers, Kramer &
  Weinthal 2024), a 294-household Lowndes County, Alabama survey
  documenting septic-system enforcement (fines/arrests since 2002) against
  a 2023 US DOJ/HHS interim agreement requiring sanitation access
  regardless of ability to pay; and S479 (Dobbin et al. 2024), a narrative
  review of unregulated-water-user regulation and assistance-program
  eligibility barriers (including a USDA owner-occupancy rule excluding
  renters) across 7 Southwestern US jurisdictions. Neither new include was
  added to `effect_sizes.csv` (no locatable inferential exposure-comparator
  estimate in either). A corpus-wide duplicate audit re-run afterwards
  came back clean against the resulting 477-study corpus.
- **2026-09-18 (later the same day): twenty-eighth full-text screening
  batch — 10 researcher-supplied PDFs, 7 excludes + 2 new includes
  (S480-S481).** Full detail in `CHANGELOG.md`. One item was a duplicate
  re-upload of an already-decided record (Brown et al. 2023 *Lancet Global
  Health* review on racism/exclusion in HIC water and sanitation access,
  already S418) and was skipped. All 7 excludes were E01 (wrong topic):
  a Harare, Zimbabwe WEF-nexus reliability/governance-perception survey; a
  97-country tax-expenditure/SDG fiscal simulation; a South African
  treatment-plant-worker institutional-capacity study; a Utah utility
  water-supply-reliability definitional study; an Ecuadorian utility
  technical-efficiency benchmarking study; an Iranian agricultural/
  irrigation water-scarcity vulnerability study; and a Brazilian WSS
  utility-regionalization financial-feasibility study. Includes: S480
  (Maxcy-Brown et al. 2024), an NPDES compliance-data analysis across 59
  Alabama Black Belt wastewater facilities (37.3% average noncompliance)
  combined with a legal review of homeowner on-site-system permitting
  responsibility and funding programs favoring utilities over households;
  and S481 (Machado et al. 2023), an 11-specialist Delphi expert panel on
  legal/institutional strategies for rural community-managed water supply
  in Brazil, covering national sanitation law, municipal-community legal
  instruments, and payment-capacity-based tariffs with default-driven
  service cuts. Neither new include was added to `effect_sizes.csv` (no
  locatable inferential exposure-comparator estimate in either). A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 479-study corpus.
- **2026-09-18 (later the same day): twenty-ninth full-text screening
  batch — 8 researcher-supplied PDFs, 5 excludes + 2 new includes
  (S482-S483).** Full detail in `CHANGELOG.md`. One item was a duplicate
  re-upload of an already-decided record (Beyene et al. 2023 Gondar urban
  governance index study, already S401) and was skipped. All 5 excludes
  were E01 (wrong topic): a Kinshasa school WASH/hand-hygiene-behavior
  study; an Arctic water-security scoping review whose own protocol
  explicitly excludes governance/law/policy-perspective studies; a
  cross-country Sanitation Coverage Index benchmarking study; a
  20-municipality South African panel econometric study of social/
  political determinants of water investment; and a gender-differentiated
  Water Poverty Index study in peri-urban Dhaka. Includes: S482 (Meehan et
  al. 2023), a conceptual synthesis on how private-home-based water/
  sanitation provision structurally excludes unhoused people, citing named
  UK anti-homeless statutes criminalizing resulting public urination/
  defecation; and S483 (Mutono et al. 2022), an 11-year Nairobi utility
  panel study finding high-income residents six times more likely to
  receive sufficient water than low-income residents (rate ratio 5.78,
  95% CI 5.34-6.25, p<0.001), tied to connection-type and tenure-security
  disparities. S483 was **added to `effect_sizes.csv`** as a genuine
  exposure-comparator estimate with rate ratios, CIs, p-values and N. A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 481-study corpus.
- **2026-09-18 (later the same day): thirtieth full-text screening batch —
  5 researcher-supplied PDFs, 2 excludes + 3 new includes (S484-S486).**
  Full detail in `CHANGELOG.md`. Excludes (both E01): a GIS drive-time
  study of proximity to voluntary water-quality testing facilities in
  Alberta, Canada; and a Granger-causality panel study of municipal
  water-investment determinants across 8 South African metros. Includes:
  S484 (Monyai et al. 2022), a 117-participant qualitative study of two
  South African municipalities finding weak by-law enforcement against
  illegal water connections due to political complicity and uncompensated
  pipeline-easement land disputes; S485 (Dektar et al. 2022), a Karamoja,
  Uganda case study of weak tariff/regulatory-policy enforcement and risky
  payment-in-kind tariff arrangements among private rural water operators;
  and S486 (Calderón-Villarreal et al. 2022), a binational mixed-methods
  study of deported/homeless Tijuana River canal residents documenting
  ID-based hospital-eligibility barriers, fee-conditioned sanitation
  access, and police raids forcing contact with heavily contaminated water.
  None of the three new includes was added to `effect_sizes.csv` (S484/
  S485 are qualitative with no inferential estimate; S486's real OR is a
  health outcome, not a legal-mechanism access estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the resulting
  484-study corpus.
- **2026-09-18 (later the same day): thirty-first full-text screening
  batch — 5 researcher-supplied PDFs, 3 excludes + 2 new includes
  (S487-S488).** Full detail in `CHANGELOG.md`. All 3 excludes were E01
  (wrong topic): a theoretical Political Ecology water-energy-food nexus
  paper with only incidental water-service content; an fsQCA of 11
  donor/NGO/government collaborative WASH-program cases identifying
  program-design conditions rather than household-level access
  mechanisms; and a Malawi climate-resilience/rainfall-trend study
  evaluating water-policy effectiveness against flood/drought
  preparedness, with only an incidental borehole-fee mention. Includes:
  S487 (Kusi-Appiah & Mkandawire 2022), a 52-participant Mzuzu, Malawi
  study finding exorbitant utility tariffs exclude the poor from formal
  connection, disconnection for non-payment, and government non-
  recognition of informal settlements barring connection eligibility;
  and S488 (Ahabwe et al. 2022), a Uganda governance study documenting
  the constitutional/statutory right-to-water framework against
  persistent gaps — unregulated, "exorbitantly high" faecal-sludge fees
  outside Kampala and an unimplemented 2015 World Bank tariff-overhaul
  recommendation. Neither new include was added to `effect_sizes.csv`
  (qualitative analyses with no inferential exposure-comparator
  estimate). A corpus-wide duplicate audit re-run afterwards came back
  clean against the resulting 486-study corpus.
- **2026-09-18 (later the same day): thirty-second full-text screening
  batch — 5 researcher-supplied PDFs, 2 excludes + 2 new includes
  (S489-S490).** Full detail in `CHANGELOG.md`. One item was a duplicate
  re-upload of an already-decided record (Hove et al. 2022 South Africa
  PHC/water-governance narrative review, already excluded E04) and was
  skipped. Both excludes were E01 (wrong topic): a global composite SDG6
  index built across 232 countries from aggregate statistics, and a
  15-interview Ghana gender-empowerment-in-WASH study whose connection-
  disparity mention was incidental to its own focal contribution.
  Includes: S489 (Koehler et al. 2021), a 1,215-household Kwale County,
  Kenya study finding households who consider their water supply costly
  have roughly half the odds of committing to a professional maintenance
  contract (OR=0.532, p=0.015); and S490 (Aliyev 2021), an Oxfam
  practitioner case study of rural Tajikistan documenting a blurred
  regulatory boundary between two government water-sector bodies, over 50
  detected illegal connections, and 74-349% operational-cost increases
  driving tariff rises across 3 Water User Associations. S489 was **added
  to `effect_sizes.csv`** as a genuine exposure-comparator estimate with
  an odds ratio, SE, p-value and N. A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 488-study corpus.
- **2026-09-18 (later the same day): thirty-third full-text screening
  batch — 5 researcher-supplied PDFs, 4 excludes + 1 new include
  (S491).** Full detail in `CHANGELOG.md`. Excludes: a 167-article SDG6
  status review spanning all SSA countries and all SDG6 targets, with
  household-level access only one of many sections (E01); a corporate
  CSR/water-use-management study of flower firms in Naivasha, Kenya (E01);
  a narrative synthesis of Indonesia's historical water-coverage
  statistics with no defined empirical study design (E05); and a
  scenario-based life-cycle cost assessment methodology paper for a
  school sanitation facility in rural India (E06, engineering only).
  Include: S491 (Sempewo et al. 2021), a 1,639-household Uganda survey
  finding 67% of households unwilling to pay for water during the
  March-June 2020 COVID-19 lockdown, set against a presidential directive
  suspending water disconnections nationwide; households without an
  existing formal payment relationship had roughly double the odds of
  unwillingness to pay (OR=2.125, 95% CI 1.581-2.857, p<0.001). S491 was
  **added to `effect_sizes.csv`** as a genuine exposure-comparator
  estimate tied directly to the disconnection-moratorium enforcement
  mechanism. A corpus-wide duplicate audit re-run afterwards came back
  clean against the resulting 489-study corpus.
- **2026-09-18 (later the same day): thirty-fourth full-text screening
  batch — 4 researcher-supplied PDFs, 1 exclude + 3 new includes
  (S492-S494).** Full detail in `CHANGELOG.md`. Exclude: a Bayesian
  mixed-effects regression study of 2,867 California water systems
  examining SDWA health-based violation counts (water quality) by
  institutional/governance type — no household-level legal-administrative
  eligibility/burden/discretion/enforcement content (E03). Includes: S492
  (Millington & Scheba 2020), a qualitative Cape Town "Day Zero" case
  study documenting an arduous indigent-registration process for Free
  Basic Water eligibility and prepaid Water Management Devices that
  automatically cut supply once the allocation is exhausted (legalized by
  the Constitutional Court's Mazibuko ruling); S493 (Giner & Pavon 2021),
  a mixed-methods program evaluation of first-time wastewater service to
  Texas colonias documenting the pre-1989 absence of county land-use
  enforcement that enabled colonia formation and subsequent Model
  Subdivision Rules legislation, with wastewater coverage growing from
  under 20% (1995) to 77% (2018); and S494 (Rahmasary et al. 2021), a City
  Blueprint governance-capacity diagnostic of Bandung, Indonesia,
  documenting slum-area legalization providing legal tenure security and
  infrastructure access, included for consistency with a companion City
  Blueprint paper already in the corpus (S172). None of the three new
  includes was added to `effect_sizes.csv` (qualitative case study;
  county-level GWR standardized residuals rather than an individual
  exposure-comparator estimate; and standardized diagnostic indicator
  scores, respectively — none meets the strict effect-size bar). A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 492-study corpus.
- **2026-09-18 (later the same day): thirty-fifth full-text screening
  batch — 5 researcher-supplied PDFs, 2 excludes + 1 new include
  (S495).** Full detail in `CHANGELOG.md`. Two items were duplicate
  re-uploads of already-decided, already-extracted records (Cooper et al.
  2021 environmental-health displacement scoping review, already S427; and
  Schramm & Ibrahim 2021 "Hacking the pipes" Nairobi study, already S460)
  and were skipped. Both excludes were E01 (wrong topic): a 600-respondent
  intra-household gender decision-making autonomy survey with no
  legal-administrative connection-mechanism content, and a 173-study
  systematic review of informal household water-insecurity coping
  behaviors (storage, purchasing, treatment, relocation). Include: S495
  (Samuel, Agbola & Olojede 2021), a mixed-methods case study of three
  medium-sized Nigerian cities documenting institutional fragmentation
  across federal/state/local/NGO/donor water-point providers (45.8% of 606
  facilities non-functional), unregulated private water vendors, and local
  government fiscal-autonomy constraints. Not added to `effect_sizes.csv`
  (descriptive secondary data and qualitative interviews, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 493-study corpus.
- **2026-09-18 (later the same day): thirty-sixth full-text screening
  batch — 5 researcher-supplied PDFs, 3 new includes (S496-S498).** Full
  detail in `CHANGELOG.md`. Two items were duplicate re-uploads of
  already-decided records (Venkataramanan et al. 2020 coping-strategies
  review, already excluded E01 earlier this same day; and Zvobgo & Do 2020
  "Safe Hands" Chitungwiza study, already included as S461) and were
  skipped. Includes: S496 (Komakech, Kwezi & Ali 2020), a mixed-methods
  multi-case study of three Tanzanian prepaid-water-technology schemes
  documenting cost-based exclusion from prepaid water tags and CBWSO
  discretion in identifying "vulnerable households" for free water credit;
  S497 (Shah & Badiger 2020), a qualitative institutional case study of
  Darjeeling, India documenting a formal water-connection process
  requiring three legal land/residency documents plus a tiered connection
  fee (USD250-520), and municipal discretion over public-standpipe
  approval requests; and S498 (Shrestha, Joshi & Roth 2020), a 74-interview
  qualitative case study of caste-based exclusion of Dalit households from
  a registered water-user committee in peri-urban Kathmandu Valley, Nepal,
  despite prior-use rights and Nepal's mandatory-representation policy.
  None of the three new includes was added to `effect_sizes.csv`
  (descriptive household-survey percentages and qualitative case studies,
  no inferential exposure-comparator estimate). A corpus-wide duplicate
  audit re-run afterwards came back clean against the resulting
  496-study corpus.
- **2026-09-18 (later the same day): thirty-seventh full-text screening
  batch — 5 researcher-supplied PDFs, 1 exclude + 4 new includes
  (S499-S502), bringing full extraction to 500 studies.** Full detail in
  `CHANGELOG.md`. Exclude: a comparative secondary-literature study of
  urban water security (SETEG framework) across three arid-region cities,
  focused on aquifer overexploitation and agricultural-vs-urban water
  competition, with no household-level legal-administrative mechanism
  content (E01). Includes: S499 (Ekane et al. 2020), a 17-interview
  qualitative study documenting Rwanda's Organic Law penalties for
  open defecation and Uganda's Public Health Act closure/prosecution
  provisions for dwellings lacking sanitation facilities; S500 (Mitlin &
  Walnycki 2020), a mixed-methods study of four sub-Saharan African cities
  finding water costs up to 112% of household income and 30% of Blantyre's
  piped connections disconnected for unpaid bills within 5 years; S501
  (Sharma et al. 2020), a comparative case study of two Indian Himalayan
  towns documenting a hotel/restaurant PHED-connection-eligibility bar and
  fragmented GTA/state-government water governance; and S502 (Chidambaram
  2020), an ethnographic study of Delhi's notified/non-notified slum legal
  classification determining formal piped-water-connection entitlement,
  with informal "quasi-legal" negotiated connections and enforcement risk
  for unauthorized toilet pipes. None of the four new includes was added
  to `effect_sizes.csv` (descriptive percentages or qualitative case
  studies, no inferential exposure-comparator estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the resulting
  500-study corpus.
- **2026-09-18 (later the same day): thirty-eighth full-text screening
  batch — 4 researcher-supplied PDFs, 2 excludes + 1 new include
  (S503).** Full detail in `CHANGELOG.md`. One item was a duplicate
  re-upload of an already-decided record (Scruggs, Pratesi & Fleck 2020,
  direct-potable-reuse public-acceptance study, already excluded E01) and
  was skipped. Both excludes were E01 (wrong topic): a macro cross-country
  PCA/regression analysis of national governance indicators against
  GINI-based access-inequality indices across 82 countries, and a
  structural-equation-modeling survey study of "human dignity" attitudes
  among 483 informal Doornkop (Soweto) dwellers. Include: S503 (Fischer et
  al. 2020), a mixed-methods infrastructure-audit study of Bangladesh's
  rural drinking-water sector documenting the historical DPHE
  group-application eligibility requirement for publicly funded tubewells
  and the complete regulatory vacuum (no permits, registration, or quality
  testing) now governing the private self-supply market that installs
  forty-five tubewells for every one publicly funded tubewell. Not added
  to `effect_sizes.csv` (growth-trend modeling, no individual
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 501-study corpus.
- **2026-09-18 (later the same day): thirty-ninth full-text screening
  batch — 5 researcher-supplied PDFs, 2 excludes + 2 new includes
  (S504-S505), passing 1,001 records decided.** Full detail in
  `CHANGELOG.md`. One item was a duplicate re-upload of an already-
  decided record (Wright-Contreras 2019 Hanoi transnational political-
  ecology study, already included as S441) and was skipped. Excludes: a
  technical GIS/data-integration methodology paper on rural water-planning
  administrative-data levels in India (E01), and a South Korea water-
  infrastructure asset-management engineering study of pipe/dam/sewage
  deterioration rates (E06). Includes: S504 (Enqvist & Ziervogel 2019), a
  narrative overview of Cape Town's water governance documenting the Free
  Basic Water indigent-registration policy and Water Management Devices
  installed without informed consent from some residents, complementing
  the corpus's existing Day Zero case studies; and S505 (Adank et al.
  2019), a diagnostic sustainability assessment of 7 Ethiopian small towns
  finding all 7 utilities scored below benchmark on affordable access for
  the urban poor, with 6 of 7 making no provision for shared yard
  connections. Neither new include was added to `effect_sizes.csv`
  (narrative review and descriptive diagnostic scores, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 503-study corpus.
- **2026-09-18 (later the same day): fortieth full-text screening batch —
  5 researcher-supplied PDFs, 3 excludes + 2 new includes (S506-S507),
  passing 1,006 records decided.** Full detail in `CHANGELOG.md`. This
  batch resolved a long-standing `wrong_file_retrieved` flag: the
  DuChanois et al. 2019 record had twice received only a 2-page erratum
  on prior delivery attempts; this delivery finally contained the actual
  substantive article, enabling a real decision — excluded E01 (technical/
  financial predictors of water service continuity, a reliability outcome
  rather than legal-administrative eligibility/burden/discretion/
  enforcement mechanisms). Two further excludes: a food-safety
  microbiological study of fish vendors in Malawi (E01), and a systematic
  climate-resilience review of urban-poor flood/drought/cholera
  vulnerability in sub-Saharan Africa (E01). Includes: S506 (Hoque et al.
  2019), a 2,103-household Bangladesh study with a complete tubewell
  infrastructure audit documenting elite-influenced public-tubewell
  allocation and a failed formal water-vending system undermined by
  political promises of free water; and S507 (Appiah-Effah et al. 2019),
  a Ghana sanitation policy review documenting a novel property-tax
  sanitation surcharge and the shift of sanitation financing
  responsibility onto households. Neither added to `effect_sizes.csv`
  (descriptive statistics and narrative policy review, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 505-study corpus.
- **2026-09-18 (later the same day): forty-first full-text screening
  batch — 5 researcher-supplied PDFs, 2 excludes + 1 new include
  (S508).** Full detail in `CHANGELOG.md`. Two items were duplicate
  re-uploads of already-decided, already-extracted records (Zaunda et al.
  2018 disability-friendly school WASH facilities in Rumphi, Malawi,
  already S403; Wang & Li 2018 rural China infrastructure governance/
  finance study, already S439) and were skipped. Both excludes were E01
  (wrong topic): a Transition Management-framework NGO case study focused
  on coalition-building processes in Kisumu, Kenya, and a broad Ghana
  national water-sector policy review with tariff content appearing only
  secondarily. Include: S508 (Domínguez Serrano & Castillo Pérez 2018), a
  qualitative case study of Veracruz, Mexico community water organizations
  documenting the absence of formal legal recognition for community water
  committees in Mexico (unlike Chile, Ecuador, and Central American
  peers) and the "municipal exclusivity" legal argument used to deny
  recognition. Not added to `effect_sizes.csv` (qualitative case study, no
  inferential exposure-comparator estimate). A corpus-wide duplicate audit
  re-run afterwards came back clean against the resulting 506-study
  corpus.
- **2026-09-18 (later the same day): forty-second full-text screening
  batch — 5 researcher-supplied PDFs, 2 new includes (S509-S510).** Full
  detail in `CHANGELOG.md`. Three items were duplicate re-uploads of
  already-decided records (Zaunda et al. 2018, already S403; Monney &
  Antwi-Agyei 2018, just excluded E01 earlier this same batch; Wang & Li
  2018, already S439) and were skipped. Includes: S509 (Akwataghibe et
  al. 2018), a mixed-methods evaluation of a Nigerian WASH programme's
  equity targeting, documenting hardship-based eligibility criteria for
  latrine-construction support and political interference in water-point
  siting; and S510 (Adams & Smiley 2018), a comparative Malawi
  household-survey study documenting the Water Works Act's legal basis for
  parastatal water boards and detailed connection-cost comparisons
  (household tap ~US$56 vs. private rural well ~US$1,200). Neither added
  to `effect_sizes.csv` (descriptive statistics, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 508-study corpus.
- **2026-09-18 (later the same day): forty-third full-text screening
  batch — 5 researcher-supplied PDFs, 4 excludes (all E01) + 1 new
  include (S511).** Full detail in `CHANGELOG.md`. Excludes: Arimah
  (2017), a city-level UN-Habitat infrastructure-prosperity Expert
  Opinion Survey (water one of three infrastructure types examined);
  Garn et al. (2017), a WHO-commissioned sanitation intervention-
  effectiveness systematic review/meta-analysis; Manda & Wanda (2017), a
  Karonga, Malawi disaster/everyday-risk household survey in which
  water/sanitation is only one of several everyday-risk categories; and
  Whaley & Cleaver (2017), a literature review of community-based
  water-point-committee "functionality" theory. Include: S511 (Poupeau &
  Hardy 2017), a mixed-methods case study of La Paz/El Alto, Bolivia
  water cooperatives documenting Bolivia's ASD cooperative registration
  requirement, the formal utility EPSAS's legal exclusion of
  "non-constructible" hazard zones from its service area, largely absent
  municipal recognition of cooperatives, and detailed comparative
  tariff/connection-fee data. Not added to `effect_sizes.csv`
  (descriptive case-study/survey tariff comparison, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 509-study corpus.
- **2026-09-18 (later the same day): forty-fourth full-text screening
  batch — 5 researcher-supplied PDFs, 2 duplicates skipped, 3 excludes.**
  Full detail in `CHANGELOG.md`. Two items were duplicate re-uploads of
  already-decided records (Muia Mutua, Agwata & Anyango 2017, Mavoko
  Municipality Kenya sanitation-policy-effectiveness study, already
  extracted as S423; Saraswat, Mishra & Kumar 2017, Kathmandu Valley WEAP
  scenario-modeling study, already excluded E06 — both re-reads
  independently confirmed the same decisions already on record) and were
  skipped without reprocessing. Excludes (all E01): Schramm &
  Wright-Contreras 2017, an urban-infrastructure-studies/STS analysis of
  socio-technical water/sanitation access practices at Hanoi's urban
  edge; Hutchings, Parker & Jeffrey 2016, a discourse-analysis study of
  technological-determinism framing in Bihar, India rural water policy;
  and Aadnesgaard & Willows 2016, a 52-municipality correlational study
  of South African audit outcomes versus a composite service-delivery
  score-card. No new includes this batch. A corpus-wide duplicate audit
  re-run afterwards came back clean against the resulting 509-study
  corpus.
- **2026-09-18 (later the same day): forty-fifth full-text screening
  batch — 5 researcher-supplied PDFs, 1 duplicate skipped, 1 exclude +
  3 new includes (S512-S514).** Full detail in `CHANGELOG.md`. One item
  was a duplicate re-upload of an already-decided record (Majuru,
  Suhrcke & Hunter 2016, a systematic review of household coping
  strategies for unreliable water supplies, already extracted as S438)
  and was skipped without reprocessing. Exclude: Ferro & Mercadier 2016,
  a stochastic-frontier-analysis econometric study of technical
  efficiency across 18 Chilean water/sewerage providers (E01, no
  household-level legal-administrative mechanism content). Includes:
  S512 (Dobbin & Sarathy 2015), a 3-ASADA comparative case study of
  Costa Rica's community water co-management model finding that the
  low-performing ASADA (Hatillo) operated in "blatant disregard" of ICAA
  regulations despite its board president being the most knowledgeable
  of all three about ICAA law, with no official sanctions imposed on any
  ASADA for regulatory violations; S513 (McGranahan 2015), a conceptual
  synthesis on sanitation access in deprived urban communities
  documenting that utilities "may not be allowed" to serve settlements
  until formally recognized by government, and that tenure insecurity
  can cut either way on landlords'/tenants' incentive to invest in
  sanitation improvements; and S514 (Chowns 2015), a mixed-methods study
  (679 water points, 276 users/managers) finding Malawian community
  water-point committees' Maintenance Fund savings averaged just 2% of
  the amount they should hold, against a national water-sector budget
  marginalized to 1-3% of government spending and a water ministry
  downgraded out of ministerial status. None of the three new includes
  was added to `effect_sizes.csv` (descriptive case-study, conceptual
  synthesis, and descriptive mixed-methods statistics, respectively — no
  inferential exposure-comparator estimate in any). A corpus-wide
  duplicate audit re-run afterwards came back clean against the
  resulting 512-study corpus.
- **2026-09-18 (later the same day): forty-sixth full-text screening
  batch — 4 researcher-supplied PDFs, 2 duplicates skipped, 2 new
  excludes.** Full detail in `CHANGELOG.md`. Two items were duplicate
  re-uploads of already-decided records, both independently
  re-confirmed against fresh reads before being skipped without
  reprocessing: Roy 2013 ("Negotiating marginalities: right to water in
  Delhi," Kathputli Colony case study, already extracted as S416); and
  Baird, Summers & Plummer 2013 ("Cisterns and safe drinking water in
  Canada," already excluded E03 — a fragmented-regulation review of
  private-cistern water-quality risk, not a formal-connection
  eligibility/burden/discretion/enforcement study). New excludes (both
  E01): Johnston et al. 2014, a synthesis of institutional-stakeholder,
  psychological (RANAS-model), and technical-geochemical research on
  arsenic-mitigation technology adoption in Bangladesh; and Okeola &
  Sule 2012, an Analytic Hierarchy Process decision-analysis exercise
  selecting among hypothetical public/private ownership models for a
  Nigerian urban water works. No new includes this batch. A corpus-wide
  duplicate audit re-run afterwards came back clean against the
  resulting 512-study corpus.
- **2026-09-18 (later the same day): forty-seventh full-text screening
  batch — 5 researcher-supplied PDFs, 1 duplicate skipped, 2 excludes +
  2 new includes (S515-S516).** Full detail in `CHANGELOG.md`. One item
  was a duplicate re-upload of an already-decided record (Milton, Hore,
  Hossain & Rahman 2012, Bangladesh arsenic-mitigation-programme review,
  already excluded E03) and was skipped. Excludes (both E01): Babah,
  Deida, Blake & Froelich 2012, a household-survey and water-quality
  study of Nouakchott, Mauritania's terminal-fountain distribution
  system; and Iribarnegaray & Seghezzo 2012, a Sustainable Water
  Governance Index (SWGI) methodology paper applied to Salta, Argentina.
  Includes: S515 (Ioris 2012, *Geoforum*), a 54-interview political-
  ecology case study of Lima, Peru documenting the 1961 law that
  legalized existing barriadas without resolving service exclusion, and
  residents' rejection of a low-cost condominial connection system as
  discriminatory; and S516 (Subbaraman et al. 2012, *Environment and
  Urbanization*), a four-year mixed-methods study of Kaula Bandar, a
  non-notified Mumbai slum, documenting the No Objection Certificate
  mechanism blocking service extension onto central-government land,
  criminalization of residents' informal water/sanitation coping
  strategies, and a 37-times-smaller disaster-compensation payout
  relative to a notified slum. Neither new include was added to
  `effect_sizes.csv` (qualitative case study and descriptive comparative
  statistics respectively, no inferential exposure-comparator estimate).
  A corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 514-study corpus.
- **2026-09-18 (later the same day): single-record screening — 1
  researcher-supplied PDF, 1 new include (S517), explicitly flagged by
  the researcher as a key/high-priority reference.** ★ **Morgan, B.
  (2006), "Turning off the tap: Urban water service delivery and the
  social construction of global administrative law," *European Journal
  of International Law* 17(1):215-246 — flagged by the researcher on
  2026-09-18 as a study to keep in mind as very high importance for the
  dissertation.** A comparative doctrinal/qualitative case study
  (Argentina and South Africa, part of a six-country research project)
  analyzing the Vivendi/Aguas del Aconquija v. Argentina ICSID
  investment-arbitration dispute arising from the Tucuman water
  concession (including the provincial Ombudsman's dispute-resolution
  interventions and five consecutive judges' refusal of jurisdiction
  over a collective non-payment lawsuit), and South Africa's shift from
  a "political" to a "transactional" water-tariff/disconnection
  regulatory model, alongside constitutional case law on disconnection
  due process (*Residents of Bon Vista Mansions*, *Manqele v Durban*)
  and cross-subsidy equality (*Pretoria City Council v Walker*). The
  paper's central finding is that "global administrative law" in urban
  water service delivery is constituted through iterative interaction
  between formal legal processes and informal political modes (protest,
  negotiation, media), with end-users and foreign water-service
  providers holding sharply asymmetric capacity to switch between
  domestic and international levels of governance — directly engaging
  the review's core administrative-law-as-mechanism-of-exclusion frame.
  Extracted as **S517** (`risk_of_bias_tool = CASP`, `mechanism_family =
  MULTIPLE` — `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = administrative_outcome`; see
  `extraction_database.csv` `regulatory_model` and `evidence_map.csv`
  `evidence_level` for the full high-priority flag and rationale). Not
  added to `effect_sizes.csv` (doctrinal/qualitative case study, no
  inferential exposure-comparator estimate). A corpus-wide duplicate
  audit re-run afterwards came back clean against the resulting
  515-study corpus.
- **2026-09-18 (later the same day): forty-eighth full-text screening
  batch — 4 researcher-supplied PDFs, 2 duplicates skipped, 2 new
  excludes.** Full detail in `CHANGELOG.md`. Two items were skipped
  without reprocessing: a re-upload of Morgan (2006, "Turning off the
  tap"), already extracted as S517 in the immediately preceding batch;
  and Acero et al. (2026, Alaska critical-infrastructure lifecycle
  study), already excluded E01. New excludes (both E01): Karmaksh &
  Kumar (2026), a 62-paper systematic review of urban development's
  relationship with water bodies in Indian cities spanning hydrology,
  urban planning, and governance broadly rather than household-level
  legal-administrative mechanisms; and Levin et al. (2002), a broad
  review of US drinking-water infrastructure challenges (pricing,
  consolidation, ownership, climate change, waterborne disease, SDWA
  regulatory history) focused on technical/public-health infrastructure
  for the already-connected population rather than connection-access
  barriers. No new includes this batch. A corpus-wide duplicate audit
  re-run afterwards came back clean against the resulting 515-study
  corpus.
- **2026-09-18 (later the same day): forty-ninth full-text screening
  batch — 3 researcher-supplied PDFs, 2 duplicates skipped, 1 new
  include (S518).** Full detail in `CHANGELOG.md`. Two items were
  skipped without reprocessing, deferring to their existing decisions:
  Busari (2002, Swaziland rural water-sector policy review, already
  excluded E01, matching an independent fresh read); and Chambolle
  (1999, "De l'eau pour tous?", a Suez Lyonnaise des Eaux corporate
  research synthesis on underprivileged-district water service,
  already excluded E05 for lacking a defined empirical study design —
  deferred to despite this batch's fresh read leaning toward inclusion
  given its institutional-exclusion content, per the project's standing
  rule never to re-litigate an already-decided record). Include: S518
  (Lee & Floris 2003, *Natural Resources Forum*), a four-country
  comparative policy analysis of private-sector water-utility
  participation documenting Buenos Aires's renegotiated obligation to
  extend service to suburban shanty towns and its universal-service
  cross-subsidy fee, La Paz/El Alto's labour-discounted connection fees
  and a proof-of-land-title requirement for new connections that was
  "reinstated at the insistence of the municipality" after being
  considered for waiver, and a welfare-loss counterfactual analysis of
  Lima's failed SEDAPAL privatization. Not added to `effect_sizes.csv`
  (comparative case-study/scenario-model figures, no inferential
  exposure-comparator estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 516-study corpus.
- **2026-09-18 (later the same day): fiftieth full-text screening
  batch — 9 researcher-supplied PDFs across two uploads, 3 duplicates
  skipped, 1 new include (S519).** Full detail in `CHANGELOG.md`. Three
  items were skipped without reprocessing, deferring to their existing
  decisions: Chambolle (1999, already excluded E05); Busari (2002,
  already excluded E01); and Lee & Floris (2003, already included as
  S518) — all re-uploaded a second time. Five new excludes: Mia, Parvin
  & Islam (2026, Faridpur City, Bangladesh, E01 — phenomenological
  gender/water-insecurity study lacking legal-administrative mechanism
  content); a Catalonia climate-change/water-quality conference abstract
  (Carranza et al. 2025, E09 — abstract-only, insufficient information);
  Mueller, Bosch, Gupta & Karg (2026, *Water Policy*, E07 — a
  comparative legal analysis of water-USE-PERMIT/property-rights systems
  across 110 Global South countries, but focused on resource-allocation
  permits rather than household service-connection access); Stiegler
  (2004, *Journal AWWA*, E05 — a brief "law & water" case-note column
  summarizing two US appellate decisions, including a Rhode Island
  zoning/building-permit dispute, with no defined empirical study
  design); and Kamga et al. (2026, *GeoJournal*, Fokoué Subdivision,
  West Cameroon, E06 — a GIS-based spatial-accessibility/infrastructure-
  compliance study with no legal-administrative mechanism analysis).
  Include: S519 (Birkinshaw 2026, *Urban Geography*, "Smart water?
  Corporate experiments and hybrid hydraulics in India"), a 21-month
  ethnographic study of the Malviya Nagar Water Services PPP in Delhi
  showing settlement-type-dependent access to metered connections and
  24/7 supply across the city's 8 legally differentiated settlement
  categories. Not added to `effect_sizes.csv` (ethnographic qualitative
  study, no locatable quantitative effect estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the
  resulting 517-study corpus.
- **2026-09-18 (later the same day): fifty-first full-text screening
  batch — 7 researcher-supplied PDFs across two uploads, 2 new
  includes (S520-S521).** Full detail in `CHANGELOG.md`. Five new
  excludes, all E01/E05: Mungekar et al. (2025, Bhuj/Bhopal India
  informal-governance-capacity ethnography, E01 — a governance-theory
  case study, not a household-level access-mechanism analysis); Hoang
  & Tran (2025, Hanoi nontraditional-security water-management
  framework, E01 — a broad city-wide governance-effectiveness rating,
  not household-level mechanism analysis); KC et al. (2025, Barahathawa
  Municipality, Nepal, groundwater-governance-index framework, E01 — a
  water-RESOURCE governance index dominated by irrigation use, not
  household drinking-water/sanitation SERVICE access); Thommandru et
  al. (2025, "Hydro-hegemony in the Anthropocene," E05 — a conceptual
  essay with no defined empirical study design); and Vignesh (2025,
  "Water Pricing, Tariff, and Conflicts," E05 — a case-based narrative
  synthesis with no defined case-selection methodology). Includes:
  S520 (Kharmylliem & Kipgen 2025, *Water Policy*, "Village councils,
  social capital and sustainability... Shillong"), a qualitative case
  study of clan-based property control over springs/borewells and
  village-council (dorbar shnong) governance producing locality-based
  disparities in water-connection access and scarcity; and S521 (Fono
  et al. 2025, *Australian Journal of Social Issues*, "Aboriginal and
  Torres Strait Islander Perspectives in Drinking Water Policy: A
  Realist Review"), a PRISMA-documented realist systematic review
  (5 peer-reviewed studies + 33 grey-literature sources) finding
  fragmented, inconsistent engagement of Aboriginal and Torres Strait
  Islander peoples in Australian drinking-water policy across
  national/state/local levels, with 400+ remote/regional communities
  lacking safe drinking-water access. Neither added to
  `effect_sizes.csv` (qualitative case study and realist review, no
  locatable quantitative effect estimate). A corpus-wide duplicate
  audit re-run afterwards came back clean against the resulting
  519-study corpus.
- **2026-09-18 (later the same day): fifty-second full-text screening
  batch — 6 researcher-supplied PDFs, 2 duplicates skipped, 3 new
  includes (S522-S524).** Full detail in `CHANGELOG.md`. Two items
  were skipped without reprocessing, deferring to their existing
  decisions: Fono et al. (2025, already included as S521) and Shoko
  (2025, "Structural Determinants of Conflicts and Cooperation in Rural
  Water Management," already excluded E05). One new exclude: Bae, Kang
  & Lynch (2025, *Race and Justice*, "Drinking Water Injustice:
  Racial Disparity in Regulatory Enforcement of Safe Drinking Water Act
  Violations," E04 — an OLS regression of SDWA noncompliance-duration
  by county racial composition, a water-quality regulatory-enforcement
  outcome, not a household-level connection/access mechanism, matching
  prior E03/E04 precedent for SDWA-compliance studies). Three new
  includes: S522 (Aizannon, Akueson & Moumouni-Moussa 2025, *IJRISS*,
  a mixed-methods case study of private-actor emergence in Benin's
  drinking-water market documenting rural/urban coverage disparities
  and regulatory-framework gaps); S523 (Rempel & Dobbin 2025, *Policy
  Studies Journal*, a qualitative policy-feedback case study of
  California's AB 685 human-right-to-water law, tracing a decade of
  funding, shutoff-moratorium/debt-relief, and water-system-
  consolidation-mandate feedbacks from a nominally "symbolic" policy);
  and S524 (Hernando-Arrese & Ibarra 2025, *Gender & Development*, a
  decolonial-feminist ethnographic case study of gendered water-rights
  and connection-access disparities among Rural Drinking Water
  Committees/Cooperatives (APRs) in the Toltén hydrosocial territory,
  Chile). None of the three new includes was added to
  `effect_sizes.csv` (descriptive/mixed-methods percentages and
  qualitative case studies, no locatable inferential exposure-
  comparator effect estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 522-study corpus.
- **2026-09-19: fifty-third full-text screening batch — 2 researcher-
  supplied PDFs, 2 new includes (S525-S526).** Full detail in
  `CHANGELOG.md`. Both were newly-decided records with no duplicates.
  S525 (Kachenje 2025, *IJRISS*, "Institutional Coordination Challenges
  in Service Delivery... Dar Es Salaam, Tanzania") is a qualitative
  case study finding that new water-connection application processing
  took a maximum of 30 days under the public (DAWASA) scheme versus 3
  days (private) and 6 days (community-based), and that most private
  water providers operate unregistered amid weak enforcement of
  Tanzania's water-sector regulatory instruments. S526 (Switzer &
  Teodoro 2025, *Policy Studies Journal*, "Public enterprise pricing as
  redistributive policy") is a cross-sectional OLS regression of 1,183
  US water utilities finding that local income inequality correlates
  positively and significantly with water-rate progressivity for
  government-owned utilities (p=0.005), while private/investor-owned
  ownership independently predicts more regressive pricing (p<0.001);
  the ownership-inequality interaction was directionally consistent but
  not statistically significant (p=0.387). S526's ownership-type effect
  estimate was added to `effect_sizes.csv` (Family C) as a genuine
  exposure-comparator regression result; S525 was not added
  (qualitative case study, no locatable inferential effect estimate). A
  corpus-wide duplicate audit re-run afterwards came back clean against
  the resulting 524-study corpus.
- **2026-09-19 (later the same day): fifty-fourth full-text screening
  batch — 2 researcher-supplied PDFs, 1 new include (S527).** Full
  detail in `CHANGELOG.md`. One new exclude: Suyeno et al. (2024,
  *Water Policy*, "Water governance puzzle in Riau Province: uncovering
  key actors and interactions," E01 — a Textual Network Analysis of
  government policy documents mapping actor networks in Indonesian
  regional water-supply governance; a governance-network/stakeholder-
  mapping study with no household-level population or access/
  connection outcome). Include: S527 (Khadam et al. 2024, *Cogent
  Social Sciences*, "Gender inequality, water rights and policy
  implications... Pakistan"), a qualitative expert-panel study (6
  water-sector experts) documenting that formal, documented water
  connections in Pakistan are tied to property ownership, automatically
  excluding landless households (disproportionately headed/represented
  by women) from formal supply, and reviewing provincial water-law
  gender-quota provisions (Sindh's 2018 amendment; Local Government
  Ordinance 2001 council-seat reservations, only ~19.6% filled in
  practice). Not added to `effect_sizes.csv` (qualitative expert-panel
  study, no locatable inferential effect estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the
  resulting 525-study corpus.
- **2026-09-19 (later the same day): fifty-fifth full-text screening
  batch — 3 researcher-supplied PDFs, 1 new include (S528).** Full
  detail in `CHANGELOG.md`. Two new excludes: Sibley et al. (2024,
  *Safer Communities*, "Exploring risk-scapes in Oklahoma..." E04 — a
  survey-regression study of subjective concern/attitude toward water
  infrastructure, not an objective access/connection/exclusion
  outcome); and Rodrigues, Goncalves & Marques (2024, *Water Policy*,
  "Public policies on human rights to water in informal settlements: a
  bibliometric analysis," E05 — a citation-network/bibliometric
  meta-analysis of 1,702 publications, containing no primary empirical
  findings about actual water access). Include: S528 (Santos & Ioris
  2024, *Land*, "Water Conflicts and Socioterritorial Dynamics... São
  Francisco River Transposition Project"), an ethnographic study of
  Brazil's largest water-infrastructure project finding that 845
  resettled families across 18 rural villages are not guaranteed
  access to the transposed water despite living in its immediate
  surroundings, and that popular participation is excluded from the
  project's formal governance Management Board. Not added to
  `effect_sizes.csv` (ethnographic case study, no locatable
  quantitative effect estimate). A corpus-wide duplicate audit re-run
  afterwards came back clean against the resulting 526-study corpus.
- **2026-09-21: fifty-sixth full-text screening batch — 3 researcher-
  supplied PDFs, 0 new includes.** Full detail in `CHANGELOG.md`. All
  three were excluded: Rivera-Nuñez et al. (2024, *Social Sciences*,
  "The Types of Water Conflicts in an Irrigation System in Northern
  Mexico," E07 — a social-network-analysis study whose dominant focus
  is irrigation-water resource governance among farmers, with only a
  secondary sub-theme on domestic-water self-management); Milligan et
  al. (2024, *Territory, Politics, Governance*, "The hydro-racial fix
  in infrastructural regions: Atlanta's situation in a regional water
  governance conflict," E07 — a racial-capitalism analysis of the
  interstate Apalachicola-Chattahoochee-Flint regional water-allocation
  dispute, not household-level service access); and Eduful (2024,
  *Natural Resources Forum*, "Toward good governance in water resources
  management in Ghana," E01 — a broad IWRM institutional/regulatory
  governance study of Ghana's Water Resources Commission and basin
  management boards). No extraction, evidence_map, or effect_sizes
  changes this batch.
- **2026-09-21 (later the same day): fifty-seventh full-text screening
  batch — 2 researcher-supplied PDFs, 0 new includes.** Full detail in
  `CHANGELOG.md`. Both were excluded: Walling (2024, *Territory,
  Politics, Governance*, "Governing infrastructure, development and
  inequality around deindustrialized US cities," E01 — a comparative
  Scranton/Providence social-network-analysis study of institutional
  governance networks and water-utility rate-setting authority
  location, with no household-level population or access/connection
  outcome data); and Hosseini & Yadav (2024, *LEAD Journal*, "The
  Significance of Traditional Legal Framework in Regulating
  Groundwater Rights in Iran," E05 — a doctrinal/historical analysis of
  traditional Iranian groundwater property-rights doctrine from the
  Sassanid Empire to 1906, with no primary empirical data collection).
  No extraction, evidence_map, or effect_sizes changes this batch.
- **2026-09-21 (later the same day): fifty-eighth full-text screening
  batch — 3 researcher-supplied PDFs, 2 new includes (S529-S530).**
  Full detail in `CHANGELOG.md`. One new exclude: Martín Velasco et
  al. (2023, *Water Policy*, OECD Water Governance Indicator Framework
  applied to General Pueyrredon Municipality, Argentina, E01 — a broad
  water-resources governance-capacity diagnostic, not focused on
  household-level service-connection mechanisms). Two new includes:
  S529 (Wagle 2024, *Journal of Urban Affairs*, "Water access
  disparity in Mumbai, India..."), documenting MCGM's two-tier water-
  connection entitlement system (45 LPCD standpost vs. 135 LPCD
  house-service connection) and the spatial/structural documentation
  conditionalities that render informal dwellings ineligible for the
  full entitlement; and S530 (Hofstetter, Bolding & Boelens 2023,
  *Water*, "Rooted Water Collectives in a Modernist and Neoliberal
  Imaginary..."), a comparative case study of three rural user-owned
  water collectives in South Africa and Switzerland, documenting how
  South Africa's Water Services Act 1997/Municipal Systems Act 2000
  rendered most community-based water schemes "technically illegal"
  absent formal recognition, leaving them in a legal grey zone
  dependent on municipal discretion. Neither new include was added to
  `effect_sizes.csv` (qualitative case studies, no locatable
  inferential exposure-comparator effect estimate). A corpus-wide
  duplicate audit re-run afterwards came back clean against the
  resulting 528-study corpus.
- **2026-09-21 (later the same day): fifty-ninth full-text screening
  batch — 4 researcher-supplied PDFs, 0 new includes.** Full detail in
  `CHANGELOG.md`. All four were excluded, all E01 (wrong topic): Gbekley
  et al. (2023, *Water*, Togo sanitation KAP descriptive survey —
  household wastewater/excreta practices, no legal-administrative
  access-mechanism content); Tangworachai, Wong & Lo (2023, *Studies in
  Economics and Finance*, ARDL econometric analysis of Thailand's
  aggregate regional water-consumption determinants — a macro price-
  elasticity/demand study at the utility level, not household-level
  access); Adeoti, Kandasamy & Vigneswaran (2023, *Water Policy*, a
  PRISMA systematic review of 15 studies on Nigerian water-
  infrastructure-failure causes — technical/financial/environmental/
  social/political/institutional factors broadly, not focused on
  household service-connection mechanisms); and Hellberg (2023, *Local
  Environment*, a governmentality-theory study of "the social" in
  South African water-governance social sustainability — a theoretical/
  conceptual expert-interview study, not an empirical analysis of a
  specific access mechanism's effect on household outcomes). No
  extraction, evidence_map, or effect_sizes changes this batch.
- **2026-09-21 (later the same day): full-text enrichment pass — 7
  previously abstract-only extractions upgraded to full text, 0 new
  includes/excludes.** A new local-to-remote retrieval pipeline (a local
  watcher script depositing retrieved PDFs into a shared Google Drive
  inbox folder) surfaced actual full-text PDFs for 7 studies extracted
  from abstract-only content on 2026-09-17: S430 (Ogunbode, Nigeria SDG
  6 review), S431 (Tantoh, McKay & Leonard, Bambili Cameroon rural water
  governance), S433 (Kadiri, Hyderabad informal-settlement "hydraulic
  citizenship"), S452 (Mazingisa, Wiysonge & Kgware, eThekwini school
  WASH), S455 (Yanquiling, Dressler & Smith, colonial cholera/water
  infrastructure Philippines), S458 (Dhaundiyal, Indian Himalayan Region
  heritage water architecture policy), and S467 (Opdyke et al.,
  post-conflict Marawi displacement/WASH). This was an enrichment pass,
  not a new-include batch -- all 7 were already counted in prior running
  totals, and no include/exclude decision was revisited. Full text
  confirmed S430, S455 and S458's existing extractions were already
  substantively accurate; S433 was enriched with a documentation-based
  eligibility barrier (Aadhaar card/residency certificate requirements
  formally disqualifying many informal-settlement households from
  municipal water); S431 was enriched with a direct conflict-of-interest
  finding (4 of 7 private water schemes owned by the water authority's
  own board members, who approved their own schemes and charge
  non-participants for connection) and household fee/contribution detail;
  S452 and S467 had their generic placeholder `citation`/`doi` fields
  completed with full bibliographic detail. No new `effect_sizes.csv`
  rows were added (candidate quantitative contrasts in S452 and S467
  were considered but judged not to be direct legal-administrative
  connection-access mechanisms). Duplicate audit and schema validation
  re-run clean afterwards. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later the same day): sixtieth full-text screening batch —
  3 Drive-retrieved PDFs, 1 new include (S531) — plus an S469
  data-gap fix.** Two new excludes (both E01): Fonta, Gordon & Toumpakari
  (2025, *International Journal of Health Governance*, cross-national DHS
  child-poverty comparison between Francophone/Anglophone sub-Saharan
  African states — a macro comparative-epidemiology study, not a specific
  legal-administrative access mechanism; the water-poverty dimension shows
  no significant colonial-origin difference); and Luyaba, Mbhele, Moyo,
  Nsubuga & Mafunda (2025, *Water Policy*, DEA-based infrastructure-
  efficiency/creditworthiness benchmarking of 144 South African municipal
  water authorities — utility-level, not household-level access). One new
  include: S531 (Aigbavboa, Addo, Ebekozien, Thwala & Arthur-Aidoo 2025,
  *Journal of Facilities Management*, "Appraising institutional management
  of urban water supply in Ghana"), documenting a real household water-
  connection procedure (site plan, affidavit "in some situations", letter
  to the district manager, ~2-week survey/estimate, payment before
  connection, assembly permit for individual connections). Separately,
  S469 (Alam et al. 2025, Dhaka sewer-connection barriers, extracted
  2026-09-18) was found to have blank `effect_measure`/`effect_estimate`
  fields despite 88 of 92 other fields being populated -- a genuine
  extraction oversight, now fixed from the full-text PDF with real
  barrier percentages and significance tests. Also: 4 inbox files this
  round turned out to be duplicate copies of already-decided records,
  mislabeled by a bug in the researcher's local retrieval script (DOIs
  pulled from a PDF's own reference list rather than its metadata); the
  researcher's local session fixed the matcher and removed the
  duplicates. `evidence_map.csv` updated for S531; duplicate audit and
  schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still, same day): sixty-first full-text screening
  batch — 8 Drive-retrieved PDFs, 4 excludes + 4 new includes
  (S532-S535).** Four excludes: an Arctic community wastewater-treatment
  engineering study (E01, no legal-administrative access dimension); a
  children's-participation urban-planning study (E01, no water-access
  mechanism); a Nigeria conflict/cholera commentary piece (E01, no
  empirical access-mechanism evidence); and a slum-participation study
  from an author surnamed Dewi (E01, general participatory-planning
  discussion, not a specific connection/eligibility/enforcement
  mechanism). Four new includes: S532 (Murray, Meyer & Fourie 2023,
  *Globalisation, Societies and Education*, "Workshopping Water Justice,"
  Cape Flats water-justice organizing linked to broader African
  water-rights struggles, CASP-appraised qualitative study); S533
  (Ghertner 2023, *Annals of the American Association of Geographers*,
  "Infrastructures of Overlordship," law/labor-camp material geographies
  of water servitude, appraised with the Legal Institutional Evidence
  Appraisal Framework used for doctrinal/jurimetric legal-case-analysis
  studies); S534 (Saha & Chakma 2026, *SN Social Sciences*, household
  water insecurity co-produced by environmental constraints,
  socio-economic inequality, and local water governance in rural
  Puruliya, India, MMAT-appraised mixed-methods study); and S535
  (Grisaffi, Leinster, Sipuma, Owako & Parker 2026, *PLOS Water*,
  regulator-as-activist practices for urban road-transported sanitation
  in eastern and southern Africa, CASP-appraised qualitative study). A
  self-caught process error is worth recording for the audit trail: the
  four new extraction rows were initially added to
  `extraction_database.csv` without their corresponding
  `full_text_decision`/`final_decision` = "include" being recorded in
  `full_text_screening_database.csv` in the same step, producing a
  transient mismatch (529 include vs. 533 extracted rows) that was
  caught immediately by the routine include-count-vs-extraction-row-count
  cross-check run before finalizing this batch, and fixed by explicitly
  recording the four missing include decisions (verified individually as
  still-open before being set). `evidence_map.csv` updated for all four;
  duplicate audit and schema validation re-run clean afterwards. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-second full-text screening batch — 2
  Drive-retrieved PDFs, both new includes (S536-S537).** Two more PDFs
  appeared in the Drive inbox after the sixty-first batch above; both
  were genuinely new, still-open records rather than mislabeled
  duplicates. S536: Abrams, Carden, Teta & Wagsaether (2021), *Water*,
  a qualitative climate-risk-and-vulnerability case-study comparison of
  WASH access in rural HaSinari (Limpopo) and small-town Prince Albert
  (Western Cape), South Africa. Genuine legal-administrative content:
  Prince Albert's "leiwater" irrigation-furrow water allocation is
  restricted to residents holding allocation rights recorded in
  historical Apartheid-era title deeds, structurally excluding
  North-End residents; in HaSinari the formal municipal water
  department has effectively ceased functioning and been replaced by
  elected, fee-funded community Water Committees. CASP-appraised
  (qualitative). S537: Alam, Rahat, Nawaz et al. (2025), *Global
  Health Action*, a PRISMA-ScR scoping review of 11 sewer-connection
  behaviour-change-intervention case studies across 8 countries.
  Synthesizes legal-administrative mechanisms directly: mandatory-
  connection legal provisions (e.g., Tamil Nadu's 100-meter connection
  mandate, Salvador's Law 7307/1998), indirect financial subsidies
  (free connections), and penalty provisions for non-connection;
  finds subsidy-plus-community-engagement packages substantially
  outperform legal mandates or promotion alone. AMSTAR2-flagged
  (`systematic_review_secondary`). `evidence_map.csv` updated for
  both; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-third full-text screening batch — 1
  Drive-retrieved PDF, 1 new include (S538).** Dallasheh (2022), *Journal
  of Palestine Studies*, "Would the United States Come to Nazareth's Aid?
  Local and International Contests over the City's Water" — a rigorous
  archival historical case study, not a doctrinal commentary, documenting
  a specific legal-administrative contest: Nazareth's elected municipal
  council formally held water-infrastructure authority under the
  Mandate-era Municipal Corporations Ordinance of 1934, but every step —
  funding, equipment import, foreign-currency access — required Israeli
  military-government authorization during 1948-1966 martial law. The
  national water utility (Mekorot) ultimately secured control of the
  municipal well as a precondition of network connection (1955), and in
  1966 cut off the city's entire water supply over an unpaid debt,
  explicitly as political leverage against an elected mayor. Extracted
  as S538 using the Legal Institutional Evidence Appraisal Framework
  (the convention for doctrinal/archival legal-institutional studies,
  matching S356/S364/S504/S507/S513/S517/S518/S533). `evidence_map.csv`
  updated; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-fourth full-text screening batch — 2
  Drive-retrieved PDFs, both excludes (E01).** Nkiaka (2022), *Water
  Policy*, "Exploring the socioeconomic determinants of water security in
  developing regions" — a macro cross-national econometric study (117
  countries) correlating a composite Water Security Index against GDP
  per capita, a cross-national governance-quality index, ODA-WSS, and
  female education, with no examination of any specific household- or
  applicant-level legal-administrative access mechanism. Laitinen,
  Katko, Hukka, Juuti & Juuti (2022), *Water*, "Governance and Practices
  for Achieving Sustainable and Resilient Urban Water Services" — a
  PESTEL/SWOT strategic-planning synthesis of Finnish urban water
  utility governance and infrastructure investment, again with no
  specific access-exclusion mechanism examined (Finland has
  near-universal water access). Both excluded E01 (wrong topic/wrong
  unit of analysis for this review's household/applicant-level scope).
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and
  schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-fifth full-text screening batch — 2
  Drive-retrieved PDFs, 1 already-decided duplicate + 1 new include
  (S539).** R844EAC3AEE12 turned out to be a correctly-relabeled
  re-upload of the already-excluded Dewi et al. slum-participation
  study (see the sixty-first batch above) — per the standing
  duplicate-defer rule, the existing exclude decision was not
  re-litigated; the file was simply moved to Processed. The genuinely
  new record, Zhang, Gonzalez Rivas, Grant & Warner (2022), *Water
  Policy*, "Water pricing and affordability in the US: public vs.
  private ownership," is a strong include: an OLS regression across
  the 500 largest US community water systems finds private ownership
  associated with a $144 higher annual water bill and a 1.55-point
  higher share of low-income household income spent on water (both
  p<0.01), and state regulation favorable to private providers
  (NJ/PA "fair value" legislation, Distribution System Improvement
  Charge surcharges) associated with a further $89 higher bill. Real
  legal-administrative mechanisms (PUC rate regulation, fair-value
  legislation) with clean, non-fabricated effect estimates — extracted
  as **S539** (JBI Analytical Cross Sectional) and added to
  `effect_sizes.csv` as the review's second ownership/regulation
  pricing-effect study alongside S526. `evidence_map.csv` updated;
  duplicate audit and schema validation re-run clean. Full detail in
  `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-sixth full-text screening batch — 4
  Drive-retrieved PDFs, 1 new include (S540) + 3 excludes.** Silva-Novoa
  Sanchez, Bossenbroek, Schilling & Berger (2022), *Water*, "Governance
  and Sustainability Challenges in the Water Policy of Morocco
  1995-2020," is a strong include: content analysis of Moroccan water
  policy plus 37 semi-structured interviews document real
  legal-administrative access mechanisms — well-digging permits
  reportedly requiring bribery, drip-irrigation subsidy eligibility
  contingent on a tribal land-use certificate that itself requires a
  digging permit (a circular exclusion of tenure-insecure farmers),
  institutional fragmentation across the Ministries of Agriculture,
  Water, and Interior, and unequal Kharouba water-rights share
  allocation among farmers. Extracted as **S540** (CASP). Three genuine
  excludes: Viljoen's South African water-law property-paradigm article
  is pure doctrinal commentary without empirical access evidence (E05);
  Mamokhere et al.'s municipal service-partnerships paper is a
  self-described non-empirical conceptual/secondary-literature synthesis
  and not water-specific (E07); Shadabi & Ward's predictors-of-safe-
  drinking-water-access study is a rigorous macro cross-national
  regression on national governance-quality indices (GDP, Gini,
  corruption, government effectiveness, civil liberties) — the wrong
  unit of analysis for this review's household/applicant-level scope,
  the same rationale as the earlier Nkiaka exclusion (E01).
  `evidence_map.csv` updated; `full_text_retrieval_queue.csv`
  regenerated; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-seventh full-text screening batch — 1
  Drive-retrieved PDF, exclude.** Nithammer, Mahabir & Dikgang (2022),
  *Applied Economics*, "Efficiency of South African water utilities: a
  double bootstrap DEA analysis," excluded E04. This is a rigorous
  double-bootstrap data envelopment analysis (DEA) benchmarking the
  technical/operational efficiency of 144 South African water utilities
  (2010-2014 panel), with institutional determinants (WSA status,
  water-board use, outsourcing, political competition). However, the
  outcome measured is a DEA efficiency/inefficiency score -- utility-level
  input-output productivity (operating cost, length of mains vs.
  authorized consumption, water quality) -- not any household/applicant
  access, connection, affordability, or reliability outcome within this
  review's scope. `full_text_retrieval_queue.csv` regenerated; duplicate
  audit and schema validation re-run clean. Full detail in
  `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-eighth full-text screening batch — 1
  Drive-retrieved PDF, new include (S541).** Singh & Pandey (2020),
  *Water Policy*, "Urban water resilience in Hindu Kush Himalaya: issues,
  challenges and way forward," is a genuine include: a narrative policy
  synthesis across 8 named cities in Afghanistan, Pakistan, India, Nepal,
  China and Bhutan, combining a quantitative supply-demand data table
  with author field observations from the HI-AWARE research consortium.
  Documents real legal-administrative access mechanisms -- groundwater
  abstraction bye-laws that exist in multiple towns (Quetta, Kabul,
  Dehradun, Haldwani) but are seldom enforced, partly due to the
  political influence of informal water-tanker operators; absence of
  metering and differential pricing; institutional fragmentation across
  water-supply departments operating in silos; and inequitable "zero
  day" water cutoffs disproportionately affecting socio-economically
  weaker areas, with unaffordable tanker-water pricing (e.g. $0.36/unit
  in Kabul) as the de facto supply mechanism where formal municipal
  supply is deficient. Extracted as **S541** using the Legal
  Institutional Evidence Appraisal Framework, since the paper is not a
  systematic review (no described search protocol). `evidence_map.csv`
  updated; `full_text_retrieval_queue.csv` regenerated; duplicate audit
  and schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): sixty-ninth full-text screening batch — 2
  Drive-retrieved PDFs, both new includes (S542-S543).** Singh, Hassan,
  Hassan & Bharti (2020), *Water Policy*, "Urbanisation and water
  insecurity in the Hindu Kush Himalaya: Insights from Bangladesh, India,
  Nepal and Pakistan," is a companion paper to S541 in the same special
  issue, covering a different 4-country subset with its own supply-demand
  data table (13 cities) and distinct legal-administrative content:
  departmental jurisdictional mandate limitations blocking spring/recharge
  protection in Darjeeling, multi-party institutional coordination
  failures that delayed and inflated the cost of a water-augmentation
  project (INR 400M to 560M), and tanker-pricing burdens restricting
  water quantity purchased by poorer households. Extracted as **S542**
  using the Legal Institutional Evidence Appraisal Framework. Twum &
  Abubakari (2020), *Water Policy*, "Drops in the city: the puzzle of
  water privatization and consumption deficiencies in urban Ghana," is a
  mixed-methods study (26 semi-structured interviews across Accra,
  Kumasi, Sekondi-Takoradi and Tamale, plus secondary data and GIS
  mapping) documenting a genuine legal-administrative access mechanism:
  informal-settlement residents lack the legal documentation required
  for formal household pipe connections, categorically barring them from
  formal service and forcing reliance on private vendors at markedly
  higher prices ($0.10/bucket, $0.18/gallon tanker, $10-20 for untreated
  well water) in a weak/unregulated private-vendor market. Extracted as
  **S543** (MMAT). `evidence_map.csv` updated for both;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and
  schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventieth full-text screening batch — 1
  Drive-retrieved PDF, new include (S544).** Turley & Caretta (2020),
  *Water*, "Household Water Security: An Analysis of Water Affect in the
  Context of Hydraulic Fracturing in West Virginia, Appalachia," is a
  strong include: 30 in-depth semi-structured interviews with mineral
  owners, surface owners, and concerned citizens across 8 northwestern
  West Virginia counties, documenting a genuine legal-administrative
  regime around household groundwater security. WV code 22-6A-18's
  "presumed liability" statute conditions legal protection for
  well-water contamination on a 1500-foot distance and 6-month time
  threshold, both set by government/industry compromise rather than
  public-health science; the mandated baseline and post-drill water
  testing is conducted by contractors hired by the oil and gas companies
  themselves, producing delayed and contested results -- one resident
  learned via a FOIA request, after months of unknowingly drinking
  E. coli-contaminated water, that a positive test had been withheld;
  oil and gas wastewater is exempt from the federal Safe Drinking Water
  Act ("the Halliburton Loophole"); and a Natural Resources Defense
  Council report found the WV Department of Environmental Protection
  failed to enforce Underground Injection Control requirements.
  Extracted as **S544** (CASP, qualitative). `evidence_map.csv` updated;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and
  schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-first full-text screening batch — 1
  Drive-retrieved PDF, new include (S545).** Dobbin (2020), *Society &
  Natural Resources*, "'Good Luck Fixing the Problem': Small Low-Income
  Community Participation in Collaborative Groundwater Governance and
  Implications for Drinking Water Source Protection," is a strong
  include: 27 semi-structured interviews with 35 individuals across 23
  small low-income San Joaquin Valley communities documenting a genuine
  legal-administrative participation regime under California's
  Sustainable Groundwater Management Act (SGMA). SGMA statutorily lists
  Disadvantaged Communities and domestic well owners among 11 mandatory
  beneficial-user categories in local Groundwater Sustainability
  Agencies (GSAs), but leaves the form of representation to GSA
  discretion; in this study, privately-owned water systems and
  domestic-well communities never achieved formal voting representation,
  formal voting seats typically required a financial contribution (one
  community saved $8,000 by choosing non-voting status), and
  transparency failures (non-Brown-Act-compliant meetings, one community
  notified three years after enactment) compounded exclusion. Drinking-
  water needs were largely absent from resulting Groundwater
  Sustainability Plans, and 25% of interviewees expected SGMA's net
  effect on their community to be negative. Extracted as **S545** (CASP,
  qualitative). `evidence_map.csv` updated; `full_text_retrieval_queue.csv`
  regenerated; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-second full-text screening batch — 3
  Drive-retrieved PDFs, 1 exclude and 2 new includes (S546-S547).** Morena
  et al. (2019), *MATEC Web of Conferences*, "The analysis of health
  aspects in housing type 45, Panorama Indah residence, Pekanbaru," is a
  single-house (N=1) building-code compliance survey against Indonesia's
  1986 housing-health standard -- water supply is one of six inspected
  physical criteria, and no legal-administrative access mechanism or
  population beyond a single dwelling is examined -- **excluded E06**
  (engineering only). Singh, Shrestha, Hamal & Prakash (2020), *Water
  Policy*, "Perform or wither: role of water users' associations in
  municipalities of Nepal," is a strong include: a 350-household survey
  (208 Damauli, 142 Tansen) plus focus group discussions documenting
  Nepal's water-law framework (Water Resource Act 1992, Water Resource
  Regulation 1993, Drinking Water Regulation 1998) and concrete
  access/burden mechanisms -- NPR 50,000 (~USD 440) new-connection costs
  with waits up to 11 years, a two-tier informal-payment pathway (NPR
  100,000 for faster connection), WUA-committee/private-repair-agency
  collusion and political capture, gendered exclusion via male-only tap
  registration despite women bearing 6-7 hrs/day of water-collection
  burden, tanker-water costs (~Rs 357/1,000L), and inequitable WUA
  spring-water pricing (NPR 20 to 80 per 6,000L). Extracted as **S546**
  (MMAT). Sarrazin, Gautier, Hollé, Grancher, de Bélizal & Hadmoko (2019),
  *GeoJournal*, "Resilience of socio-ecological systems in volcano
  risk-prone areas, but how much longer? Assessment of adaptive water
  governance in Merapi volcano, Central Java, Indonesia," is a strong
  include: 73 stakeholder interviews (42 household-level) across 7
  villages/dusun documenting Indonesia's irrigation-reform and
  decentralization framework, the "Turnover Program" transferring
  irrigation governance from customary Ulu-Ulu rights-holders to formal
  Water Users Associations, institutional pluralism across multiple
  government agencies producing an undelivered 2013 WUA subvention
  payment, and post-2010-eruption lahar damage causing drinking- and
  irrigation-water crises met by unequal government emergency-water-tank
  distribution and informal Gotong Royong mutual-aid canal repair.
  Extracted as **S547** (MMAT). `evidence_map.csv` updated for both;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and
  schema validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-third full-text screening batch — 4
  Drive-retrieved PDFs, 2 excludes and 2 new includes (S548-S549).**
  Nyamwanza (2018), *International Journal of Climate Change Strategies
  and Management*, "Local institutional adaptation for sustainable water
  management... A case in the mid-Zambezi Valley, Zimbabwe," is a strong
  include: a qualitative case study (34 semi-structured interviews, 3
  community workshops, key informant interviews) documenting that
  Zimbabwe's statutorily mandated Catchment/Sub-Catchment Councils and
  ZINWA are functionally absent in rural Mbire District (over 90% of
  residents had no knowledge of them), leaving the Rural District Council,
  Environmental Management Agency, traditional authorities, and community
  Borehole Water Committees as the institutions actually governing access
  -- including a contested streambank-cultivation by-law later modified
  through local negotiation, and chronic borehole shortage (up to 2,000
  people per functioning borehole against a 250-person government
  recommendation). Extracted as **S548** (CASP, qualitative). Bartels,
  Bruns & Alba (2018), *Local Environment*, "The production of uneven
  access to land and water in peri-urban spaces: de facto privatisation in
  greater Accra," is a strong include: a mixed-methods study (62 household
  interviews, transect walks, photo diaries) documenting unlicensed de
  facto private control of groundwater bypassing Ghana's Water Resources
  Commission Act 1996 permit requirement, private-vendor water pricing
  3-20x the official GWCL rate, customary land tenure exploited via a
  20-year chieftaincy dispute enabling multiple sale of the same land
  plots, and an extra-legal "digging fee" required before construction.
  Extracted as **S549** (MMAT). Post, Agnihotri & Hyun (2018), *Studies in
  Comparative International Development*, "Using Crowd-Sourced Data to
  Study Public Services: Lessons from Urban India," is a research-methods
  paper (water-intermittency data from Bangalore illustrates a broader
  toolkit for political-science crowd-sourced-data research) --
  **excluded E01** (wrong topic), since its actual contribution is
  methodological rather than a primary empirical study of
  legal-administrative water access. Silva Rodríguez de San Miguel (2018),
  *Management of Environmental Quality*, "Gender and water management in
  Mexico," self-labeled "Paper type: General review," is a narrative
  literature survey with no original empirical data collection of its own
  -- **excluded E05** (no empirical evidence). `evidence_map.csv` updated
  for both includes; `full_text_retrieval_queue.csv` regenerated;
  duplicate audit and schema validation re-run clean. Full detail in
  `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-fourth full-text screening batch — 2
  Drive-retrieved PDFs, 1 exclude and 1 new include (S550).** Nastar,
  Abbas, Aponte Rivero, Jenkins & Kooy (2018), *African Studies*, "The
  emancipatory promise of participatory water governance for the urban
  poor... Dodowa, Ghana and Arusha, Tanzania," is a strong include: a
  mixed-methods comparative case study (104 household interviews in
  Dodowa, 56 household interviews plus 120 water-point interviews in
  Arusha) documenting Ghana's Community Water and Sanitation Agency Act/
  WATSAN committee structure and GWCL connection process (with tank-resold
  water priced roughly 10x the regulated tariff), and Tanzania's Water
  Resource Management Act framework for groundwater regulation undermined
  by an unfunded Pangani Basin Water Board and by Arusha City Council land
  permits issued illegally in groundwater recharge areas -- alongside
  tenure-, kinship-, and land-ownership-based exclusion from community
  water governance in both cities. Extracted as **S550** (MMAT). Nohong
  (2018), *International Journal of Law and Management*, "The moderating
  effect of efficiency and non-market capability... performance of water
  supply companies (PDAM) in Sulawesi, Indonesia," is a PLS-SEM survey
  study of company-level performance -- **excluded E04** (wrong outcome),
  the same technical/organizational-efficiency rationale applied to the
  earlier DEA exclusion. `evidence_map.csv` updated for S550;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and schema
  validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-fifth full-text screening batch — 5
  Drive-retrieved PDFs, 2 excludes and 3 new includes (S551-S553).** Harris,
  Kooy, Rusca et al. (2017), "Gendered lives, gendered waters," is a strong
  include: a mixed-methods statistical study (487-household survey across
  Ashaiman/Teshie in Accra, Ghana and Khayelitsha/Philippi in Cape Town,
  South Africa) documenting Ghana's GWCL urban piped-supply mandate and the
  AVRL private-consortium management period (2006-2011), and South
  Africa's Constitutional right to water and sanitation, the Free Basic
  Water policy (6kl/household/month regardless of household size), and
  apartheid-era infrastructure siting still shaping access via the ongoing
  RDP housing-formalization process. Extracted as **S551** (JBI Analytical
  Cross Sectional Studies). Romano (2017), on Nicaragua's community-based
  water committees (CAPS), is a qualitative case study (18 committee
  interviews plus NGO/multilateral/government staff interviews, 2007-2010
  fieldwork plus a 2014 follow-up) documenting the Special Law of Potable
  Water and Sanitation Committees (Law 722, 2010) that formally recognized
  over 5,000 previously unrecognized CAPS serving more than 1 million rural
  residents, superseding the exclusionary General Water Law (Law 620,
  2007); CAPS' lack of personeria juridica preventing legal receipt of
  constructed water systems; informally negotiated non-enforcement of
  shutoff rules for seasonal-labor households; and legal-gray-area land/
  water-source access negotiation with private landowners. Extracted as
  **S552** (CASP, qualitative). Forster, Downsborough & Chomba (2017), on
  Water User Association establishment in South Africa's Groot Marico
  catchment, is a qualitative case study (48 interviews, fieldwork 2011 and
  2015) documenting the National Water Act 1998's WUA-establishment
  guidelines and its "existing lawful use" provision continuing to
  advantage the white minority of commercial irrigation farmers, and a
  documented WUA-establishment meeting from which Black rural community
  members and emerging farmers were functionally excluded via short
  notice, an inaccessible venue, and English-only proceedings. Extracted as
  **S553** (CASP, qualitative). A "Defining Moments" reflective essay
  (*Health Communication* journal) about water access in southeastern Ohio
  -- built around unstructured focus-group anecdotes with no described
  sample size, sampling method, or systematic coding protocol, analyzed
  through communication/narrative theory rather than legal-institutional
  mechanism analysis -- was **excluded E12** (wrong study design). A
  multiple-regression study of technical/financial/social/institutional
  factors influencing faecal sludge management service performance across
  160 Thai municipalities was **excluded E04** (wrong outcome): a
  municipality-level service-performance metric, not a household- or
  applicant-level access outcome, the same institutional/organizational-
  performance rationale applied to the earlier DEA and PDAM exclusions.
  `evidence_map.csv` updated for S551-S553; `full_text_retrieval_queue.csv`
  regenerated; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-sixth full-text screening batch — 6
  Drive-retrieved PDFs, 3 excludes and 3 new includes (S554-S556).** Cole &
  Browne (2015), "Tourism and Water Inequity in Bali," is a strong include:
  a mixed-methods case study (39 interviews, 2 focus groups, 110 tourist
  surveys) using Ostrom's SES framework to document 11 fragmented, poorly
  coordinated Balinese government departments sharing water responsibility,
  the subak irrigation-governance system, and widespread non-enforcement of
  water-metering/tariff regulations against the tourism industry, leaving
  local households on multi-year waitlists for connections and paying
  unlicensed vendors up to Rp50,000/gallon. Extracted as **S554** (MMAT).
  Palta, du Bray, Stotts, Wolf & Wutich (2016), on ecosystem services and
  disservices for people experiencing homelessness in Phoenix, Arizona, is
  a mixed-methods ethnographic study (155 site visits, 17 interviews,
  water-quality monitoring at 5 sites) documenting Phoenix's 2004
  anti-camping ordinances criminalizing public water access, locked public
  facilities at night, and the illegality of accessing state/federal
  wetlands used as an extra-legal water-access strategy by this excluded
  population -- alongside a serious documented health-risk trade-off (E.
  coli exceeding EPA drinking standards in up to 100% of monsoon-season
  measurements). Extracted as **S555** (MMAT). Ghertner (2017), "When Is
  the State?", is a strong include: a qualitative ethnographic case study
  (24 months of fieldwork, 2006-2014) of everyday negotiation of water,
  electricity, and building-permission access in Delhi's informal slum
  settlements and unauthorized colonies, documenting illegal utility
  reconnection via direct bureaucratic negotiation, unauthorized colonies
  categorically barred from formal water connections despite valid
  property documentation, Jal Board officials operating unregistered
  borewells in violation of a state drilling ban (financed via an MLA's
  discretionary fund), and Resident Welfare Associations as informal
  intermediaries controlling water-delivery and construction-approval
  access. Extracted as **S556** (CASP, qualitative). A doctrinal
  legal-theoretical analysis of Australian Indigenous water rights
  (Burdon, Drew, Stubbs, Webster & Barber, *Settler Colonial Studies*
  2015), drawing only on existing scholarship and case law with no
  original empirical data collection, was **excluded E05** (no empirical
  evidence). A discrete-choice-experiment survey-methodology paper on
  status-quo bias in English water-utility price regulation (Lanz &
  Provins, *Journal of Regulatory Economics* 2015) was **excluded E01**
  (wrong topic): its actual contribution is survey-methodology validity,
  not a primary empirical study of legal-administrative water access. A
  theoretical incomplete-contracts economic model of PPP water-utility
  contract design in Senegal and Burkina Faso (Nakhla, *European Journal
  of Law and Economics* 2016), illustrated with secondary published
  utility-performance statistics, was **excluded E04** (wrong outcome):
  network yield, connection counts, and staff productivity are
  utility-level performance metrics, not a household-level access
  outcome, the same rationale applied to the earlier DEA, PDAM, and Thai
  FSM exclusions. `evidence_map.csv` updated for S554-S556;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and schema
  validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-seventh full-text screening batch —
  2 Drive-retrieved PDFs, 2 new includes (S557-S558).** Kim (2014), on
  gendered exclusion from a participatory Water User Association project
  in rural Uzbekistan, is a strong include: a qualitative institutional
  ethnographic case study (40 in-depth interviews with women peasant
  farmers plus 65 additional stakeholder interviews, participant
  observation, and ~400-document institutional text analysis) documenting
  the Uzbek government's WUA institutionalization, 1994 household
  peasant-farm land-rights formalization, state lease-contract cotton/wheat
  quotas, and "community mobiliser" selection criteria that discursively
  excluded women -- the majority of household farmers -- despite their
  extensive unrecognized water-access labor. Extracted as **S557** (CASP,
  qualitative). Selfa, Bain & Moreno (2014), on Bonsucro biofuel
  certification in the Valle del Cauca, Colombia, is a strong include: a
  qualitative case study (14 in-depth interviews with sugarcane/ethanol
  industry stakeholders plus additional interviews with displaced rural
  residents), documenting Colombia's water-concession regulatory regime
  administered by a regulator interviewees describe as captured by the
  sugar industry (which holds 64%/88% of surface/underground water
  concessions versus 26%/2% for household use), industry lobbying to
  reclassify potable groundwater as non-potable to free it for irrigation,
  and Bonsucro's "obey the law" certification standard legitimizing this
  disproportionate access without addressing underlying inequitable
  distribution. Extracted as **S558** (CASP, qualitative).
  `evidence_map.csv` updated for S557-S558; `full_text_retrieval_queue.csv`
  regenerated; duplicate audit and schema validation re-run clean. Full
  detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-eighth full-text screening batch —
  5 Drive-retrieved PDFs, 2 excludes, 2 new includes (S559-S560), 1
  wrong-file-retrieved left open.** Two studies were excluded, both E01
  (wrong topic): a study of small NGOs' access to geological/
  hydrogeological data for water-point siting in eastern Africa (Wagaba et
  al.), a different unit of analysis and concept of "access"
  (practitioner/NGO access to technical data, not household-level
  legal-administrative access); and a policy/hydrological-geography
  analysis of South Africa's 1998 National Water Act "Reserve"
  environmental-flow mechanism (Blanchon), drawn from government reports
  and secondary sources with no original household-level empirical data
  collection. The fifth PDF (R81549C4709FC) was a **fourth consecutive
  wrong-file delivery**: the target record is Singh & Singh (2024),
  "Building Political Capabilities through Participation for
  Environmental Justice in Informal Housing in Kathmandu," but the file
  delivered was again two book chapters on climate-change adaptation and
  Indigenous Environmental Justice in Nepal (Sherpa; Awale) from a
  different part of the same edited volume. A first pass this session
  mistakenly recorded this record as excluded E01 based on the
  wrongly-delivered content, without checking the record's prior
  `wrong_file_retrieved` history first; this was caught and reverted the
  same session (decision fields cleared, the erroneous exclusion_log row
  removed, and `notes` updated) — the record remains open pending correct
  retrieval, per `CHANGELOG.md`. Boucher-Hedenström &
  Rutherford (2010), on municipal water/sanitation service configuration
  amid urban sprawl in Stockholm County, Sweden, is a strong include: a
  qualitative case study (interviews with named municipal/regional
  officials) documenting Sweden's 2007 Water Services Act municipal
  responsibility and cost-price tariff principle, a four-type service-
  configuration typology (A-D), an estimated ~90,000 households on
  alternative (non-municipal) solutions, and a mini-network
  (samfällighet) model requiring unanimous neighbor consent to connect.
  Extracted as **S559** (CASP, qualitative). Baron & Bonnassieux (2013),
  on hybrid water governance and Water Users' Associations (AUE) in
  rural/semi-urban Burkina Faso, is a strong include: a qualitative case
  study (field studies conducted 2011-2014 under the ANR Sud II APPI
  research project) documenting the 2001 Water Law right to water, the
  2009 decentralization decree transferring infrastructure competence to
  communes, AUE legal homologation criteria (30-80 members, gender
  parity, youth quotas, elected 6-member bureau), AUE's formal tariff-
  setting and conflict-mediation authority, AEPS delegation via affermage
  contracts, and documented gendered exclusion from AUE leadership
  despite formal parity requirements. Extracted as **S560** (CASP,
  qualitative). `evidence_map.csv` updated for S559-S560;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and schema
  validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): seventy-ninth full-text screening batch —
  7 Drive-retrieved PDFs, 1 exclude, 4 new includes (S561-S564), 2
  wrong-file-retrieved left open.** Dwipayanti et al. (2022), on
  Inclusive WASH in the tourism destination of Labuan Bajo, Indonesia, is
  a strong include: a qualitative case study (20 interviews, 6 focus
  groups) documenting the municipal utility PDAM's intermittent supply
  amid a 10 L/s deficit, Indonesia's minimum water-requirement service
  standard, a tiered hotel/household tariff with documented preferential-
  delivery effects, and the POKJA AMPL governance working group.
  Extracted as **S561** (CASP, qualitative). Akpabio & Ozoh (2026), on
  household WaSH access in Cross River State, Nigeria, is a strong
  include: a mixed-methods 800-household cross-sectional survey (751
  retrieved, 93.9% response rate) documenting the State's new 2025 Water
  Supply and Sanitation Law, a newly inaugurated WaSH regulatory
  department, and the 2025 WaSH Policy's financing/accountability-
  dashboard mechanisms. Extracted as **S562** (MMAT, mixed methods).
  Nkolola & Phiri (2024), on gender dynamics in Water Point Committee
  governance in rural Mbala, Zambia, is a strong include: a mixed-methods
  study (122 mWater-tool interviews, Empowerment in WASH Index survey)
  documenting WPC membership eligibility criteria and election cycles,
  with an EWI-quantified finding that lack of enforced financial
  contribution -- not gendered exclusion -- is the primary barrier to
  water-point sustainability. Extracted as **S563** (MMAT, mixed
  methods). Mandara, Butijn & Niehof (2013), on community management of
  rural water facilities in Kondoa and Mpwapwa districts, Tanzania, is a
  strong include: a mixed-methods study (221-household survey, 6 FGDs, 2
  village case studies) documenting Tanzania's 2002 NAWAPO and 2008
  NWSDS national water-policy frameworks, subsidiarity-principle
  cost-recovery devolution, District Water Department staffing deficits
  (41-50% below required), and Village Water Committee gender-parity
  requirements. Extracted as **S564** (MMAT, mixed methods). Schiedek et
  al. (2021), a deductive content analysis of 291 Sanitation and Water
  for All partnership commitment texts submitted to a global online
  database, was **excluded E01** (wrong topic): the unit of analysis is
  international-partnership commitment-text quality, not a primary
  empirical study of household-level legal-administrative water access,
  the same macro/cross-national rationale as the earlier Nkiaka, Shadabi
  & Ward, and Laitinen exclusions. Two further PDFs were confirmed as
  wrong-file deliveries and left open: RDA537B7BBB17 (target: "Fecal
  sludge management (FSM): Analytical tools for assessing FSM in
  cities"; delivered: Agbo, Jeffrey & Sule 2025, a Sub-Saharan Africa WSS
  systematic review) and R22849E39FE23 (target: "Community engagement
  and capacity building... Malawi"; delivered: Suleiman 2011, an Accra
  water-utility-privatisation governance case study) -- both records'
  `full_text_status` updated to `wrong_file_retrieved` with notes
  documenting the mismatch. `evidence_map.csv` updated for S561-S564;
  `full_text_retrieval_queue.csv` regenerated; duplicate audit and schema
  validation re-run clean. Full detail in `CHANGELOG.md`.
- **2026-09-21 (later still): eightieth full-text screening batch —
  10 Drive-retrieved PDFs, 4 excludes, 6 new includes (S565-S570), all
  title/content-verified against target records, no wrong-file
  deliveries.** Six strong includes: Mbiza et al. (2026), a mixed-methods
  150-household study developing the Greywater Service Innovation Ladder
  governance-maturity framework for decentralised greywater services in
  Southlea Park, Harare, Zimbabwe, documenting Zimbabwe's greywater
  policy vacuum, RDC/ward-committee gate-decision authority, and the
  Equity Safeguard Ratio affordability mechanism (S565, MMAT). Abawari et
  al. (2026), a qualitative photovoice study of school WASH governance
  gaps in two Ethiopian primary schools (20 core participants, 75-
  participant advocacy event), documenting weak inter-agency
  accountability and the advocacy event's bureaucratic-gap-bridging role
  (S566, CASP). Gashaw et al. (2025), a mixed-methods 400-household
  survey of rural water-scheme functionality/sustainability governance in
  Gursum District, Ethiopia, documenting WASHCO tariff authority and
  government-dominated technology selection despite nominal community
  ownership (S567, MMAT). Azupogo, Dassah & Bisung (2023), a
  participatory concept-mapping study (22 stakeholders) of inclusive
  school WASH strategies for students with physical disabilities in
  Ghana, documenting the CRPD normative baseline and an unimplemented
  Inclusive Education Policy (S568, MMAT). Karim et al. (2024), a
  mixed-methods 150-household study applying SFD/CSDA/SWOT analysis to
  citywide sanitation governance in Noakhali Pourashava, Bangladesh,
  documenting Bangladesh's national sanitation strategy's silence on
  fecal sludge management and CSDA-scored institutional gaps (S569,
  MMAT). Coultas et al. (2022), a qualitative multi-case study (31
  combined key-informant interviews) of sub-national government
  sanitation-leadership mechanisms across Kenya, Rwanda, and Uganda,
  documenting each country's decentralisation architecture, a governor's
  signed financial-commitment letter, and mandatory livelihood-benefit/
  toilet-use conditionality (S570, CASP). Four excludes: R65E0D0F26A0A
  (Celume, Donoso et al., a 63-study PRISMA-style systematic review plus
  comparative legal-text analysis of Chile's 2022 Water Code reform) —
  **excluded E05**, extending the Viljoen/Burdon doctrinal-commentary
  precedent to systematic reviews of secondary legal literature.
  R73C7494E55DD (Gidion, a network-DEA efficiency-benchmarking study of
  40 Tanzanian urban water utilities) — **excluded E04**, utility-level
  performance ranking, matching the established DEA-exclusion precedent.
  R96593F742647 (Satpathy & Jha, Indian intermittent-water-supply
  social-relations analysis) — **excluded E05**, the authors' own stated
  reliance on literature review with no original household-level data
  collection. R3BF9C93DC6A9 (Saadi & Johns, "Governing smart water
  cities," a Canadian policy framework) — **excluded E05**, explicitly
  self-described as a policy-oriented scoping review of 51 secondary
  sources with no original empirical data collection. `evidence_map.csv`
  updated for S565-S570; `exclusion_log.csv` updated (569 rows total);
  `full_text_retrieval_queue.csv` regenerated (2,522 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,137/3,659 screened (568 include/569 exclude), 2,522 open, 568
  extracted studies, 27 effect_sizes rows (unchanged). Full detail in
  `CHANGELOG.md`.
- **2026-09-22: eighty-first full-text screening batch — 15
  Drive-retrieved PDFs, 10 excludes, 5 new includes (S571-S575). Three
  already-decided duplicates from the same inbox check (RD864629E91F7,
  R0482B6E724C6, R2C5270DE77D8) were moved to Processed without
  re-screening; one record (R22849E39FE23) carried prior
  `wrong_file_retrieved` history and was re-verified, confirmed matching
  this time.** Five includes: a Mvila Division, Cameroon rural
  water-security study (647 water-point WSSI assessments + 103 committee
  interviews) documenting Cameroon's General Code of Decentralized
  Territorial Collectivities (Law No. 2019/024) and a proposed
  intermunicipal syndicate legal structure (S571, MMAT). Foggitt, Cawood,
  Evans & Acheampong (2019), a mixed-methods study (152 house-unit toilet
  mapping, natural group discussions, 2 focus groups) of shared-sanitation
  exclusion in Kumasi, Ghana, documenting a landlord-permission exclusion
  mechanism (49% non-permittance, 84% attributed to landlord-exclusive
  use) and the legal abolition of bucket latrines (S572, MMAT). Shields et
  al. (2021), a qualitative study (243 interviews + 39 FGDs across 18
  communities in Ghana, Kenya, and Zambia) of community participation in
  rural water governance, documenting tariff-setting decision-making and
  transparency/accountability rights (S573, CASP). Chimphero, Tembo &
  Gadama (2026), a mixed-methods study (299 respondents, 8 FGDs, 12 KIIs)
  of Water Point Committee governance in Nkhata Bay District, Malawi,
  documenting traditional-authority by-law enforcement and informal
  contribution-based exclusionary access rules with recommendations to
  codify inter-village access rights (S574, MMAT). Bazaanah, Buthelezi &
  Oppong (2024), a qualitative study (98 participants) of household WASH
  access in Ghana and South Africa, documenting corruption/favouritism
  against named statutory frameworks (South Africa's Water Services Act,
  Free Basic Water policy; Ghana's CWSA Act) and a public-private-
  partnership water-treatment model (S575, CASP). Ten excludes:
  R7BC30D37A001 (India/Nepal water-quality book chapter) — **excluded
  E05**, pure literature-review/synthesis with no original data
  collection. R2DDCC2FC03E7 (Nigeria OECD water-governance-principles
  study) — **excluded E01**, macro/basin-level analysis, same
  Nkiaka/Laitinen rationale. RF16C02EE1F2F (South African Free Basic Water
  constitutional-law paper) — **excluded E05**, explicitly self-described
  doctrinal legal research methodology, no human participants. RC28E7E20373D
  (Zimbabwe community-health-club Group Maturity Index study) — **excluded
  E01**, hygiene-promotion organizational-monitoring tool, not a water/
  sanitation access mechanism. R178AF8716D6A (Delhi urban water system
  hydrological study) — **excluded E06**, IDW spatial interpolation on
  secondary GIS data, no household-level collection. RDC76C62702D0 (Pierce
  & Lai 2019, California retail-water-stores regression study) —
  **excluded E01**, models market-substitution behavior, not a
  legal-administrative access mechanism. RD5DE21EB6425 (Hlongwa, Nkomo &
  Desai, Sub-Saharan Africa WASH-barriers mini-review) — **excluded E05**,
  explicit PRISMA-style systematic review of 76 secondary sources.
  R7E702A70F8C6 (Kimbugwe et al. 2022, WaterAid SusWASH programmatic
  process review) — **excluded E01**, stakeholder-perception surveys of
  institutional building blocks, not household-level access. R3B73F903D49F
  (Chatterley et al. 2018, institutional WASH-in-the-SDGs monitoring-data
  review) — **excluded E01**, explicitly non-household settings (schools,
  health facilities). R345D7E2BCAC6 (Schiel, Wilson, Langford & Faulkner
  2023, cross-national democracy/water-access regression study, 140
  states) — **excluded E01**, macro governance-index study using aggregate
  datasets, no household-level access examination. `evidence_map.csv`
  updated for S571-S575; `exclusion_log.csv` updated (579 rows total);
  `full_text_retrieval_queue.csv` regenerated (2,507 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,152/3,659 screened (573 include/579 exclude), 2,507 open, 573
  extracted studies, 27 effect_sizes rows (unchanged). Full detail in
  `CHANGELOG.md`.
- **2026-09-22: eighty-second full-text screening batch — 6
  Drive-retrieved PDFs, 2 excludes, 4 new includes (S576-S579).** All six
  were open with no prior `wrong_file_retrieved` history and no
  duplicates to defer. Four includes: Mallory, Omoga, Kiogora, Riungu,
  Kagendi & Parker (2021), a qualitative study (53 interviews) of
  informal pit emptiers in Mukuru and Kibera informal settlements,
  Nairobi, Kenya, documenting Kenya's Water Act 2016 devolving sanitation
  to counties, the absence of legal recognition/licencing for pit
  emptiers, cartel violence/NEMA enforcement threats, and Sanergy's
  private transfer-station formalisation model (S576, CASP). de Menezes
  Fraga & de Maria Albuquerque Alves (2025), a quantitative study
  (tariff/consumption microdata across 35 Federal District, Brazil,
  service areas plus a binary logistic regression) of water-tariff
  subsidy regressivity, documenting demographic predictors of
  water-poverty risk (female household head OR=2.78; brown race
  OR=2.84; children OR=1.49) against Brazil's 2020 New Legal Framework
  for Basic Sanitation, Law 14,026/2020 (S577, JBI observational).
  Maiello, de Paiva Britto & Quintslr (2021), a mixed-methods case study
  (90-respondent survey + 9 interviews) of hybrid formal/informal water
  supply in Queimados, Rio de Janeiro Metropolitan Region, Brazil,
  documenting CEDAE's 30-year concession contract and clientelist-politics
  dynamics in infrastructure siting (S578, MMAT). Fallon Grasham &
  Neville (2021), a mixed-methods comparative case study (household
  surveys n=95/96; interviews n=90+90+19) of urban water insecurity
  across three Ethiopian cities, documenting Ethiopia's WASH
  Implementation Framework, a nationally illegal informal water-vending
  sector, a formal Addis Ababa rationing policy, and the 2013 National
  Guideline for Urban Water Utilities Tariff Setting, with quantified
  financial-burden ratios (informal water up to 20x, bottled water up to
  76x the formal tariff) (S579, MMAT). Two excludes: R4BFAEC61E31D (Armah
  & Rodrigues 2026, output-oriented DEA study of 23 Ghanaian water
  utilities) — **excluded E04**, utility-level technical/scale-efficiency
  outcome, same DEA/PDAM/Thai-FSM/Tanzanian rationale. R90EB686B9582
  (Porse et al. 2022, GIS/parcel-level stormwater-utility-fee
  affordability simulation methodology, Sacramento County, California) —
  **excluded E01**, a generalizable fee-affordability-modeling
  methodology, not a primary empirical study of a legal-administrative
  access mechanism, same Post/Agnihotri/Hyun and Lanz/Provins rationale.
  `evidence_map.csv` updated for S576-S579; `exclusion_log.csv` updated
  (581 rows total); `full_text_retrieval_queue.csv` regenerated (2,501
  open records); duplicate audit and schema validation re-run clean.
  Running totals: 1,158/3,659 screened (577 include/581 exclude), 2,501
  open, 577 extracted studies, 27 effect_sizes rows (unchanged — S577's
  logistic-regression odds ratios are demographic predictors of
  water-poverty risk, not a legal-institutional exposure-vs-comparator
  effect). Full detail in `CHANGELOG.md`.
- **2026-09-22: eighty-third full-text screening batch — 9
  Drive-retrieved PDFs, 7 excludes, 2 new includes (S580-S581).** All nine
  were open with no prior `wrong_file_retrieved` history and no
  duplicates to defer. Two includes: Craps, Dewulf, Mancero, Santos &
  Bouwen (2004), a qualitative case study of an indigenous-community/
  professional negotiation process over water/resource governance in the
  Chambo river subbasin, Ecuador, documenting indigenous communities'
  legal land titles, a judicial workshop, and formation of a new
  interinstitutional legal consortium (S580, Legal Institutional Evidence
  Appraisal Framework). Hess, Wold, Hunter, Nay, Worland, Gilligan &
  Hornberger (2016), a mixed-methods 22-MSA study of the American
  Southwest combining qualitative institutional-logics conflict coding of
  water-supply-policy disputes (development, preservation, environmental,
  consumer logics — e.g. Choctaw/Chickasaw Nations litigation over Sardis
  Lake, San Antonio's Vista Ridge ratepayer opposition) with a
  quantitative decision-tree/random-forest model identifying a city's
  Partisan Voting Index as the dominant predictor of municipal
  water-conservation-policy adoption (S581, JBI observational; not added
  to `effect_sizes.csv` — the variable-importance analysis is not a
  coefficient-plus-standard-error effect estimate). Seven excludes:
  RF7AFEEC69292 (Suleiman 2011, civil-society development-discourse
  study) — **excluded E01**, governance-process/participation study at a
  macro/institutional unit of analysis. RCBAA22BF401E (Murdocca 2010,
  Kashechewan water-crisis race/legal-violence analysis) — **excluded
  E05**, documentary/case-study analysis of secondary sources, no
  original empirical data collection. RADD32264AC64 (Jaffee & Newman
  2013, bottled-water commodification study) — **excluded E01**,
  corporate resource-extraction contestation, not household-level
  access. R7863774753EC (Abu, Elliott & Karanja 2021, Kenyan
  healthcare-facility WASH) — **excluded E01**, institutional (non-
  household) unit of analysis. RE41EC0C4C23A (Krishna et al. 2024,
  workplace menstrual-health pilot study) — **excluded E01**,
  workplace-based, not household access. R720E1DE4E7C8 (Rehman 2022,
  "Epidemic Infrastructures... Lahore") — **excluded E01**, dengue
  epidemiology/public-health-surveillance study; the reported outcome is
  epidemiological, not water access. R49DDEAB1849F (Yusuf, Murray &
  Okereke 2022, WaterAid Nigeria LGA-INGO participatory partnership case
  study) — **excluded E01**, governance-process/participation study at
  institutional (LGA) level. `evidence_map.csv` updated for S580-S581;
  `exclusion_log.csv` updated (588 rows total); `full_text_retrieval_queue.csv`
  regenerated (2,492 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,167/3,659 screened (579 include/588
  exclude), 2,492 open, 579 extracted studies, 27 effect_sizes rows
  (unchanged). Full detail in `CHANGELOG.md`.
- **2026-09-22: eighty-fourth full-text screening batch — 1
  Drive-retrieved PDF, 1 new include (S582).** A recurring 10-minute
  Drive-inbox check was scheduled per researcher request; this PDF
  surfaced on the first such check. Open with no prior
  `wrong_file_retrieved` history, no duplicate to defer: Jambadu, Pilo' &
  Monstadt (2024), a qualitative comparative case study (48 interviews
  plus field observations, 2018-2020) of hybrid public/private
  maintenance-and-repair labor relations in water supply across Nima
  (informal settlement) and Dodowa (peri-urban), Accra, Ghana, documenting
  GWCL's PURC/WRC-regulated maintenance mandate, the legality/illegality
  distinction for private and illegal water connections and informal
  self-repair, and Ghana's decentralized CWSA/Water and Sanitation
  Management Team framework (S582, CASP qualitative). `evidence_map.csv`
  updated for S582; `full_text_retrieval_queue.csv` regenerated (2,491
  open records); duplicate audit and schema validation re-run clean.
  Running totals: 1,168/3,659 screened (580 include/588 exclude), 2,491
  open, 580 extracted studies, 27 effect_sizes rows (unchanged). Full
  detail in `CHANGELOG.md`.
- **2026-09-22: eighty-fifth full-text screening batch — 2
  Drive-retrieved PDFs, 2 excludes.** Both open with no prior
  `wrong_file_retrieved` history, no duplicates to defer: Hushie (2018), a
  qualitative study (24 interviews, 16 CSO-District Assembly
  collaborations) of state-civil-society partnership dynamics for W&S
  service delivery in the Northern region of Ghana — **excluded E01**,
  institutional-level governance-process/partnership-dynamics study, not
  a household-level access mechanism. Soublière & Cloutier (2015), a
  qualitative ethnographic study of power/control dynamics between
  Malawian District Councils and rural-water-supply development partners
  — **excluded E01**, the studied outcome is the level of
  local-government involvement in service delivery, an institutional
  governance-process outcome, same rationale as the Hushie exclusion.
  `exclusion_log.csv` updated (590 rows total); `full_text_retrieval_queue.csv`
  regenerated (2,489 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,170/3,659 screened (580 include/590
  exclude), 2,489 open, 580 extracted studies, 27 effect_sizes rows
  (unchanged). Full detail in `CHANGELOG.md`.
- **2026-09-22: eighty-sixth full-text screening batch — 2
  Drive-retrieved PDFs, 1 exclude, 1 new include (S583).** Both open with
  no prior `wrong_file_retrieved` history, no duplicates to defer:
  Hallström (2005), a historical case-comparative study using primary
  archival sources (City Council/Waterworks Board/Water Company minutes,
  contemporary newspaper accounts) of whether working-class suburbs of
  Norrköping and Linköping, Sweden received municipal piped-water
  connections, 1860-1890, documenting the "planned area"/rural-district
  administrative boundary determining building/fire/health-code
  applicability, discretionary municipal extension decisions, and the
  "10 percent rule" financing criterion (S583, Legal Institutional
  Evidence Appraisal Framework). Jiménez & Pérez-Foguet (2010), a
  GIS/water-point-mapping technical analysis of 5,921 rural water points
  across 15 Tanzanian districts — **excluded E06**, infrastructure/
  technical-methodology study of coverage-estimation methodology and
  technology functionality decay, no legal-administrative access
  mechanism examined. `evidence_map.csv` updated for S583;
  `exclusion_log.csv` updated (591 rows total); `full_text_retrieval_queue.csv`
  regenerated (2,487 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,172/3,659 screened (581 include/591
  exclude), 2,487 open, 581 extracted studies, 27 effect_sizes rows
  (unchanged). Full detail in `CHANGELOG.md`.
- **2026-09-22: eighty-seventh full-text screening batch — 14
  Drive-retrieved PDFs, 1 duplicate deferred, 8 excludes, 5 new includes
  (S584-S588).** One (Li/McManus/Cronk, Liberia water-point functionality)
  was a duplicate of an already-`include`-decided record — moved to
  Processed without re-screening, per the standing duplicate-defer rule.
  Of the remaining 13, all open with no prior `wrong_file_retrieved`
  history: Cortes et al. (2021), a comparative constitutional-law/
  case-law study of Brazil, Colombia, and Peru documenting Colombia's
  Constitutional Court tutela jurisprudence enforcing household
  reconnection for low-income petitioners and Peru's amparo action/2017
  constitutional amendment (S584, directly analogous to the S517 Morgan
  precedent); Granados-Munoz (2022), a Spanish-language ethnographic case
  study of Mexico's Acueducto II documenting broken PPP-financed
  restitution promises to the Maconi agrarian community (S585);
  Silva-Novoa Sanchez et al. (2019), an ethnographic study of a
  self-installed household pipe extension in Moamba, Mozambique that the
  utility tacitly tolerated while a neighborhood chief's contribution fee
  created a new exclusionary access rule (S586); Alba et al. (2019), an
  ethnographic study of Accra's tanker water-supply governance
  documenting the exclusive legal recognition of GWCL and the land-tenure
  barrier excluding Old Fadama informal-settlement residents from legal
  piped connections (S587); and Richmond et al. (2018), a mixed-methods
  study of Kampala's 57 informal settlements documenting how overlapping
  land tenure and connection-fee requirements determine legal
  piped-water eligibility (S588). Eight excludes: Lieberherr & Ingold
  (Swiss organizational-preference survey, **E04**); Germann &
  Langergraber (Austria SDG6 indicator-selection desk review, **E05**);
  a Kenya/Slovenia constitutionalization process study (**E01**);
  Wingfield et al. (Ecuador legal/policy desk review, **E05**); de Castro
  et al. (Brazil water-energy-sanitation systems-mapping methodological
  paper, **E01**); Machado et al. (Brazil rural-water-supply NGT
  expert-opinion survey, only n=7 community-level respondents, **E04**);
  Dhoba (Zimbabwe WASH sector institutional-coordination study, **E01**);
  and Poudel et al. (Nepal climate-resilient water-safety-plan technical
  resilience-scoring study, **E06**). `evidence_map.csv` updated for
  S584-S588; `exclusion_log.csv` updated (599 rows total);
  `full_text_retrieval_queue.csv` regenerated (2,474 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,185/3,659 screened (586 include/599 exclude), 2,474 open, 586
  extracted studies, 27 effect_sizes rows (unchanged). Full detail in
  `CHANGELOG.md`.
- **2026-09-22: eighty-eighth full-text screening batch — 3
  Drive-retrieved PDFs (the first delivered by an Antigravity retrieval
  session), 2 wrong-file deliveries flagged, 1 new include (S589).** Two
  of the three targets were caught as mismatches only by cross-checking
  the delivered PDF's actual author names against the `authors` field
  already on file, not by title alone: Leopold & McDonald's (2012)
  "Municipal Socialism Then and Now" arrived instead as an unrelated
  Jamie Peck (2009) book chapter on creative-cities urban policy (zero
  water/sanitation mentions in ~1,600 lines), and Sharma et al.'s (2014)
  Community Development Journal article arrived instead as an unrelated
  1-page UK-Aid field resilience-assessment summary for Kinna ward,
  Isiolo County. Neither was screened; both flagged
  `wrong_file_retrieved` and left open pending correct retrieval. The
  third, a World Bank/IDB (2004) Ecuador fiscal-management and
  public-expenditure review, was a genuine match — **included**: within
  a much larger multi-sector fiscal report, its water-subsection
  documents an original World-Bank-staff quantile subsidy-incidence
  estimate (poorest quintile receives 7.9% of water subsidies vs. 41.3%
  to the richest) and a household case (Machala, El Oro) showing
  connected households pay roughly 22-24x less per unit of water than
  unconnected households served by tankers (0.4% vs. 9.0% of monthly
  income), tied to decentralized, under-resourced municipal water
  governance. Extracted as S589; also added to `effect_sizes.csv`
  (Family A, descriptive/unadjusted, not eligible for pooling) — the
  first change to that table all session, 27 → 28 rows.
  `evidence_map.csv` updated for S589; `exclusion_log.csv` unchanged (no
  excludes); `full_text_retrieval_queue.csv` regenerated (2,473 open —
  the two wrong-file-flagged records remain open, not decided);
  duplicate audit and schema validation re-run clean. Running totals:
  1,186/3,659 screened (587 include/599 exclude), 2,473 open, 587
  extracted studies, 28 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: eighty-ninth full-text screening batch — 5
  Drive-retrieved PDFs, all delivered by an Antigravity retrieval session
  and all genuine matches (no wrong-file issues this time), 2 excludes, 3
  new includes (S590-S592).** Mundonde & Makoni (2024), a national-level
  Tobit econometric study of macro/financial/governance determinants of
  aggregate Zimbabwe water-sanitation PPP investment financing value —
  **excluded E04**, the outcome is investment dollars, not an access
  outcome. Tomalty & Skaburskis (1997), a qualitative case study of
  Ontario municipal development-charge calculation methodology across 8
  Greater Toronto Area municipalities — **excluded E01**, water/sewer is
  one of many bundled "hard services" with no water-specific data or
  outcome anywhere in the paper. Three includes: Brown (1989), a
  historical quasi-experimental logit analysis of 244 Prussian cities
  showing municipal franchise/voting-power concentration (the tax-weighted
  Three Class System) predicts the probability of investing in waterworks
  infrastructure, with instrumented cost, full covariate adjustment, and
  counterfactual province-swap simulations (S590, also added to
  `effect_sizes.csv` Family C — one of the strongest quasi-experimental
  designs in the corpus); Wu (1999), an institutional/fiscal-reform case
  study of China documenting a socialist-era employment/housing-linked
  water-access mechanism and fiscal-decentralization reforms, with
  tap-water coverage tracked as an explicit outcome (81.0%→94.9%
  nationally 1990-1996) (S591); and Marvin & Laurie (1999), a qualitative
  case study of SEMAPA's legal restructuring and privatization in
  Cochabamba, Bolivia, documenting a privatization bid structure tied to
  a 90%-connection-within-5-years target and stark connection-rate
  disparities by neighborhood income (99% in affluent Casco Viejo vs.
  under 4% in some suburbs) (S592). `evidence_map.csv` updated for
  S590-S592; `exclusion_log.csv` updated (601 rows total);
  `full_text_retrieval_queue.csv` regenerated (2,468 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,191/3,659 screened (590 include/601 exclude), 2,468 open, 590
  extracted studies, 29 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: ninetieth full-text screening batch — 1 Drive-retrieved
  PDF, 1 exclude.** Willis & Buonocore (2023), a short AJPH editorial
  commenting on oil and gas extraction siting near marginalized
  communities and reviewing California/New York fracking-regulation
  timelines — **excluded E01**, the paper's subject is oil/gas
  extraction environmental-justice regulation, not water/sanitation
  service access ("community water supply contamination" is mentioned
  once in passing, attributed to a different cited study).
  `exclusion_log.csv` updated (602 rows total);
  `full_text_retrieval_queue.csv` regenerated (2,467 open records);
  duplicate audit and schema validation re-run clean (no
  extraction/evidence_map/effect_sizes changes — pure exclude). Running
  totals: 1,192/3,659 screened (590 include/602 exclude), 2,467 open,
  590 extracted studies, 29 effect_sizes rows (unchanged). Full detail
  in `CHANGELOG.md`.
- **2026-09-22: ninety-first full-text screening batch — 7 Drive-retrieved
  PDFs, 6 includes (S593-S598), 1 exclude.** Ko (2024), a Tobit-regression
  study of water-service equity across 152 South Korean local governments
  (2010/2016/2021) — **included** (S593), also added to `effect_sizes.csv`
  as a Family C candidate: administrative si/gun district classification
  and local tax burden significantly improve equity, while municipal
  fiscal autonomy significantly worsens it, consistently across all 3
  years. Linn, Robbins-Panko, Perry & Seibel (2023), a Flint, Michigan
  ethnographic study of older adults navigating the Emergency Manager
  law and a court-ordered lead-pipe-replacement deadline — **included**
  (S594). Mokoena (2023), a Cape Town Day Zero qualitative study of the
  constitutional water right, Free Basic Water policy, *Mazibuko v.
  Johannesburg* litigation, and prepaid Water Management Devices —
  **included** (S595). Kashem et al. (2023), a Dhaka right-to-water
  study comparing 2 legally-connected and 1 illegally-connected slum,
  finding a 17x water-price differential tied to DWASA's land-title
  connection requirement — **included** (S596). Kouassi et al. (2023),
  a Burkina Faso content-analysis study of CLTS sanitation-program
  abandonment, attributing 26.28% of abandonment to governance/
  institutional factors — **included** (S597). Aluko et al. (2023), a
  548-household Osun State, Nigeria study directly testing an EU/AfDB
  WASH institutional-reform program as an exposure against water
  security (finding no significant effect) — **included** (S598).
  Hamdan, Libânio & Costa (2023), a methodological/engineering paper
  proposing a regulatory inspection-prioritization index (RIQS) across
  591 Minas Gerais, Brazil municipalities — **excluded E06**, the unit
  of analysis is the municipality/utility and the outcome is an
  engineering index score, not a population-level access outcome.
  `extraction_database.csv`/`evidence_map.csv` updated (S593-S598, 590
  → 596 rows each); `effect_sizes.csv` updated (29 → 30 rows, S593
  added); `exclusion_log.csv` updated (603 rows total; E06 45 → 46);
  `full_text_retrieval_queue.csv` regenerated (2,460 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,199/3,659 screened (596 include/603 exclude), 2,460 open, 596
  extracted studies, 30 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: ninety-second full-text screening batch — 8 Drive-retrieved
  PDFs, 6 includes (S599-S604), 2 excludes.** Theodory (2022), a
  mixed-methods Tanzania study finding 58% improved-water access/72%
  satisfaction in a village with a functioning Community Based Water
  Supply Organisation (COBWSO) vs. under 3% access/over 80%
  dissatisfaction in 2 villages without one — **included** (S599). Rout &
  Kattumuri (2022), a book-length 3,714-household survey across 4 Indian
  cities with an institutional-arrangement-type ANOVA on utility
  performance (preface/TOC/intro read in full; Chapters 5-9 body text not
  completely read, so numeric findings flagged provisional) — **included**
  (S600). Twani & Soyapi (2022), a jurimetric analysis of 4 South African
  cases showing an escalating judicial remedy pattern for sanitation
  failures, from deference (Nokotyana) to enforced structural interdicts
  (Beja: 1,316 toilets ordered enclosed; Msunduzi: VIP-toilet construction
  ordered for named farm-occupier households) — **included** (S601). Aluko
  et al. (2022), a 420-inmate Nigerian prison sanitation study —
  **excluded E01**, institutional (non-household) unit of analysis, same
  rationale as prior healthcare-facility/school WASH exclusions. Sullivan
  Lemaitre & Stoler (2023), a narrative review finding Cartagena,
  Colombia's 2001 land-use zoning law (never updated across 11 mayors in 9
  years) masks an estimated 25,898-70,000 unserviced residents behind
  official coverage rates up to 99.91% — **included** (S602). Dakyaga,
  Schramm & Kyessi (2023), a 292-household Dar es Salaam study finding an
  unenforced statutory groundwater-extraction-permit regime linked to
  sharp income-stratified water-price/reliability/health disparities —
  **included** (S603). Wang et al. (2022, Chinese-language, read and
  evaluated in the original Chinese), a Shenzhen urban-political-ecology
  study — **excluded E01**, macro/city-level water-resources governance
  outcome (aggregate consumption/discharge/river-quality), not a
  household-level water-service-access outcome. Mariwah (2022), a rapid
  review of Ghana's sanitation decentralization finding a 6%→18% national
  access increase over 1990-2017 despite an ~80% ungazetted-by-law
  enforcement gap, alongside a GAMA World Bank project completing 21,091
  household toilets ahead of schedule — **included** (S604).
  `extraction_database.csv`/`evidence_map.csv` updated (S599-S604, 596 →
  602 rows each); `effect_sizes.csv` unchanged (30 rows); `exclusion_log.csv`
  updated (605 rows total; E01 196 → 198); `full_text_retrieval_queue.csv`
  regenerated (2,452 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,207/3,659 screened (602 include/605
  exclude), 2,452 open, 602 extracted studies, 30 effect_sizes rows
  (unchanged). Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-third full-text screening batch — 6 Drive-retrieved
  PDFs, 4 includes (S605-S608), 2 excludes.** Meredith et al. (2021), a
  Kibera Nairobi slum-upgrading case study finding the Settlement
  Executive Committee (a formally constituted community institution)
  negotiated legal property ownership plus water/sanitation
  infrastructure for 822 families across a 15-year process including
  litigation — **included** (S605). Zhou & Liang (2021), a 290-city
  Chinese panel regression finding hukou household-registration status
  significantly predicts lower wastewater/solid-waste treatment capacity
  (p<0.01) — **included** (S606), also added to `effect_sizes.csv` as a
  Family C candidate. Biswas et al. (2020), a mobile sanitation-app
  usability study — **excluded E01**, methodology/app-design paper, not a
  population-access-outcome study. Jeil & Abass (2021), an 86-household
  Northern Ghana water-choice study — **excluded E01**, no legal/
  institutional exposure examined (risk-perception/cultural-belief
  study). Romano, Nelson-Nuñez & LaVanchy (2021), a 3-country (Nicaragua/
  Honduras/Costa Rica) comparative review of community-based water
  management legal-recognition frameworks, finding only partial
  registration rates in all 3 countries (e.g. 30% of Nicaraguan CAPS
  within 5 years of the 2010 law) — **included** (S607). Basu et al.
  (2020), a multi-actor India rural-water-governance study (282 community
  participants + 33 Panchayat heads + Block officials, 16 villages)
  documenting a caste-based handpump-exclusion instance and a
  discretionary construction-vs-maintenance funding pattern — **included**
  (S608). `extraction_database.csv`/`evidence_map.csv` updated (S605-S608,
  602 → 606 rows each); `effect_sizes.csv` updated (30 → 31 rows, S606
  added); `exclusion_log.csv` updated (607 rows total; E01 198 → 200);
  `full_text_retrieval_queue.csv` regenerated (2,446 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,213/3,659 screened (606 include/607 exclude), 2,446 open, 606
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-fourth full-text screening batch — 4 Drive-retrieved
  PDFs, 3 includes (S609-S611), 1 exclude.** Jana et al. (2021), a
  documentary/institutional policy analysis of 12 Indian national water
  policies (1949-2012) against 20 SDG-6 sustainability indicators, with
  real city-level coverage/tariff/metering benchmark data, finding no
  policy has ever explicitly addressed water metering — **included**
  (S609). Sohns et al. (2021), a 14-stakeholder participatory causal-loop-
  diagram study of household water vulnerability in rural Alaska,
  documenting regulatory/funding mechanisms constraining access — **
  included** (S610). Gordon & Byron (2021), a cultural-studies essay on
  homeless-encampment "sweeps" and infrastructure-maintenance politics in
  Toronto/San Francisco — **excluded E01**, homelessness/housing policing
  topic, no household water/sanitation access outcome examined. Gonzalez
  Rivas (2023), a mixed-methods analysis of 2,450 Mexican municipalities
  (1950-2010 census) plus 15 official interviews, finding decentralized
  water-policy funding requirements concentrate low household water-
  connection rates among low-technical-capacity municipalities —
  **included** (S611). `extraction_database.csv`/`evidence_map.csv`
  updated (S609-S611, 606 → 609 rows each); `effect_sizes.csv` unchanged
  (31 rows; no new candidates); `exclusion_log.csv` updated (608 rows
  total; E01 200 → 201); `full_text_retrieval_queue.csv` regenerated
  (2,442 open records); duplicate audit and schema validation re-run
  clean. Running totals: 1,217/3,659 screened (609 include/608 exclude),
  2,442 open, 609 extracted studies, 31 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: ninety-fifth full-text screening batch — 2 Drive-retrieved
  PDFs, 2 includes (S612-S613), 0 excludes.** Chapman et al. (2020), a
  32-interview qualitative ethnographic study of women's water access in
  Gressier, Haiti, documenting informal unregulated neighbor-to-neighbor
  pipe networks with no government oversight (~40% of piped households
  restricted monthly for non-payment) — **included** (S612). McCulligh,
  Arellano-García & Casas-Beltrán (2020), a mixed-methods 293-household
  survey across 4 Jalisco municipalities documenting Mexico's weak/
  unenforced water regulation (CONAGUA averaging only 269 inspections/
  year across 41,116 concessions) against household water-service
  intermittency (only 34.1% receive water daily) and affordability
  outcomes — **included** (S613). `extraction_database.csv`/
  `evidence_map.csv` updated (S612-S613, 609 → 611 rows each);
  `effect_sizes.csv` unchanged (31 rows; no new candidates);
  `exclusion_log.csv` unchanged (608 rows; no new exclusions);
  `full_text_retrieval_queue.csv` regenerated (2,440 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,219/3,659 screened (611 include/608 exclude), 2,440 open, 611
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-sixth full-text screening batch — 3 Drive-retrieved
  PDFs, 2 includes (S614-S615), 1 exclude.** Agbemor & Smiley (2021), a
  case-study census of 98 mechanised boreholes plus 2,439 water-user
  interviews in Ghana's Sunyani West District, documenting privately
  managed informal boreholes operating in unenforced violation of Water
  Resources Commission permitting against household access/reliability/
  quantity outcomes — **included** (S614). Tantoh & McKay (2020), a
  108-household survey of community-based water management under
  Cameroon's 1998 water law, finding 34% of households achieved private
  connections (35.6 L/capita/day) vs 66% on communal taps (24.7
  L/capita/day), with 71/108 households unable to afford connection fees
  — **included** (S615). Sandoval & Sarmiento (2020), a macro
  17-country comparative content analysis of Habitat III National Reports
  on informal-settlement/disaster-risk-reduction governance discourse —
  **excluded E01**, water/sewerage access is only an aggregate national
  statistic, no specific legal/administrative mechanism tested.
  `extraction_database.csv`/`evidence_map.csv` updated (S614-S615, 611 →
  613 rows each); `effect_sizes.csv` unchanged (31 rows; no new
  candidates); `exclusion_log.csv` updated (609 rows total; E01 201 →
  202); `full_text_retrieval_queue.csv` regenerated (2,437 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,222/3,659 screened (613 include/609 exclude), 2,437 open, 613
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-seventh full-text screening batch — 2 Drive-
  retrieved PDFs, 1 include (S616), 1 exclude.** Reniko & Kolawole
  (2020), a 35-resident qualitative case study of a proposed prepaid
  water meter (PWM) policy in Karoi, Zimbabwe, framed by residents and
  officials as violating the Zimbabwean Constitution's right to water via
  automatic disconnection, with real revenue-collection data (only 8.2%
  of possible monthly revenue collected under the existing post-paid
  system) — **included** (S616). Grigg (2020), a conceptual/theoretical
  discussion paper on smart water management technologies, with an
  explicitly illustrative (non-empirical) demonstration scenario —
  **excluded E05**, no original empirical data collection.
  `extraction_database.csv`/`evidence_map.csv` updated (S616, 613 → 614
  rows each); `effect_sizes.csv` unchanged (31 rows; no new candidates);
  `exclusion_log.csv` updated (610 rows total; E05 67 → 68);
  `full_text_retrieval_queue.csv` regenerated (2,435 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,224/3,659 screened (614 include/610 exclude), 2,435 open, 614
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-eighth full-text screening batch — 4 Drive-
  retrieved PDFs, 1 include (S617), 3 excludes.** Foster, McSorley &
  Willetts (2019), a field regression comparing handpump technology types
  in Kenya/Gambia — **excluded E06**, engineering exposure, not
  legal/institutional. Venugopal, Foord & Singaram (2020), an MBA-style
  business teaching case on a single toilet-tech social enterprise in
  India — **excluded E12**, no described research methodology. Ahmed
  (2020), an 87-country panel study of state capacity mediating aid
  effectiveness on aggregate national water-access percentages —
  **excluded E01**, macro cross-national governance-index study. Shuaib
  & Rana (2020), a 100-household questionnaire survey across 10 Rajshahi
  slums documenting unrecognized-settlement legal status barring formal
  connection applications and connection-installation bribery against
  household water access/quantity/reliability outcomes — **included**
  (S617). `extraction_database.csv`/`evidence_map.csv` updated (S617,
  614 → 615 rows each); `effect_sizes.csv` unchanged (31 rows; no new
  candidates); `exclusion_log.csv` updated (613 rows total; E01 202 →
  203, E06 46 → 47, E12 3 → 4); `full_text_retrieval_queue.csv`
  regenerated (2,431 open records); duplicate audit and schema
  validation re-run clean. Running totals: 1,228/3,659 screened (615
  include/613 exclude), 2,431 open, 615 extracted studies, 31
  effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: ninety-ninth full-text screening batch — 3 Drive-
  retrieved PDFs, 1 include (S618), 2 excludes.** Adams, Sambu & Smiley
  (2019), a documentary/narrative synthesis of historical and emerging
  institutional arrangements for urban water supply across Sub-Saharan
  Africa, with real tracked city-level household connection-rate and
  service-delivery outcome data cited from the underlying primary
  literature — **included** (S618) via the Legal Institutional Evidence
  Appraisal Framework. Thoradeniya, Pinto & Maheshwari (2019), a
  35-key-informant Sri Lanka study of water quality's effects on
  agriculture and community well-being — **excluded E03**, water-quality
  exposure, no legal/administrative access mechanism. Hailu, Tolossa &
  Alemu (2019), a basin-level multi-stakeholder study of water-security
  governance in the Awash River Basin, Ethiopia — **excluded E01**, macro
  water-resources-governance unit of analysis. `extraction_database.csv`/
  `evidence_map.csv` updated (S618, 615 → 616 rows each);
  `effect_sizes.csv` unchanged (31 rows; no new candidates);
  `exclusion_log.csv` updated (615 rows total; E01 203 → 204, E03 21 →
  22); `full_text_retrieval_queue.csv` regenerated (2,428 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,231/3,659 screened (616 include/615 exclude), 2,428 open, 616
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundredth full-text screening batch — 2 Drive-retrieved
  PDFs, 1 include (S619), 1 exclude.** Robina Ramirez, De Clercq &
  Jackson (2019), a PLS-SEM survey of 124 informal dwellers in Kayamandi
  and Enkanini, Stellenbosch, South Africa, documenting municipal
  by-law application-based connection requirements, statutory
  free-basic-water entitlements, legally-mandated community
  participation, and contested illegal-settlement legal status against
  household-level water/sanitation access, service-parity, and
  affordability outcomes — **included** (S619). Sengupta, Misra,
  Chaudhary & Prakash (2019), an ICT/e-Governance experience paper on
  India's Swachh Bharat Mission-Gramin rural sanitation programme —
  **excluded E06**, technology/engineering exposure, no
  legal/administrative access mechanism. `extraction_database.csv`/
  `evidence_map.csv` updated (S619, 616 → 617 rows each);
  `effect_sizes.csv` unchanged (31 rows; no new candidates);
  `exclusion_log.csv` updated (616 rows total; E06 47 → 48);
  `full_text_retrieval_queue.csv` regenerated (2,426 open records);
  duplicate audit and schema validation re-run clean. Running totals:
  1,233/3,659 screened (617 include/616 exclude), 2,426 open, 617
  extracted studies, 31 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-first full-text screening batch — 2 Drive-
  retrieved PDFs, 2 includes.** Poonia & Punia (2019), a 280-household
  survey along the urban-rural continuum of two Rajasthan cities, using
  logistic regression with payment-for-water interpreted as a proxy for
  institutional (municipal) vs. private water-supply arrangement against
  household drinking-water access — **included** (S620). Reddy (2018), a
  mixed-methods comparative case study of public-private-community
  institutional partnership models for water treatment service delivery
  across 8 Andhra Pradesh villages, with real coverage-by-socioeconomic-
  group and financial-viability outcome data — **included** (S621).
  `extraction_database.csv`/`evidence_map.csv` updated (S620-S621, 617 →
  619 rows each); `effect_sizes.csv` unchanged (31 rows; no new
  candidates); `exclusion_log.csv` unchanged (616 rows total; no
  excludes this batch); `full_text_retrieval_queue.csv` regenerated
  (2,424 open records); duplicate audit and schema validation re-run
  clean. Running totals: 1,235/3,659 screened (619 include/616 exclude),
  2,424 open, 619 extracted studies, 31 effect_sizes rows. Full detail
  in `CHANGELOG.md`.
- **2026-09-22: hundred-second full-text screening batch — 3 Drive-
  retrieved PDFs, 1 include (S622), 1 exclude, 1 left open.** Yadav
  (2018), a case study of an NGO market-based water/sanitation
  improvement project in an illegal informal settlement in NOIDA,
  India, documenting the township authority's explicit refusal to
  extend service due to illegal-settlement status against real
  household baseline-survey access data (85% bottled-water dependence,
  0.6% no sanitation access) — **included** (S622). Mansur, Brondizio,
  Roy, de Miranda Araujo Soares & Newton (2018), a Belem, Brazil
  flood-risk adaptive-capacity study bundling water/sanitation into a
  composite infrastructure index — **excluded E01**, wrong topic (core
  focus is flood-risk climate adaptation). Mabiza (2013), a PhD
  dissertation on IWRM in Zimbabwe — **left open**, flagged
  `wrong_file_retrieved`: correct title/author match, but the delivered
  PDF is a truncated/preview edition missing the empirical Chapters 2-9
  body text, confirmed via two independent extraction methods.
  `extraction_database.csv`/`evidence_map.csv` updated (S622, 619 → 620
  rows each); `effect_sizes.csv` unchanged (31 rows; no new
  candidates); `exclusion_log.csv` updated (617 rows total; E01 204 →
  205); `full_text_retrieval_queue.csv` regenerated (2,422 open
  records); duplicate audit and schema validation re-run clean. Running
  totals: 1,237/3,659 screened (620 include/617 exclude), 2,422 open,
  620 extracted studies, 31 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-third full-text screening batch — 5 Drive-
  retrieved PDFs, 4 includes, 1 exclude.** Ablo & Yekple (2018), a
  200-household Ashaiman, Ghana survey documenting legal land-document/
  building-permit barriers to GWCL water connection — **included**
  (S623). Muchadenyika & Williams (2018), a 30-interview study of the
  2005-2009 ZINWA centralization of Zimbabwean urban water/sanitation
  functions, contravening the Urban Councils Act, against real
  before/after tracked outcomes — **included** (S624). Filcak, Szilvasi
  & Skobla (2018), 17-municipality fieldwork documenting land-title/
  construction-permit denial and debt-conditioned disconnection barring
  Roma settlements' water access in Slovakia — **included** (S625).
  Abubakar (2018), a 60-household Abuja, Nigeria interview study
  documenting regulatory bans on self-supply wells/boreholes and
  informal vending restricting coping-strategy availability —
  **included** (S626). Silva Rodriguez de San Miguel, Trujillo Flores &
  Lambarry-Vilchis (2018), a PRISMA-style systematic review of 21
  secondary documents on Mexico's urban-water legal/institutional
  framework — **excluded E05**, no original empirical data collection.
  `extraction_database.csv`/`evidence_map.csv` updated (S623-S626, 620
  → 624 rows each); `effect_sizes.csv` unchanged (31 rows; no new
  candidates); `exclusion_log.csv` updated (618 rows total; E05 68 →
  69); `full_text_retrieval_queue.csv` regenerated (2,417 open
  records); duplicate audit and schema validation re-run clean. Running
  totals: 1,242/3,659 screened (624 include/618 exclude), 2,417 open,
  624 extracted studies, 31 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-fourth full-text screening batch — 4 Drive-
  retrieved PDFs, 3 includes, 1 exclude.** Akpabio & Udofia (2017), a
  field study of 20 public spaces and 100 interviews in Ikot Ekpene,
  Nigeria, documenting weak/non-existent regulatory enforcement of WASH
  standards — **included** (S627). Pierce (2017), a mixed-methods study
  of 4 Hyderabad, India slums documenting government-recognition/
  notification status and inter-agency jurisdictional disputes as
  institutional access barriers — **included** (S628). Eichelberger
  (2018), an ethnographic study of household water insecurity in
  Newtok, Alaska, documenting village-government funding constraints
  and a school-district water-rationing rule alongside its cultural
  framing — **included** (S629). de Carvalho, Cunha Marques & Cordeiro
  Netto (2018), an ex-post Delphi/TOPSIS regulatory impact assessment
  of Portugal's Law no.194/2009 PPP water reform — **excluded E04**,
  utility/concessionaire-level performance metrics, not household-level
  access outcomes. `extraction_database.csv`/`evidence_map.csv` updated
  (S627-S629, 624 → 627 rows each); `effect_sizes.csv` unchanged (31
  rows; no new candidates); `exclusion_log.csv` updated (619 rows
  total; E04 58 → 59); `full_text_retrieval_queue.csv` regenerated
  (2,413 open records); duplicate audit and schema validation re-run
  clean. Running totals: 1,246/3,659 screened (627 include/619
  exclude), 2,413 open, 627 extracted studies, 31 effect_sizes rows.
  Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-fifth full-text screening batch — 3 Drive-
  retrieved PDFs, 3 includes, 0 excludes.** Button (2017), a 22-
  building/52-interviewee Mumbai qualitative case study documenting the
  city's mandatory rainwater-harvesting ordinance shifting formal
  water-provision responsibility onto households, against real
  household/servant-level access disparities — **included** (S630, not
  effect_sizes eligible). Lewis (2017), a quasi-experimental panel study
  (generalized DiD + dynamic GMM, 336 districts, 2,714 district-year
  observations) exploiting the exogenous timing of Indonesian local-
  government proliferation (*pemekaran*) to identify its causal effect
  on household water/sanitation access — new-district creation reduces
  access by ~1.35 percentage points short-run (long-run ~1.75%,
  p=.023) relative to original districts — **included** (S631,
  **effect_sizes eligible, Family C** — the first new effect_sizes
  candidate found since S606). Fonjong & Fokum (2017), a mixed-methods
  study (49 household + 15 official interviews across 5 municipalities)
  documenting Cameroon's 2005 water-sector privatization running
  contrary to Law 98/005's state-responsibility mandate, against real
  household access-percentage and privatization-perception survey data
  — **included** (S632, not effect_sizes eligible).
  `extraction_database.csv`/`evidence_map.csv` updated (S630-S632, 627
  → 630 rows each); `effect_sizes.csv` updated (31 → 32 rows; S631
  added); `exclusion_log.csv` unchanged (619 rows total; no excludes
  this batch); `full_text_retrieval_queue.csv` regenerated (2,410 open
  records); duplicate audit and schema validation re-run clean. Running
  totals: 1,249/3,659 screened (630 include/619 exclude), 2,410 open,
  630 extracted studies, 32 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-sixth full-text screening batch — 2 Drive-
  retrieved PDFs, 1 include, 1 exclude.** Padowski, Carrera & Jawitz
  (2016), a macro/city-level comparative analysis of urban water
  availability and a 12-metric Institutional Complexity Assessment
  index across 108 large cities in the US and Africa — **excluded E01**,
  outcome variable is city-wide hydrologic+captured water volume versus
  GDP and institutional-complexity score, not household-level access
  data, following the established macro/city-level governance-index
  exclusion precedent. Kasri, Wirutomo, Kusnoputranto & Moersidik
  (2017), a qualitative comparative case study of 4 Pamsimas rural
  water-supply villages in Indonesia, documenting village-government
  decrees and BPSPAMS community-body legal status — explicitly absent
  in one collapsed village — as institutional determinants of
  service-delivery sustainability, against real village-level tracked
  access outcomes (full population access achieved in one village vs.
  zero functioning access in another) — **included** (S633, not
  effect_sizes eligible). `extraction_database.csv`/`evidence_map.csv`
  updated (S633, 630 → 631 rows each); `effect_sizes.csv` unchanged (32
  rows; no new candidates); `exclusion_log.csv` updated (620 rows
  total; E01 205 → 206); `full_text_retrieval_queue.csv` regenerated
  (2,408 open records); duplicate audit and schema validation re-run
  clean. Running totals: 1,251/3,659 screened (631 include/620
  exclude), 2,408 open, 631 extracted studies, 32 effect_sizes rows.
  Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-seventh full-text screening batch — 15 Drive-
  retrieved PDFs, the largest this segment, 9 includes, 6 excludes.**
  Oteng-Ababio (2014), a 520-household Accra, Ghana survey documenting
  GWCL's tenure-based connection refusal and the post-judgment illegal
  status of pan latrines against household water-source/sanitation/
  cholera-incidence data — **included** (S634). McMillan, Spronk & Caswell
  (2014), a qualitative case study of Venezuela's legally-institutionalized
  technical water committees under the 2006 Organic Law on Communal
  Councils, Caracas — **included** (S635). Lewis (2014), a propensity-
  score-matched quasi-experimental evaluation of Indonesia's Water Hibah
  intergovernmental performance-grant program against PDAM equity
  investment and household water connections — **included** (S636,
  **effect_sizes eligible** — grant-financed investment is a significant
  positive determinant of new household water connections). McClanahan
  (2014), a theoretical green-criminology essay on water-privatization/
  greywater criminalization drawing entirely on secondary sources —
  **excluded E05**. Yerian et al. (2014), a qualitative study of statutory
  Water Management Committees under Kenya's 2002 Water Act alongside
  customary governance, Marsabit — **included** (S637). Akinboade, Mokwena
  & Kinfack (2014), a 1,000-respondent Sedibeng, South Africa protest-
  participation survey bundling water into 9 service categories —
  **excluded E01**. Pandey (2015), a municipal-finance book chapter
  bundling water into a seven-point inclusive-habitat charter, India —
  **excluded E01**. van Dijk & Blokland (2016), an editorial introduction
  to a special journal issue summarizing other papers' pro-poor
  benchmarking research — **excluded E05**. Hossain & Ahmed (2015), a
  case study of an NGO-facilitated non-conventional PPP overcoming a
  legal-tenure barrier to DWASA connection in Dhaka slums — **included**
  (S638). Bell (2015), a historical archival analysis of colonial Lima's
  Cabildo water-connection licensing system (1578-1700) — **included**
  (S639). Sutherland, Scott & Hordijk (2015), a 126-interview case study
  of eThekwini Municipality's Free Basic Water Policy and Urban
  Development Line across 4 settlements with contrasting tenure status,
  Durban — **included** (S640). Seward, Xu & Turton (2015), a desk-based
  backcasting analysis of South African national groundwater-resource
  governance with no household-level data — **excluded E01**. Alexander
  et al. (2015), a regression analysis of water-committee governance
  characteristics against scheme functionality, 89 rural Ethiopian
  community water schemes — **included** (S641). De & Nag (2016), a
  541-household survey across 23 Kolkata slums examining notified/non-
  notified legal status and political clientelism against water/
  sanitation/drainage access — **included** (S642). Favaro et al. (2016),
  a municipal-level water-as-environmental-service study across 39 Sao
  Paulo metropolitan-region municipalities with no household-level access
  data — **excluded E01**. `extraction_database.csv`/`evidence_map.csv`
  updated (S634-S642, 631 → 640 rows each); `effect_sizes.csv` updated
  (32 → 33 rows; S636 added); `exclusion_log.csv` updated (626 rows
  total; E01 206 → 210, E05 69 → 71); `full_text_retrieval_queue.csv`
  regenerated (2,393 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,266/3,659 screened (640 include/626
  exclude), 2,393 open, 640 extracted studies, 33 effect_sizes rows. Full
  detail in `CHANGELOG.md`.
- **2026-09-22: hundred-eighth full-text screening batch — 3 Drive-
  retrieved PDFs, 2 includes, 1 exclude.** Appelblad Fredby & Nilsson
  (2013), a historical-institutional case study documenting Kampala,
  Uganda's 2004 NWSC connection-subsidy policy, land-tenure/property-
  rights barriers to piped connections in informal settlements, and the
  2006-onward pre-paid-meter pro-poor pilot project, against real tracked
  connection-count data — **included** (S643, not effect_sizes eligible).
  Erhard, Degabriele, Naughton & Freeman (2013), a WASH-in-schools-for-
  children-with-disabilities policy and provision case study in Malawi and
  Uganda — **excluded E01**, school-based (institutional, non-household)
  unit of analysis, same rationale as the Chatterley/Abu-Elliott-Karanja
  exclusion precedent. Vasquez & Franceschi (2013), a 690-household
  contingent-valuation survey testing preferences for centralized (ENACAL)
  versus decentralized (municipal) water-service governance under
  Nicaragua's Law of Municipalities and National Water Strategy, Leon —
  **included** (S644, not effect_sizes eligible — the centralization
  coefficient itself is not statistically significant in the pooled WTP
  regression). `extraction_database.csv`/`evidence_map.csv` updated
  (S643-S644, 640 → 642 rows each); `effect_sizes.csv` unchanged (33 rows;
  no new candidates); `exclusion_log.csv` updated (627 rows total; E01
  210 → 211); `full_text_retrieval_queue.csv` regenerated (2,390 open
  records); duplicate audit and schema validation re-run clean. Running
  totals: 1,269/3,659 screened (642 include/627 exclude), 2,390 open,
  642 extracted studies, 33 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-ninth full-text screening batch — 1 Drive-
  retrieved PDF, 1 include.** Mugambe, Tumwesigye & Larkan (2013), a
  qualitative study (6 focus group discussions/49 participants, 12
  key-informant interviews) of WASH access barriers among people living
  with HIV/AIDS in Gomba and Mpigi districts, Uganda, documenting
  flat-rate public-facility fee structures lacking pro-poor/vulnerability
  accommodation and exclusion of PLWHA from water-user-committee
  governance, alongside financial/social/physical barriers — **included**
  (S645, not effect_sizes eligible). `extraction_database.csv`/
  `evidence_map.csv` updated (S645, 642 → 643 rows each); `effect_sizes.csv`
  unchanged (33 rows; no new candidates); `exclusion_log.csv` unchanged
  (627 rows total; no excludes this batch); `full_text_retrieval_queue.csv`
  regenerated (2,389 open records); duplicate audit and schema validation
  re-run clean. Running totals: 1,270/3,659 screened (643 include/627
  exclude), 2,389 open, 643 extracted studies, 33 effect_sizes rows. Full
  detail in `CHANGELOG.md`.
- **2026-09-22: hundred-tenth full-text screening batch — 1 Drive-
  retrieved PDF, 1 exclude.** Larson, Alexander, Djalante & Kirono (2013),
  a social-network analysis of formal, informal and "ideal" inter-agency
  governance networks among 6 Makassar, Indonesia water-management
  agencies plus NGO/university collaborators — **excluded E01**,
  institutional-level network-centrality outcome, no household-level water
  access data, same rationale as the Hushie/Soublière-Cloutier/Kimbugwe
  exclusion precedent. `extraction_database.csv`/`evidence_map.csv`
  unchanged (no new includes); `effect_sizes.csv` unchanged (33 rows);
  `exclusion_log.csv` updated (628 rows total; E01 211 → 212);
  `full_text_retrieval_queue.csv` regenerated (2,388 open records);
  schema validation re-run clean. Running totals: 1,271/3,659 screened
  (643 include/628 exclude), 2,388 open, 643 extracted studies, 33
  effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-eleventh full-text screening batch — 10 Drive-
  retrieved PDFs, 8 includes (S646-S653), 2 excludes.** Mycoo (2011,
  Trinidad water-pricing policy, S646) and Bond (2013, South African
  Mazibuko/Phiri constitutional water-rights litigation, S647); Singh,
  Mittal & Upadhyay (2011, North Indian urban water-utility DEA
  benchmarking) **excluded E01** (utility-level technical efficiency, no
  household data); Pierce (2012, Mexico City water-privatization political
  economy, S648); González Rivas (2012, Mexico indigenous-municipality
  piped-water-coverage regression, S649 — **effect_sizes eligible**,
  federal-transfers mechanism under Article 115 municipal water
  governance, indigenous coefficient -0.031 p=0.014, transfers coefficient
  0.571 p=0.019); Fernández & Buitrón Cisneros (2012, Ecuador
  constitutional right-to-water framework, S650); Obeng-Odoom (2012,
  Ghana PURC-regulated water privatization, S651); Harutyunyan (2012,
  Armenia state-vs-private water-service performance benchmarking)
  **excluded E01** (utility-level benchmarking, no household data);
  Hackenbroch & Hossain (2012, Dhaka bosti informal water-supply
  governance ethnography, S652); Brinkerhoff, Wetterberg & Dunn (2012,
  Iraq water-services survey/state-legitimacy study, S653).
  `extraction_database.csv`/`evidence_map.csv` updated (S646-S653, 643 →
  651 rows each); `effect_sizes.csv` updated (S649 added, 33 → 34 rows);
  `exclusion_log.csv` updated (630 rows total; E01 212 → 214); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,378 open records); schema validation re-run clean. Running totals:
  1,281/3,659 screened (651 include/630 exclude), 2,378 open, 651
  extracted studies, 34 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-twelfth full-text screening batch — 7 Drive-
  retrieved PDFs, 3 includes (S654-S656), 3 excludes, 1 wrong_file_retrieved.**
  Hatton MacDonald, Morrison & Barnes (2010, Adelaide WTP/WTA choice-
  modelling methodological comparison for water customer service
  standards) **excluded E01** (methodological contribution, not a
  legal-administrative access-mechanism study); Zagonari (2011, Algeria
  integrated urban-planning optimization model) **excluded E01**
  (technical modeling methodology, no household data); Maclean, Boar &
  Lugo (2011, papyrus-swamp conservation economic-valuation review)
  **excluded E01** (wrong topic, not water/sanitation service access);
  Packialakshmi, Ambujam & Nelliyat (2011, Chennai peri-urban informal
  groundwater market documenting a weakly-enforced regulatory licensing
  regime against household income-based access-bifurcation survey data,
  S654); Tshishonga & Mafema (2011, gendered water/sanitation access in
  two South African informal settlements documenting tenure-based
  institutional barriers and a successful legal tenure-defense case,
  S655); Cahill-Ripley (2011, *The Human Right to Water and its
  Application in the Occupied Palestinian Territories*) **remains open,
  flagged `wrong_file_retrieved`** — correct title/author match but the
  delivered PDF's extraction is missing all substantive chapters
  including the empirical Chapter 6 case study; Mudege & Zulu (2011,
  Nairobi slum water-access discourses documenting Kenya's Water Act
  No. 8/2002 tenure-based exclusion and real disconnection-enforcement
  episodes against a 23,344-household survey and 36 FGDs, S656).
  `extraction_database.csv`/`evidence_map.csv` updated (S654-S656, 651 →
  654 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (633 rows total; E01 214 → 217); duplicate audit found no
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,372 open
  records); schema validation re-run clean. Running totals: 1,287/3,659
  screened (654 include/633 exclude), 2,372 open, 654 extracted studies,
  34 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-thirteenth full-text screening batch — 1 Drive-
  retrieved PDF, 1 include.** Toubkiss (2010, book chapter, "Meeting the
  Sanitation Challenge in Sub-Saharan Cities: Lessons Learnt from a
  Financial Perspective") — a comparative multi-case-study synthesis of
  12 primary Hydroconseil/pS-Eau field case studies (Mali, Burkina Faso,
  Senegal, Niger, Uganda) documenting sanitation-financing institutional
  mechanisms (household-subsidy schemes, sanitation-surcharge fees,
  decentralization without financial transfer, land-tenure barriers)
  against real tracked household-level outcomes (~900,000-1,000,000
  people gaining access via a subsidy scheme over 14-15 years; 56% of
  registered household requests unfulfilled after Senegal's PAQPUD
  programme was prematurely interrupted), S657.
  `extraction_database.csv`/`evidence_map.csv` updated (S657, 654 → 655
  rows each); `effect_sizes.csv` and `exclusion_log.csv` unchanged;
  duplicate audit found no duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,371 open records); schema validation re-run clean.
  Running totals: 1,288/3,659 screened (655 include/633 exclude), 2,371
  open, 655 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-fourteenth full-text screening batch — 3 Drive-
  retrieved PDFs, 1 include, 2 excludes.** Jepson (2012, legal-geography
  case study of two companion 1971-1976 federal legal cases -- Jimenez
  and Fonseca v. Hidalgo WCID 2 et al. -- documenting farmer-controlled
  water-district territorial exclusion of south Texas colonias, denying
  voting rights and political standing over water-service provision,
  against real population-level access-deficiency data for 238,000
  colonias residents, S658); Rasmussen et al. (2009, Lake Manzala
  hydrodynamic-ecological water-quality model, Egypt) **excluded E01**
  (environmental hydrology, no legal/institutional factor); Green &
  Blinkhorn (2010, discussion paper on Aboriginal oral-health
  inequalities, Australia) **excluded E01** (wrong topic, water
  fluoridation is a dental-health input, not a service-access outcome).
  `extraction_database.csv`/`evidence_map.csv` updated (S658, 655 → 656
  rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (635 rows total; E01 217 → 219); duplicate audit found no
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,368 open
  records); schema validation re-run clean. Running totals: 1,291/3,659
  screened (656 include/635 exclude), 2,368 open, 656 extracted studies,
  34 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-fifteenth full-text screening batch — 1 Drive-
  retrieved PDF, 1 exclude.** Gurría (2009, OECD Secretary-General
  policy-commentary essay on global water-governance/financing
  challenges, *Water International*) — **excluded E05**, no original
  empirical data collection, secondary macro-level statistics only, same
  rationale as the McClanahan/van Dijk & Blokland policy-essay
  exclusions. `extraction_database.csv`/`evidence_map.csv` unchanged (no
  new includes); `effect_sizes.csv` unchanged; `exclusion_log.csv`
  updated (636 rows total; E05 71 → 72); `full_text_retrieval_queue.csv`
  regenerated (2,367 open records); schema validation re-run clean.
  Running totals: 1,292/3,659 screened (656 include/636 exclude), 2,367
  open, 656 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-sixteenth full-text screening batch — 5 Drive-
  retrieved PDFs, 3 includes (S659-S661), 2 excludes.** Lanti (2006,
  Jakarta water-supply concession-contract regulatory case study under
  Indonesia's Law No. 7/2004, real longitudinal household connection/
  coverage data, S659); Graham (2006, Great Britain water-disconnection
  judicial-review case producing the Water Industry Act 1999's statutory
  disconnection ban, S660); Moretto (2007, comparative policy-document
  review of donor governance philosophies) **excluded E05** (no original
  empirical data); Klepov (2007, Upper Volga basin hydraulic-engineering
  release-regulation model, Moscow) **excluded E06** (technical modeling
  only); Chappells & Medd (2008, England/Wales post-privatization
  water-charging equity study with real household affordability data and
  22 drought-period interviews, S661).
  `extraction_database.csv`/`evidence_map.csv` updated (S659-S661, 656 →
  659 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (638 rows total; E05 72 → 73, E06 48 → 49); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,362 open records); schema validation re-run clean. Running totals:
  1,297/3,659 screened (659 include/638 exclude), 2,362 open, 659
  extracted studies, 34 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-seventeenth full-text screening batch — 1
  Drive-retrieved PDF, 1 exclude.** Arnell & Delaney (2006, utility-level
  supply-side climate-adaptation study of privatized water companies'
  organizational strategy and Ofwat's regulatory investment-review
  process, England and Wales) — **excluded E01**, no household-level
  access, connection, affordability, or exclusion outcome data, same
  rationale as the utility-level-benchmarking exclusion precedent.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes); `effect_sizes.csv` unchanged; `exclusion_log.csv` updated
  (639 rows total; E01 219 → 220); `full_text_retrieval_queue.csv`
  regenerated (2,361 open records); schema validation re-run clean.
  Running totals: 1,298/3,659 screened (659 include/639 exclude), 2,361
  open, 659 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-eighteenth full-text screening batch — 13
  Drive-retrieved PDFs, 6 includes, 7 excludes.** Includes: Hoko et al.
  (2024, Zimbabwe urban O&M legal-provision institutional study, 11
  local authorities, S662); Muridzo, Hungwe & Chadambuka (2025, Zimbabwe
  disability WASH-access National Disability Policy implementation-gap
  study, 104 women with disabilities, S663); Lewis & Miller (1987,
  Sub-Saharan Africa public-private water-partnership comparative
  institutional review with a primary household-vendor survey, S664);
  Chenoweth (2004, four-country comparative water-ownership-structure
  legal/institutional analysis, S665); Seneviratne (2000, Sri Lanka
  urban water-governance institutional case study, S666); Gyau-Boakye &
  Ampomah (2003, Ghana water-pricing/sector-reform legal-institutional
  case study, S667). Excludes: Chen, Chen & Mitchell (2024, Guangzhou
  NPM sanitation-delivery-mode reform) **E01**; Ahmed (2025, Ghana
  kitchen WEF-nexus diet/cooking study) **E01**; Wutich et al. (2025,
  managed-retreat opinion editorial) **E05**; Gebeyaw et al. (2026,
  Ethiopia IDP elders' crisis-experience study) **E01**; Bajracharya
  (2003, Myanmar sanitation behavior-change program evaluation) **E01**;
  Sikor (2004, Central/Eastern Europe agrarian commons framing paper)
  **E01**; Fonchingong & Ngwa (2005, Cameroon VDA gender-participation
  study) **E01**.
  `extraction_database.csv`/`evidence_map.csv` updated (S662-S667, 659 →
  665 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (646 rows total; E01 220 → 226, E05 73 → 74); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,348 open records); schema validation re-run clean. Running totals:
  1,311/3,659 screened (665 include/646 exclude), 2,348 open, 665
  extracted studies, 34 effect_sizes rows. Full detail in `CHANGELOG.md`.
- **2026-09-22: hundred-nineteenth full-text screening batch — 2
  Drive-retrieved PDFs, 2 excludes.** Foster & Gathu (2024, "VIEWPOINT"
  article synthesizing secondary published surveys on urban groundwater
  use across six tropical African cities) — **excluded E05**, no
  original empirical data collection, same rationale as the Gurria/
  Moretto policy-essay exclusions. Lee (2000, watershed/drinking-
  water-source environmental-protection institutional-failure case
  study, Tegucigalpa, Honduras) — **excluded E01**, measured outcome is
  watershed/environmental degradation and treatment cost, not
  household-level water access, same rationale as the environmental/
  ecological-hydrology wrong-topic precedent.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes); `effect_sizes.csv` unchanged; `exclusion_log.csv` updated
  (648 rows total; E01 226 → 227, E05 74 → 75); `full_text_retrieval_queue.csv`
  regenerated (2,346 open records); schema validation re-run clean.
  Running totals: 1,313/3,659 screened (665 include/648 exclude), 2,346
  open, 665 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twentieth full-text screening batch — 3
  Drive-retrieved PDFs, 2 includes, 1 exclude.** Includes: Dakyaga,
  Ahmed & Sillim (2021, qualitative institutional case study of
  informal/non-state water governance across three Dar es Salaam
  settlements, 35 provider interviews plus key informants, real
  settlement-level household/income data, S668); Brown-Luthango &
  Arendse (2023, qualitative comparative case study of co-production
  between the City of Cape Town and two informal settlements,
  documenting a real municipal Water & Sanitation Department
  regulation on communal-facility siting and a negotiated
  institutional workaround, S669). Exclude: Sun, Gu, Chen, Xia & Chen
  (2022, macro/city-level composite-index panel-regression study of
  urban water supply system resilience, Yangtze River Delta) —
  **excluded E01**, no household-level access data or specific
  legal/administrative mechanism examined, same rationale as the
  Nkiaka/Schiel/Laitinen/Padowski macro-governance-index exclusions.
  `extraction_database.csv`/`evidence_map.csv` updated (S668-S669, 665
  → 667 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (649 rows total; E01 227 → 228); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,343 open records); schema validation re-run clean.
  Running totals: 1,316/3,659 screened (667 include/649 exclude), 2,343
  open, 667 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-first full-text screening batch — 1
  Drive-retrieved PDF, 1 include.** Dosu, Hanrahan, Johnston & Spaling
  (2022, qualitative institutional case study of decentralized rural
  water management capacity gaps across three rural Ghanaian
  communities and multi-level water management agencies, documenting
  the real CWSA/district-assembly regulatory framework via household/
  informant interviews and focus group discussions, S670) — **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S670, 667 →
  668 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` unchanged (no new excludes); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,342 open records); schema validation re-run clean.
  Running totals: 1,317/3,659 screened (668 include/649 exclude), 2,342
  open, 668 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-second full-text screening batch — 1
  Drive-retrieved PDF, 1 include.** Drew, Deepika, Jyotishi & Suripeddi
  (2021, qualitative ethnographic case study of household water
  insecurity across three unplanned-settlement neighbourhood enclaves
  in south-eastern Bangalore, documenting municipal governance failure
  and exclusion from the formal piped-water grid including a BWSSB
  connection fee of US$1340-2680, real primary fieldwork across three
  neighbourhoods, S671) — **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S671, 668 →
  669 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` unchanged (no new excludes); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,341 open records); schema validation re-run clean.
  Running totals: 1,318/3,659 screened (669 include/649 exclude), 2,341
  open, 669 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-third full-text screening batch — 2
  Drive-retrieved PDFs, 2 includes.** Gondo & Kolawole (2020,
  mixed-methods institutional case study of dissonance between
  customary and statutory water institutions in the Okavango Delta,
  Botswana, documenting the WUC Act 1970 and 2008 water-sector reform
  against a large-N primary sample of 455 household heads/44 elders/17
  officials across 3 villages, S672) and Tantoh, Simatele, Ebhuoma,
  Donkor & McKay (2021, mixed-methods institutional case study of
  community-based water management sustainability across six rural
  Cameroonian villages, documenting the decentralization ministerial
  decree and traditional-authority governance against a real
  156-household systematic-sample survey, S673) — both **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S672-S673, 669
  → 671 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` unchanged (no new excludes); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,339 open records); schema validation re-run clean.
  Running totals: 1,320/3,659 screened (671 include/649 exclude), 2,339
  open, 671 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-fourth full-text screening batch — 1
  Drive-retrieved PDF, 1 exclude.** Silva Rodríguez de San Miguel,
  Lambarry-Vilchis & Trujillo Flores (2019, CFA-based drinking-water
  management-quality/user-satisfaction model-building study, Iztapalapa,
  Mexico City) — **excluded E01**, a methodological model-building
  contribution ("role of law" is one of 19 qualitatively-rated
  dimensions, not a primary study of a legal/institutional access
  mechanism), same rationale as the Lanz & Provins/Hatton MacDonald/
  Post-Agnihotri-Hyun/Porse methodological-contribution exclusions.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes); `effect_sizes.csv` unchanged; `exclusion_log.csv` updated
  (650 rows total; E01 228 → 229); `full_text_retrieval_queue.csv`
  regenerated (2,338 open records); schema validation re-run clean.
  Running totals: 1,321/3,659 screened (671 include/650 exclude), 2,338
  open, 671 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-fifth full-text screening batch — 1
  Drive-retrieved PDF, 1 exclude.** Rashid & Pandit (2018, psychometric-
  scaling technical service-quality/design-standard benchmarking study
  of household-toilet construction attributes, rural India) —
  **excluded E06**, no legal/institutional access-barrier mechanism
  examined, same rationale as the Morena et al. 2019 Pekanbaru single-
  dwelling engineering/construction-standard exclusion.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes); `effect_sizes.csv` unchanged; `exclusion_log.csv` updated
  (651 rows total; E06 49 → 50); `full_text_retrieval_queue.csv`
  regenerated (2,337 open records); schema validation re-run clean.
  Running totals: 1,322/3,659 screened (671 include/651 exclude), 2,337
  open, 671 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-22: hundred-twenty-sixth full-text screening batch — 5
  Drive-retrieved PDFs, 5 includes.** Brottem (2018, political-ecology
  study of Mali administrative-territory legal codification driving
  village-level drinking-water-access disparities, 44-municipality
  field survey plus regression, S674); Bond (2019, documentary
  institutional case study of Durban's Free Basic Water policy and the
  litigated Manquele v. eThekwini disconnection case, S675); Hernandez
  Aguilar, Lerner, Manuel-Navarrete & Siqueiros-Garcia (2021, qualitative
  case study of Mexico City's 2017 Sustainable Water Law excluding
  informal settlers, 27 key-informant interviews plus a 41-resident
  questionnaire, S676); Birkenholtz (2013, mixed-methods case study of
  state-planned rural water-network expansion producing intervillage/
  caste/gender differentiation in Rajasthan, real 180-household
  caste-disaggregated survey, S677); Eguavoen (2013, ethnographic-
  historical case study of Ghana's 1992 constitution and WRC Act
  522/1996 in dissonance with customary water rights, 2004-2006 primary
  fieldwork spanning four historical periods, S678) — all **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S674-S678, 671
  → 676 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` unchanged (no new excludes); duplicate audit
  found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,332 open records); schema validation re-run clean.
  Running totals: 1,327/3,659 screened (676 include/651 exclude), 2,332
  open, 676 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-twenty-seventh full-text screening batch, 2
  Drive-retrieved PDFs, 1 include, 1 exclude.** Goldin (2010, qualitative
  institutional case study of South Africa's Breede-Overberg Water
  Management Area, National Water Act/Water Services Act and Catchment
  Management Agency participation structures, paired ethnographic case
  narratives contrasting a white commercial-farmer irrigation scheme with
  the excluded Kassiesbaai fishing village, S679) — **INCLUDE**. Thunqvist,
  Ilskog & Mvungi (2012, qualitative photo-elicitation methodology
  research note on general infrastructural deprivation in a Dar es
  Salaam informal settlement, no legal/institutional factor examined) —
  **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S679, 676
  → 677 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (651 → 652 rows; E01 229 → 230); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,330 open records); schema validation re-run clean.
  Running totals: 1,329/3,659 screened (677 include/652 exclude), 2,330
  open, 677 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-twenty-eighth full-text screening batch, 1
  Drive-retrieved PDF, 1 exclude.** Matous & Ozawa (2010, social-capital
  measurement-instrument methodology paper; water-connection access is a
  brief illustrative validation vignette, not the paper's object of
  study) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes, 677 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (652 → 653 rows; E01 230 → 231); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,329 open records); schema validation re-run clean.
  Running totals: 1,330/3,659 screened (677 include/653 exclude), 2,329
  open, 677 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

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
- Full-text screening itself is far from complete: 1,330 of the 3,659
  Phase-5 includes have been assessed; 2,329 records have not yet been
  reached, not confirmed unretrievable, since retrieval depends entirely
  on the researcher supplying full-text PDFs. Six of those 2,329
  (`wrong_file_retrieved`) were retrieved but did not match their target
  record or lacked complete content, and are pending a correct/complete
  re-retrieval attempt.
- Extraction (Phase 8) is caught up with screening completely — all 677
  current full-text includes are extracted, no outstanding gap.
- **No risk-of-bias rating has been performed on the great majority of the
  677 extracted studies** (a first 12-study partial pilot batch was
  appraised 2026-09-16, plus 2 further studies -- S370, S372 -- with a
  positively-determined AMSTAR 2 rating, see `PRISMA_WORKFLOW.md` Phase 9) —
  `risk_of_bias_tool` is identified per study, but
  `risk_of_bias_rating` is deliberately left blank for the rest pending the official
  version of each appraisal instrument (`RISK_OF_BIAS.md`'s explicit
  prohibition on reconstructing a validated tool from memory). This is a
  real, reportable limitation at this stage, not an oversight.
- **No quantitative-feasibility determination (Phase 11) has been made
  for any candidate synthesis family** — 180 studies being individually
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
- Effect sizes now exist for 26 studies in `effect_sizes.csv` (added
  2026-09-16, extended 2026-09-17 and in later full-text-screening
  batches through 2026-09-19, most recently S526 -- Switzer & Teodoro's
  public-enterprise-pricing ownership-type effect estimate, Family C),
  but none is pooled, and no family-level meta-analysis has
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
