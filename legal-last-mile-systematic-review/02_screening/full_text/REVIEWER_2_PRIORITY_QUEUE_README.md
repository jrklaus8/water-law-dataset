# Reviewer 2 — prioritised queue (2026-09-28)

`full_text_reviewer_2_priority_queue_2026-09-28.csv` is the recommended order of work for a human second reviewer of the
full-text decisions. The older `full_text_reviewer_2_queue.csv` (175 records from an early snapshot) is superseded.
**One-page working checklist: `REVIEWER_2_CHECKLIST.md`.** At 2026-10-14 a human has confirmed 197 of the 1,078 includes (S001–S200 less three the PI later excluded) and the PI has ruled on 166 excludes and 104 further includes in the adjudications, in A6 tier 1 and in the A26 SWiM core confirmations (open items A16, A19, A22–A26 and A6; 467 of 2,277 full-text decisions, 20.5%, carry human verification or adjudication); no other exclude has been independently confirmed by a human (`AI_USE_STATEMENT.md`). **The queue holds 225 rows (73 + 102 + 50).** Progress on 2026-10-14: **tier 1 (73 rows) is complete**: every row carries a CK ruling (the 18 rows with a blind second-model decision in `A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv`, the other 54 in `A6_TIER1_BATCHES_2_TO_4_CK_SHEET_2026-10-14.csv`, one earlier A16 reversal). All were confirmations, and 13 included reports carry a `BORDERLINE INCLUDE` note (a thin rule-type link, or borderline on criterion 3). Tiers 2 (102 excludes) and 3 (50 includes) are untouched.

## What is in it

| Tier | Rows | Selection | Why |
|---|---|---|---|
| 1 | 73 (46 include, 27 exclude) | **Every** decided row whose reviewer label was not recorded (an AI label was inferred on 2026-10-14, open item A2) | Provenance not recorded at the time; the inferred label is not human review |
| 2 | 102 excludes | Seeded random sample, stratified by exclusion code (about 100 in proportion, at least 3 per code; codes E08 duplicate and E10 inaccessible-text are not sampled because a second reader cannot re-make them from the paper) | Checks that AI excludes are correct; errors here silently remove eligible studies |
| 3 | 50 includes | Seeded random sample of includes beyond S001–S200 (optional) | Checks that AI includes — and the extraction built on them — are correct |

Seed `20260928`; regenerate with `python3 code/screening/build_reviewer2_priority_queue.py` (deterministic). Sampling proportions
and the seed are in the script, so the sample can be audited and re-drawn.

## How to use it

1. Work tier by tier, in `priority_rank` order. Get the full text (the DOI/URL columns; the PDFs are not in this repository).
2. **Form your own decision first**, using `INCLUSION_EXCLUSION.md`. Only then read the last column, `ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT`, to avoid anchoring on the AI.
3. Fill the four `reviewer_2_*` columns. Use `cannot_tell` rather than forcing a decision.
4. Record confirmed decisions with `code/screening/update_full_text_record.py` (sets `reviewer_2` in `full_text_screening_database.csv`); log any disagreement in `CHANGELOG.md` with the record and the reason, and re-run `code/analysis/current_figures.py --write`.
5. Report agreement per tier. A high overall agreement is *not* reassuring on its own (the title/abstract stage's 99.8% is already flagged as suspiciously high): look at the tier-2 sample by exclusion code and at the tier-1 rows separately.

## Limits

The samples are for spot-checking, not a certified error rate: 102 of the 1,199 excludes and 50 of the 881 unconfirmed includes (1,078 less the 197 confirmed) cannot
bound the true error rate tightly. If a tier shows disagreement, widen it rather than extrapolate.
