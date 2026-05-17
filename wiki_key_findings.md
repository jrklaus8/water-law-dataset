# Key Findings

Summary of jurimetric analysis across **83,596 decisions (2016–2026)** — Brazil (11,724), Netherlands (68,654), Canada (3,218).  
Coding engine: `jurimetric_coding.py` v2.0 — 21 governance categories, 4 languages (PT/EN/NL/FR).  
Dataset DOI: [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413) · **Version: v0.3.0 (May 2026)**

---

## Brazil — Administrative Gatekeeping in Action

Brazil's **11,724 cases** reveal a striking governance distribution:

**Governance category breakdown (v0.3.0):**

| Category | Count | % |
|---|---|---|
| Tariff disputes | 5,689 | 48.52% |
| Other water (genuine residual) | 3,769 | 32.15% |
| Connection refusal | 1,275 | 10.88% |
| Sanitation / sewage | 216 | 1.84% |
| Water infrastructure contract | 202 | 1.72% |
| Pipe leak / damage | 190 | 1.62% |
| Environmental protection | 86 | 0.73% |
| **Informal settlement** | **88** | **0.75%** |
| Flooding / drainage | 65 | 0.55% |
| Water quality | 47 | 0.40% |
| Regulatory permit | 26 | 0.22% |
| Riparian / waterway | 24 | 0.20% |
| Hydroelectric / dam | 19 | 0.16% |
| Water theft / fraud | 14 | 0.12% |
| Groundwater | 12 | 0.10% |
| Irrigation / agricultural | 3 | <0.1% |
| Fisheries | 1 | <0.1% |
| Not water-related | 38 | 0.32% |

**Theoretical significance (Legal Last Mile thesis):**

The near-absence of informal settlement cases (**0.75%**) is not evidence that excluded populations have fewer legal problems — it is evidence that they cannot access the legal system as plaintiffs in the first place. This confirms the **"Administrative Ghost" thesis**: residents of irregular settlements are excluded *before* they can litigate, lacking the formal address, utility contract, or property title required to establish standing as a water user.

By contrast, **48.52%** of Brazilian cases are tariff disputes — a category that *presupposes* an existing formal water contract. The distribution reveals a legal system that adjudicates the terms of service for the connected while remaining structurally invisible to the unconnected.

**Win/loss outcomes (4,481 coded decisions):**

| Outcome | Count | % of coded |
|---|---|---|
| User / plaintiff wins | 1,400 | 31.2% |
| Utility wins | 1,165 | 26.0% |
| Mixed outcome | 1,916 | 42.8% |
| Unclear / no outcome language | ~7,243 | — |

> Users prevail in **31.2%** of coded decisions — modestly more than utilities (26.0%). The dominance of "mixed" outcomes (42.8%) reflects Brazilian courts' frequent practice of partially granting relief (e.g., ordering reconnection while upholding arrears). Win/loss coding is unavailable for decisions with non-standard outcome language, particularly TJDFT (Brasília), which uses administrative docket framing.

**Win/loss by thesis-critical category:**

| Category | n | User wins | Win rate |
|---|---|---|---|
| Tariff dispute | 5,689 | 1,048 | 18.4% |
| Connection refusal | 1,275 | 220 | 17.3% |
| **Informal settlement** | **88** | **0** | **0.0%** |
| Pipe leak / damage | 190 | 45 | 23.7% |

**Zero user wins in informal settlement (n = 88)** is the starkest quantitative expression of the Administrative Ghost thesis.

**Human rights language:** **1.93%** of Brazilian decisions (226/11,724) invoke human rights or right-to-water framing — despite Brazil's constitutional guarantee of sanitation access (Art. 6, CF/1988). HR language is **0.0%** in informal settlement decisions specifically.

**Public interest / Ministério Público:**
- MP involvement: 427 cases (3.6%)
- Public interest / collective framing: 1,616 cases (13.8%)

---

## Netherlands — Pre-Litigation Absorption

