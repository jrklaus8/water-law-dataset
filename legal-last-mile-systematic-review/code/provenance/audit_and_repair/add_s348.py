import csv, os, tempfile, sys
csv.field_size_limit(sys.maxsize)

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

assert len(rows) == 61
assert "S348" not in {r["study_id"] for r in rows}

new_row = {
    "study_id": "S348",
    "outcome_family": "service_coverage",
    "synthesis_family": "C",
    "exposure_definition": (
        "Ghanaian local government district classified as 'badly_managed' -- a "
        "governance-quality cluster identified via fuzzy c-means clustering on "
        "district characteristics (population size, density, poverty, and percentage "
        "of annual action plan implemented) -- distinguished from the separate "
        "'rural_poor' cluster because 'badly_managed' districts are not economically "
        "poor, isolating governance/institutional quality from socio-economic context "
        "as the exposure."
    ),
    "comparator_definition": (
        "Other Ghanaian local government district cluster types identified in the "
        "same classification ('big_wealthy_urban', 'middling', 'small'), within the "
        "same national cross-section of Ghanaian local government districts, 2021 "
        "secondary data."
    ),
    "effect_measure": (
        "Hierarchical multivariate regression coefficient on cluster-membership dummy "
        "variables (fuzzy c-means clustering + regression design)"
    ),
    "effect_estimate": (
        "'badly_managed' districts have access to infrastructure -- especially safe "
        "drinking water -- almost as weak as the 'rural_poor' cluster despite not "
        "being economically poor, across regression models controlling for the listed "
        "covariates; 'big_wealthy_urban' districts show significantly better access to "
        "sanitation and electricity in all models, and to drinking water in two of the "
        "models, than other district types. Exact coefficients, CIs, and p-values are "
        "not recoverable from the extracted text (narrative-only result reporting in "
        "the source's own presentation of the clustering-regression models)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "sample_size": "All Ghanaian local government districts, 2021 secondary data",
    "direction": (
        "negative (weak local-governance quality, independent of economic poverty, "
        "associated with substantially reduced water/sanitation/electricity access)"
    ),
    "adjusted": (
        "adjusted (political-party alignment with national government, local "
        "government form [municipal/metropolitan/standard], expenditure per capita, "
        "local government age)"
    ),
    "evidence_status": "OBSERVED",
    "provenance_note": (
        "extraction_database.csv S348; source Andrews, Beynon & Baafi 2025, Local "
        "Government Studies 51(1):178-201. Added 2026-09-28 as part of a re-mining "
        "pass across the 187 quantitative-synthesis-eligible studies that had an "
        "extracted effect_estimate but no effect_sizes.csv row -- see "
        "06_outputs/supplementary/effect_sizes_remining_2026-09-28.md for the full "
        "audit. S348 was the only one of 4 regression-family candidates from that pass "
        "that genuinely met the same bar as this file's other 61 rows; the other 3 "
        "(S006, S696, S1025) had already been deliberately excluded with sound "
        "reasoning recorded in their own extraction_note, not newly evaluated here."
    ),
    "included_in_pooled_estimate": "FALSE",
    "exclusion_from_pooling_reason": (
        "ANALYSIS_PLAN.md S2 -- single study for this district-governance-cluster "
        "exposure-comparator; no other Family C study shares this operationalization "
        "(a governance-quality classification derived from clustering, rather than a "
        "directly measured institutional variable), so pooling is not yet possible or "
        "meaningful. No CI/p-value available to report even if a comparable study did "
        "exist, since the source itself reports these models narratively rather than "
        "in a coefficient table recoverable from this project's extraction."
    ),
}

assert set(new_row.keys()) == set(fieldnames), set(new_row.keys()) ^ set(fieldnames)

rows.append(new_row)
assert len(rows) == 62

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(PATH), suffix=".tmp")
with os.fdopen(fd, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp_path, PATH)

print("OK, effect_sizes.csv now has", len(rows), "rows")
