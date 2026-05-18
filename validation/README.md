# Validation

This folder contains the inter-coder reliability and residual audit
infrastructure for the Global Water Law Judicial Decisions Dataset.

## The Problem

The jurimetric engine classified 83,596 decisions but left 57,695 (69%) in a
residual bucket labelled `other_water`. A peer reviewer at JELS, Law and Society
Review, or Jurimetrics will ask: what is inside that residual? Could it be
hiding the very connection-refusal or informal-settlement cases the Administrative
Ghost thesis claims are absent?

## The Answer (Short Version)

Mostly no — but the picture is more nuanced than v0.2.x documentation implied.
The `other_water` residual was dominated by false positives from the broad keyword scrape.
The v0.3.0 filter reclassifies 67,703 decisions to `not_water_related`, reducing the genuine
residual from 89.2% → 8.3%. However:

1. **Reconciliation gap:** The full reconciliation (§2 of the audit) accounts for the ~17,120
   NL decisions that appear in `not_water_related` beyond the vocabulary-audit count — they
   comprise 15,589 from the pre-existing immigration filter and 1,531 from old classified
   categories that failed the v0.3.0 vocabulary check.
2. **NWR is not a clean dustbin:** Approximately 263 confirmed (and up to ~2,487 in full text)
   NL NWR decisions contain substantive water vocabulary, predominantly Waterwet permits and
   spatial planning cases. The filter privileges precision over recall (documented in §5).
   **Gold-standard evaluation (207 NWR hand-coded, May 2026): population-weighted precision =
   99.79%; ~141 estimated false positives in 67,703 NWR — zero involve connection refusal or
   informal settlement.**
3. **The *aansluitplicht* confound:** A search for Dutch connection-obligation vocabulary in NWR
   returns 14 cases — all electricity/heat network, zero water/sanitation. This is an
   affirmative finding confirming pre-litigation absorption (see §4 and `METHODS_NOTE_aansluitplicht.md`).
4. **LLM-assisted reproducibility audit (May 2026):** Independent LLM relabelling of 91
   decisions under explicit decision rules. With the documented *mananciais* rule applied:
   κ = 0.832 (95% CI [0.718, 0.926]; agreement 90.1%). Binary WATER/NOT_WATER kappa
   (exclude-UNCERTAIN) κ = 0.932 (n = 59, 95% CI [0.830, 1.000]). Pre-rule three-label
   baseline κ = 0.568 — gap driven by Brazil stratum protocol ambiguity (19/20 Brazil
   *mananciais* cases), resolved by the documented decision rule. NL strata: 95.5% plain,
   86.7% broad_water, 100% aansluiting. NOT_WATER precision 97%. The audit validates the
   upstream water/not-water filter; downstream 21-category governance validation is future
   work. See `kappa_results.json` and §5.2 of `RESIDUAL_AUDIT.md`.

**Full analysis:** [`RESIDUAL_AUDIT.md`](RESIDUAL_AUDIT.md)

## Files in This Folder

| File | Purpose |
|---|---|
| `RESIDUAL_AUDIT.md` | Full audit — reconciliation table, NWR purity, *aansluitplicht* confound, precision/recall, thesis robustness |
| `residual_audit.py` | Reproduces the audit from any coded CSV |
| `second_coder_protocol.md` | Route B: second-coder kappa protocol + §6 gold-standard precision/recall evaluation |
| `kappa_calculator.py` | Cohen's kappa + bootstrap CI + per-category agreement |
| `transformer_classifier.py` | Route A: XLM-RoBERTa fine-tuning and residual classification |
| `METHODS_NOTE_aansluitplicht.md` | Standalone methods note: cross-utility lexical confounds in Dutch administrative law |
| `generate_all_outputs.py` | Reproducibility script: generates kappa files, Excel workbook, and report data |
| `second_coder_sample_raw.csv` | 207-decision stratified NWR sample (NL_broad_water=100, NL_aansluiting=12, NL_plain=60, BR_all=35) |
| `second_coder_labeled.csv` | Same sample with author (coder1) WATER/NOT_WATER/UNCERTAIN labels + reasons |
| `coder1_labels.csv` | Clean coder1 label file for kappa input |
| `coder2_labels_template.csv` | 91-decision template for independent second coder (fill in `coder2_label`, return as `coder2_labels.csv`) |
| `coder1_kappa.csv` | Coder1 labels formatted for `kappa_calculator.py` (91 matched cases) |
| `coder2_labels.csv` | Coder2 labels (91 cases) — **κ = 0.734** |
| `kappa_agreement_detail.csv` | Case-by-case comparison: coder1 vs coder2, agree/disagree flag |
| `kappa_results.json` | Official kappa output: κ, CI, per-category precision/recall |
| `precision_recall_results.json` | Per-stratum and population-weighted precision/recall for the NWR filter |
| `validation_results.xlsx` | 5-sheet Excel workbook: Executive Summary, Kappa Results, Agreement Detail, Precision/Recall, Governance Breakdown |
| `validation_report_data.json` | All validation numbers in machine-readable form |

## Quick Start

**Reproduce the audit:**
```bash
# Set path to your coded CSV
export CODED_CSV=data/water_law_global_coded.csv
python validation/residual_audit.py
```

**Compute kappa (after second-coder labels are available):**
```bash
python validation/kappa_calculator.py \
    --coder1 validation/coder1_labels.csv \
    --coder2 validation/coder2_labels.csv
```

**Train the transformer classifier:**
```bash
# Step 1: prepare data
python validation/transformer_classifier.py prepare

# Step 2: fine-tune (GPU recommended)
python validation/transformer_classifier.py train --model xlm-roberta-base

# Step 3: classify residual
python validation/transformer_classifier.py classify

# Step 4: compare against second coder
python validation/transformer_classifier.py compare
```

## Engine Fix Applied

The false-positive filter in `utils/jurimetric_coding.py` was strengthened
based on this audit. The original filter only caught immigration/asylum cases
in Dutch decisions. The revised filter applies a **water core vocabulary check**
to every decision: any case with no substantive water vocabulary in its title or
summary is classified as `not_water_related` rather than `other_water`.

This reclassifies 56,488 decisions and reduces the genuine residual from 57,695
to approximately 1,207. Three rescue patterns were also added for Brazil tariff,
connection, and pipe-damage cases that the main regex had missed.
