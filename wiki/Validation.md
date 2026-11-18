# Validation — Residual Audit and Reproducibility Audit (v0.3.0)

This page summarises the validation infrastructure in the [`validation/`](https://github.com/jrklaus8/water-law-dataset/tree/main/validation) folder. Full detail is in [`RESIDUAL_AUDIT.md`](https://github.com/jrklaus8/water-law-dataset/blob/main/validation/RESIDUAL_AUDIT.md).

---

## The problem

Under the earlier engine (v0.2.x) most decisions sat in a residual bucket called `other_water`. A reviewer at a socio-legal journal will ask what is inside it, and whether it hides the very connection-refusal or informal-settlement cases that the *Administrative Ghost* thesis says are absent. If it did, the comparative argument would fail.

## The answer in short

Mostly no. The residual was dominated by false positives from a deliberately broad keyword scrape, not by hidden substantive cases.

| Jurisdiction | v0.2.x not water-related | v0.2.x other water | v0.2.x classified | v0.3.0 not water-related | v0.3.0 other water | v0.3.0 classified |
|---|---|---|---|---|---|---|
| Brazil | 0 | 4,015 | 7,709 | 38 | 3,769 | 7,917 |
| Netherlands | 15,589 | 50,883 | 2,182 | 67,665 | 338 | 651 |
| Canada | 0 | 2,797 | 421 | 0 | 2,797 | 421 |
| **Total** | **15,589** | **57,695** | **10,312** | **67,703** | **6,904** | **8,989** |

What the v0.3.0 engine does (`utils/jurimetric_coding.py`):
- **Water-core vocabulary check on every decision.** A decision with no substantive water vocabulary in its title or summary is coded `not_water_related`, not `other_water`. This moved 50,547 decisions out of the old residual and 1,567 out of old substantive categories (for example, "dijk" appearing as a street name).
- **Three Brazil rescue patterns** recover cases the old regexes missed: tariff disputes (+55), connection refusal (+115) and pipe leak or damage (+151); net 244 decisions rescued from the old residual.

## Is `not_water_related` a clean dustbin?

No, and the audit says so. Some Dutch decisions in that bucket contain real water vocabulary (mainly water-permit and spatial-planning cases); the filter deliberately favours **precision over recall**.

**Gold-standard precision (207 decisions hand-coded by the author, May 2026):**

| Stratum | Stratum precision | Population weight |
|---|---|---|
| NL broad water vocabulary | 0.358 | 0.29% |
| NL *aansluitplicht* | 1.000 | 0.02% |
| NL plain / no water vocabulary | 1.000 | 99.64% |
| Brazil | 0.538 | 0.06% |
| **Population-weighted precision** | **99.79%** | |

About 141 false positives are estimated among the 67,703 `not_water_related` decisions (0.21%); none involve connection refusal or informal settlement.

**The *aansluitplicht* confound.** A search for the Dutch connection-obligation term in the `not_water_related` bucket returns 14 decisions, all electricity or heat-network cases and none about water or sanitation. Dutch water-connection disputes are handled by the Geschillencommissie Energie & Water and the National Ombudsman, outside the courts indexed in Rechtspraak.nl — an affirmative finding consistent with pre-litigation absorption (see `validation/METHODS_NOTE_aansluitplicht.md`).

---

## LLM-assisted reproducibility audit (May 2026)

An independent large-language-model coder applied explicit, documented decision rules to the same 91 decisions, using a three-label scheme (WATER / NOT_WATER / UNCERTAIN). This measures agreement between the keyword engine and an LLM coder; it is a **reproducibility audit, not traditional inter-coder reliability**, and not a human second coder.

| Specification | N | Cohen's κ | 95% CI | Agreement |
|---|---|---|---|---|
| **Documented *mananciais* rule applied** (headline) | 91 | **0.832** | 0.721–0.926 | 90.1% |
| Binary WATER / NOT_WATER, excluding UNCERTAIN | 59 | **0.932** | 0.830–1.000 | 96.6% |
| Cases where coder 1 gave a non-UNCERTAIN label | 63 | 0.821 | 0.685–0.938 | 90.5% |
| Three labels, no rule (pre-calibration baseline) | 91 | 0.568 | 0.440–0.694 | 71.4% |

- **Why the baseline is lower.** 17 of the 26 disagreements concern São Paulo *mananciais* (watershed-protection) cases the author had coded UNCERTAIN because they adjudicate demolition and land-use law, while the LLM coder labelled them WATER because they protect drinking-water sources. The documented rule — *mananciais* protection cases count as water law for Legal Last Mile purposes — resolves a protocol ambiguity rather than masking unreliability.
- **NOT_WATER precision is 97%** (30 of 31) under every specification, which supports the claim that the filter removes non-water cases correctly.
- Agreement by stratum (before the rule): Netherlands plain 95.5%, broad water 86.7%, *aansluitplicht* 100%; Brazil 5.0% before the rule and 90.0% after.

**What this does not validate.** It validates the upstream water / not-water filter. It does **not** validate the downstream 21-category governance scheme (tariff dispute, connection refusal, informal settlement and so on); that is future work. A human bilingual (Portuguese and Dutch) second-coder pass over the 207-decision sample is still recommended before submission to a socio-legal journal. Brazilian win/loss outcome coding is AI-assisted, and the Netherlands sub-dataset carries no outcome coding at all.

> **Note on earlier figures.** Earlier documents quote κ = 0.734 for a previous label file. That figure is superseded; the table above reflects the current audit.

---

## Files in `validation/`

| File | Purpose |
|---|---|
| `RESIDUAL_AUDIT.md` | Full audit: reconciliation, purity of the not-water bucket, the *aansluitplicht* confound, precision and recall, reproducibility audit |
| `residual_audit.py` | Reproduces the audit from any coded CSV |
| `kappa_calculator.py` | Cohen's kappa with bootstrap confidence interval and per-category agreement |
| `kappa_sensitivity.py` | Reproduces the four specifications in the table above (5,000 bootstrap resamples, seed 42) into `kappa_results.json` |
| `second_coder_protocol.md` | Second-coder protocol and the gold-standard evaluation |
| `generate_all_outputs.py` | Regenerates kappa files, the Excel workbook and report data |
| `kappa_results.json`, `kappa_agreement_detail.csv`, `precision_recall_results.json` | Machine-readable results |
| `validation_results.xlsx` | Workbook: summary, kappa, agreement detail, precision/recall, governance breakdown |
| `transformer_classifier.py` | Route A: XLM-RoBERTa fine-tuning to classify the residual |

```bash
export CODED_CSV=data/water_law_global_coded.csv
python validation/residual_audit.py
python validation/kappa_calculator.py --coder1 validation/coder1_labels.csv --coder2 validation/coder2_labels.csv
```

The **systematic review** has its own, separate verification machinery (`verify_repository.py`, a source-verification dossier and human-verification accounting); see [[Systematic Review]].
