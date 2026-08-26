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
  (the Gaikwad & Thomas 2026 exemplar). Total unscreened pool: **536
  records**. The title-only triage memo has not yet been extended to cover
  these 500 — it still only covers the original 37.

## What has not been done

- **No database has been fully searched, and only Scopus has been
  searched at all, partially** (`SEARCH_PROTOCOL.md` §7–8) — Web of
  Science, HeinOnline, Westlaw, Lexis, ProQuest, Sociological Abstracts,
  CanLII, and Rechtspraak.nl remain entirely unsearched, and Scopus itself
  is ~91% unexported. This remains the actual Phase 3 requirement, largely
  unmet.
- No screening decision has been made on any record.
- No study has been included or excluded from the review.
- No data has been extracted.
- No risk-of-bias appraisal has been performed.
- No quantitative-feasibility determination has been made for any candidate
  synthesis family.
- No effect size, pooled or otherwise, exists in this project.

## Why this file exists in its current, empty form

`PROJECT_SPEC.md` §14 (operating instructions) prohibits inventing
literature, results, sample sizes, effect sizes, or confidence intervals,
and prohibits claiming an exhaustive search that was not actually
performed. Populating this file with plausible-sounding preliminary
findings before the search is run would violate that rule regardless of how
carefully hedged the language was. The next entry in this file should be
written only once `01_search/raw_exports/` contains real, logged search
exports (`SEARCH_PROTOCOL.md` §6) and `02_screening/` contains real
screening decisions.
