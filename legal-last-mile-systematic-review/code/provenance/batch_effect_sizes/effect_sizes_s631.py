#!/usr/bin/env python3
import csv, os, tempfile

DB = "05_analysis/effect_sizes/effect_sizes.csv"


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    assert "S631" not in existing_ids, "S631 already exists"

    row = {
        "study_id": "S631",
        "outcome_family": "service_coverage",
        "synthesis_family": "C",
        "exposure_definition": (
            "Creation of a new local government (kabupaten/kota) via pemekaran -- the "
            "legal/administrative splitting of an existing district jurisdiction into "
            "smaller administrative units -- in Indonesia's post-2001 decentralization "
            "era, exploiting the plausibly exogenous timing of district-splitting "
            "decisions as the identifying exposure."
        ),
        "comparator_definition": (
            "Original (non-split) parent districts, and separately, sibling split-off "
            "districts, all within the same national panel of 336 kabupaten/kota, "
            "2001-2014."
        ),
        "effect_measure": (
            "Generalized difference-in-differences regression coefficient (static "
            "model) and two-step dynamic panel GMM regression coefficient with "
            "district-clustered standard errors"
        ),
        "effect_estimate": (
            "New-district creation reduces household access to protected water and "
            "sanitation by approximately 1% in year 2 relative to original districts "
            "(static DiD model) and by approximately 1.35 percentage points in the "
            "second year of operation (dynamic GMM model), implying a long-run "
            "reduction of approximately 1.75% (beta/(1-gamma) = -1.35/(1-0.23)), "
            "p=.023. No significant contemporaneous or lagged effect relative to "
            "split-off (sibling) districts, and no significant effect on school "
            "enrollment in either comparison. Falsification tests using first and "
            "second leads of the new-district dummy show no significant pre-trend, "
            "supporting the parallel-trends assumption."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "336 districts (98 groups for split-vs-new comparison); 2,714 district-year observations (infrastructure equation, original-vs-new comparison)",
        "direction": "negative (local government proliferation associated with LOWER household water/sanitation access, relative to original non-split districts)",
        "adjusted": (
            "adjusted (total local government spending per capita, population size, "
            "percentage of households with electricity access, percentage of "
            "population in poverty, Gini coefficient of personal consumption, "
            "personal consumption per capita; district and year fixed effects, "
            "district-specific time trends; dynamic model additionally instruments "
            "the lagged dependent variable via two-step difference-GMM)"
        ),
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S631; source Lewis 2017, Journal of Urban "
            "Affairs 39(8):1047-1065, Tables 4-5. A clean legal/administrative-"
            "jurisdictional-restructuring exposure (local government proliferation "
            "via pemekaran) tested by a well-identified quasi-experimental panel "
            "design (generalized DiD plus dynamic GMM, parallel-trends falsification "
            "test) against a directly measured, nationally-representative household "
            "water/sanitation access-percentage outcome (BPS/SUSENAS), with a "
            "statistically significant long-run point estimate."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 -- single quantitative study using an Indonesia-"
            "specific administrative-jurisdiction-splitting exposure and a household "
            "water/sanitation access-percentage outcome; no other Family C study in "
            "the corpus shares this specific institutional/legal operationalization "
            "(local government proliferation/pemekaran), so pooling is not yet "
            "possible or meaningful."
        ),
    }

    rows.append(row)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended effect_sizes row for S631. New total:", len(rows))


if __name__ == "__main__":
    main()
