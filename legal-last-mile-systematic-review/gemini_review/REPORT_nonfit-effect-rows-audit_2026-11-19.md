# Report: Task J — Two-Phase Blind + Adversarial Audit of All 21 Reasoned Non-Fit Rows in `effect_sizes.csv`

*AI-generated second-model output. Not human verification.*

---

## 1. Summary Counts (`21` Non-Fit Rows)

- **Readable verified source PDFs:** **`21 / 21`** (`0` `not accessible`).
- **Printed-number verification (`gemini_numbers_match_paper`):** `{'no (discrepancy found)': 11, 'yes': 10}`
- **Non-fit classification verdict (`gemini_nonfit_verdict`):** `{'questionable_could_fit_family_ABC': 6, 'moot_study_appears_ineligible': 10, 'justified_nonfit': 5}`
- **Review-level scope consistency check (`gemini_review_eligibility_flag`, applying the `2026-10-13/14` narrow Criterion 2 & Criterion 4 `CK` rulings):** `{'borderline_flag_for_pi': 9, 'likely_ineligible_flag_e03_e04_e05_e07': 10, 'eligible_keep_included': 2}`
- **Quote verification:** **`164 / 168` (`97.62%`)** verified.

---

## 2. Per-Study Audit Matrix (`21` Rows)

| Study ID | Paper Read | Numbers Match PDF? | Non-Fit Verdict | Review Eligibility Flag (`CK` Scope Consistency) | Key Finding / Critique |
|---|---|---|---|---|---|
| `S149` | `full text` | `no (discrepancy found)` | `questionable_could_fit_family_ABC` | **borderline_flag_for_pi** | Claude's stored row for S149 fails adversarial audit on three independent fronts: (1) obvious abstract-only numerical extraction that omits explicitly printed SEs/95… |
| `S178` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | Adversarial audit of S178 (Sikder et al. 2018, Conflict and Health) uncovers two substantive defects in Claude's stored `effect_sizes.csv` row alongside a review-lev… |
| `S353` | `full text` | `yes` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | 1. SCOPE & ELIGIBILITY AUDIT (E03 / E05 UNDER A24/A26/A28 STANDARD): Marcillo, Krometis, and Krometis (2021) is an ecological environmental-justice geospatial study … |
| `S358` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | Adversarial audit of S358 (Williams et al., 2025) identifies both material extraction/specification discrepancies in `effect_sizes.csv` (indicating Abstract-only ext… |
| `S388` | `full text` | `yes` | `questionable_could_fit_family_ABC` | **borderline_flag_for_pi** | 1. Numeric accuracy vs. substantive mischaracterization: Every printed statistic in Claude's stored row matches Table 5 (p. 8) and Section 3.1 (p. 6) verbatim (Local… |
| `S434` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | Adversarial audit reveals two major defects in the stored `effect_sizes.csv` record and its `exclusion_from_pooling_reason` for S434 (Frempong, Stadelmann, & Thiam, … |
| `S445` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | 1. Statistical & Provenance Audit (`no_discrepancy_found` due to sample-size N mismatch): All four stored point estimates and p-values for North vs. Center-West scho… |
| `S448` | `full text` | `no (discrepancy found)` | `questionable_could_fit_family_ABC` | **borderline_flag_for_pi** | 1. Truncated-Excerpt Extraction Defect in `effect_sizes.csv` (Wrong Primary Outcome & Missing Statistics): Claude's `provenance_note` reveals that S448 was originall… |
| `S483` | `full text` | `yes` | `justified_nonfit` | **borderline_flag_for_pi** | 1. Quantitative & Specification Audit: Every regression statistic stored in Claude's `effect_sizes.csv` row (R1 RR = 5.78, 95% CI 5.34–6.25, p < 0.001; R2 RR = 3.80,… |
| `S489` | `full text` | `yes` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | 1. Numerical & Metric Audit (`numbers_match_paper = "yes"`): Every number stored in `effect_sizes.csv` matches Table 2 (PDF p. 8) and Section 3.3 (PDF p. 5) verbatim… |
| `S491` | `full text` | `yes` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | Adversarial audit of S491 (Sempewo et al., 2021) confirms that while Claude's extracted numerical statistics match Table 5 and Section 3.3 of the PDF verbatim, the s… |
| `S590` | `full text` | `no (discrepancy found)` | `justified_nonfit` | **borderline_flag_for_pi** | 1. Numerical & Specification Conflation Discrepancy: Claude's stored row (`effect_estimate`, `provenance_note`, and `exclusion_from_pooling_reason`) misreports `"SKE… |
| `S606` | `full text` | `yes` | `justified_nonfit` | **borderline_flag_for_pi** | 1. Non-fit classification (`justified_nonfit`): CK's A26 ruling (2026-10-14) moving S606 out of Family C to reasoned non-fits is completely justified. Conceptually, … |
| `S636` | `full text` | `yes` | `justified_nonfit` | **borderline_flag_for_pi** | 1. Numerical & Packaging Audit: Every printed number in Claude's `effect_sizes.csv` row matches Lewis (2014) verbatim across pp. 417, 420, 425, 427 (Table 7), 429, a… |
| `S649` | `full text` | `yes` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | 1. NUMERICAL AUDIT: Every point estimate, standard error, p-value, and sample size in Claude's stored `effect_sizes.csv` row matches Tables 3, 4, and 5 of González R… |
| `S795` | `full text` | `no (discrepancy found)` | `questionable_could_fit_family_ABC` | **eligible_keep_included** | 1. SCOPE & ELIGIBILITY (KEEP INCLUDED): Under the strict 2026-10-13 / 2026-10-14 CK scope standard (A24/A26/A28), S795 (Hailu, Osorio, & Tsukada 2012) clearly satisf… |
| `S869` | `full text` | `no (discrepancy found)` | `questionable_could_fit_family_ABC` | **borderline_flag_for_pi** | Three substantive issues emerge from auditing S869 against the full text: 1. CRITICAL SIGN / DIRECTION INVERSION IN `effect_sizes.csv`: Claude defines the exposure a… |
| `S1136` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | (1) Numerical accuracy audit (`no_discrepancy_found` = discrepancy found): Claude's `effect_sizes.csv` row contains three material extraction errors. First, in Table… |
| `S1140` | `full text` | `no (discrepancy found)` | `moot_study_appears_ineligible` | **likely_ineligible_flag_e03_e04_e05_e07** | 1. Scope & Eligibility Audit (`likely_ineligible_flag_e03_e04_e05_e07` / `moot_study_appears_ineligible`): Applying the exact 2026-10-13 / 2026-10-14 CK scope standa… |
| `S1166` | `full text` | `yes` | `questionable_could_fit_family_ABC` | **eligible_keep_included** | 1. Statistical Accuracy & Provenance Slip: Every numerical figure in Claude's `effect_sizes.csv` row matches Jiang and Zheng (2014) exactly, including the headline T… |
| `S331` | `full text` | `yes` | `justified_nonfit` | **borderline_flag_for_pi** | 1. Statistical & Factual Audit of Stored Row: Every numerical value in `effect_sizes.csv` (`OR = 4.27`, `95% CI: 3.07–5.93`, blank `standard_error`, regression `n = … |
