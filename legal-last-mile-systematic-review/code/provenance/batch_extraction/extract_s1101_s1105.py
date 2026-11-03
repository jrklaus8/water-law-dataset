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

# S1101 -- Debbane & Keil 2004
r = blank_row(fieldnames)
r.update({
    "study_id": "S1101",
    "citation": "Debbane AM, Keil R (2004). Multiple Disconnections: Environmental Justice and Urban Water in Canada and South Africa. Space and Polity 8(2):209-225.",
    "doi": "10.1080/1356257042000273968",
    "publication_year": "2004",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa; Canada",
    "subnational_unit": "Zwelihle/Hermanus, Western Cape; Toronto",
    "legal_system": "common law (South Africa, Canada)",
    "urban_rural": "urban",
    "service_provider": "Hermanus Municipality (Overstrand)",
    "regulatory_model": "Greater Hermanus Water Conservation Programme (GHWCP) tiered tariff/indigent-subsidy structure",
    "population": "Zwelihle township residents, Hermanus, South Africa",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "GHWCP tariff structure achieved 30% reduction in water demand and 20% revenue surplus in first 3 years. During the same period, about 60% of Zwelihle residents (majority income-qualified for indigent tariffs but 'have not had access to this subsidy') were affected by water cut-offs due to non-payment/accruing arrears.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "comparative case study",
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
        "High: documents that the Greater Hermanus Water Conservation Programme's tiered "
        "tariff structure includes a lower 'indigent' rate for which the majority of "
        "Zwelihle township residents qualify by income, yet these residents 'have not "
        "had access to this subsidy'; combined with strict credit-control enforcement, "
        "this produced water cut-offs affecting approximately 60% of Zwelihle residents "
        "due to accruing arrears, even as the tariff programme generated a 20% revenue "
        "surplus for the municipality during peak holiday season."
    ),
    "source_document": "Debbane & Keil 2004 (retrieved via Google Drive)",
    "page": "209-225",
    "table": "",
    "figure": "",
    "section": "Environmental justice and water reform in Hermanus",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal mechanism case "
        "study directly documenting a tariff/credit-control mechanism producing "
        "differential water-service disconnection outcomes. No regression-based effect "
        "size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1102 -- Prokopy 2009
r = blank_row(fieldnames)
r.update({
    "study_id": "S1102",
    "citation": "Prokopy LS (2009). Determinants and Benefits of Household Level Participation in Rural Drinking Water Projects in India. Journal of Development Studies 45(4):471-497.",
    "doi": "",
    "publication_year": "2009",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "45 villages (Uttar Pradesh Hills, North Karnataka, South Karnataka)",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "community-based water user groups/committees",
    "regulatory_model": "community-based rural drinking-water project management",
    "population": "rural households, 45 villages, India",
    "sample_size": "households in 45 villages",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "propensity-score-matched treatment-control difference (t-statistic)",
    "effect_estimate": "Capital cost contribution -> water improvements index: treatment 0.364, control -0.676, difference 1.04 (t=4.26). Capital cost contribution -> satisfaction: treatment 0.813, control 0.458, difference 0.355 (t=8.54). Meeting attendance -> water improvements index: treatment 0.497, control -0.252, difference 0.749 (t=3.46). Meeting attendance -> satisfaction: treatment 0.790, control 0.685, difference 0.105 (t=4.16). Water improvements index composed of change in distance to source, collection time, reliability, quality, pressure, adequacy, and perceived access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "significant at t>2 threshold for pooled ('All') estimates",
    "extraction_sample_size": "45 villages, household-level data",
    "adjusted_or_unadjusted": "adjusted (propensity score matching)",
    "covariates": "wealth, literacy, household size, village size",
    "model_type": "propensity score matching (quasi-experimental)",
    "study_design": "quantitative quasi-experimental study",
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
        "High: using propensity score matching to address self-selection into "
        "participation, finds that both capital-cost contribution and meeting attendance "
        "(institutional/administrative participation mechanisms in community-based water "
        "project governance) are significantly associated with improvements in a "
        "composite water-access index (distance, collection time, reliability, quality, "
        "pressure, adequacy, perceived access) and with household satisfaction, with no "
        "evidence of elite capture -- both poor and wealthy households benefit "
        "significantly."
    ),
    "source_document": "Prokopy 2009 (retrieved via Google Drive)",
    "page": "471-497",
    "table": "Table 4",
    "figure": "Figures 2-3",
    "section": "Benefits of participation: propensity score matching results",
    "exact_location": "Table 4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous quasi-experimental study directly "
        "isolating a participatory/administrative institutional mechanism's causal effect "
        "on a composite water-access outcome. ADDED to effect_sizes.csv (Family B: "
        "administrative-assistance/participation mechanism directly isolated via "
        "propensity-score matching with a significant effect on a water-access outcome "
        "index)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1103 -- Wu & Malaluan 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1103",
    "citation": "Wu X, Malaluan NA (2008). A Tale of Two Concessionaires: A Natural Experiment of Water Privatisation in Metro Manila. Urban Studies 45(1):207-229.",
    "doi": "",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Philippines",
    "subnational_unit": "Metro Manila (East Zone: Manila Water; West Zone: Maynilad)",
    "legal_system": "civil law (Philippines)",
    "urban_rural": "urban",
    "service_provider": "Manila Water Company, Inc.; Maynilad Water Services, Inc.",
    "regulatory_model": "1997 MWSS 25-year concession contracts; MWSS Regulatory Office",
    "population": "low-income communities, Metro Manila",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "comparative before/after descriptive statistics (natural experiment)",
    "effect_estimate": "Connections increased 30% across both concessions in first 5 years post-privatization (vs. ~30 years at MWSS's historical rate), with much of the expansion in economically distressed areas. Manila Water's NRW fell from 58% to 35% (East Zone, territory-management model); Maynilad's NRW rose from 64% to 69% (West Zone, system-wide approach). Manila Water's Tubig Para sa Barangay programme served ~850,000 people in poor communities by 2005 via shared/bulk connections.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "natural experiment (identical external contract/regulatory conditions)",
    "study_design": "comparative natural-experiment case study",
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
        "High: leveraging a natural experiment (two concessionaires under identical "
        "concession-contract terms and the same regulatory office), documents that "
        "internal corporate-governance and management-model differences -- Manila Water's "
        "decentralized territory-management structure vs. Maynilad's centralized system-"
        "wide approach -- produced markedly different non-revenue-water outcomes and that "
        "each concessionaire's 'Water for the Community' programme (shared/bulk "
        "connections, waived land-title requirements, installment-based connection fees) "
        "expanded formal water access substantially faster than the pre-privatization "
        "public utility, concentrated in economically distressed areas."
    ),
    "source_document": "Wu & Malaluan 2008 (retrieved via Google Drive)",
    "page": "207-229",
    "table": "Table 1",
    "figure": "Figures 2-5",
    "section": "Effects of privatization on service coverage and the poor",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous natural-experiment institutional-"
        "arrangement study directly documenting differential water-access-expansion "
        "outcomes for the poor attributable to corporate-governance/management-model "
        "differences. NOT added to effect_sizes.csv: comparative before/after descriptive "
        "statistics between two cases, not a regression-based estimate isolating a single "
        "mechanism's effect with a formal statistical test."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1104 -- Franceys & Weitz 2003
r = blank_row(fieldnames)
r.update({
    "study_id": "S1104",
    "citation": "Franceys R, Weitz A (2003). Public-Private Community Partnerships in Infrastructure for the Poor. Journal of International Development 15(8):1083-1098.",
    "doi": "10.1002/jid.1052",
    "publication_year": "2003",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (10 Asian countries)",
    "subnational_unit": "20 case-study communities across 10 Asian countries",
    "legal_system": "mixed (Asia)",
    "urban_rural": "urban",
    "service_provider": "public utilities, private operators, NGOs, community organizations",
    "regulatory_model": "public-private-community partnership institutional arrangements",
    "population": "urban poor, informal settlements, 10 Asian countries",
    "sample_size": "20 case studies; focus group discussions with low-income slum residents",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
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
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "Maynilad's Bayan Tubig programme waives land-title requirements and allows connection fees paid over 6-24 monthly installments. Palyja (Jakarta) charges $0.71/month over 12 installments for connection fees, reducing effective water cost from $2.50/m3 (vended) to ~$1.50/month for 20m3 consumption. Group-tap schemes in Manila serve 2-5 households sharing one 'mother meter.'",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "20 case studies",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "multi-country comparative case-study analysis",
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
        "High: across 20 case studies in 10 Asian countries, documents specific formal "
        "eligibility and fee-structure mechanisms enabling or constraining water/"
        "sanitation access for the urban poor, including waiver of land-title "
        "requirements for connections (a common barrier given that most poor residents "
        "lack security of tenure), installment-based connection-fee payment plans "
        "replacing large upfront costs, and group-tap/shared-connection schemes with "
        "formal registration requirements."
    ),
    "source_document": "Franceys & Weitz 2003 (retrieved via Google Drive)",
    "page": "1083-1098",
    "table": "",
    "figure": "Figure 1",
    "section": "Case study findings",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous multi-country comparative case-"
        "study analysis directly documenting formal eligibility, fee-structure and "
        "connection-requirement mechanisms shaping water/sanitation access for the urban "
        "poor. No regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1105 -- Trepied 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1105",
    "citation": "Trepied B (2012). Indigenous struggles and water policies in contemporary New Caledonia. Social Identities 18(4):465-479.",
    "doi": "10.1080/13504630.2012.673876",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "New Caledonia (France)",
    "subnational_unit": "Commune of Kone",
    "legal_system": "civil law (France/New Caledonia) with customary Kanak law",
    "urban_rural": "rural",
    "service_provider": "Municipality Council of Kone",
    "regulatory_model": "Adduction d'eau potable (AEP) Grombaou water-conveyance project",
    "population": "Kanak tribes of Neami, Noeli, Tiaoue, Poindah",
    "sample_size": "",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "ethnographic case study",
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
        "Moderate: documents that the AEP Grombaou water-conveyance pipeline, sourced "
        "from the territory of the Kanak tribe of Neami, was planned by the municipal "
        "council to bypass Neami and serve the tribes of Noeli, Tiaoue and Poindah first "
        "(justified by their more urgent drought-driven need), deferring Neami's own "
        "connection to a later project phase; this sequencing decision triggered a formal "
        "protest letter and threatened work-site obstruction by Neami's customary Council "
        "of Elders, resolved through negotiation with the mayor in July 2004."
    ),
    "source_document": "Trepied 2012 (retrieved via Google Drive)",
    "page": "465-479",
    "table": "",
    "figure": "",
    "section": "Water policies and customary claims in the commune of Kone",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/political case study "
        "documenting how municipal water-infrastructure sequencing decisions, contested "
        "through customary Indigenous governance structures, determine which communities "
        "receive water-service connections and in what order. Ethnographic case study, no "
        "regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
