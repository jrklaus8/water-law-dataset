#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"


def blank_row(fieldnames):
    return {k: "" for k in fieldnames}


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

new_rows = []

# S1012 -- Ruiz Rosado 2008, Trujillo, Peru
r = blank_row(fieldnames)
r.update({
    "study_id": "S1012",
    "citation": "Ruiz Rosado LE (2008). Urbanization, Migration and Water Management in Trujillo, Peru.",
    "doi": "",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Peru",
    "subnational_unit": "Bellavista, Trujillo",
    "legal_system": "civil law (Peru)",
    "urban_rural": "urban peri-urban settlement",
    "service_provider": "SEDALIB (municipal water enterprise); Comite de Agua neighborhood water committee",
    "regulatory_model": "SEDALIB institutional water-rationing policy (scheduled intermittent supply); community-committee-mediated formal-connection process",
    "population": "residents of Bellavista, Trujillo, with and without formal piped-network connections",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "TRUE",
    "refusal": "",
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
    "study_design": "case study with household survey and community-institutional documentation of a municipal water enterprise's rationing policy",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": "High: SEDALIB's explicit institutional rationing policy (piped supply limited to three days/week, two hours/day) and the Comite de Agua community committee's mediating role in accelerating or delaying formal network connections are documented as directly producing measured price disparities for households lacking adequate access -- up to 16.6x the network tariff via tricycle vendors and 5-8x via official retail resale -- with only 17% of Bellavista households achieving 'optimal access' status.",
    "source_document": "Ruiz Rosado 2008 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout, esp. water supply/rationing and price-disparity discussion",
    "exact_location": "Throughout results/discussion sections",
    "extraction_note": "INCLUDE per INCLUSION_EXCLUSION.md: municipal water enterprise's institutional rationing policy plus community-committee gatekeeping of formal connections directly and measurably produce differential water-access and price outcomes. Extends the institutional-rationing/informal-market-price-disparity precedent (Matsinhe et al Maputo, S1005) and community-committee-gatekeeping precedent. No regression-based effect size isolating the mechanism's marginal effect is reported; not added to effect_sizes.csv per the strict Family A/B/C framework.",
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1013 -- Ratner & Rivera Gutierrez 2004, Panajachel, Guatemala
r = blank_row(fieldnames)
r.update({
    "study_id": "S1013",
    "citation": "Ratner BD, Rivera Gutierrez A (2004). Reasserting Community: The Social Challenge of Wastewater Management in Panajachel, Guatemala. Human Organization 63(1):47-56.",
    "doi": "",
    "publication_year": "2004",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Guatemala",
    "subnational_unit": "Panajachel, Lake Atitlan basin, Solola",
    "legal_system": "civil law (Guatemala)",
    "urban_rural": "small multiethnic town",
    "service_provider": "municipal government (Jucanya wastewater treatment plant); traditional Mayan alcaldia/cofradia institutions (historical); neighborhood alley committees",
    "regulatory_model": "municipal connection-eligibility rules (legal property ownership + tax-currency requirement, later relaxed to water/trash-bill currency + connection fee); differentiated fee schedule negotiated via multi-stakeholder dialogue; alley-committee collective-connection agreements",
    "population": "households and businesses in Panajachel eligible for sewage-system connection",
    "sample_size": "~1,400 households recorded by municipal government; qualitative interviews and stakeholder-dialogue forum",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
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
    "study_design": "action-research case study using interviews, participant observation, stakeholder-dialogue forum, and documentary/financial analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": "High: initial municipal connection rules requiring proof of legal property ownership and current tax-payment status are documented as discouraging household connection to the new wastewater system; relaxation of these rules to require only water/trash-bill currency plus a Q75 fee, a differentiated stakeholder-negotiated fee schedule, and neighborhood alley-committee collective-connection agreements are documented as directly producing measured connection-rate increases (550 of ~1,400 households connected by April 2001; +185 households via alley-committee agreements by March 2002).",
    "source_document": "Ratner & Rivera Gutierrez 2004, Human Organization (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Social History of the Jucanya Wastewater Treatment Plant; Reasserting Community",
    "exact_location": "Throughout results/discussion sections",
    "extraction_note": "INCLUDE per INCLUSION_EXCLUSION.md: documented legal/institutional eligibility-documentation requirement for service connection, a negotiated differentiated fee structure, and a community-committee-mediated collective-connection mechanism, all tied to directly measured connection-rate outcomes. Extends the institutional-eligibility-documentation-requirement and community-committee-mediated-connection precedents (Ruiz Rosado S1012, this batch). No regression-based effect size isolating the mechanism's marginal effect is reported; not added to effect_sizes.csv per the strict Family A/B/C framework.",
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
