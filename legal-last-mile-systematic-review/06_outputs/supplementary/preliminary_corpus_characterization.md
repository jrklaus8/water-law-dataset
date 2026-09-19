# Preliminary Descriptive Analysis of Phase 6 Full-Text Includes

**Status: descriptive corpus characterization, not a results section.** This
document reports what the 509 studies currently extracted under Phase 8
(`03_extraction/extracted_data/extraction_database.csv`) and classified under
Phase 10 (`05_analysis/descriptive/evidence_map.csv`) look like — geography,
study design, mechanism coding, outcome coding, and the small set of studies
with a locatable quantitative effect estimate. Per `PROJECT_SPEC.md` §14 and
`ANALYSIS_PLAN.md`, this is **not** a systematic-review results section, a
meta-analysis, or a synthesis judgment: Phase 9 (risk of bias) is rated for
only 12 of 509 studies, and Phase 11 (quantitative-synthesis feasibility) has
not cleared any candidate family (`PROJECT_SPEC.md` §8) through
`ANALYSIS_PLAN.md` §2's decision tree. Every number below is reproducible
directly from the two CSVs cited above (and `05_analysis/effect_sizes/
effect_sizes.csv` in §6), as of 2026-09-18 (509 full-text includes; 1,016 of
3,659 Phase-5 includes assessed at Phase 6; 2,643 still open).

## 1. Corpus overview

- **509 studies** fully extracted (92-field `CODEBOOK.md` schema), covering
  full-text-screening includes **S001–S511** (two permanent gaps: `S227` and
  `S399`, both resolved post-hoc duplicate-merge cases documented in
  `CHANGELOG.md`).
- This is **28% of the 3,659-record Phase-5 include pool** (1,016 decided at
  full-text stage: 509 include / 507 exclude); 2,643 records remain open,
  awaiting the researcher's rolling PDF supply — retrieval status, not a
  confirmed unretrievable population.
- **Peer-reviewed: 491 / not peer-reviewed: 18** (PhD/master's theses, working
  papers, book chapters, a practitioner report).
- **Publication type** is dominated by journal articles (~450 once minor
  formatting variants — `journal article`, `journal_article`, `journal
  article (systematic review)`, etc. — are combined), plus 6 explicit
  systematic reviews, 5 PhD dissertations, 5 conference papers, 3 narrative
  reviews, and a long tail of single-instance types (book chapters, master's
  theses, working papers, a scoping review, a realist review).
- **Publication decade:** 2000s = 12, 2010s = 135, **2020s = 362 (71%)** — this
  is a heavily contemporary literature; pre-2010 empirical work on this topic
  is sparse in the corpus as currently searched and screened.

## 2. Geographic and legal-system distribution

**122 distinct country/country-label values** are represented (a handful of
rows are explicitly multi-country comparative or cross-national studies, and
7 rows are blank — typically secondary reviews or cross-jurisdictional
syntheses with no single-country focus).

Top 15 by study count:

| Country | Studies | Country | Studies |
|---|---|---|---|
| Brazil | 63 | Bangladesh | 11 |
| India | 40 | Argentina | 9 |
| South Africa | 37 | Ethiopia | 9 |
| United States | 31 | Peru | 9 |
| Kenya | 29 | Nepal | 8 |
| Ghana | 18 | Colombia | 8 |
| Mexico | 17 | Malawi | 8 |
| Uganda | 15 | | |

This mirrors the dissertation's comparative frame only loosely — Brazil is
heavily represented (partly reflecting the doctrinal/jurimetric strand's own
searches), but the Netherlands and Canada (Ontario) are thin in this
empirical-evidence pipeline (Canada: 7 studies; the Netherlands does not
appear in the top 15 at all), a genuine and disclosable asymmetry for the
dissertation's three-jurisdiction comparison to address separately through
the doctrinal/judicial-dataset strands (`PROJECT_SPEC.md` §9–10).

**Legal system** free-text coding shows substantial heterogeneity (over 70
distinct string values, reflecting genuine case-by-case complexity — hybrid
statutory/customary systems, post-colonial overlays, multi-country reviews
spanning both families). Collapsing obvious formatting duplicates: roughly
**common law ≈ 194**, **civil law ≈ 177**, explicit **"mixed"/hybrid ≈ 138**
(including many single-instance descriptions of customary, indigenous, or
religious-law overlays), and 28 blank. This long tail of one-off
descriptions is itself a data-quality note: `legal_system` was extracted as
a descriptive field rather than a constrained enum, which is appropriate for
capturing real institutional pluralism but means it cannot currently support
a clean subgroup count without a separate normalization pass.

