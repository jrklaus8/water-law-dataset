# Key Findings

Summary of jurimetric analysis across **83,596 decisions (2016–2025)** — Brazil (11,724), Netherlands (68,654), Canada (3,218).  
Coding engine: `jurimetric_coding.py` v2.0 — 21 governance categories, 4 languages (PT/EN/NL/FR).  
Dataset DOI: [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413)

---

## Brazil — Administrative Gatekeeping in Action

Brazil's **11,724 cases** reveal a striking governance distribution:

**Governance category breakdown:**

| Category | Count | % |
|---|---|---|
| Tariff disputes | 5,634 | 48.1% |
| Other water (unclassified) | 4,015 | 34.2% |
| Connection refusal | 1,160 | 9.9% |
| Sanitation / sewage | 264 | 2.3% |
| Water infrastructure contract | 219 | 1.9% |
| Informal settlement | 96 | 0.8% |
| Environmental protection | 63 | 0.5% |
| Water quality | 62 | 0.5% |
| Riparian / waterway | 48 | 0.4% |
| Water theft / fraud | 42 | 0.4% |
| Pipe leak / damage | 39 | 0.3% |
| Flooding / drainage | 32 | 0.3% |
| Regulatory permit | 18 | 0.2% |
| Hydroelectric / dam | 17 | 0.1% |
| Groundwater | 11 | 0.1% |
| Irrigation / agricultural | 3 | <0.1% |
| Fisheries | 1 | <0.1% |

**Theoretical significance (Legal Last Mile thesis):**

The near-absence of informal settlement cases (**0.8%**) is not evidence that excluded populations have fewer legal problems — it is evidence that they cannot access the legal system as plaintiffs in the first place. This confirms the **"Administrative Ghost" thesis**: residents of irregular settlements are excluded *before* they can litigate, lacking the formal address, utility contract, or property title required to establish standing as a water user.

By contrast, **48.1%** of Brazilian cases are tariff disputes — a category that *presupposes* an existing formal water contract. The distribution reveals a legal system that adjudicates the terms of service for the connected while remaining structurally invisible to the unconnected.

**Win/loss outcomes (4,481 coded decisions):**

| Outcome | Count | % of coded |
|---|---|---|
| User / plaintiff wins | 1,400 | 31.2% |
| Utility wins | 1,165 | 26.0% |
| Mixed outcome | 1,916 | 42.8% |
| Unclear / no outcome language | ~7,243 | — |

> Users prevail in **31.2%** of coded decisions — modestly more than utilities (26.0%). The dominance of "mixed" outcomes (42.8%) reflects Brazilian courts' frequent practice of partially granting relief (e.g., ordering reconnection while upholding arrears). Win/loss coding is unavailable for decisions with non-standard outcome language, particularly TJDFT (Brasília), which uses administrative docket framing.

**Human rights language:** **1.9%** of Brazilian decisions (226/11,724) invoke human rights or right-to-water framing — despite Brazil's constitutional guarantee of sanitation access (Art. 6, CF/1988). Rights language is present but not dominant even in a rights-rich system.

**Public interest / Ministério Público:**
- MP involvement: 427 cases (3.6%)
- Public interest / collective framing: 1,616 cases (13.8%)

---

## Netherlands — Pre-Litigation Absorption

The Netherlands' **68,654 cases** show a governance distribution dominated by systemic water governance rather than household service disputes:

| Category | Count | % |
|---|---|---|
| Other water (unclassified) | 50,883 | 74.1% |
| Not water-related (immigration pre-filter) | 15,589 | 22.7% |
| Flood protection | 1,266 | 1.8% |
| Environmental protection | 344 | 0.5% |
| Spatial planning / water assessment | 100 | 0.1% |
| Riparian / waterway | 88 | 0.1% |
| Waterboard governance (waterschap) | 82 | 0.1% |
| Flooding / drainage | 74 | 0.1% |
| Regulatory permit | 73 | 0.1% |
| Sanitation / sewage | 44 | 0.1% |
| Fisheries | 32 | <0.1% |
| Groundwater | 29 | <0.1% |
| Hydroelectric / dam | 24 | <0.1% |
| Water quality | 13 | <0.1% |
| **Connection refusal** | **12** | **<0.1%** |

**Note on the not_water_related category:** 15,589 NL decisions (22.7%) were identified by the pre-filter as vreemdelingenrecht (immigration law) false positives — Dutch administrative court decisions about residence permits that were returned by broad water-related keyword searches. These are genuine published court decisions but are not water law cases; they are excluded from substantive analysis.

**Theoretical significance:**

The near-total absence of household connection refusal cases (**12 decisions, <0.1%**) reflects the **pre-litigation absorption model**: the Netherlands' universal service obligation, administrative objections procedure (bezwaar/beroep under the Awb), Geschillencommissie consumer tribunal, and Ombudsman system resolve household disputes before they reach courts. Formal judicial proceedings address water governance at the systemic level — flood protection, environmental licensing, spatial planning, waterboard governance — not at the household service level.

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
| Dominant dispute type | Tariff (48.1%) | Fisheries/riparian (8.3%) | Systemic governance (74.1%) |
| Connection refusal | 9.9% | ~0% | <0.1% |
| Informal settlement | 0.8% | 0% | 0% |
| HR language | 1.9% | 0% | 0% |
| User win rate (coded) | 31.2% | N/A | N/A |
| Utility win rate (coded) | 26.0% | N/A | N/A |
| Pre-litigation absorption | Low | Medium | High |
| Legal Last Mile model | Rights-declared, administration-deficient | Fragmented opacity | Pre-litigation absorption |

**Key cross-national observation:** The governance distribution across all three jurisdictions is consistent with the **Legal Last Mile thesis**. Where administrative systems are robust and universal (Netherlands), courts address systemic governance, not household access. Where administrative filtering is weak (Brazil), courts are flooded with household service disputes — but only for the *formally connected*. The pattern of who *doesn't* appear in court (the informally settled, the unconnected) is as theoretically important as who does.

---

## Coding Methodology Note

The `other_water` residual (57,695 decisions, 69.0% of total) is a structural feature of the dataset, not a coding failure. Three mechanisms produce it:

1. **Netherlands** — Rechtspraak.nl returns all published decisions; water is often mentioned incidentally in planning/environmental cases whose one-sentence XML summaries don't repeat the water term
2. **Canada** — CanLII records for many courts provide only case titles; water law cases are identified by title matching, leaving the substantive issue unclassifiable
3. **Brazil** — TJSP and some other courts return list-view results where only the citation number and court name are available, not the decision summary

Full explanation in the [dataset methodology note](https://github.com/jrklaus8/water-law-dataset/blob/main/RESEARCH_CONTEXT.md).

---

*Dataset v1.0 · jurimetric_coding.py v2.0 · May 2026*
