# Reviewer 2 — prioritised queue (2026-09-28)

`full_text_reviewer_2_priority_queue_2026-09-28.csv` is the recommended order of work for a human second reviewer of the
full-text decisions. The older `full_text_reviewer_2_queue.csv` (175 records from an early snapshot) is superseded.
**One-page working checklist: `REVIEWER_2_CHECKLIST.md`.** Currently only 100 of the 1,159 includes (S001–S100) and none of the
1,117 excludes have been independently confirmed by a human (`AI_USE_STATEMENT.md`).

## What is in it

| Tier | Rows | Selection | Why |
|---|---|---|---|
| 1 | 73 (47 include, 26 exclude) | **Every** decided row with no reviewer label | Provenance unknown; nothing can be said about who or what made these decisions |
| 2 | 103 excludes | Seeded random sample, stratified by exclusion code (about 100 in proportion, at least 3 per code; codes E08 duplicate and E10 inaccessible-text are not sampled because a second reader cannot re-make them from the paper) | Checks that AI excludes are correct; errors here silently remove eligible studies |
| 3 | 50 includes | Seeded random sample of includes beyond S001–S100 (optional) | Checks that AI includes — and the extraction built on them — are correct |

Seed `20260928`; regenerate with `python3 code/screening/build_reviewer2_priority_queue.py` (deterministic). Sampling proportions
and the seed are in the script, so the sample can be audited and re-drawn.

## How to use it

1. Work tier by tier, in `priority_rank` order. Get the full text (the DOI/URL columns; the PDFs are not in this repository).
2. **Form your own decision first**, using `INCLUSION_EXCLUSION.md`. Only then read the last column, `ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT`, to avoid anchoring on the AI.
3. Fill the four `reviewer_2_*` columns. Use `cannot_tell` rather than forcing a decision.
4. Record confirmed decisions with `code/screening/update_full_text_record.py` (sets `reviewer_2` in `full_text_screening_database.csv`); log any disagreement in `CHANGELOG.md` with the record and the reason, and re-run `code/analysis/current_figures.py --write`.
5. Report agreement per tier. A high overall agreement is *not* reassuring on its own (the title/abstract stage's 99.8% is already flagged as suspiciously high): look at the tier-2 sample by exclusion code and at the tier-1 rows separately.

## Limits

The samples are for spot-checking, not a certified error rate: 103 of 1,117 excludes and 50 of 1,059 unconfirmed includes cannot
bound the true error rate tightly. If a tier shows disagreement, widen it rather than extrapolate.
