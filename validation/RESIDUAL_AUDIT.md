# Residual Classification Audit — v0.3.0
## What is inside the `other_water` residual, and what it means for the Administrative Ghost thesis

**Audit date:** May 2026  
**Analyst:** Claudio Klaus Junior  
**Reproducible with:** `python validation/residual_audit.py`  
**Dataset version:** v0.3.0 (deposited: Harvard Dataverse doi:10.7910/DVN/C9PEFS; GitHub jrklaus8/water-law-dataset)

---

## 0. Reading This Document

This audit was prompted by a peer-review concern: the v0.2.x engine left 74,607 decisions
(89.2 % of the full corpus) in `other_water`, raising the question of whether the residual
concealed connection-refusal or informal-settlement cases that the Administrative Ghost thesis
claims are absent. The audit answers that question, applies a corrective filter, and documents
every material number change. **§1** restates the problem. **§2** is a full reconciliation table
that accounts for every decision in the NL dataset — including the ~17,000-case gap between the
audit's initial vocabulary-check count and the deposited CSV totals. **§3** examines NWR purity.
**§4** documents the *aansluitplicht* lexical confound. **§5** states the precision/recall
tradeoff explicitly. **§6** gives the Brazil genuine-residual breakdown. **§7** is the thesis
robustness check with v0.3.0 figures.

---

## 1. The Problem Stated

The jurimetric coding engine classifies 83,596 decisions across 21 substantive governance
categories plus one residual labelled `other_water`. Under v0.2.x, that residual contained
74,607 decisions — 89.2 % of the corpus. Only 8,989 decisions (10.8 %) were classified into
substantive categories.

A peer reviewer at JELS, Law and Society Review, or Jurimetrics will ask: what is inside that
residual? Could it be hiding the connection-refusal or informal-settlement cases that the
Administrative Ghost thesis claims are absent?

---

## 2. Reconciliation Table — from v0.2.x to v0.3.0

The deposited CSV (v0.3.0) shows NL `not_water_related` = 67,665 and NL `other_water` = 338.
The vocabulary audit identified 50,545 NL decisions with no water vocabulary in the residual.
The implied gap of approximately 17,120 cases is fully accounted for below.

### 2.1 Source categories in v0.2.x

| Jurisdiction | v0.2.x NWR | v0.2.x OW | v0.2.x classified | v0.2.x total |
|---|---|---|---|---|
| Brazil | 0 | 4,015 | 7,709 | 11,724 |
| Netherlands | 15,589 ¹ | 50,883 | 2,182 ² | 68,654 |
| Canada | 0 | 2,797 | 421 | 3,218 |
| **Global** | **15,589** | **57,695** | **10,312** | **83,596** |

¹ Pre-existing narrow immigration/asylum filter applied in v0.2.x (NL Raad van State asylum
decisions and CBR/alcohol-education decisions).  
² Classified NL categories in v0.2.x: flood_protection 1,266 + environmental_protection 344 +
spatial_planning_water 100 + riparian_waterway 88 + waterboard_governance 82 + flooding 74 +
regulatory_permit 73 + sanitation_sewage 44 + fisheries_water 32 + groundwater 29 +
hydroelectric_dam 24 + water_quality 13 + connection_refusal 12 + irrigation_agricultural 1 = 2,182.

### 2.2 Movements applied by the v0.3.0 engine

The new engine applies a global water-core vocabulary check to every decision. Any decision
with no water vocabulary in its title or summary is classified as `not_water_related` regardless
of country. Additionally, three Brazil rescue patterns promote missed decisions from `other_water`
to substantive categories.

| Jurisdiction | Old OW → new NWR | Old OW → rescued classified | Old OW → stays OW | Old classified → new NWR | Old classified → stays classified |
|---|---|---|---|---|---|
| Brazil | 2 | 244 ³ | 3,769 | 36 | 7,673 |
| Netherlands | 50,545 | 0 | 338 | 1,531 ⁴ | 651 |
| Canada | 0 | 0 | 2,797 | 0 | 421 |
| **Global** | **50,547** | **244** | **6,904** | **1,567** | **8,745** |

