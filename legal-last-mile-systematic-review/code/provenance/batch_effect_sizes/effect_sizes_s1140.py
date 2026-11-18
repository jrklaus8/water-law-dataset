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
        "study_id": "S1140",
        "outcome_family": "service_coverage",
        "synthesis_family": "B",
        "exposure_definition": (
            "Village communities' self-organized network capital in applying for "
            "Rural Water Supply and Sanitation Program (RWSSP) infrastructure "
            "funding, Nepal: (1) number of organizational partners, (2) indirect "
            "bridging reach to other communities via partners, (3) subgroup "
            "cohesion among partners."
        ),
        "comparator_definition": "Communities with fewer partners, less indirect reach, and lower partner cohesion, holding other covariates at their means.",
        "effect_measure": "Logistic regression, log odds / predicted probability",
        "effect_estimate": (
            "Number of partners: log odds 0.55*** (SE 0.10); predicted funding-"
            "success probability rises from 0.02 (1 partner) to 0.38 (7 partners, "
            "mean) to 0.99 (16 partners, maximum). Indirect reach: probability "
            "rises from 0.02 (0 reach) to 0.044 (12, mean) to 0.31 (38, maximum). "
            "Subgroup cohesion: probability rises from 0.43 (0, minimum) to 0.51 "
            "(16, average) to 0.86 (100, maximum). Remote communities "
            "significantly less likely to be funded."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "0.10 (number of partners); Hubert-White robust, clustered (UCINET hierarchical clustering, 37 clusters)",
        "sample_size": "RWSSP applicant communities, Nepal",
        "direction": "positive (greater network capital -- partners, reach, cohesion -- increases probability of securing water/sanitation infrastructure funding)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1140; source Shrestha 2013, Journal of Public "
            "Administration Research and Theory, Table 3 and Figure 2. Family B "
            "(administrative assistance/access): logistic-regression estimates with "
            "robust clustered standard errors directly isolating a network-capital/"
            "bureaucratic-assistance institutional mechanism's effect on "
            "communities' success in securing water/sanitation infrastructure "
            "program funding."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
            "exposure-outcome pairing (self-organized network capital and RWSSP "
            "funding-application success in Nepal); no other Family B study yet "
            "shares this operationalization, so pooling is not yet possible or "
            "meaningful."
        ),
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
