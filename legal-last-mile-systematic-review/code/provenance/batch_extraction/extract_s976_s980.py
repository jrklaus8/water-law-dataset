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

# S976 - R44B35D130A49 - Mwenge Kahinda, Taigbenu & Boroto 2007 - South Africa DRWH
r = blank_row(fieldnames)
r.update({
    "study_id": "S976",
    "citation": "Mwenge Kahinda J, Taigbenu AE, Boroto JR (2007). Domestic rainwater harvesting to improve water supply in rural South Africa. Physics and Chemistry of the Earth.",
    "doi": "10.1016/j.pce.2007.07.007",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "rural South Africa (national policy review with local case reference)",
    "legal_system": "common law",
    "urban_rural": "rural",
    "service_provider": "Department of Water Affairs and Forestry (DWAF) national government; households (self-supply via domestic rainwater harvesting)",
    "regulatory_model": "statutory water-use licensing under the National Water Act (Act No. 36 of 1998) and Water Services Act (Act No. 108 of 1997), with a government-funded Pilot Programme for financial assistance to poor households",
    "population": "rural households relying on domestic rainwater harvesting (DRWH) for domestic water supply",
    "sample_size": "national policy review, no primary household sample",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "fees": "TRUE",
    "discretion": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "TRUE",
    "study_design": "policy/legal analysis with national program review",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": "High: paper directly demonstrates a statutory ambiguity/illegality problem for a household water-access mechanism (DRWH), and documents a specific government financial-assistance program (DWAF Pilot Programme, ss. 61/62 National Water Act) targeting it.",
    "source_document": "Mwenge Kahinda, Taigbenu & Boroto 2007, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    "section": "Legal and institutional framework; DWAF Pilot Programme",
    "exact_location": "Sections on legal status of DRWH and the DWAF Pilot Programme for financial assistance",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: explicit legal-status ambiguity/illegality of domestic rainwater "
        "harvesting under South Africa's National Water Act (Act No. 36 of 1998) and Water Services Act (Act No. 108 of 1997) "
        "-- the paper states DRWH is illegal by strict application of the water legislation despite being a critical "
        "household-level water-access mechanism for rural, water-scarce areas -- combined with the DWAF Pilot Programme's "
        "government financial-assistance mechanism (sections 61/62 of the National Water Act) for poor households. "
        "NOT effect_sizes eligible: policy/legal review article, no regression-based estimate isolating a legal mechanism's "
        "effect on a water-access outcome. Extracted for record_id R44B35D130A49."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S977 - R4443C2EFEEE0 - Bolaane & Ikgopoleng 2011 - Botswana sanitation
r = blank_row(fieldnames)
r.update({
    "study_id": "S977",
    "citation": "Bolaane B, Ikgopoleng H (2011). Towards improved sanitation: Constraints and opportunities in accessing waterborne sewerage in major villages of Botswana. Habitat International.",
    "doi": "10.1016/j.habitatint.2011.01.001",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Botswana",
    "subnational_unit": "Ramotswa and Tlokweng major villages",
    "legal_system": "common law",
    "urban_rural": "urban/peri-urban (major villages)",
    "service_provider": "government (Major Village Infrastructure Programme, MVIP)",
    "regulatory_model": "cost-recovery-limited-to-operation-and-maintenance institutional design; capital connection cost borne by government, tariff/connection-fee structure set for households",
    "population": "households in Ramotswa and Tlokweng major villages, Botswana",
    "sample_size": "429 household questionnaires plus secondary sources",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "application_success": "TRUE",
    "extraction_sample_size": "429",
    "study_design": "cross-sectional mixed-methods household survey",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original empirical household survey directly linking the Major Village Infrastructure "
        "Programme's institutional cost-recovery design and household income/tariff willingness-to-pay to measured "
        "waterborne-sewerage connection uptake."),
    "source_document": "Bolaane & Ikgopoleng 2011, Habitat International (retrieved via Google Drive)",
    "section": "Results; household income and willingness-to-pay analysis",
    "exact_location": "Household survey results section, WTP tariff-scenario tables",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: empirical mixed-methods study (429 household questionnaires "
        "+ secondary sources, Ramotswa and Tlokweng) of the Major Village Infrastructure Programme's institutional design "
        "(government-funded capital cost, cost-recovery limited to O&M) and household income as the strongest barrier to "
        "waterborne-sewerage uptake -- only 23-39% of eligible households connected despite 7 years of availability, with "
        "detailed WTP tariff-scenario analysis. Strong Family C match (administrative/financial barriers/access inequality). "
        "NOT effect_sizes eligible: descriptive survey statistics and WTP scenarios, no regression-based estimate isolating "
        "a legal/institutional mechanism's effect. Extracted for record_id R4443C2EFEEE0."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S978 - R4288E0B980A6 - Osumanu, Zumayelleh & Kosoe 2021 - Ghana Upper West
r = blank_row(fieldnames)
r.update({
    "study_id": "S978",
    "citation": "Osumanu IK, Zumayelleh EA, Kosoe EA (2022). Sustainability of community-managed small town and rural water systems in northern Ghana: lessons from Upper West Region. Community Development Journal.",
    "doi": "10.1093/cdj/bsab015",
    "publication_year": "2022",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Upper West Region",
    "legal_system": "common law",
    "urban_rural": "rural/small town",
    "service_provider": "community-based management (Water and Sanitation Management Teams / WATSANs / Water Management Boards) under Ghana's National Community Water and Sanitation Programme",
    "regulatory_model": "decentralized community-management institutional structure (WSMTs/WATSANs/WMBs) under the National Community Water and Sanitation Programme",
    "population": "households in small towns and rural communities, Upper West Region, Ghana",
    "sample_size": "225 household questionnaires plus 15 in-depth interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_continuity": "TRUE",
    "extraction_sample_size": "225",
    "study_design": "cross-sectional mixed-methods case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original empirical mixed-methods study directly linking the introduction of the "
        "community-management institutional structure (WSMTs/WATSANs/WMBs) to a quantified before/after change in potable "
        "water access (38% to 97%), while also documenting institutional/governance failures (absent Water Management "
        "Board, tariff-setting failures) threatening sustainability."),
    "source_document": "Osumanu, Zumayelleh & Kosoe 2022, Community Development Journal (retrieved via Google Drive)",
    "section": "Findings; access and sustainability of community-managed systems",
    "exact_location": "Results section reporting pre/post community-management access statistics",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: empirical mixed-methods case study (225 household "
        "questionnaires + 15 in-depth interviews) of Ghana's National Community Water and Sanitation Programme "
        "institutional structure (WSMTs/WATSANs/WMBs); potable water access increased from 38% to 97% following "
        "introduction of community management, but functionality/sustainability challenges persist due to tariff-setting "
        "failures, an absent Water Management Board, and lack of continuing government support. Strong Family A/B match. "
        "NOT effect_sizes eligible: descriptive before/after case-study statistics, no regression-based estimate isolating "
        "the institutional mechanism's effect. Extracted for record_id R4288E0B980A6."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S979 - R45641CF1C6FA - El-Jazairi 2017 - Occupied Palestinian Territory
r = blank_row(fieldnames)
r.update({
    "study_id": "S979",
    "citation": "El-Jazairi L (2017). The occupied Palestinian territory: Challenges to progressive realisation. In: The Human Right to Water and Sanitation. Cambridge University Press.",
    "doi": "10.1017/9780511862601.014",
    "publication_year": "2017",
    "publication_type": "book chapter",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "occupied Palestinian territory (West Bank, Gaza Strip)",
    "subnational_unit": "Oslo II Areas A/B/C jurisdictional division",
    "legal_system": "mixed (Palestinian statutory law under belligerent occupation; public international law)",
    "urban_rural": "national",
    "service_provider": "Palestinian Water Authority (PWA), municipalities, Joint Service Councils; subject to Israeli occupation authority control over shared water resources",
    "regulatory_model": "Palestinian Water Law No. 3 (2002) human-right-to-water recognition, constrained by Oslo II jurisdictional fragmentation (Area C = full Israeli control, ~61% of West Bank) and belligerent-occupation law (Hague Regulations 1907, Fourth Geneva Convention 1949)",
    "population": "Palestinian population of the occupied Palestinian territory",
    "sample_size": "legal/documentary analysis, no primary household sample",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "legal/documentary analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: detailed legal analysis of Palestinian Water Law No. 3 (2002)'s explicit human-right-to-"
        "water provision (Art. 3(3)), Oslo II jurisdictional fragmentation (Areas A/B/C) constraining the Palestinian Water "
        "Authority's territorial control over water resources, and occupying-power obligations under the Hague Regulations "
        "and Fourth Geneva Convention that directly determine Palestinian access to water and sanitation."),
    "source_document": "El-Jazairi 2017, in Langford & Russell (eds), The Human Right to Water and Sanitation, Cambridge University Press (retrieved via Google Drive)",
    "section": "Sections 2-4: Palestinian legislative framework; obligations of an occupying power; impact of occupation on realisation of the right to water",
    "exact_location": "Throughout chapter, esp. Section 4.1 Inequitable Access to Water Resources: Occupation and Military Orders",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: legal analysis of the Palestinian Water Law No. 3 (2002), Oslo "
        "II jurisdictional fragmentation (Area C under full Israeli control constitutes ~61% of West Bank), and the "
        "obligations of an occupying power under the Hague Regulations of 1907 and Fourth Geneva Convention of 1949, "
        "showing how these legal/institutional mechanisms directly constrain the Palestinian Water Authority's ability to "
        "progressively realise the right to water and sanitation. Strong match to the constitutional/legal water-rights-"
        "reform comparative-case-study inclusion precedent (Diaz-Cayeros Mexico, Guidi Bolivia). NOT effect_sizes "
        "eligible: doctrinal legal analysis, no regression-based estimate. Extracted for record_id R45641CF1C6FA."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S980 - R45B892C461F4 - Cobbinah, Kosoe & Diawuo 2020 - Ghana toilet facilities
r = blank_row(fieldnames)
r.update({
    "study_id": "S980",
    "citation": "Cobbinah PB, Kosoe EA, Diawuo F (2020). Environmental planning crisis in urban Ghana: Local responses to nature's call. Science of the Total Environment.",
    "doi": "10.1016/j.scitotenv.2019.134898",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Wa municipality",
    "legal_system": "common law",
    "urban_rural": "urban",
    "service_provider": "urban planning/environmental sanitation regulatory regime (municipal)",
    "regulatory_model": "urban planning regime with limited monitoring systems, inadequate logistics and personnel for enforcement of household toilet-facility provision requirements",
    "population": "urban households in Wa municipality, Ghana",
    "sample_size": "household survey plus key informant interviews",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "building_permit": "TRUE",
    "discretion": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "effect_measure": "correlation coefficient",
    "effect_estimate": "0.750",
    "p_value": "0.001",
    "adjusted_or_unadjusted": "unadjusted",
    "model_type": "correlation/regression analysis",
    "study_design": "cross-sectional mixed-methods household survey",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original household survey and key informant interviews directly linking distortions "
        "in the urban planning regulatory regime (limited monitoring, inadequate logistics/personnel) alongside "
        "socio-economic and cultural factors to the absence of in-house household toilet facilities and residents' "
        "resort to communal facilities, open defecation, and 'perching'."),
    "source_document": "Cobbinah, Kosoe & Diawuo 2020, Science of the Total Environment (retrieved via Google Drive)",
    "section": "Abstract; Findings on institutional/urban-planning distortions",
    "exact_location": "Results section reporting regression analysis (r=0.750, df=13, p=0.001) between attitudes and toilet-facility benefits",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: empirical household survey and key-informant-interview study "
        "(Wa municipality, Ghana) explicitly analyzing institutional/urban-planning-regime distortions (limited monitoring "
        "systems, inadequate logistics and personnel) as one of three factor categories -- alongside socio-economic and "
        "cultural factors -- inhibiting household in-house toilet facility provision; residents resort to communal "
        "toilets, open defecation, and 'perching'. Strong Family C match. NOT effect_sizes eligible: the reported "
        "correlation (r=0.750, p=0.001) measures the relationship between attitudes and perceived benefits, not a "
        "regression-based estimate isolating the institutional/planning mechanism's effect on a water/sanitation-access "
        "outcome. Extracted for record_id R45B892C461F4."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
