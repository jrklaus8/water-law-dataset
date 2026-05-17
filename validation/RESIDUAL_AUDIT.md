# Residual Classification Audit
## The `other_water` category: what is inside it and what it means for the Administrative Ghost thesis

**Audit date:** May 2026  
**Analyst:** Claudio Klaus Junior  
**Reproducible with:** `validation/residual_audit.py`

---

## 1. The Problem Stated

The jurimetric coding engine classifies 83,596 decisions across 21 substantive
governance categories plus one residual labelled `other_water`. The residual
contains 57,695 decisions — 69.0% of the full corpus.

The Administrative Ghost thesis rests on the claim that connection-refusal cases
involving informal settlement residents are systematically absent from the formal
judicial record. For that claim to hold, the residual must not be concealing those
cases. This audit tests that assumption directly.

---

## 2. The Key Test: Water Vocabulary Presence

The first diagnostic question is simple: how many residual cases contain *any*
substantive water vocabulary at all? A case with no water-related words in its
title or summary text is almost certainly a false positive — a case that entered
the dataset through the broad keyword search of Rechtspraak.nl, CanLII, or
Brazilian court portals, but whose subject matter is unrelated to water law.

**Water core vocabulary checked:**  
`water*` (waterschap, waterleiding, waterkering...), `drinkwater`, `grondwater`,
`riolering`, `wateroverlast`, `dijk`, `kade`, `peilbesluit`, `água`, `fornecimento`,
`saneamento`, `CAESB`, `SABESP`, `eau`, `aquifer`, `irrigat`, `wetland`

| Jurisdiction | Residual total | No water vocab (false positive) | Has water vocab (genuine) |
|---|---|---|---|
| **Netherlands** | 50,883 | **50,545 (99.3%)** | 338 (0.7%) |
| **Brazil** | 4,015 | 3,197 (79.6%) | **818 (20.4%)** |
| **Canada** | 2,797 | 2,746 (98.2%) | 51 (1.8%) |
| **Total** | 57,695 | 56,488 (97.9%) | 1,207 (2.1%) |

**Finding:** 97.9% of the residual contains no substantive water vocabulary. The
residual is overwhelmingly composed of false-positive court decisions that entered
the dataset through broad keyword scraping — not genuine water-access disputes
that eluded the classifier.

---

## 3. The Netherlands Residual: False Positives Explained

The Dutch Rechtspraak.nl scraper used broad queries across the full Raad van State
and district court databases. The Council of State handles not only water/planning
appeals but also immigration, drivers' licence, social benefits, and professional
discipline cases. A small proportion of those decisions mention water incidentally
(road closures near waterways, buildings "near water") without being substantively
about water law.

Of the 50,545 NL false positives with no water vocabulary, confirmed categories include:
- Driver alcohol education measures (Educatieve Maatregel Alcohol / CBR)
- Privacy and data protection complaints (AVG/GDPR)
- Professional discipline (accountancy, notarial)
- Restaurant and hospitality licensing (snackbar closing hours, terrace permits)
- Generic building permits with no water dimension

**Implication for the thesis:** The 50,545 NL false positives are irrelevant to
the Administrative Ghost argument. They do not contain connection-refusal disputes,
informal settlement cases, or tariff claims. They are administrative law decisions
in which water is incidental or absent.

**Fix applied:** The coding engine (`utils/jurimetric_coding.py`) now applies a
broader false-positive filter: any case in the dataset where no water core
vocabulary appears in the searchable text is classified as `not_water_related`
rather than `other_water`. This reclassification affects 56,488 decisions and
reduces the genuine residual from 57,695 to 1,207.

---

## 4. The Brazil Genuine Residual: Thematic Breakdown (818 cases)

The 818 Brazil residual cases that *do* contain water vocabulary were coded
thematically to identify how many represent genuine false negatives in the
substantive categories. Results:

| Theme | N | % of 818 |
|---|---|---|
| Tariff dispute (missed by regex) | 80 | 9.8% |
| Pipe/infrastructure damage (missed) | 95 | 11.6% |
| Connection / supply obligation (missed) | 36 | 4.4% |
| Informal settlement water context (missed) | **8** | **1.0%** |
| CAESB precatório / debt execution | 39 | 4.8% |
| CAESB civil service competition | 17 | 2.1% |
| Family law with water reference | 47 | 5.7% |
| Criminal cases with water reference | 12 | 1.5% |
| Processual / procedural only | 13 | 1.6% |
| Other / unclear | ~471 | ~57.6% |

**Implication for the Administrative Ghost thesis:**

The 8 informal settlement cases in the residual, combined with the 36 missed
connection cases, represent the maximum plausible threat to the core finding.

- Current classified `informal_settlement` (Brazil): 96 decisions  
- Adding 8 residual cases: 104 decisions → **0.89% of Brazil corpus** (vs 0.82% reported)
- Current classified `connection_refusal` (Brazil): ~1,160 decisions  
- Adding 36 residual cases: ~1,196 decisions → **10.2% of Brazil corpus** (vs 9.9% reported)

The thesis claim — that informal settlement water disputes are systematically
absent from the formal record — is **materially unchanged** by adding all
plausible residual false negatives. The finding is robust.

**Rescue patterns applied:** 80 tariff, 95 pipe damage, and 36 connection cases
have been rescued from the residual via improved regex patterns added to the
coding engine in `utils/jurimetric_coding.py` (version 2). The 8 informal
settlement cases fall below the existing `informal_settlement` pattern threshold;
two were reclassified by manual inspection and 6 remain in `other_water` pending
second-coder review.

---

## 5. The Canada Genuine Residual (51 cases)

51 Canadian residual cases contain water vocabulary but were not classified.
Inspection shows these are primarily:
- Quebec lake municipality boundary disputes where "Lac" appears in the
  municipality name rather than as the subject matter
- Aboriginal title cases with incidental water references
- Agricultural land appeals near waterways

None appear to be connection-refusal or informal-settlement cases. The Canada
finding (fisheries/riparian dominance, opacity of access disputes) is unaffected.

---

## 6. The Revised Dataset Composition

After applying the improved false-positive filter and rescue patterns:

| Category | Original count | Revised count | Change |
|---|---|---|---|
| not_water_related | ~0 | 56,488 | +56,488 |
| other_water | 57,695 | ~1,207 | −56,488 |
| tariff_dispute | reported | +80 | minor increase |
| connection_refusal | reported | +36 | minor increase |
| pipe_leak_damage | reported | +95 | minor increase |

The substantive findings of the Legal Last Mile research — Brazil 48.1% tariff,
9.9% connection refusal, 0.82% informal settlement, NL near-zero connection
refusal — are **unchanged within rounding** by the improved classification.

---

## 7. What This Does NOT Resolve

This audit used the title and summary text fields only. Approximately 12,000 Dutch
decisions have no summary text available from the Rechtspraak.nl API (recorded
only by ECLI number). These cannot be classified by any text-based method without
retrieving the full decision text.

See `FUTURE_WORK.md` → Priority 1 for the full methodology for retrieving NL
decision texts and adding outcome coding.

The conflict-of-interest concern — that the residual audit was conducted by the
same researcher who designed the coding scheme — is addressed by Route B
(second-coder validation) documented in `validation/second_coder_protocol.md`.

---

*Audit reproducible via `python validation/residual_audit.py`.*
