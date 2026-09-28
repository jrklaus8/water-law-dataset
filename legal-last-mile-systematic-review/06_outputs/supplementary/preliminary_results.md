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
- **2026-09-23, hundred-twenty-ninth full-text screening batch, 1
  Drive-retrieved PDF, 1 include.** Ofer (2009, historical-archival/
  oral-history institutional case study of Orcasitas, an illegal Madrid
  shantytown negotiating formal water/sanitation infrastructure via a
  1971 Neighborhood Association legalization and direct negotiation with
  the Canal de Isabel II water-canal company, a primary 230-family
  Ministry of Housing archival database, S680) — **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S680, 677 → 678
  rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  unchanged (no new excludes); duplicate audit found no duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,328 open records);
  schema validation re-run clean.
  Running totals: 1,331/3,659 screened (678 include/653 exclude), 2,328
  open, 678 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-thirtieth full-text screening batch, 1
  Drive-retrieved PDF, 1 exclude.** Crow & McPike (2009, narrative
  literature review of gender/time-use/water-collection drudgery, no
  original data collection or documented systematic search
  methodology; institutional/legal themes only incidental) — **EXCLUDE
  (E05)**.
  `extraction_database.csv`/`evidence_map.csv` unchanged (no new
  includes, 678 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (653 → 654 rows; E05 75 → 76); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,327 open records); schema validation re-run clean.
  Running totals: 1,332/3,659 screened (678 include/654 exclude), 2,327
  open, 678 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-thirty-first full-text screening batch, 4
  Drive-retrieved PDFs, 3 includes, 1 exclude.** Singh (2006, ethnographic
  institutional case study of India's ARWSP statutory coverage criteria
  and PRI site-selection, only 9 of 46 handpumps within SC/ST localities
  despite formal coverage, S681); Singh (2006, companion ethnographic
  case study of PRI/VWSC participation contradictions, hand-pump siting
  denying access to SC/Jatav women despite formal representation, S682);
  Avila Garcia (2006, historical-documentary institutional case study of
  Morelia, Mexico across four centuries of legal water-rights frameworks,
  89% household connection with 300 vs. under 100 lpcd wealthy/poor
  disparity, S683) — all **INCLUDE**. Agnihotri (2008, empirical study of
  land-acquisition/resettlement law and displacement impacts for an
  irrigation project; no water-access outcome examined despite nominal
  "potable water" framing) — **EXCLUDE (E04)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S681-S683, 678
  → 681 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (654 → 655 rows; E04 59 → 60); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,323 open records); schema validation re-run clean.
  Running totals: 1,336/3,659 screened (681 include/655 exclude), 2,323
  open, 681 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-thirty-second full-text screening batch, 2
  Drive-retrieved PDFs, 1 include, 1 exclude.** Hasan (2006, documentary
  institutional case study of NGO-mediated community sanitation in
  Karachi informal settlements, Pakistan's Katchi Abadi regularization
  programme and a provincial ombudsman ruling compelling KWSB to take
  over community-built sewer maintenance, infant mortality 128->37 per
  1,000, S684) — **INCLUDE**. Kucher (2005, historical-legal study of
  medieval Sienese industrial water-use statutes; domestic use barely
  covered, no household access-exclusion outcome examined) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S684, 681 →
  682 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (655 → 656 rows; E01 231 → 232); duplicate
  audit found no duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,321 open records); schema validation re-run clean.
  Running totals: 1,338/3,659 screened (682 include/656 exclude), 2,321
  open, 682 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-23, hundred-thirty-third full-text screening batch, 4
  Drive-retrieved PDFs, 1 include, 3 excludes.** Sawchuk, Burke & Padiak
  (2002, historical demographic natural-experiment study of an 1884
  gubernatorial order granting military families free condenser-water
  access in Gibraltar, statistically significant infant-mortality
  divergence emerging only post-policy, S685) — **INCLUDE**. Sandhu
  (2000, secondary-source housing-poverty synthesis, water one
  incidental indicator among ~10) — **EXCLUDE (E01)**. Dhar (2000,
  narrative policy essay across five basic-service sectors, no original
  data) — **EXCLUDE (E05)**. Banerjee (2001, macro/regional IWRM project
  proposal, no household-level access data) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S685, 682 →
  683 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (656 → 659 rows; E01 232 → 234, E05 76 →
  77); duplicate audit found no duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,317 open records); schema validation re-run clean.
  Running totals: 1,342/3,659 screened (683 include/659 exclude), 2,317
  open, 683 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **2026-09-23, hundred-fortieth full-text screening batch, 16
  Drive-retrieved PDFs, 8 includes, 8 excludes, plus 1 wrong_file_retrieved
  flag.** Bakker (2005, England & Wales privatization/reregulation,
  Ofwat statutory duty, High Court ruling against prepayment meters,
  disconnection-protection legislation, S686) — **INCLUDE**. Schusterman &
  Hardoy (1997, Barrio San Jorge Buenos Aires, 10-year legal-tenure and
  formal-utility-connection transition, S687) — **INCLUDE**. Faisal &
  Kabir (2005, rural Bangladesh gender-water field study, WMG/WMA
  participation-mandate vs. de facto exclusion, S688) — **INCLUDE**. Allen,
  Davila & Hofmann (2006, five-metro-area comparative peri-urban
  water-poor study, policy-driven vs. needs-driven access, S689) —
  **INCLUDE**. Anand (2007, Chennai institutional mapping and household
  entitlements analysis, S690) — **INCLUDE**. Jenson (2008, 19th-century
  Britain citizenship regimes and differential sewer/water connection,
  S691) — **INCLUDE**. Kumara (2013, Bangalore metropolitan governance
  fragmentation and water-supply service delivery, S692) — **INCLUDE**.
  Chathukulam & Devavrathan (2014, Kerala Gram Panchayat sanitation
  field study, S693) — **INCLUDE**. Mustafa (2007, Indus Basin
  hydropolitics narrative review) — **EXCLUDE (E05)**. Ali (2010, slum
  water-treatment technology review) — **EXCLUDE (E06)**. Yang et al.
  (1991, Fujian PHC programme, water incidental) — **EXCLUDE (E01)**.
  Jaglin (2002, sub-Saharan Africa water-reform narrative review) —
  **EXCLUDE (E05)**. Memon et al. (2006, 14-Asian-city macro reform
  review, no household outcome data) — **EXCLUDE (E01)**. Kay et al.
  (2007, UK private-water-supply microbiological quality) — **EXCLUDE
  (E03)**. Perkins (2009, Cairo NGO site-visit commentary) — **EXCLUDE
  (E05)**. Buckley (2011, Mumbai SPARC economic commentary,
  self-described non-empirical) — **EXCLUDE (E05)**. Also: R2EAEC279B644
  (target Koros et al. 2024, Kenya user-owned utilities) flagged
  `wrong_file_retrieved` — delivered PDF was an unrelated 2015 GIZ/World
  Bank Kenya water-kiosk case study; not screened, committed separately.
  `extraction_database.csv`/`evidence_map.csv` updated (S686-S693, 683 →
  691 rows each); `effect_sizes.csv` unchanged (34 rows);
  `exclusion_log.csv` updated (659 → 667 rows; E01 234 → 236, E03 22 →
  23, E05 77 → 81, E06 50 → 51); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,301 open
  records); schema validation re-run clean.
  Running totals: 1,358/3,659 screened (691 include/667 exclude), 2,301
  open, 691 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **2026-09-27, hundred-forty-first full-text screening batch, first
  sub-batch of a large Antigravity-retrieved PDF drop, 10 records, 7
  includes, 3 excludes.** A separate researcher-run retrieval agent
  ("Antigravity") delivered 103 unique full-text PDFs into a new Drive
  folder following the established naming convention; all 103 record_ids
  were cross-checked as open with no prior decisions or wrong_file_retrieved
  history. This is the first of several planned sub-batches; ~93 records
  remain to be processed. Sauri, Olcina & Rico (2007, Spanish water
  privatization and the "Barcelona Water War" court ruling, S694) —
  **INCLUDE**. Mansur & Olmstead (2012, drought-rationing welfare
  economics) — **EXCLUDE (E01)**. Pihljak et al. (2021, Lilongwe uneven
  water pricing regimes, S695) — **INCLUDE**. Fan (2016, Taiwan water-
  diversion megaproject EIA) — **EXCLUDE (E01)**. Lim & Prakash (2020,
  112-country panel study of democratization mitigating industrialization's
  pro-urban water-access bias, S696) — **INCLUDE**, not effect_sizes
  eligible (democracy is a moderator, not a clean isolated exposure).
  Narayanan et al. (2017, meta-analysis of bottom-up urban-poor
  infrastructure delivery, S697) — **INCLUDE** (secondary synthesis, not
  pooled). Page (2003, Kumbo Water Authority community takeover, Cameroon,
  S698) — **INCLUDE**. González-Parra & Simon (2008, Pehuenche resettlement,
  Chile, water incidental to broader compensation package) — **EXCLUDE
  (E01)**. Hoffmann (2004, Zamfara Reserve pastoral common-property
  institutions, Nigeria, S699) — **INCLUDE**. Masanyiwa et al. (2014,
  Tanzania decentralisation and gendered water/health participation, S700)
  — **INCLUDE**.
  `extraction_database.csv`/`evidence_map.csv` updated (S694-S700, 691 →
  698 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (667 → 670 rows; E01 236 → 239); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,291 open
  records); schema validation re-run clean.
  Running totals: 1,368/3,659 screened (698 include/670 exclude), 2,291
  open, 698 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-second full-text screening batch, second
  sub-batch of the Antigravity-retrieved PDF drop, 10 records, 6 includes,
  2 excludes, 2 wrong_file_retrieved flags.** Naz (2015, caste-based water
  exclusion and the Jyotirgram Scheme, Gujarat, S701) — **INCLUDE**. Ley
  (2022, Semarang stormwater/flood drainage, sanitation incidental) —
  **EXCLUDE (E07)**. Mellah (2018, Tunisia's 1975 Water Code allocation
  institution, S702) — **INCLUDE**. Sunderland (2003, London's private
  water monopolies pre-1852 Metropolis Water Act, S703) — **INCLUDE**.
  Cole (2012, Bali tourism-vs-household water competition under Indonesian
  Law No. 7/2004, S704) — **INCLUDE**. Imonikhe & Moodley (2018, four
  Nigerian state water laws and utility autonomy/tariff-setting, S705) —
  **INCLUDE**. Castán Broto & Sudhira (2019, Bangalore historical
  connection-extension regulation and peri-urban informal tenure, S706) —
  **INCLUDE**. Turman-Bryant et al. (2019, Northern Kenya borehole
  remote-monitoring engineering study, no legal/institutional
  access-barrier mechanism) — **EXCLUDE (E01)**. Two records had delivered
  PDF content that did not match their target metadata and were flagged
  `wrong_file_retrieved` without screening: R31E29BB9CFED (target: World
  Bank India water-resources press release; delivered: The Lancet
  Commission's unrelated "Global health 2035" report) and R19FD5701BC0D
  (target: Dondeynaz 2014 on water governance; delivered: an unrelated
  paper on Malaysian construction-industry corporate sustainability).
  `extraction_database.csv`/`evidence_map.csv` updated (S701-S706, 698 →
  704 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (670 → 672 rows; E01 239 → 240, E07 20 → 21); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,283 open records); schema validation re-run clean.
  Running totals: 1,376/3,659 screened (704 include/672 exclude), 2,283
  open, 704 extracted studies, 34 effect_sizes rows. Approximately 83
  records remain from the Antigravity delivery folder. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-third full-text screening batch.** The
  Antigravity delivery folder grew substantially with new uploads beyond
  the original 103-record delivery, reaching roughly 290 genuinely open
  records at time of sweep -- confirming the researcher's advance notice
  of a "big batch." A folder re-sweep also surfaced 10 duplicate
  re-uploads of record_ids already decided in Batch 141 (new Drive file
  IDs, same record_ids), moved directly to Processed without
  re-screening per the standing duplicate-detection/defer rule. Of the
  next 10 open records screened: Wankhade (2015, tenure/legal status and
  urban sanitation access, India, S707) — **INCLUDE**. De & Nag (2016,
  74th Constitutional Amendment decentralization and clientelism, Kolkata
  water vs. drainage delivery, S708) — **INCLUDE**. Reddy (2010, de
  jure/de facto groundwater-rights gap, Rajasthan, S709) — **INCLUDE**.
  Jimenez Cisneros & Torregrosa Armentia (2007, Mexican Water Law reforms
  and urban-rural coverage gap, S710) — **INCLUDE**. Duggal (2004,
  unauthorized-colony legal status and formal/informal water connections,
  Panchkula, S711) — **INCLUDE**. Oberg (2019, discourse analysis of
  open-defecation problematization, Agra) — **EXCLUDE (E01)**. Mumme
  (2016, US-Mexico transboundary treaty, interstate not household-level)
  — **EXCLUDE (E01)**. White (1983, general community-participation
  synthesis essay) — **EXCLUDE (E05)**. Balali et al. (2009, conceptual
  water-management paradigms, Iran) — **EXCLUDE (E05)**. One record had
  delivered PDF content that did not match its target metadata and was
  flagged `wrong_file_retrieved` without screening: RFEBA9E5C7885
  (target: Madeley 2012, "Tourism and water"; delivered: an unrelated
  2023 microbiology/water-quality study of Yucatan cenotes).
  `extraction_database.csv`/`evidence_map.csv` updated (S707-S711, 704 →
  709 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (672 → 676 rows; E01 240 → 242, E05 81 → 83); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,274 open records); schema validation re-run clean.
  Running totals: 1,385/3,659 screened (709 include/676 exclude), 2,274
  open, 709 extracted studies, 34 effect_sizes rows. Roughly 280 records
  remain open in the Antigravity delivery folder, with more uploads
  expected. Full detail in `CHANGELOG.md`.
- **2026-09-27, hundred-forty-fourth full-text screening batch, 10
  records, 4 includes, 6 excludes.** Nyangena (2008, Kenya Water Act 2002
  licensing/tariff regime tied to connection and disconnection outcomes,
  S712) — **INCLUDE**. Morgan (2006, UK Water Industry Act 1999
  disconnection prohibition and UN General Comment 15 tenure
  non-discrimination, S713) — **INCLUDE**. Paerregaard, Stensrud &
  Andersen (2016, Peru's new water law and redefined access rights,
  Andes, S714) — **INCLUDE**. Sambu & Tarhule (2013, Kenyan colonial
  legislative fiat through post-2000 water reforms, S715) — **INCLUDE**.
  Mullen, Vladi & Mills (2006, organizational sensemaking theory applied
  to the Walkerton crisis) — **EXCLUDE (E01)**. Upadhyay (2005, gendered
  intra-household water allocation, Gujarat) — **EXCLUDE (E01)**. Moran
  et al. (2016, NFP-utility hardship-referral partnership network
  analysis, Australia) — **EXCLUDE (E01)**. Arbués & Villanúa (2006,
  water-demand price elasticity, Zaragoza) — **EXCLUDE (E01)**. Adams &
  Vásquez (2019, household-tap willingness-to-pay choice experiment,
  Accra) — **EXCLUDE (E01)**. Cottam (1997, discourse analysis of urban
  poverty applied to a World Bank Zambia project) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S712-S715, 709 →
  713 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (676 → 682 rows; E01 242 → 248); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,264 open
  records); schema validation re-run clean.
  Running totals: 1,395/3,659 screened (713 include/682 exclude), 2,264
  open, 713 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-fifth full-text screening batch, 10
  records, 3 includes, 7 excludes.** Drew & Rai (2016, colonial-legacy
  centralized infrastructure and the Darjeeling 'water mafia' income
  stratification, S716) — **INCLUDE**. Paul (2013, South Africa's
  Promotion of Administrative Justice Act as a water-privatization
  accountability mechanism, S717) — **INCLUDE**. Gilbert (2007, Bogota's
  stratified-tariff legislation and EAAB public utility tied to a
  drop in child diarrhoeal mortality in poor neighborhoods, S718) —
  **INCLUDE**. Tantoh & Simatele (2017, general CBNRM community-
  development framework, Cameroon) — **EXCLUDE (E01)**. Brown & van den
  Broek (2020, NGO-piloted community byelaws for handpump free-riding,
  Uganda) — **EXCLUDE (E01)**. Pietila, Hukka & Katko (2007, well-
  functioning Finnish municipal water system, no documented exclusion
  outcome) — **EXCLUDE (E01)**. Low (2015, Ottoman/Saudi imperial
  pilgrimage-infrastructure technopolitics, Hijaz) — **EXCLUDE (E02)**.
  Lai et al. (2020, systems-engineering non-revenue-water reform,
  Malaysia) — **EXCLUDE (E06)**. Sherval & Askew (2012, agricultural
  irrigation drought/water-allocation study, rural Victoria) — **EXCLUDE
  (E01)**. Dimaano (2015, Maynilad non-revenue-water engineering case
  study, Manila) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S716-S718, 713 →
  716 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (682 → 689 rows; E01 248 → 252, E02 33 → 34, E06 51 → 53);
  duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,254 open records); schema validation re-run clean.
  Running totals: 1,405/3,659 screened (716 include/689 exclude), 2,254
  open, 716 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-sixth full-text screening batch, 10
  records, 5 includes, 5 excludes.** Whitfield (2006, Ghana's PSP water
  policy and World Bank-mandated lease contract tied to poor-household
  affordability, S719) — **INCLUDE**. Jimenez (2004, municipal sewer-
  connection permit system, Morelia, Mexico 1880-1920, S720) —
  **INCLUDE**. Acey (2019, differential regulation of state vs. non-state
  water markets, Lagos and Benin City, S721) — **INCLUDE**. Solo (1999,
  state utility monopoly-rights laws constraining independent providers
  who reach the poor better than subsidized monopolies, multi-country,
  S722) — **INCLUDE**. McDonald & Grineski (2012, colonias/colonias
  populares excluded from municipal annexation, institutional racism,
  El Paso/Ciudad Juarez, S723) — **INCLUDE** (not effect_sizes eligible:
  ecological spatial regression, tenure is one of several general
  covariates, not an isolated legal-mechanism estimate). Mamo & Novotny
  (2024, Ethiopia market-based-sanitation implementation challenges) —
  **EXCLUDE (E01)**. Geels (2005, socio-technical transitions theory,
  Netherlands water supply 1850-1930) — **EXCLUDE (E01)**. Lopus et al.
  (2017, farmer-satisfaction survey of CWP irrigation, Mount Kenya) —
  **EXCLUDE (E01)**. Rogers et al. (2015, elderly perceptions of water
  policy, rural Australia) — **EXCLUDE (E01)**. Bouwer (2006, "Women and
  Water" synthesis essay) — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S719-S723, 716 →
  721 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (689 → 694 rows; E01 252 → 256, E05 83 → 84); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,244 open records); schema validation re-run clean.
  Running totals: 1,415/3,659 screened (721 include/694 exclude), 2,244
  open, 721 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-seventh full-text screening batch, 10
  records, 6 includes, 4 excludes.** Schuller & Levey (2014, land
  ownership status significantly predicts WASH-service gaps across 108
  Haiti IDP camps, S724) — **INCLUDE** (not effect_sizes eligible:
  chi-square is nonparametric). Wilcox et al. (2010, Wisconsin's lack of
  local well-construction regulatory authority vs. Kansas/Utah, S725) —
  **INCLUDE**. Franceys & Gerlach (2011, comparative consumer-involvement
  regulatory design for low-income/informal water consumers, S726) —
  **INCLUDE**. Strauss (2011, Indonesian water law/decrees and Bali Local
  Government Regulation on subak rights vs. tourism licensing, S727) —
  **INCLUDE** (extends Cole 2012/S704). Taks (2008, Uruguay's 2004
  Constitutional Water Referendum and Maldonado privatization exclusion,
  S728) — **INCLUDE**. Aguilar & Lopez (2009, settlement legal status and
  water-supply-security disparity, Xochimilco, S729) — **INCLUDE**.
  da Silva Wells & Sijbesma (2012, CLTS practitioner methods, Asia) —
  **EXCLUDE (E01)**. Campos et al. (2015, sanitary-risk assessment
  methodology, Maputo) — **EXCLUDE (E01)**. Abedin & Shaw (2013, SIPE
  composite adaptability index, Bangladesh) — **EXCLUDE (E01)**. O'Keefe
  et al. (2015, market-driven sanitation social enterprise, East Africa)
  — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S724-S729, 721 →
  727 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (694 → 698 rows; E01 256 → 260); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,234 open
  records); schema validation re-run clean.
  Running totals: 1,425/3,659 screened (727 include/698 exclude), 2,234
  open, 727 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-eighth full-text screening batch, 10
  records, 7 includes, 3 excludes.** Galvin (2011, municipal capacity and
  urban-biased national delivery programmes limiting rural participation,
  S730) — **INCLUDE** (extends Masanyiwa 2014/S700). Hillier (2014,
  permissive regulatory environment for private water companies,
  nineteenth-century London, S731) — **INCLUDE** (extends
  Sunderland 2003/Jenson 2008, S703/S691). Tewari & Oumar (2013, South
  Africa's National Water Act 1998 permit system's institutional
  inefficiencies undermining its own equity objective, S732) —
  **INCLUDE**. Truelove (2011, illegal-slum vs. legal-resettlement-colony
  status tied to water/sanitation access and "criminalization of the
  poor" discourse, Delhi, S733) — **INCLUDE**. Kooy & Bakker (2008,
  colonial and contemporary kampung/formal-settlement legal
  classification producing enduring water-access differentiation,
  Jakarta, S734) — **INCLUDE**. Fisher (2009, national resource-
  governance reform and local hybrid public/private utility
  restructuring, Tagbilaran City, S735) — **INCLUDE**. Reis & Mollinga
  (2015, structural gap between formal Rural Water Supply policy design
  and informal implementation practice, Vietnam, S736) — **INCLUDE**.
  Reddy et al. (2012, life-cycle-costs public-finance methodology, rural
  Andhra Pradesh) — **EXCLUDE (E01)**. Bauchspies (2012, gender/
  technology ethnography, Guinea) — **EXCLUDE (E01)**. Chandola (2013,
  sound-studies/cultural-anthropology soundscapes analysis, Delhi) —
  **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S730-S736, 727 →
  734 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (698 → 701 rows; E01 260 → 263); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,224 open
  records); schema validation re-run clean.
  Running totals: 1,435/3,659 screened (734 include/701 exclude), 2,224
  open, 734 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-forty-ninth full-text screening batch, 10
  records, 5 includes, 5 excludes.** Singh, Wickenberg, Astrom & Hyden
  (2008, field data showing 9 of 44 public handpumps sited in
  underprivileged-caste localities despite prioritized-beneficiary status,
  caste-blind numerical siting criterion, central India, S737) —
  **INCLUDE**. Munala & Kainz (2012, weak regulatory enforcement over
  corporatised utility KIWASCO enabling water-cartel control of kiosk
  access/pricing, informal settlements, Kisumu, Kenya, S738) — **INCLUDE**
  (extends Ranganathan/Bangalore water-mafia precedent, S706). Sutherland,
  Hordijk, Lewis, Meyer & Buthelezi (2014, constitutional right-to-water/
  Free Basic Water Policy and Municipal Structures Act devolution combined
  with spatial-differentiation service model, eThekwini Municipality,
  Durban, S739) — **INCLUDE**. Asthana (2003, regression isolating
  centralised vs. decentralised utility management, n=1,708, central
  India, S740) — **INCLUDE** (not effect_sizes eligible: outcomes are
  utility production/cost-efficiency metrics, not a water-access outcome).
  Baer & Gerlak (2015, comparative discourse analysis finding the global
  HRtWS implementation approach fails to address state corruption/
  peri-urban residents' needs, Bolivia, S741) — **INCLUDE**. Wafer (2012,
  citizenship-discourse analysis of electricity-disconnection protests,
  post-apartheid Soweto) — **EXCLUDE (E01)**. Lee (2014, border-studies
  analysis of transboundary bulk water supply, Hong Kong/China) —
  **EXCLUDE (E01)**. Willoughby-Herard (2014, literary genealogy of three
  works of fiction, black feminist politics) — **EXCLUDE (E05)**.
  Choguill (1994, generic implementation-theory framework, Bangladesh/
  Honduras) — **EXCLUDE (E01)**. Roth et al. (2004, STS boundary-work
  analysis of a water-main-extension dispute, Canada) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S737-S741, 734 →
  739 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (701 → 706 rows; E01 263 → 267, E05 84 → 85); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,214 open records); schema validation re-run clean.
  Running totals: 1,445/3,659 screened (739 include/706 exclude), 2,214
  open, 739 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fiftieth full-text screening batch, 10 records,
  5 includes, 5 excludes.** Nemarundwe & Kozanayi (2003, formal/informal
  institutional rules directly determining conditional access to
  community and private water sources, with documented denial-of-access
  mechanisms, southern Zimbabwe, S742) — **INCLUDE**. Nash (2007, federal
  groundwater-extraction permits granted to Coca-Cola, unmetered and
  uncompensated, tied to water scarcity for indigenous residents, Chiapas,
  Mexico, S743) — **INCLUDE**. Farooqui (2020, ethnographic case study of
  formal/informal status distinctions shaping water access, low-income
  settlement, Karachi, S744) — **INCLUDE** (extends Truelove/S733 and
  Kooy & Bakker/S734). Gorostiza, March & Sauri (2013, anarchist-union
  worker collectivization of a private water utility introducing a single
  citywide tariff and subsidized "social" price, Barcelona, Spanish Civil
  War, S745) — **INCLUDE**. Thomas-Slayter (1992, county-council
  sand-extraction permits documented to destroy a community's dry-season
  water source, with a traced causal chain to declining well levels and a
  5-hour round-trip water-fetching burden, rural Kenya, S746) —
  **INCLUDE**. Earle (2007, Lesotho Highlands Water Project bribery-
  prosecution legal doctrine, bulk transboundary megaproject) — **EXCLUDE
  (E01)**. Schwartz & McConnell (2009, comparative regulatory-failure/
  reform theory, Walkerton and an unrelated Israeli disaster) — **EXCLUDE
  (E01)**. Madon & Sahay (2002, NGO information/communication mediation
  model, Bangalore slums) — **EXCLUDE (E01)**. Zwarteveen (1997, gender
  and water rights in irrigation/productive water use) — **EXCLUDE
  (E01)**. Quaghebeur, Masschelein & Nguyen (2004, Foucauldian
  governmentality critique of participatory-methodology theory, Vietnam
  water-management project) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S742-S746, 739 →
  744 rows each); `effect_sizes.csv` unchanged (34 rows); `exclusion_log.csv`
  updated (706 → 711 rows; E01 267 → 272); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,204 open
  records); schema validation re-run clean.
  Running totals: 1,455/3,659 screened (744 include/711 exclude), 2,204
  open, 744 extracted studies, 34 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-first full-text screening batch, 10
  records, 7 includes, 3 excludes.** K'Akumu (2008, Water Act 2002
  rights ambiguity, powerless CAAC, WRUAs never established, Kenya,
  S747) — **INCLUDE**. Cornea, Zimmer & Veron (2016, ambiguous statutory
  governance and fragmented control enabling informal-institution-
  mediated, caste/class/gender-differentiated pond access, Bardhaman,
  West Bengal, S748) — **INCLUDE**. Barbosa & Brusca (2015, unbalanced
  panel regression, 51 corporations, private-ownership coefficient
  +0.3456 R$/m3 on water tariffs, significant, Brazil, S749) —
  **INCLUDE** (effect_sizes eligible, added as the 35th row; ownership/
  regulatory-structure exposure not mapped to Family A/B/C, not pooled).
  Pascual Sanz, Schouten & Hantke-Domas (2011, comparative case study of
  three tariff-setting regulatory regimes, Netherlands/Spain/Scotland,
  S750) — **INCLUDE**. Saravanan et al. (2015, historical infrastructure
  legacy and municipal policy producing sociospatial water-access
  inequality and disease burden, Ahmedabad, S751) — **INCLUDE**. Narsiah
  (2013, corporatisation/ring-fencing institutional restructuring tied
  to tariff increases affecting vulnerable residents, Durban, S752) —
  **INCLUDE** (extends Sutherland et al. 2014/S739). Nilsson (2006,
  colonial-era piped water/sewer system designed for affluent groups
  with durable institutional inertia, Kampala, S753) — **INCLUDE**
  (extends Kooy & Bakker 2008/S734). Chitonge (2014, broad continent-
  level infrastructure-financing review, African cities) — **EXCLUDE
  (E01)**. Capone (2013, Naples toxic-waste-trafficking narrative, water
  mentioned only in passing) — **EXCLUDE (E01)**. Ballestero (2012, NGO
  project audit-culture/transparency ethnography, Costa Rica) —
  **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S747-S753, 744 →
  751 rows each); `effect_sizes.csv` updated (34 → 35 rows, S749 added);
  `exclusion_log.csv` updated (711 → 714 rows; E01 272 → 275); duplicate
  audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,194 open records); schema validation re-run clean.
  Running totals: 1,465/3,659 screened (751 include/714 exclude), 2,194
  open, 751 extracted studies, 35 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-second full-text screening batch, 10
  records, 5 includes, 5 excludes.** Bjorkman (2014, 18-month ethnographic
  account of water-infrastructure criminalization mediating a
  settlement's legal reclassification from municipal colony to illegal
  slum, Mumbai, S754) — **INCLUDE** (extends Truelove/S733, Kooy &
  Bakker/S734). White et al. (2008, government Water Reserve land
  declarations with eviction powers and a 14-year-unenacted water-
  ownership statute explaining rural/urban access inequity, Kiribati,
  S755) — **INCLUDE**. Diedericks & Nealer (2015, statutory district
  water-sector-planning requirement documented as unimplemented, South
  Africa, S756) — **INCLUDE**. Awortwi (2006, users' satisfaction survey
  comparing sanitation service quality across public/private/community
  institutional arrangements, 3 Ghanaian cities, S757) — **INCLUDE**.
  Brocas, Chan & Perrigne (2006, structural model of CPUC rate-of-return
  regulation with quantified counterfactual consumer-surplus effects, 32
  California districts, S758) — **INCLUDE** (not effect_sizes eligible:
  simulated counterfactuals, not a directly-observed regression
  coefficient). Boland (2007, ideology/discourse analysis of affluent
  secession via premium water networks, China) — **EXCLUDE (E01)**.
  Nayak & Samal (2025, composite Water Security Index from secondary
  data, Bhubaneswar) — **EXCLUDE (E01)**. Douvitsa & Kassavetis (2014,
  normative water-cooperative policy-proposal essay, Greece) — **EXCLUDE
  (E05)**. Barrington et al. (2016, social-marketing-exchange behaviour-
  change framework for WASH, Melanesia) — **EXCLUDE (E01)**. Zeitoun,
  Eid-Sabbagh & Loveless (2014, International Humanitarian Law analysis
  of wartime water-infrastructure damage, Israel-Lebanon) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S754-S758, 751 →
  756 rows each); `effect_sizes.csv` unchanged (35 rows); `exclusion_log.csv`
  updated (714 → 719 rows; E01 275 → 279, E05 85 → 86); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,184 open records); schema validation re-run clean.
  Running totals: 1,475/3,659 screened (756 include/719 exclude), 2,184
  open, 756 extracted studies, 35 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-third full-text screening batch, 10
  records, 3 includes, 7 excludes.** Bakker (2003, foundational typology
  distinguishing privatization from commercialization/regulatory change,
  linked to fragmented class-differentiated water coverage, global South,
  S759) — **INCLUDE**. Ahlers, Schwartz & Perez Guida (2013, field
  research showing inequities between small-scale independent water
  providers undermine market-competition/formalization policy, Maputo,
  S760) — **INCLUDE** (extends Ranganathan/Munala & Kainz). Nzengya
  (2018, quasi-experimental DMM-vs-control comparison, significantly
  lower water costs in DMM settlements, Kisumu, S761) — **INCLUDE** (not
  effect_sizes eligible: ANOVA, not a regression-based estimate, per S724
  precedent). O'Leary (2018, citizen-science/data-collection-methodology
  paper, Delhi) — **EXCLUDE (E01)**. Almandoz et al. (2005, hydraulic-
  engineering leakage-simulation methodology) — **EXCLUDE (E06)**.
  Bischoff-Mattson et al. (2020, Q-methodology practitioner-perception
  study, Cape Town Day Zero) — **EXCLUDE (E01)**. Das, Laishram & Jawed
  (2019, public-participation project-management framework development,
  Guwahati) — **EXCLUDE (E01)**. Xu et al. (2009, sensor-placement
  engineering/operations-research paper) — **EXCLUDE (E06)**. Arlosoroff,
  Roche & Wright (1989, pumping-technology cost-benefit engineering
  tool) — **EXCLUDE (E06)**. Mitchell, Whiteside & Jones (2009, GIS
  asset-management prioritization tool) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S759-S761, 756 →
  759 rows each); `effect_sizes.csv` unchanged (35 rows); `exclusion_log.csv`
  updated (719 → 726 rows; E01 279 → 282, E06 53 → 57); duplicate audit
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (2,174 open records); schema validation re-run clean.
  Running totals: 1,485/3,659 screened (759 include/726 exclude), 2,174
  open, 759 extracted studies, 35 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-fourth full-text screening batch, 10
  records, 9 includes, 1 exclude.** Kumasi, Agbemor & Burr (2019, Ghana
  decentralised rural water governance, post-paid financing model and
  repair delay, S762) — **INCLUDE**. Nzengya (2015, IAD Framework case
  study of Kenya Water Act 2002 DMM, Lake Victoria, S763) — **INCLUDE**
  (companion to S761). Helgegren et al. (2021, multi-regime institutional
  analysis with legislation as an institutionalization dimension,
  Bolivia, S764) — **INCLUDE**. Meeks (2018, quasi-experimental modified
  difference-in-differences, PETT land-titling program, Peru, S765) —
  **INCLUDE, EFFECT_SIZES ELIGIBLE (Family A)**: core DiD estimate on
  improved water source access = 0.059 (SE 0.027, p<0.05, n=3,182), added
  as the 36th effect_sizes.csv row. Jones, Reed & Bevan (2003, WEDC
  disability-WASH research project, S766) — **INCLUDE**. Ravnborg &
  Jensen (2012, comparative institutional analysis of statutory vs.
  actual water governance, 5 countries, S767) — **INCLUDE**. Smith (2004,
  Cape Town corporatization/cost-recovery case study, extends
  Sutherland/eThekwini precedent, S768) — **INCLUDE**. Adeoti & Fati
  (2020, Ekiti State Water Corporation Law No. 4 of 1997 case study,
  Nigeria, S769) — **INCLUDE**. Novotny, Humnalova & Kolomaznikova (2018,
  command-and-control CLTSH sanitation-enforcement mechanism, Ethiopia,
  S770) — **INCLUDE**. Onabolu et al. (2011, water-quality
  contamination-tracking/KAP study, Katsina State Nigeria) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S762-S770, 759 →
  768 rows each); `effect_sizes.csv` updated (35 → 36 rows; S765 Meeks
  2018 added); `exclusion_log.csv` updated (726 → 727 rows; E01 282 →
  283); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,164 open records);
  schema validation re-run clean.
  Running totals: 1,495/3,659 screened (768 include/727 exclude), 2,164
  open, 768 extracted studies, 36 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-fifth full-text screening batch, 10
  records, 8 includes, 2 excludes.** Hendry (2016, Customer Forum
  negotiated-settlement regulation, Water Industry (Scotland) Act 2002,
  S771) — **INCLUDE**. Nagaraj & Namasivayam (2010, Sen's entitlements
  approach, planned/unplanned urban-limit legal status, Cuddalore Tamil
  Nadu, S772) — **INCLUDE**. Clifford-Holmes et al. (system-dynamics
  case study, National Water Act 1998/Water Services Act 1997, South
  Africa, S773) — **INCLUDE**. Abubakar (2016, institutional/governance
  case study of water service quality, Abuja, S774) — **INCLUDE**.
  Marson & van Dijk (2016, NWASCO pro-poor regulatory tools, Zambia,
  S775) — **INCLUDE**. Laryea-Adjei & van Dijk (2012, Local Government
  Act 1993/CWSA Act 1998 two-district decentralisation comparison,
  Ghana, S776) — **INCLUDE**. Sally et al. (2014, Cameroonian water
  law's exclusive utility mandate excluding community schemes, Buea,
  S777) — **INCLUDE**. Heller, Rezende & Cairncross (2014, Concessions
  Law No. 8987/1995 and Planasa 1971 institutional-history analysis,
  Brazil, S778) — **INCLUDE**. Weaver et al. (2019, Communities of
  Practice theory applied to CSO emergence, South Africa) — **EXCLUDE
  (E01)**. Nigam & Ghosh (1995, global cost-estimation/financing model)
  — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S771-S778, 768 →
  776 rows each); `effect_sizes.csv` unchanged (36 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (727 → 729 rows; E01 283 → 284, E05 86 →
  87); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,154 open records);
  schema validation re-run clean.
  Running totals: 1,505/3,659 screened (776 include/729 exclude), 2,154
  open, 776 extracted studies, 36 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-sixth full-text screening batch, 10
  records, 5 includes, 5 excludes.** Tynan (2013, historical-legal
  analysis of sewer-connection legality and Parliamentary investment-
  approval regulation, 19th c. London, S779) — **INCLUDE**. Pizzi
  (2020, OLS regression on Chinese ethnic-minority-autonomous-county
  legal status and drinking-water beneficiaries, Guizhou, S780) —
  **INCLUDE, EFFECT_SIZES ELIGIBLE (Family A)**: coefficient -41,810.91
  (SE 25,959.55), not significant, recorded as a null result; added as
  the 37th effect_sizes.csv row. Crawford & Bell (2012, three-
  settlement comparative case study extending the splintering-
  urbanism precedent, Cusco Peru, S781) — **INCLUDE**. Pierce &
  Gmoser-Daskalakis (2021, regression analysis of incorporation date
  and water-system fragmentation, 482 California cities, S782) —
  **INCLUDE**, companion to S037. Pezon (2017, ONEA concession/
  affermage price-cap regulation analysis, Burkina Faso, S783) —
  **INCLUDE**. Ezeudu (2019, literature review, no original empirical
  data, Nigeria sanitation) — **EXCLUDE (E05)**. Takeda & Putthividhya
  (2015, inter-sectoral irrigation allocation, Thailand) — **EXCLUDE
  (E01)**. Rowles et al. (2020, water-quality chemistry study,
  colonias) — **EXCLUDE (E03)**. Ouellet-Plamondon et al. (2009,
  vehicle washdown biosecurity engineering audit) — **EXCLUDE (E06)**.
  Asay (2007, backflow prevention plumbing trade article) — **EXCLUDE
  (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S779-S783, 776 →
  781 rows each); `effect_sizes.csv` updated (36 → 37 rows; S780 Pizzi
  2020 added); `exclusion_log.csv` updated (729 → 734 rows; E01 284 →
  285, E03 23 → 24, E05 87 → 88, E06 57 → 59); duplicate audit found no
  new duplicates; `full_text_retrieval_queue.csv` regenerated (2,144
  open records); schema validation re-run clean.
  Running totals: 1,515/3,659 screened (781 include/734 exclude), 2,144
  open, 781 extracted studies, 37 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-seventh full-text screening batch, 10
  records, 7 includes, 3 excludes.** Bhattarai et al. (2021, statutory
  30% women's-quota mechanism in local water governance, Nepal, S784)
  — **INCLUDE**. Wait et al. (2020, administrative-implementation gap
  in state private-well regulations, North Carolina, S785) —
  **INCLUDE**. Lloyd Owen (2013, Ofwat price-cap regulation and
  statutory disconnection ban, Glas Cymru, Wales, S786) — **INCLUDE**.
  Montgomery & Dacin (longitudinal case study of the 2014 Detroit mass
  water-shutoff crisis, S787) — **INCLUDE**. Marques, Simoes & Berg
  (2013, ARE multi-sector regulator benchmarking design, Cape Verde,
  S788) — **INCLUDE**. Grimes (2011, South Africa's constitutional
  right to water, UN GC15, provider-consumer disputes, S789) —
  **INCLUDE**. Krasznai Kovacs et al. (2019, six-town comparative
  political-ecology case study of water-infrastructure governance,
  India/Nepal, S790) — **INCLUDE**. Nallathiga (2011, normative policy-
  reform-agenda review, India) — **EXCLUDE (E05)**. Ruet, Gambiez &
  Lacour (2007, peri-urban farmer bulk-water property-rights conflict,
  Chennai) — **EXCLUDE (E01)**. Mulas et al. (2011, wastewater
  treatment soft-sensor engineering study) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S784-S790, 781 →
  788 rows each); `effect_sizes.csv` unchanged (37 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (734 → 737 rows; E01 285 → 286, E05 88 →
  89, E06 59 → 60); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,134 open records);
  schema validation re-run clean.
  Running totals: 1,525/3,659 screened (788 include/737 exclude), 2,134
  open, 788 extracted studies, 37 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-eighth full-text screening batch, 10
  records, 7 includes, 3 excludes.** Fuente & Bartram (2018, GLAAS
  pro-poor governance survey document analysis, S791) — **INCLUDE**.
  Swatuk & Kgomotso (2007, deliberate government under-service policy
  for remote areas, Botswana, S792) — **INCLUDE**. Beisheim et al.
  (transnational PPP institutional-design comparison, 10 projects,
  Bangladesh/India/Kenya, S793) — **INCLUDE**. Vasquez (2015,
  municipal vs. community-managed governance-type comparison,
  Guatemala, S794) — **INCLUDE**. Hailu, Osorio & Tsukada (2012,
  probit DiD across 4 Bolivian cities, S795) — **INCLUDE, EFFECT_SIZES
  ELIGIBLE**: privatization effect on piped-water access = 0.077 (SE
  0.016, p<0.01), added as the 38th effect_sizes.csv row (blank
  synthesis_family). Bradlow (comparative-historical case study of
  bureaucratic embeddedness/cohesion, Sao Paulo favelas, S796) —
  **INCLUDE**. Britto, Maiello & Quintslr (2018, 1974 complementary
  law and CEDAE state water company governance, Rio de Janeiro, S797)
  — **INCLUDE**. Guppy (2014, Water Poverty Index methodology-
  validation study) — **EXCLUDE (E01)**. Lee (1995, secondary-
  statistics regional financing-policy model) — **EXCLUDE (E05)**.
  Ako et al. (2010, descriptive MDG-progress synthesis, Cameroon) —
  **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S791-S797, 788 →
  795 rows each); `effect_sizes.csv` updated (37 → 38 rows; S795 added);
  `exclusion_log.csv` updated (737 → 740 rows; E01 286 → 287, E05 89 →
  91); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,124 open records);
  schema validation re-run clean.
  Running totals: 1,535/3,659 screened (795 include/740 exclude), 2,124
  open, 795 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-fifty-ninth full-text screening batch, 10
  records, 6 includes, 4 excludes.** Mulwafu & Msosa (2005, absence-of-
  enabling-legislation barrier blocking Catchment Management Authorities,
  Malawi, S798) — **INCLUDE**. Roy, Akshintala & Sharma (2013, JNNURM
  reform analysis, tenure documentation linked to resettlement-colony
  water quality, Delhi, S799) — **INCLUDE**. Lewis (1998, local-vs-
  central administrative authority OLS/2SLS regression and access-time/
  reliability comparison, Kenya, S800) — **INCLUDE**, not effect_sizes
  eligible (Table 3's significant finding is an unadjusted difference-
  of-means comparison, not a regression, per the S724/S761 precedent;
  Table 1's regression found the authority dummy not significant).
  Townsend & Eyles (2004, 30 key-informant interviews on clientelistic
  administrative practice and institutional fragmentation, Tijuana,
  S801) — **INCLUDE**. Brady & Gray (2013, survey of 104 Group Water
  Schemes and 34 local authorities, fragmented unregulated tariff-
  setting, Ireland, S802) — **INCLUDE**. Vasquez (2011, official-
  perceptions interviews, companion to S794, Guatemala, S803) —
  **INCLUDE**. Khan (1988, normative policy-synthesis review, Asia) —
  **EXCLUDE (E05)**. Otis et al. (2004, GIS/database permit-tracking
  tool, Minnesota) — **EXCLUDE (E01)**. Bes-Pia et al. (2010, NF
  membrane textile-effluent engineering study) — **EXCLUDE (E06)**.
  Cain, Irias & Pratt (2009, seismic safety engineering case study,
  EBMUD California) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S798-S803, 795 →
  801 rows each); `effect_sizes.csv` unchanged (38 rows; Lewis 1998
  finding judged not eligible, see above); `exclusion_log.csv` updated
  (740 → 744 rows; E01 287 → 288, E05 91 → 92, E06 60 → 62); duplicate
  audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,114 open records); schema validation re-run clean.
  Running totals: 1,545/3,659 screened (801 include/744 exclude), 2,114
  open, 801 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixtieth full-text screening batch, 10 records,
  4 includes, 6 excludes.** Kalulu & Hoko (2010, Blantyre Water Board
  performance benchmarking plus 100 low-income customer interviews on
  tariff burden/disconnection/reconnection, Malawi, S804) —
  **INCLUDE**. Begolli & Lajci (2016, consolidation of 30 municipal
  utilities into 7 Regional Water Companies via UNMIK law, independent
  regulator, Kosova, S805) — **INCLUDE**. Guimaraes, Malheiros &
  Marques (2016, land-tenure regularization as a legal barrier to
  WS&S access, SABESP connection program, Brazil, S806) —
  **INCLUDE**. Gerlach & Franceys (2009, household survey and
  regulatory-gap analysis for poor consumers, private-management
  contract, Amman Jordan, S807) — **INCLUDE**. Lagerwey (2009,
  historical missionary-nursing cleanliness discourse study) —
  **EXCLUDE (E01)**. Jimenez-Moleon & Gomez-Albores (2011, spatial-
  epidemiological GIS waterborne-disease study, Mexico) — **EXCLUDE
  (E03)**. Samwel & Gabizon (2009, urine-diverting school-toilet
  demonstration project, EECCA/EU) — **EXCLUDE (E01)**. Nabulo & Cole
  (Uganda environmental-health encyclopedia entry) — **EXCLUDE
  (E01)**. Rusca & Schwartz (2014, institutional-governance literature-
  review essay) — **EXCLUDE (E05)**. Neto & Tropp (2000, global UN
  coverage-statistics policy synthesis) — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S804-S807, 801 →
  805 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (744 → 750 rows; E01 288 → 291, E03 24 →
  25, E05 92 → 94); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,104 open records);
  schema validation re-run clean.
  Running totals: 1,555/3,659 screened (805 include/750 exclude), 2,104
  open, 805 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-first full-text screening batch, 10
  records drawn, 5 includes, 4 excludes, 1 left undecided.** Koelble &
  LiPuma (2010, 18-municipality institutional case study, enforcement
  gaps driving service-delivery failure, South Africa, S808) —
  **INCLUDE**. Hirvi & Whitfield (2015, clientelist political-
  settlement dynamics shaping private-sector-participation outcomes,
  Ghana Water Company, S809) — **INCLUDE**. Kelly-Richards & Banister
  (2017, informal land-tenure as access-control mechanism, Nogales
  Sonora colonias, S810) — **INCLUDE**. Devas (1996, provincial water
  enterprise capacity constraints, 8% coverage, informal-vendor price
  premiums, Battambang Cambodia, S811) — **INCLUDE**. Jimu (2008,
  stakeholder case study, institutional weaknesses undermining
  affordable kiosk water access, Blantyre Malawi, S812) — **INCLUDE**.
  Akosa et al. (DEA efficiency-measurement methodology paper, Ghana) —
  **EXCLUDE (E01)**. Peter & Nkambule (2012, multi-criteria rural
  water-scheme sustainability-factors analysis, Swaziland) — **EXCLUDE
  (E01)**. Petelet-Giraud et al. (2017, hydrogeological field study,
  Recife Brazil) — **EXCLUDE (E03)**. Furlong (2015, water-utility
  corporate international-expansion strategy analysis) — **EXCLUDE
  (E01)**. Olmstead (2004, "Thirsty Colonias," Land Economics) — **LEFT
  UNDECIDED**: correct file delivered but the scanned PDF's text
  extraction returned only JSTOR cover-page boilerplate, no article
  body; not a `wrong_file_retrieved` case, left open pending a future
  extraction retry.
  `extraction_database.csv`/`evidence_map.csv` updated (S808-S812, 805 →
  810 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (750 → 754 rows; E01 291 → 294, E03 25 →
  26); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,095 open records);
  schema validation re-run clean.
  Running totals: 1,564/3,659 screened (810 include/754 exclude), 2,095
  open, 810 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-second full-text screening batch, 10
  records, 8 includes, 2 excludes.** Hylton & Charles (2018, informal
  'negotiated institution' mechanisms overcoming a legal barrier to
  service extension, Sao Paulo favelas, S813) — **INCLUDE**. Costa et
  al. (2009, legally-mandated participatory water-governance
  committees, Belo Horizonte, S814) — **INCLUDE**. Bakker et al.
  (2018, unresolved Aboriginal-title water rights and fragmented
  federal/provincial governance, Canada, S815) — **INCLUDE**. Kibassa
  (2011, 145-household survey, cost-recovery-driven service reduction
  and denial of extension, Ileje Tanzania, S816) — **INCLUDE**. Wanda
  et al. (2017, absence of WASH legal framework, council/NRWB
  jurisdictional disconnect, Karonga Malawi, S817) — **INCLUDE**.
  Wanda, Gulula & Phiri (2012, 420-respondent study, discretionary
  halt on unplanned-settlement connections, Mzuzu Malawi, S818) —
  **INCLUDE**. Donoso (2017, Chile WSS tariff/concession regulatory
  framework, quantified subsidy-targeting errors, S819) —
  **INCLUDE**. Komala, Nur & Septanisa (2020, 200-household survey,
  connection-fee/tariff affordability barriers, Padang Indonesia,
  S820) — **INCLUDE**. Kolb & Williamson (2012, utility infrastructure-
  expansion cost/capacity study for new housing, Marcellus Shale
  region) — **EXCLUDE (E01)**. Alley, Barr & Mehta (2018, wastewater/
  fecal-sludge infrastructure-chain governance and manual-scavenging
  labor study, India) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S813-S820, 810 →
  818 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (754 → 756 rows; E01 294 → 296); duplicate
  audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,085 open records); schema validation re-run clean.
  Running totals: 1,574/3,659 screened (818 include/756 exclude), 2,085
  open, 818 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-third full-text screening batch, 10
  records, 5 includes, 5 excludes.** Whittington, Lauria & Mu (1991,
  seminal household/market survey, public-utility coverage gap and
  informal water-vending market, Onitsha Nigeria, S821) —
  **INCLUDE**. Nolan, Bloom & Subbaraman (2018, multilevel regression,
  2,901 slums, legal notification status strongest predictor of
  services deprivation, beta=-0.768/year p<0.001, India, S822) —
  **INCLUDE**, not added to effect_sizes.csv (composite deprivation
  outcome, not isolated to water access). Alvez Marin (2016,
  constitutional water-commodification vs. Indigenous water rights,
  Chile, S823) — **INCLUDE**. Cook & Wei (2002, government rainwater-
  harvesting programme eligibility/exclusion mechanisms, Gansu China,
  S824) — **INCLUDE**. Perumal (2011, Mazibuko prepayment-meter/Free
  Basic Water Policy litigation feminist legal analysis, South
  Africa, S825) — **INCLUDE**. Parkinson & Tayler (2003, decentralized
  wastewater technology-options review) — **EXCLUDE (E06)**. Bah
  (1992, NGO community self-help well-construction case study, Sierra
  Leone) — **EXCLUDE (E01)**. Frumkin (2005, general built-environment
  opinion editorial) — **EXCLUDE (E01)**. Moller & Radloff (2010,
  broad quality-of-life survey, South Africa) — **EXCLUDE (E01)**.
  Bartlett (2003, child-health literature-review synthesis) —
  **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S821-S825, 818 →
  823 rows each); `effect_sizes.csv` unchanged (38 rows; S822's
  regression judged not eligible, see above); `exclusion_log.csv`
  updated (756 → 761 rows; E01 296 → 299, E05 94 → 95, E06 62 → 63);
  duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,075 open records); schema validation re-run clean.
  Running totals: 1,584/3,659 screened (823 include/761 exclude), 2,075
  open, 823 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-fourth full-text screening batch, 10
  records, 4 includes, 6 excludes.** Anand (2011, ethnographic study of
  a 1995 settlement-cutoff eligibility rule and its circumvention,
  Mumbai water supply, S826) — **INCLUDE**. Schnegg & Kiaka (2019,
  Community-Based Management devolution and pricing, institutional
  breakdown, Namibia, S827) — **INCLUDE**. dos Santos et al. (2019,
  comparative six-indicator analysis of two national WatSan laws'
  tenure/housing provisions, Brazil, S828) — **INCLUDE**. Wutich et
  al. (2013, 135-interview cross-cultural study of institutional
  rules/norms in water-access justice, Bolivia/Fiji/Arizona/New
  Zealand, S829) — **INCLUDE**. Basnet (book review, Cahill-Ripley's
  Occupied Palestinian Territories water-rights book) — **EXCLUDE
  (E05)**. Ferreyra, de Loe & Kreutzwiser (2008, agricultural water-
  quality-protection governance study, Ontario) — **EXCLUDE (E01)**.
  Fontana & Elson (2014, policy-advocacy synthesis on water/ECEC
  unpaid work) — **EXCLUDE (E05)**. Hecker, Watzold & Markwardt (2020,
  spatial-econometric wastewater-policy-diffusion study, Mexico) —
  **EXCLUDE (E01)**. Young & Keil (2005, political-ecology analysis of
  Toronto's privatization debate) — **EXCLUDE (E01)**. Book review of
  Shannon & De Meulder, "Water Urbanisms 2 - East" — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S826-S829, 823 →
  827 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (761 → 767 rows; E01 299 → 302, E05 95 →
  98); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,065 open records);
  schema validation re-run clean.
  Running totals: 1,594/3,659 screened (827 include/767 exclude), 2,065
  open, 827 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-fifth full-text screening batch, 10
  records, 4 includes, 6 excludes.** Silva (2000, administrative-law
  utility-privatization analysis and qualitative connectivity
  exclusion, Sao Paulo, S830) — **INCLUDE**. Madrigal, Alpizar &
  Schluter (2011, matched comparative case study, working-rule
  determinants of community water-organization performance, Costa
  Rica, S831) — **INCLUDE**. O'Reilly & Dhanju (2012, longitudinal
  ethnographic study, payment/participation-for-accountability reform
  failure, Rajasthan, S832) — **INCLUDE**. Aladuwaka & Momsen (2010,
  formally-registered women's water organization, fee/billing/
  disconnection governance, Sri Lanka, S833) — **INCLUDE**. Hasanov
  (2009, broad civic-engagement survey, Azerbaijan) — **EXCLUDE
  (E01)**. Rao & Purkayastha (2003, fisheries common-property
  management, Assam) — **EXCLUDE (E01)**. Karim et al. (2012, water-
  development-project marital-violence study, Bangladesh) — **EXCLUDE
  (E01)**. Abers & Keck (2006, river-basin water-resource governance
  legislation politics, Brazil) — **EXCLUDE (E01)**. Earl & Czerniak
  (1996, interstate bulk-water-rights legal conflict, El Paso-New
  Mexico) — **EXCLUDE (E01)**. Bartram et al. (2014, JMP monitoring-
  methodology review) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S830-S833, 827 →
  831 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (767 → 773 rows; E01 302 → 308); duplicate
  audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,055 open records); schema validation re-run clean.
  Running totals: 1,604/3,659 screened (831 include/773 exclude), 2,055
  open, 831 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-sixth full-text screening batch, 10
  records, 4 includes, 6 excludes.** Anand (2015, companion ethnographic
  study to already-included S826, 1995 settlement-eligibility cutoff via
  failed water-audit/privatization reform, Mumbai, S834) — **INCLUDE**.
  Peda, Argento & Grossi (2013, 15-year mixed public-private
  service-contract governance case study with quantified household
  coverage/affordability outcomes, Estonia, S835) — **INCLUDE**. Valencia
  & Ecuyer (2023, documentary/policy analysis identifying absence of
  legal recognition of community water associations as a structural
  barrier, Colombian post-conflict PDET subregions, S836) — **INCLUDE**.
  Scott, Moldogaziev & Greer (2018, quantitative panel study of 500+
  special purpose water districts, hierarchical Bayesian regression on
  institutional fragmentation and capital-investment response to
  regulatory violations, Houston, S837) — **INCLUDE** (not effect_sizes
  eligible: outcome is capital investment/debt issuance, a fiscal-
  response proxy, not a water-access outcome isolated per
  PROJECT_SPEC.md Family A). Bolatova et al. (2021, school WASH
  infrastructure-condition survey, rural Kazakhstan) — **EXCLUDE
  (E01)**. Byrnes (2013, aggregate utility regulatory/efficiency-
  comparison history, Australia) — **EXCLUDE (E01)**. Berg & Mugisha
  (2010, linear-programming technology-selection optimisation study,
  Uganda) — **EXCLUDE (E06)**. Peres, Fernandes & Peres (2004,
  water-fluoridation policy-diffusion inequality study, Southern Brazil)
  — **EXCLUDE (E03)**. Hunt, Staunton & Dunstan (2013, entity-level
  user-pays pricing-mechanism adoption study, Queensland Australia) —
  **EXCLUDE (E01)**. Hagan & Kaiser (2011, water destruction as a
  genocide weapon, Darfur) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S834-S837, 831 →
  835 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (773 → 779 rows; E01 308 → 312, E03 26 →
  27, E06 63 → 64); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,045 open records);
  schema validation re-run clean.
  Running totals: 1,614/3,659 screened (835 include/779 exclude), 2,045
  open, 835 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-seventh full-text screening batch, 10
  records, 4 includes, 6 excludes.** Derman (2003, ethnographic study,
  Water Act 1998 primary/commercial water classification, Zimbabwe,
  S838) — **INCLUDE**. Odeku & Konanani (2014, independent
  legal-doctrinal Mazibuko case analysis, Free Basic Water/pre-paid
  meters, South Africa, S839) — **INCLUDE**. Grant (1955, institutional
  case study, Tennessee State Utility District Act special-district
  tariff fragmentation, Nashville, S840) — **INCLUDE**. Addai &
  Pokimica (2012, national Afrobarometer survey, isolated water-
  deprivation regression model, institutional trust, Ghana, S841) —
  **INCLUDE** (not effect_sizes eligible: exposure is subjective
  institutional trust, not a documented legal/institutional mechanism
  per PROJECT_SPEC.md Family A/B/C). Safransky (2014, water as one
  minor service category in settler-colonial Detroit planning
  analysis) — **EXCLUDE (E01)**. Punjabi (2016, IJURR book-review/
  debate forum on Bakker's Privatizing Water) — **EXCLUDE (E05)**.
  Dukhovny & Ziganshina (2011, normative global water-governance essay,
  no empirical data) — **EXCLUDE (E05)**. Heath, Parker & Weatherhead
  (2012, technical climate-adaptation engineering methodology,
  sub-Saharan Africa) — **EXCLUDE (E06)**. Gonzalez Rivas (2014,
  ethnic-fragmentation political-economy regression, no specific legal/
  institutional mechanism, Mexico) — **EXCLUDE (E01)**. Nyong &
  Kanaroglou (1999, hydrological/behavioral survey, no formal water
  institution, Katarko village, Nigeria) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S838-S841, 835 →
  839 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (779 → 785 rows; E01 312 → 315, E05 98 →
  100, E06 64 → 65); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (2,035 open records);
  schema validation re-run clean.
  Running totals: 1,624/3,659 screened (839 include/785 exclude), 2,035
  open, 839 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-eighth full-text screening batch, 10
  records, 8 includes, 2 excludes.** An unusually strong batch
  topically. Swyngedouw (1995, seminal urban-political-ecology case
  study, tariff/clientelism exclusion, Guayaquil, S842) — **INCLUDE**.
  Kooy & Walter (2019, household survey, land/tax documentation
  eligibility for piped connection, Jakarta, S843) — **INCLUDE**.
  Hordijk, Sara & Sutherland (2014, comparative institutional case
  study, water-governance decentralization, 4 cities, S844) —
  **INCLUDE**. Romero Lankao & Gunther (2011, comparative institutional
  case study, neoliberal privatization outcomes, Mexico City/Buenos
  Aires, S845) — **INCLUDE**. Ducrot, Bueno, Barban & Reydon (2010,
  participatory role-playing-game study, land tenure insecurity as
  access barrier, Sao Paulo, S846) — **INCLUDE**. Hill (2015,
  cross-sectional survey, SMS e-governance access barriers for
  vulnerable populations, Cape Town, S847) — **INCLUDE**. Hanrahan
  (2017, five case studies, Indian Act reserve system, 90-fold
  Indigenous water-access disparity, Canada, S848) — **INCLUDE**.
  Ayalew, Chenoweth, Malcolm, Mulugetta, Okotto & Pedley (2014,
  legal/regulatory research project, unregulated small independent
  water vendors, Kenya/Ethiopia, S849) — **INCLUDE**. Hutchings et al.
  (2015, secondary systematic review of 174 case studies, not primary
  research) — **EXCLUDE (E12)**. Shandra, Shandra & London (2011,
  cross-national panel regression, child mortality as sole dependent
  variable) — **EXCLUDE (E04)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S842-S849, 839 →
  847 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (785 → 787 rows; E04 60 → 61, E12 4 → 5);
  duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,025 open records); schema validation re-run clean.
  Running totals: 1,634/3,659 screened (847 include/787 exclude), 2,025
  open, 847 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-sixty-ninth full-text screening batch, 10
  records, 4 includes, 6 excludes.** Aiga & Umenai (2002, comparative
  201-household survey, Zonal Improvement Program tenure legalization
  and water connections, Manila, S850) — **INCLUDE**. Post (2014,
  comparative case study, 14 Argentine water privatization concessions,
  investor-type/coverage outcomes, S851) — **INCLUDE**. Narsiah & Ahmed
  (2012, legal-text case study, Water Services Act 1997 private-
  provider provision and municipal privatization collapses, South
  Africa, S852) — **INCLUDE**. Gomez, Perdiguero & Sanz (2019, cross-
  national panel regression, governance indicators predicting rural
  piped-water access, S853) — **INCLUDE** (not effect_sizes eligible:
  exposure is a broad perception-based governance index, not a
  documented legal/institutional mechanism per PROJECT_SPEC.md Family
  A/B/C). Blanchard-Boehm et al. (2008, Applewhite Dam referendum,
  macro-scale bulk-water infrastructure, San Antonio) — **EXCLUDE
  (E01)**. Gonzalez-Gomez & Guardiola (2009, duration model of
  municipal contracting-out decision, no access-outcome content, Spain)
  — **EXCLUDE (E01)**. Bond (2004, theoretical/polemical Essay, no
  original data) — **EXCLUDE (E05)**. Castro (2008, short Dialogue
  opinion piece, no original data) — **EXCLUDE (E05)**. Olutayo,
  Omobowale & Amzat (2009, policy-advocacy essay on secondary sources,
  Africa) — **EXCLUDE (E05)**. Adida & Girod (2011, remittances as a
  private financial substitute for state provision, Mexico) —
  **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S850-S853, 847 →
  851 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (787 → 793 rows; E01 315 → 318, E05 100 →
  103); duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (2,015 open records); schema validation re-run clean.
  Running totals: 1,644/3,659 screened (851 include/793 exclude), 2,015
  open, 851 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-seventieth full-text screening batch, 10
  records, 5 includes, 5 excludes.** Razavi (2019, doctoral-fieldwork
  case study, SEMAPA remunicipalization 'social control' participatory
  governance, Cochabamba, S854) — **INCLUDE**. Kumasi & Agbemor (2018,
  1,181-household survey vs. CWSA institutional benchmarks, Community
  Ownership and Management model, northern Ghana, S855) —
  **INCLUDE**. Spencer, Meng, Nguyen & Guzinsky (2008, four original
  institutional case studies, contractual/subsidy mechanisms, Southeast
  Asia, S856) — **INCLUDE**. Akpabio (2011, ethnographic study,
  customary land-tenure water rights vs. state cost-recovery framework,
  Nigeria, S857) — **INCLUDE**. Cleaver & Toner (2006, longitudinal
  ethnographic case study, 2002 water-policy decentralization mandate,
  Uchira Tanzania, S858) — **INCLUDE**. Grafton, Garrick, Manero & Do
  (2019, macro-scale basin-level water-resource governance framework,
  Murray-Darling/Rufiji/Colorado basins) — **EXCLUDE (E01)**. Sigler,
  Mahmoudi & Graham (2015, public-health behavior-change intervention
  methodology, CLTS) — **EXCLUDE (E01)**. Magee (2013, secondary
  literature review, rural China water politics) — **EXCLUDE (E12)**.
  Pawar (2013, conceptual framework paper on secondary data analysis,
  social work) — **EXCLUDE (E05)**. Wutich & Ragsdale (2008, outcome is
  emotional distress not water access, Bolivian squatter settlement) —
  **EXCLUDE (E04)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S854-S858, 851 →
  856 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (793 → 798 rows; E01 318 → 320, E04 61 →
  62, E05 103 → 104, E12 5 → 6); duplicate audit found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (2,005 open
  records); schema validation re-run clean.
  Running totals: 1,654/3,659 screened (856 include/798 exclude), 2,005
  open, 856 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.
