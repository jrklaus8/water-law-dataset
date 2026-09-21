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
- Full-text screening itself is far from complete: 1,105 of the 3,659
  Phase-5 includes have been assessed; 2,554 records have not yet been
  reached, not confirmed unretrievable, since retrieval depends entirely
  on the researcher supplying full-text PDFs.
- Extraction (Phase 8) is caught up with screening completely — all 548
  current full-text includes are extracted, no outstanding gap.
- **No risk-of-bias rating has been performed on the great majority of the
  548 extracted studies** (a first 12-study partial pilot batch was
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
