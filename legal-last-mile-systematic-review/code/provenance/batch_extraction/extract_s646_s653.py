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

# S646 - Mycoo 2011, Trinidad water pricing
r = blank_row(fieldnames)
r.update({
    "study_id": "S646",
    "citation": "Mycoo M (2011). Conflicting Objectives of Trinidad's Water Pricing Policy: A Need for Good Water Pricing and Governance. International Journal of Water Resources Development 27:783-800.",
    "doi": "10.1080/07900627.2011.619899",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Trinidad and Tobago",
    "subnational_unit": "national",
    "legal_system": "common law (Trinidad and Tobago)",
    "urban_rural": "urban and rural",
    "service_provider": "Water and Sewerage Authority (WASA, national parastatal utility)",
    "regulatory_model": "WASA's flat annual-rental-value (ARV) based tariff, unchanged since 1993, provides no direct metering-based cost recovery incentive; national water policy debates over pricing reform, metering, and privatization spanning 1988-2008",
    "population": "national household population served (or seeking service) from WASA, Trinidad",
    "sample_size": "national administrative accounts data 1988-2008; interviews conducted 1993, 2000, 2002, 2010",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "",
    "eligibility": "",
    "burden": "",
    "fees": "TRUE",
    "service_area": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "national accounts data (1988-2008); household survey (1996 WTP survey)",
    "model_type": "descriptive policy case study; secondary analysis of utility accounts and survey data",
    "study_design": "longitudinal institutional case study (20-year policy analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: a genuine institutional/administrative water-pricing-policy factor (flat ARV-based tariff unchanged since 1993, absence of metering) is documented against real longitudinal WASA accounts data and household coping/expenditure evidence spanning two decades, showing clear reliability decline (45% receiving 24-hour service in 1994 down to 18-21% by 2008) and rising household storage-tank ownership (66% in 1991 to 80% in 2010) as a coping response to unreliable pricing-linked service.",
    "source_document": "Mycoo 2011, International Journal of Water Resources Development 27:783-800 (retrieved via Google Drive inbox)",
    "page": "783-800",
    "section": "Water Pricing Policy History; Impacts of Pricing Policy",
    "exact_location": "Sections on tariff history (1988-2008) and household reliability/coping data",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional/administrative water-pricing-policy case study documenting flat ARV-based tariff and its household-level reliability, equity, and coping-behavior impacts in Trinidad, 1988-2008. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive longitudinal case study, no regression-based causal estimate. Extracted for record_id RE9D7E0998707.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S647 - Bond 2013, South Africa Mazibuko/Phiri
r = blank_row(fieldnames)
r.update({
    "study_id": "S647",
    "citation": "Bond P (2013). Water rights, commons and advocacy narratives. South African Journal on Human Rights 29:125-143.",
    "doi": "10.1080/19962126.2013.11865068",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Soweto, Johannesburg",
    "legal_system": "common law/mixed (South Africa); Constitution s27(1)(b)",
    "urban_rural": "urban (informal settlements)",
    "service_provider": "Johannesburg Water (managed by Suez/Johannesburg Water)",
    "regulatory_model": "South African Constitution s27(1)(b) (right to water), Water Services Act 108 of 1997, Free Basic Water policy (block tariff); litigated through Mazibuko v. City of Johannesburg ('Phiri case') -- High Court 2008 (50L/person/day, pre-payment meters unconstitutional) -> Supreme Court of Appeal (42L conditional on indigency) -> Constitutional Court 2009 (upheld 25L/person/day and pre-payment meters as reasonable and lawful)",
    "population": "households in Soweto/Johannesburg informal settlements (Phiri)",
    "sample_size": "documentary/case-law analysis with household service-type survey data",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "household service-type breakdown (Soweto/Johannesburg informal settlements)",
    "model_type": "documentary/case-law analysis with descriptive household service-type data",
    "study_design": "historical-archival/legal institutional case study (constitutional litigation trajectory)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "High: a rigorously documented constitutional water-rights litigation trajectory (Mazibuko/Phiri case, Constitution s27(1)(b), Water Services Act 108 of 1997) through three court levels directly adjudicated household litre-per-person-per-day entitlements and pre-payment-meter legality, evidenced against real household-level service-type data (65% communal standpipes, 20% tanker water, 15% yard taps for water access; 52% pit latrines, 45% chemical toilets, 2% communal flush, 1% ablution blocks for sanitation) and Free Basic Water block-tariff/price-elasticity-by-income data.",
    "source_document": "Bond 2013, South African Journal on Human Rights 29:125-143 (retrieved via Google Drive inbox)",
    "page": "125-143",
    "section": "Mazibuko litigation history; household service-type data",
    "exact_location": "Sections on the Phiri case litigation trajectory and service-type breakdown tables",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Constitutional/legal water-rights litigation case study (Mazibuko v. City of Johannesburg) documenting household-level service-type, tariff, and price-elasticity data for Soweto/Johannesburg informal settlements. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: documentary/legal case-study design, no regression-based causal estimate. Extracted for record_id R0299C96CF472.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S648 - Pierce 2012, Mexico City privatization
r = blank_row(fieldnames)
r.update({
    "study_id": "S648",
    "citation": "Pierce G (2012). The Political Economy of Water Service Privatization in Mexico City, 1994-2011. International Journal of Water Resources Development 28:675-691.",
    "doi": "10.1080/07900627.2012.685126",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Federal District (Distrito Federal), Mexico City",
    "legal_system": "civil law (Mexico)",
    "urban_rural": "urban",
    "service_provider": "four private concession consortia (SAPSA, IASA, TECSA, AGUAMEX) under Comision de Aguas del Distrito Federal (CADF)/Sistema de Aguas de la Ciudad de Mexico (SACM)",
    "regulatory_model": "concession-contract privatization structure (1994 initial 10-year contracts, renegotiated post-2003); 2002 Federal Transparency Law of Access to Public Information used by civil-society coalition COMDA to obtain contract/tariff information",
    "population": "households in Distrito Federal (DF), outer Metropolitan Area of Mexico City (ZMCM), and outer Metropolitan Area of the Valley of Mexico (ZMVM)",
    "sample_size": "Mexican census data 1990-2010 (INEGI)",
    "household_level": "TRUE",
    "income_group": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "fees": "TRUE",
    "participation": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "census data, DF/ZMCM/ZMVM household populations 1990-2010",
    "model_type": "descriptive political-economy case study using census time-series data",
    "study_design": "longitudinal institutional case study (privatization contract periods 1994-2003 and 2003-2011)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate: a legal/institutional water-service-privatization concession framework is documented against real census-based household-level basic-access and in-home-piped-connection data across three geographic scales (DF, outer ZMCM, outer ZMVM) over a 20-year period, plus a documented legal-transparency mechanism (COMDA's use of the 2002 Federal Transparency Law); however, the descriptive analysis does not isolate privatization's causal effect from confounding factors such as in-migration and political will.",
    "source_document": "Pierce 2012, International Journal of Water Resources Development 28:675-691 (retrieved via Google Drive inbox)",
    "page": "675-691",
    "table": "Table 3 (household access by geographic scale, 1990-2010)",
    "section": "Impact of Service Privatization on Household Water Access; Civil Society Groups Scale up Concerns",
    "exact_location": "Table 3 and the COMDA/transparency-law section",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Political-economy case study of Mexico City water-service concession privatization documenting household-level census access data and a civil-society legal-transparency mechanism. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive census time-series comparison, no regression-based causal estimate isolating the privatization effect. Extracted for record_id RC4DF38E3B363.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S649 - Rivas 2012, Mexico indigenous municipalities piped water (effect_sizes candidate)
r = blank_row(fieldnames)
r.update({
    "study_id": "S649",
    "citation": "Gonzalez Rivas M (2012). Why do indigenous municipalities in Mexico have worse piped water coverage? Development in Practice 22:31-43.",
    "doi": "10.1080/09614524.2012.630983",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "2,372 municipalities nationwide",
    "legal_system": "civil law (Mexico); Article 115 of the Mexican Constitution (municipal responsibility for water services)",
    "urban_rural": "national (urban and rural municipalities)",
    "service_provider": "municipal water utilities (funded substantially by federal intergovernmental transfers, Aportaciones Federales)",
    "regulatory_model": "Article 115 of the Mexican Constitution assigns water-service management to municipalities; federal government contributes up to 45% of municipal water-infrastructure investment via per-capita transfers (Aportaciones Federales)",
    "population": "households in Mexican municipalities, 2000-2005, disaggregated by indigenous population share",
    "sample_size": "2,372 municipalities (GLM regression); 2,342 municipalities (OLS transfer regression)",
    "household_level": "TRUE",
    "indigenous_population": "TRUE",
    "income_group": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "effect_measure": "regression coefficient (GLM logit-link and OLS)",
    "effect_estimate": "indigenous population share: -0.0310 (piped-water-coverage GLM model); federal transfers per capita: 0.5713 (piped-water-coverage GLM model with transfers)",
    "standard_error": "0.0126 (indigenous coefficient); 0.2437 (transfers coefficient)",
    "p_value": "0.014 (indigenous coefficient); 0.019 (transfers coefficient)",
    "extraction_sample_size": "2,372 municipalities (2005 coverage model); 2,342 municipalities (transfers models)",
    "adjusted_or_unadjusted": "adjusted (density, income, migration, water-in-2000, spatial lag, state dummies)",
    "covariates": "population density, per-capita income, migration share, prior (2000) piped-water coverage, spatial lag, state fixed effects, vote share for president (transfers model)",
    "model_type": "generalised linear model (logit link) and ordinary least squares regression",
    "study_design": "national cross-sectional/panel regression analysis (2000-2005 census-based)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "High: a rigorous national regression design (2,372-2,342 municipalities) identifies a specific institutional/fiscal mechanism -- reduced per-capita federal transfers under Mexico's constitutionally assigned (Article 115) municipal water-management system -- as significantly driving lower piped-water coverage for indigenous municipalities, with both the indigenous-population and transfers-per-capita coefficients statistically significant, and a three-model causal chain (coverage model, transfers model, coverage-with-transfers model) explicitly testing and confirming the mechanism.",
    "source_document": "Gonzalez Rivas 2012, Development in Practice 22:31-43 (retrieved via Google Drive inbox)",
    "page": "31-43",
    "table": "Table 3; Table 4; Table 5",
    "section": "Results",
    "exact_location": "Tables 3-5 (regression results)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). National regression study of Mexican municipalities linking constitutionally assigned municipal water governance and federal fiscal-transfer allocation to unequal piped-water coverage for indigenous populations. Included per INCLUSION_EXCLUSION.md criteria 1-9. Effect_sizes eligible: significant institutional/fiscal-transfer mechanism coefficient. Extracted for record_id RAFD43FB2362E.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S650 - Fernandez & Buitron Cisneros 2012, Ecuador right to water
r = blank_row(fieldnames)
r.update({
    "study_id": "S650",
    "citation": "Fernandez N, Buitron Cisneros R (2012). The Right to Water and Sanitation in Ecuador: Progress, Limitations, and Challenges. Environmental Justice 5:77-81.",
    "doi": "10.1089/env.2011.0021",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ecuador",
    "subnational_unit": "national (Amazonia, Coastal, Sierra regions)",
    "legal_system": "civil law (Ecuador); 2008 Constitution Article 318 (unique water authority)",
    "urban_rural": "urban and rural",
    "service_provider": "SENAGUA (National Secretariat for Water Provision), MIDUVI, municipalities (219 municipalities), community systems (JAAPRE)",
    "regulatory_model": "2008 Constitution Article 318 establishes a single water authority (SENAGUA) responsible for water-resource planning/management; overlapping jurisdiction with MIDUVI, MAE, MSP, INAR; pending Water Resources, Uses and Management Act",
    "population": "national household population, disaggregated by region, income quintile, urban/rural, and ethnicity/race",
    "sample_size": "national census and living-conditions survey data (1990-2008)",
    "household_level": "TRUE",
    "indigenous_population": "TRUE",
    "income_group": "TRUE",
    "institutional_fragmentation": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_continuity": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "national census/survey data disaggregated by region, income quintile, ethnicity",
    "model_type": "descriptive institutional/policy analysis with disaggregated census data",
    "study_design": "descriptive national policy case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate: Ecuador's 2008 constitutional water-rights framework (Article 318) and resulting institutional fragmentation among multiple overlapping agencies (SENAGUA, MIDUVI, MAE, MSP) are documented against real household-level access data disaggregated by region, income quintile, urban/rural status, and ethnicity/race (piped-water coverage 18% for indigenous-headed vs. 48% national average vs. 57% white-headed households), though the study is primarily descriptive and does not isolate the institutional-fragmentation mechanism via regression.",
    "source_document": "Fernandez & Buitron Cisneros 2012, Environmental Justice 5:77-81 (retrieved via Google Drive inbox)",
    "page": "77-81",
    "section": "The Country's Situation Evolution; Institution, Legislation, and Public Policy",
    "exact_location": "Sections on national/regional/quintile access data and institutional fragmentation",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Descriptive institutional/policy analysis of Ecuador's constitutional water-rights framework and institutional fragmentation, documenting disaggregated household-level access data by region, income, and ethnicity. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive policy analysis, no regression-based causal estimate. Extracted for record_id R5A010875D9FB.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S651 - Obeng-Odoom 2012, Ghana Beyond access to water
r = blank_row(fieldnames)
r.update({
    "study_id": "S651",
    "citation": "Obeng-Odoom F (2012). Beyond access to water. Development in Practice 22:1135-1146.",
    "doi": "10.1080/09614524.2012.714744",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Accra and urban Ghana",
    "legal_system": "common law (Ghana)",
    "urban_rural": "urban",
    "service_provider": "Ghana Water Company Limited (GWCL)/Ghana Urban Water Company Ltd (GUWCL); Aqua Vitens Rand Limited (AVRL, private management contractor 2006-2011)",
    "regulatory_model": "Public Utilities Regulatory Commission Act 538 (1997) established PURC as regulator; affermage-style management-contract public-private partnership model for urban water (AVRL)",
    "population": "urban households in Accra and urban Ghana, disaggregated by income",
    "sample_size": "World Bank 2010 Accra citizen survey; Ghana Statistical Service 2007 national household data",
    "household_level": "TRUE",
    "income_group": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "World Bank 2010 Accra survey (household connection/reliability data); Ghana Statistical Service 2007 quintile data",
    "model_type": "descriptive institutional/regulatory case-study analysis with household survey data",
    "study_design": "descriptive case study synthesizing multiple household survey sources",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Moderate-high: Ghana's institutional/regulatory water-privatization framework (PURC Act 538/1997, affermage-style AVRL management contract) is documented against real household-level survey data on connection rates by income quintile (57%/70%/83% by income band; 43% vs. 18.5% top-vs-bottom quintile), reliability (46% of connected households receive water 'only sometimes'/'rarely'), affordability (9-15% of household income spent on water), and a documented health outcome (80% reduction in diarrhea incidence with piped access), though the analysis is descriptive/comparative rather than a formal regression isolating the institutional-regulatory mechanism.",
    "source_document": "Obeng-Odoom 2012, Development in Practice 22:1135-1146 (retrieved via Google Drive inbox)",
    "page": "1135-1146",
    "section": "Access to water",
    "exact_location": "Access to water section (income-quintile connection, reliability, affordability, health data)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Descriptive institutional/regulatory case study of Ghana's urban water privatization documenting disaggregated household-level connection, reliability, affordability, and health data by income quintile. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive/comparative case study, no regression-based causal estimate. Extracted for record_id RE4E5A4029D2D.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S652 - Hackenbroch & Hossain 2012, Dhaka bosti water/public space
r = blank_row(fieldnames)
r.update({
    "study_id": "S652",
    "citation": "Hackenbroch K, Hossain S (2012). \"The organised encroachment of the powerful\"--Everyday practices of public space and water supply in Dhaka, Bangladesh. Planning Theory & Practice 13:397-420.",
    "doi": "10.1080/14649357.2012.694265",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Bangladesh",
    "subnational_unit": "a bosti (informal settlement), Dhaka",
    "legal_system": "common law (Bangladesh)",
    "urban_rural": "urban (informal settlement on public land)",
    "service_provider": "Dhaka Water Supply and Sewerage Authority (DWASA); informal local water vendors (political-committee leaders)",
    "regulatory_model": "settlement's illegal tenure status bars direct DWASA connection; local political leaders illegally tap the DWASA main and resell water under informal verbal contracts; a decade of NGO advocacy secured a 2007 government mandate for DWASA to supply water to 'slum' committees regardless of land-tenure status (GOB, 2007), though network extension was blocked by a neighbouring housing society's protest",
    "population": "residents of a bosti (informal settlement) in Dhaka, including room-cluster tenants and water vendors",
    "sample_size": "ethnographic fieldwork 2008-2010 (participant observation, in-depth interviews, Venn-diagram method, solicited photography)",
    "household_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "institutional_fragmentation": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_reliability": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "qualitative ethnographic fieldwork with in-depth interviews (2008-2010)",
    "model_type": "qualitative ethnographic/participatory analysis",
    "study_design": "qualitative ethnographic case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": "Moderate: tenure-based exclusion from statutory DWASA connection and an informal political-committee institutional arrangement governing illegal water resale are documented via rich ethnographic evidence, with real household-level outcome variation in water price ($9-22/hour) and service reliability/quality tied to political position, plus a documented 2007 institutional shift (DWASA mandated to serve informal settlements regardless of tenure) whose implementation remained blocked by a neighbouring housing society's objection at time of study.",
    "source_document": "Hackenbroch & Hossain 2012, Planning Theory & Practice 13:397-420 (retrieved via Google Drive inbox)",
    "page": "397-420",
    "section": "The Practice of Negotiating Access to Water Supply",
    "exact_location": "Section on negotiating access to water supply",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative ethnographic study of informal/political-institutional governance of illegal water access in a Dhaka bosti, documenting tenure-based exclusion, informal resale pricing, and a 2007 institutional shift toward tenure-blind DWASA service. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: qualitative ethnographic study. Extracted for record_id R658467768162.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S653 - Brinkerhoff, Wetterberg & Dunn 2012, Iraq water services/legitimacy
r = blank_row(fieldnames)
r.update({
    "study_id": "S653",
    "citation": "Brinkerhoff DW, Wetterberg A, Dunn S (2012). Service Delivery and Legitimacy in Fragile and Conflict-Affected States: Evidence from water services in Iraq. Public Management Review 14:273-293.",
    "doi": "10.1080/14719037.2012.657958",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Iraq",
    "subnational_unit": "14 provinces (9 surveyed: Babil, Najaf, Qadisiyah, Muthanna, Karbala, Wasit, Dhi Qar, Baghdad Province, Baghdad Amanat)",
    "legal_system": "civil law (Iraq); 2005 Constitution (decentralized federal structure), Law 21 of 2008 (provincial-level responsibilities)",
    "urban_rural": "urban and peri-urban neighbourhoods",
    "service_provider": "provincial/subnational water utilities (post-Saddam decentralized governance structure)",
    "regulatory_model": "2005 Iraqi Constitution created a decentralized federal structure; Law 21 of 2008 allocated new water/service responsibilities to the provincial level (subsequently contested; national parliament transferred functions to provinces in 2010, Supreme Court suspended the transfer)",
    "population": "household water-service customers across 9 Iraqi provinces",
    "sample_size": "6,979 completed household questionnaires across 9 provinces (2010 USAID-funded water services survey)",
    "household_level": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "service_reliability": "TRUE",
    "service_continuity": "TRUE",
    "effect_measure": "",
    "extraction_sample_size": "6,979 household questionnaires across 9 provinces",
    "model_type": "descriptive survey analysis (satisfaction and willingness-to-pay by province)",
    "study_design": "cross-sectional household survey (multi-province)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "2",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": "Low: a large real household-level water-services survey (6,979 respondents across 9 provinces) documents service continuity/satisfaction and willingness-to-pay outcomes against Iraq's institutional/legal decentralization framework (2005 Constitution, Law 21 of 2008), but the study's own framing is exploratory/suggestive regarding the specific legal-institutional (decentralization) mechanism, and the analysis centers on state-legitimacy theory rather than isolating a specific legal/administrative factor's effect on water access.",
    "source_document": "Brinkerhoff, Wetterberg & Dunn 2012, Public Management Review 14:273-293 (retrieved via Google Drive inbox)",
    "page": "273-293",
    "table": "Table 1 (survey implementation by province)",
    "figure": "Figure 2; Figure 3; Figure 4",
    "section": "The water services survey; Findings",
    "exact_location": "Table 1 and Findings section (satisfaction/WTP by province)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Large household water-services survey across 9 Iraqi provinces examining service continuity/satisfaction and willingness-to-pay within Iraq's post-2005 decentralized institutional/legal framework. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive survey analysis, no regression-based causal estimate isolating a legal/institutional mechanism. Extracted for record_id R34FB4E74EB11.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-22",
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, f"Duplicate study_id: {r['study_id']}"
    for key in list(r.keys()):
        if key not in fieldnames:
            raise AssertionError(f"Unexpected field not in schema: {key}")

rows.extend(new_rows)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"Appended {len(new_rows)} rows. New total: {len(rows)}")
