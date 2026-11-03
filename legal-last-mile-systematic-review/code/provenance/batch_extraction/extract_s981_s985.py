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

# S981 - R420211B3E670 - Molinos-Senante 2018 - Chile urban water management
r = blank_row(fieldnames)
r.update({
    "study_id": "S981",
    "citation": "Molinos-Senante M (2018). Urban Water Management. Chapter 9 in Donoso G (ed), Water Policy in Chile, Global Issues in Water Policy 21. Springer.",
    "doi": "10.1007/978-3-319-76702-4_9",
    "publication_year": "2018",
    "publication_type": "book chapter",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Chile",
    "subnational_unit": "national, with regional tariff/company detail",
    "legal_system": "civil law",
    "urban_rural": "urban",
    "service_provider": "fully private companies (FPC) and concessionary companies (CC) under Superintendencia de Servicios Sanitarios (SISS) regulation",
    "regulatory_model": "Law 382 (General Law of Sanitation Services, 1988), Law 70 (General Law of Tariffs, 1988), hypothetical-efficient-company tariff-setting model administered by SISS; Law 18,778 (1989) direct subsidy for vulnerable households",
    "population": "urban water/sanitation customers in Chile, with focus on low-income/vulnerable households",
    "sample_size": "national policy/institutional review with company-level and national statistics",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "study_design": "policy/institutional review with national statistics",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: detailed legal/institutional analysis of Chile's tariff-setting law (Law 70) and "
        "targeted subsidy law (Law 18,778) directly tied to documented affordability outcomes for vulnerable households "
        "(14.8% of customers received subsidies in 2015, sliding-scale co-payment 15-85% of the water bill)."),
    "source_document": "Molinos-Senante 2018, in Donoso (ed), Water Policy in Chile, Springer (retrieved via Google Drive)",
    "section": "9.2 Legal and Institutional Framework; 9.4 Water and Sanitation Tariffs and Affordability",
    "exact_location": "Sections on Law 382/Law 70 tariff-setting and Law 18,778 subsidy system",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: legal/institutional review of Chile's water-sector "
        "privatization reforms (Law 382 General Law of Sanitation Services, Law 70 General Law of Tariffs, SISS "
        "regulator, hypothetical-efficient-company tariff model) and Law 18,778's targeted subsidy system for "
        "low-income households, with documented affordability outcomes (14.8% of customers subsidized in 2015). "
        "Strong Family A/C match, consistent with PSP/tariff-affordability inclusion precedent (Reynaud France, "
        "March & Sauri Barcelona). NOT effect_sizes eligible: descriptive institutional/policy review with national "
        "statistics, no regression-based estimate isolating a legal mechanism's effect. Extracted for record_id "
        "R420211B3E670."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S982 - R418BDADF8E47 - Dismas, Mulungu & Mtalo 2018 - Tanzania RWH
r = blank_row(fieldnames)
r.update({
    "study_id": "S982",
    "citation": "Dismas J, Mulungu DMM, Mtalo FW (2018). Advancing rainwater harvesting as a strategy to improve water access in Kinondoni municipality, Tanzania. Water Science & Technology: Water Supply.",
    "doi": "10.2166/ws.2018.007",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Kinondoni municipality, Dar es Salaam (Makongo, Mbezi, Msasani, Kimara wards)",
    "legal_system": "common law",
    "urban_rural": "urban/peri-urban",
    "service_provider": "household self-supply (domestic rainwater harvesting); Ministry of Water",
    "regulatory_model": "Tanzania Water Resources Management Act 2009 (water-permit exemption for domestic RWH), National Water Policy (2002), municipal building-permit bylaws mandating RWH inclusion for new construction",
    "population": "households in Kinondoni municipality with and without DAWASCO piped water access",
    "sample_size": "102 households (68 RWH adopters, 34 non-adopters), plus interviews with institutions/vendors",
    "household_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "building_permit": "TRUE",
    "documentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "extraction_sample_size": "102",
    "study_design": "cross-sectional mixed-methods household survey with water-quality laboratory testing",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: household survey directly linking the statutory water-permit exemption for domestic "
        "rainwater harvesting under the Tanzania Water Resources Management Act 2009 and municipal building-permit "
        "bylaws mandating RWH inclusion to household adoption patterns, with initial investment cost as the principal "
        "documented barrier."),
    "source_document": "Dismas, Mulungu & Mtalo 2018, Water Science & Technology: Water Supply (retrieved via Google Drive)",
    "section": "Opportunities for the development of RWH technologies: Government's legal framework on RWH",
    "exact_location": "Results section on legal framework and challenges for adoption",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: household survey (102 households, Kinondoni municipality, "
        "Dar es Salaam) examining rainwater-harvesting adoption under the Tanzania Water Resources Management Act "
        "2009's exemption from water permits for domestic RWH and municipal bylaws mandating RWH inclusion in new "
        "building permits; investment cost identified as the principal adoption barrier. Consistent with the South "
        "Africa DRWH inclusion precedent (R44B35D130A49/S976). NOT effect_sizes eligible: descriptive survey "
        "statistics, no regression-based estimate isolating the legal mechanism's effect. Extracted for record_id "
        "R418BDADF8E47."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S983 - R410CAF95F628 - Irshad 2013 - Kerala foreign-funding institutional weakening
r = blank_row(fieldnames)
r.update({
    "study_id": "S983",
    "citation": "Irshad SM (2013). Foreign funding-induced development, institutional weakening and access to water: a case study from Kerala, India. Water Policy.",
    "doi": "10.2166/wp.2012.203",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Kerala (92 villages, four districts, rural; Thiruvananthapuram and Kozhikode, urban)",
    "legal_system": "common law",
    "urban_rural": "rural and urban",
    "service_provider": "Kerala Water Authority (KWA), transitioning to Kerala Rural Water Supply and Sanitation Agency (KRWSA) community-based beneficiary groups",
    "regulatory_model": "World Bank/JBIC-funded institutional reform: shift from subsidized state-run KWA supply to demand-responsive-approach community ownership (KRWSA), 100% O&M cost recovery by beneficiary groups, removal of public taps",
    "population": "rural and urban households in Kerala, particularly those previously served or unserved by KWA",
    "sample_size": "field survey across 92 villages/four districts (rural), plus urban water-supply institutional data",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "study_design": "field survey with institutional/policy analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: field survey directly linking foreign-aid-conditioned institutional restructuring "
        "(World Bank/JBIC-funded shift from subsidized KWA provision to a cost-recovery community-ownership model, "
        "KRWSA) to quantified changes in household water access (49.3% of beneficiaries without prior sustainable "
        "access now 'getting water' through KRWSA) and tariff structure."),
    "source_document": "Irshad 2013, Water Policy (retrieved via Google Drive)",
    "section": "Implementation of reforms and the modus operandi of the rural scheme",
    "exact_location": "Table 1 (water sources before KRWSA), section 3.1",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: field-survey-based institutional analysis of World "
        "Bank/JBIC-funded reform of Kerala's water-supply governance (shift from subsidized KWA state provision to "
        "cost-recovery community-based KRWSA scheme), documenting removal of free public taps, new tariff structure, "
        "and quantified before/after household access change (49.3% of beneficiaries newly 'getting water' through "
        "KRWSA). Strong Family A/C match. NOT effect_sizes eligible: descriptive survey statistics, no regression-"
        "based estimate isolating the institutional mechanism's effect. Extracted for record_id R410CAF95F628."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S984 - R43C575771C91 - ElDidi & Corbera 2017 - Egypt charity wells
r = blank_row(fieldnames)
r.update({
    "study_id": "S984",
    "citation": "ElDidi H, Corbera E (2017). A Moral Economy of Water: Charity Wells in Egypt's Nile Delta. Development and Change.",
    "doi": "10.1111/dech.12286",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Egypt",
    "subnational_unit": "Shubra Qubala village, Monoufeya governorate, Nile Delta",
    "legal_system": "civil law with customary/religious (Islamic waqf) legal pluralism",
    "urban_rural": "rural",
    "service_provider": "charitable water wells (sobol) established by individuals/NGO; government canal-irrigation and municipal piped-water systems",
    "regulatory_model": "Egypt's 1984 Irrigation and Drainage Law (unspecified water-amount entitlement, no regulatory enforcement mechanism), property rights regimes (marwa access rights), Islamic waqf charitable-endowment institution, NGO institutional legitimacy for communal water-source land donation",
    "population": "farmers and households in Shubra Qubala village",
    "sample_size": "55 semi-structured interviews (25 farmers on irrigation wells, 30 residents at drinking-water filtration station)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "tenure_status": "TRUE",
    "property": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "extraction_sample_size": "55",
    "study_design": "qualitative case study with semi-structured interviews",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original qualitative fieldwork directly linking property-rights regimes and "
        "charitable-institution governance (sobol/waqf) -- and the 1984 Irrigation and Drainage Law's unenforceable "
        "legal right to irrigation water -- to differential household/farmer access to drinking and irrigation water, "
        "including documented remaining access discrepancies by physical proximity and institutional arrangement."),
    "source_document": "ElDidi & Corbera 2017, Development and Change (retrieved via Google Drive)",
    "section": "Sobol's Contribution to Water Provision; Limits to Reciprocity: Property Rights, Individualism and Collective Moral Actions",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: qualitative case study (55 interviews) of charitable water "
        "wells (sobol) as an institutional/property-rights mechanism reshaping water access in Egypt's Nile Delta, "
        "examining Egypt's 1984 Irrigation and Drainage Law's unenforceable legal right to irrigation water, "
        "property-rights regimes (marwa access), and NGO institutional legitimacy requirements for establishing "
        "communal drinking-water access, with documented remaining access inequities by proximity and institutional "
        "arrangement. Strong Family A/C match. NOT effect_sizes eligible: qualitative interview-based case study, no "
        "regression-based estimate. Extracted for record_id R43C575771C91."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S985 - R3DCC4CCBD760 - Matros-Goreses & Franceys 2008 - Namibia price-setting
r = blank_row(fieldnames)
r.update({
    "study_id": "S985",
    "citation": "Matros-Goreses A, Franceys R (2008). The price-setting process and a potential role for economic regulation in a water scarce developing country. Water Science & Technology: Water Supply.",
    "doi": "10.2166/ws.2008.081",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Namibia",
    "subnational_unit": "Windhoek",
    "legal_system": "common law",
    "urban_rural": "urban, including informal settlements",
    "service_provider": "NamWater (bulk water supplier); City of Windhoek local authority",
    "regulatory_model": "Ministry of Agriculture, Water and Forestry / Ministry of Local Government and Housing and Rural Development political tariff-approval process; Water Resources Management Act 2004 (provision for a Water Regulatory Board, not yet implemented); block-tariff system with cross-subsidization",
    "population": "domestic water users in Windhoek, with focus on urban poor/informal-settlement residents",
    "sample_size": "35 individuals representing 16 organizations (government, providers, domestic/non-domestic users, NGOs)",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "discretion": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "affordability": "TRUE",
    "extraction_sample_size": "35",
    "study_design": "exploratory/descriptive case study with semi-structured interviews and secondary data",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original interview-based study directly examining Namibia's politically-approved "
        "(non-independent) tariff price-setting process within its legal/institutional framework and the Water "
        "Resources Management Act 2004's not-yet-implemented Water Regulatory Board, documenting affordability "
        "outcomes for the urban poor (32% barely able to afford, 22% unable to afford communal water/sanitation "
        "facilities) and the lack of targeted subsidies."),
    "source_document": "Matros-Goreses & Franceys 2008, Water Science & Technology: Water Supply (retrieved via Google Drive)",
    "section": "Price-setting process; Affordability of services; Economic regulation in Namibia",
    "exact_location": "Table 1 (perceptions on economic regulator); affordability section",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: interview-based study (35 individuals, 16 organizations) "
        "of Namibia's water tariff price-setting process within its legal framework (Water Resources Management Act "
        "2004, proposed but unimplemented Water Regulatory Board), documenting a politically-driven, non-transparent "
        "tariff process and its affordability consequences for the urban poor (32% barely afford, 22% unable to "
        "afford communal facilities), with no subsidy scheme in place. Strong Family C match, consistent with PSP/"
        "tariff-affordability precedent. NOT effect_sizes eligible: qualitative/descriptive interview-based case "
        "study, no regression-based estimate. Extracted for record_id R3DCC4CCBD760."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
