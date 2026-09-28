# PRISMA 2020 Flow Diagram — Data

Status: **Identification and title/abstract screening (first pass only)
are populated with real counts as of 2026-09-11, now that the search
phase has closed by researcher decision** (candidate pool judged large
enough to move to screening — see `SEARCH_PROTOCOL.md` §7 and
`PRISMA_WORKFLOW.md` Phase 3). **"Reports sought for retrieval" has a
real count (n = 3,659) as of 2026-09-12, the size of the tracking file
Phase 6 was seeded with. Full-text retrieval/screening (Phase 6) was
itself formally closed by researcher decision on 2026-09-28** (the
researcher's institutional access to further database providers is
exhausted, and the corpus was judged large and comprehensive enough for
the review's purposes — the same kind of judgment call as the
2026-09-11 search closure). **Final figures: of 3,659, 2,276 were
assessed (1,160 include / 1,116 exclude — 1,162 / 1,114 before two duplicate records were merged on 2026-09-28), and "Reports not retrieved" is
1,383 — 182 flagged `wrong_file_retrieved` (a delivery was attempted and
the wrong content arrived) and 1,201 `not_retrievable` (no successful
retrieval attempt). These 1,383 will not grow further, and will not be
resolved, unless a future researcher makes a new, separately-recorded
decision to reopen retrieval.** Per `PROJECT_SPEC.md` §14, no number below is estimated,
illustrative, or a placeholder dressed as data; every filled count traces
to `01_search/raw_exports/`, `01_search/deduplicated/`, or
`02_screening/title_abstract/screening_database.csv` as of this date, and
is annotated as provisional wherever it is.

**Two things this diagram is not, yet:**

1. **The search phase closed with real, documented gaps.** Databases
   actually searched: Scopus (18/18 planned batches), Web of Science
   (`SEARCH_035`), HeinOnline (`SEARCH_036`-`SEARCH_038`, minimal real
   yield), ProQuest (`SEARCH_039`, full account-based export) and
   ProQuest/Sociological Abstracts (`SEARCH_040`), and JSTOR (`SEARCH_041`,
   50 of 356 identified results). SSRN (`SEARCH_042`) and Westlaw/Lexis
   (`SEARCH_043`) were never searched at all — the phase was closed before
   either was reached; see `SEARCH_PROTOCOL.md` §7 for the full account.
   This is a real, disclosed limitation of this review's search strategy,
   not a placeholder gap awaiting completion.
2. **Title/abstract screening below shows reviewer_1 (AI) numbers only —
   a human `reviewer_2` pass has since completed (2026-09-12) but is not
   yet reflected in the boxes below**, which this file derives strictly
   from `screening_database.csv`'s `title_abstract_decision` (reviewer_1)
   field per its own re-derivation rule. The real post-reviewer_2 result:
   3,659 include / 6 exclude / 0 conflicts out of the 3,665 include+unsure
   records — see `PRISMA_WORKFLOW.md` Phase 5 and `CHANGELOG.md` for the
   number **and** an important caveat that must travel with it: the
   agreement rate between the two reviewers was unusually high (99.8%)
   for genuinely independent screening, flagged to and confirmed by the
   researcher before being recorded rather than treated as routine. Any
   manuscript reporting this step should disclose that caveat alongside
   the number.