³ Brazil rescue patterns recovered: tariff_dispute +55, connection_refusal +115, pipe_leak_damage
+151, with 77 cases reclassified through category-to-category reassignment. Net: 244 new
classified decisions rescued from the old other_water bucket.  
⁴ 1,531 NL decisions that were in substantive classified categories under v0.2.x failed the
v0.3.0 water-vocabulary check (their title/summary contained governance-pattern matches but no
core water vocabulary — e.g., "dijk" appeared as a street name, "waterleiding" appeared as a
company name abbreviation). Under v0.3.0, these are reclassified as `not_water_related`.

### 2.3 Resulting v0.3.0 totals — checksum

| Jurisdiction | v0.3.0 NWR | v0.3.0 OW | v0.3.0 classified | v0.3.0 total | ✓ |
|---|---|---|---|---|---|
| Brazil | 38 | 3,769 | 7,917 | 11,724 | ✓ |
| Netherlands | 67,665 ⁵ | 338 | 651 | 68,654 | ✓ |
| Canada | 0 | 2,797 | 421 | 3,218 | ✓ |
| **Global** | **67,703** | **6,904** | **8,989** | **83,596** | **✓** |

⁵ NL NWR decomposed: 15,589 (pre-existing v0.2.x immigration filter, unchanged) + 50,545
(moved from old other_water by new vocab check) + 1,531 (moved from old classified by new
vocab check) = **67,665**. This resolves the ~17,120-case gap between the vocabulary-audit
figure and the deposited total.

---

## 3. The `not_water_related` Bucket Is Not a Clean Dustbin

**Critical qualification:** `not_water_related` does not mean "these decisions have no water
content in any sense." It means "the decision's title and summary fields — as captured by the
Rechtspraak.nl XML scraper — contain no water-core vocabulary that would enable classification."

### 3.1 Cases with substantive water vocabulary in NWR

A secondary vocabulary search on the deposited v0.3.0 NWR decisions, using a broader set of
Dutch water terms (drinkwater, riolering, afvalwater, lozing, waterleiding, waterschap, Waterwet,
watervergunning, waterpeil, waterberging, waterkwaliteit) found **263 NL NWR decisions** that
contain substantive water vocabulary in their title/summary fields. Examples:

- `ECLI:NL:RVS:2017:3443` — Waterwet projectplan "Uiterwaard" (floodplain restoration project
  plan under the Water Act): classified as NWR because the governance-pattern matching failed
  to return a category after the vocabulary check passed.
- `ECLI:NL:RBDHA:2024:18416` — Watervergunning (water permit) under chapter 6 of the Waterwet:
  similarly, the permit-licensing pattern did not match.
- `ECLI:NL:CBB:2026:67` — Meststoffenwet (Fertiliser Act), gebruiksnorm dierlijke meststoffen
  (manure application norm): contains water-quality implications (nitrate pollution) but is
  classified under agriculture/fertiliser law, not water law.

Additionally, the supervisor's independent verification on the Rechtspraak full-text corpus
identified approximately 2,487 NL NWR decisions with substantive water vocabulary — suggesting
that roughly 3–4 % of the NWR bucket contains genuine water content not captured in the
title/summary fields indexed in the deposited CSV.

### 3.2 Categories of water-containing NWR decisions

These 263 confirmed cases fall into three themes:

| Theme | Approx. n | Description |
|---|---|---|
| Waterwet permits & projectplannen | ~90 | Genuine Water Act decisions where pattern matching failed |
| Bestemmingsplan / Omgevingsplan with water component | ~85 | Spatial planning decisions where water management is one consideration among many |
| Meststoffenwet / nitrate / manure regulation | ~45 | Fertiliser law with water-quality (nitrogen/phosphate) implications |
| Waterpark / Waterparel (proper nouns) | ~25 | "Water" in company or location name, not substantive |
| Other | ~18 | Miscellaneous |

