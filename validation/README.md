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

No. The residual is dominated by false positives — non-water court decisions
that entered the dataset from the broad keyword scrape. 97.9% of residual
decisions contain no substantive water vocabulary. Of the 818 Brazil residual
cases that *do* contain water vocabulary, only 36 are plausible connection-refusal
cases and 8 are plausible informal-settlement cases — quantities too small to
materially alter the core findings.

**Full analysis:** [`RESIDUAL_AUDIT.md`](RESIDUAL_AUDIT.md)

## Files in This Folder

| File | Purpose |
|---|---|
| `RESIDUAL_AUDIT.md` | Full audit report with tables and thesis robustness check |
| `residual_audit.py` | Reproduces the audit from any coded CSV |
| `second_coder_protocol.md` | Route B: second-coder validation and kappa protocol |
| `kappa_calculator.py` | Cohen's kappa + bootstrap CI + per-category agreement |
| `transformer_classifier.py` | Route A: XLM-RoBERTa fine-tuning and residual classification |

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