- **2026-09-27, hundred-seventy-first full-text screening batch, 10
  records, 7 includes, 3 excludes.** This batch completes the original
  290-record snapshot pool. Masanyiwa, Niehof & Termeer (2015,
  mixed-methods decentralization-reform comparison, Tanzania, S859) —
  **INCLUDE**. Singh (2014, citywide poverty-mapping survey, slum
  notification/eligibility barrier, Madhya Pradesh, S860) —
  **INCLUDE**. Das & Walton (2015, survey/ethnographic study, political
  leaders navigating bureaucratic/legal processes, Delhi, S861) —
  **INCLUDE**. Galvin & Roux (2019, documentary analysis of DWS
  regulatory capture cascading to service failures, South Africa,
  S862) — **INCLUDE**. Liu Haiyan (2011, historical case study, divided
  treaty-port municipal governance, Tianjin, S863) — **INCLUDE**. Chng
  (2008, original interview-based case study, bulk-water contract
  mechanism, Manila, S864) — **INCLUDE**. Abrahams, Mhlongo & Napo
  (2011, statutory-framework review with government survey data, South
  Africa, S865) — **INCLUDE**. MacKillop & Boudreau (2008, macro-scale
  historical annexation politics, no household content, Los Angeles) —
  **EXCLUDE (E01)**. Mahon & Fernandes (2010, menstrual hygiene
  gender-health issue, not a water-access mechanism, South Asia) —
  **EXCLUDE (E01)**. Driedger, Mazur & Mistry (2014, media/focus-group
  blame-trust study of a water-quality contamination event, Walkerton
  Ontario) — **EXCLUDE (E03)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S859-S865, 856 →
  863 rows each); `effect_sizes.csv` unchanged (38 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (798 → 801 rows; E01 320 → 322, E03 27 →
  28); duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,995 open records); schema validation re-run clean.
  Running totals: 1,664/3,659 screened (863 include/801 exclude), 1,995
  open, 863 extracted studies, 38 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-second batch (10 records, 2026-09-27), first batch
  drawn from a freshly-built 68-record pool (`new_batch_pool.json`)
  assembled from the actively-growing Antigravity delivery folder (37
  already-decided duplicates found and moved to Processed without
  re-screening during pool construction).** Mwihaki (2018, 766-household
  survey comparing decentralisation types under Kenya's Water Acts,
  S866) — **INCLUDE**. Lenneiye (2000, documentary case study of
  Zimbabwe's Democratic Development Structures governing the national
  rural water/sanitation programme, S867) — **INCLUDE**. Mbanaso (1989,
  dissertation, mixed-methods structural/bureaucratic case study of
  federal fiscal constraints on Lagos-suburb water delivery, S868) —
  **INCLUDE**. Silvestre, Marques, Dollery & Correia (2022, panel GLM
  regression isolating intermunicipal sanitation-consortium cooperation
  as exposure and water/sewage coverage as outcome, Brazil, S869) —
  **INCLUDE, EFFECT_SIZES ELIGIBLE** (cooperation not significant for
  water coverage p=.494, significant for sewage coverage p=.026;
  distinguished from the S837 Houston precedent because the outcome is
  directly a coverage measure, not capital investment). Cleaver (1994,
  five-month ethnographic field report on historical state water-supply
  policy shaping present-day community participation, Nkayi Zimbabwe,
  S870) — **INCLUDE**. Ogle (1999, historical case study of municipal
  legal/financing doctrine explaining resistance to centralized
  waterworks, mid-19th-century American cities, S871) — **INCLUDE**.
  Prieto (2016, ethnographic case study of Atacameño customary rules
  subverting Chile's 1981 Water Code market framework, S872) —
  **INCLUDE**. Penn, Loring & Schnabel (2017, ethnographic
  diagnostic-framework synthesis centered on Arctic infrastructure
  engineering suitability, rural Alaska) — **EXCLUDE (E06)**. Marara,
  Palamuleni & Ebenso (2011, survey centered on acid-mine-drainage
  water-quality/contamination risk, Wonderfonteinspruit South Africa) —
  **EXCLUDE (E03)**. Huby (2001, theoretical/policy-comparative essay
  on secondary cross-national statistics, no original data) — **EXCLUDE
  (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S866-S872, 863 →
  870 rows each); `effect_sizes.csv` updated (38 → 39 rows; S869 added);
  `exclusion_log.csv` updated (801 → 804 rows; E03 28 → 29, E05 104 →
  105, E06 65 → 66); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,985 open records);
  schema validation re-run clean.
  Running totals: 1,674/3,659 screened (870 include/804 exclude), 1,985
  open, 870 extracted studies, 39 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-third batch (10 records, 2026-09-27), second batch
  from `new_batch_pool.json`.** Kim (2012, Wageningen dissertation,
  mixed-methods case study of Malaysia's 2006 WSIA/SPANA water-sector
  reform with public/private comparative performance data, S873) —
  **INCLUDE**. Morvaridi (1994, fieldwork field report on caste-based
  mediation of a formal ODA rural water-entitlement standard,
  Maharashtra India, S874) — **INCLUDE**. Hanchett, Akhter & Khan (2003,
  1,130-household matched-comparison survey of a WaterAid formal
  water-authority-connection mechanism, Dhaka/Chittagong slums, S875) —
  **INCLUDE**. Mumme & Ingram (1985, original Papago tribal-member survey
  -- 92.5% favoring collective water-rights ownership -- plus Hispanic
  acequia-community analysis documenting customary institutions resisting
  market-based water law, southwest US, S876) — **INCLUDE**. Bradshaw &
  Schafer (2000, cross-national INGO-density regression on aggregate
  water access, not a legal/institutional mechanism) — **EXCLUDE (E01)**.
  Payne, Nakato & Nabalango (2008, NGO gender-skills-training case study
  on household rainwater-tank adoption, Uganda) — **EXCLUDE (E01)**.
  Whittington, Briscoe, Mu & Barron (1990, contingent-valuation
  survey-methodology validation study, southern Haiti) — **EXCLUDE
  (E06)**. Presbey (2015, water shutoffs as one section within a broader
  Detroit bankruptcy/political-economy analysis, Safransky-Detroit
  precedent) — **EXCLUDE (E01)**. Loftus (2009, theoretical/conceptual
  political-ecology review essay on secondary literature) — **EXCLUDE
  (E05)**. Tojal Ramos dos Santos (2024, ProQuest dissertation target) —
  **WRONG_FILE_RETRIEVED**: delivered PDF was an entirely different
  dissertation (Lea Bignon, Toulouse, pharmaceutical/health-insurance
  industrial organization) with no environmental/water content; not
  screened, not moved from inbox.
  `extraction_database.csv`/`evidence_map.csv` updated (S873-S876, 870 →
  874 rows each); `effect_sizes.csv` unchanged (39 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (804 → 809 rows; E01 322 → 325, E05 105 →
  106, E06 66 → 67); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,976 open records);
  schema validation re-run clean.
  Running totals: 1,683/3,659 screened (874 include/809 exclude), 1,976
  open, 874 extracted studies, 39 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-fourth batch (10 records, 2026-09-27), third batch
  from `new_batch_pool.json`.** Miller (2000, historical case study of
  colonial-era sanitary regulation/water concession contesting
  traditional authority, Tangier, S877) — **INCLUDE**. Spronk (2007,
  comparative case study of Bolivia's capitalization-law water
  privatizations and resistance coalitions, S878) — **INCLUDE**.
  Coville, Galiani, Gertler & Yoshida (2025, RCT of utility
  contract-disconnection enforcement, Nairobi informal settlements,
  S879) — **INCLUDE, EFFECT_SIZES ELIGIBLE** (30pp increase in payment,
  p<0.001, but a precisely estimated null effect on household water
  access/connection rates at 9-month follow-up). Gero & Willetts (2020,
  multi-country qualitative study of local-government regulatory roles
  in WASH markets, Vietnam/Cambodia/Indonesia, S880) — **INCLUDE**.
  Kabogo et al. (2017, basin-scale Water Users' Associations under
  Tanzania's WRM Act -- water-resource governance, not household
  access) — **EXCLUDE (E01)**. Olivera (2001, published single-
  informant interview transcript, not an independent empirical study)
  — **EXCLUDE (E05)**. Torras (2005, cross-national power-inequality
  regression, generic exposure) — **EXCLUDE (E01)**. Coles (2009,
  reflective review essay on secondary/grey literature) — **EXCLUDE
  (E05)**. Stokman (1995, game-theoretic methodology paper on Dutch
  water-utility merger policy) — **EXCLUDE (E01)**. Griesinger & Moody
  (2001, conference rapporteur summary report) — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S877-S880, 874 →
  878 rows each); `effect_sizes.csv` updated (39 → 40 rows; S879
  added); `exclusion_log.csv` updated (809 → 815 rows; E01 325 → 328,
  E05 106 → 109); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,966 open records);
  schema validation re-run clean.
  Running totals: 1,693/3,659 screened (878 include/815 exclude), 1,966
  open, 878 extracted studies, 40 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-fifth batch (10 records, 2026-09-27), fourth batch
  from `new_batch_pool.json`; one record (RFEBA9E5C7885, Madeley
  "Tourism and water") confirmed a repeat wrong-file delivery
  (identical Arcega-Cabrera et al. cenotes microbiology paper as a
  prior attempt), notes updated, not screened.** Brown (1987, historical
  median-voter econometric model of Prussia's wealth-weighted
  electoral franchise explaining municipal waterworks investment,
  Germany 1870-1910, S881) — **INCLUDE**. Mason (2014, 396-household
  survey with regression models isolating formal BWD utility-
  connection status, Philippines, S882) — **INCLUDE, EFFECT_SIZES
  ELIGIBLE** (own connection: +27.2% consumption, +0.35 SD
  cleanliness, 2.16x odds of ease, 2.76x odds of affordability, all
  significant). Bukari, Authur & Zachary (2024, mixed-methods study of
  the gap between Ghana's National Water Policy and implicit rural
  groundwater governance, Wa West District, S883) — **INCLUDE**.
  Estache & Grifell-Tatje (2013, quantitative welfare-distribution
  decomposition of Mali's 2001 SAUR water-privatisation concession,
  finding poor rural users benefited far less than other stakeholders,
  S884) — **INCLUDE**. Torterotot et al. (2005, utility asset-
  management decision-process study for pipe rehabilitation) —
  **EXCLUDE (E06)**. Munasinghe (1991, broad World Bank policy-review
  essay on secondary statistics) — **EXCLUDE (E05)**. Satterthwaite
  (2003, statistical-methodology/policy critique essay on MDG
  statistics) — **EXCLUDE (E05)**. Syaukat & Fox (2004, hydro-economic
  optimization modeling study, Jakarta) — **EXCLUDE (E06)**. Urakami &
  Parker (2011, utility-merger cost-efficiency econometric study,
  Japan) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S881-S884, 878 →
  882 rows each); `effect_sizes.csv` updated (40 → 41 rows; S882
  added); `exclusion_log.csv` updated (815 → 820 rows; E05 109 → 111,
  E06 67 → 70); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,957 open records);
  schema validation re-run clean.
  Running totals: 1,702/3,659 screened (882 include/820 exclude), 1,957
  open, 882 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-sixth batch (10 records, 2026-09-27), fifth batch
  from `new_batch_pool.json`.** Von Schnitzler (2013, ethnographic/legal
  study of prepaid water-meter self-disconnection enforcement and the
  Mazibuko constitutional case, South Africa, S885) — **INCLUDE**.
  Brown (2010, documentary analysis of Dar es Salaam's City Water
  concession-contract termination and gendered TGNP household-survey
  data, Tanzania, S886) — **INCLUDE**. Marcos (2024, five-city
  comparative case study of institutional fragmentation under a shared
  legal framework, Zamboanga Peninsula Philippines, S887) —
  **INCLUDE**. Kornberg (2016, FOIA-based archival case study of DWSD
  infrastructure financing and racialized regional water-governance
  conflict, Detroit, S888) — **INCLUDE**. Hasna (1995, participatory
  action-research case study of CWASA street-hydrant institutional
  practices and community Water-Committee formation, Chittagong,
  S889) — **INCLUDE**. Mohanty & Rout (2020, utility O&M cost-recovery
  regression study, not a water-access mechanism, eastern India) —
  **EXCLUDE (E06)**. Vintges et al. (2026, Gaza war-zone humanitarian
  blockade study, water denial as weapon of war) — **EXCLUDE (E01)**.
  Rondinelli (1991, conceptual policy synthesis on secondary
  evaluations, no original fieldwork) — **EXCLUDE (E05)**. Hope (2013,
  Swaziland SWAP assessment across 4 sectors, water SWAP "not
  functioning") — **EXCLUDE (E01)**. Olmstead (2004, "Thirsty
  colonias") — **UNDECIDED**: delivered PDF is entirely JSTOR
  boilerplate with no article text, a content-extraction failure
  (Batch 161 precedent); left open, not moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S885-S889, 882 →
  887 rows each); `effect_sizes.csv` unchanged (41 rows; no regression-
  based estimate met the strict Family A/B/C criteria this batch);
  `exclusion_log.csv` updated (820 → 824 rows; E01 328 → 330, E05 111 →
  112, E06 70 → 71); duplicate audit found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,948 open records);
  schema validation re-run clean.
  Running totals: 1,711/3,659 screened (887 include/824 exclude), 1,948
  open, 887 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-seventh batch (10 records, 2026-09-27), sixth batch
  from `new_batch_pool.json`.** Aleixo et al. (2016, 232-household
  survey of within-community water-access inequality under Brazil's
  PLANSAB legal framework, Cristais, Brazil, S890) — **INCLUDE**.
  Bellaubi & Boehm (2018, multi-case-study principal-agent analysis of
  regulatory-capture/political-opportunism/state-capture corruption
  risks in water service delivery, Kenya and Ghana, S891) —
  **INCLUDE**. Truelove (2018, ethnographic/documentary analysis of
  state water-measurement bureaucratic practices as a mechanism
  producing distributive water-access injustice, Delhi, S892) —
  **INCLUDE**. Jocoy (2000, chi-square/Mann-Whitney statistical
  analysis of PENNVEST Safe Drinking Water Act aid-allocation data
  showing systematic under-service of the smallest water systems,
  Pennsylvania, S893) — **INCLUDE**. Anzera et al. (2016, household
  survey linking the 1995 Oslo Agreement Joint Water Committee
  bilateral allocation regime to constrained Palestinian household
  water access, Palestine and Tunisia, S894) — **INCLUDE**.
  Satterthwaite (2016, MDG statistical-methodology critique, same
  author as the Batch 175 exclusion) — **EXCLUDE (E05)**. Kundu (2000,
  water as one of several "basic amenities" in a broad India
  poverty-trends analysis) — **EXCLUDE (E01)**. Dos Santos et al.
  (2017, explicitly labeled "Review" article, sub-Saharan Africa urban
  water access) — **EXCLUDE (E12)**. Boardman (2010, confirmed via
  full-text read to concern Mexican biosimilar-drug regulation, zero
  water content despite exact title/author match, a corpus-inclusion
  error) — **EXCLUDE (E01)**. Li et al. (2009, confirmed via full-text
  read to be a purely agronomic dryland-crop-nutrition book chapter,
  China, a corpus-inclusion error) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S890-S894, 887 →
  892 rows each); `effect_sizes.csv` unchanged (41 rows; all five
  includes are qualitative/descriptive or, for Jocoy, exposure-side
  mismatched -- water-system size is not itself a documented
  legal/institutional mechanism -- so none met the strict Family A/B/C
  criteria this batch); `exclusion_log.csv` updated (824 → 829 rows;
  E01 330 → 333, E05 112 → 113, E12 6 → 7); duplicate audit (exact-DOI
  + study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,938 open records); schema validation re-run clean.
  Running totals: 1,721/3,659 screened (892 include/829 exclude), 1,938
  open, 892 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-eighth batch (10 records, 2026-09-27), first batch
  from a new, much larger pool.** A bulk delivery of 552 unique PDFs
  arrived across the Drive inbox and Antigravity folders; reconciled
  against `full_text_screening_database.csv` (0 already-decided
  duplicates, 9 already flagged `wrong_file_retrieved`/`undecided`
  left untouched, 543 genuinely open records saved as the new
  `new_batch_pool.json`). This batch is `new_batch_pool.json[0:10]`.
  Kotsila & Saravanan (2017, mixed-methods fieldwork on state WSS
  success narratives obscuring unequal access, Mekong Delta Vietnam,
  S895) — **INCLUDE**. Crow, Swallow & Asamba (2012, comparative field
  study of household connection-status effects under Kenya's Water Act
  2002, Nyando basin, S896) — **INCLUDE**. Whittington (1992, household
  survey/regression showing Kumasi's increasing-block-tariff structure
  regressively burdens shared-connection households, Ghana, S897) —
  **INCLUDE**. Monstadt & Schramm (2017, field-based documentary
  analysis of formal planning institutions vs. hybrid unequal access,
  Dar es Salaam, S898) — **INCLUDE**. Nyarko, Oduro-Kwarteng &
  Owusu-Antwi (2011, comparative case study of 5 water systems under
  Ghana's Local Government Act 462, S899) — **INCLUDE**. Tiwale (2019,
  socio-technical field study of institutional/regulatory governance
  producing differentiated network access, Lilongwe Malawi, S900) —
  **INCLUDE**. Van Vugt (2001, social-psychology study of household
  water-conservation behavior, UK, not an access-mechanism study) —
  **EXCLUDE (E01)**. Devkar, Mahalingam, Deep & Thillairajan (2013,
  self-labeled "a systematic review" of PSP across electricity/
  telecom/water) — **EXCLUDE (E12)**. Arlosoroff et al. (1988, World
  Bank/UNDP handpump-technology engineering report) — **EXCLUDE
  (E06)**. Nimoh, Poku, Ohene-Yankyera, Konradsen & Abaidoo (2014,
  supply-side small-business economics of sanitation service
  providers, Ghana, not household access barriers) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S895-S900, 892 →
  898 rows each); `effect_sizes.csv` unchanged (41 rows; all six
  includes are qualitative/documentary/case-study designs, or, for
  Whittington, exposure-side mismatched -- households-sharing-a-
  connection is a housing-density variable, not itself the
  institutional tariff mechanism -- so none met the strict Family
  A/B/C criteria this batch); `exclusion_log.csv` updated (829 → 833
  rows; E01 333 → 335, E06 71 → 72, E12 7 → 8); duplicate audit
  (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,928 open records);
  schema validation re-run clean.
  Running totals: 1,731/3,659 screened (898 include/833 exclude), 1,928
  open, 898 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-seventy-ninth batch (10 records, 2026-09-27), second batch
  from the 543-record pool.** `new_batch_pool.json[10:20]`. Larrain
  (2012, documentary/statistical analysis of Chile's 1981 Water Code
  and post-privatization rate/coverage outcomes, S901) — **INCLUDE**.
  Avidar (2018, mixed-methods analysis of Kenya's 2010 devolution
  reform and Water Acts 2002/2016, Siaya County, S902) — **INCLUDE**.
  Allison (2002, multiple-case study of CBO/local-government sanitation
  governance under South Africa's bill-of-rights framework, Cape Town,
  S903) — **INCLUDE**. Wahby (2021, two-case-study ethnography of
  state/informal water-governance arrangements, Cairo, S904) —
  **INCLUDE**. Akumuntu, Wehn, Mulenga & Brdanovic (2017, case study of
  government institutional/regulatory constraints on sustainable FSM
  access, Kigali Rwanda, S905) — **INCLUDE**. Bond (2000, water is one
  of three illustrative topics in a broader political-economy
  discourse essay, South Africa) — **EXCLUDE (E01)**. Frenoux &
  Tsitsikalis (2015, market-efficiency framing of Cambodia's private
  FSM operator market, distinguished from Akumuntu's institutional
  framing) — **EXCLUDE (E01)**. Ranganathan (2016, confirmed via
  full-text read as a self-framed theoretical essay on Flint with no
  original data collection) — **EXCLUDE (E05)**. Vivekanandan (2009,
  confirmed via full-text read to concern India's nanotechnology
  health sector with water mentioned only in passing, a
  corpus-inclusion error) — **EXCLUDE (E01)**. Hoko & Hertle (2006,
  technical M&E study of an NGO borehole-rehabilitation project's
  breakdown rates and pump functionality, Zimbabwe) — **EXCLUDE
  (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S901-S905, 898 →
  903 rows each); `effect_sizes.csv` unchanged (41 rows; all five
  includes are documentary/case-study/ethnographic designs, no
  regression-based estimate); `exclusion_log.csv` updated (833 → 838
  rows; E01 335 → 338, E05 113 → 114); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,918 open records); schema validation re-run clean.
  Running totals: 1,741/3,659 screened (903 include/838 exclude), 1,918
  open, 903 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eightieth batch (10 records, 2026-09-27), third batch from
  the 543-record pool.** `new_batch_pool.json[20:30]`. Nizkorodov
  (2021, comparative case study of 10 Southern California water PPPs'
  risk-allocation design, S906) — **INCLUDE**. Saleth & Sastry (2004,
  documentary/financial analysis of Karnataka's coverage-criteria
  policy and subsidy dynamics, S907) — **INCLUDE**. Alzahrani (2019,
  three-essay econometric dissertation on SDWA violations, boil-water
  notices, and West Virginia's Source Water Protection Act, S908) —
  **INCLUDE** (Essay 3's SB 373/water-charges regression considered
  for effect_sizes but not added, consistent with the Whittington S897
  precedent). Adams, Braune, Cobbing, Fourie & Riemann (2015,
  documentary analysis of South Africa's National Water Act 1998
  groundwater reclassification and 20-year coverage gains, S909) —
  **INCLUDE**. Kundu (2014, documentary/statistical analysis of
  JnNURM's city-size-based water-investment disparities, S910) —
  **INCLUDE**. Hazarika & Nitivattananon (2016, household survey
  linking Guwahati's groundwater/land-rights legal linkage to
  household water access, S911) — **INCLUDE**. O'Toole (1989,
  confirmed via full-text read as a public-administration
  implementation-theory study using EPA wastewater-treatment-plant
  privatization, not household access) — **EXCLUDE (E07)**. Jimenez &
  Perez-Foguet (2011, Water Point Mapping technical
  functionality-decay study, Tanzania) — **EXCLUDE (E06)**. Guragai,
  Takizawa, Hashimoto & Oguma (2017, intermittent-supply
  reliability/water-quality engineering study, Kathmandu) — **EXCLUDE
  (E06)**. Salmoral, Zegarra, Vazquez-Rowe et al. (2020, water-food-
  energy-land nexus resource-governance stakeholder study, Arequipa
  Peru) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S906-S911, 903 →
  909 rows each); `effect_sizes.csv` unchanged (41 rows); `exclusion_log.csv`
  updated (838 → 842 rows; E01 338 → 339, E06 73 → 75, E07 21 → 22);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,908 open records);
  schema validation re-run clean.
  Running totals: 1,751/3,659 screened (909 include/842 exclude), 1,908
  open, 909 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-first batch (10 records, 2026-09-27), fourth batch
  from the 543-record pool.** `new_batch_pool.json[30:40]`. Hossain
  (2012, ethnographic case study of Dhaka bosti utility negotiation
  under formal non-recognition, S912) — **INCLUDE**. Baud &
  Dhanalakshmi (2007, comparative 2-municipality multi-stakeholder
  sewerage-governance case study, Chennai, S913) — **INCLUDE**. Dugard
  (2011, documentary/legal analysis of South Africa's constitutional
  water-rights framework vs. municipal service-delivery reality, S914)
  — **INCLUDE**. Gopakumar (2014, qualitative case study of a
  Bengaluru water-supply PPP pilot and resident counter-mobilization,
  S915) — **INCLUDE**. Toure, Kane, Noel, Turmine, Nedeff & Lazar
  (2012, GIS-based household survey linking the 1995 Senegalese
  water-sector reform to connection/affordability outcomes, Mbour,
  S916) — **INCLUDE**. Crane (1994, household survey on Jakarta's
  April 1990 water-resale deregulation measure, S917) — **INCLUDE**.
  van Steenbergen (1995, basin-scale groundwater-management-regime
  analysis, Balochistan Pakistan) — **EXCLUDE (E01)**. Isunju, Orach
  & Kemp (2016, environmental-vulnerability/livelihood-adaptation
  study, water a minor topic, Kampala wetlands) — **EXCLUDE (E01)**.
  Rehan, Knight, Haas & Unger (2011, System Dynamics utility financial-
  modeling methodology paper, Canada) — **EXCLUDE (E06)**. "Ecology
  in Public Health" (Kiss 2005) — **WRONG_FILE_RETRIEVED**: confirmed
  via full-text read that the delivered PDF is an unrelated 2025 PRRSV
  swine-virus One Health veterinary review; flagged, not screened, not
  moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S912-S917, 909 →
  915 rows each); `effect_sizes.csv` unchanged (41 rows);
  `exclusion_log.csv` updated (842 → 845 rows; E01 339 → 341, E06 75 →
  76); duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,899 open records;
  R99433B75F8E9 remains open/wrong_file_retrieved); schema validation
  re-run clean.
  Running totals: 1,760/3,659 screened (915 include/845 exclude), 1,899
  open, 915 extracted studies, 41 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-second batch (10 records, 2026-09-27), fifth batch
  from the 543-record pool.** `new_batch_pool.json[40:50]`.
  Martinez-Espineira, Garcia-Valinas & Gonzalez-Gomez (2012, econometric
  analysis of unjustified water-price disparities under a decentralized/
  unregulated tariff framework, Spanish cities, S918) — **INCLUDE**.
  Peal, Evans, Blackett, Hawkins & Heymans (2014, comparative 12-city
  FSM institutional scoring, S919) — **INCLUDE**. Barde (2017,
  difference-in-differences/kernel-matching isolating water-user-
  association vs. local-government management effects on rural
  piped-water access, Brazil, S920) — **INCLUDE**, added to
  `effect_sizes.csv` (Family A, first new row since Batch 175). Biddle
  & Baehler (2019, two-case process-tracing of NYC vs. Flint under the
  Safe Drinking Water Act's polycentric federalism, S921) —
  **INCLUDE**. Rachwal (2007, documentary/historical analysis of the
  UK's 1989 privatisation legal framework's household-bill and
  disconnection-protection effects, S922) — **INCLUDE**. Wride, Chen
  & Johnstone (2004, rainfall-measurement engineering methodology,
  Cincinnati) — **EXCLUDE (E06)**. Humphries et al. (2011, pure
  ecohydrology/geochemistry wetland study, South Africa, corpus error)
  — **EXCLUDE (E01)**. Grimes (2012, conceptual UWAF framework paper
  with desk-based illustrative application) — **EXCLUDE (E05)**. Obani
  (2017, confirmed via full-text read as a self-described literature
  review) — **EXCLUDE (E12)**. Harvey (2007, technical tariff-
  hierarchy/cost-calculation planning-tool methodology paper) —
  **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S918-S922, 915 →
  920 rows each); `effect_sizes.csv` updated (41 → 42 rows; S920
  added); `exclusion_log.csv` updated (845 → 850 rows; E01 341 → 342,
  E05 114 → 115, E06 76 → 78, E12 8 → 9); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,889 open records); schema validation re-run clean.
  Running totals: 1,770/3,659 screened (920 include/850 exclude), 1,889
  open, 920 extracted studies, 42 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-third batch (10 records, 2026-09-27), sixth batch
  from the 543-record pool.** `new_batch_pool.json[50:60]`. Reynaud
  (2010, instrumental-variable econometric analysis of PSP/delegation-
  contract effects on household water-affordability under France's 1992
  RMI water-access law, S923) — **INCLUDE**. Furlong (2012, documentary
  case study of 30+ years of Ontario water-sector regulatory reform,
  including post-Walkerton Safe Drinking Water Act 2002/Clean Water Act
  2006 reregulation, S924) — **INCLUDE**. Zaato & Ohemeng (2015,
  original 9-interview case study of Ghana Water Company Limited's
  organizational-autonomy reform, S925) — **INCLUDE**. Vijay & Ghosh
  (2018, institutional/programmatic case study of Nadia District's
  Sabar Shouchagar sanitation program with quantified before/after
  coverage outcomes, India, S926) — **INCLUDE**. Roth (2008, ten-year
  anthropological case study of municipal decision-making over
  extending a watermain to 64 contaminated-well households, Central
  Saanich, British Columbia, S927) — **INCLUDE**. Shah & Narain (2019,
  self-labeled Geoforum "Review" section conceptual argument piece
  synthesizing secondary literature only) — **EXCLUDE (E12)**. Bazoglu
  (2011, UN-HABITAT 52-119-city urban-growth typology with piped-water
  access as one of several infrastructure indicators) — **EXCLUDE
  (E01)**. Tapela (2002, basin/catchment-scale water-resources
  allocation and interstate governance study, Zimbabwe/Mozambique
  Pungwe-Mutare project) — **EXCLUDE (E01)**. Roncoli, Dowd-Uribe,
  Orlove, West & Sanon (2016, Burkina Faso water user committee whose
  core function is an irrigation allocation plan among agro-industrial
  users and farmers, not household access) — **EXCLUDE (E01)**;
  initially screened INCLUDE on preview, corrected to EXCLUDE after
  full-text reading, before extraction. Dinpanah & Lashgarara (2008,
  general agricultural/natural-resource sustainability conceptual
  model, Iran, water tangential) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S923-S927, 920 →
  925 rows each); `effect_sizes.csv` unchanged (42 rows: none of this
  batch's includes are effect_sizes eligible — qualitative case studies,
  or a clean regression on a water-affordability outcome that does not
  map to Family A/B/C per the established Whittington/Alzahrani
  precedent); `exclusion_log.csv` updated (850 → 855 rows; E01 342 →
  346, E12 9 → 10); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,879 open
  records); schema validation re-run clean.
  Running totals: 1,780/3,659 screened (925 include/855 exclude), 1,879
  open, 925 extracted studies, 42 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-fourth batch (10 records, 2026-09-27), seventh batch
  from the 543-record pool.** `new_batch_pool.json[60:70]`.
  Golooba-Mutebi (2012, comparative ethnographic fieldwork on
  decentralization/PPP water-provision institutions, Rwanda & Uganda,
  S928) — **INCLUDE**. Obeta (2018, investigative/qualitative study of
  institutional policy-gaps behind rural water-scheme failure, Nigeria,
  S929) — **INCLUDE**. Diaz-Cayeros, Magaloni & Ruiz-Euler (2014,
  kernel-matching quasi-experimental design isolating the 1995 Oaxaca
  usos y costumbres legal-recognition reform's effect on sewerage
  access, Mexico, S930) — **INCLUDE**, added to `effect_sizes.csv`
  (Family A, sanitation_access outcome). Mallick (2010, participatory
  action-research project linking community-government institutional
  links to drinking-water/sanitation access gains, Bangladesh, S931) —
  **INCLUDE**. Brocklehurst (2014, descriptive coding of 307 stated
  political commitments at a global partnership meeting, no evidence of
  actual institutional-mechanism effects) — **EXCLUDE (E05)**.
  Scodanibbio & Manez (2005, basin-scale dam-operation/water-resources
  governance study of downstream livelihoods, Lower Zambezi Mozambique)
  — **EXCLUDE (E01)**. Huby (1995, self-labeled review of UK water-
  poverty issues, no original data collection) — **EXCLUDE (E12)**.
  Parsa, Nakendo, McCluskey & Page (2011, land-tenure/credit-access
  formalization study, Dar es Salaam, water/sanitation a brief
  background mention only) — **EXCLUDE (E01)**. Kefeni & Yallew (2018,
  cross-sectional survey of behavioral/environmental determinants of
  latrine use among households with existing access, Addis Ababa) —
  **EXCLUDE (E01)**. Salman, Al-Karablieh & Haddadin (2008, household
  water-demand price/income-elasticity econometrics among already-
  connected households, Jordan) — **EXCLUDE (E04)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S928-S931, 925 →
  929 rows each); `effect_sizes.csv` updated (42 → 43 rows; S930 added,
  Family A, sanitation_access outcome); `exclusion_log.csv` updated
  (855 → 861 rows; E01 346 → 349, E04 62 → 63, E05 115 → 116, E12 10 →
  11); duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,869 open records);
  schema validation re-run clean.
  Running totals: 1,790/3,659 screened (929 include/861 exclude), 1,869
  open, 929 extracted studies, 43 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-fifth batch (10 records, 2026-09-27), eighth batch
  from the 543-record pool.** `new_batch_pool.json[70:80]`. Guidi
  Gutierrez, Gonzalez Gomez & Guardiola (2013, documentary institutional
  case study diagnosing water-governance-framework gaps as the root
  cause of service-delivery conflict, Sucre Bolivia, S932) —
  **INCLUDE**. Smith (2011, four-year multi-city implementation study of
  institutional fragmentation constraining citizen accountability for
  water services, South Africa, S933) — **INCLUDE**. Rama Mohan (2003,
  documentary/policy analysis of India's rural water-management
  institutional shift with NGO case studies, S934) — **INCLUDE**.
  Hellberg (2014, original 2008/2009 narrative-interview fieldwork on
  eThekwini's differentiated water-service technologies, South Africa,
  S935) — **INCLUDE**. Blase, Green & Matson (1973, mail-survey
  before/after study of Missouri Public Water Supply District formation
  effects on household connection/consumption/land values, S936) —
  **INCLUDE**. de Carvalho, Costa, Marques & Netto (2019, MCDA
  regulatory impact assessment of household wastewater-connection
  policy options under Brazilian legal connection mandates, S937) —
  **INCLUDE**. Hirano (2016, doctrinal global-administrative-law
  analysis of World Bank Inspection Panel/investment arbitration, no
  original empirical data) — **EXCLUDE (E05)**. Lawanson & Fadare (2013,
  comparative household survey of general socioeconomic/environmental-
  health disparities, Lagos, water one of several indicators) —
  **EXCLUDE (E01)**. Rowles et al (2021, structural-equation-model
  water-quality/health study, Texas colonias) — **EXCLUDE (E06)**.
  Fuller, Goldstick, Bartram & Eisenberg (2016, statistical monitoring-
  methodology paper for JMP global drinking-water/sanitation trends) —
  **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S932-S937, 929 →
  935 rows each); `effect_sizes.csv` unchanged (43 rows: no eligible
  regression-based estimates this batch); `exclusion_log.csv` updated
  (861 → 865 rows; E01 349 → 350, E06 78 → 80); duplicate audit
  (exact-DOI + study_id) found no new duplicates; `full_text_retrieval_
  queue.csv` regenerated (1,859 open records); schema validation
  re-run clean.
  Running totals: 1,800/3,659 screened (935 include/865 exclude), 1,859
  open, 935 extracted studies, 43 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-sixth batch (10 records, 2026-09-27), ninth batch
  from the 543-record pool.** `new_batch_pool.json[80:90]`. Bontianti,
  Hungerford, Younsa & Noma (2014, neighborhood-scale comparative
  fieldwork on Niger's 2001 PPP water-reform effects on two disadvantaged
  Niamey neighborhoods, S938) — **INCLUDE**. Pierce & Gonzalez (2017,
  mixed-methods content-analysis/administrative-data study of California
  mobile-home-park water access under the state's legislated Human Right
  to Water, S939) — **INCLUDE**. Muchadenyika (2015, case study of the
  Harare Slum Upgrading Programme's incremental water/sanitation-access
  institutional structure, Zimbabwe, S940) — **INCLUDE**. Gutierrez
  (2007, documentary analysis of water/sanitation under-prioritization
  within Malawi's and Zambia's Poverty Reduction Strategy Papers, S941)
  — **INCLUDE**. Lele, Madhyastha, Sulagna, Dhavamani & Srinivasan (2018,
  four-town comparative study of municipal vs. para-statal institutional
  water-governance arrangements, south India, S942) — **INCLUDE**. Liu,
  Brown, Demargne & Seo (2011, hydrologic-forecasting wavelet-based
  timing-error methodology paper) — **EXCLUDE (E06)**. Mancilla Garcia &
  Bodin (2019, basin-scale participatory water-resource-council
  inclusion-dynamics study, Peru/Brazil, zero household-water mentions)
  — **EXCLUDE (E01)**. Thompson (2016, feminist-geography intersectionality
  conceptual framework paper with secondary-literature illustrative case
  studies) — **EXCLUDE (E05)**. Batley (2006, editorial preface
  introducing a journal symposium, not a primary study) — **EXCLUDE
  (E12)**. Crocker, Shields, Venkataramanan, Saywell & Bartram (2016,
  CLTS management-training evaluation study, Kenya, outcome is trainee
  performance not household access) — **EXCLUDE (E04)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S938-S942, 935 →
  940 rows each); `effect_sizes.csv` unchanged (43 rows: no eligible
  regression-based estimates this batch); `exclusion_log.csv` updated
  (865 → 870 rows; E01 350 → 351, E04 63 → 64, E05 117 → 118, E06 80 →
  81, E12 11 → 12); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,849 open
  records); schema validation re-run clean.
  Running totals: 1,810/3,659 screened (940 include/870 exclude), 1,849
  open, 940 extracted studies, 43 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-seventh batch (10 records, 2026-09-27), tenth batch
  from the 543-record pool.** `new_batch_pool.json[90:100]`. Cobbing,
  Eales, Gibson, Lenkoe & Cobbing (2015, multi-province interview study
  linking institutional O&M capacity to domestic groundwater reliability,
  South Africa, S943) — **INCLUDE**. Johnson, Parnell, Joyner, Christman
  & Marsh (2004, GIS-based case study of ETJ/annexation/zoning-driven
  race-differentiated sewer-service denial, Mebane NC, S944) —
  **INCLUDE**. Bassi & Kabir (2016, 850-household 12-scheme comparative
  institutional performance study, rural Maharashtra India, S945) —
  **INCLUDE**. Boex, Malik, Brookins, Edwards & Zaidi (2020, 18-city
  comparative institutional assessment of intergovernmental authority
  structures, South/Southeast Asia, S946) — **INCLUDE**. Tadadjeu,
  Njangang, Ningaye & Nourou (2020, 44-country dynamic-panel GMM
  regression showing regulation quality raises water/sanitation access
  and narrows the urban-rural gap, Africa, S947) — **INCLUDE**, added to
  `effect_sizes.csv` (Family C). Kujinga, Vanderpost, Mmopelwa & Wolski
  (2013, mixed-methods study linking gazetted/ungazetted settlement
  legal status to household water security, Ngamiland Botswana, S948) —
  **INCLUDE**. Jaffee (2018, literature-synthesis book chapter on water
  privatization/commodification, no original data) — **EXCLUDE (E12)**.
  Harutyunyan (2014, Armenia water-metering consumption/demand-
  elasticity study) — **EXCLUDE (E04)**. Pailla (2011, engineering
  capacity-assessment decision-support-tool paper, Nalgonda India) —
  **EXCLUDE (E06)**. Roy, Sowgat, Islam & Anjum (2020, broad Dhaka
  urban-sprawl sustainability study, water/sanitation minor topic) —
  **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S943-S948, 940 →
  946 rows each); `effect_sizes.csv` updated (43 → 44 rows; S947 added,
  Family C, regulation-quality/access-inequality outcome);
  `exclusion_log.csv` updated (870 → 874 rows; E01 351 → 352, E04 64 →
  65, E06 81 → 82, E12 12 → 13); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,839 open records); schema validation re-run clean.
  Running totals: 1,820/3,659 screened (946 include/874 exclude), 1,839
  open, 946 extracted studies, 44 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-eighth batch (10 records, 2026-09-27), eleventh batch
  from the 543-record pool.** `new_batch_pool.json[100:110]`.
  Nelson-Nunez, Walters & Charpentier (2019, Delphi study assessing
  Chile's Law No. 20.998 rural water-governance reform, S949) —
  **INCLUDE**. O'Reilly & Dhanju (2014, longitudinal ethnography of
  caste-differentiated water access via village governance institutions,
  Rajasthan India, S950) — **INCLUDE**. Ennis-McMillan (2001,
  ethnography with local water-official interviews on community water-
  governance and access hardship, Mexico, S951) — **INCLUDE**. Rammelt,
  Masud, Boes & Masud (2014, NGO program-implementation case study on
  arsenic-affected communities' water access, Bangladesh, S952) —
  **INCLUDE**. De & Nag (2016, household survey with logit regression
  linking slum notification legal status and ethnicity to water-
  accountability outcomes, Kolkata India, S953) — **INCLUDE**. Reddy &
  Batchelor (2012, life-cycle cost approach financial-methodology paper,
  Andhra Pradesh) — **EXCLUDE (E06)**. O'Connell & Devine (2015,
  SaniFOAM behavioral-determinants study of latrine ownership) —
  **EXCLUDE (E01)**. Ray & Shaw (2016, desk-based resilience-framework
  application to Kolkata using secondary data, no original fieldwork) —
  **EXCLUDE (E05)**. Baruah (2010, NGO slum-electrification study,
  wrong service) — **EXCLUDE (E07)**. Mitra & Pool (2000, broad gender/
  urban-poverty study, water/sanitation a minor topic) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S949-S953, 946 →
  951 rows each); `effect_sizes.csv` unchanged (44 rows: S953's
  regression outcome is accountability perception, not a direct access
  outcome under Family A/B/C); `exclusion_log.csv` updated (874 → 879
  rows; E01 352 → 354, E05 118 → 119, E06 82 → 83, E07 22 → 23);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,829 open records);
  schema validation re-run clean.
  Running totals: 1,830/3,659 screened (951 include/879 exclude), 1,829
  open, 951 extracted studies, 44 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-eighty-ninth batch (10 records, 2026-09-27), twelfth batch
  from the 543-record pool.** `new_batch_pool.json[110:120]`. Mwendera
  (2006, government-commissioned institutional assessment of Swaziland's
  RWSS budget-allocation/community-governance structure, S954) —
  **INCLUDE**. Monney, Baffoe-Kyeremeh & Amissah-Reynolds (2015,
  400-respondent mixed-methods study of local-assembly institutional
  constraints on rural sanitation coverage, Ghana, S955) — **INCLUDE**.
  Tantoh & McKay (2021, Cultural Theory/Systems Thinking assessment of
  decentralization-law vs. centralized water control, North-West
  Cameroon, S956) — **INCLUDE**. Rydhagen (2002, interview-based
  fieldwork on gender-differentiated participation in water/sanitation
  decision-making, Vioolsdrif South Africa, S957) — **INCLUDE**. Carrera
  & Flowers (2018, documentary case study of sanitation-law enforcement
  and heir-property tenure producing racial sanitation-access denial,
  Lowndes County Alabama, S958) — **INCLUDE**. Hossain (2011, empirical
  case study of informal regulatory institutions in a Dhaka bosti, S959)
  — **INCLUDE**. Beck (2018, self-labeled "Advanced Review" literature-
  synthesis article on Water Operator Partnerships) — **EXCLUDE (E12)**.
  Arvai & Post (2012, structured decision-making study for point-of-use
  water-treatment technology choice, Tanzania) — **EXCLUDE (E06)**.
  Park & Visvanathan (2018, comparative engineering study of drinking-
  water treatment-technology trajectories) — **EXCLUDE (E06)**. Rey
  (2003, "Framework for action") — **WRONG_FILE_RETRIEVED**: delivered
  PDF is unrelated 2026 BJPsych Open mental-health conference abstracts,
  Wales; flagged, not screened, Drive file left untouched.
  `extraction_database.csv`/`evidence_map.csv` updated (S954-S959, 951 →
  957 rows each); `effect_sizes.csv` unchanged (44 rows: no eligible
  estimates this batch); `exclusion_log.csv` updated (879 → 882 rows;
  E06 83 → 85, E12 13 → 14); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,820 open records, including the wrong_file_retrieved record left
  undecided); schema validation re-run clean.
  Running totals: 1,839/3,659 screened (957 include/882 exclude), 1,820
  open, 957 extracted studies, 44 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninetieth batch (10 records, 2026-09-27), thirteenth batch
  from the 543-record pool.** `new_batch_pool.json[120:130]`. Narzetti &
  Marques (2021, PIR documentary case study of Brazilian WSS legal
  reform and isomorphic mimicry driving peri-urban/rural access
  exclusion, S960) — **INCLUDE**. Kachenje (2019, qualitative case study
  of a community-based Water Committee's 3-6 day connection processing
  vs. ~4 weeks under the comparator public system, Dar es Salaam, S961)
  — **INCLUDE**. Rusca, Alda-Vidal & Kooy (2018, interview-based case
  study tracing Uganda's 1997 sanitation-devolution reform to persistent
  access inequality, Kampala, S962) — **INCLUDE**. Nastar & Ramasar
  (2012, interview-based case study and litigation tracing of the Phiri
  pre-paid water-meter case through South African courts, Johannesburg,
  S963) — **INCLUDE**. Laurie & Crespo (2007, mixed-methods case study
  and regulatory/contract analysis of the La Paz-El Alto "pro-poor"
  concession's densification-inflated coverage claims, Bolivia, S964) —
  **INCLUDE**. Walkinshaw, Hecht, Patel & Podrabsky (2019, photo-
  evidence citizen-science feasibility study of school water-fountain
  condition) — **EXCLUDE (E06)**. Parker, Kirkpatrick &
  Figueira-Theodorakopoulou (2008, self-described literature review of
  infrastructure regulation and poverty across multiple sectors) —
  **EXCLUDE (E12)**. Naghibi-Beidokhti & Lence (2005, engineering/
  hydrogeology optimization study of manganese/iron removal for
  Fredericton, NB groundwater supply) — **EXCLUDE (E06)**. Robinson et
  al. (2004, conservation-biology study of bird distribution in the
  Panama Canal corridor, zero water-access content) — **EXCLUDE (E01)**,
  corpus-inclusion error. Vasquez (2013, hedonic-price analysis of
  households' willingness-to-pay for water connections under different
  governance types, Guatemala) — **EXCLUDE (E04)**, wrong outcome
  (economic valuation, not an access outcome).
  `extraction_database.csv`/`evidence_map.csv` updated (S960-S964, 957 →
  962 rows each); `effect_sizes.csv` unchanged (44 rows: no eligible
  estimates this batch); `exclusion_log.csv` updated (882 → 887 rows;
  E01 354 → 355, E04 65 → 66, E06 85 → 87, E12 14 → 15); duplicate audit
  (exact-DOI + study_id) found no new duplicates; `full_text_retrieval_
  queue.csv` regenerated (1,810 open records); schema validation re-run
  clean.
  Running totals: 1,849/3,659 screened (962 include/887 exclude), 1,810
  open, 962 extracted studies, 44 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-first batch (10 records, 2026-09-27), fourteenth
  batch from the 543-record pool.** `new_batch_pool.json[130:140]`.
  Nakyagaba et al (2021, ethnographic case study of KCCA regulatory
  legitimization of gulper pit-emptying sanitation technology, Kampala,
  S965) — **INCLUDE**. Jimenez, Mtango & Cairncross (2014, PGPE analysis
  of district-council institutional constraints on the National
  Sanitation Campaign, Tanzania, S966) — **INCLUDE**. Balazs & Lubell
  (2014, case study of California Water Code-mandated disadvantaged-
  community participation in regional water planning, S967) —
  **INCLUDE**. Lea (2008, ethnographic case study of institutional
  funding fragmentation and bureaucratic racial bias in Indigenous
  Australian water/sanitation infrastructure, S968) — **INCLUDE**. Njoh
  & Akiwumi (2011, cross-national OLS regression, colonial-era
  governance duration significantly predicting urban water/sanitation
  access across 43 African countries, S969) — **INCLUDE**, added to
  `effect_sizes.csv` (Family A). Terhorst, Olivera & Dwinell (2013,
  comparative case study of constitutional water-rights reforms and
  their limited institutional implementation, Uruguay/Bolivia/Ecuador,
  S970) — **INCLUDE**. Spaling, Brouwer & Njoka (2014, case study of
  Kenya's Water Act 2002 compliance and community-governance capacity
  threatening water-supply sustainability, S971) — **INCLUDE**. Lin &
  Berg (2008, technical DEA/Malmquist-index benchmarking study of Peru
  water-utility productivity) — **EXCLUDE (E06)**. Aubin (2011, general
  water-resource-rivalry typology, Belgium/Switzerland) — **EXCLUDE
  (E01)**. Kubler & Schwab (2007, Swiss metropolitan governance across
  four co-equal policy sectors including water supply, outcome is
  democratic accountability not water access) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S965-S971, 962 →
  969 rows each); `effect_sizes.csv` updated (44 → 45 rows: S969 added);
  `exclusion_log.csv` updated (887 → 890 rows; E01 355 → 357, E06 87 →
  88); duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,800 open records);
  schema validation re-run clean.
  Running totals: 1,859/3,659 screened (969 include/890 exclude), 1,800
  open, 969 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-second batch (10 records, 2026-09-27), fifteenth
  batch from the 543-record pool.** `new_batch_pool.json[140:150]`.
  Ponder & Omstedt (2019, documentary case study of interest rate swap
  debt and federal-court/emergency-manager mechanisms driving mass
  racially disparate household water shutoffs, Detroit, S972) —
  **INCLUDE**. Danesi, Passarelli & Peruzzi (2007, policy/institutional
  analysis of Italy's Galli Law utility-aggregation reform and tariff
  affordability, S973) — **INCLUDE**. Kacker & Joshi (2016, qualitative
  case study of legal-status transitions in informal-settlement water
  provision improving access/affordability, Sangam Vihar New Delhi,
  S974) — **INCLUDE**. March & Sauri (2013, documentary analysis of EU
  directives and Catalan water-financing design driving tariff increases
  and reduced public participation, Barcelona, S975) — **INCLUDE**.
  Ludwig (2000, book review of a World Bank wastewater-management
  brochure) — **EXCLUDE (E12)**. Stoler (2017, self-labeled WIREs Water
  "Advanced Review" of sachet drinking water in West Africa) — **EXCLUDE
  (E12)**. Taddei (2011, basin-committee reservoir water-allocation
  governance study, Northeast Brazil) — **EXCLUDE (E01)**. Xie et al
  (2011, technical chance-constrained programming model for industrial
  water quality, China) — **EXCLUDE (E06)**. Lockie, Momtaz & Taylor
  (1999, Social Impact Assessment methodology study for an industrial
  dam project, Australia) — **EXCLUDE (E01)**. Kudebayeva (2010, general
  rural-poverty logit-regression study, Kazakhstan, water one of several
  covariates) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S972-S975, 969 →
  973 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch); `exclusion_log.csv` updated (890 → 896 rows;
  E01 357 → 360, E06 88 → 89, E12 15 → 17); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,790 open records); schema validation re-run clean.
  Running totals: 1,869/3,659 screened (973 include/896 exclude), 1,790
  open, 973 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-third batch (10 records, 2026-09-27), sixteenth
  batch from the 543-record pool.** `new_batch_pool.json[150:160]`.
  Mwenge Kahinda, Taigbenu & Boroto (2007, legal/policy review of
  domestic rainwater harvesting's ambiguous/illegal status under South
  Africa's National Water Act and Water Services Act, plus the DWAF
  Pilot Programme financial-assistance mechanism, S976) — **INCLUDE**.
  Bolaane & Ikgopoleng (2011, empirical household-survey study of the
  Major Village Infrastructure Programme's cost-recovery design and
  income barriers to waterborne-sewerage uptake, Botswana, S977) —
  **INCLUDE**. Osumanu, Zumayelleh & Kosoe (2022, mixed-methods case
  study of community-management institutional structure lifting potable
  water access from 38% to 97%, Upper West Region, Ghana, S978) —
  **INCLUDE**. El-Jazairi (2017, legal analysis of Palestinian Water Law
  No. 3, Oslo II jurisdictional fragmentation, and occupying-power
  obligations under international humanitarian law constraining
  realisation of the right to water, occupied Palestinian territory,
  S979) — **INCLUDE**. Cobbinah, Kosoe & Diawuo (2020, household-survey
  study of urban-planning-regime enforcement distortions inhibiting
  in-house toilet provision, Wa municipality, Ghana, S980) —
  **INCLUDE**. Furlong (2021, WIREs Water article explicitly labeled
  "OPINION," argumentative synthesis with no original empirical data
  collection) — **EXCLUDE (E05)**. Mbereko, Scott & Chimbari (2016,
  HIV/AIDS-water-scarcity health/caregiving dialectic and stigma-driven
  social exclusion as the primary analytical focus, Zimbabwe Water
  Act/Catchment Council content contextual only, Nyamakate) — **EXCLUDE
  (E01)**. String & Lantagne (2016, self-labeled systematic review of
  Water Safety Plan outcomes, a water-quality/engineering topic distinct
  from legal/institutional access mechanisms) — **EXCLUDE (E12)**.
  Nallathiga (2006, general institutional-reform overview of Mumbai's
  water-sector supply/tariff efficiency, not household-access
  inequality) — **EXCLUDE (E01)**. Kumasi, Obiri-Danso & Ephraim (2010,
  catchment/watershed conservation study of community attitudes toward
  upstream land degradation, Barekese, Ghana, not household water
  access) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S976-S980, 973 →
  978 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch — all five includes are qualitative/descriptive,
  none report a regression-based estimate isolating a legal/institutional
  mechanism's effect); `exclusion_log.csv` updated (896 → 901 rows;
  E01 360 → 363, E05 119 → 120, E12 17 → 18); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,780 open records); schema validation re-run clean.
  Running totals: 1,879/3,659 screened (978 include/901 exclude), 1,780
  open, 978 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-fourth batch (10 records, 2026-09-27), seventeenth
  batch from the 543-record pool.** `new_batch_pool.json[160:170]`.
  Molinos-Senante (2018, book chapter on Chile's Law 382/Law 70 tariff-
  setting reforms and Law 18,778 subsidy system for vulnerable
  households, S981) — **INCLUDE**. Dismas, Mulungu & Mtalo (2018,
  household survey of rainwater-harvesting adoption under Tanzania's
  Water Resources Management Act 2009 permit exemption and municipal
  building-permit bylaws, Kinondoni, S982) — **INCLUDE**. Irshad (2013,
  field survey of World Bank/JBIC-funded institutional reform shifting
  Kerala Water Authority from subsidized to cost-recovery community
  provision, S983) — **INCLUDE**. ElDidi & Corbera (2017, qualitative
  case study of charitable water wells/property-rights institutions
  under Egypt's 1984 Irrigation and Drainage Law, Nile Delta, S984) —
  **INCLUDE**. Matros-Goreses & Franceys (2008, interview study of
  Namibia's politically-driven tariff price-setting process and its
  affordability consequences for the urban poor, Windhoek, S985) —
  **INCLUDE**. Bisung et al (2015, photovoice ecosocial/health-geography
  study, Kenya) — **EXCLUDE (E01)**. Long et al (2013, anthropological
  water-values/chemical-contamination study, Ghanaian gold-mining
  community) — **EXCLUDE (E01)**. Hamed & Sannen (1993, technical/
  financial engineering planning report, Fayoum Egypt) — **EXCLUDE
  (E06)**. Zhuang, Fang & Ji (2021, program-implementation-factor
  regression study for urine-diverting dry toilets, rural China) —
  **EXCLUDE (E01)**. Herrala & Haapasalo (2012, SWOT-analysis comparison
  of public waterworks governance/ownership models on efficiency
  grounds, Finland) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S981-S985, 978 →
  983 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch — all five includes are qualitative/descriptive,
  none report a regression-based estimate isolating a legal/institutional
  mechanism's effect); `exclusion_log.csv` updated (901 → 906 rows;
  E01 363 → 367, E06 89 → 90); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,770 open records); schema validation re-run clean.
  Running totals: 1,889/3,659 screened (983 include/906 exclude), 1,770
  open, 983 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-fifth batch (10 records, 2026-09-27), eighteenth
  batch from the 543-record pool.** `new_batch_pool.json[170:180]`.
  Lovei & Whittington (1993, institutional-economic framework and
  numerical modeling of rent-extracting behavior by government
  officials, utility staff and licensed public-tap operators/vendors
  restricting household connections and inflating vended-water prices,
  Jakarta, S986) — **INCLUDE**. Ducrot (2017, field study of water-
  committee leadership/governance quality determining borehole
  sustainability under Mozambique's National Rural Water Supply and
  Sanitation Program, S987) — **INCLUDE**. Rout (2014, comparative
  field study of two institutional arrangements implementing India's
  Demand Responsive Approach reform, finding it reinforced existing
  water-access inequality, Odisha, S988) — **INCLUDE**. Andersen (2016,
  ethnographic study of Peru's Water Law 29338 basin-scale irrigation-
  rights redistribution among farmers, mining and urban users, Arequipa)
  — **EXCLUDE (E01)**. Molinos-Senante et al (2016, DEA technical-
  efficiency benchmarking of water companies, England and Wales) —
  **EXCLUDE (E06)**. Stiegler (2000, Journal AWWA legal case-note
  column summarizing three utility-law court decisions) — **EXCLUDE
  (E12)**. Crum (2005, book review of Troesken's "Water, Race, and
  Disease") — **EXCLUDE (E12)**. Madhoo (2007, self-labeled cross-
  country survey/taxonomy of water-utility-regime reforms) — **EXCLUDE
  (E12)**. Oduro-Kwarteng, Monney & Braimah (2015, human-resources
  capacity/workforce-staffing study of Ghana's WASH sector) — **EXCLUDE
  (E01)**. Cross & Morel (2005, World Bank WSP-Africa proposed pro-poor
  work-program document, no original empirical data) — **EXCLUDE
  (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S986-S988, 983 →
  986 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch — all three includes are qualitative/descriptive
  or theoretical-modeling studies, none report a regression-based
  estimate isolating a legal/institutional mechanism's effect);
  `exclusion_log.csv` updated (906 → 913 rows; E01 367 → 369, E05 120 →
  121, E06 90 → 91, E12 18 → 21); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,760 open records); schema validation re-run clean.
  Running totals: 1,899/3,659 screened (986 include/913 exclude), 1,760
  open, 986 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-sixth batch (10 records, 2026-09-27), nineteenth
  batch from the 543-record pool.** `new_batch_pool.json[180:190]`.
  Gimelli, Rogers & Bos (2018, qualitative case study of legal
  notification status and Bombay High Court PIL/Article 21 litigation
  shaping informal settlers' water access, India, S989) — **INCLUDE**.
  Giglioli & Swyngedouw (2008, historical/political-economy case study
  of Mafia-linked institutional capture producing documented water-
  interruption disparities for the poor, Sicily's 2002 crisis, S990) —
  **INCLUDE**. Nelson et al (2022, qualitative study of statutorily-
  mandated village water committee governance and gender dynamics,
  Fiji, S991) — **INCLUDE**. Harvey (2017, Uganda WASH program case
  study of regulatory structure, PPP contracts, and new legal status/
  by-laws for community water-management committees, S992) —
  **INCLUDE**. Chidya, Mulwafu & Banda (2016, mixed-methods study of
  informal water-provider dynamics under Malawi's Water Works Act 1995,
  Lilongwe low-income areas, S993) — **INCLUDE**. Behailu, Hukka &
  Katko (2017, field study diagnosing local-government institutional
  incapability as the primary driver of rural water-scheme failures,
  Ethiopia, S994) — **INCLUDE**. Ching, Yishu, Rajoo & Tan (2019,
  psychological "paradox of resilience" narrative study, Kathmandu) —
  **EXCLUDE (E01)**. Fry, Mihelcic & Watkins (2008, cross-national
  statistical/geospatial modeling of governance-index correlates of
  sanitation coverage) — **EXCLUDE (E01)**. Planas (1991, conceptual
  seminar essay on Latin American water-utility O&M obstacles, no
  original empirical data) — **EXCLUDE (E05)**. Jewell & Wutich (2011,
  ethnography/economic-experiment study of religiosity and prosocial
  water-sharing norms, Bolivia) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S989-S994, 986 →
  992 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch — all six includes are qualitative/descriptive
  case studies, none report a regression-based estimate isolating a
  legal/institutional mechanism's effect); `exclusion_log.csv` updated
  (913 → 917 rows; E01 369 → 372, E05 121 → 122); duplicate audit
  (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,750 open records);
  schema validation re-run clean.
  Running totals: 1,909/3,659 screened (992 include/917 exclude), 1,750
  open, 992 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-seventh batch (10 records, 2026-09-27), twentieth
  batch from the 543-record pool.** `new_batch_pool.json[190:200]`.
  Mustafa & Reeder (2009, ethnographic study of failed water-supply
  privatization -- tariff increases, disconnection rates -- Belize
  City, S995) — **INCLUDE**. Scott, Cotton & Khan (2013, household
  study of de facto tenure security shaping sanitation-investment
  decisions, Dakar, S996) — **INCLUDE**. Vibhu & James (2010, project
  policy analysis of flexible O&M tariff-collection institutional
  design improving rural water-supply sustainability, Tamil Nadu,
  S997) — **INCLUDE**. Jackson & Barber (2013, legal/institutional
  analysis of Australia's National Water Initiative/Native Title Act
  and indigenous water-entitlement inequity, Northern Territory, S998)
  — **INCLUDE**. Subbaraman & Murthy (2015, legal analysis of notified/
  non-notified slum status and the 2014 Bombay High Court PIL Article
  21 right-to-water ruling, Mumbai, S999) — **INCLUDE**. Tempelhoff
  (2021, historical/environmental narrative of Emfuleni wastewater
  infrastructure collapse, Vaal River, South Africa) — **EXCLUDE
  (E01)**. Mishra & Ray (2013, broad composite multi-dimensional
  deprivation index study, India) — **EXCLUDE (E01)**. Butala,
  VanRooyen & Patel (2010, quasi-experimental regression of slum-
  upgrading intervention on waterborne-illness health-insurance
  claims, Ahmedabad) — **EXCLUDE (E04)**. Welle, Schaefer, Butterworth
  & Bostoen (2012, political-economy analysis of WASH inventory data-
  monitoring-system governance, Ethiopia) — **EXCLUDE (E01)**. Kurland
  & Zell (2011, naturological business-ethics case study of a
  California utility rate-regulation proceeding) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S995-S999, 992
  → 997 rows each); `effect_sizes.csv` unchanged (45 rows: no eligible
  estimates this batch — all five includes are qualitative/descriptive
  studies, none report a regression-based estimate isolating a legal/
  institutional mechanism's effect); `exclusion_log.csv` updated (917
  → 922 rows; E01 372 → 376, E04 66 → 67); duplicate audit (exact-DOI
  + study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,740 open records); schema validation re-run clean.
  Running totals: 1,919/3,659 screened (997 include/922 exclude), 1,740
  open, 997 extracted studies, 45 effect_sizes rows. Full detail in
  `CHANGELOG.md`.

- **Hundred-ninety-eighth batch (10 records, 2026-09-27), twenty-first
  batch from the 543-record pool.** `new_batch_pool.json[200:210]`.
  Bakker, Kooy, Shofiani & Martijn (2008, mixed-methods "governance
  failure" study of utility/household institutional disincentives to
  connect poor households, Jakarta, S1000) — **INCLUDE**. Kooy &
  Bakker (2008, archival/historical study of colonial-era institutional
  citizenship classification producing persistent fragmented water
  access, Jakarta, S1001) — **INCLUDE**. Statman-Weil, Nanus &
  Wilkinson (2020, regression study of disparities in Safe Drinking
  Water Act compliance by system size/rurality, Pennsylvania, S1002) —
  **INCLUDE**. Anand (2007, comparative cross-country study testing
  whether legal right-to-water promulgation improves access via
  Hohfeldian framework and governance indicators, S1003) —
  **INCLUDE**. Pinto, Da Cruz & Marques (2015, comparative case study
  of PPP/public-public water-utility contract design quality,
  Portugal) — **EXCLUDE (E01)**. Daniere & Takahashi (1999,
  socioeconomic-determinants-of-access measurement study, Bangkok
  slums) — **EXCLUDE (E01)**. Gupta, Ahlers & Ahmed (2010, theoretical/
  doctrinal argument on UN human-right-to-water resolution and PPP-to-
  NGO partnership shift) — **EXCLUDE (E05)**. Criqui (2015, urban-
  planning theory of infrastructure-extension mechanisms for water and
  electricity, Delhi/Lima) — **EXCLUDE (E01)**. Gandy (2006, historical/
  political-economy essay on general multi-sector infrastructure
  crisis, Lagos) — **EXCLUDE (E01)**. Devkar, Thillai Rajan, Narayanan
  & Elayaraja (2019, self-labeled systematic review of slum basic-
  service provision approaches) — **EXCLUDE (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1000-S1003,
  997 → 1,001 rows each); `effect_sizes.csv` unchanged (45 rows: no
  eligible estimates this batch — all four includes are qualitative/
  descriptive or comparative-secondary-data studies, none report a
  regression-based estimate isolating a legal/institutional mechanism's
  effect on a Family A/B/C water-access outcome); `exclusion_log.csv`
  updated (922 → 928 rows; E01 376 → 380, E05 122 → 123, E12 21 → 22);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,730 open records);
  schema validation re-run clean.
  Running totals: 1,929/3,659 screened (1,001 include/928 exclude),
  1,730 open, 1,001 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Hundred-ninety-ninth batch (10 records, 2026-09-27), twenty-second
  batch from the 543-record pool.** `new_batch_pool.json[210:220]`.
  Rusca, Boakye-Ansah, Loftus, Ferrero & van der Zaag (2017,
  interdisciplinary political-ecology study finding Waterworks Act
  statutory disconnection authority and utility governance decisions
  produce laboratory-measured water-quality disparities by income area,
  Lilongwe, Malawi, S1004) — **INCLUDE**. Matsinhe, Juízo, Macheve &
  dos Santos (2008, field-survey study finding the delegated-management
  regulatory framework does not extend to informal water resellers/
  SSIPs, who serve 32-45% of unconnected peri-urban residents at
  unregulated higher prices, Maputo, Mozambique, S1005) — **INCLUDE**.
  Torres-Rouff (2006, historical case study finding the legal
  transition from communal pueblo water rights to individual-property/
  special-assessment doctrine structurally excluded Mexican and Chinese
  neighbourhoods from 19th-century sewer infrastructure, Los Angeles,
  S1006) — **INCLUDE**. Fisher (2008, discourse/media analysis of the
  Tagbilaran privatization-legitimacy debate as an election issue,
  Philippines) — **EXCLUDE (E01)**. Derman & Ferguson (2003, Zimbabwe
  Water Act 1998/catchment-council study of irrigation/agricultural/
  mining water-permit allocation) — **EXCLUDE (E01)**. Clark & Mondello
  (2003, theoretical real-options economic model of delegation-contract
  pricing, France) — **EXCLUDE (E01)**. Sutton (2017, technical/
  financial-planning review of sub-Saharan rural water-supply coverage
  strategy and Self-supply cost-benchmarking) — **EXCLUDE (E06)**.
  Estache & Iimi (2011, econometric auction-theory analysis of
  procurement bundling/bidder cost structure for water and sewage
  projects) — **EXCLUDE (E06)**. Mitra (2008, Foucauldian
  policy-discourse analysis of the Hubli-Dharwad 24x7 pilot project's
  "lifestyle vs. lifeline" narrative framing, Karnataka, India) —
  **EXCLUDE (E01)**. One record (target: Pu 2024, "Amplifying the
  Poverty-Alleviation Impacts of Water Infrastructure Investments in
  Sub-Saharan Africa") flagged **wrong_file_retrieved**: the delivered
  PDF was an unrelated 2015 drought-tolerant-maize adoption study by a
  different author team; not screened, not moved, needs re-retrieval.
  `extraction_database.csv`/`evidence_map.csv` updated (S1004-S1006,
  1,001 → 1,004 rows each); `effect_sizes.csv` unchanged (45 rows: all
  three includes are qualitative/mixed-methods or historical case
  studies, none report a regression-based estimate isolating a legal/
  institutional mechanism's effect on a Family A/B/C water-access
  outcome); `exclusion_log.csv` updated (928 → 934 rows; E01 380 → 384,
  E06 91 → 93); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,721 open
  records); schema validation re-run clean.
  Running totals: 1,938/3,659 screened (1,004 include/934 exclude),
  1,721 open, 1,004 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundredth batch (10 records, 2026-09-27), twenty-third batch
  from the 543-record pool.** `new_batch_pool.json[220:230]`. Gomes &
  Hermans (2018, institutional-change case study finding WATSAN
  licensing discretion versus successful constitutional/statutory legal
  challenge determined divergent groundwater-access outcomes across two
  peri-urban communities, Khulna, Bangladesh, S1007) — **INCLUDE**.
  Morales & Zambrano (2018, mixed-methods survey/wastewater-sampling
  study finding informal tenure and eviction risk discourage sanitation
  investment, corroborated by DBO5 sampling, Costa Rica, S1008) —
  **INCLUDE**. Das (2016, cross-case comparative study finding
  decentralization-law-based governance arrangements produced divergent
  water-connection/cost-recovery outcomes across three otherwise
  comparable Indian cities, S1009) — **INCLUDE**. Zekri (2008, E01
  Oman agricultural groundwater-abstraction quota/subsidy study for
  irrigation) — **EXCLUDE (E01)**. Mkondiwa, Jumbe & Wiyo (2013, E01
  Canonical Correlation Analysis of poverty-water access, rural Malawi)
  — **EXCLUDE (E01)**. Massarutto & Ermano (2013, E01 national
  regulatory-design critique of Italy's 1994 water reform, no
  documented access-inequality mechanism) — **EXCLUDE (E01)**. Adams,
  Boateng & Amoyaw (2015, E01 GLM regression of socioeconomic
  predictors of water/sanitation access, Ghana DHS data) — **EXCLUDE
  (E01)**. McKay & Bjornlund (2001, E01 broad review of Australian
  COAG water-reform instruments across rural irrigation markets and
  urban pricing) — **EXCLUDE (E01)**. Musembi (2014, E05
  normative/doctrinal argument on participation as a human right, no
  original empirical data) — **EXCLUDE (E05)**. Kohlitz, Chong &
  Willetts (2016, E01 document-analysis of HRWS-monitoring policy
  design across 13 Pacific island countries) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1007-S1009,
  1,004 → 1,007 rows each); `effect_sizes.csv` unchanged (45 rows: all
  three includes are qualitative/mixed-methods comparative case
  studies, none report a regression-based estimate isolating a legal/
  institutional mechanism's effect on a Family A/B/C water-access
  outcome); `exclusion_log.csv` updated (934 → 941 rows; E01 384 → 390,
  E05 123 → 124); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,711 open
  records); schema validation re-run clean.
  Running totals: 1,948/3,659 screened (1,007 include/941 exclude),
  1,711 open, 1,007 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-first batch (10 records, 2026-09-27), twenty-fourth
  batch from the 543-record pool.** `new_batch_pool.json[230:240]`.
  Sarkar (2019, mixed-methods case study finding weak Water Act 2002
  tariff-enforcement and tribal favouritism at Mathare slum standpipes
  produce documented price disparities, traced to a colonial Vagrancy
  Act legacy, Nairobi, Kenya, S1010) — **INCLUDE**. Romano (2012,
  qualitative case study finding decades of non-recognition and
  eventual legal recognition (Special CAPS Law 722) of community water
  committees serving over 1 million rural Nicaraguans, S1011) —
  **INCLUDE**. Almebo et al (2021, E01 behavioral-determinants study of
  fluoride-filter-technology utilization, Ethiopia) — **EXCLUDE
  (E01)**. Sharma (2009, E01 historical water-reservoir/architecture
  study, pre-modern India) — **EXCLUDE (E01)**. Dobyns (1952, E01
  anthropological narrative of well-introduction among the Tohono
  O'odham) — **EXCLUDE (E01)**. Okumura et al (2021, E01 City Blueprint
  governance-capacity benchmarking-tool application, Rio de Janeiro) —
  **EXCLUDE (E01)**. Andajani-Sutjahjo, Chirawatkul & Saito (2015, E01
  qualitative gender study of domestic water burden/governance
  participation, Northeast Thailand) — **EXCLUDE (E01)**. Zakiya (2014,
  E05 reflective practitioner essay on endogenous-development praxis,
  Ghana) — **EXCLUDE (E05)**. Schories (2008, E06 membrane-bioreactor
  wastewater-treatment engineering pilot) — **EXCLUDE (E06)**. Vasquez
  & Adams (2019, E01 discrete-choice-experiment willingness-to-pay
  study for standpipe attributes, Accra, Ghana) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1010-S1011,
  1,007 → 1,009 rows each); `effect_sizes.csv` unchanged (45 rows: both
  includes are qualitative/mixed-methods case studies, none report a
  regression-based estimate isolating a legal/institutional mechanism's
  effect on a Family A/B/C water-access outcome); `exclusion_log.csv`
  updated (941 → 949 rows; E01 390 → 396, E05 124 → 125, E06 93 → 94);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,701 open records);
  schema validation re-run clean.
  Running totals: 1,958/3,659 screened (1,009 include/949 exclude),
  1,701 open, 1,009 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-second batch (10 records, 2026-09-27), twenty-fifth
  batch from the 543-record pool.** `new_batch_pool.json[240:250]`.
  Ruiz Rosado (2008, case study finding SEDALIB's institutional water-
  rationing policy and Comite de Agua committee gatekeeping produce
  documented price disparities up to 16.6x network tariff, Trujillo,
  Peru, S1012) — **INCLUDE**. Ratner & Rivera Gutierrez (2004,
  action-research case study finding a municipal sewage-connection
  legal-eligibility requirement (later relaxed) plus a negotiated
  differentiated fee schedule and alley-committee collective-connection
  mechanism directly producing measured connection-rate increases,
  Panajachel, Guatemala, S1013) — **INCLUDE**. Yntiso (2008, E01 broad
  multi-domain urban-resettlement-impact study, water access a minor
  sub-finding among six impact domains, Addis Ababa) — **EXCLUDE
  (E01)**. Patel et al (2010, E01 school beverage/nutrition-policy
  barriers study, California) — **EXCLUDE (E01)**. Ndesamburo, Flynn &
  French (2012, E05 reflective NGO practitioner case study, Tanzania) —
  **EXCLUDE (E05)**. Cleaver & Hamada (E05 conceptual/analytical
  framework paper synthesizing secondary case examples, no original
  empirical data) — **EXCLUDE (E05)**. Kapuria (2013, E01 multi-service
  fuzzy-sets quality-of-life index study, water one of seven domains,
  Delhi) — **EXCLUDE (E01)**. Chang et al (2020, E01 City Blueprint
  Approach governance-capacity benchmarking study, 32 Chinese cities) —
  **EXCLUDE (E01)**. Kolesar & Serio (2011, E01 basin-scale interstate
  reservoir-release operations-research study, Delaware River) —
  **EXCLUDE (E01)**. Chaudhuri et al (2020, E01 nationwide
  state-aggregated statistical appraisal of RWSS coverage performance,
  India) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1012-S1013,
  1,009 → 1,011 rows each); `effect_sizes.csv` unchanged (45 rows: both
  includes are qualitative/action-research case studies, none report a
  regression-based estimate isolating a legal/institutional mechanism's
  effect on a Family A/B/C water-access outcome); `exclusion_log.csv`
  updated (949 → 957 rows; E01 396 → 402, E05 125 → 127); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,691 open records);
  schema validation re-run clean.
  Running totals: 1,968/3,659 screened (1,011 include/957 exclude),
  1,691 open, 1,011 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-third batch (10 records, 2026-09-27), twenty-sixth
  batch from the 543-record pool.** `new_batch_pool.json[250:260]`.
  Gowlland-Gualtieri (2010, doctrinal/policy analysis finding
  disconnection and pre-paid-meter mechanisms under South Africa's
  Water Services Act directly deprive poor households of the Free
  Basic Water entitlement, documented via case law including Mazibuko/
  Phiri litigation, S1014) — **INCLUDE**. Njoh (2011, comparative case
  study finding a formalized differentiated connection-fee structure
  directly tied to divergent success/failure outcomes across two
  Cameroonian community water projects, S1015) — **INCLUDE**. Muller
  (2008, policy-evaluation study finding pre-payment tariff mechanisms
  produced severe under-consumption before, and South Africa's 2001
  Free Basic Water policy improved access after, documented via the
  Shemula kiosk sub-case and national coverage statistics, S1016) —
  **INCLUDE**. Zlolniski (2011, ethnographic case study finding
  Mexico's 1992 National Water Law's differential agribusiness/
  domestic subsidy structure and CESPE tariff/quota policies directly
  producing measured price and access disparities in Baja California,
  S1017) — **INCLUDE**. Ormerod & Scott (2013, E01 public-trust/
  technology-acceptance survey for potable reuse, Tucson) — **EXCLUDE
  (E01)**. Ibem (2013, E01 multi-service accessibility survey, public
  housing, Ogun State Nigeria) — **EXCLUDE (E01)**. Meinzen-Dick &
  Pradhan (2001, E05 conceptual legal-pluralism article with secondary
  case examples, no original empirical data) — **EXCLUDE (E05)**.
  Lopez Porras, Stringer & Quinn (2019, E01 agricultural/watershed
  governance study, Rio del Carmen, Mexico) — **EXCLUDE (E01)**.
  Bisung et al (2014, E01 social-capital-theory application study,
  rural Kenya) — **EXCLUDE (E01)**. McGeough (2013, E12 performance-
  studies/rhetorical analysis of Indian toilet festivals) — **EXCLUDE
  (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1014-S1017,
  1,011 → 1,015 rows each); `effect_sizes.csv` unchanged (45 rows: all
  four includes are doctrinal/policy-evaluation or qualitative case
  studies, none report a regression-based estimate isolating a legal/
  institutional mechanism's effect on a Family A/B/C water-access
  outcome); `exclusion_log.csv` updated (957 → 963 rows; E01 402 → 406,
  E05 127 → 128, E12 22 → 23); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,681 open records); schema validation re-run clean.
  Running totals: 1,978/3,659 screened (1,015 include/963 exclude),
  1,681 open, 1,015 extracted studies, 45 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-fourth batch (10 records, 2026-09-27), twenty-seventh
  batch from the 543-record pool.** `new_batch_pool.json[260:270]`.
  Mogomotsi, Mogomotsi & Matlhola (2018, new-institutional-economics
  review finding Botswana's Water Act 1968 borehole-permission regime,
  absent a justiciable right to water, was used per the Mosetlhanyane/
  Sesana case law to deny indigenous Basarwa/San residents of the
  Central Kalahari Game Reserve water access as a coercive relocation
  tool, S1018) — **INCLUDE**. Fischer (2021, mixed-methods study
  finding India's MGNREGA decentralized-planning mechanism improved
  water access in 79% of 251 water-related interventions across a
  798-project dataset, benefits skewed toward marginalized groups,
  Himachal Pradesh, S1019) — **INCLUDE**. Hope (2007, propensity-score-
  matched evaluation finding a government watershed-development
  intervention increased domestic water collection time by 17.37
  min/day on average with heterogeneous effects by income and social
  group, Madhya Pradesh, S1020) — **INCLUDE, added to effect_sizes.csv
  (Family A)**. Zerah (2008, historical-institutional analysis finding
  the 1888 Bombay Municipal Corporation Act and notified/non-notified
  slum eligibility classification tied to documented differential
  water-access outcomes, Mumbai, S1021) — **INCLUDE**. Bardosh (2015,
  E01 behavioral/participatory CLTS sanitation-programme ethnography,
  Zambia) — **EXCLUDE (E01)**. Romero Lankao (2010, E01 climate-hazard/
  flood-drought vulnerability study, Mexico City) — **EXCLUDE (E01)**.
  Ilahi & Grimard (2000, E01 econometric infrastructure-quality/time-
  allocation study, rural Pakistan) — **EXCLUDE (E01)**. Nkwocha (2009,
  E01 general water-scarcity-impact survey, Niger-Delta Nigeria) —
  **EXCLUDE (E01)**. Poonia & Punia (2018, E01 macro-level district-
  scale AHP spatial-index study, India) — **EXCLUDE (E01)**. Adegun
  (2015, E07 stormwater-drainage/flood-management study, wrong service,
  Johannesburg) — **EXCLUDE (E07)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1018-S1021,
  1,015 → 1,019 rows each); `effect_sizes.csv` updated (45 → 46 rows:
  S1020 added, a propensity-score-matched estimate isolating a legal/
  institutional mechanism's effect on a Family A water-access outcome);
  `exclusion_log.csv` updated (963 → 969 rows; E01 406 → 411, E07
  23 → 24); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,671 open
  records); schema validation re-run clean.
  Running totals: 1,988/3,659 screened (1,019 include/969 exclude),
  1,671 open, 1,019 extracted studies, 46 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-fifth batch (10 records, 2026-09-27), twenty-eighth
  batch from the 543-record pool.** `new_batch_pool.json[270:280]`.
  Drew (2008, case study finding India's 73rd/74th Constitutional
  Amendments empowering panchayats over groundwater directly enabled a
  court-ordered closure of Coca-Cola's water-mining operation in
  Plachimada, Kerala, S1022) — **INCLUDE**. Loftus (2007, political-
  ecology study with 20 interviews finding Durban's differentiated
  ground-tank connections and tiered tariffs tied to differential
  payment burdens, S1023) — **INCLUDE**. Driessen (2008, case study of
  Cochabamba SEMAPA's post-Water-War participatory-governance model,
  elite capture vs. Southern Zone service expansion, S1024) —
  **INCLUDE**. Tardanico (2008, regression study finding dwelling-title
  status and water-service-establishment status predict municipal
  service-coverage deficits, San Salvador, n=1,243, S1025) —
  **INCLUDE**. Anand (2004, case study finding Chennai's unaccountable
  Metro Water Board institutional structure coincides with 31% of
  households lacking secure water entitlements despite official 90%+
  access statistics, S1026) — **INCLUDE**. Alston & Mason (2008, E01
  gender-composition-of-water-boards study, Murray-Darling Basin
  Australia) — **EXCLUDE (E01)**. Rahaman, Everett & Neu (2013, E01
  business-ethics/trust analysis of Ghana privatization) — **EXCLUDE
  (E01)**. Douglas (2016, E01 general Public Value Management study
  across mixed Caribbean utilities) — **EXCLUDE (E01)**. Gondhalekar et
  al (2013, E01 water-scarcity/health study, Leh Ladakh India) —
  **EXCLUDE (E01)**. Meinzen-Dick & Bakker (1999, E01 agricultural/
  irrigation multiple-use-commons study, Sri Lanka) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1022-S1026,
  1,019 → 1,024 rows each); `effect_sizes.csv` unchanged (46 rows: no
  confirmed regression-based estimate isolating a legal/institutional
  mechanism's effect on a Family A/B/C water-access outcome this batch);
  `exclusion_log.csv` updated (969 → 974 rows; E01 411 → 416); duplicate
  audit (exact-DOI + study_id) found no new duplicates; `full_text_
  retrieval_queue.csv` regenerated (1,661 open records); schema
  validation re-run clean.
  Running totals: 1,998/3,659 screened (1,024 include/974 exclude),
  1,661 open, 1,024 extracted studies, 46 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-sixth batch (10 records, 2026-09-27), twenty-ninth
  batch from the 543-record pool.** `new_batch_pool.json[280:290]`.
  White, Murphy & Spence (2012, policy analysis finding federal
  jurisdiction and fragmented departmental responsibility over First
  Nations reserve water systems tied to 119 of 600+ communities under
  water advisories despite $2.5B+ in federal spending, Canada, S1027)
  — **INCLUDE**. Snider (2004, case study of a formal Public Inquiry
  attributing the 2000 Walkerton E. coli disaster to neo-liberal
  deregulation of water-safety oversight, Ontario, S1028) —
  **INCLUDE**. Zaki & Amin (2009, household survey finding Thailand's
  1998 water-supply privatisation improved access/quality/tenure
  prospects for the poor despite higher charges, S1029) — **INCLUDE**.
  Graham, Desai & McFarlane (2013, nine-month ethnography documenting
  criminalization of informal water-pump use and a threefold
  differentiated municipal allocation quota, Mumbai, S1030) —
  **INCLUDE**. Chappells & Medd (2012, E01 drought-resilience policy-
  discourse study, southeast England) — **EXCLUDE (E01)**. Sharan
  (2011, E01 historical water-quality/pollution-discourse study,
  colonial Delhi) — **EXCLUDE (E01)**. Mugagga & Nabaasa (2016, E12
  self-labeled literature review, Africa SDGs) — **EXCLUDE (E12)**.
  Guardiola, Garcia-Rubio & Guidi-Gutierrez (2014, E04 wrong outcome --
  subjective well-being, not water access -- Sucre Bolivia) —
  **EXCLUDE (E04)**. Perez Prado (2006, E12 book review) — **EXCLUDE
  (E12)**. Hardy (2014, E01 historical disease-control study, typhoid
  America/England) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1027-S1030,
  1,024 → 1,028 rows each); `effect_sizes.csv` unchanged (46 rows: no
  confirmed regression-based estimate isolating a legal/institutional
  mechanism's effect on a Family A/B/C water-access outcome this
  batch); `exclusion_log.csv` updated (974 → 980 rows; E01 416 → 419,
  E04 67 → 68, E12 23 → 25); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,651 open records); schema validation re-run clean.
  Running totals: 2,008/3,659 screened (1,028 include/980 exclude),
  1,651 open, 1,028 extracted studies, 46 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-seventh batch (10 records, 2026-09-27), thirtieth
  batch from the 543-record pool.** `new_batch_pool.json[290:300]`.
  Nastar (2014, comparative case study finding 'world city'
  development-plan strategies in Johannesburg and Hyderabad produce
  documented water-access disparity favoring elites, S1031) —
  **INCLUDE**. Russ & Takahashi (2013, logistic regression, n=277,
  finding institutional redress-seeking contact -- municipal
  corporation OR=0.60*, NGO OR=0.56* -- significantly predicts reduced
  water-complaint odds, Ahmedabad Slum Networking Project, S1032) —
  **INCLUDE, added to effect_sizes.csv (Family C)**. Galaa & Bukari
  (2014, case study of a Tri-Water Sector Partnership using
  chieftaincy-based conflict resolution to resolve water-tariff
  payment conflicts, northern Ghana, S1033) — **INCLUDE**. Chappells,
  Medd & Shove (2011, E01 household gardening-practices drought
  study) — **EXCLUDE (E01)**. Kobayashi et al (eds., E12 full
  multi-chapter edited book, not screenable as one study) — **EXCLUDE
  (E12)**. Ferro, Romero & Covelli (2011, E01 utility operational-
  efficiency benchmarking study, Latin America) — **EXCLUDE (E01)**.
  Gomez-Temesio (2019, E01 reflexive ethnographic-methodology essay,
  Senegal) — **EXCLUDE (E01)**. Khan & Yang (2014, E01 water-quality/
  arsenic-mitigation stakeholder-opinion study, Bangladesh) —
  **EXCLUDE (E01)**. Moretto (2015, E01 governance-assessment-tool
  critique/application study, Venezuela) — **EXCLUDE (E01)**. Castro
  (2007, E12 self-labeled overview/conceptual article) — **EXCLUDE
  (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1031-S1033,
  1,028 → 1,031 rows each); `effect_sizes.csv` updated (46 → 47 rows:
  S1032 added, a logistic-regression estimate isolating institutional
  redress-seeking mechanisms' effect on a Family C water-service-
  complaint outcome); `exclusion_log.csv` updated (980 → 987 rows; E01
  419 → 424, E12 25 → 27); duplicate audit (exact-DOI + study_id)
  found no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,641 open records); schema validation re-run clean.
  Running totals: 2,018/3,659 screened (1,031 include/987 exclude),
  1,641 open, 1,031 extracted studies, 47 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-eighth batch (10 records, 2026-09-27), thirty-first
  batch from the 543-record pool.** `new_batch_pool.json[300:310]`.
  Granados & Sanchez (2014, difference-in-difference panel study of
  Colombia's Law 142/1994 water-provision reform, finding slower child-
  mortality reduction and smaller water-coverage gains in reformed
  municipalities, S1034) — **INCLUDE**. Makwara & Tavuyanago (2012,
  Zimbabwe urban water crisis, documenting municipal councils' lack of
  tariff-setting autonomy as an institutional barrier compounding the
  2008-2009 cholera epidemic, S1035) — **INCLUDE**. Francois, Kakeu &
  Kouame (2021, dynamic-panel GMM study of institutional quality and
  sanitation access across 44 sub-Saharan African countries, S1036) —
  **INCLUDE**. Leite (2010, qualitative case study of women's
  leadership in two Brazilian community water-management projects,
  S1037) — **INCLUDE**. Bruggink (1985, econometric study finding
  state-level regulation of US municipal water utilities significantly
  reduces monopoly welfare loss/excess pricing relative to local-only
  regulation, S1038) — **INCLUDE, added to effect_sizes.csv (Family
  C)**. McEvoy & Wilder (2012, E01 desalination climate-adaptation
  risk-discourse study, Arizona-Sonora) — **EXCLUDE (E01)**. Gorostiza,
  March & Sauri (2015, E01 historical case study of Madrid water supply
  during the Spanish Civil War) — **EXCLUDE (E01)**. Moglia, Perez &
  Burn (2008, E01 participatory water-development process-design
  paper, Pacific Islands) — **EXCLUDE (E01)**. Mbuvi, De Witte &
  Perelman (2012, E01 utility operational-efficiency benchmarking
  study, Africa) — **EXCLUDE (E01)**. Norman et al (2013, E01
  governance-assessment-tool development/application study, British
  Columbia) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1034-S1038,
  1,031 → 1,036 rows each); `effect_sizes.csv` updated (47 → 48 rows:
  S1038 added, an econometric estimate isolating a regulatory/
  institutional mechanism's -- state vs. local economic regulation --
  effect on a Family C water-affordability outcome); `exclusion_log.csv`
  updated (987 → 992 rows; E01 424 → 429); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,631 open records); schema validation re-run clean.
  Running totals: 2,028/3,659 screened (1,036 include/992 exclude),
  1,631 open, 1,036 extracted studies, 48 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-ninth batch (10 records, 2026-09-27), thirty-second
  batch from the 543-record pool.** `new_batch_pool.json[310:320]`.
  Guardia, Rossello & Garriga (2014, historical case study of
  Barcelona's water supply 1867-1967, documenting municipal-concession
  and private-monopoly mechanisms excluding poorer/peripheral districts
  until the 1960s, S1039) — **INCLUDE**. Rana & Piracha (2018,
  qualitative case study of the DSK Model community-based water
  governance partnership in Karail slum, Dhaka, documenting
  house-ownership/CBO-membership eligibility criteria and only 28%
  formal coverage, S1040) — **INCLUDE**. Greiner (2016, logistic
  regression of social drivers of US water utility privatization,
  n=47,367, S1041) — **INCLUDE**. Nickum & Lee (2006, E01 institutional
  water-supply bureaucracy reform, China) — **EXCLUDE (E01)**. Abers &
  Keck (2009, E01 Brazilian river-basin participatory water-resource
  governance) — **EXCLUDE (E01)**. Novotny, Hasman & Lepic (2018, E01
  systematic review of rural-sanitation contextual factors/motivations,
  institutional factors a minor 4.4% subcategory) — **EXCLUDE (E01)**.
  Nealer (2009, E12 conceptual SWOT-analysis essay, South African
  municipal water governance) — **EXCLUDE (E12)**. Lowatanatrakul
  (1991, E01 Thailand Provincial Waterworks Authority progress report)
  — **EXCLUDE (E01)**. Traverso-Yepez (2009, E07 Brazil Family Health
  Program social inequities, wrong service) — **EXCLUDE (E07)**.
  Troeger, Pham & Van Arsdale (2015, E01 community perceptions of
  water-source projects, Timor-Leste) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1039-S1041,
  1,036 → 1,039 rows each); `effect_sizes.csv` unchanged (48 rows --
  none of this batch's includes cleanly satisfied the strict Family
  A/B/C direct-exposure-to-access-outcome requirement); `exclusion_log.csv`
  updated (992 → 999 rows; E01 429 → 434, E07 24 → 25, E12 27 → 28);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,621 open records);
  schema validation re-run clean.
  Running totals: 2,038/3,659 screened (1,039 include/999 exclude),
  1,621 open, 1,039 extracted studies, 48 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-tenth batch (10 records, 2026-09-27), thirty-third
  batch from the 543-record pool.** `new_batch_pool.json[320:330]`.
  Two Google Drive deliveries did not match their target records
  despite correct filename/title metadata (caught only by reading the
  actual delivered text against expected title/authors/journal): Crow
  & Sultana 2002 (target) vs. Sneddon et al.'s introductory essay to
  the same special issue actually delivered — **wrong_file_retrieved**,
  not screened; Bazaanah 2021 (target) vs. Bardhan 2002 actually
  delivered — **wrong_file_retrieved**, not screened.
  Kvartiuk (2016, SUR/ordered-Probit-IV regressions finding non-
  electoral participation and CBO establishment significantly increase
  the probability of good local water-supply-system quality in rural
  Ukraine, S1042) — **INCLUDE**, added to `effect_sizes.csv` (Family A).
  Hoogesteger (2012, case study of Ecuador's Interjuntas-Chimborazo
  water-users federation eliminating a provincial Water Agency's
  corruption/ethnic discrimination via grassroots advocacy, S1043) —
  **INCLUDE**. González-Gómez, García-Rubio & González-Martínez (2014,
  fieldwork-based critique of Spain's privatized water-utility market
  structure and higher prices tied to institutional/regulatory
  deficiencies, S1044) — **INCLUDE**. Teodoro & Switzer (2016, E01
  human-capital/SDWA-compliance logistic regression, n=8,962 US
  utilities) — **EXCLUDE (E01)**. Neri Serneri (2007, E01 Italian urban
  water/sewer infrastructure history 1880-1920) — **EXCLUDE (E01)**.
  Price, Fielding & Leviston (2012, E01 Toowoomba recycled-water
  referendum attitudes study) — **EXCLUDE (E01)**. Hope, Foster, Money
  & Rouse (2012, E01 mobile-payment/smart-metering innovations, Kenya/
  Zambia) — **EXCLUDE (E01)**. Vidal de Llobatera (2003, E05 ~1-page
  advocacy column, no empirical evidence) — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1042-S1044,
  1,039 → 1,042 rows each); `effect_sizes.csv` updated (48 → 49 rows:
  S1042 added, town-hall-meeting-participation and CBO marginal effects
  on water-supply-system quality, Family A); `exclusion_log.csv`
  updated (999 → 1,004 rows; E01 434 → 438, E05 128 → 129); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,613 open records);
  schema validation re-run clean.
  Running totals: 2,046/3,659 screened (1,042 include/1,004 exclude;
  17 records now flagged wrong_file_retrieved, not counted as decided),
  1,613 open, 1,042 extracted studies, 49 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-eleventh batch (10 records, 2026-09-27), thirty-fourth
  batch from the 543-record pool.** `new_batch_pool.json[330:340]`.
  Jimenez, Cortobius & Kjellen (2014, systematic review of 185 articles
  on indigenous peoples and WASH, with a dedicated legislative-
  frameworks/indigenous-rights theme as a central organizing category,
  not a minor subcategory, S1045) — **INCLUDE**. Alda-Vidal, Kooy &
  Rusca (2018, 38-interview fieldwork study of Lilongwe Water Board
  staff documenting how everyday operational practices produce
  differential water-supply continuity between low-income and
  high-end areas, S1046) — **INCLUDE**. Haglund (2014, qualitative case
  study of legal adjudication via Brazilian courts and the Ministerio
  Publico reshaping water/sanitation access equity in Sao Paulo,
  S1047) — **INCLUDE**. McDonald & Jones (2018, E03 county-level SDWA-
  violation regression, water-quality outcome not access outcome) —
  **EXCLUDE (E03)**. Baffrey & Adis (2012, E06 Manila Water sewerage
  expansion engineering/operational case study) — **EXCLUDE (E06)**.
  Wong & Sharp (2009, E01 environmental-citizenship participation-
  theory case study, England) — **EXCLUDE (E01)**. Belzer (2020, E12
  normative SDWA "economic feasibility" regulatory-design essay, no
  original empirical data) — **EXCLUDE (E12)**. McFarlane (2008, E01
  discursive/theoretical sanitation-governmentality history, colonial/
  post-colonial Bombay) — **EXCLUDE (E01)**. Cole (2014, E01 tourism-
  water-scarcity/business-human-rights-advisory study, Bali) —
  **EXCLUDE (E01)**.
  One record, Behnke, Cronk, Shackelford et al. (2020, "Environmental
  health conditions in protracted displacement"), left **undecided**:
  title/authors/DOI confirmed correct, but the delivered PDF contained
  only the article's Supplemental Material, not the main-text
  synthesis; not screened, Drive file not moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S1045-S1047,
  1,042 → 1,045 rows each); `effect_sizes.csv` unchanged (49 rows --
  all three includes are qualitative/review studies with no
  regression-based estimate); `exclusion_log.csv` updated (1,004 →
  1,010 rows; E01 438 → 441, E03 29 → 30, E06 94 → 95, E12 28 → 29);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,604 open records);
  schema validation re-run clean.
  Running totals: 2,055/3,659 screened (1,045 include/1,010 exclude;
  17 wrong_file_retrieved, 1 further record left undecided, neither
  counted as decided), 1,604 open, 1,045 extracted studies, 49
  effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-twelfth batch (10 records, 2026-09-27), thirty-fifth
  batch from the 543-record pool.** `new_batch_pool.json[340:350]`.
  Heller (2007, Brazil basic sanitation, PLANASA concession model and
  2007 National Sanitation Law, documented coverage asymmetries by
  income and region, S1048) — **INCLUDE**. Murungi & van Dijk (2014,
  Kampala feacal sludge emptying economics, unregulated pricing and
  institutional fragmentation excluding poorer slum dwellers, S1049)
  — **INCLUDE**. Gerlach & Franceys (2010, 11-metropolitan-area
  comparative study of economic regulation's pro-poor constraints,
  S1050) — **INCLUDE**. van Dijk, Etajak, Mwalwega & Ssempebwa (2014,
  sanitation financing/governance-structure-dependent eligibility,
  Dar es Salaam & Kampala slums, S1051) — **INCLUDE**. Kurup (1991,
  Kerala participatory Ward Water Committee site-selection targeting
  the poor, before/after documented improvement, S1052) — **INCLUDE**.
  Barraque (2007, E01 French water-services delegation history, no
  documented differential-access outcome) — **EXCLUDE (E01)**.
  Alvarez, Prieto & Zofio (2014, E06 stochastic-frontier cost-
  efficiency methodology) — **EXCLUDE (E06)**. Grafton, Chu & Kompas
  (2015, E06 optimal water-tariff/supply-augmentation timing model,
  Sydney) — **EXCLUDE (E06)**. Lee (2014, E01 medieval English civic
  piped-water history, no documented differential-access outcome) —
  **EXCLUDE (E01)**. Zaato (2015, E01 Ghana water-sector management-
  contract efficiency case study) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1048-S1052,
  1,045 → 1,050 rows each); `effect_sizes.csv` unchanged (49 rows --
  all five includes are qualitative/comparative-case-study evidence);
  `exclusion_log.csv` updated (1,010 → 1,015 rows; E01 441 → 444, E06
  95 → 97); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,594 open
  records); schema validation re-run clean.
  Running totals: 2,065/3,659 screened (1,050 include/1,015 exclude),
  1,594 open, 1,050 extracted studies, 49 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-thirteenth batch (10 records, 2026-09-27), thirty-
  sixth batch from the 543-record pool.** `new_batch_pool.json[350:360]`.
  Sahu (2008, Orissa Pani Panchayat statutory WUA excluding marginal/
  landless farmers from irrigation-water access, S1053) — **INCLUDE**.
  Jacobs (1978, treaty-protected acequia water-rights institution
  threatened by top-down water-rights adjudication, New Mexico,
  S1054) — **INCLUDE**. Menon (2013, citizenship/legal-subject status
  determining water/sanitation infrastructure eligibility for Mumbai
  pavement dwellers, S1055) — **INCLUDE**. Motiram & Osberg (2010,
  Indian Time Use Survey analysis of caste/land-inequality/social-
  capital correlates of community water-supply outcomes, correlational
  not causal, S1056) — **INCLUDE**. Isham & Kahkonen (2001, OLS/probit/
  IV estimates of community design-participation's effect on
  water-collection time-savings, Sri Lanka/Karnataka/Maharashtra,
  S1057) — **INCLUDE**, added to `effect_sizes.csv` (Family A). Cheng
  (2013, Manila concessionaires' asymmetric non-payment enforcement
  producing differential affordability burdens, S1058) — **INCLUDE**.
  Wong (2016, E01 Volta River Basin trans-boundary water-resource
  governance) — **EXCLUDE (E01)**. Strauch & Almedom (2011, E01 Sonjo
  traditional water-resource/quality management, Tanzania) —
  **EXCLUDE (E01)**. Njeri et al. (2026, E07 Kenya hand hygiene policy
  governance-gap analysis) — **EXCLUDE (E07)**. Aiyer (2007, E12
  Plachimada Coca-Cola political-economy essay, self-described
  exploratory/incomplete) — **EXCLUDE (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1053-S1058,
  1,050 → 1,056 rows each); `effect_sizes.csv` updated (49 → 50 rows:
  S1057 added, community design-participation effect on water-
  collection time-savings, Family A); `exclusion_log.csv` updated
  (1,015 → 1,019 rows; E01 444 → 446, E07 25 → 26, E12 29 → 30);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,584 open records);
  schema validation re-run clean.
  Running totals: 2,075/3,659 screened (1,056 include/1,019 exclude),
  1,584 open, 1,056 extracted studies, 50 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-fourteenth batch (10 records, 2026-09-27), thirty-
  seventh batch from the 543-record pool.** `new_batch_pool.json[360:370]`.
  Massey (2014, Cape Town informal-settlement upgrading failure
  prompting illegal water/electricity connections as counter-conduct,
  S1059) — **INCLUDE**. Acey (2010, 783-household survey of gendered
  exclusion from water-governance voice channels, Lagos and Benin
  City, Nigeria, S1060) — **INCLUDE**. Hoque & Hoque (1994, Bangladesh
  rural WSS partnership, gender-differentiated tubewell site-selection
  participation, S1061) — **INCLUDE**. Marson & Savin (2015, panel
  regression across 22 SSA countries finding curvilinear cost-
  recovery-policy effect on water-coverage change, S1062) —
  **INCLUDE**, added to `effect_sizes.csv` (Family C). van Koppen &
  Schreiner (2014, South Africa statutory water-licensing law
  analysis identifying three forms of legal injustice against poor/
  Black small-scale water users, S1063) — **INCLUDE**. Godlewski
  (2010, E01 Israeli-Palestinian water-politics geopolitical essay) —
  **EXCLUDE (E01)**. Proskuryakova et al. (2018, E01 Russia water-
  sector scenario-planning study) — **EXCLUDE (E01)**. Kulkarni &
  Shankar (2014, E01 India groundwater-resource-competition study) —
  **EXCLUDE (E01)**. Kot, Gagnon & Castleden (2015, E01 Canadian
  small-water-system regulatory-compliance-capacity study) —
  **EXCLUDE (E01)**. Reddy & Snehalatha (2011, E01 sanitation/hygiene
  meaning to poor women, socio-cultural perceptions study, Hyderabad)
  — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1059-S1063,
  1,056 → 1,061 rows each); `effect_sizes.csv` updated (50 → 51 rows:
  S1062 added, cost-recovery-policy effect on water-coverage change,
  Family C); `exclusion_log.csv` updated (1,019 → 1,024 rows; E01
  446 → 451); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,574 open
  records); schema validation re-run clean.
  Running totals: 2,085/3,659 screened (1,061 include/1,024 exclude),
  1,574 open, 1,061 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-fifteenth batch (10 records, 2026-09-27), thirty-
  eighth batch from the 543-record pool.** `new_batch_pool.json[370:380]`.
  Walsh (2011, JAD cost-recovery/water-meter enforcement in Matamoros
  targeting wealthy neighborhoods first, within a legal non-denial-of-
  service constraint, Mexico, S1064) — **INCLUDE**. Jemmali & Amara
  (2015, Human Opportunity Index study of regional water/sanitation
  access disparities, Tunisia, S1065) — **INCLUDE**. Dawson (2010,
  Operation Gcin'amanzi prepaid water-meter program and class-
  differentiated citizenship, Soweto, S1066) — **INCLUDE**. Schoeffel
  (1995, multiple compounding institutional failures in a failed
  donor-funded rural water project, South Pacific, S1067) —
  **INCLUDE**. Schur (2017, comparative institutional study of
  Palomas/Columbus water-security outcomes shaped by binational
  policy parameters, US-Mexico transboundary aquifer, S1068) —
  **INCLUDE**. Warner & Bel (2008, E01 US/Spain privatization
  institutional-efficiency comparison, no documented access outcome)
  — **EXCLUDE (E01)**. Fedulova (2016, E01 Ukraine water-resources-
  market capitalization theory) — **EXCLUDE (E01)**. Hu (2011, E01
  Ninth Dragon God religious-political anthropology, North China) —
  **EXCLUDE (E01)**. Lukasiewicz et al. (2013, E01 Australian water-
  reform social-justice-framework content analysis) — **EXCLUDE
  (E01)**. Eggers et al. (2018, E03 Crow Reservation well-water
  contaminant risk assessment) — **EXCLUDE (E03)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1064-S1068,
  1,061 → 1,066 rows each); `effect_sizes.csv` unchanged (51 rows --
  all five includes are qualitative/descriptive-disparity studies);
  `exclusion_log.csv` updated (1,024 → 1,029 rows; E01 451 → 455, E03
  30 → 31); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,564 open
  records); schema validation re-run clean.
  Running totals: 2,095/3,659 screened (1,066 include/1,029 exclude),
  1,564 open, 1,066 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-sixteenth batch (10 records, 2026-09-27), thirty-
  ninth batch from the 543-record pool.** `new_batch_pool.json[380:390]`.
  Bond (2012, Free Basic Water convex tariff design, prepaid metering,
  and mass disconnections disproportionately burdening the poor,
  South Africa, S1069) — **INCLUDE**. Ducrot & Bourblanc (2017,
  contradictions between pro-poor rural water-program design intent
  and delivered equity outcomes, Mozambique, S1070) — **INCLUDE**.
  Galaz (2004, game-theoretic/empirical study of Chile's tradable
  water-rights market incentivizing rights violations against
  underprivileged users, S1071) — **INCLUDE**. Shandra, Shandra &
  London (2012, fixed-effects regression confirming water/sanitation
  access as a mediating pathway of IMF structural adjustment's effect
  on infant mortality, Sub-Saharan Africa, S1072) — **INCLUDE**.
  Birkenholtz (2010, full-cost-recovery tariff reform producing
  class-differentiated water-collection practices, Jaipur, India,
  S1073) — **INCLUDE**. Taylor (2014, E01 Sevenoaks sewage-reform
  political history, no documented differential-access outcome) —
  **EXCLUDE (E01)**. Hoag (2006, E01 gender and water-resource
  development, Rufiji Delta) — **EXCLUDE (E01)**. Moore (2014, E01
  China South-North Water Transfer Project, water-resource
  infrastructure politics) — **EXCLUDE (E01)**. Boucheron (2001, E01
  medieval Milan water-governance history, elite resource allocation)
  — **EXCLUDE (E01)**. Sternlieb & Laituri (2010, E12 WASH indicator
  frameworks conceptual review) — **EXCLUDE (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1069-S1073,
  1,066 → 1,071 rows each); `effect_sizes.csv` unchanged (51 rows --
  all five includes are qualitative/theoretical or mediation-model
  studies); `exclusion_log.csv` updated (1,029 → 1,034 rows; E01 455 →
  459, E12 30 → 31); duplicate audit (exact-DOI + study_id) found no
  new duplicates; `full_text_retrieval_queue.csv` regenerated (1,554
  open records); schema validation re-run clean.
  Running totals: 2,105/3,659 screened (1,071 include/1,034 exclude),
  1,554 open, 1,071 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-seventeenth batch (10 records, 2026-09-27), fortieth
  batch from the 543-record pool.** `new_batch_pool.json[390:400]`.
  Anand (2012, deliberate municipal inaction and discriminatory
  infrastructure neglect rendering a Muslim settler community
  "abject" and denied formal water access, Mumbai, S1074) —
  **INCLUDE**. Silvestre (2012, institutional-arrangement comparison
  finding prices track organizational costs and quality tracks
  ownership model rather than management-model alone, Portugal,
  S1075) — **INCLUDE**. Valerio (2024, multi-level-governance
  fragmentation and tariff-approval delay producing stagnant coverage
  and higher effective costs for poorer households, Zamboanga City,
  Philippines, S1076) — **INCLUDE**. Panda (2007, critical policy
  analysis of gender-mainstreaming rhetoric vs. practice in
  water-sector reform and privatization, India, S1077) — **INCLUDE**.
  Eguavoen (2008, Ghana's NCWSP community-based management policy
  formally restricting pre-existing customary equal-use water rights,
  excluding non-resident farmers and households unable to raise the
  required contribution, S1078) — **INCLUDE**. Antunes & Martins
  (2020, fixed-effects panel regression across 111 countries finding
  significant socioeconomic/structural determinants of water-access
  coverage, S1079) — **INCLUDE**. Crook & Ayee (2006,
  privatization/contracting-out of environmental sanitation
  undermining street-level regulatory enforcement capacity, Kumasi
  and Accra, Ghana, S1080) — **INCLUDE**. Alam et al. (2020,
  qualitative assessment of institutional/infrastructural barriers
  and financing strategies for connecting low-income communities to
  the proposed Dhaka Sanitation Improvement Project sewerage network,
  S1081) — **INCLUDE**. Zawahri (2006, E01 Iraq/Indus transboundary
  water-treaty comparison, geopolitical not household-service access)
  — **EXCLUDE (E01)**. Gehrke (2016, E01 Joseph Chamberlain municipal
  socialism, Birmingham, historical municipal-ownership politics
  without documented differential-access outcome) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1074-S1081,
  1,071 → 1,079 rows each); `effect_sizes.csv` unchanged (51 rows --
  Silvestre's ownership/management-model comparison and Antunes &
  Martins' panel regression both lack a specific legal/institutional
  fee/tenure/eligibility mechanism isolated per the strict Family
  A/B/C framework; the remaining six includes are qualitative/
  ethnographic case studies without a mechanism-isolating regression
  on water access); `exclusion_log.csv` updated (1,034 → 1,036 rows;
  E01 459 → 461); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,544
  open records); schema validation re-run clean.
  Running totals: 2,115/3,659 screened (1,079 include/1,036 exclude),
  1,544 open, 1,079 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-eighteenth batch (10 records, 2026-09-27), forty-
  first batch from the 543-record pool.** `new_batch_pool.json[400:410]`.
  Etongo et al. (2018, Water User Committee financial-contribution
  requirements and participation as determinants of rural
  water-system functionality, Uganda, S1082) — **INCLUDE**. Badri &
  Joshi (2018, NGO-ULB cost-sharing "One Home-One Toilet" household
  sanitation delivery model, pre-post impact assessment, Maharashtra,
  India, S1083) — **INCLUDE**. Behera, Rahut & Sethi (2020,
  multinomial logit regression on Nepal Living Standard Survey panel
  data finding broad socioeconomic/geographic determinants of
  water/sanitation access, S1084) — **INCLUDE**. Tigabu et al. (Tobit
  regression on Water User Committee-set tariff/contribution
  determinants of water-system maintenance funding, Ethiopia, S1085)
  — **INCLUDE**. Ranganathan (2014, formal land-tenure-proof
  requirement for water connection waived in favor of payment-proof
  following resident welfare association lobbying, Bangalore, India,
  S1086) — **INCLUDE**. Chng (2012, National Water Resources Board
  Certificate of Public Convenience licensing framework for
  small-scale water providers and regulatory mobilization by
  NGOs/community groups, post-privatization Metro Manila,
  Philippines, S1087) — **INCLUDE**. Khabo-Mmekoa & Momba (2019, E03
  microbiological water-quality/contamination-exposure study,
  KwaZulu-Natal) — **EXCLUDE (E03)**. Sperling, Romero-Lankao & Beig
  (2016, E04 wrong outcome -- policy-priority ranking, not water
  access, Mumbai) — **EXCLUDE (E04)**. Sommer et al. (2014, E12
  narrative literature review, no original empirical data) —
  **EXCLUDE (E12)**. Nauges & Strand (2007, E06 pure economic
  demand-elasticity estimation, no legal/institutional content,
  Central America) — **EXCLUDE (E06)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1082-S1087,
  1,079 → 1,085 rows each); `effect_sizes.csv` unchanged (51 rows --
  all six includes are qualitative/mixed-methods case studies or
  regressions whose outcome variable does not isolate a specific
  legal/institutional mechanism's effect on a water-access outcome
  per the strict Family A/B/C framework); `exclusion_log.csv` updated
  (1,036 → 1,040 rows; E03 31 → 32, E04 68 → 69, E06 97 → 98, E12 31
  → 32); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,534
  open records); schema validation re-run clean.
  Running totals: 2,125/3,659 screened (1,085 include/1,040 exclude),
  1,534 open, 1,085 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-nineteenth batch (10 records, 2026-09-27), forty-
  second batch from the 543-record pool.** `new_batch_pool.json[410:420]`.
  Rajaraman, Travasso & Heymann (2013, labour-law coverage vs. its
  absence produces sharply differential workplace sanitation access
  for low-income working women, Bangalore, India, S1088) —
  **INCLUDE**. Javed & Farhan (2020, decentralized-governance
  fragmentation and NGO-WASA bulk-purchase partnership as
  institutional mechanisms for low-income water access, Pakistan,
  S1089) — **INCLUDE**. Colbran (2017, legal eligibility obstacles
  restricting low-income household water qualification and
  disproportionate tariff increases for the poor, Jakarta, Indonesia,
  S1090) — **INCLUDE**. Mukherjee et al. (2009, eight-dimension
  institutional "enabling environment" framework for rural sanitation
  scale-up, India/Indonesia/Tanzania, S1091) — **INCLUDE**. Singh,
  Upadhyay & Mittal (2005, connection charges as a major obstacle to
  formal water access for the poor, ~50% of India's poor unconnected
  and unsubsidized, S1092) — **INCLUDE**. Loftus & McDonald (2001,
  regressive infrastructure/connection charges and regulatory-capture
  tariff increases under Buenos Aires water privatization, S1093) —
  **INCLUDE**. Danso-Appiah et al. (2008, E01 wrong-topic Cochrane
  review of schistosomiasis drug treatments) — **EXCLUDE (E01)**.
  Nelson & Murray (2008, E12 conceptual/technology sanitation review,
  no original empirical data) — **EXCLUDE (E12)**. Postel & Thompson
  (2005, E01 watershed protection/ecosystem-services governance
  study) — **EXCLUDE (E01)**. Grigg (2017, E01 regulatory-
  compliance/water-quality-crisis study, Flint, Michigan) — **EXCLUDE
  (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1088-S1093,
  1,085 → 1,091 rows each); `effect_sizes.csv` unchanged (51 rows --
  all six includes are qualitative/policy-analysis case studies with
  descriptive statistics, not regression-based estimates isolating a
  mechanism's effect per the strict Family A/B/C framework);
  `exclusion_log.csv` updated (1,040 → 1,044 rows; E01 461 → 464, E12
  32 → 33); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,524
  open records); schema validation re-run clean.
  Running totals: 2,135/3,659 screened (1,091 include/1,044 exclude),
  1,524 open, 1,091 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twentieth batch (10 records, 2026-09-27), forty-
  third batch from the 543-record pool.** `new_batch_pool.json[420:430]`.
  de Sardan (2011, multiple institutional modes of governance
  co-delivering water, project-imposed contribution quotas, traders
  circumventing subsidized-water eligibility, Niger, S1094) —
  **INCLUDE**. Adams & Zulu (2015, Water User Associations as
  business-based community-public partnership model, land-tenure
  insecurity shaping peri-urban water access, Malawi, S1095) —
  **INCLUDE**. Sandoval-Minero (2019, federal subsidy allocation
  without performance linkage, connections financed directly by
  users shifting cost burden onto households, Mexico, S1096) —
  **INCLUDE**. Agthe & Billings (1987, E06 pure demand-elasticity
  economics study, Tucson block-rate pricing) — **EXCLUDE (E06)**.
  Jiang & Zheng (2014, E06 utility financial/efficiency study, China
  PSP, non-significant coverage estimate) — **EXCLUDE (E06)**.
  Plummer et al. (2010, E01 water-quality regulatory-policy study,
  Walkerton multi-barrier approach) — **EXCLUDE (E01)**. Closmann
  (2007, E01 historical water-pollution study, Hamburg 1919-1923) —
  **EXCLUDE (E01)**. Ivens (2008, E12 synthesis/opinion essay, no
  original empirical data) — **EXCLUDE (E12)**. Kansal & Cole (2019,
  E01 broad WASH sustainability/customer-satisfaction framework,
  Sierra Leone) — **EXCLUDE (E01)**. Gero et al. (2014, E12 explicitly
  labeled systematic review, no original empirical data) — **EXCLUDE
  (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1094-S1096,
  1,091 → 1,094 rows each); `effect_sizes.csv` unchanged (51 rows --
  all three includes are qualitative/institutional-analysis case
  studies without a regression-based effect size); `exclusion_log.csv`
  updated (1,044 → 1,051 rows; E01 464 → 467, E06 98 → 100, E12 33 →
  35); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,514
  open records); schema validation re-run clean.
  Running totals: 2,145/3,659 screened (1,094 include/1,051 exclude),
  1,514 open, 1,094 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-first batch (10 records, 2026-09-27), forty-
  fourth batch from the 543-record pool.** `new_batch_pool.json[430:440]`.
  Botton & de Gouvello (2008, ETOSS vs. ORAB regulatory-tolerance
  divergence for informal water access, AASA sole-provider clause,
  desvinculados networks, Buenos Aires, Argentina, S1097) —
  **INCLUDE**. Whittington (2003, pro-poor tariff-reform agenda:
  guaranteed connections, upfront-cost subsidies, legalized vending,
  South Asia, S1098) — **INCLUDE**. Adubofour, Obiri-Danso & Quansah
  (2013, illegal-settlement status barring legal water connections,
  informal purchase at 10-11x official tariff, Kumasi, Ghana, S1099)
  — **INCLUDE**. Willis et al. (2008, National Water Initiative
  full-cost-recovery tariff applied to a 15-household bulk
  connection, Yarilena Aboriginal homeland, Australia, S1100) —
  **INCLUDE**. Bel, González-Gómez & Picazo-Tadeo (2013, E01
  regulatory-agency institutional architecture, no documented access
  outcome, Spain) — **EXCLUDE (E01)**. Sandhu (E01 wrong topic,
  waste-picker affordable-housing vulnerability, Amritsar, India) —
  **EXCLUDE (E01)**. Kotze & Mathola (2012, E01 broad multi-service
  urban-renewal satisfaction survey, Alexandra, Johannesburg) —
  **EXCLUDE (E01)**. Caldwell et al. (2003, E03 water-quality/
  arsenic-contamination study, Bangladesh) — **EXCLUDE (E03)**.
  Wutich et al. (2021, E12 conceptual agenda-setting synthesis, no
  original empirical data) — **EXCLUDE (E12)**. Mpanga (2016, E05
  doctrinal right-to-water constitutional analysis, no empirical
  evidence, Uganda) — **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1097-S1100,
  1,094 → 1,098 rows each); `effect_sizes.csv` unchanged (51 rows --
  all four includes are institutional case studies/policy analyses
  without a regression-based effect size); `exclusion_log.csv`
  updated (1,051 → 1,057 rows; E01 467 → 470, E03 32 → 33, E05 129 →
  130, E12 35 → 36); duplicate audit (exact-DOI + study_id) found no
  new duplicates; `full_text_retrieval_queue.csv` regenerated (1,504
  open records); schema validation re-run clean.
  Running totals: 2,155/3,659 screened (1,098 include/1,057 exclude),
  1,504 open, 1,098 extracted studies, 51 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-second batch (10 records, 2026-09-27),
  forty-fifth batch from the 543-record pool.** `new_batch_pool.json[440:450]`.
  Debbane & Keil (2004, Zwelihle residents excluded from indigent-
  tariff subsidy, ~60% affected by credit-control water cut-offs,
  Hermanus, South Africa, S1101) — **INCLUDE**. Prokopy (2009,
  propensity-score-matched estimates showing capital-cost
  contribution and meeting attendance significantly improve a
  composite water-access index, India, S1102) — **INCLUDE**, added to
  `effect_sizes.csv` (Family B). Wu & Malaluan (2008, natural
  experiment of identical concession terms producing divergent
  corporate-governance outcomes, 30% connection growth concentrated
  in poor areas, Metro Manila, S1103) — **INCLUDE**. Franceys & Weitz
  (2003, 20 case studies across 10 Asian countries documenting land-
  title-waiver, installment-fee and shared-connection mechanisms for
  the urban poor, S1104) — **INCLUDE**. Trepied (2012, municipal
  water-pipeline sequencing dispute bypassing the source-territory
  Kanak tribe, contested via customary governance, New Caledonia,
  S1105) — **INCLUDE**. Kooy, Furlong & Lamb (E12 conceptual
  viewpoint essay, no original empirical data, Nature Based
  Solutions) — **EXCLUDE (E12)**. Muller (2003, E05 policy-opinion
  essay by responsible government official, South Africa) —
  **EXCLUDE (E05)**. Ioris (2007, E01 water-resource/political-
  economy critique, Brazil) — **EXCLUDE (E01)**. Subramaniam &
  Williford (2012, E12 explicit literature review, no original
  empirical data) — **EXCLUDE (E12)**. Van Vugt & Samuelson (1999,
  E01 consumption/conservation behavior study, not an access-
  eligibility mechanism) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1101-S1105,
  1,098 → 1,103 rows each); `effect_sizes.csv` updated (51 → 52 rows
  -- S1102 added as Family B); `exclusion_log.csv` updated (1,057 →
  1,062 rows; E01 470 → 472, E05 130 → 131, E12 36 → 38); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,494 open records);
  schema validation re-run clean.
  Running totals: 2,165/3,659 screened (1,103 include/1,062 exclude),
  1,494 open, 1,103 extracted studies, 52 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-third batch (10 records, 2026-09-27),
  forty-sixth batch from the 543-record pool.** `new_batch_pool.json[450:460]`.
  Baijius & Patrick (2019, political-ecology case study of colonial
  institutional/jurisdictional exclusion, boil-water advisories 2.5x
  more frequent for First Nations, Canada, S1106) — **INCLUDE**.
  Katomero & Georgiadou (2018, institutional-theory case study of
  formal/informal COWSO complementarity associated with superior rural
  water access, Tanzania, S1107) — **INCLUDE**. Patrick, Grant &
  Bharadwaj (2019, federal/provincial jurisdictional fragmentation
  under the Indian Act and Constitution Act 1982 linked to a
  74%/21%/remainder piped/truck/well service-type split on reserve,
  Muskowekwan First Nation, Saskatchewan, S1108) — **INCLUDE**. Jama &
  Mourad (2019, overlapping/uncoordinated agency mandates and a PPP
  concession pricing structure driving unaffordable water for the
  poor, Garowe, Puntland, Somalia, S1109) — **INCLUDE**. Baird,
  Plummer, Dupont & Carter (2015, E04 perceptions/satisfaction survey,
  not an institutional access-eligibility mechanism, Ontario First
  Nations) — **EXCLUDE (E04)**. Huda et al. (2012, E04 child
  diarrhea/respiratory-illness handwashing-behavior RCT, wrong
  outcome, Bangladesh SHEWA-B) — **EXCLUDE (E04)**. Jackson, Hatton
  MacDonald & Bark (2019, E04 contingent-valuation public-willingness-
  to-pay survey, not a documented access mechanism, Murray-Darling
  Basin, Australia) — **EXCLUDE (E04)**. Yulistyorini et al. (2019, E06
  pure engineering/treatment-performance study, Malang, Indonesia) —
  **EXCLUDE (E06)**. Snyder et al. (2020, E06 facility-maintenance/
  service-delivery-model performance comparison, not a legal-
  eligibility mechanism, Nairobi, Kenya) — **EXCLUDE (E06)**. Sinclair
  et al. (2011, E01 clinical vaccine-efficacy review, wrong topic,
  Cochrane cholera-vaccine review) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1106-S1109,
  1,103 → 1,107 rows each); `effect_sizes.csv` unchanged (52 rows --
  all four includes are qualitative institutional case studies without
  a regression-based effect size); `exclusion_log.csv` updated (1,062
  → 1,068 rows; E01 472 → 473, E04 69 → 72, E06 100 → 102); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,484 open records);
  schema validation re-run clean.
  Running totals: 2,175/3,659 screened (1,107 include/1,068 exclude),
  1,484 open, 1,107 extracted studies, 52 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-fourth batch (10 records, 2026-09-27),
  forty-seventh batch from the 543-record pool.** `new_batch_pool.json[460:470]`.
  Mafuta, Zuwarimwe & Mwale (2021, near-zero state WASH investment in
  Jariban district financed instead by NGOs 54.3%/diaspora
  34.5%/community 11.2%, Somalia, S1110) — **INCLUDE**. Faure, Faust &
  Kaminsky (2019, 28-interview institutional-decision-making study,
  reactive rather than proactive WASH planning response to the
  2015-2016 refugee crisis, Germany, S1111) — **INCLUDE**. Martinez
  Moscoso, Aguilar Feijo & Verdugo Silva (2018, constitutional
  minimum-water cost-recovery charge disproportionately burdens
  smaller/less-efficient/more-indigenous municipalities -- Suscal 4.17%
  vs. Cuenca 0.31% of extreme-poverty income, Ecuador, S1112) —
  **INCLUDE**. Betera, Nyamandi & Nunu (2025, E12 explicit scoping
  review, no original empirical data, Zimbabwe WASH) — **EXCLUDE
  (E12)**. Turley et al. (2013, E12 Cochrane slum-upgrading systematic
  review) — **EXCLUDE (E12)**. Pories, Fonseca & Delmon (2019, E12
  multi-country synthesis/framework paper, not a bounded case study,
  "Mobilising Finance for WASH") — **EXCLUDE (E12)**. Li, Cohen, Li &
  Zhang (2019, E01 broad province-level socioeconomic-determinants CCA
  study, no institutional mechanism, China rural drinking water) —
  **EXCLUDE (E01)**. Patel et al. (2012, E04 child water-consumption
  behavior study, wrong outcome, California school food-service
  areas) — **EXCLUDE (E04)**. Jimenez et al. (2019, E12
  literature-review-based conceptual framework, "The Enabling
  Environment for Participation in Water and Sanitation") — **EXCLUDE
  (E12)**. Bellaubi & Bustamante (2018, E05 theoretical/values-based
  paradigm analysis, no empirical data, Cochabamba water agenda) —
  **EXCLUDE (E05)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1110-S1112,
  1,107 → 1,110 rows each); `effect_sizes.csv` unchanged (52 rows --
  S1112's cross-municipality IH percentages are a 3-unit formula-based
  comparative calculation, not a regression-based estimate);
  `exclusion_log.csv` updated (1,068 → 1,075 rows; E01 473 → 474, E04
  72 → 73, E05 131 → 132, E12 38 → 42); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,474 open records); schema validation re-run clean.
  Running totals: 2,185/3,659 screened (1,110 include/1,075 exclude),
  1,474 open, 1,110 extracted studies, 52 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-fifth batch (10 records, 2026-09-27),
  forty-eighth batch from the 543-record pool.** `new_batch_pool.json[470:480]`.
  Narzetti & Marques (2021, informal settlements excluded from urban
  WSS statistics, regulatory reform needed for universalization,
  Brazil, S1113) — **INCLUDE**. Safari et al. (2019, village WASH
  by-laws + SMART enforcement drove latrine coverage 7.5%->99.8%,
  Njombe, Tanzania, S1114) — **INCLUDE**. Danert et al. (2003,
  multi-district stakeholder analysis of decentralization/
  privatization policy shaping private-sector rural water delivery,
  Uganda, S1115) — **INCLUDE**. Mottelson (2020, government repression
  of informal development linked to lower water/sanitation access
  across 4 East African cities, S1116) — **INCLUDE**. Amaechina et al.
  (2020, multi-country documentation of COVID-19 disconnection
  moratoriums/reconnection programs/subsidy eligibility criteria, 14
  countries, S1117) — **INCLUDE**. Mawani (2019, town planning scheme
  premised on illegal-construction status mediates water access in
  Muslim-majority Ahmedabad, S1118) — **INCLUDE**. Silvestri et al.
  (2018, 57-interview/2-workshop study of landownership/governance-
  capacity mechanisms incl. KCCA exclusion of Kawaala settlement from
  a water well, Tanzania/Ghana/Uganda, S1119) — **INCLUDE**. Yeboah
  (2006, service-area reclassification urban->rural CWSD on an
  explicit "ability to pay" criterion, Ghana, S1120) — **INCLUDE**.
  Akiwumi (2015, E05 doctrinal legal-text analysis, no empirical data,
  Sierra Leone water reform) — **EXCLUDE (E05)**. Taylor & Trentmann
  (2011, E01 Victorian-era propertied-ratepayer tariff-politics
  history, not a marginalized-population exclusion mechanism,
  "Liquid Politics") — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1113-S1120,
  1,110 → 1,118 rows each); `effect_sizes.csv` unchanged (52 rows --
  all eight includes are qualitative/comparative institutional case
  studies without regression-based estimates); `exclusion_log.csv`
  updated (1,075 → 1,077 rows; E01 474 → 475, E05 132 → 133); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,464 open records);
  schema validation re-run clean.
  Running totals: 2,195/3,659 screened (1,118 include/1,077 exclude),
  1,464 open, 1,118 extracted studies, 52 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-sixth batch (10 records, 2026-09-27),
  forty-ninth batch from the 543-record pool.** `new_batch_pool.json[480:490]`.
  Hanak (2008, panel regression: water-adequacy screening policy
  reduces new residential permitting 16%-41%, impact fees have no
  effect, California, S1121) — **INCLUDE**, added to `effect_sizes.csv`
  (Family A). Dos Santos & LeGrand (2013, Cox regression: non-zoned
  settlement hazard ratio 0.14*** for piped-water access, Ouagadougou,
  S1122) — **INCLUDE**, added to `effect_sizes.csv` (Family A).
  Mukhija & Mason (2013, municipal annexation-refusal excluding poor
  colonias from water/sewer, federal funding as enabling reversal,
  California, S1123) — **INCLUDE**. Smiley (2016, connection-fee/
  service-fragmentation mechanisms producing differential consumption
  by income, Dar es Salaam, S1124) — **INCLUDE**. Fiki et al. (2007,
  centralized state water program's politicization vs. community-
  centered nodal governance, Nigeria, S1125) — **INCLUDE**. Ojha et al.
  (2020, 4 of 5 Himalayan cities lack water-governance institutions,
  Nepal/India, S1126) — **INCLUDE**. Arku & Arku (2010, E01 water-
  resource/irrigation time-use ethnography, gender and drought, Ghana)
  — **EXCLUDE (E01)**. Sullivan & Meigh (2003, E12 methodological
  Water Poverty Index implementation paper) — **EXCLUDE (E12)**. Ojha
  et al. (2018, E06 engineering/economic tariff-optimization
  simulation, Melamchi, Nepal) — **EXCLUDE (E06)**. Target record
  Nallathiga 2009 (Mumbai private-sector water supply) —
  **wrong_file_retrieved**: delivered PDF was instead Bakker 2008
  ("The Ambiguity of Community," Cochabamba), confirmed by title
  metadata and full-text content; not screened, file not moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S1121-S1126,
  1,118 → 1,124 rows each); `effect_sizes.csv` updated (52 → 54 rows
  -- S1121, S1122 added as Family A); `exclusion_log.csv` updated
  (1,077 → 1,080 rows; E01 475 → 476, E06 102 → 103, E12 42 → 43);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,455 open records,
  incl. 18 wrong_file_retrieved records); schema validation re-run
  clean.
  Running totals: 2,204/3,659 screened (1,124 include/1,080 exclude),
  1,455 open, 1,124 extracted studies, 54 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-seventh batch (10 records, 2026-09-27),
  fiftieth batch from the 543-record pool.** `new_batch_pool.json[490:500]`.
  Gulyani, Talukdar & Kariuki (2005, 674-household survey testing the
  "poor pay more, get less" narrative and demand-driven/water-markets
  prescription, Kenya, S1127) — **INCLUDE**. Ballestero (2015,
  ethnography of ARESEP's water-tariff regulatory formula
  operationalizing the constitutional human right to water, Costa
  Rica, S1128) — **INCLUDE**. Pastore (2015, colonial-era "piped
  paradigm" infrastructure design as a mechanism of differential
  sanitation access, Dar es Salaam, S1129) — **INCLUDE**. McSpirit &
  Reid (2011, E04 bottled-water consumer-perceptions/purchasing-
  behavior study, Appalachia) — **EXCLUDE (E04)**. Willetts et al.
  (2013, E12 gender-equality strengths-based assessment methodology
  paper) — **EXCLUDE (E12)**. Kiunsi (2013, E01 climate-change-
  adaptation-policy overview, water statistics contextual only, Dar
  es Salaam) — **EXCLUDE (E01)**. Imo State Evaluation Team (1989,
  E04 quasi-experimental public-health epidemiological evaluation,
  Nigeria) — **EXCLUDE (E04)**. Stewart & Gray (2006, E01 governance/
  stakeholder-theory analysis, no documented access outcomes, Type
  Two multistakeholder partnerships) — **EXCLUDE (E01)**. Perez
  (2002, E01 participatory-development/gender-inclusion critique,
  Mexican rural community) — **EXCLUDE (E01)**. Leon (2014, E01
  land-tenure/eviction political economy, water only incidentally
  mentioned, World Bank Ethiopia) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1127-S1129,
  1,124 → 1,127 rows each); `effect_sizes.csv` unchanged (54 rows --
  all three includes are qualitative institutional case studies);
  `exclusion_log.csv` updated (1,080 → 1,087 rows; E01 476 → 480, E04
  73 → 75, E12 43 → 44); duplicate audit (exact-DOI + study_id) found
  no new duplicates; `full_text_retrieval_queue.csv` regenerated
  (1,445 open records); schema validation re-run clean.
  Running totals: 2,214/3,659 screened (1,127 include/1,087 exclude),
  1,445 open, 1,127 extracted studies, 54 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-eighth batch (10 records, 2026-09-27),
  fifty-first batch from the 543-record pool.** `new_batch_pool.json[500:510]`.
  Rahaman, Everett & Neu (2007, governmentality/institutional-
  sociology study of accounting technologies in Ghana's water-
  privatization debate, 34 interviews, S1130) — **INCLUDE**.
  Subramaniam (2014, National Water Policy analysis + Tarun Bharat
  Sangh "water parliament" institutional case study, differential
  participation by caste/class/gender, Rajasthan, S1131) —
  **INCLUDE**. Manikutty (1997, matched comparative study of Ward
  Water Committee participatory-governance mechanism, n=80x2, Kerala,
  S1132) — **INCLUDE**. McFarlane & Desai (2015, ethnography of
  notified/non-notified legal slum status and residency-cutoff
  eligibility producing differential water/sanitation entitlements,
  Mumbai, S1133) — **INCLUDE**. Das (2015, comparative case study of
  notified-slum eligibility/cost-recovery mechanism, n=422 survey,
  Madhya Pradesh, S1134) — **INCLUDE**. Wutich (2009, panel survey of
  community-membership eligibility institution excluding renters from
  a tapstand system, 72 households x 5 rounds, Cochabamba, S1135) —
  **INCLUDE**. Yacoob (1990, E12 policy essay/literature review on
  cost-recovery methodology, no original case study) — **EXCLUDE
  (E12)**. Medilanski et al. (2006, E06 engineering/technology-
  adoption feasibility survey of decentralized sanitation
  alternatives, Kunming) — **EXCLUDE (E06)**. Arar (1998, E04
  biocultural epidemiological study, childhood diarrhea as primary
  outcome, Palestinians in Jordan) — **EXCLUDE (E04)**. Target record
  Fombe & Bih 2014 (surface water pollution, Kumba, Cameroon) —
  **wrong_file_retrieved**: delivered PDF was instead Kimengsi & Fogwe
  2017 ("Urban Green Development Planning," Bamenda City, Cameroon),
  confirmed by title metadata and full-text content; not screened,
  file not moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S1130-S1135,
  1,127 → 1,133 rows each); `effect_sizes.csv` unchanged (54 rows --
  all six includes are qualitative/descriptive institutional case
  studies, none regression-based); `exclusion_log.csv` updated (1,087
  → 1,090 rows; E04 75 → 76, E06 103 → 104, E12 44 → 45); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,436 open records,
  incl. 19 wrong_file_retrieved records); schema validation re-run
  clean.
  Running totals: 2,223/3,659 screened (1,133 include/1,090 exclude),
  1,436 open, 1,133 extracted studies, 54 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-twenty-ninth batch (10 records, 2026-09-27),
  fifty-second batch from the 543-record pool.** `new_batch_pool.json[510:520]`.
  Ban, Das Gupta & Rao (2010, regression study of political capture of
  Gram Panchayat sanitation function, village/road fixed effects,
  South India, S1136) — **INCLUDE**. Shah et al. (2010, multi-state
  colloquium on governance-reform/outsourcing models and differential
  sanitation outcomes, 6 Indian states, S1137) — **INCLUDE**.
  Habich-Sobiegalla (2018, "project mechanism" earmarked-fund
  allocation case study, Yunnan China, S1138) — **INCLUDE**. Kazora &
  Mourad (2018, multi-criteria sustainability assessment scoring
  legal/institutional gaps in decentralized wastewater systems, Kigali
  Rwanda, S1139) — **INCLUDE**. Bos & Brown (2012, E01
  environmental-governance transition-management case study, Cooks
  River Sydney) — **EXCLUDE (E01)**. Hauck & Youkhana (2010, E01
  fisheries-management institutional case study, Northern Ghana) —
  **EXCLUDE (E01)**. Devnarain & Matthias (2011, E04 gendered
  education/safety consequences of water/sanitation infrastructure
  absence, rural South African school) — **EXCLUDE (E04)**. Kósa,
  Darago & Adany (2011, E12 methodological environmental-survey
  scoring-system paper, segregated Roma habitats Hungary) — **EXCLUDE
  (E12)**. Refulio Coronado (2025, E01 recreational-beach/PFAS
  consumer-behavior economics dissertation, US) — **EXCLUDE (E01)**.
  Barber & Jackson (2014, E01 customary water-resource/riparian-law
  history, Roper River Australia) — **EXCLUDE (E01)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1136-S1139,
  1,133 → 1,137 rows each); `effect_sizes.csv` updated (54 → 55 rows
  -- S1136 added as Family C); `exclusion_log.csv` updated (1,090 →
  1,096 rows; E01 480 → 484, E04 76 → 77, E12 45 → 46); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,426 open records);
  schema validation re-run clean.
  Running totals: 2,233/3,659 screened (1,137 include/1,096 exclude),
  1,426 open, 1,137 extracted studies, 55 effect_sizes rows. Full
  detail in `CHANGELOG.md`.

