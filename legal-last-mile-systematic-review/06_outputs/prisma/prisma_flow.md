# PRISMA 2020 Flow Diagram — Data

Status: **Identification and title/abstract screening (first pass only)
are populated with real counts as of 2026-09-11, now that Scopus's own
18-batch plan is fully executed and Web of Science's first batch has
landed. Everything from "Reports sought for retrieval" onward is still
genuinely unfilled — that work has not started.** Per `PROJECT_SPEC.md`
§14, no number below is estimated, illustrative, or a placeholder dressed
as data; every filled count traces to `01_search/raw_exports/`,
`01_search/deduplicated/`, or
`02_screening/title_abstract/screening_database.csv` as of this date, and
is annotated as provisional wherever it is.

**Two things this diagram is not, yet:**

1. **Only two Tier 1 databases have actually been searched.** Scopus is
   complete per its own plan (`01_search/scopus_batch_plan_2026-08-26.md`,
   all 18 batches done). Web of Science has only its first batch in
   (`SEARCH_035`, 4,058 records) — whether that's the platform's full
   result set or more batches remain hasn't been confirmed by the
   researcher yet. Every other Tier 1/2/legal-repository database in
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
  Records identified from databases (n = 10,042)
    [Scopus: SEARCH_018 (500, 2026-08-26) + all 18 planned batches from
    scopus_batch_plan_2026-08-26.md (5,484, 2026-09-10/11) = 5,984.
    Web of Science: SEARCH_035, first batch only (4,058, 2026-09-11) --
    completeness of the WoS result set unconfirmed. No other Tier 1/2
    database has been searched.]
  Records identified from grey literature / registers (n = 37)
    [34 from an explicitly non-systematic Claude WebSearch pilot
    (SEARCH_003-017, 2026-08-25 -- SEARCH_PROTOCOL.md S7, not a
    substitute for a real database search) + 3 SOURCES.md exemplars
    added directly to the pipeline.]
  Records removed before screening:
    Duplicate records removed (n = 3,475)
      [code/search/deduplicate.py, DOI-match + title/year-similarity
      match, full merge log in 01_search/deduplicated/merge_log.csv.
      2,934 of these are Scopus/Web-of-Science cross-database overlap
      (expected -- both index a lot of the same journal literature),
      541 within-Scopus, plus record_id is a stable content hash -- see
      CHANGELOG.md.]
    Records marked ineligible by automation tools (n = 0)
    Records removed for other reasons (n = 0)

Screening  [reviewer_1 (AI) first pass only -- see caveat above]
  Records screened (n = 7,109)
    [Of 7,145 unique records, 36 have no real abstract (pre-2026-09-10
    exports or grey-lit records lacking one) and were deliberately left
    unscreened rather than judged on title alone -- see
    title_only_triage_memo.md for why title-only judgments are
    non-binding in this project.]
  Records excluded at title/abstract (n = 5,151, PROVISIONAL)
    [reviewer_1 only. Breakdown by code, all provisional:
      E01 wrong topic (n = 2,326)
      E02 wrong population (n = 24)
      E03 wrong exposure / water-quality-only (n = 78)
      E04 wrong outcome (n = 462)
      E05 no empirical evidence (n = 573)
      E06 engineering only (n = 1,201)
      E07 wrong service (n = 390)
      E08 duplicate (n = 26)
      E09 insufficient information (n = 70)
      E10 inaccessible full text (n = 0)
      E11 wrong jurisdiction/context (n = 1)
      E12 wrong study design (n = 0)
    248 further records marked "unsure" by reviewer_1 are NOT counted
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
number that matters for planning Phase 6): 1,958 records are currently
either `include` (1,710) or `unsure` (248) after the reviewer_1 pass —
see `02_screening/title_abstract/reviewer_2_queue.csv`. This is the upper
bound of what full-text screening will need to retrieve, pending
`reviewer_2` narrowing it.

Source data for these counts is
`02_screening/title_abstract/screening_database.csv` and
`02_screening/exclusion_log/exclusion_log.csv` — this file is a summary
derived from those, not an independent source of truth. Re-derive rather
than hand-edit this file's numbers when the underlying data changes.
