# Evidence Classification (Phase 10) — Start Here

`evidence_map.csv` is the one-row-per-study summary used to plan
synthesis (`PRISMA_WORKFLOW.md` §"Evidence classification matrix",
`CODEBOOK.md`). Once a study has been extracted
(`03_extraction/extraction_form/EXTRACTION_FORM.md`) and appraised
(`04_quality/appraisal_forms/APPRAISAL_FORM.md`), it's ready for a row
here.

## Run the builder first

```
python3 code/analysis/build_evidence_map.py \
    --extraction-db 03_extraction/extracted_data/extraction_database.csv \
    --evidence-map 05_analysis/descriptive/evidence_map.csv
```

Idempotent and append-only, same discipline as `init_screening_db.py` and
`init_full_text_db.py` — safe to rerun any time, never overwrites a row
you've already completed. It fills in three fields mechanically:

- **`study_design_class`** — inverts the design↔tool mapping
  `RISK_OF_BIAS.md` §1 already commits to (whatever tool
  `extraction_database.csv`'s `risk_of_bias_tool` names, mapped back to
  the design it's for).
- **`mechanism_family`** — from which of the four top-level mechanism
  booleans (`eligibility`/`burden`/`discretion_accommodation`/
  `enforcement`) are true; `MULTIPLE` if more than one.
- **`legal_context`** / **`institutional_context`** — copied straight
  from `legal_system` / `regulatory_model`, already recorded during
  extraction — not re-typed, just carried over.

## What it leaves blank, and why — these need your judgment

- **`study_design_class`** stays blank if `risk_of_bias_tool` was the
  project's own Legal Institutional Evidence Appraisal Framework — that
  framework covers both doctrinal and jurimetric studies
  (`RISK_OF_BIAS.md` §2), and the tool name alone can't tell you which
  this particular study is.
- **`mechanism_family`** stays blank if none of the four booleans came
  through true — check the extraction, this shouldn't normally happen if
  `CODEBOOK.md` §4 was followed.
- **`evidence_level`** is *never* derived — `DATA_DICTIONARY.md` is
  explicit this is a narrative tier, not a numeric score. Write it as
  prose, referencing the design-matched appraisal in `RISK_OF_BIAS.md` §1.
- **`outcome_family`** is *never* derived, and this is the one worth
  reading carefully: `PROJECT_SPEC.md` §7's own outcome hierarchy lists
  "approval/refusal" under **both** the primary outcome (formal
  connection) and under the secondary "administrative outcomes" category.
  A study coded with `application_success`/`refusal`/`delay_outcome` in
  `extraction_database.csv` could genuinely belong to either
  `primary_connection` or `administrative_outcome` depending on what was
  actually being approved, refused, or delayed — the connection
  application itself, or some other administrative process. There is no
  mechanical rule that resolves this from the boolean fields alone.
  **Read the study and decide** which family the specific
  approval/refusal/delay concerned; guessing here risks exactly the
  "manufactured comparability" `PROJECT_SPEC.md` §3 warns against, since
  outcome family is what determines which studies can ever be pooled
  together.
- **`quantitative_synthesis_eligible`** / **`qualitative_synthesis_eligible`**
  are *never* derived — see "Then Phase 11" below.

## Then Phase 11 (quantitative feasibility)

Phase 11 applies `ANALYSIS_PLAN.md` §2's decision tree **per candidate
synthesis family** (`PROJECT_SPEC.md` §8's Families A/B/C), not once per
study in isolation — a family only becomes eligible once enough
comparable studies exist and clear every branch of that tree (empirical
study → clearly defined exposure → clearly defined outcome → comparable
population/context → meaningful comparator → calculable effect estimate
→ substantively comparable estimand → enough independent studies →
acceptable heterogeneity). That's a corpus-level methodological judgment,
not a per-study mechanical fact, so there's no script to run ahead of
time here the way `build_evidence_map.py` helps with Phase 10 — the
decision tree in `ANALYSIS_PLAN.md` §2 already **is** the complete
process; apply it once `evidence_map.csv` is populated enough to see
which families have enough studies to even ask the question. Set
`quantitative_synthesis_eligible`/`qualitative_synthesis_eligible` in
`evidence_map.csv` directly once you've walked the tree for a study's
family.