- **Two-hundred-thirtieth batch (10 records, 2026-09-27),
  fifty-third batch from the 543-record pool.** `new_batch_pool.json[520:530]`.
  Shrestha (2013, logistic-regression study of self-organized network
  capital and RWSSP infrastructure-funding success, Nepal, S1140) —
  **INCLUDE**. Hajek & Petruzela (2016, E06 tariff-pricing sustainability
  econometrics, Czech Republic) — **EXCLUDE (E06)**. Kayser et al.
  (2019, E12 WASH gender-measurement perspectives article) — **EXCLUDE
  (E12)**. Hannah et al. (2021, E01 gender-quota
  governance-representation study, WRUA committees Kenya) — **EXCLUDE
  (E01)**. Agarwal (2011, E01 broad wealth-quartile urban health
  disparities, India) — **EXCLUDE (E01)**. Berk et al. (1980, E06
  water-conservation demand-management econometrics, California) —
  **EXCLUDE (E06)**. Kane (2012, E01 hydropolitics/disaster-narrative
  ethnography, Buenos Aires) — **EXCLUDE (E01)**. Wutich (2011, E01
  informal reciprocity/moral-economy coping-strategy study, Cochabamba)
  — **EXCLUDE (E01)**. Target "AFRICA: Barriers to investment in water
  are lowering" (2011) — **WRONG_FILE_RETRIEVED**: delivered PDF was
  instead Cotula et al. (2009), an unrelated agricultural-land-deals
  report. Ananga (2015, dissertation on community participation in
  water production/management, Kisumu Kenya) — **LEFT UNDECIDED**:
  title/authorship confirmed correct, but the Google Drive extraction
  delivered only front matter and Chapters 1-3, omitting the empirical
  results chapters (4-7); record left open per the undecided-record
  rule, file not moved.
  `extraction_database.csv`/`evidence_map.csv` updated (S1140,
  1,137 → 1,138 rows each); `effect_sizes.csv` updated (55 → 56 rows
  -- S1140 added as Family B); `exclusion_log.csv` updated (1,096 →
  1,103 rows; E01 484 → 488, E06 104 → 106, E12 46 → 47); duplicate
  audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,418 open records);
  schema validation re-run clean.
  Running totals: 2,241/3,659 screened (1,138 include/1,103 exclude),
  1,418 open (including 20 wrong_file_retrieved), 1,138 extracted
  studies, 56 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-first batch (10 records, 2026-09-27),
  fifty-fourth batch from the 543-record pool.** `new_batch_pool.json[530:540]`.
  Victor (2019, ethnographic case study of "DIY formalisation" and
  informal-settlement legal-status gating water-service eligibility,
  Marikana South Africa, S1141) — **INCLUDE**. Smith & Hanson (2003,
  cost-recovery/disconnection policy case study, urban poor water
  access, Cape Town, S1142) — **INCLUDE**. Both qualitative, no
  regression-based effect estimate — not added to effect_sizes.csv.
  Sinha & Pokhriyal (2001, E01 Tehri Dam resettlement/rehabilitation
  evaluation, India) — **EXCLUDE (E01)**. Okpala (1980, E01 broad
  economic-development essay on water-supply constraints, Nigeria) —
  **EXCLUDE (E01)**. Katani (2010, E01 legal-pluralism/water-resource
  tenure dissertation, spring forests, Ukerewe Tanzania) — **EXCLUDE
  (E01)**. Staddon et al. (2018, E01 household rainwater-harvesting
  adoption-decision study, Uganda) — **EXCLUDE (E01)**. Shrestha, Roth
  & Joshi (2018, E01 informal water-resource contestation ethnography,
  peri-urban Kathmandu) — **EXCLUDE (E01)**. Roth et al. (2019, E01
  policy-discourse synthesis, peri-urban South Asia) — **EXCLUDE
  (E01)**. Paerregaard (2013, E01 irrigation/water-resource governance,
  Cabanaconde Peru) — **EXCLUDE (E01)**. Target "Stream-flow bill bad
  for state" (Pederson 2009) — **WRONG_FILE_RETRIEVED**: delivered PDF
  was instead an unrelated computer-science paper on stream-processing
  optimizations.
  `extraction_database.csv`/`evidence_map.csv` updated (S1141-S1142,
  1,138 → 1,140 rows each); `effect_sizes.csv` unchanged (56 rows);
  `exclusion_log.csv` updated (1,103 → 1,110 rows; E01 488 → 495);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,409 open records);
  schema validation re-run clean.
  Running totals: 2,250/3,659 screened (1,140 include/1,110 exclude),
  1,409 open (including 21 wrong_file_retrieved), 1,140 extracted
  studies, 56 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-second batch (3 records, 2026-09-27), fifty-fifth
  and final batch from the 543-record pool.** `new_batch_pool.json[540:543]`.
  `new_batch_pool.json` is now fully exhausted; a fresh Drive re-sweep for
  new deliveries is the next step. Jones, Greenberg, Kaufman & Drew (1978,
  regression study of administrative service-delivery rules and
  differential sanitation-resource distribution, three Detroit
  bureaucracies, S1143) — **INCLUDE**, added to effect_sizes.csv as
  Family C. Tukahirwa (2011, logit-regression study of social-proximity
  trust and urban-poor access to NGO/CBO-supplied sanitation services,
  Kampala Uganda, S1144) — **INCLUDE**, added to effect_sizes.csv as
  Family B. Krueger, Rao & Borchardt (2019, E12 Capital Portfolio
  Approach water-security index/framework paper) — **EXCLUDE (E12)**.
  `extraction_database.csv`/`evidence_map.csv` updated (S1143-S1144,
  1,140 → 1,142 rows each); `effect_sizes.csv` updated (56 → 58 rows --
  S1143 added as Family C, S1144 as Family B); `exclusion_log.csv`
  updated (1,110 → 1,111 rows; E12 47 → 48); duplicate audit
  (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,406 open records);
  schema validation re-run clean.
  Running totals: 2,253/3,659 screened (1,142 include/1,111 exclude),
  1,406 open (including 21 wrong_file_retrieved), 1,142 extracted
  studies, 58 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-third batch (10 records, 2026-09-27), first batch
  drawn from a large new Google Drive delivery (510 PDFs, reconciled by a
  background agent: 464 already-decided duplicates moved to Processed, 45
  genuinely open records queued for screening, 1 fresh delivery for a
  previously-flagged wrong_file_retrieved record still wrong).**
  Gopakumar (2012, PPP-driven water-supply reform book, Bangalore/Chennai/
  Kochi India, S1145) — **INCLUDE**. Breen & Gillanders (2024, Afrobarometer
  corruption/water-access probit study, multi-country Africa, S1146) —
  **INCLUDE**, added to effect_sizes.csv as Family C. Romero (2022,
  private/public water-management history, Colombia, S1147) — **INCLUDE**.
  Amis & Kumar (2000, E01 broad infrastructure/poverty study, Visakhapatnam
  India) — **EXCLUDE (E01)**. Santana et al. (2023, E05 theoretical
  geography paper, Brazilian Northeast) — **EXCLUDE (E05)**. Five records
  flagged wrong_file_retrieved this batch (an unusually high rate):
  R180DB01E1A79, R1F37F14B3722, R1F2EDC030C66, R1ECC532A797B, R1D27DF36A4B5
  — each delivered a completely unrelated paper. A sixth, previously-
  flagged record (RE07A5B3A53CD) was re-delivered and re-checked, and is
  still the wrong file (same unrelated Toulouse thesis as before).
  `extraction_database.csv`/`evidence_map.csv` updated (S1145-S1147,
  1,142 → 1,145 rows each); `effect_sizes.csv` updated (58 → 59 rows --
  S1146 added as Family C); `exclusion_log.csv` updated (1,111 → 1,113
  rows; E01 495 → 496, E05 133 → 134); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,401 open records); schema validation re-run clean.
  Running totals: 2,258/3,659 screened (1,145 include/1,113 exclude),
  1,401 open (including 26 wrong_file_retrieved), 1,145 extracted
  studies, 59 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-fourth batch (10 records, 2026-09-27), a full
  wash.** Second batch of 10 from the 45-record open queue. All 10
  records turned out to be wrong_file_retrieved. A new, more insidious
  failure mode was confirmed for 7 of the 10 (R1D096BB71916,
  R198209A1D839, R189CB69DDE8B, R16D87BB47C02, R14569CA54EA8,
  R131D44D2032B, R1261BA60DC49): the Drive file's own filename/title
  metadata matched the target citation exactly, but the actual PDF
  content behind that fileId was a completely unrelated paper -- caught
  only by reading full-text content, not by the filename check alone.
  The remaining 3 (R19D28505FC8A, R155835EF1B8F, R13BB56FEF2D1) were
  ordinary title+content mismatches, two from an apparent
  predatory-journal source (abstract-only, "request full paper"). No
  includes, no excludes, no extraction/evidence_map/effect_sizes changes.
  `full_text_retrieval_queue.csv` regenerated (1,401 open records,
  unchanged); schema validation re-run clean.
  Running totals: 2,258/3,659 screened (1,145 include/1,113 exclude),
  1,401 open (including 36 wrong_file_retrieved, up from 26), 1,145
  extracted studies, 59 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-fifth batch (10 records, 2026-09-27), third batch
  from the 45-record open queue.** Salazar Adams, Haro Velarde & Loera
  Burnes (comparative institutional-capacity case study, Saltillo/
  Hermosillo Mexican municipal water utilities, S1148) — **INCLUDE**.
  Martinez-Fernandez et al. 2020 (Water Alternatives, EU Water Framework
  Directive regulatory-paradigm transition, Spain/Portugal, S1149) —
  **INCLUDE**. World Bank & Inter-American Development Bank 2018
  ("Transforming Karachi into a Livable and Competitive Megacity,"
  multi-agency institutional/legal fragmentation and informal-settlement
  status as determinants of water/sanitation access, Karachi, S1150) —
  **INCLUDE**. EEA/WHO Regional Office for Europe ("Water and health in
  Europe," a water-quality/public-health report) — **EXCLUDE (E03)**. Six
  records flagged wrong_file_retrieved this batch: R0EF03089DEC3,
  R0999DC7092C9, R08432C1433E1, and R0142AEB4AB16 were ordinary
  title+content mismatches (R08432C1433E1 notably delivered the identical
  wrong content — a Mexico migration/water-rights paper — already flagged
  wrong for a different record_id, R13BB56FEF2D1, in Batch 234, now
  confirmed a repeat delivery under a second record_id); R0E7A7452FD2B and
  R7C6EB2B41FD4 are two more instances of the content-behind-filename
  mismatch failure mode first identified in Batch 234 (filename/title
  metadata matched the target exactly, but the actual PDF content was an
  unrelated paper, caught only by reading full text).
  `extraction_database.csv`/`evidence_map.csv` updated (S1148-S1150,
  1,145 → 1,148 rows each, all three qualitative-synthesis-eligible only);
  `effect_sizes.csv` unchanged (59 rows — no regression-based effect
  estimate among the three includes); `exclusion_log.csv` updated
  (1,113 → 1,114 rows; E03 33 → 34); duplicate audit (exact-DOI +
  study_id) found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,397 open records); schema validation re-run clean.
  Running totals: 2,262/3,659 screened (1,148 include/1,114 exclude),
  1,397 open (including 42 wrong_file_retrieved), 1,148 extracted
  studies, 59 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-sixth batch (15 records, 2026-09-27), final batch
  from the 45-record open queue -- queue now fully exhausted.** Covered
  the 2 records inadvertently skipped between Batch 234 and Batch 235
  (R117905075AEC, R116235C8172D) plus the final 13 in the queue. Beall,
  Crankshaw & Parnell 2000 (Journal of Southern African Studies, historical
  racial housing-type determinants of water/sanitation/electricity access,
  Johannesburg, S1151) — **INCLUDE**. Marra 2008 (Rural Society, gendered
  impacts of water-policy reform, Malawi, S1152) — **INCLUDE**. Das &
  Takahashi 2014 (International Development Planning Review,
  non-participation of low-income households in community-managed water
  projects, India, S1153) — **INCLUDE** (contains a genuine multivariate
  logistic regression, but on a program-participation outcome rather than
  a water-access outcome, so no `effect_sizes.csv` entry under this
  project's strict access-outcome requirement). Marumahoko, Afolabi, Sadie
  & Nhede 2020 (Strategic Review for Southern Africa, governance and urban
  service delivery post-devolution, Zimbabwe, S1154) — **INCLUDE**. Oumar &
  Tewari 2012 (development of water-management institutions, Cameroon,
  S1155) — **INCLUDE**. Goldman 2007 (Geoforum, World Bank-driven "Water
  for All!" privatization-policy diffusion with South African
  cutoff/cholera-outbreak evidence, S1156) — **INCLUDE**. All six
  qualitative; no effect_sizes.csv entries. Nine records flagged
  wrong_file_retrieved this batch: R117905075AEC, R16E56D8BCECE,
  R746C33035455, and RA38256CBC26F were ordinary title+content mismatches;
  R116235C8172D, RC8E1C6959D2C, RD08AB246F841, RD7C03A60934A, and
  RD841349D5ED3 are five more instances of the content-behind-filename
  mismatch failure mode first identified in Batch 234 -- the highest count
  in a single batch so far.
  `extraction_database.csv`/`evidence_map.csv` updated (S1151-S1156,
  1,148 → 1,154 rows each); `effect_sizes.csv` unchanged (59 rows);
  `exclusion_log.csv` unchanged (1,114 rows -- no excludes this batch);
  duplicate audit (exact-DOI + study_id) found no new duplicates;
  `full_text_retrieval_queue.csv` regenerated (1,391 open records); schema
  validation re-run clean.
  Running totals: 2,268/3,659 screened (1,154 include/1,114 exclude),
  1,391 open (including 51 wrong_file_retrieved), 1,154 extracted
  studies, 59 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Drive reorganization (2026-09-27, later that day)**: created a
  dedicated "wrong_file records" Google Drive folder and consolidated
  every file corresponding to a `wrong_file_retrieved` record_id into it
  (51 record_ids located Drive-wide by filename prefix, 0 not found),
  regardless of which folder each had previously been sitting in. Pure
  Drive-organization change; no screening-database fields or counts
  affected.

- **Two-hundred-thirty-seventh batch (69 records, 2026-09-28), a new,
  much larger Drive delivery (774 PDFs, "Sep 26 2026" folder) reconciled,
  and a systemic retrieval-tool failure mode identified.** Reconciliation
  found 677 already-decided duplicates (moved to Processed), 28
  re-appearances of already-flagged wrong_file records (confirmed already
  correctly parked in the new "wrong_file records" folder -- a stale read
  from two concurrent background agents, not genuine re-deliveries), and
  69 genuinely open records. Of those 69: 1 include, 0 excludes, 68
  wrong_file_retrieved, 1 left undecided (empty/unreadable Drive
  extraction, R0908697F9FE5). **Root-cause finding**: the delivery tool's
  own tracking file showed 99 records harvested via fuzzy "title word
  match" against local Zotero storage at confidence as low as 40% (95 of
  99 below 80%), yet all self-labeled `RETRIEVED_AND_VERIFIED`; 65 of this
  batch's 69 open records fell inside that low-confidence set, and direct
  full-text verification confirmed 68 of 69 as wrong-file. This tool's
  self-reported verification status is now a disclosed, named limitation
  -- never trust it without reading actual content.
  **RC8E1C6959D2C** (Samano Romero & Chavez-Mejia 2025, "Water Access in
  Mexico City: A Review of Local Research Approaches") -- **INCLUDE** →
  **S1157**. This corrects a Batch 236 wrong_file_retrieved flag: the
  correct target content was found, by direct full-text reading, mislabeled
  under a different record_id (R023B3A0D827A) in the new delivery -- a
  genuine delivery-side cross-contamination, confirmed via the read tool's
  own `.viewUrl`/`.title` fields. R023B3A0D827A itself is flagged
  wrong_file_retrieved, since its own target citation remains unretrieved.
  `extraction_database.csv`/`evidence_map.csv` updated (S1157, 1,154 →
  1,155 rows each); `effect_sizes.csv` unchanged (59 rows -- S1157 is a
  qualitative narrative review); `exclusion_log.csv` unchanged (1,114 rows
  -- no excludes); duplicate audit (exact-DOI + study_id) found no new
  duplicates; `full_text_retrieval_queue.csv` regenerated (1,390 open
  records); schema validation re-run clean.
  Running totals: 2,269/3,659 screened (1,155 include/1,114 exclude),
  1,390 open (including 118 wrong_file_retrieved), 1,155 extracted
  studies, 59 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-eighth batch (50 records, 2026-09-28), a second
  reconciliation pass on the same "Sep 26 2026" folder found 967 unique
  files (193 more than the 774 already accounted for), confirming the
  delivery process is continuously adding files, not a one-time drop.**
  870 already-decided duplicates moved to Processed; 43 re-appearances of
  already-flagged wrong_file records moved to the "wrong_file records"
  folder (by database status only); 50 genuinely new open records
  screened here. Behnke et al. 2020 (WASH/environmental-health scoping
  review in protracted displacement, S1158), de Lima et al. 2026 (ESG
  strategies for a fiscally-constrained Brazilian sanitation utility,
  S1159), Ananga 2015 (community participation in Kisumu NGO water
  schemes -- genuine logistic regression but on a satisfaction/hygiene
  outcome, not access, so no effect size, S1160), Ikeda 2024 (Florianopolis
  dam-rupture disaster-governance case study, S1161), and Kurian &
  McCarney eds. 2010 (peri-urban WSS comparative case-study volume, S1164)
  -- all **INCLUDE**, qualitative. Two genuine quantitative access-outcome
  studies also included: Subramanyam 2020 (multilevel regression, 3,547
  Indian urban local governments; local-government administrative
  category significantly predicts water-coverage growth, -4.062 to -5.432
  percentage points depending on category, p<0.05-0.01; **Family C**,
  S1162) and Cronk et al. 2021 (multilevel logistic regression, 2,677
  rural schools, 14 LMICs; external WaSH-program funding significantly
  predicts basic on-premises water service, OR=1.4, p=0.021; **Family B**,
  S1163). 41 wrong_file_retrieved. 2 left undecided per the partial/
  unusable-extraction rule: R0908697F9FE5 (empty extraction, confirmed a
  second time) and RBEDB6556B711 (Olmstead 2004 "Thirsty Colonias" --
  bibliographic front matter confirmed exactly, but body text was only
  JSTOR boilerplate, no substantive content recoverable).
  `extraction_database.csv`/`evidence_map.csv` updated (S1158-S1164, 1,155
  → 1,162 rows each); `effect_sizes.csv` updated (59 → 61 rows -- S1162
  Family C, S1163 Family B); `exclusion_log.csv` unchanged (1,114 rows);
  duplicate audit found no new duplicates; `full_text_retrieval_queue.csv`
  regenerated (1,383 open records); schema validation re-run clean.
  Running totals: 2,276/3,659 screened (1,162 include/1,114 exclude),
  1,383 open (including 159 wrong_file_retrieved), 1,162 extracted
  studies, 61 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Two-hundred-thirty-ninth batch (23 records, 2026-09-28), a complete
  wash -- a third, finer-grained reconciliation pass (16 hex-prefix bucket
  queries defeating a persistent Drive search-pagination anomaly) finally
  cleared the "Sep 26 2026" folder.** Found 69 more files: 41 duplicates
  moved to Processed, 3 more wrong_file re-appearances moved to the
  wrong_file records folder, 25 open (23 new plus the 2 already-known
  undecided records, left untouched). All 23 new records: **WRONG_FILE**.
  Two received special attention as likely resurfacing of already-flagged
  targets under duplicate record_ids (Carrera 2015 "Sanitation and social
  power" and Stopnitzky 2012 "Household Sanitation... India," both
  mirroring Batch 238 targets) -- both confirmed independent, unrelated
  wrong deliveries, not the correct paper. Two deliveries were not
  research papers at all: a law-firm client letter and an Ontario court
  decision, both self-labeled "verified" by the delivery tool -- the same
  failure mode now confirmed to extend to non-academic document types.
  Folder now treated as exhaustively reconciled: 1,036 unique PDFs seen
  across all three passes. No database changes beyond wrong_file flags;
  `full_text_retrieval_queue.csv` regenerated (1,383 open, count
  unchanged); schema validation re-run clean.
  Running totals: 2,276/3,659 screened (1,162 include/1,114 exclude),
  1,383 open (including 182 wrong_file_retrieved), 1,162 extracted
  studies, 61 effect_sizes rows. Full detail in `CHANGELOG.md`.

- **Full-text retrieval phase (Phase 6) formally closed by researcher
  decision, 2026-09-28.** The researcher reported that institutional
  access to further database providers is exhausted and confirmed the
  current corpus (1,162 included, fully extracted studies) is judged
  sufficient for a review of unusually comprehensive scope for
  administrative law, comparative law, and sociolegal studies -- the same
  kind of judgment-call closure, at the same level of seriousness, as the
  2026-09-11 database-search closure. Every one of the 1,383 records
  never screened at full-text stage (because the correct full text was
  never obtained) was updated to record this permanently: 182 keep their
  `wrong_file_retrieved` status; the remaining 1,201 (previously a mix of
  blank and several legacy statuses -- `not_retrievable`,
  `no_oa_copy_found`, `oa_page_candidate`, `undecided` -- inherited from
  at least one earlier, undocumented tooling generation) were normalized
  to `not_retrievable`, the value `DATA_DICTIONARY.md` already documents.
  `final_decision` was not touched for any of them -- they stay correctly
  blank permanently, per the standing rule against forcing a decision
  when the correct source material was never in hand.
  `full_text_retrieval_queue.csv` regenerated one final time (1,383,
  unchanged in count); schema validation re-run clean (13/13) after this
  1,383-row mass update. **This closes Phase 6 at 2,276/3,659 screened
  (62.2%) -- the final figure, not a running total.** Extraction,
  evidence classification, risk-of-bias appraisal, human reviewer_2, and
  Phase 11's quantitative-feasibility write-up are all unaffected by this
  closure and remain open work on the 1,162 studies already included.
  README.md and `06_outputs/prisma/prisma_flow.md` updated throughout to
  reflect this as final rather than provisional/growing. Full detail in
  `CHANGELOG.md`, "Full-text retrieval phase (Phase 6) formally closed by
  researcher decision."

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
- Full-text screening itself is far from complete: 1,485 of the 3,659
  Phase-5 includes have been assessed; 2,174 records have not yet been
  reached, not confirmed unretrievable, since retrieval depends entirely
  on the researcher supplying full-text PDFs. Eleven of those 2,174
  (`wrong_file_retrieved`) were retrieved but did not match their target
  record or lacked complete content, and are pending a correct/complete
  re-retrieval attempt.
- Extraction (Phase 8) is caught up with screening completely — all 795
  current full-text includes are extracted, no outstanding gap.
- **No risk-of-bias rating has been performed on the great majority of the
  795 extracted studies** (a first 12-study partial pilot batch was
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
- Effect sizes now exist for 38 studies in `effect_sizes.csv` (added
  2026-09-16, extended 2026-09-17 and in later full-text-screening
  batches through 2026-09-27, most recently S795 -- Hailu, Osorio &
  Tsukada's probit difference-in-differences estimate of Bolivian
  water-utility privatization's effect on piped-water access (0.077,
  SE 0.016, p<0.01), not mapped to a Family A/B/C synthesis family),
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