The Netherlands' **68,654 cases** show a governance distribution now fully clarified by the v0.3.0 residual audit:

| Category | Count | % |
|---|---|---|
| **Not water-related** | **67,665** | **98.56%** |
| Other water (genuine residual — has water vocab) | 338 | 0.49% |
| Flood protection | 212 | 0.31% |
| Spatial planning / water assessment | 98 | 0.14% |
| Waterboard governance (waterschap) | 79 | 0.12% |
| Regulatory permit | 65 | 0.09% |
| Environmental protection | 60 | 0.09% |
| Sanitation / sewage | 26 | 0.04% |
| Riparian / waterway | 19 | 0.03% |
| Groundwater | 14 | 0.02% |
| Water quality | 12 | 0.02% |
| Hydroelectric / dam | 11 | 0.02% |
| Fisheries | 9 | 0.01% |
| Flooding / drainage | 8 | 0.01% |
| **Connection refusal** | **8** | **0.012%** |
| Other classified | 30 | 0.04% |

**Note on the not_water_related category (v0.3.0):** 67,665 NL decisions (98.56%) were classified as not water-related by the v0.3.0 vocabulary filter. This includes: 15,589 from a pre-existing immigration/asylum pre-filter (v0.2.x), 50,545 moved from the old other_water residual (no substantive water vocabulary in title/summary), and 1,531 reclassified from old substantive categories that failed the vocabulary check. A gold-standard precision/recall evaluation (207 NWR decisions, hand-coded) found the filter operates at **99.79% population-weighted precision** — approximately 141 false positives estimated in the full 67,703 NWR bucket, all confirmed as systemic governance cases with zero connection-refusal or informal-settlement content.

**The *aansluitplicht* confound:** A search for *aansluitplicht* (connection obligation) in NWR returns 14 decisions — all electricity (Elektriciteitswet Art. 23, CBB) or heat network (Warmtewet) cases, zero water/sanitation. This is an affirmative finding: Dutch water-sanitation connection disputes are resolved by the Geschillencommissie Energie & Water and National Ombudsman, not by courts indexed in Rechtspraak.nl.

**Theoretical significance:**

The near-total absence of household connection refusal cases (**8 decisions, 0.012% of 68,654**) reflects the **pre-litigation absorption model**: the Netherlands' universal service obligation, administrative objections procedure (bezwaar/beroep under the Awb), Geschillencommissie consumer tribunal, and Ombudsman system resolve household disputes before they reach courts. Formal judicial proceedings address water governance at the systemic level — flood protection, environmental licensing, spatial planning, waterboard governance — not at the household service level.

---

## Canada — Fragmented Opacity

Canada's **3,218 cases** show an intermediate and substantively different pattern, dominated by resource and environmental governance rather than urban service access:

| Category | Count | % |
|---|---|---|
| Other water (unclassified) | 2,797 | 86.9% |
| Fisheries | 160 | 5.0% |
| Riparian / waterway | 108 | 3.4% |
| Hydroelectric / dam | 44 | 1.4% |
| Irrigation / agricultural | 38 | 1.2% |
| Sanitation / sewage | 34 | 1.1% |
| Regulatory permit | 15 | 0.5% |
| Flooding / drainage | 11 | 0.3% |
| Tariff dispute | 6 | 0.2% |
| Groundwater | 3 | 0.1% |
| Flood protection | 2 | 0.1% |

**Theoretical significance:**

Canada's water law disputes are predominantly about **resource governance** (fisheries, riparian rights, hydroelectric licensing, agricultural water allocation) rather than household water service access — the inverse of Brazil's pattern. The near-absence of connection refusal and tariff disputes reflects both the provincial-level service delivery model (no federal universal service obligation) and the opacity of administrative processes: disputes are resolved at the municipal or utility level before reaching courts.

The fisheries category (160 cases, 5.0%) reflects the jurisdictional reach of the federal *Fisheries Act*, which generates litigation across provinces on water quality and habitat protection — a distinctly Canadian pattern absent in Brazil and the Netherlands.