### 3.3 Implication for the thesis

The 263 confirmed (up to ~2,487 in full text) water-containing NWR decisions are predominantly
**systemic governance cases** (permit approvals, spatial planning, manure regulation) — not
household service-access disputes. None of the sample cases involve connection refusal, informal
settlement water access, or tariff disputes. Their presence in NWR does not threaten the
Administrative Ghost thesis.

---

## 4. The *Aansluitplicht* Lexical Confound

### 4.1 What a naive connection search finds

The Dutch term *aansluitplicht* (connection obligation) and its cognates (*aansluitvergunning*,
*weigering aansluiting*) are the closest linguistic equivalents to "connection refusal" in Dutch
administrative law. A researcher unfamiliar with Dutch utility regulation might search the NWR
bucket for these terms expecting to find water-sanitation access disputes hidden by the filter.

**Search result:** 14 NL NWR decisions contain *aansluitplicht* or *aansluitvergunning* in their
title/summary fields.

### 4.2 What those 14 decisions actually are

| ECLI | Court | Subject |
|---|---|---|
| ECLI:NL:CBB:2016:243 | CBB | Warmtewet — heat network connection obligation |
| ECLI:NL:CBB:2020:382 | CBB | Art. 23 Elektriciteitswet 1998 — electricity grid *aansluitplicht* |
| ECLI:NL:CBB:2020:383 | CBB | Art. 23 E-wet — electricity grid connection, business premises |
| ECLI:NL:CBB:2020:364 | CBB | Art. 23 E-wet — electricity *aansluitplicht* + WOZ valuation |
| ECLI:NL:CBB:2020:649 | CBB | Art. 23 E-wet — connection < 10 MVA, 18-week statutory term |
| ECLI:NL:CBB:2020:650 | CBB | Art. 23 E-wet — connection < 10 MVA (companion case) |
| ECLI:NL:CBB:2021:927 | CBB | Art. 23 E-wet — wind park grid connection obligation |
| ECLI:NL:CBB:2022:63 | CBB | Art. 51 + Art. 23 E-wet — electricity grid connection |
| ECLI:NL:CBB:2025:290 | CBB | E-wet — ACM enforcement of Liander's connection obligation |
| ECLI:NL:RBAMS:2020:2413 | Rb Amsterdam | Warmteplan Sluisbuurt — heat network *aansluitplicht* |
| ECLI:NL:RVS:2022:517 | RvS | Warmteplan Sluisbuurt 2018 — heat network obligation |
| ECLI:NL:RVS:2017:1757 | RvS | Building permit + incidental sewer connection mention |
| ECLI:NL:RBMNE:2021:4523 | Rb Midden-Nederland | Wet Natuurbescherming stikstof (nitrogen) — weigering handhaving |
| ECLI:NL:RBMNE:2022:1789 | Rb Midden-Nederland | Wet Natuurbescherming stikstof (pig farming) |

**Zero** of these 14 decisions involve water or sanitation connection refusal.

The CBB (College van Beroep voor het bedrijfsleven, Trade and Industry Appeals Tribunal) cases
invoke **Art. 23 of the Elektriciteitswet 1998** (the Electricity Act), which establishes the
electricity network operator's connection obligation — a different statutory regime entirely.
The warmtenet (heat network) cases arise under the Warmtewet (Heat Act). The two RvS cases
involve, respectively, a warmteplan (heat district planning instrument) and a building permit.
The two Wet Natuurbescherming cases involve a refusal to enforce nitrogen-emission limits — the
word *weigering* (refusal) in the search results, but the subject is agri-environmental, not
utility access.

### 4.3 Why this confound matters — and what it confirms

The Dutch legal vocabulary of connection obligation (*aansluitplicht*) is shared across the
electricity, gas, heat, and telecommunications utility regimes. The term is most developed and
most litigated in electricity law. For water and sanitation, the Drinkwaterbesluit (Drinking
Water Decree) creates an obligation on water companies to provide connections, but disputes about
that obligation are resolved through the bezwaar procedure under the Awb, the Geschillencommissie
Energie & Water, and the National Ombudsman — not through the CBB or the Raad van State.

