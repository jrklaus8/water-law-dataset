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

# S1141 -- Victor 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1141",
    "citation": "Victor H (2019). \"There is life in this place\": \"DIY formalisation,\" buoyant life and citizenship in Marikana informal settlement, Potchefstroom, South Africa. Anthropology Southern Africa 42(4):302-315.",
    "doi": "10.1080/23323256.2019.1639522",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Marikana informal settlement, Potchefstroom, North West province",
    "legal_system": "mixed (Roman-Dutch/common law); post-apartheid municipal service-delivery framework",
    "urban_rural": "urban",
    "service_provider": "Tlokwe municipality (local government), self-organized residential committee",
    "regulatory_model": "formal-settlement/informal-settlement legal status as a precondition for municipal service extension",
    "population": "residents of Marikana informal settlement, an unrecognized/undeclared informal settlement",
    "sample_size": "ethnographic fieldwork, residential committee census (~internal count), key informant interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "informal/unrecognized occupation; residents self-formalized via NPO registration",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "qualitative/ethnographic (no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative case study: Marikana's shack settlement was administratively labeled "
        "'too informal' to receive basic municipal service provision (piped water, "
        "electricity). Residents undertook self-organized 'DIY formalisation' -- laying out "
        "stands and streets, installing their own water infrastructure, and registering their "
        "residential committee as an NPO ('The Voice of the People') -- as a 'politics of "
        "legibility' strategy to politically appeal to the city council for recognition and "
        "formal service extension. The study documents that formal/informal legal-"
        "administrative status functions directly as the eligibility gate for municipal water "
        "service, and that residents' path to service access required performing legibility "
        "and organizational formality to the local government, rather than merely physical "
        "proximity to infrastructure."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "ethnographic fieldwork, Marikana informal settlement",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "ethnographic case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "High: detailed ethnographic documentation of a legal/administrative informality-"
        "status mechanism directly gating municipal water-service eligibility, and of "
        "residents' self-organized formalization strategy used to overcome it."
    ),
    "source_document": "Victor 2019 (retrieved via Google Drive)",
    "page": "302-315",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional access-mechanism "
        "case study (informal-settlement legal status as a service-eligibility gate, and a "
        "self-organized legibility/formalization strategy to overcome it). Qualitative only; "
        "no effect_sizes.csv entry (no defined comparator or effect estimate)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1142 -- Smith & Hanson 2003
r = blank_row(fieldnames)
r.update({
    "study_id": "S1142",
    "citation": "Smith L, Hanson S (2003). Access to Water for the Urban Poor in Cape Town: Where Equity Meets Cost Recovery. Urban Studies 40(8):1517-1548.",
    "doi": "10.1080/0042098032000094414",
    "publication_year": "2003",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Cape Town, townships",
    "legal_system": "mixed (Roman-Dutch/common law); post-apartheid municipal service-delivery framework",
    "urban_rural": "urban",
    "service_provider": "Cape Town local municipal government (post-1997 restructuring)",
    "regulatory_model": "cost-recovery/commercialisation model: underinvestment in low-income infrastructure plus disconnection for non-payment",
    "population": "low-income township residents, Cape Town, 1997-2001",
    "sample_size": "five-year (1997-2001) policy case study; 160,000 water cutoffs documented over 3 years",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
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
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "policy case-study analysis (no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative/descriptive policy case study of Cape Town's five-year (1997-2001) "
        "water-sector commercialisation process, focused on two cost-recovery policies: "
        "chronic underinvestment in township water infrastructure and disconnection for "
        "non-payment (160,000 water cutoffs documented over the 3-year study period). Finds "
        "that historically apartheid-produced territorial service inequities are being "
        "recreated through contemporary 'basic needs' cost-recovery approaches, and that "
        "historically entrenched service debts drive continuing disconnections among "
        "low-income township residents. Documents both distributive inequity (infrastructure "
        "underinvestment by area) and procedural inequity (disconnection policy application) "
        "as institutional mechanisms directly producing differential water access/continuity "
        "for the urban poor."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "Cape Town townships, 1997-2001, 160,000 water cutoffs documented",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "policy case-study analysis",
    "study_design": "qualitative/descriptive institutional/legal-mechanism case study",
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
        "High: detailed policy case-study documentation of a cost-recovery/disconnection "
        "institutional mechanism directly producing differential water access/continuity for "
        "low-income township residents in post-apartheid Cape Town, with a concrete "
        "descriptive outcome measure (160,000 cutoffs in 3 years)."
    ),
    "source_document": "Smith & Hanson 2003 (retrieved via Google Drive)",
    "page": "1517-1548",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional access-mechanism "
        "case study (cost-recovery and disconnection policy directly producing differential "
        "water access). Descriptive cutoff count (160,000/3 years) is a count, not a "
        "regression-based effect estimate isolating the mechanism against a defined "
        "comparator; no effect_sizes.csv entry."
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
