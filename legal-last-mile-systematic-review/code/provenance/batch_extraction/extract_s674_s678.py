import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


new_rows = []

# S674 - Brottem 2018, Mali administrative-territory legal codification and water access
r = blank_row(fieldnames)
r.update({
    "study_id": "S674",
    "citation": "Brottem LV (2018). Dig Your Own Well: A Political Ecology of Rural Institutions in Western Sub-Saharan Africa. Annals of the American Association of Geographers 108:1075-1095.",
    "doi": "10.1080/24694452.2017.1406328",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mali",
    "subnational_unit": "Kayes region (Kita and Nioro districts)",
    "legal_system": "civil law (Mali)",
    "urban_rural": "rural",
    "service_provider": "local/municipal government; decentralized administrative institutions",
    "regulatory_model": "administrative-territory legal codification under a succession of governments determining the size/reach of officially recognized villages and administrative units, shaping eligibility for officially funded water infrastructure",
    "population": "villages/hamlets in 44 municipalities in Kayes region, Mali",
    "sample_size": "44 municipalities (field survey sample); archival sources; 20th-century census data (INSTAT); cartographic data",
    "household_level": "",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "documentation": "TRUE",
    "eligibility": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "effect_measure": "coefficient (R-squared improvement)",
    "extraction_sample_size": "44 municipalities; regression predicting hamlet count from administrative reach and other covariates",
    "model_type": "linear regression (best subsets, extra sum of squares test)",
    "study_design": "mixed-methods institutional case study (archival, census, field survey, geospatial regression analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate-high: administrative-territory legal codification (the historical-geographic formation of officially recognized administrative units under successive Malian governments) is documented via a formal regression model as a significant predictor of hamlet/settlement proliferation (R2 improving from 0.53 to 0.63, p<0.05), which the study argues drives real village-level exclusion from officially funded water infrastructure, though the regression's direct dependent variable is hamlet count rather than a water-access outcome itself; the water-access disparity analysis is presented via descriptive/geospatial (kernel density) methods.",
    "source_document": "Brottem 2018, Annals of the American Association of Geographers 108:1075-1095 (retrieved via Google Drive inbox)",
    "page": "1075-1095",
    "table": "Tables 4-7 (regression results)",
    "figure": "Figure 7 (kernel density of villages with improved water sources)",
    "section": "Results; Discussion",
    "exact_location": "Sections on administrative reach regression and water-access disparity mapping",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/legal political-ecology study of administrative-territory legal codification driving water-access disparities in rural Mali, with real archival/census/field-survey/regression evidence. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: the regression's dependent variable is hamlet count/settlement structure, not a water-access outcome directly. Extracted for record_id RDE671123A010.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S675 - Bond 2019, Durban post-apartheid water/sanitation policy
r = blank_row(fieldnames)
r.update({
    "study_id": "S675",
    "citation": "Bond P (2019). Tokenistic water and neoliberal sanitation in post-apartheid Durban. Journal of Contemporary African Studies 37:275-293.",
    "doi": "10.1080/02589001.2019.1710115",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Durban (eThekwini Municipality)",
    "legal_system": "common law (South Africa)",
    "urban_rural": "urban",
    "service_provider": "eThekwini Water and Sanitation (EWS); Umgeni Water (bulk supplier)",
    "regulatory_model": "Free Basic Water policy (6 kl/household/month, later 9 kl); means-testing indigence policy; disconnection/flow-limiter enforcement; litigated case Manquele v. eThekwini (2000-2001, unsuccessful constitutional challenge to disconnection); Project Viability (1997) credit-control framework",
    "population": "domestic water/sanitation consumers in Durban, disproportionately low-income Black and Indian residents",
    "sample_size": "documentary/historical policy analysis with administrative disconnection statistics and secondary household price-elasticity data (Bailey & Buckley 2005)",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "judicial_review": "TRUE",
    "sanction": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "effect_measure": "price elasticity (cited secondary estimate)",
    "extraction_sample_size": "administrative disconnection data (~1,000/day; 40,000 more disconnected than connected 2002-2003); price elasticities by wealth band (-0.55, -0.15, -0.11) from Bailey & Buckley 2005",
    "model_type": "documentary/historical institutional-policy analysis",
    "study_design": "historical-institutional case study (documentary/policy analysis with administrative statistics)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "High: Durban's real Free Basic Water and disconnection/means-testing policy framework, including a real litigated constitutional disconnection case (Manquele), is documented against real administrative disconnection statistics (1,000/day) and household-level price-elasticity/consumption data disaggregated by wealth band, showing poor households were overcharged relative to ability to pay and disproportionately disconnected.",
    "source_document": "Bond 2019, Journal of Contemporary African Studies 37:275-293 (retrieved via Google Drive inbox)",
    "page": "275-293",
    "section": "Demand, disconnections and pricing",
    "exact_location": "Sections on the Manquele litigation, Free Basic Water history, and price-elasticity findings",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documentary institutional/legal case study of post-apartheid Durban water/sanitation policy, disconnection litigation, and household-level pricing/consumption outcomes. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: price-elasticity estimates are cited from a secondary source (Bailey & Buckley 2005), not this paper's own primary regression analysis. Extracted for record_id R3520D2BF6FB3.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S676 - Hernandez Aguilar et al 2021, Mexico City informal-settlement water narratives
r = blank_row(fieldnames)
r.update({
    "study_id": "S676",
    "citation": "Hernandez Aguilar B, Lerner AM, Manuel-Navarrete D, Siqueiros-Garcia JM (2021). Persisting narratives undermine potential water scarcity solutions for informal areas of Mexico City: the case of two settlements in Xochimilco. Water International 46:919-937.",
    "doi": "10.1080/02508060.2021.1923179",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Amplicacion Tizilclipa and San Jose Obrero, Xochimilco municipality, Mexico City",
    "legal_system": "civil law (Mexico)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "Mexico City Water System Authority (SACMEX); local government (Alcaldia); water truck operators (piperos); community water committees (paradas)",
    "regulatory_model": "Sustainable Water Law of Mexico City (2017), prohibiting provision of public services to informal settlers in the Conservation Zone; land-titling/formalization process",
    "population": "residents of two informal settlements without land title in the Xochimilco Conservation Zone",
    "sample_size": "27 key-informant interviews (community leaders, water-committee leaders, local/city government officials) plus a 41-resident questionnaire (20 San Jose Obrero, 21 Amplicacion Tizilclipa)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "documentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "27 key-informant interviews; 41-resident questionnaire across 2 informal settlements",
    "model_type": "qualitative thematic/narrative analysis with coded interview and questionnaire data",
    "study_design": "qualitative case study (semi-structured interviews, structured questionnaire, MAXQDA coding)",
    "risk_of_bias_tool": "CASP",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Mexico City's 2017 Sustainable Water Law explicitly prohibiting public-service provision to informal settlers in the Conservation Zone is documented as a real legal barrier via 27 key-informant interviews (including government officials) and a 41-resident questionnaire, showing how formalization/land-titling narratives shape household-level water-access coping strategies and costs in two named informal settlements.",
    "source_document": "Hernandez Aguilar, Lerner, Manuel-Navarrete & Siqueiros-Garcia 2021, Water International 46:919-937 (retrieved via Google Drive inbox)",
    "page": "919-937",
    "table": "Table 1 (study participants)",
    "figure": "Figure 2 (narrative/impact coding); Figure 3 (water supply preferences)",
    "section": "Methodology; Results",
    "exact_location": "Sections on the 2017 Sustainable Water Law and formalization-narrative interview findings",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative institutional case study of legal exclusion of informal settlements from Mexico City's water grid, with real primary interview/questionnaire data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative thematic-coding design, no regression-based causal estimate. Extracted for record_id R8645861E4624.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S677 - Birkenholtz 2013, Rajasthan intervillage/intragender water differentiation
r = blank_row(fieldnames)
r.update({
    "study_id": "S677",
    "citation": "Birkenholtz T (2013). \"On the network, off the map\": developing intervillage and intragender differentiation in rural water supply. Environment and Planning D: Society and Space 31:354-371.",
    "doi": "10.1068/d11510",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "western Rajasthan (Indira Gandhi Canal command area)",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "state water-supply network (Indira Gandhi Canal-fed reservoirs, treatment facilities, distribution centers, supply pipelines); government engineers",
    "regulatory_model": "state-planned rural water-supply network expansion program; caste-stratified (General/OBC/SC/ST) differential village-level network access",
    "population": "households across multiple villages in the Indira Gandhi Canal command area, Rajasthan",
    "sample_size": "180-household survey with caste-disaggregated data (General n=45, Muslim n=20, OBC n=70, SC n=38, ST n=7), plus interviews with water users and government engineers, and participant observation",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "indigenous_population": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "effect_measure": "correlation coefficient",
    "extraction_sample_size": "180 households across multiple villages, caste-disaggregated (Table with village/caste-level water-collection-time and network-connection data)",
    "model_type": "mixed-methods analysis (descriptive statistics, correlation analysis, qualitative interviews)",
    "study_design": "cross-sectional mixed-methods case study (household surveys, interviews, participant observation)",
    "risk_of_bias_tool": "MMAT",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: state-planned rural water-supply network expansion is documented as producing real intervillage and intra-caste/gender differentiation in water access, via a primary 180-household survey with caste-disaggregated outcome data (water-collection time, network connection) plus interviews with water users and government engineers, showing village-of-residence as a stronger predictor of water-collection burden than caste alone among high-caste households.",
    "source_document": "Birkenholtz 2013, Environment and Planning D: Society and Space 31:354-371 (retrieved via Google Drive inbox)",
    "page": "354-371",
    "table": "caste/village-disaggregated household water-access data table",
    "section": "Methods; Results",
    "exact_location": "Sections on the 180-household survey and caste/village correlation analysis",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods political-ecology case study of state water-network expansion producing intervillage/intragender/caste differentiation in rural water access, with real primary household survey data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: reported statistics are descriptive correlations (caste/village vs. collection time), not a regression-based estimate of a legal/institutional mechanism. Extracted for record_id R59B2D594C94F.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S678 - Eguavoen 2013, Northern Ghana household water rights 1965-2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S678",
    "citation": "Eguavoen I (2013). Far from basic rules: social dynamics, legal regulations and access to household water in Northern Ghana, 1965-2012. Canadian Journal of African Studies 47:483-500.",
    "doi": "10.1080/00083968.2013.827987",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Nankana East District, Northern Ghana (village of ~8,000 inhabitants)",
    "legal_system": "common law (Ghana) with customary law",
    "urban_rural": "rural",
    "service_provider": "state water authorities; Community Water and Sanitation Agency (CWSA); Water and Sanitation Development Boards (WSDBs); customary/project-based water user communities",
    "regulatory_model": "1992 Ghanaian constitution (Article 257/6, vesting water resources in the state); Water Resources Commission Act 522 (1996); National Community Water and Sanitation Program (1998); customary and project-based water rights operating alongside statutory law; Public Utility Regulatory Commission (PURC) for urban/metropolitan areas",
    "population": "households in a rural Northern Ghana village, 1965-2012",
    "sample_size": "ethnographic and archival data collected primarily 2004-2006, including a survey of all water user groups, water user communities, and interest groups in the study village",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "survey of all water user groups/communities/interest groups in an 8,000-inhabitant village; historical analysis spanning four periods, 1965-2012",
    "model_type": "ethnographic/historical qualitative analysis with archival and interview data",
    "study_design": "ethnographic-historical case study (interviews, participant observation, archival/project-document review)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "High: Ghana's real statutory legal framework for water (1992 constitution Article 257/6, Water Resources Commission Act 522/1996, National Community Water and Sanitation Program) is documented in dissonance with customary and project-based water rights via long-term primary ethnographic and archival fieldwork (2004-2006, plus historical data back to 1965) in a single well-characterized rural village, directly tracing institutional bricolage and its effect on real household-level water access across four historical periods.",
    "source_document": "Eguavoen 2013, Canadian Journal of African Studies 47:483-500 (retrieved via Google Drive inbox)",
    "page": "483-500",
    "table": "Table 2 (statutory vs. customary/project water rights comparison)",
    "section": "Domestic water development in Northern Ghana; The interface between statutory and local water rights",
    "exact_location": "Sections on the 1992 constitution, WRC Act 522, and customary/statutory rights dissonance",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Ethnographic/historical institutional-legal case study of statutory/customary water-rights dissonance in rural Northern Ghana over nearly five decades, with real primary ethnographic and archival data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: ethnographic-historical design, no regression-based causal estimate. Extracted for record_id RF456013643C2.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, f"{r['study_id']} already exists"

rows.extend(new_rows)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"Added {len(new_rows)} rows. New total: {len(rows)}")