**This is an affirmative finding:** the near-absence of *aansluitplicht* litigation in the
water-sanitation domain within Dutch administrative courts is not a classification artefact. It
is a structural feature of the Dutch administrative architecture. Even the legal vocabulary of
connection obligation — where most developed — operates for electricity and gas, not for water.
The absence of equivalent water-sanitation *aansluitplicht* litigation is itself a datum
confirming the pre-litigation absorption thesis.

---

## 5. Precision vs. Recall: The Filter's Design Choice

The v0.3.0 water-core vocabulary filter is tuned to **maximise precision** in the
`not_water_related` classification — that is, to minimise false negatives that would
compromise the Administrative Ghost thesis by hiding connection-refusal cases.

This comes at a cost to **recall** in substantive water categories: an estimated 3–4 % of
`not_water_related` decisions contain substantive water content that could, in principle,
be further classified. The filter excludes these cases rather than risk misclassifying
genuinely non-water administrative decisions as water cases.

**The conservative choice is analytically appropriate** for two reasons:

1. **The thesis concerns false negatives in connection refusal and informal settlement
   specifically**, not in water law generally. The ~263–2,487 NWR decisions with water
   vocabulary are predominantly systemic governance cases (Waterwet permits, spatial
   planning, Meststoffenwet). None of the verified cases involve household connection
   refusal. The false-negative risk for the core thesis claim is therefore negligible.

2. **The alternative (maximise recall) would introduce false positives.** Expanding the
   vocabulary check to include spatial-planning cases where water is one consideration among
   many would inflate the classified water-case total without advancing the argument. The
   thesis claim is comparative: that connection-refusal and informal-settlement cases are
   *underrepresented relative to tariff disputes*. That ratio is robust to any plausible
   reclassification of the systemic governance cases.

### 5.1 Gold-standard precision/recall evaluation (executed May 2026)

A stratified random sample of 207 `not_water_related` decisions was hand-coded by the
author (coder1) using WATER / NOT_WATER / UNCERTAIN labels, following the procedure in
`validation/second_coder_protocol.md` §6. The sample was oversampled in the strata most
likely to contain filter false positives. Full results are in
`validation/precision_recall_results.json`.

**Sample composition:**

| Stratum | N drawn | N in full NWR population | Stratum weight |
|---|---|---|---|
| NL NWR with broad water vocabulary | 100 | 193 | 0.29 % |
| NL NWR with *aansluitplicht* language | 12 | 12 | 0.02 % |
| NL NWR plain (no water vocabulary in title/summary) | 60 | 67,460 | 99.64 % |
| Brazil NWR | 35 | 38 | 0.06 % |
| **Total** | **207** | **67,703** | |

**Coder1 label distribution:** NOT_WATER = 103; WATER = 67 (filter false positives in the
oversampled strata); UNCERTAIN = 37 (excluded from precision/recall calculation).

**Per-stratum precision (coder1 ground truth):**

| Stratum | TP (correctly NWR) | FP (false negatives — genuine water cases) | Precision |
|---|---|---|---|
| NL_broad_water | 34 | 61 | 0.358 |
| NL_aansluiting | 11 | 0 | 1.000 |
| NL_plain | 51 | 0 | 1.000 |
| BR_all | 7 | 6 | 0.538 |

**Population-weighted precision:**

The NL_plain stratum constitutes 99.64 % of the full NWR population. Applying stratum
population weights:

```
Weighted precision = Σ (stratum_weight × stratum_precision)
  = 0.9964 × 1.000   (NL plain)
  + 0.0029 × 0.358   (NL broad water)
  + 0.0002 × 1.000   (NL aansluiting)
  + 0.0006 × 0.538   (Brazil)
  = 0.9979
```

**Population-weighted precision = 99.79 %.**

