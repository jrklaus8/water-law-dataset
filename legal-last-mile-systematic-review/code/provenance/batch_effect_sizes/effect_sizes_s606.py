import csv, os, tempfile

EF = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

def main():
    with open(EF, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    assert not any(r["study_id"] == "S606" for r in rows)

    new_row = {
        "study_id": "S606",
        "outcome_family": "service_coverage",
        "synthesis_family": "C",
        "exposure_definition": ("Share of a Chinese prefectural city's population who are temporary "
            "residents without official permanent household registration (hukou) -- a legal/"
            "administrative status ascribed at birth that determines eligibility for place-specific "
            "public services -- measured across 290 cities, 2008-2014."),
        "comparator_definition": ("Within-city variation over time and across-city variation in the "
            "share of hukou-registered (permanent) vs. unregistered (temporary) resident population, "
            "analyzed via city and year fixed effects (panel comparison, not a discrete treatment/"
            "control group)."),
        "effect_measure": "Panel fixed-effects regression coefficient (city and year fixed effects, clustered standard errors)",
        "effect_estimate": ("A one-percentage-point increase in the share of hukou-unregistered "
            "temporary residents is associated with a reduction of 0.00164 (10,000 m3/day) per 10,000 "
            "persons in wastewater treatment capacity (p<0.01) and 0.0897 tons/day per 10,000 persons "
            "in solid waste treatment capacity (p<0.01); also significant negative associations with "
            "quantity of wastewater treated (p<0.1) and quantity of solid waste treated (p<0.1). No "
            "significant association with public green space provision. For an average city of ~1.5 "
            "million residents, results imply a need for an additional 2,460 m3/day wastewater "
            "treatment capacity and 13.455 tons/day solid waste treatment capacity per 1-percentage-"
            "point increase in temporary-resident share merely to maintain constant per-capita service "
            "levels."),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "0.000529 (wastewater treatment capacity); 0.0268 (solid waste treatment capacity)",
        "sample_size": "290 cities; 1,577-1,769 city-year observations across 5 outcome models (2008-2014)",
        "direction": "negative (higher hukou-unregistered temporary-resident share associated with lower per-capita pollution-treatment infrastructure provision)",
        "adjusted": "adjusted (population density, GRP per capita, education enrollment, unemployment rate, government spending per capita; city and year fixed effects)",
        "evidence_status": "OBSERVED",
        "provenance_note": ("extraction_database.csv S606; source Zhou & Liang 2021, J. Environmental "
            "Policy & Planning 23(6):781-795, Table 3. A clean legal/administrative-status exposure "
            "(hukou household registration) tested via panel fixed-effects regression against a "
            "directly measured, population-relevant infrastructure-provision outcome across 290 cities "
            "and 7 years, with consistent significant results and multiple robustness checks (lagged "
            "and cross-sectional change models in the appendix)."),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": ("ANALYSIS_PLAN.md S2 -- single quantitative study using a "
            "China-specific hukou household-registration exposure and a wastewater/solid-waste "
            "treatment-capacity outcome; no other Family C study in the corpus shares this specific "
            "institutional/legal operationalization (household-registration-based service exclusion), "
            "so pooling is not yet possible or meaningful."),
    }
    rows.append(new_row)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EF) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EF)

    print("Appended effect_sizes row for S606")

if __name__ == "__main__":
    main()
