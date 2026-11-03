#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
for sid in ("S1121", "S1122"):
    assert sid not in existing_ids

new_rows = [
    {
        "study_id": "S1121",
        "outcome_family": "water_access",
        "synthesis_family": "A",
        "exposure_definition": (
            "Local government adoption of a water-adequacy screening policy "
            "(an administrative-review growth-control mechanism requiring "
            "demonstration of long-term water supply before residential "
            "development approval, under California SB 901/610/221), 289 "
            "jurisdictions, 1994-2003."
        ),
        "comparator_definition": (
            "Jurisdictions/periods without a water-adequacy screening policy in "
            "place, and, separately, the presence vs. absence of price-based water "
            "connection impact fees within the same jurisdictions."
        ),
        "effect_measure": "Fixed-effects/random-effects panel regression coefficient (semi-elasticity)",
        "effect_estimate": (
            "Water adequacy rule coefficient -0.31** to -0.53** (FE models; "
            "semi-elasticity -0.26 to -0.41) and -0.18* to -0.29** (RE models; "
            "implied reduction 16%-25%). Overall, adoption of a water-adequacy "
            "screening policy reduces new residential permitting by approximately "
            "16%-41% depending on sample/specification. Water connection impact "
            "fees (price-based mechanism) show no statistically significant effect "
            "on housing growth in any specification."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "0.10-0.21 (water adequacy rule coefficient, across specifications)",
        "sample_size": "289 jurisdictions (Full Sample), 1994-2003 panel (2,890 observations)",
        "direction": "negative (water-adequacy screening reduces new residential water-connection permitting)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1121; source Hanak 2008, Land Economics, "
            "Tables 2-4. Family A (legal recognition/institutional-management-model "
            "and access): fixed-effects/random-effects panel-regression estimates "
            "directly isolating an administrative/legal institutional mechanism's "
            "(water-adequacy screening review) effect on new-housing/water-"
            "connection access, controlling for MSA price growth, prime rate, "
            "pre-1990 housing stock, and other growth controls; robustness checked "
            "via Hausman and Granger-causality tests."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
            "exposure-outcome pairing (water-adequacy administrative screening "
            "policy and new-residential-permitting growth in US jurisdictions); no "
            "other Family A study yet shares this operationalization, so pooling is "
            "not yet possible or meaningful."
        ),
    },
    {
        "study_id": "S1122",
        "outcome_family": "water_access",
        "synthesis_family": "A",
        "exposure_definition": (
            "Legal/administrative zoning status of residence (zoned vs. non-zoned/"
            "spontaneous-settlement land-allocation status) and residence status "
            "(owner vs. renter), Ouagadougou, Burkina Faso."
        ),
        "comparator_definition": (
            "Zoned-periphery residents (reference category) vs. non-zoned-"
            "periphery (informal-settlement) residents; owner/co-owner residents "
            "(reference) vs. renting/co-renting residents; interaction of tenure "
            "status by zone."
        ),
        "effect_measure": "Cox proportional-hazards regression, hazard ratios",
        "effect_estimate": (
            "Zone of residence (zoned periphery = reference): non-zoned periphery "
            "hazard ratio = 0.14*** for first access to piped water (formal "
            "connection explicitly described as 'not possible in non-zoned "
            "areas'); downtown hazard ratio = 3.12***. Residence status (owner/"
            "co-owner = reference): renting/co-renting hazard ratio = "
            "2.56***-2.94**. Interaction terms: renting * non-zoned periphery "
            "hazard ratio = 0.00***; other's-residence * non-zoned periphery "
            "hazard ratio = 0.00***. Access disparity: 48% of households had "
            "piped water access in the city centre vs. 22% in zoned peripheral "
            "areas (2000 data)."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "residential life-history person-time data, Ouagadougou",
        "direction": "negative (non-zoned/informal legal status sharply reduces hazard of gaining piped water access; effect compounded for renters)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1122; source Dos Santos & LeGrand 2013, "
            "Urban Studies, Tables 2-4. Family A (legal recognition/institutional-"
            "management-model and access): Cox proportional-hazards event-history "
            "estimates directly isolating a legal/administrative zoning-status "
            "mechanism's effect on first access to piped water, adjusted for "
            "migration origin, gender, education, and employment type."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
            "exposure-outcome pairing (zoned/non-zoned legal settlement status and "
            "piped-water-access hazard in Ouagadougou); no other Family A study yet "
            "shares this operationalization, so pooling is not yet possible or "
            "meaningful."
        ),
    },
]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