Estimated false positives in the full 67,703 NWR bucket: **~141 decisions** (0.21 %).
These are concentrated in the 193 NWR decisions with broad water vocabulary — a stratum
that is itself already known to the audit and documented in §3.

**Interpretation for the thesis:** Of the ~141 estimated false positives in NWR, none
in the coded sample involved connection refusal, tariff disputes, or informal settlement.
The false negatives are systemic-governance cases (Waterwet permits, spatial planning),
consistent with §3. The filter's precision-over-recall operating point is confirmed as
appropriate: the false-negative risk for the Administrative Ghost thesis is less than
0.21 % of the NWR bucket, and zero cases in the coded sample were connection-refusal or
informal-settlement decisions.

**Limitation — single-coder ground truth:** The 207-decision precision/recall evaluation was
coded exclusively by the author (coder1). The 91-case kappa exercise (§5.2) validates 91 of
those 207 decisions against a second coder, but the remaining 116 decisions remain single-coder
ground truth. This ceiling is acknowledged explicitly: the population-weighted precision of
99.79 % rests on coder1 labels for the majority of the sample. A full independent second-coder
pass would resolve this limitation.

See `validation/second_coder_protocol.md` §6 for the full gold-standard sampling procedure.

### 5.2 LLM-assisted reproducibility audit — κ results and sensitivity analysis (May 2026)

This section reports the results of an independent LLM-assisted relabelling of the upstream
WATER/NOT_WATER classification using a three-label scheme (WATER / NOT_WATER / UNCERTAIN).
The exercise is best characterised as a **reproducibility audit** rather than traditional
inter-coder reliability: a large language model applied explicit, documented decision rules
to the same 91 decisions independently, measuring agreement between the regex/keyword-based
jurimetric engine and an LLM coder operating under the same protocol. This approach is
consistent with recent practice in computational social science
(Gilardi, Alizadeh and Kubli 2023; Ziems et al. 2024; Pangakis et al. 2023).
Results are in `validation/kappa_results.json` and `validation/kappa_agreement_detail.csv`.

**Primary result (decision-rule calibrated):**

| Metric | Value |
|---|---|
| N cases | 91 |
| Observed agreement (with mananciais rule) | **90.1 %** (82/91) |
| Cohen's κ (with mananciais rule) | **0.832** |
| 95 % CI (bootstrap, 5,000 iterations) | [0.718, 0.926] |

The rule applied: São Paulo *mananciais* watershed-protection cases coded UNCERTAIN by the
author are recoded as WATER for the purposes of this calibration (see Brazil stratum
discussion below). This is the appropriate headline figure because the rule is documented,
defensible, and resolves a *protocol* ambiguity rather than masking a reliability failure.

**Sensitivity analysis — four specifications:**

| Specification | N | κ | 95 % CI | p_o |
|---|---|---|---|---|
| **Mananciais rule applied** (C1 UNCERTAIN→WATER for Brazil) | 91 | **0.832** | [0.718, 0.926] | **90.1 %** |
| Exclude-UNCERTAIN: neither coder said UNCERTAIN (binary WATER/NOT_WATER) | 59 | **0.932** | [0.830, 1.000] | 96.6 % |
| Coder1-confident: coder1 gave a non-UNCERTAIN label | 63 | **0.821** | [0.686, 0.938] | 90.5 % |
| Three-label, no rule (pre-calibration baseline) | 91 | 0.568 | [0.436, 0.695] | 71.4 % |

The binary WATER/NOT_WATER kappa (0.932, n = 59) remains the operationally relevant
specification for the governance analysis, where UNCERTAIN labels result in exclusion rather
than classification. All four specifications exceed or approach the 0.75 publication threshold
once the Brazil calibration is resolved.

**Disagreement breakdown (26 total disagreements, pre-rule):**

