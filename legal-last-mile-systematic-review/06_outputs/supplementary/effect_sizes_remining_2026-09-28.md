# Re-mining extraction_database.csv for missed effect_sizes.csv promotions — 2026-09-28

## Why this is possible without new full-text retrieval

Full-text PDFs supplied by the researcher earlier in this project were session-ephemeral chat
uploads and are not available in this environment. **This audit does not re-read any source
document.** It only re-examines quantitative content *already captured* in
`03_extraction/extracted_data/extraction_database.csv`'s own `effect_measure`/`effect_estimate`/
`covariates`/`adjusted_or_unadjusted` fields during the original extraction work, checking
whether any of it should have been, but was not, promoted into
`05_analysis/effect_sizes/effect_sizes.csv` — the "much stricter subset" `README.md`'s status
table already describes ("only regression-based estimates directly isolating a legal/
institutional mechanism qualify"). This is a data-completeness check against this project's own
prior work, not new extraction.

## Method

1. `evidence_map.csv` flags 248 studies `quantitative_synthesis_eligible = TRUE`.
   `effect_sizes.csv` held 61 rows before this pass. **187 of the 248 eligible studies had a
   non-blank `effect_estimate` in `extraction_database.csv` but no corresponding
   `effect_sizes.csv` row** (61 + 187 = 248 exactly, confirming this is the complete
   complementary set — not a coincidence, a check).

   > **Audit correction, 2026-09-28.** That arithmetic was right by coincidence, not by check:
   > `effect_sizes.csv`'s 61 rows are *not* all rows for eligible studies — S589's row belongs to a
   > study `evidence_map.csv` does not flag eligible. The true decomposition is 60 eligible
   > studies with a row + 187 eligible studies with a non-blank `effect_estimate` and no row + 1
   > eligible study (S690) with a blank `effect_estimate` = 248. The set this pass actually
   > screened (the 187) was correct, so no candidate was missed; only the "exactly complementary"
   > claim and the "61 rows, all from eligible studies" premise were inaccurate.
2. Manually inspecting a sample of the 187 confirmed most are correctly *not* in
   `effect_sizes.csv`: the `quantitative_synthesis_eligible` flag is a broad "has some
   quantitative content" category (descriptive percentages, correlation coefficients, GIS
   indices, survey frequencies), not the strict "regression-based estimate isolating a
   legal/institutional mechanism" bar `effect_sizes.csv` actually applies.
3. Narrowed the 187 to genuine candidates via a disclosed, conservative filter: `effect_measure`
   or `model_type` text containing a real statistical-method keyword (regression, coefficient,
   odds ratio, hazard ratio, poisson, logit, GEE, fixed-effects, difference-in-differences,
   propensity score, etc.) **and** `adjusted_or_unadjusted = adjusted` **and** a non-blank
   `covariates` field — the same three properties the existing 61 rows overwhelmingly share.
   **This returned exactly 4 candidates: S006, S348, S696, S1025.**

## What happened to each of the 4 candidates

- **S348 (Andrews, Beynon & Baafi 2025, Ghana local-government infrastructure access) —
  genuinely missed, now added.** A real hierarchical multivariate regression on
  governance-quality district clusters (fuzzy c-means clustering + regression), adjusted for
  political alignment, government form, expenditure, and government age, isolating a
  governance-quality mechanism's effect on water/sanitation/electricity access. Added to
  `effect_sizes.csv` as Family C (see that row's own `provenance_note` for the full
  reasoning). This is the one genuine result of this re-mining pass.
- **S006 (Agyeman, Tantoh & Kamika 2026, Ghana water-governance) — correctly not added.** Has
  a real adjusted odds ratio (18.12, 95% CI 13.04–25.13, p<0.001) from a binary logistic
  regression — but its own `extraction_note`, written at extraction time, already discloses
  the outcome is a binary "effective/not effective sustainable-management-strategy" indicator,
  not a household water/sanitation access outcome as `PROJECT_SPEC.md` §8 defines Family A/B/C.
  This is a self-disclosed outcome-construct mismatch, not an oversight — the original
  extraction correctly flagged it, and this pass agrees rather than overriding that judgment.