**Urban/rural setting:** urban = 114, rural = 102, mixed = 98, blank = 16,
plus a further ~35 rows using more specific informal-settlement phrasing
(`urban_informal`, `peri-urban`, `urban (informal settlements)`, etc.) that a
stricter normalization would likely fold into the urban/mixed categories.

## 3. Study design mix (`study_design_class`, Phase 10)

| Design class | n | % |
|---|---|---|
| Qualitative | 167 | 33% |
| Mixed methods | 116 | 23% |
| Observational | 85 | 17% |
| Doctrinal (Legal Institutional Evidence Appraisal Framework) | 41 | 8% |
| Jurimetric (same framework, empirical legal/institutional analysis) | 39 | 8% |
| Systematic review (secondary) | 31 | 6% |
| Quasi-experimental | 26 | 5% |
| Experimental | 4 | 1% |

**Only 30 of 509 studies (6%) use an experimental or quasi-experimental
design** capable of directly supporting a causal claim about a legal or
administrative mechanism's effect on access. The evidentiary base for this
review is overwhelmingly qualitative, observational, and mixed-methods —
consistent with `PROJECT_SPEC.md` §15 treating a qualitative mechanism
synthesis (Option D) as a fully legitimate outcome, not a fallback from a
"real" meta-analysis. The 31 secondary systematic reviews are never pooled
as independent primary evidence (`CHANGELOG.md`, `PRISMA_WORKFLOW.md` Phase 8).

## 4. Risk-of-bias status (Phase 9 — the review's largest quality-assessment gap)

`risk_of_bias_tool` is design-matched and populated for all 509 studies, but
`risk_of_bias_rating` has been **actually rated for only 12 studies** (a
2026-09-16 partial pilot batch: 3 RoB 2, 9 ROBINS-I) plus **2 further
secondary reviews with a positively-determined AMSTAR 2 rating of
"Critically Low"** (S370, S372). **497 of 509 studies (98%) have no
risk-of-bias rating yet.** This is a disclosed, deliberate limitation, not an
oversight (`RISK_OF_BIAS.md` prohibits reconstructing a validated instrument
from memory) — the much larger CASP (~167) and MMAT (~116) groups remain
entirely unappraised. No statement below should be read as risk-of-bias-
adjusted.

## 5. Mechanism coding (`PROJECT_SPEC.md` §6, extraction-level booleans, n=509, not mutually exclusive)

| Core mechanism | Studies coded TRUE | % |
|---|---|---|
| Discretion / accommodation | 313 | 61% |
| Enforcement | 202 | 40% |
| Burden | 191 | 38% |
| Eligibility | 178 | 35% |

Most studies implicate more than one mechanism at once: the evidence map's
derived `mechanism_family` field is `MULTIPLE` for **338 of 509 (66%)**
studies. Where a single mechanism dominates: `DISCRETION_ACCOMMODATION` only
— 104; `ENFORCEMENT` only — 27; `ELIGIBILITY` only — 20; `BURDEN` only — 17;
3 blank (pending judgment).

Most prevalent detailed sub-codes (of 22 tracked; top 7 shown):

| Sub-code | n | Sub-code | n |
|---|---|---|---|
| Institutional fragmentation | 263 | Service area (bounded) | 162 |
| Political coordination | 167 | Participation | 161 |
| Fees | 167 | Planning | 125 |
| | | Discretion (administrative) | 124 |

**Institutional fragmentation (52% of the corpus) and discretionary
administrative accommodation (61%) are the two most pervasive themes** in
this literature. Read descriptively, not causally: this reflects what the
included empirical literature chose to study and what this review's search
strategy and screening criteria surfaced, not a demonstrated real-world
ranking of mechanism importance (`PROJECT_SPEC.md` §11's anti-confirmation-
bias mandate applies here — see §6 below for genuine null/contrary findings
already present in the corpus).

## 6. Outcome coding (`PROJECT_SPEC.md` §7 hierarchy, Phase 10)

