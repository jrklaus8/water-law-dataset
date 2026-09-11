# PRISMA 2020 Flow Diagram — Data

Status: **Identification and title/abstract screening (first pass only)
are populated with real counts as of 2026-09-11, now that Scopus's own
18-batch plan is fully executed. Everything from "Reports sought for
retrieval" onward is still genuinely unfilled — that work has not
started.** Per `PROJECT_SPEC.md` §14, no number below is estimated,
illustrative, or a placeholder dressed as data; every filled count traces
to `01_search/raw_exports/`, `01_search/deduplicated/`, or
`02_screening/title_abstract/screening_database.csv` as of this date, and
is annotated as provisional wherever it is.

**Two things this diagram is not, yet:**

1. **Only one Tier 1 database (Scopus) has actually been searched.**
   Scopus itself is now complete per its own plan
   (`01_search/scopus_batch_plan_2026-08-26.md`, all 18 batches done),
   but every other Tier 1/2/legal-repository database in
   `SEARCH_PROTOCOL.md` remains untouched. Every count below undercounts
   what a completed Phase 3 search across all planned databases will
   produce.
2. **Title/abstract screening below is a first pass by one AI reviewer
   (`reviewer_1`, `Claude-AI-1stpass-2026-09-10`) only.** `PROTOCOL.md`'s
   two-reviewer process needs a human `reviewer_2` and conflict
   resolution before any inclusion/exclusion at this stage is final — see
   `02_screening/title_abstract/REVIEWER_2_README.md`. Treat every number
   under "Screening" as provisional.

```
Identification
  Records identified from databases (n = 5,984)
    [Scopus only -- SEARCH_018 (500, 2026-08-26) + all 18 planned batches
    from scopus_batch_plan_2026-08-26.md (5,484, 2026-09-10/11, the last
    of them SEARCH_026 received 2026-09-11). No other Tier 1/2 database
    has been searched.]
  Records identified from grey literature / registers (n = 37)
    [34 from an explicitly non-systematic Claude WebSearch pilot
    (SEARCH_003-017, 2026-08-25 -- SEARCH_PROTOCOL.md S7, not a
    substitute for a real database search) + 3 SOURCES.md exemplars
    added directly to the pipeline.]
  Records removed before screening:
    Duplicate records removed (n = 541)
      [code/search/deduplicate.py, DOI-match + title/year-similarity
      match, full merge log in 01_search/deduplicated/merge_log.csv.
      record_id is a stable content hash -- see CHANGELOG.md. One of the
      541 is worth flagging: the same DOI appeared in both SEARCH_026
      and SEARCH_027 with a trivial title-capitalization/year-metadata
      discrepancy -- a Scopus indexing quirk for that one paper, not a
      pipeline error; correctly DOI-matched and merged.]
    Records marked ineligible by automation tools (n = 0)
    Records removed for other reasons (n = 0)

Screening  [reviewer_1 (AI) first pass only -- see caveat above]
  Records screened (n = 5,445)
    [Of 5,480 unique records, 35 have no real abstract (pre-2026-09-10
    exports or grey-lit records lacking one) and were deliberately left
    unscreened rather than judged on title alone -- see
    title_only_triage_memo.md for why title-only judgments are
    non-binding in this project.]
  Records excluded at title/abstract (n = 3,747, PROVISIONAL)
    [reviewer_1 only. Breakdown by code, all provisional:
      E01 wrong topic (n = 1,621)
      E02 wrong population (n = 21)
      E03 wrong exposure / water-quality-only (n = 70)
      E04 wrong outcome (n = 273)
      E05 no empirical evidence (n = 513)
      E06 engineering only (n = 813)
      E07 wrong service (n = 347)
      E08 duplicate (n = 19)
      E09 insufficient information (n = 69)
      E10 inaccessible full text (n = 0)
      E11 wrong jurisdiction/context (n = 1)
      E12 wrong study design (n = 0)
    189 further records marked "unsure" by reviewer_1 are NOT counted
    as excluded here -- they carry forward with the includes pending
    full-text review; see below.]
  Reports sought for retrieval (n = )
  Reports not retrieved (n = )
  Reports assessed for eligibility (n = )
  Reports excluded at full text, by reason (E01-E12, see INCLUSION_EXCLUSION.md):
    E01 wrong topic (n = )
    E02 wrong population (n = )
    E03 wrong exposure (n = )
    E04 wrong outcome (n = )
    E05 no empirical evidence (n = )
    E06 engineering only (n = )
    E07 wrong service (n = )
    E08 duplicate (n = )
    E09 insufficient information (n = )
    E10 inaccessible full text (n = )
    E11 wrong jurisdiction/context (n = )
    E12 wrong study design (n = )

Included
  Studies included in systematic review (n = )
  Studies included in quantitative evidence synthesis (n = )
  Studies included in restricted meta-analysis, by family (n = ), if any
```

**Provisional pool carried forward** (not a PRISMA box on its own, but the
number that matters for planning Phase 6): 1,698 records are currently
either `include` (1,509) or `unsure` (189) after the reviewer_1 pass —
see `02_screening/title_abstract/reviewer_2_queue.csv`. This is the upper
bound of what full-text screening will need to retrieve, pending
`reviewer_2` narrowing it.

Source data for these counts is
`02_screening/title_abstract/screening_database.csv` and
`02_screening/exclusion_log/exclusion_log.csv` — this file is a summary
derived from those, not an independent source of truth. Re-derive rather
than hand-edit this file's numbers when the underlying data changes.