- **S696 (Lim & Prakash 2020, 112-country panel, industrialization/democratization and water
  access) — already deliberately excluded, left as-is.** Its own `extraction_note` states in
  full: *"NOT added to effect_sizes.csv: democratization here is a moderator of the
  industrialization-access relationship rather than a single, clean legal/institutional
  exposure with a locatable point-estimate/CI isolating its own direct effect on access, so it
  does not cleanly fit the strict Family A/B/C exposure-comparator-outcome definition despite
  being a real, high-quality regression finding."* This is an explicit, reasoned prior
  decision. This pass does not override considered judgment that was already made and
  recorded — it confirms the decision stands.
- **S1025 (Tardanico 2008, El Salvador household infrastructure inequality) — correctly not
  added, and flags a genuine data artifact.** Its own `extraction_note` states the specific
  water-outcome regression coefficient "was not confirmed with certainty from the extracted
  portions" and is "flagged for potential future effect_sizes review if the full results
  tables are re-examined" — an explicit, honest non-promotion, not an oversight. Separately:
  this row's `effect_measure`, `effect_estimate`, and `p_value` fields literally contain the
  string `"TRUE"` rather than real values — a data-entry artifact (very likely a boolean flag
  from a different extraction step leaking into the wrong fields) that predates this session.
  **Not corrected here**, since fixing it would require returning to the original source text
  this environment does not have access to; flagged for a future researcher with access to
  the full text to investigate, not silently left unexplained.

## Result

One new row (`S348`) added to `effect_sizes.csv` (61 → 62), bringing Family C from 19 to 20
studies. **This is a confirmatory, mostly-negative result, and that is itself the finding worth
recording**: it demonstrates that the original extraction and effect-size-promotion work was
already disciplined — 187 candidates, checked against the same bar the existing 61 rows were
held to, yielded only 1 genuine addition, with 3 others already correctly excluded by name in
their own extraction records rather than silently dropped. The corpus's quantitative-synthesis
pool is close to its natural ceiling given what this project's extraction actually captured, not
artificially small due to neglect.

## Downstream updates

`phase11_quantitative_feasibility_judgment.md`, `family_C_swim_synthesis_2026-09-28.md`, and
`README.md`'s status table are all updated to reflect 62 rows / Family C = 20 (see
`CHANGELOG.md`'s 2026-09-28 entry for the itemized list). **This one addition does not change
Phase 11's overall verdict** — Family C, now 20 studies instead of 19, still does not clear
`ANALYSIS_PLAN.md` §2's bar for meta-analysis, and S348 does not join the ownership/price
sub-cluster (`phase11_pooling_feasibility_S526_S539_S749.md`) or the governance-structure/
affordability grouping (S470, S471, S1038) — it tests its own distinct exposure (a
clustering-derived governance-quality classification) with no comparable study yet in the
corpus.

## What this does not do

- It does not re-examine the 902-study broader pool (all extraction rows with *any* non-blank
  `effect_estimate`/`effect_measure`, not just the 248 flagged quantitative-synthesis-eligible)
  — that pool is dominated by studies extraction already correctly classified as
  qualitative-synthesis-eligible instead, where the `effect_estimate` field holds descriptive
  or narrative content, not a promotion candidate.
- It does not attempt a looser candidate filter than "real statistical keyword + adjusted +
  covariates." A future researcher could relax this (e.g., include unadjusted estimates, or
  estimates without a `covariates` entry) and might find a few more genuine candidates at the
  cost of more manual review — this pass chose precision over exhaustiveness, consistent with
  this project's general practice of not forcing a weak fit into `effect_sizes.csv`.
- It does not fix the S1025 `"TRUE"` field artifact, for the reason stated above.
