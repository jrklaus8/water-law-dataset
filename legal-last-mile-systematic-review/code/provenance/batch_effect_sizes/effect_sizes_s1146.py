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

new_rows = [
    {
        "study_id": "S1146",
        "outcome_family": "water_access",
        "synthesis_family": "C",
        "exposure_definition": (
            "Regional incidence of utilities-sector corruption (Afrobarometer round 7, multi-country "
            "Africa sample), measured as the share of households in a region reporting corruption "
            "experiences with utilities officials."
        ),
        "comparator_definition": "Households in regions with lower/zero reported utilities-sector corruption incidence, holding piped-water-system presence, urban/rural location, gender, and country fixed effects constant.",
        "effect_measure": "Probit / ordered probit regression, marginal effects (region-clustered standard errors, country fixed effects)",
        "effect_estimate": (
            "Regional utilities corruption has a statistically significant negative marginal effect "
            "on the likelihood a household reports access to enough clean water (Table 2), robust to "
            "controlling for individual bribery experience and confirmed in an ordered-probit "
            "specification (Table 3, N=44,778). A household in the most-corrupt sampled area is "
            "approximately 10% less likely to report adequate water access than one in the cleanest "
            "area; a one-standard-deviation increase in the corruption measure is associated with an "
            "approximate 0.5% drop in reported access likelihood."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "clustered by region (Tables 2-4)",
        "sample_size": "N = 44,778 (Table 3, ordered probit)",
        "direction": "negative (higher regional utilities-sector corruption reduces likelihood of reported adequate household water access)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1146; source Breen & Gillanders 2024, Governance, Tables 2, 3 "
            "and 4. Family C (administrative/legal barriers and access inequality): probit/ordered-"
            "probit regression estimates with country fixed effects and region-clustered standard "
            "errors directly isolating a corruption-based administrative-barrier mechanism's effect "
            "on differential household water access."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact exposure-outcome "
            "pairing (regional utilities-sector corruption incidence and household water-access "
            "likelihood, multi-country Africa); no other Family C study yet shares this "
            "operationalization, so pooling is not yet possible or meaningful."
        ),
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
