# Extraction Form — Phase 7/8 Working Guide

This is the document to have open while actually reading a full-text
study and filling in a row of
`03_extraction/extracted_data/extraction_database.csv`.
`CODEBOOK.md` defines what each field *means*; this form turns that into
an ordered, fillable checklist so nothing gets skipped mid-read. One pass
through this form = one row in `extraction_database.csv` (one row per
study **and outcome family** — see step 7 on multiple effects).

Read `CODEBOOK.md` in full at least once before extracting your first
study. This form assumes it, and doesn't repeat its definitions.

## Before you start: is this study in scope for extraction at all?

Only a study with `final_decision == "include"` in
`02_screening/full_text/full_text_screening_database.csv` reaches this
form. If you're piloting (Phase 7), see `PILOT_EXTRACTION.md` in this
same folder for how the ~10 pilot studies are selected — don't hand-pick
studies yourself outside that process, to avoid unconsciously favoring
studies that will extract cleanly.

## 1. Identification (`CODEBOOK.md` §1)

- Assign `study_id`: next unused `S0NN` — check the last row of
  `extraction_database.csv`, never reuse a retired one even if that study
  is later dropped.
- `citation`, `doi`, `publication_year`, `publication_type` (journal
  article / working paper / report / thesis / book chapter / conference
  paper — use whatever the source actually is, don't force it into
  "journal article"), `language`, `database_source` (which database in
  `screening_database.csv` this came from), `peer_reviewed`.

## 2. Jurisdiction (`CODEBOOK.md` §2)

`country`, `subnational_unit` (state/province/municipality if the study
is subnational — blank if genuinely national), `legal_system` (civil law
/ common law / mixed / customary — as it actually operates for this
population, not just the country's textbook classification),
`urban_rural`, `service_provider` (public utility / private concession /
community-managed / informal — whatever the study reports),
`regulatory_model` (centralized / decentralized / fragmented — per
`PROJECT_SPEC.md` §"institutional_context" usage in `evidence_map.csv`).

## 3. Population — decide the unit of analysis explicitly

**Do this before extracting a single number.** `PROJECT_SPEC.md` §4: a
study is the review-level unit, but an *effect estimate* is the
meta-analytic unit, and the two must never be conflated. Ask: is this
study's outcome measured at the household level, the community level, or
some other level entirely? Get `household_level` / `community_level`
right now — the answer determines whether this study's effect can ever be
pooled with another study's later, and is much harder to reconstruct
after the fact than to record correctly the first time.

Fill: `population`, `sample_size`, `household_level`, `community_level`,
`income_group`, `tenure_status`, `legal_status`, `indigenous_population`,
`migrant_population`.

## 4. Legal mechanism (`CODEBOOK.md` §4)

Identify which of the four families the study's exposure actually is —
`ELIGIBILITY` / `BURDEN` / `DISCRETION_ACCOMMODATION` / `ENFORCEMENT` —
then check off every detailed code the study actually documents from the
list in `CODEBOOK.md` §4 (a study may carry more than one; boolean
columns in `extraction_database.csv`, so leave unobserved codes as
false/blank rather than guessing). **A code earns its place by describing
a mechanism this specific study observed** — resist the pull to check a
box just because the study's topic is adjacent to that mechanism.

## 5. Outcomes (`CODEBOOK.md` §5)

Same discipline as mechanisms: check only the outcome(s) this study
actually measured, and map each to `PROJECT_SPEC.md` §7's hierarchy
(primary connection / effective access / economic access / administrative
outcome) — record that mapping in `05_analysis/descriptive/evidence_map.csv`
once the study is fully extracted (`outcome_family` field there), not in
this file. **Never pool two outcomes across families just because both
use the word "access" in the abstract** — that's exactly the shortcut
`PROJECT_SPEC.md` §7 exists to block.

## 6. Mediators and moderators (`CODEBOOK.md` §6)

Note anything the study discusses as a mediator or moderator in
`extraction_note` (free text) even though most of these stay contextual
rather than becoming formal statistical variables — see
`ANALYSIS_PLAN.md` §"Meta-regression" for the minimum-study-count rule
before any moderator gets promoted to a covariate. Don't pre-judge that
here; just record what the study itself discusses.

## 7. Statistical information — one row per study **and outcome family**

If the study reports multiple effects, `CODEBOOK.md` §12's first-paper
default is **one prespecified effect per study and outcome family** — do
not create a row for every reported coefficient. Choose the effect that
best matches this review's primary specification for that outcome family
(the paper's own primary/preferred model, not the largest or most
significant one — picking on significance is exactly the kind of
selection `PROJECT_SPEC.md`'s anti-confirmation-bias rule, §11, exists to
prevent). If a study reports genuinely distinct effects for *different*
outcome families, that's multiple rows (same `study_id`, different
outcome), not a violation of the one-effect default.

