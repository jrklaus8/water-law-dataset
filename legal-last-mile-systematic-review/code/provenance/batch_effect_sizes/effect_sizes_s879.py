#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EFF = f"{BASE}/05_analysis/effect_sizes/effect_sizes.csv"

with open(EFF, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

assert "S879" not in existing_ids

rows.append({
    "study_id": "S879",
    "outcome_family": "water_access",
    "synthesis_family": "C",
    "exposure_definition": "Randomized assignment to systematic contract enforcement (transparent, credible service-disconnection notices for nonpayment, per the terms of the property owner's utility connection-loan contract), Nairobi informal settlements.",
    "comparator_definition": "Disconnection-eligible control compounds exempted from enforcement (ad hoc/no systematic disconnection).",
    "effect_measure": "Randomized controlled trial, intent-to-treat regression estimates with robust standard errors, 9-month follow-up survey plus 5 years of daily administrative billing panel data",
    "effect_estimate": "Payment likelihood within one month increased by 30 percentage points from an 11-percentage-point control base (p<0.001); total payments increased by US$8.80 from a US$5.02 base (p<0.001). Water-access outcomes at 9-month endline: piped water/sanitation connection rates statistically indistinguishable between treatment and control (most of 96 disconnected compounds reconnected after partial payment); main water source = piped water 4.4 percentage points higher in treatment, not significant (p=0.243); monthly water spending Control US$6.62 vs Treatment US$6.86 (p=0.803); weekly water-collection time Control 118 min vs Treatment 100 min (p=0.388) -- a precisely estimated null effect of contract enforcement on actual household water access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "field experiment across Nairobi informal-settlement compounds with utility connection loans; 96 disconnected compounds in enforcement arm; 5-year daily billing panel (2014-2018) plus 9-month post-intervention survey",
    "direction": "positive and significant for payment compliance; null (no significant effect) for water access, connection rates, spending and collection time",
    "adjusted": "adjusted (randomized design with baseline balance checks; robust standard errors)",
    "evidence_status": "OBSERVED",
    "provenance_note": "extraction_database.csv S879; source Coville, Galiani, Gertler & Yoshida 2025, Review of Economics and Statistics (NBER WP 27569), Tables 4-7. Randomized controlled trial directly isolating a specific contractual/legal enforcement mechanism (disconnection-for-nonpayment) with directly measured household water-access outcomes -- a genuine Family C (legal/administrative barriers and access inequality) estimate with a precisely estimated null result on access despite a strong effect on payment compliance.",
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-comparator (RCT of utility contract-disconnection enforcement on household water access, Nairobi); no other Family C study yet shares this specific operationalization, so pooling is not yet possible or meaningful (too few independent studies in this family, per PROJECT_SPEC.md S8 guidance).",
})

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EFF))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EFF)

print(f"New total: {len(rows)}")
