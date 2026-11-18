# Normalizing evidence_map.csv's study_design_class — 2026-09-28

`DATA_DICTIONARY.md` documents `study_design_class` as an 8-value enum: `experimental` /
`quasi_experimental` / `observational` / `qualitative` / `doctrinal` / `jurimetric` /
`systematic_review_secondary` / `mixed_methods`. Several documents written earlier today
(`04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`, `PRISMA_WORKFLOW.md`'s Phase 10
row) flagged, without fixing, that the live data violates this schema: **482 distinct free-text
values** were sitting in the field, against 8 documented ones — a genuine enum-compliance bug,
not just staleness, inherited from `build_evidence_map.py`'s original judgment-call population
plus every design reclassification made since (including several made earlier today) never
being propagated back into this field.

## Method

`risk_of_bias_tool` — fully audited and internally consistent as of today's corpus-wide
risk-of-bias work (`RISK_OF_BIAS.md` §4) — maps unambiguously onto 6 of the 8 enum values, per
`RISK_OF_BIAS.md` §1's own design-to-tool table:

| `risk_of_bias_tool` | canonical `study_design_class` | n |
|---|---|---|
| RoB 2 | `experimental` | 5 |
| ROBINS-I | `quasi_experimental` | 63 |
| JBI Cross-Sectional | `observational` | 166 |
| MMAT | `mixed_methods` | 205 |
| CASP Qualitative | `qualitative` | 246 |
| AMSTAR 2 | `systematic_review_secondary` | 22 |

For these 707 studies, `evidence_map.csv`'s `study_design_class` was set to the canonical value
wherever it did not already match. **228 of 707 needed correction; 479 were already correct.**
A sample of the mismatches confirms this is real, not spurious: 10 of them (S150, S422, S423,
S426, S428, S432, S452, S454, S467, S551) are studies today's own JBI-reassignment batch
(`reassignment_batch_2026-09-28.md`) moved from MMAT to JBI — their `risk_of_bias_tool` was
correctly updated at the time, but `evidence_map.csv` was never touched to match, leaving them
stuck at `mixed_methods` until this pass. The rest are spelling/formatting variants already
converging on the same canonical value (`mixed-methods case study`, `mixed-methods`,
`cross-sectional mixed-methods household survey` → `mixed_methods`) or genuine leftover
free-text from before any systematic normalization was attempted.

`evidence_map.csv`'s distinct-value count for this field: **482 → 297.**

## What was deliberately not touched, and why

The remaining 455 studies — 449 tagged with the project's own Legal Institutional Evidence
Appraisal Framework, plus 12 `NONE` — were **not** forced into `doctrinal` or `jurimetric`,
even though those are the two enum values that would seem closest. Checking their actual
`study_design` free text (`extraction_database.csv`) shows why: this population spans
ethnographic case studies (15), qualitative case studies (10+), historical-institutional case
studies (9+), comparative institutional case studies, documentary/institutional analyses,
policy analyses, and only a genuine handful of studies whose own description contains the word
"jurimetric" (4) or "doctrinal" (3) outright. `RISK_OF_BIAS.md` §2 itself describes this
framework's intended scope as covering "doctrinal/documentary/jurimetric/institutional-case-study
analyses" — **four** design types, not the two the enum actually has room for. Forcing this
population's real methodological diversity into a binary doctrinal-vs-jurimetric split would
produce a classification that reads as decisive but is not — exactly the kind of "manufactured
comparability" this project's own rules elsewhere warn against, this time applied to a
categorical field rather than an effect size.

**This is a genuine, disclosed limit of `DATA_DICTIONARY.md`'s current schema, not a limit of
this pass's effort.** A future researcher extending this project should consider adding a
category (something like `qualitative_institutional_case_study`, or splitting `qualitative`
into household-level and institutional-level variants) before attempting to fully resolve this
remaining 455-study population — see `DATA_DICTIONARY.md`'s own field definition, which this
note does not amend.

## Downstream effect

This does not change `risk_of_bias_tool`, any `risk_of_bias_rating`, any `effect_sizes.csv`
row, or any Phase 11/13 conclusion — it only corrects `evidence_map.csv`'s own
`study_design_class` field to match data this project already trusts elsewhere. 1,162 rows
unchanged in count; `code/analysis/validate_schemas.py` re-run clean.

## Audit addendum (2026-09-28, later the same day): 22 values re-synced

The repository audit re-ran the tool-implied mapping above against the *live*
`extraction_database.csv` and found **22 studies whose `study_design_class` no longer matched their
`risk_of_bias_tool`**, because those tools were reassigned *after* this normalization pass ran (the
counts in the table above — JBI 166, MMAT 205, CASP 246, AMSTAR 2 22 — are the pass-time counts, not
the final ones, which are JBI 140, MMAT 206, CASP 263, AMSTAR 2 24). The 22 were re-synced with the
same rule: 19 CASP-tool studies had been left at `observational` (S403, S410, S412, S414, S415, S416,
S417, S419, S420, S424, S431, S433, S441, S446, S447, S451, S456, S459, S460 → `qualitative`), 1 MMAT-tool
study at `observational` (S461 → `mixed_methods`), and 2 AMSTAR 2-tool studies at `qualitative`
(S344, S350 → `systematic_review_secondary`). Script: `code/provenance/audit_and_repair/resync_study_design_class.py`.
After the re-sync every study whose tool implies a design in the 6-row table above carries the
matching value; the Legal Framework/`NONE` studies (461 at the final counts, not 455) remain free
text by design.