Fill: `effect_measure`, `effect_estimate`, `lower_CI`, `upper_CI`,
`standard_error`, `p_value`, `extraction_sample_size` (may differ from
population `sample_size` in §3 if the effect is on a subsample —
record both, they answer different questions), `adjusted_or_unadjusted`,
`covariates`, `model_type`.

**Leave a cell blank, never zero, for anything not reported or not
calculable** (`DATA_DICTIONARY.md`) — a blank and a true zero mean
different things downstream and must never be conflated.

## 8. Study quality (`CODEBOOK.md` §8, `RISK_OF_BIAS.md`)

Classify the study's design first, then apply the matched tool from
`RISK_OF_BIAS.md` §1 (RoB 2 / ROBINS-I / JBI cross-sectional / JBI cohort
/ CASP qualitative / MMAT / the project's own Legal Institutional
Evidence Appraisal Framework for legal-empirical studies that fit none of
the conventional designs). Record which tool you used in
`risk_of_bias_tool` alongside `risk_of_bias_rating` — the rating's scale
is meaningless without knowing which tool produced it (a RoB 2 "some
concerns" is not the same scale as a ROBINS-I "moderate"). Also:
`study_design`, `selection_bias`, `measurement_bias`, `confounding`,
`attrition`, `reporting_bias`, `legal_measurement_quality`,
`outcome_measurement_quality`.

## 9. Mechanism certainty (`CODEBOOK.md` §9)

Set `mechanism_certainty` (0–4) honestly against the table in
`CODEBOOK.md` §9 — this distinguishes *the authors argue X* (0–1) from
*the study directly demonstrates X* (2–4). Resist rating a well-written,
persuasively-argued study higher than its actual design supports.

## 10. Evidence status (`CODEBOOK.md` §10, `PROJECT_SPEC.md` §13)

Set `evidence_status` **per extracted statistic, not per study** — a
single row can legitimately mix an `OBSERVED` effect estimate with an
`ASSUMED` standard error you reconstructed from a reported confidence
interval. If you do reconstruct or convert anything (a logistic
coefficient to an odds ratio, a linear-probability coefficient
deliberately left unconverted, an SE from a CI), log the exact
transformation in `09_data_dictionary/transformations/` per
`DATA_DICTIONARY.md`'s transformation log — this is a per-value audit
trail, not optional.

## 11. Provenance (`CODEBOOK.md` §11, `REPRODUCIBILITY.md` §3)

**Never skip this section.** Every extracted statistic must be traceable
back to an exact spot in the source document — `source_document`, `page`,
`table`, `figure`, `section`, `exact_location`, plus `extraction_note`
(anything about the extraction judgment call itself), `researcher` (your
name/initials), `date_extracted`. `REPRODUCIBILITY.md` §3 has a worked
example. A number with no provenance is not usable in this review,
however correct it might be.

## 12. Dependent effect sizes (`CODEBOOK.md` §12)

Already addressed in step 7 above for the first-paper default. Only
depart from "one effect per study and outcome family" once the evidence
base is large enough to justify a multilevel/robust-variance/multivariate
dependence model — see `ANALYSIS_PLAN.md` §"Dependent effect sizes" for
when that threshold is met. Don't reach for those models just because
they're available.

## After extracting: two more files, not this one

- **`05_analysis/descriptive/evidence_map.csv`** — one row per study,
  the evidence-classification summary (`study_design_class`,
  `evidence_level`, `mechanism_family`, `outcome_family`,
  synthesis-eligibility flags, `legal_context`, `institutional_context`).
  Fill this once the study's `extraction_database.csv` row(s) are
  complete — it's a derived summary, not a duplicate data-entry step.
- **`05_analysis/effect_sizes/effect_sizes.csv`** — only for effects
  actually judged eligible for quantitative synthesis, per
  `ANALYSIS_PLAN.md` §2's decision tree. Most extracted studies will
  *not* have a row here even though every included study has a row in
  `extraction_database.csv` — inclusion in the review and eligibility for
  pooling are different questions.

## Two reviewers, same discipline as screening

`PROTOCOL.md` §6 calls for extraction accuracy checks the same way it
calls for two-reviewer screening. For the pilot (Phase 7) specifically,
see `PILOT_EXTRACTION.md` for how disagreements during piloting are
supposed to be used — to revise the codebook/form, not just to resolve
that one study's numbers.
