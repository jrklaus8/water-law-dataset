import csv, tempfile, os

path = "03_extraction/extracted_data/extraction_database.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

def blank_row():
    return {k: "" for k in fieldnames}

row = blank_row()
row.update({
    "study_id": "S550",
    "citation": 'Nastar M, Abbas S, Aponte Rivero C, Jenkins S, Kooy M (2018). "The emancipatory promise of participatory water governance for the urban poor: Reflections on the transition management approach in the cities of Dodowa, Ghana and Arusha, Tanzania." African Studies, 77(4), 504-525.',
    "doi": "10.1080/00020184.2018.1459287",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana; Tanzania",
    "subnational_unit": "Dodowa (Shai-Osudoku District, Greater Accra Region), Ghana; Arusha, Tanzania",
    "legal_system": "common law",
    "urban_rural": "peri-urban/urban (low-income informal and unplanned settlements)",
    "service_provider": "Ghana Water Company Limited (GWCL, urban piped supply), Community Water and Sanitation Agency (CWSA, rural/small-town coordination), District Assembly (DA)-supported WATSAN committees, and traditional community leaders (Dodowa); Arusha Urban Water Supply and Sewerage Authority (AUWSA), Pangani Basin Water Board (PBWB), Arusha City Council (ACC), and informal Balozi/street-chair structures (Arusha)",
    "regulatory_model": "In Ghana, the Community Water and Sanitation Agency Act assigns CWSA responsibility for coordinating participatory rural/small-town water management and supporting District Assembly-established WATSAN committees that manage groundwater boreholes, while GWCL holds the statutory urban piped-supply mandate; new tank connections require a GWCL site inspection and application process. In Tanzania, the Water Resource Management Act assigns the Pangani Basin Water Board regulatory authority over groundwater drilling/permitting, but a lack of monitoring budget has left a growing number of boreholes unregistered; the Arusha City Council's land-permitting authority for the expanding urban periphery has been used to issue permits in designated groundwater recharge areas, a practice a National Environment Management Council official confirmed is illegal under the Water Resource Management Act.",
    "population": "Households in low-income and informal peri-urban/urban settlements of Dodowa, Ghana (9 suburbs) and Arusha, Tanzania (6 wards)",
    "sample_size": "104 household interviews in Dodowa (42 in Dec 2015, 72 in Feb/Mar 2016); 56 household interviews plus 120 unstructured interviews at 70 water points in Arusha (Nov 2015-Jan 2016); plus document analysis and interviews with government/NGO organizational actors",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "TRUE",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "TRUE",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
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
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "Qualitative thematic analysis (coded interview data) of 104 Dodowa household interviews, 56 Arusha household interviews, and 120 Arusha water-point interviews, triangulated with document analysis; no statistical contrast",
    "effect_estimate": "In Dodowa, over half of residents rely on GWCL piped water delivered via household connections or nearby water tanks requiring an application/inspection process and connection fee; residents without their own connection buy water from tank owners at roughly 10 times the per-unit GWCL tariff (approx. 3.5 pesewas/20L for connection owners vs. 30-70 pesewas/20L from tank resellers), with no price monitoring by GWCL. Of nine studied suburbs, only three had an established WATSAN committee to manage boreholes, and even there many households were unaware of the committee's existence or membership; renters and non-native residents (e.g. the respondent Afua) reported feeling they had no standing to raise complaints about water governance because they did not own land. In Arusha, AUWSA's piped network serves only 44% of the population and is concentrated in the city centre; the Pangani Basin Water Board lacks the operational budget to identify or monitor a growing number of unregistered boreholes, and the Arusha City Council has issued land permits for development in designated groundwater recharge areas, confirmed by a National Environment Management Council official to be illegal under the Water Resource Management Act. Both cities show household-level access to water and to community water governance shaped by informal social hierarchies -- traditional chiefs/elder committees/royal families and Balozi/street chairs/landlords -- with tenure status, kinship ties, and land ownership determining who is heard and who is structurally excluded from decision-making and resource access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "160",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "mixed-methods case study (document analysis, semi-structured/open-ended household interviews, water-point ethnographic interviews) across two cities",
    "study_design": "mixed-methods comparative case study of power dynamics in participatory groundwater governance for the urban poor in Dodowa, Ghana and Arusha, Tanzania, based on document analysis and 104+56 household interviews plus 120 water-point interviews",
    "risk_of_bias_tool": "MMAT (Mixed Methods Appraisal Tool)",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "",
    "outcome_measurement_quality": "",
    "mechanism_certainty": "2",
    "source_document": "Nastar, Abbas, Aponte Rivero, Jenkins & Kooy 2018, African Studies 77(4):504-525",
    "page": "",
    "table": "Tables 2, 3, 4",
    "figure": "",
    "section": "Composition of actors and resources in relation to groundwater access; The power dynamics in the process of groundwater management (Findings from Dodowa; Findings from Arusha)",
    "exact_location": "Tables 2-4 (organizational and community actors and their controlled resources); sections on findings from Dodowa and Arusha documenting connection costs, WATSAN committee non-transparency, illegal ACC land permits in groundwater recharge areas, and tenure/kinship-based exclusion from water governance",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents genuine legal-administrative access mechanisms across two countries: Ghana's CWSA Act/WATSAN committee structure and GWCL connection process with a 10x informal-resale price markup; Tanzania's Water Resource Management Act regulatory framework undermined by an unfunded Pangani Basin Water Board and Arusha City Council land permits issued illegally in groundwater recharge areas; and household-level exclusion from community water governance tied to tenure status, kinship, and land ownership in both cities. record_id R9BAE8BE9ADB8.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-21",
    "evidence_status": "OBSERVED",
})
rows.append(row)

fd, tmp = tempfile.mkstemp(dir="03_extraction/extracted_data")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, path)

print("done, extraction rows now", len(rows))
