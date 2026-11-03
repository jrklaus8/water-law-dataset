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

# S989 - R375DC07A5C67 - Gimelli, Rogers & Bos 2018 - India informal settlements
r = blank_row(fieldnames)
r.update({
    "study_id": "S989",
    "citation": "Gimelli FM, Rogers BC, Bos JJ (2018). The Quest for Water, Rights and Freedoms: Informal Urban Settlements in India. International Journal of Urban and Regional Research.",
    "doi": "10.1111/1468-2427.12708",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Faridabad, Delhi and Mumbai (six informal settlements)",
    "legal_system": "common law",
    "urban_rural": "urban informal settlements",
    "service_provider": "state/municipal water providers (Municipal Corporation of Greater Mumbai), water tankers, standpipes",
    "regulatory_model": "Maharashtra Slum Areas (Improvement, Clearance and Redevelopment) Act 1971; MCGM pre-2000-residency documentation eligibility cutoff; notified vs. non-notified settlement status",
    "population": "residents of non-notified (unauthorized) informal urban settlements",
    "sample_size": "44 in-depth interviews (24 men, 20 women) over 8 months",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "tenure_status": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "judicial_review": "TRUE",
    "participation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "extraction_sample_size": "44",
    "study_design": "qualitative embedded case study with narrative analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original qualitative case study directly linking notified/non-notified legal status "
        "under the Maharashtra Slum Areas Act 1971 and MCGM's pre-2000 documentation eligibility cutoff, as well as a "
        "Public Interest Litigation case in the Bombay High Court asserting an Article 21 constitutional right-to-"
        "water claim, to differential household water-service access for informal settlers."),
    "source_document": "Gimelli, Rogers & Bos 2018, International Journal of Urban and Regional Research (retrieved via Google Drive)",
    "section": "Interpreting the voices of informal settlers and development workers",
    "exact_location": "Settlers have a right to the city, its resources and its water",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: qualitative case study (44 interviews, three Indian "
        "megacities) examining legal notification status (Maharashtra Slum Areas Act 1971, MCGM documentation "
        "eligibility cutoff) and constitutional/judicial mechanisms (Bombay High Court PIL, Article 21 right-to-life "
        "claim) as determinants of differential water access for informal settlers. Strong Family A/C match, closely "
        "matches the environmental-justice/institutional-exclusion inclusion precedent. NOT effect_sizes eligible: "
        "qualitative narrative case study, no regression-based estimate. Extracted for record_id R375DC07A5C67."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S990 - R375CB03774D9 - Giglioli & Swyngedouw 2008 - Sicily water crisis
r = blank_row(fieldnames)
r.update({
    "study_id": "S990",
    "citation": "Giglioli I, Swyngedouw E (2008). Let's Drink to the Great Thirst! Water and the Politics of Fractured Techno-natures in Sicily. International Journal of Urban and Regional Research.",
    "doi": "10.1111/j.1468-2427.2008.00789.x",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Italy",
    "subnational_unit": "Sicily (Palermo)",
    "legal_system": "civil law",
    "urban_rural": "urban and rural",
    "service_provider": "regional/municipal water agencies (Ente Acquedotti Siciliani, Palermo Municipal Aqueduct), Commissario for hydraulic emergencies",
    "regulatory_model": "national structural water-sector reform of the early 2000s; Commissario appointment mechanism for hydraulic emergencies; public-works tendering regulations captured by Mafia-linked contracting networks",
    "population": "households in Palermo and other Sicilian municipalities, disproportionately poorer neighborhoods",
    "sample_size": "content analysis of two newspapers, official/judicial documents, parliamentary transcripts, and in-depth interviews with key figures",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "enforcement": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_reliability": "TRUE",
    "service_continuity": "TRUE",
    "study_design": "historical/political-economy case study with document analysis and key-informant interviews",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original documentary and interview-based analysis directly linking Mafia-linked "
        "institutional capture of public-works contracting, regional/national government dysfunction (the "
        "Commissario mechanism), and unfinished hydraulic infrastructure to a documented, quantified household "
        "water-supply-interruption disparity (national average 6.6 days/year vs. 36.1 days/year in the south), "
        "disproportionately affecting the poorest neighborhoods during the 2002 crisis."),
    "source_document": "Giglioli & Swyngedouw 2008, International Journal of Urban and Regional Research (retrieved via Google Drive)",
    "section": "Prolegomena to a techno-natural crisis; Chronicle of a drought foretold",
    "exact_location": "Interruption-days statistic and neighborhood-level mobilization mapping (Figure 1)",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: historical/political-economy case study of institutional "
        "capture (Mafia-linked public-works contracting, dysfunctional Commissario oversight mechanism) directly "
        "causing documented water-supply-interruption disparities (6.6 vs. 36.1 days/year) disproportionately "
        "affecting poor neighborhoods during Sicily's 2002 water crisis. Similar to the Detroit water crisis/"
        "institutional-capture inclusion precedent. NOT effect_sizes eligible: qualitative documentary/interview "
        "case study, no regression-based estimate. Extracted for record_id R375CB03774D9."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S991 - R355ECFDBF14D - Nelson et al 2021 - Fiji water committees
r = blank_row(fieldnames)
r.update({
    "study_id": "S991",
    "citation": "Nelson S, Abimbola S, Mangubhai S, Jenkins A, Jupiter S, Naivalu K, Naivalulevu V, Negin J (2022). Understanding the decision-making structures, roles and actions of village-level water committees in Fiji. International Journal of Water Resources Development.",
    "doi": "10.1080/07900627.2021.1916449",
    "publication_year": "2022",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Fiji",
    "subnational_unit": "Tailevu and Namosi provinces (six iTaukei villages)",
    "legal_system": "common law with customary institutions",
    "urban_rural": "rural",
    "service_provider": "village-level water committees under the Water Authority of Fiji (WAF), a statutory body",
    "regulatory_model": "WAF Rural Water Scheme requiring evidence of a functioning water committee; village governance structure (chief, Turaga ni koro, monthly village meetings, district meetings)",
    "population": "residents of six iTaukei villages",
    "sample_size": "40 key informant interviews/focus group discussions",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "eligibility": "TRUE",
    "discretion_accommodation": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "extraction_sample_size": "40",
    "study_design": "qualitative case study with semi-structured interviews and focus groups",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original qualitative study directly examining the decision-making structures, "
        "gendered membership patterns, and accountability mechanisms of statutorily-mandated village water "
        "committees under Fiji's Water Authority framework, and how these institutional/governance factors shape "
        "water access and security management."),
    "source_document": "Nelson et al 2022, International Journal of Water Resources Development (retrieved via Google Drive)",
    "section": "Results: water committee structure, decision-making, members' roles",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: qualitative study (40 KIIs/FGDs, 6 villages) of "
        "village-level water committee governance under Fiji's Water Authority statutory framework, examining "
        "decision-making structures, gender dynamics and accountability mechanisms directly shaping water access "
        "and security management. Strong Family A/B match, consistent with the Mozambique/community-water-"
        "committee inclusion precedent. NOT effect_sizes eligible: qualitative interview-based case study, no "
        "regression-based estimate. Extracted for record_id R355ECFDBF14D."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S992 - R35461F430753 - Harvey 2017 - Uganda WASH road map
r = blank_row(fieldnames)
r.update({
    "study_id": "S992",
    "citation": "Harvey A (2017). Steps to sustainability: A road map for WASH. Waterlines.",
    "doi": "10.3362/1756-3488.17-00002",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Uganda",
    "subnational_unit": "rural Uganda, national program",
    "legal_system": "common law",
    "urban_rural": "rural",
    "service_provider": "community management committees, service utility under public-private-partnership arrangement, Whave Solutions (social enterprise)",
    "regulatory_model": "regulatory structure and service-delivery PPP developed by the Ministry of Water and Environment 'Learning Alliance'; proposed new by-laws; standard constitutions and legal status (banking/legal registration) for community water-management committees; reliability-assurance contracts",
    "population": "rural households across 200+ communities",
    "sample_size": "implementation program across 200+ communities, multi-year Learning Alliance consultation process",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "fees": "TRUE",
    "institutional_fragmentation": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_reliability": "TRUE",
    "service_continuity": "TRUE",
    "study_design": "program case study/action research",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original program case study documenting the design and implementation of a "
        "regulatory structure, public-private-partnership maintenance contracts, proposed new by-laws, and formal "
        "legal status (standard constitutions, banking/legal registration) for community water-management "
        "committees, implemented in over 200 communities to improve reliable household water access."),
    "source_document": "Harvey 2017, Waterlines (retrieved via Google Drive)",
    "section": "PPP key elements; regulatory structure and by-laws",
    "exact_location": "Throughout, esp. sections on regulatory structure and management-committee legal status",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: program case study of a Ugandan Ministry of Water and "
        "Environment-supported 'Learning Alliance' regulatory structure and service-delivery PPP, including "
        "proposed new by-laws and formal legal status (standard constitutions, banking/legal registration) for "
        "community water-management committees, implemented via performance-payment maintenance contracts in over "
        "200 communities. Strong Family A/B match. NOT effect_sizes eligible: descriptive program case study, no "
        "regression-based estimate. Extracted for record_id R35461F430753."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S993 - R330A544EACCE - Chidya, Mulwafu & Banda 2016 - Malawi Lilongwe
r = blank_row(fieldnames)
r.update({
    "study_id": "S993",
    "citation": "Chidya RCG, Mulwafu WO, Banda S (2016). Water supply dynamics and quality of alternative water sources in low-income areas of Lilongwe City, Malawi. Physics and Chemistry of the Earth.",
    "doi": "10.1016/j.pce.2016.03.003",
    "publication_year": "2016",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Malawi",
    "subnational_unit": "Lilongwe City low-income areas",
    "legal_system": "common law",
    "urban_rural": "urban low-income/informal areas",
    "service_provider": "Lilongwe Water Board (formal utility); small-scale independent providers (SSIPs) -- vendors, boreholes, shallow wells",
    "regulatory_model": "Malawi Water Works Act (1995) regulating urban water supply/sanitation and the five regional water boards; National Water Policy (2005); National Sanitation Policy (2008); Land Act",
    "population": "households in low-income areas of Lilongwe not adequately reached by the formal utility",
    "sample_size": "120 households, 25 key informant interviews, 24 SSIP water-quality sampling sites",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "service_area": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "extraction_sample_size": "120",
    "study_design": "cross-sectional mixed-methods household survey with water-quality testing",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original empirical mixed-methods study (120 households, 25 key informants) "
        "directly linking the formal utility's institutional/regulatory framework under Malawi's Water Works Act "
        "(1995) and its failure to reach low-income informal areas to the emergence and water-quality "
        "characteristics of small-scale independent water providers filling the access gap."),
    "source_document": "Chidya, Mulwafu & Banda 2016, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    "section": "Introduction: Provision of water and sanitation services in Malawi; Results on SSIP dynamics",
    "exact_location": "Throughout, esp. institutional/regulatory framework discussion and household survey results",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: empirical mixed-methods study (120 households, 25 "
        "informants, 24 SSIP sites) of alternative/informal water-provider dynamics in low-income Lilongwe under "
        "Malawi's Water Works Act (1995) institutional/regulatory framework, documenting the formal utility's "
        "failure to reach informal settlements and the resulting reliance on unregulated small-scale providers. "
        "Family A/C match. NOT effect_sizes eligible: descriptive survey and water-quality data, no regression-"
        "based estimate isolating a legal mechanism's effect. Extracted for record_id R330A544EACCE."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S994 - R317C83144950 - Behailu, Hukka & Katko 2017 - Ethiopia rural water supply failures
r = blank_row(fieldnames)
r.update({
    "study_id": "S994",
    "citation": "Behailu BM, Hukka JJ, Katko TS (2017). Service Failures of Rural Water Supply Systems in Ethiopia and Their Policy Implications. Public Works Management & Policy.",
    "doi": "10.1177/1087724X16656190",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ethiopia",
    "subnational_unit": "national, multiple rural water schemes",
    "legal_system": "civil law",
    "urban_rural": "rural",
    "service_provider": "local government institutions responsible for rural water-scheme implementation, operation and maintenance",
    "regulatory_model": "lack of uniform implementation approaches across local government institutions; institutional and organizational capability of local government",
    "population": "rural communities served (or formerly served) by failed rural water supply schemes",
    "sample_size": "48 expert interviews, 35 artisan interviews, 20 failed water schemes visited with village elder discussions",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "eligibility": "TRUE",
    "documentation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_continuity": "TRUE",
    "service_reliability": "TRUE",
    "extraction_sample_size": "48 experts, 35 artisans, 20 schemes",
    "study_design": "mixed-methods field study with literature review and expert/artisan interviews",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": ("High: original field study (48 experts, 35 artisans, 20 failed schemes visited) "
        "directly diagnosing lack of uniformity in implementation approaches and institutional/organizational "
        "incapability of local government as primary determinants of rural water-supply service failures forcing "
        "communities back to unprotected water sources."),
    "source_document": "Behailu, Hukka & Katko 2017, Public Works Management & Policy (retrieved via Google Drive)",
    "section": "Findings on determinant factors of service failures",
    "exact_location": "Throughout results sections",
    "extraction_note": ("INCLUDE per INCLUSION_EXCLUSION.md: mixed-methods field study (48 experts, 35 artisans, 20 "
        "failed schemes) diagnosing local-government institutional and organizational incapability -- not merely "
        "technical/financial constraints -- as the primary determinant of rural water-supply service failures in "
        "Ethiopia, forcing communities to revert to unprotected sources. Strong Family A/B match. NOT effect_sizes "
        "eligible: qualitative/descriptive field study, no regression-based estimate. Extracted for record_id "
        "R317C83144950."),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