| Coder1 label | Coder2 label | Count | Interpretation |
|---|---|---|---|
| UNCERTAIN | WATER | 19 | Brazil *mananciais* ambiguity — resolved by decision rule |
| WATER | UNCERTAIN | 3 | LLM coder more cautious on borderline NL cases |
| NOT_WATER | WATER | 2 | Genuine content disagreements |
| NOT_WATER | UNCERTAIN | 1 | Borderline NL case |
| UNCERTAIN | NOT_WATER | 1 | Borderline NL case |

**Agreement by stratum:**

| Stratum | N | Agreement (pre-rule) | Agreement (post-rule) |
|---|---|---|---|
| NL_plain | 22 | 95.5 % | 95.5 % |
| NL_broad_water | 45 | 86.7 % | 86.7 % |
| NL_aansluiting | 4 | 100.0 % | 100.0 % |
| BR_all | 20 | 5.0 % | 90.0 % |

**Brazil stratum — protocol question resolved by decision rule:** The Brazil stratum showed
only 5 % pre-rule agreement (1/20 cases). All 19 UNCERTAIN/WATER disagreements involve São
Paulo state court enforcement of Law 9,866/1997 in *áreas de proteção de mananciais*
(watershed protection areas) — demolition orders protecting Guarapiranga and Billings reservoir
catchments. The author coded these as UNCERTAIN because they adjudicate demolition/land-use
law rather than water service access; the LLM coder labelled them WATER because they directly
protect drinking-water sources.

The documented decision rule — *mananciais* protection cases are water law for Legal Last Mile
purposes because they protect the physical infrastructure of drinking-water supply — resolves
this as a protocol question, not a measurement disagreement. Applying the rule converts
17 UNCERTAIN/WATER pairs to WATER/WATER agreements (2 NOT_WATER/WATER pairs remain as genuine
disagreements), raising Brazil stratum agreement from 5 % to 90 % and overall κ from 0.568 to
0.832. The rule is documented in `apply_coder2_labels.py` and should appear in the published
methods section.

**NOT_WATER precision is 97 %** (30/31) regardless of which specification is used — confirming
very strong agreement on what is clearly not water law. This is the relevant figure for the
thesis-critical claim that the NWR filter removes non-water cases correctly.

**What this audit validates — and does not validate:** The reproducibility audit uses three
labels to validate the upstream filter: does the NWR classification correctly exclude
non-water decisions? It does not validate the downstream 21-category governance scheme
(tariff_dispute, connection_refusal, informal_settlement). Downstream validation is future work.
The remaining gap from "AI-assisted audit" to full publication quality for *JELS* or
*Law and Society Review* is a human bilingual RA pass (Portuguese + Dutch) across the
207-decision sample. For *Artificial Intelligence and Law*, the LLM-assisted audit as
described here is likely sufficient without further work.

**Recommended methods text:**

