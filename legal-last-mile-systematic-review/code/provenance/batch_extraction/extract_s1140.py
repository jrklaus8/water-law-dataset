#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def blank_row(fieldnames):
    return {fn: "" for fn in fieldnames}


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
new_rows = []

# S1140 -- Shrestha 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1140",
    "citation": "Shrestha MK (2013). Self-Organizing Network Capital and the Success of Collaborative Public Programs. Journal of Public Administration Research and Theory 23:307-329.",
    "doi": "10.1093/jopart/mus007",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nepal",
    "subnational_unit": "village communities applying to Rural Water Supply and Sanitation Program (RWSSP)",
    "legal_system": "civil law (Nepal); donor-funded collaborative government program",
    "urban_rural": "rural",
    "service_provider": "Rural Water Supply and Sanitation Program (RWSSP), NGO/government partner organizations",
    "regulatory_model": "competitive application-based infrastructure-fund allocation via self-organized partner networks",
    "population": "village communities applying for RWSSP water/sanitation project funding",
    "sample_size": "community-level network survey data, RWSSP applicant communities",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "Logistic regression, log odds (Hubert-White robust SEs, hierarchical clustering)",
    "effect_estimate": (
        "Number of organizational partners: log odds 0.55*** (SE 0.10); increasing "
        "partners from 1 (minimum) to 7 (mean) to 16 (maximum) raises predicted "
        "probability of RWSSP funding success from 0.02 to 0.38 to 0.99. Indirect "
        "reach (bridging access to other communities via partners): increasing from "
        "0 to 12 (mean) to 38 (maximum) raises funding-success probability from "
        "0.02 to 0.044 to 0.31. Subgroup cohesion among partners: increasing from "
        "0 (minimum) to 16 (average) to 100 (maximum) raises funding-success "
        "probability from 0.43 to 0.51 to 0.86. Remote community projects are "
        "significantly less likely to be funded; smaller projects and those "
        "generating greater time savings for beneficiaries are more likely to be "
        "funded. Full model correctly classifies 83% of cases and explains 43% of "
        "variation in funding success (vs. 24% for controls-only model)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.10 (number of partners); Hubert-White robust SEs throughout, clustered via UCINET hierarchical clustering (37 clusters)",
    "p_value": "*** p<0.001 (reported per coefficient in Table 3)",
    "extraction_sample_size": "RWSSP applicant communities, Nepal",
    "adjusted_or_unadjusted": "adjusted (controls for project size, remoteness, time savings, social inclusion, regional dummies)",
    "covariates": "project size, time savings, remoteness, social inclusion, region",
    "model_type": "logistic regression",
    "study_design": "quantitative regression-based institutional/administrative-mechanism study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: rigorous logistic-regression analysis with robust clustered standard "
        "errors directly isolating a network-capital/bureaucratic-assistance "
        "mechanism's effect on village communities' success in securing water/"
        "sanitation infrastructure program funding, with substantively large and "
        "statistically significant coefficients across all three network-capital "
        "measures."
    ),
    "source_document": "Shrestha 2013 (retrieved via Google Drive)",
    "page": "307-329",
    "table": "Table 3",
    "figure": "Figure 2",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based institutional/"
        "administrative-mechanism study directly isolating network-capital/"
        "bureaucratic-assistance effects on differential access to water/sanitation "
        "infrastructure funding. Added to effect_sizes.csv as Family B "
        "(administrative assistance/access)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
