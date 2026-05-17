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
3. **The *aansluitplicht* confound:** A search for Dutch connection-obligation vocabulary in NWR
   returns 14 cases — all electricity/heat network, zero water/sanitation. This is an
   affirmative finding confirming pre-litigation absorption (see §4 and `METHODS_NOTE_aansluitplicht.md`).

**Full analysis:** [`RESIDUAL_AUDIT.md`](RESIDUAL_AUDIT.md)

## Files in This Folder

| File | Purpose |
|---|---|
| `RESIDUAL_AUDIT.md` | Full audit — reconciliation table, NWR purity, *aansluitplicht* confound, thesis robustness |
| `residual_audit.py` | Reproduces the audit from any coded CSV |
| `second_coder_protocol.md` | Route B: second-coder kappa protocol + §6 gold-standard precision/recall evaluation |
| `kappa_calculator.py` | Cohen's kappa + bootstrap CI + per-category agreement |
| `transformer_classifier.py` | Route A: XLM-RoBERTa fine-tuning and residual classification |
| `METHODS_NOTE_aansluitplicht.md` | Standalone methods note: cross-utility lexical confounds in Dutch administrative law |

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