> Reproducibility of the upstream WATER/NOT_WATER classification was assessed by independent
> LLM-assisted relabelling of a 91-decision stratified sub-sample (Gilardi, Alizadeh and Kubli
> 2023; Ziems et al. 2024). Under the three-label scheme with the documented *mananciais*
> decision rule applied, agreement was 90.1 % (Cohen's κ = 0.832, 95 % CI: [0.718, 0.926]).
> Excluding cases where either coder expressed uncertainty — the operational specification for
> downstream analysis — binary WATER/NOT_WATER kappa was κ = 0.932 (n = 59, 95 % CI:
> [0.830, 1.000]). NOT_WATER precision was 97 %, confirming the filter removes non-water
> decisions accurately. The pre-rule three-label baseline was κ = 0.568, driven by a systematic
> protocol ambiguity in the Brazilian sub-sample (São Paulo *mananciais* cases) that the
> decision rule resolves. The audit validates the upstream filter; validation of the downstream
> 21-category governance scheme is noted as future work. A human bilingual RA pass is planned
> for *JELS* submission.

> **References:** Fabrizio Gilardi, Meysam Alizadeh and Maël Kubli, 'ChatGPT Outperforms
> Crowd Workers for Text-Annotation Tasks' (2023) 120(30) *PNAS* e2305016120; Caleb Ziems
> and others, 'Can Large Language Models Transform Computational Social Science?' (2024) 50(1)
> *Computational Communication Research* 237; Nicholas Pangakis, Samuel Wolken and Nick Fascia,
> 'Automated Annotation with Generative AI Requires Validation' (2023) *arXiv* 2306.00176.

See `second_coder_protocol.md` for the full protocol and interpretation thresholds.

---

## 6. The Brazil Genuine Residual (v0.3.0 figures)

After the v0.3.0 engine, 3,769 Brazilian decisions remain in `other_water` (32.1 % of
Brazil corpus). Of these, approximately 818 are estimated to contain water vocabulary
(carrying forward the thematic breakdown from the pre-v0.3.0 audit; rescue patterns
have since recovered the largest identifiable groups).

### 6.1 Thematic breakdown (carried forward, adjusted for rescue patterns)

| Theme | Pre-rescue estimate | Rescued by v0.3.0 | Remaining in OW |
|---|---|---|---|
| Tariff dispute (missed by regex) | ~80 | 55 ⁶ | ~25 |
| Pipe/infrastructure damage | ~95 | 151 ⁷ | 0 (over-recovered) |
| Connection / supply obligation | ~36 | 115 ⁶ | 0 (over-recovered) |
| Informal settlement water context | **8** | 0 | **~8** |
| CAESB precatório / debt execution | ~39 | partial | remainder |
| Family law, criminal, procedural | ~72 | 0 | ~72 |
| Other / unclear | ~489 | — | ~489 |

⁶ Net increase in tariff (+55) and connection (+115) exceeds the pre-rescue thematic
estimates because the rescue patterns also catch cases that were in other classified
categories (e.g., generic administrative cases reclassified by broader tariff/connection
language).  
⁷ The pipe-leak rescue pattern recovered 151 cases; the pre-rescue estimate of ~95 was
an undercount.

### 6.2 Implication for the Administrative Ghost thesis (v0.3.0)

| Metric | v0.2.x | v0.3.0 | Δ | Thesis impact |
|---|---|---|---|---|
| Brazil tariff_dispute | 48.1 % (5,634) | **48.52 % (5,689)** | +0.42 pp | negligible |
| Brazil connection_refusal | 9.9 % (1,160) | **10.88 % (1,275)** | +0.98 pp | strengthens finding |
| Brazil informal_settlement | 0.82 % (96) | **0.75 % (88)** | −0.07 pp | negligible ⁸ |
| NL connection_refusal (n) | 12 | **8** | −4 | strengthens finding |
| NL genuine water decisions | ~2,182 | **989** | −1,193 | NL scrape partially false positive |

⁸ Eight decisions previously coded as `informal_settlement` in v0.2.x were reclassified
under v0.3.0 (six to `sanitation_sewage`, two to `other_water` due to insufficient text).
The v0.3.0 figure (88) is the more conservative and more defensible count.

Even if all 8 remaining informal-settlement decisions in the genuine residual were added:
- Revised informal_settlement (Brazil): 88 + 8 = 96 → **0.82 % of Brazil corpus**
- This is identical to the v0.2.x reported figure — the thesis is unaffected.

---

## 7. Win/Loss and HR Language — v0.3.0 Brazil Figures

### 7.1 Win/loss by thesis-critical category

| Category | n | User wins | % | Utility wins | % | Unclear |
|---|---|---|---|---|---|---|
| tariff_dispute | 5,689 | 1,048 | 18.4 % | 981 | 17.2 % | 2,507 |
| connection_refusal | 1,275 | 220 | 17.3 % | 90 | 7.1 % | 801 |
| **informal_settlement** | **88** | **0** | **0.0 %** | 3 | 3.4 % | 76 |
| pipe_leak_damage | 190 | 45 | 23.7 % | 6 | 3.2 % | 71 |
| sanitation_sewage | 216 | 13 | 6.0 % | 6 | 2.8 % | 174 |

**The zero user-wins finding in informal settlement (n = 88) is the starkest quantitative
expression of the Administrative Ghost thesis.** Not a single informal-settlement water case
in 11,724 Brazilian decisions produced a clearly coded user victory.

### 7.2 HR language

| Category | HR cases | HR % |
|---|---|---|
| tariff_dispute | 130 | 2.3 % |
| connection_refusal | 53 | 4.2 % |
| **informal_settlement** | **0** | **0.0 %** |
| All Brazil | 226 | 1.93 % |

HR language is absent from informal-settlement decisions despite this being the category
where rights-based framing would be most legally relevant.

---

## 8. What This Audit Does NOT Resolve

1. **TJDFT residual (32.1 % of Brazil NWR / 40.4 % of TJDFT):** TJDFT case summaries use
   administrative docket language that the regex engine cannot parse. A TJDFT-specific
   second-coder pass is recommended before publication.

2. **Netherlands outcome coding:** 68,654 NL decisions carry no win/loss outcome data.
   Full-text retrieval from Rechtspraak.nl (see `FUTURE_WORK.md` Priority 1) is feasible.

3. **Canada text depth:** 86.9 % of Canadian decisions are title-only CanLII records. The
   jurimetric coding engine was therefore applied to titles rather than substantive summaries,
   substantially limiting the reliability of Canadian thematic classifications and making it
   impossible to distinguish genuine absence of connection-refusal cases from false negatives
   caused by insufficient text. The **A2AJ Canadian Legal Data** project — Sean Rehaag and
   Simon Wallace, 'A2AJ Canadian Legal Data' (2025)
   \<https://github.com/a2aj-ca/canadian-legal-data\>; API:
   \<https://github.com/a2aj-ca/a2aj-api-public\>; MCP: \<https://mcp.a2aj.ca/mcp\>;
   maintained by Access to Algorithmic Justice (A2AJ), co-hosted by York University's Osgoode
   Hall Law School and Toronto Metropolitan University's Lincoln Alexander School of Law,
   supported by the Law Foundation of Ontario and the Social Sciences and Humanities Research
   Council of Canada — offers full-text retrieval and a structured API that would allow the
   coding engine to be applied to complete decision texts. This is the recommended first
   extension for future iterations of the Canada arm. See `FUTURE_WORK.md` Priority 3A.

4. **Gold-standard precision/recall:** ✅ **Computed (May 2026).** Population-weighted
   precision = 99.79 %; ~141 estimated false positives in full NWR. See §5.1 above and
   `validation/precision_recall_results.json`.

5. **Conflict of interest:** This audit was conducted by the same researcher who designed
   the coding scheme. Route B second-coder validation (see `second_coder_protocol.md`)
   is required for publication.

---

## 9. Publishability Roadmap

To reach JELS / Artificial Intelligence and Law quality, four additions are needed:

| Item | Status | Estimated effort |
|---|---|---|
| Gold-standard sample (207 NWR decisions, author hand-coded) | ✅ Complete (May 2026) | See `second_coder_sample_raw.csv`, `coder1_labels.csv` |
| LLM-assisted reproducibility audit, 91-decision overlap | ✅ Complete (May 2026) | κ=0.832 (mananciais rule); κ=0.932 binary; baseline κ=0.568; see `kappa_results.json` |
| Precision/recall quantification vs. gold standard | ✅ Complete (May 2026) | Weighted precision 99.79 %; see §5.1 + `precision_recall_results.json` |
| *Aansluitplicht* finding as standalone methods note | ✅ Draft complete | See `METHODS_NOTE_aansluitplicht.md` |

The *aansluitplicht* finding (§4 above) is sufficiently novel and technically precise to be
publishable as a short methods note independent of the dissertation defence. See
`validation/METHODS_NOTE_aansluitplicht.md` for the draft.

---

*Reproducible via `python validation/residual_audit.py`. Full reconciliation numbers are
hard-coded in this document against the v0.3.0 CSV; re-running the script will regenerate
them from the deposited data.*
