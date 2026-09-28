# Methods note: does a defensible common-metric transformation exist for the S526/S539/S749 ownership-price cluster?

**Status: written 2026-09-28**, per Phase 11's explicit instruction (§5.1, §8) that this
question "deserve[s] their own dedicated methods note before anyone attempts it, not a
decision made in passing." This note answers that question directly: **no defensible
transformation exists that would put all three studies on one common, poolable metric without
introducing researcher-invented assumptions the corpus does not support.** The cluster stays
in Family C's structured synthesis (SWiM), not meta-analysis. This is a methods finding, not a
default to caution — the reasoning is laid out below so a future researcher does not have to
re-derive it, and can see exactly what evidence would change the answer.

## 1. What the three studies actually measure

All three test the same **exposure** (private/investor-owned vs. public, cooperative, or
mixed-capital water utility ownership — an institutional-governance mechanism) against a
price/affordability **outcome**, and all three find the same **direction** (private ownership
associated with a worse affordability outcome for the household). But "same direction" is not
"same estimand" — `ANALYSIS_PLAN.md`'s opening rule is explicit that a mathematically
convertible statistic is not automatically a substantively comparable effect, and here the
three outcomes are not even superficially on convertible scales without added assumptions:

| Study | Outcome construct | Reported metric | Units | Effect | SE reported? |
|---|---|---|---|---|---|
| S526 | Rate-structure **progressivity** — the ratio of the unit price at a high usage tier (30,000 gal/mo) to the unit price at a low usage tier | Unit Price Ratio (UPR) | Dimensionless ratio | −0.167 (p<0.001) | No |
| S539 | Bill **level** and income-share **burden** | Annual household bill (USD); % of lowest-quintile income | USD; percentage points | +$144.04/yr (p<0.01); +1.55 pp (p<0.01) | No (std. coefficients 0.35/0.26 reported separately) |
| S749 | Tariff **level** | Water tariff per cubic metre | R$/m³ | +0.3456 R$/m³ (significant) | No |

## 2. Why S526 cannot be harmonized with the other two, in principle

S526's outcome is a **within-utility ratio between two price tiers** — it measures how
regressive or progressive a utility's own rate *schedule* is, not the *level* of what any
household actually pays. S539 and S749 both measure a price or bill **level** (how much a
household pays, in absolute or income-relative terms). These are different constructs, not
just different units: a utility could have a highly progressive rate structure (high UPR) and
still charge every household more in absolute terms than a utility with a flatter structure
and a lower overall price level. No transformation converts a rate-structure-shape statistic
into a price-level statistic without additional data neither paper reports (the actual price
levels at both tiers, for S526's sample, which would be needed to back out an absolute price
effect — not provided). **S526 is excluded from any pooling attempt on construct-validity
grounds alone, independent of the currency/units problem below.**

## 3. Why S539 and S749 cannot be harmonized without manufactured assumptions

Setting S526 aside, S539 (USD annual bill; also a percentage-of-income figure) and S749 (R$/m³
tariff level) both measure price *level*, which is the right starting point — but converting
between them requires at least three separate assumptions, none of which either paper's
reported estimate lets a researcher make without inventing a number:

1. **A common unit basis.** S539's estimate is an *annual bill amount*; S749's is a *per-cubic-metre
   tariff rate*. Converting S749's rate into a bill amount (or S539's bill into an implied
   rate) requires an assumed household monthly consumption volume. Neither this project's
   extraction of S749 nor of S539 captured a reported average household consumption figure for
   either sample — using a generic assumed consumption value (e.g. a WHO minimum-adequacy
   benchmark) would be inventing a number the studies themselves did not report, which
   `PROJECT_SPEC.md`'s never-fabricate rule and this project's own repeated practice (see
   `RISK_OF_BIAS.md` and `CHANGELOG.md`'s many disclosed "not assessable" calls) forbid.
2. **A currency conversion, at the right historical point.** S749's sample runs 2005–2012;
   S539's underlying utility data is not dated precisely in this project's extraction (the
   paper is Zhang, Gonzalez Rivas, Grant & Warner 2022, but the survey year of the underlying
   utility bill data was not captured). Converting R$ to USD requires choosing a specific
   exchange-rate or PPP basis for a specific year — and the Brazilian real's exchange rate
   moved substantially across 2005–2012 alone, so even *within* S749's own sample period the
   choice of reference year would materially change the converted figure.
3. **An inflation adjustment to a common reference year**, on top of the currency conversion,
   since the two studies' data come from different, non-overlapping periods.

Each of these three choices is a real researcher degree of freedom that neither source paper
made for us. Stacking three independent, uncorroborated assumptions to force two studies onto
one metric is close to the textbook case `ANALYSIS_PLAN.md`'s opening rule warns against:
manufacturing comparability rather than finding it. **This is not a judgment call under time
pressure — it is a structural data gap**: the missing consumption-volume and survey-year
figures are not implied anywhere in what this project extracted from either source, and
inventing them would put a fabricated number into a systematic review whose central discipline
is not doing that.

## 4. Could S539's already-standardized coefficients help?

S539 reports standardized regression coefficients (0.35 for the bill-amount model, 0.26 for
the income-share model) alongside its raw estimates. In principle, a standardized coefficient
is closer to a common metric across studies than a raw dollar amount is. But this route is
blocked for the same reason as everything else here: neither S526 nor S749's `effect_sizes.csv`
row reports a standard error or the outcome variable's standard deviation, so their own
coefficients cannot be standardized for comparison — there's a real number for S539's side of
the comparison and nothing to put on the other side of it.

## 5. Verdict

**No defensible common-metric transformation exists for this cluster with the data currently
in `effect_sizes.csv` and `extraction_database.csv`.** This is not a permanently closed
question — §6 below states exactly what would reopen it — but as of today it stays a
**structured synthesis (SWiM) grouping, not a pooling candidate**, consistent with Phase 11's
overall verdict. `included_in_pooled_estimate` remains `FALSE` for S526, S539, and S749, and
should not be changed without the additional data named in §6 actually being retrieved and
extracted, and a specific transformation then justified explicitly — not silently applied.

**What the cluster *can* support, and should, in the Family C SWiM synthesis**: a
vote-counting presentation. All three studies test the same exposure (private vs.
public/cooperative/mixed-capital ownership), all three are adjusted for a reasonable set of
observable confounders, and all three find a statistically significant effect in the same
substantive direction (private ownership → worse affordability/progressivity outcome for the
household). That is a real, reportable finding — "the direction of association is consistent
across three independent studies in three different national contexts" — that does not require
a pooled effect size to state honestly. `family_C_swim_synthesis_2026-09-28.md` presents it
this way.

## 6. What would change this answer

A future researcher could revisit this verdict if any of the following became available:

- The original S526, S539, or S749 source papers' full tables report a household
  average-consumption figure or a baseline (reference-category) price level not currently in
  this project's extraction — re-mining the full texts specifically for these figures (not
  currently extracted because the 92-field codebook does not have a dedicated field for them)
  would close gap (1) in §3.
- A precise survey year for S539's underlying utility bill data is located, narrowing the
  currency-conversion reference point in gap (2).
- A fourth or fifth study is added to this cluster reporting the same ownership exposure
  against a price outcome on a metric shared with one of the existing three (e.g. another
  study reporting a dimensionless UPR, which could then pool with S526 on construct-consistent
  grounds even without S539/S749).
- Someone with domain expertise in utility-tariff economics proposes and defends a specific,
  citable conversion methodology (e.g. a standard "typical monthly consumption" benchmark used
  elsewhere in the tariff-economics literature) — at that point this becomes a genuine methods
  decision worth documenting, not an invented number.

Until then, this cluster's honest contribution to this review is a consistent-direction
narrative finding, not a pooled effect size.