| Outcome family | n | % |
|---|---|---|
| Effective access (quantity/reliability/continuity/quality/distance) | 241 | 47% |
| Primary connection (the review's primary outcome) | 129 | 25% |
| Administrative outcome (submission/approval/refusal/delay/appeal/enforcement) | 85 | 17% |
| Economic access (cost/affordability/tariff burden) | 54 | 11% |

Synthesis-eligibility flags (a per-study judgment, not a pooling decision):
**quantitative_synthesis_eligible = TRUE for 197/509 (39%)**;
**qualitative_synthesis_eligible = TRUE for 422/509 (83%)** (mixed-methods
studies contribute to both).

## 7. The 25-study `effect_sizes.csv` pool — descriptive only, not pooled

25 of the 509 studies have a genuine, non-fabricated exposure-vs-comparator
contrast with a locatable effect estimate, meeting the review's strict bar
for this file (excluding descriptive percentages, growth-trend models, and
qualitative case studies even when they contain real quantitative data).
**`included_in_pooled_estimate = FALSE` for all 25** — no candidate family
has cleared `ANALYSIS_PLAN.md` §2's decision tree, and no family yet has more
than one study sharing a genuinely comparable exposure-comparator definition.

By preliminary candidate family (`PROJECT_SPEC.md` §8):

| Family | n | Description |
|---|---|---|
| A — legal recognition/eligibility status → access | 8 | |
| B — bureaucratic assistance → access | 2 | |
| C — institutional capacity/barriers → access inequality | 1 | |
| (unmatched) | 14 | Real estimates that do not fit any predefined family |

By outcome family: effective_access 14, economic_access 7, primary_connection 4.

**Illustrative estimates spanning the mechanism framework** (reported here as
what each individual study found — not combined, weighted, or otherwise
synthesized):

- **Eligibility / legal recognition:** S358 — Tribal regulatory oversight
  associated with lower odds of groundwater-decline risk (OR = 0.62,
  p < 0.001); S404 — WRUA legal-membership status reduced a water-poverty
  index by 14–32% across three independent estimators (ATT); S142 —
  unincorporated municipal status and poverty rate both associated with
  reduced centralized water/wastewater infrastructure access.
- **Bureaucratic assistance (Family B):** S085 — bureaucratic assistance
  combined with political coordination raised full land/service
  formalization by 19 percentage points; **neither factor alone had a
  significant average effect** — a genuine conditional/null finding, not a
  simple main effect.
- **Discretion / administrative barriers:** S483 — Nairobi utility income
  tiers showed rate ratios up to 5.78 for receiving sufficient water
  (p < 0.001); S489 — households who perceive their water supply as costly
  had roughly half the odds of contracting professional maintenance
  (OR = 0.53, p = 0.015); S491 — households without an existing formal
  payment relationship had roughly double the odds of being unwilling to pay
  during a COVID-19 disconnection moratorium (OR = 2.13, p < 0.001).
- **Enforcement:** S470 — a 2021 Brazilian regulatory-enforcement
  intervention (Arsae-MG) associated with a ~19-percentage-point increase in
  social-tariff enrollment; S398 — Recife's ZEIS zoning-law designation
  associated with a ~23-percentage-point increase in sewage-network access
  14–17 years later (difference-in-differences).

**Genuine null or contrary findings already present** (`PROJECT_SPEC.md` §11
anti-confirmation-bias check): S037 found no statistically significant
difference in poor drinking-water exposure between disadvantaged and
comparison communities (p = 0.14–0.79 across measures); S294's cluster-RCT
found no effect on child diarrhea or growth despite a measurable improvement
in a community WASH-institutions index; S085's bureaucratic-assistance-alone
and political-coordination-alone arms both showed no significant average
effect; S471's mayor-vs-manager governance tariff effect attenuates from
significant (p < 0.05) to non-significant once fiscal/community/environmental
covariates are added.

## 8. What this is, and is not

**Is:** a reproducible descriptive characterization of the 509 studies
extracted so far — every count above traces to `extraction_database.csv`,
`evidence_map.csv`, or `effect_sizes.csv` as of 2026-09-18.

**Is not:** a systematic-review results section, a meta-analysis, or a claim
that any legal/administrative mechanism has been shown to affect access.
Phase 9 (risk of bias) is rated for only 2% of studies; Phase 11
(quantitative-synthesis feasibility) has not cleared any candidate family;
per `PROJECT_SPEC.md` §14, no pooled estimate or causal conclusion may be
asserted at this stage. The corpus itself is also incomplete: full-text
screening has reached only 28% of the 3,659-record Phase-5 pool, and two
protocol databases (SSRN, Westlaw/Lexis) were never searched at all
(`06_outputs/supplementary/preliminary_results.md`, "What has not been
done"). This document should be revisited once Phase 9 ratings are more
complete and/or Phase 11 has made an actual per-family pooling determination.