**Indigenous water rights:** 0 cases coded as `indigenous_water` in the current dataset — almost certainly an undercount reflecting the limitations of keyword-based coding on title-only CanLII records rather than the absence of such disputes. First Nations water insecurity generates significant administrative and political contestation that is largely invisible in the formal judicial record.

---

## Comparative Summary

| Dimension | Brazil | Canada | Netherlands |
|---|---|---|---|
| Total cases | 11,724 | 3,218 | 68,654 |
| Dominant dispute type | Tariff (48.52%) | Fisheries/riparian (8.4%) | Not water-related (98.56%) |
| Connection refusal | 10.88% | ~0% | 0.012% (8 cases) |
| Informal settlement | 0.75% | 0% | 0% |
| User wins — informal settlement | **0.0%** | N/A | N/A |
| HR language | 1.93% | 0% | 0% |
| User win rate (coded) | 31.2% | N/A | N/A |
| Pre-litigation absorption | Low | Medium | High |
| Legal Last Mile model | Rights-declared, administration-deficient | Fragmented opacity | Pre-litigation absorption |

**Key cross-national observation:** The governance distribution across all three jurisdictions is consistent with the **Legal Last Mile thesis**. Where administrative systems are robust and universal (Netherlands), courts address systemic governance, not household access. Where administrative filtering is weak (Brazil), courts are flooded with household service disputes — but only for the *formally connected*. The pattern of who *doesn't* appear in court (the informally settled, the unconnected) is as theoretically important as who does.

---

## Validation — v0.3.0 Results

**Gold-standard precision/recall (207 NWR decisions, author hand-coded):**

| Stratum | Stratum precision | Population weight |
|---|---|---|
| NL broad water vocabulary (193 cases) | 0.358 | 0.29% |
| NL *aansluitplicht* (12 cases) | 1.000 | 0.02% |
| NL plain / no water vocab (67,460 cases) | 1.000 | 99.64% |
| Brazil NWR (38 cases) | 0.538 | 0.06% |
| **Population-weighted precision** | **99.79%** | |

Estimated false positives in full 67,703 NWR bucket: ~141 decisions (0.21%). None involve connection refusal or informal settlement.

**Inter-coder reliability (91-decision overlap, κ computed May 2026):**

| Metric | Value |
|---|---|
| Cohen's κ | 0.734 |
| 95% CI (bootstrap, 2,000 iter.) | [0.622, 0.835] |
| Observed agreement | 82.4% |
| Connection refusal disagreements | 0 |
| Informal settlement disagreements | 0 |

The kappa is in the moderate-to-substantial range; the CI overlaps 0.75 (the standard threshold for JELS/jurimetrics publications). Zero disagreements on the two thesis-critical labels.

---

## Coding Methodology Note (v0.3.0)

The v0.2.x dataset left 57,695 decisions (69%) in `other_water`. The v0.3.0 engine applied a global water-core vocabulary check and three Brazil rescue patterns (tariff +55, connection refusal +115, pipe damage +151). Result: 67,703 decisions reclassified to `not_water_related`; genuine residual reduced from 57,695 to 6,904.

The `other_water` genuine residual (6,904 decisions, 8.3% of corpus) reflects three structural mechanisms:
1. **Netherlands** — Rechtspraak.nl returns all published decisions; water is often mentioned incidentally in planning/environmental cases whose short XML summaries don't carry the core vocabulary
2. **Canada** — CanLII records for many courts provide only case titles; water law cases identified by title matching, leaving the substantive issue unclassifiable
3. **Brazil** — 32.15% of Brazil corpus remains in genuine residual; TJDFT uses administrative docket language that pattern-matching cannot fully parse

Full explanation in [`validation/RESIDUAL_AUDIT.md`](https://github.com/jrklaus8/water-law-dataset/blob/main/validation/RESIDUAL_AUDIT.md).

---

*Dataset v0.3.0 · jurimetric_coding.py v2.0 · May 2026*