```
Identification
  Records identified from databases (n = 34,557)
    [Scopus: SEARCH_018 (500) + all 18 planned batches (5,484) = 5,984.
    Web of Science: SEARCH_035, 4,058 (5 export batches). HeinOnline:
    SEARCH_037, 1 (SEARCH_036 was count-only, no export mechanism at
    71,226 hits; SEARCH_038's 3 records were never delivered). ProQuest:
    SEARCH_039, 7,728 (full account-based export). ProQuest/Sociological
    Abstracts: SEARCH_040, 16,736. JSTOR: SEARCH_041, 50 (of 356
    identified; the remaining 306 were never exported before the search
    phase closed). SSRN and Westlaw/Lexis were never searched -- see
    SEARCH_PROTOCOL.md S7.]
  Records identified from grey literature / registers (n = 37)
    [34 from an explicitly non-systematic Claude WebSearch pilot
    (SEARCH_003-017, 2026-08-25 -- SEARCH_PROTOCOL.md S7, not a
    substitute for a real database search) + 3 SOURCES.md exemplars
    added directly to the pipeline.]
  Records removed before screening:
    Duplicate records removed (n = 7,113)
      [code/search/deduplicate.py, DOI-match + title/year-similarity
      match, full merge log in 01_search/deduplicated/merge_log.csv.
      Heavy Scopus/WoS/ProQuest cross-database overlap is expected --
      several major academic databases index much of the same journal
      literature. record_id is a stable content hash -- see
      CHANGELOG.md.]
    Records marked ineligible by automation tools (n = 0)
    Records removed for other reasons (n = 0)

Screening  [reviewer_1 (AI) first pass only -- see caveat above]
  Records screened (n = 26,222)
    [Of 27,481 unique records, 1,259 have no real abstract (pre-2026-09-10
    exports or grey-lit/JSTOR records lacking one) and were deliberately
    left unscreened rather than judged on title alone -- see
    title_only_triage_memo.md for why title-only judgments are
    non-binding in this project.]
  Records excluded at title/abstract (n = 22,557, PROVISIONAL)
    [reviewer_1 only. Breakdown by code, all provisional:
      E01 wrong topic (n = 16,666)
      E02 wrong population (n = 51)
      E03 wrong exposure / water-quality-only (n = 263)
      E04 wrong outcome (n = 1,000)
      E05 no empirical evidence (n = 1,510)
      E06 engineering only (n = 1,617)
      E07 wrong service (n = 1,040)
      E08 duplicate (n = 26)
      E09 insufficient information (n = 208)
      E10 inaccessible full text (n = 0)
      E11 wrong jurisdiction/context (n = 1)
      E12 wrong study design (n = 175)
    E01's large share reflects the ProQuest/Sociological Abstracts
    round's much broader, noisier search (wire-service press releases,
    medical conference proceedings, a large general sociology-of-
    bureaucracy literature pulled in by thesaurus-term matching) rather
    than a screening-quality issue -- see search_log.csv's SEARCH_039/040
    notes and REVIEWER_2_README.md.
    603 further records marked "unsure" by reviewer_1 are NOT counted
    as excluded here -- they carry forward with the includes pending
    full-text review; see below.]
  Reports sought for retrieval (n = 3,659)
    [02_screening/full_text/full_text_screening_database.csv seeded
    2026-09-12 by code/screening/init_full_text_db.py from every
    screening_database.csv record with final_decision == "include" -- this
    is the population now in scope for retrieval, not yet the count
    actually retrieved. See the reviewer_2 agreement-rate caveat above
    before treating 3,659 as settled without qualification.]
  Reports not retrieved (n = 1,383, FINAL)
    [Phase 6 formally closed by researcher decision, 2026-09-28 --
    institutional access to further database providers exhausted; see
    CHANGELOG.md, "Full-text retrieval phase (Phase 6) formally closed by
    researcher decision." Of these 1,383: 182 are flagged
    wrong_file_retrieved (a delivery was attempted for this record and the
    wrong content arrived, confirmed by direct full-text reading) and
    1,201 are flagged not_retrievable (no successful retrieval attempt
    ever occurred, for a mix of historical reasons folded into this one
    closure). Neither group is claimed to be provably unobtainable by
    every conceivable means -- this is a judgment-call closure, exactly
    parallel to the 2026-09-11 database-search closure, not a claim of
    exhaustion.]
  Reports assessed for eligibility (n = 2,276, FINAL)
    [02_screening/full_text/full_text_screening_database.csv, as of the
    2026-09-28 Phase 6 closure. 62.2% of the 3,659 records sought for
    retrieval were actually screened; this is now the final figure for
    this box, not a provisional/growing one.]
  Reports excluded at full text, by reason (E01-E12, see INCLUSION_EXCLUSION.md; n = 1,116 total, FINAL after the 2026-09-28 duplicate merge):
    E01 wrong topic (n = 496)
    E02 wrong population (n = 34)
    E03 wrong exposure (n = 34)
    E04 wrong outcome (n = 77)
    E05 no empirical evidence (n = 134)
    E06 engineering only (n = 106)
    E07 wrong service (n = 26)
    E08 duplicate (n = 8)
    E09 insufficient information (n = 2)
    E10 inaccessible full text (n = 151)
    E11 wrong jurisdiction/context (n = 0)
    E12 wrong study design (n = 48)

Included
  Studies included in systematic review (n = 1,160, FINAL)
    [Full-text include count as of the 2026-09-28 Phase 6 closure (1,162 at closure,
    reduced by 2 when the repository audit's two live double-counted papers, S233 and
    S299, were merged into S1008 and S392 with the researcher's approval and their
    screening records re-classified as E08 duplicates). This
    figure will not grow further unless a future researcher makes a new,
    separately-recorded decision to reopen full-text retrieval for some or
    all of the 1,383 never-screened records.]
  Studies included in full extraction so far (n = 1,160)
    [03_extraction/extracted_data/extraction_database.csv, S001-S1164 (S227,
    S233, S299 and S399 documented duplicate gaps, see CHANGELOG.md). Fully caught up
    with the full-text include count as of 2026-09-27 -- no outstanding gap.]
  Studies included in quantitative evidence synthesis (n = 62 effect-size rows, as of 2026-09-28; 61 of them from quantitative-synthesis-eligible studies, plus S589's row, an unresolved eligibility inconsistency flagged by the repository audit)
    [05_analysis/effect_sizes/effect_sizes.csv, first populated 2026-09-16
    and extended in almost every full-text-screening batch since as new
    genuinely quantitative, non-fabricated exposure-vs-comparator studies
    cleared screening -- see CHANGELOG.md's dated batch entries for the
    complete study-by-study history (this paragraph previously narrated
    that history inline up to S649/2026-09-22 and was left unmaintained
    for several weeks of subsequent batches; it is now a pointer rather
    than a re-narration, to avoid the same drift recurring). Of the 62
    rows: 20 Family A, 6 Family B, 20 Family C, and 16 that carry no family
    because each was individually judged a reasoned non-fit to Family A/B/C
    (not a data-cleanliness gap -- see
    06_outputs/supplementary/phase11_blank_family_resolution_2026-09-28.md
    and README.md's Current project status table; an earlier version of this
    paragraph described 16 Family C and 19 blank rows, which the 2026-09-28
    Phase 11 follow-ups superseded). These are the studies with
    a genuine, non-fabricated exposure-vs-comparator contrast and a
    locatable effect estimate -- a much smaller, stricter subset than the
    247 studies evidence_map.csv flags quantitative_synthesis_eligible =
    TRUE, most of which are single-group descriptive statistics with no
    defined comparator. This figure is now final in the sense that no
    further full-text retrieval will add new candidate studies (Phase 6
    closed 2026-09-28); the blank-family rows were resolved
    2026-09-28, see above.]
  Studies included in restricted meta-analysis, by family (n = 0)
    [No pooling has occurred -- every effect_sizes.csv row has
    included_in_pooled_estimate = FALSE at this stage (project is still
    pre-Phase-12); each row cites the specific ANALYSIS_PLAN.md S2
    decision-tree branch preventing pooling for now, most commonly a
    single study per exposure-comparator definition.]
```

**Pool carried forward to Phase 6** (not a PRISMA box on its own, but the
number that matters for planning full-text screening): reviewer_1 marked
3,665 records `include` (3,062) or `unsure` (603) — see
`02_screening/title_abstract/reviewer_2_queue.csv`. reviewer_2 has since
reviewed all 3,665 and set `final_decision`: **3,659 include / 6 exclude**,
zero conflicts. **3,659 records** are the actual set Phase 6 should
retrieve full text for — see the reviewer_2 agreement-rate caveat above
before treating this number as settled without qualification.

Source data for these counts is
`02_screening/title_abstract/screening_database.csv` and
`02_screening/exclusion_log/exclusion_log.csv` — this file is a summary
derived from those, not an independent source of truth. Re-derive rather
than hand-edit this file's numbers when the underlying data changes.
