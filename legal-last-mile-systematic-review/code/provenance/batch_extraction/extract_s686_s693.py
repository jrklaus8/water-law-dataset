import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
for sid in ("S686", "S687", "S688", "S689", "S690", "S691", "S692", "S693"):
    assert sid not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

RESEARCHER = "Claude-AI-fulltext-2026-09-23"
DATE = "2026-09-23"

# ---------------- S686: Bakker 2005, England & Wales ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S686",
    "citation": "Bakker K (2005). Neoliberalizing Nature? Market Environmentalism in Water Supply in England and Wales. Annals of the Association of American Geographers 95(3):542-565.",
    "doi": "10.1111/j.1467-8306.2005.00474.x",
    "publication_year": "2005",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United Kingdom",
    "subnational_unit": "England and Wales",
    "legal_system": "common law",
    "urban_rural": "mixed",
    "service_provider": "privatized regional water and sewerage companies, regulated by Ofwat (Office of Water Services)",
    "regulatory_model": (
        "1989 privatization of water supply industry; economic regulator (Ofwat) operating under "
        "formal legal duty to protect consumers from discriminatory prices and maintain affordability; "
        "High Court ruling that prepayment water meters installed in low-income households were "
        "illegal; subsequent legislation increasing legal protection against domestic disconnection "
        "for non-payment"
    ),
    "population": "domestic water consumers in England and Wales, particularly low-income households",
    "sample_size": "national industry-level (not a household sample)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "FALSE",
    "eligibility": "FALSE",
    "fees": "TRUE",
    "disconnection": "TRUE",
    "water_access": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "study_design": "legal/regulatory documentary case study (post-privatization industry analysis)",
    "extraction_sample_size": "not applicable (documentary/regulatory case study)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "2",
    "mechanism_certainty": (
        "Moderate: the study documents specific, verifiable legal/regulatory events (Ofwat's statutory "
        "duty, a High Court ruling against prepayment meters, and subsequent disconnection-protection "
        "legislation) and their link to affordability/disconnection outcomes for low-income consumers, "
        "but does not provide a household-level dataset quantifying the resulting change in access; "
        "the causal narrative is documentary/qualitative rather than measured."
    ),
    "source_document": "Bakker 2005, Annals of the Association of American Geographers 95(3):542-565 (retrieved via Google Drive inbox)",
    "page": "542-565",
    "section": "Contradictions of Market Environmentalism; Conclusions: Uncooperative Commodity",
    "exact_location": "Discussion of Ofwat's regulatory duty, prepayment meter High Court ruling, and disconnection-protection legislation",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Legal/regulatory case study "
        "of England & Wales water privatization documenting real institutional mechanisms "
        "(regulator's statutory duty, court ruling, protective legislation) tied to household "
        "affordability/disconnection outcomes for low-income consumers. Included per "
        "INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: no regression-based point "
        "estimate/CI isolating the mechanism, purely documentary/narrative analysis. Extracted for "
        "record_id R483391EAF0A4."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S687: Schusterman & Hardoy 1997, Barrio San Jorge ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S687",
    "citation": "Schusterman R, Hardoy A (1997). Reconstructing Social Capital in a Poor Urban Settlement: the Integral Improvement Programme in Barrio San Jorge. Environment and Urbanization 9(1):91-119.",
    "doi": "10.1177/095624789700900109",
    "publication_year": "1997",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Argentina",
    "subnational_unit": "Barrio San Jorge, Buenos Aires",
    "legal_system": "civil law",
    "urban_rural": "urban",
    "service_provider": "official public water/sewerage utilities (after transition from informal arrangements); IIED-America Latina Community Support Programme (facilitating NGO)",
    "regulatory_model": (
        "Ten-year (1987-1997) community-support process through which an informal 'illegal' "
        "settlement acquired legal land tenure and a newly-formed representative community "
        "organization negotiated directly with municipal government agencies and utility companies, "
        "resulting in water and sanitation provision transitioning from informal/self-organized "
        "arrangements to formal management by the official utilities"
    ),
    "population": "residents of Barrio San Jorge, an informal settlement in Buenos Aires",
    "sample_size": "single settlement, longitudinal case study (1987-1997)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "FALSE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "longitudinal qualitative case study (historical/documentary, 10-year community-support programme)",
    "extraction_sample_size": "not applicable (single-settlement longitudinal case study)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": (
        "Moderate-high: the study documents, through 10 years of continuous programme engagement, a "
        "specific institutional pathway (legal tenure acquisition plus formation of a representative "
        "community organization) that directly produced formal utility management of water and "
        "sanitation provision where none existed before, with the settlement's legal status changing "
        "from 'illegal' to tenured. The causal chain is well-documented but qualitative/narrative "
        "rather than quantified."
    ),
    "source_document": "Schusterman & Hardoy 1997, Environment and Urbanization 9(1):91-119 (retrieved via Google Drive inbox)",
    "page": "91-119",
    "section": "Improving Physical Conditions and Access to Basic Services",
    "exact_location": "Discussion of land tenure acquisition and transition of water/sanitation provision to official utility management",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Historical-institutional "
        "case study extending the established Ofer 2009 Orcasitas (Madrid) precedent: illegal-"
        "settlement-to-legal-recognition-to-formal-utility-connection pathway via community "
        "organization negotiation. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not "
        "effect_sizes eligible: no regression-based point estimate/CI. Extracted for record_id "
        "R9741314656A3."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S688: Faisal & Kabir 2005, rural Bangladesh ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S688",
    "citation": "Faisal IM, Kabir MR (2005). An Analysis of Gender-Water Nexus in Rural Bangladesh. Journal of Developing Societies 21(1-2):175-194.",
    "doi": "10.1177/0169796X05054623",
    "publication_year": "2005",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "Bangladesh",
    "subnational_unit": "seven rural study locations across Bangladesh",
    "legal_system": "mixed (common law with statutory/customary elements)",
    "urban_rural": "rural",
    "service_provider": "Water Management Groups/Associations (WMG/WMA) under participatory irrigation-management schemes",
    "regulatory_model": (
        "Guidelines for Participatory Water Management (Ministry of Water Resources, 2000) mandating "
        "that women, landless persons, sharecroppers and Project Affected Persons be included as "
        "general members and members of the Managing/Executive Committee of Water Management Groups "
        "and Associations"
    ),
    "population": "rural households, particularly women, across seven study locations in Bangladesh",
    "sample_size": "field survey, focus group discussions and key-informant interviews at 7 study locations",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "participation": "TRUE",
    "eligibility": "TRUE",
    "water_access": "TRUE",
    "service_quantity": "TRUE",
    "affordability": "FALSE",
    "study_design": "mixed-methods primary field study (survey, FGD, key-informant interviews)",
    "extraction_sample_size": "seven study locations (household-level survey, FGDs, interviews)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": (
        "Moderate: the study documents a specific, real national policy mandate for gender-inclusive "
        "participation in water-management institutions and, via original field data across seven "
        "locations, finds this mandate is not reflected in actual practice - women have very little "
        "participation in agricultural/irrigation water management. The mechanism-outcome link is "
        "empirically grounded but presented narratively rather than via a formal statistical test."
    ),
    "source_document": "Faisal & Kabir 2005, Journal of Developing Societies 21(1-2):175-194 (retrieved via Google Drive inbox)",
    "page": "175-194",
    "section": "Irrigation Water Management",
    "exact_location": "Discussion of Guidelines for Participatory Water Management (MoWR 2000) and WMG/WMA membership provisions",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Primary field study tying a "
        "real national institutional/legal participation mandate (WMG/WMA membership guidelines) to "
        "documented de facto exclusion of women from water-management institutions, extending the "
        "established Singh 2006 PRI/ARWSP formal-inclusion-vs-de-facto-exclusion precedent. Included "
        "per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: no regression-based point "
        "estimate/CI. Extracted for record_id R02C6DE366093."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S689: Allen, Davila & Hofmann 2006, peri-urban water poor ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S689",
    "citation": "Allen A, Davila JD, Hofmann P (2006). The peri-urban water poor: citizens or consumers? Environment and Urbanization 18(2):333-351.",
    "doi": "10.1177/0956247806069608",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "multi-country (Mexico, Venezuela, India, Tanzania, Egypt)",
    "subnational_unit": "peri-urban areas of Mexico City, Caracas, Chennai, Dar es Salaam and Cairo (10 localities)",
    "legal_system": "mixed (civil law and common law jurisdictions)",
    "urban_rural": "peri-urban",
    "service_provider": "mix of centralized public utilities, private/market providers, and informal providers",
    "regulatory_model": (
        "Comparative institutional analysis distinguishing 'policy-driven' access practices (formal "
        "mechanisms rooted in citizens' rights/entitlements) from 'needs-driven' access practices "
        "(informal, market-based practices where residents are treated as consumers rather than "
        "rights-holders); finds peri-urban water/sanitation access is predominantly needs-driven and "
        "informal rather than the result of formal rights-based policy"
    ),
    "population": "peri-urban poor residents and producers in five metropolitan areas",
    "sample_size": "10 localities across 5 metropolitan areas; household interviews, focus groups, institutional interviews and multi-stakeholder workshops",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "TRUE",
    "institutional_fragmentation": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "affordability": "TRUE",
    "study_design": "comparative multi-site primary qualitative research (interviews, focus groups, institutional analysis)",
    "extraction_sample_size": "10 localities, 5 metropolitan areas (multi-method qualitative fieldwork)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": (
        "Moderate-high: a structured, multi-site three-year comparative research design (metropolitan-"
        "wide institutional analysis plus localized fieldwork with interviews, focus groups and "
        "transect walks across five metropolitan areas) consistently finds that peri-urban water/"
        "sanitation access is governed by informal needs-driven practice rather than formal "
        "citizen-entitlement policy, across highly varied legal/institutional contexts, strengthening "
        "confidence in the generality of the finding."
    ),
    "source_document": "Allen, Davila & Hofmann 2006, Environment and Urbanization 18(2):333-351 (retrieved via Google Drive inbox)",
    "page": "333-351",
    "section": "Policy-driven and Needs-driven Practices",
    "exact_location": "Comparative discussion of citizen entitlement vs. consumer market access across the five metropolitan case studies",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Comparative multi-site "
        "primary research project directly examining legal/institutional (rights-based/policy-driven) "
        "vs. informal/market (needs-driven) water and sanitation access mechanisms for the peri-urban "
        "poor. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: "
        "qualitative comparative synthesis, no regression-based point estimate/CI. Extracted for "
        "record_id RF3056823844E."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S690: Anand 2007, India/Chennai ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S690",
    "citation": "Anand PB (2007). Semantics of Success or Pragmatics of Progress? An Assessment of India's Progress With Drinking Water Supply. Journal of Environment & Development 16(1):32-57.",
    "doi": "10.1177/1070496506297005",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "national analysis with detailed case study of Chennai (Tamil Nadu)",
    "legal_system": "common law",
    "urban_rural": "mixed",
    "service_provider": "Chennai Metropolitan Water Supply and Sewerage Board (state-owned utility, created 1978)",
    "regulatory_model": (
        "Institutional mapping: Madras City Municipal Corporation Act 1919 originally assigned water "
        "supply/sanitation to elected local government; in 1978, on World Bank advice, the Tamil Nadu "
        "state government created a separate state-owned water board removing the function from local "
        "government, later adding a 1998 citizen's charter"
    ),
    "population": "households in Chennai metropolitan area, stratified by income group and location",
    "sample_size": "National Sample Survey 54th round (1998, national); household water-endowment survey n=148 households across 5 income groups (Chennai, from Anand 2001a/2001b)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "legal_status": "FALSE",
    "eligibility": "FALSE",
    "service_area": "TRUE",
    "water_access": "TRUE",
    "service_quantity": "TRUE",
    "affordability": "TRUE",
    "study_design": "institutional case study combining secondary national survey data with household-level entitlements analysis",
    "extraction_sample_size": "148 households across 5 income groups (Chennai case study)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "3",
    "mechanism_certainty": (
        "Moderate: the study documents a specific institutional transition (1919 municipal-law "
        "assignment of water supply to elected local government, superseded in 1978 by a state-created "
        "water board outside local democratic control) and shows, via household-level entitlements "
        "data, substantial income-stratified inequality in water access (33 lpcd for lowest-income "
        "households vs. 152 lpcd for highest-income) and worse outcomes in institutionally-weak "
        "peri-urban areas, but does not formally isolate the institutional-transition effect via "
        "regression."
    ),
    "source_document": "Anand 2007, Journal of Environment & Development 16(1):32-57 (retrieved via Google Drive inbox)",
    "page": "32-57",
    "section": "Water Supply and Water 'Scarcity' in Chennai; Institutional Mapping; Water Supply Scenario",
    "exact_location": "Table 5 (households in Chennai by income and water endowment) and surrounding institutional-mapping discussion",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Institutional case study "
        "applying an entitlements framework to household-level income-stratified water-access data in "
        "Chennai, tied to a documented legal/institutional history of the water utility. Included per "
        "INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: descriptive income-"
        "stratified endowment data, no regression-based point estimate/CI isolating an institutional "
        "mechanism. Extracted for record_id RF307BBEBB415."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S691: Jenson 2008, 19th century Britain ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S691",
    "citation": "Jenson J (2008). Getting to Sewers and Sanitation: Doing Public Health within Nineteenth-Century Britain's Citizenship Regimes. Politics & Society 36(4):532-566.",
    "doi": "10.1177/0032329208324712",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United Kingdom",
    "subnational_unit": "England (national, with provincial-city examples)",
    "legal_system": "common law",
    "urban_rural": "mixed",
    "service_provider": "private water/sewage companies (retaining existing distribution rights); local boards of health under the 1848 Public Health Act",
    "regulatory_model": (
        "Public Health Act 1848 (left responsibility for water supply/sewer provision with private "
        "companies, no central enforcement power, opt-in local boards of health); Municipal "
        "Corporations Act 1835; New Poor Law 1834; Vaccination Act 1853 (compulsory, enforced via Poor "
        "Law Guardians targeting the poor); citizenship-status-differentiated state intervention "
        "(surveillance/compulsion for the poor and non-citizens vs. reliance on market/self-regulation "
        "for full citizens)"
    ),
    "population": "English population, differentiated by class/citizenship status (property-owning ratepayers vs. the poor)",
    "sample_size": "historical-documentary (statutory record, contemporary reports, e.g. Royal Sanitary Commission 1871, General Registrar Office)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "eligibility": "FALSE",
    "fees": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "study_design": "historical-institutional documentary case study (statutory/archival analysis)",
    "extraction_sample_size": "not applicable (documentary/historical-institutional case study)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "2",
    "mechanism_certainty": (
        "Moderate-high: the study documents, via primary statutory and contemporary documentary "
        "sources, that the 1848 Public Health Act's specific governance design (private ownership of "
        "water/sewer rights, no central enforcement, opt-in local boards) produced a directly "
        "verifiable differential outcome - by 1846 only 10 of ~190 local authorities owned their own "
        "waterworks, and mass household connection lagged decades behind wealthier suburban villa "
        "connection - explicitly because market incentives to connect the poor were absent. The "
        "outcome evidence is documentary/qualitative rather than a measured dataset."
    ),
    "source_document": "Jenson 2008, Politics & Society 36(4):532-566 (retrieved via Google Drive inbox)",
    "page": "532-566",
    "section": "Paring Down Sanitarianism; The Citizenship Regime of the Age of Reform",
    "exact_location": "Discussion of the 1848 Public Health Act's governance design and its effect on household water/sewer connection rates",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Historical-institutional case "
        "study distinguished from the excluded Kucher 2005 precedent (pure doctrinal commentary with no "
        "access-outcome data): this study documents actual differential connection patterns by class/"
        "citizenship status tied to specific statutory mechanisms (1848 Public Health Act design). "
        "Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: documentary/"
        "narrative analysis, no regression-based point estimate/CI. Extracted for record_id "
        "R5DEFEB3CB256."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S692: Kumara 2013, Bangalore ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S692",
    "citation": "Kumara HS (2013). Revisit the Debate on Issues of Metropolitan Governance and Service Delivery: A Trajectory of Efficient Service Delivery Model for Water Supply in Bangalore, India. Environment and Urbanization ASIA 4(1):203-220.",
    "doi": "10.1177/0975425313477766",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Bangalore Metropolitan Region, Karnataka",
    "legal_system": "common law",
    "urban_rural": "urban",
    "service_provider": "Bangalore Water Supply and Sewerage Board (BWSSB) for the metropolitan center; ten Urban Local Bodies (Town/City Municipal Councils) served by KUWSDB in the metropolitan region",
    "regulatory_model": (
        "Institutional/governance fragmentation: a single dedicated metropolitan water-supply agency "
        "(BWSSB) for the core city vs. ten separate fragmented Urban Local Bodies for the surrounding "
        "metropolitan region, each with its own governance/service-delivery capacity"
    ),
    "population": "households in Bangalore Metropolitan Center and Bangalore Metropolitan Region (10 ULBs)",
    "sample_size": "11 governance units (1 metropolitan center + 10 ULBs), benchmarking indicator data",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "institutional_fragmentation": "TRUE",
    "service_area": "TRUE",
    "water_access": "TRUE",
    "service_coverage": "TRUE",
    "service_quantity": "TRUE",
    "service_reliability": "TRUE",
    "affordability": "FALSE",
    "study_design": "comparative institutional performance study (secondary benchmarking data, composite indices, correlation analysis)",
    "effect_measure": "Pearson correlation coefficient (inter-indicator correlation matrix)",
    "effect_estimate": "e.g., coverage in general households (COV1) vs. average weekly water availability (AVI1): r=0.8; COV1 vs. consumption (CON): r=0.5",
    "extraction_sample_size": "11 governance units (1 water board + 10 Urban Local Bodies)",
    "adjusted_or_unadjusted": "unadjusted",
    "model_type": "Pearson correlation matrix (not regression)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": (
        "Moderate: the study uses real benchmarking data (Karnataka Urban Service Level Benchmarking "
        "reports) to compare household- and slum-level water coverage, availability, consumption and "
        "cost-recovery across 11 differently-governed units, finding the single dedicated metropolitan "
        "board (BWSSB) outperforms the fragmented Urban Local Bodies on the composite Service Delivery "
        "Index (59.12 vs. a range of 21.31-52.36). This is a cross-sectional comparison across 11 "
        "units, not a controlled or regression-based causal test of the fragmentation mechanism."
    ),
    "source_document": "Kumara 2013, Environment and Urbanization ASIA 4(1):203-220 (retrieved via Google Drive inbox)",
    "table": "Table 4 (Water Utilities Indicator - Service Delivery Index and Operational Efficiency Index); Table 5 (Ranking); Table 6 (Correlation Matrix)",
    "page": "203-220",
    "section": "Service Delivery Model for Water Supply",
    "exact_location": "Tables 4-6, comparative service-delivery-index data by governance unit",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Comparative institutional "
        "performance study directly tying governance fragmentation (single metropolitan board vs. "
        "fragmented Urban Local Bodies) to differential household- and slum-level water-access "
        "outcomes via real benchmarking data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not "
        "effect_sizes eligible under the strict Family A/B/C framework: uses a Pearson correlation "
        "matrix among indicators and a descriptive composite index/ranking across 11 governance units, "
        "not a regression-based point estimate/CI isolating the institutional-fragmentation mechanism's "
        "effect. quantitative_synthesis_eligible in evidence_map.csv. Extracted for record_id "
        "R1F58000B5617."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

# ---------------- S693: Chathukulam & Devavrathan 2014, Kerala Gram Panchayats ----------------
r = blank_row(fieldnames)
r.update({
    "study_id": "S693",
    "citation": "Chathukulam J, Devavrathan S (2014). Applying Narrative and Quantitative Models for Understanding the Sanitation Arena of Selected Gram Panchayats in a Post-TSC Era from Kerala. Journal of Health Management 16(4):509-526.",
    "doi": "10.1177/0972063414548553",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "seven Gram Panchayats, Kozhikode district, Kerala",
    "legal_system": "common law",
    "urban_rural": "rural",
    "service_provider": "Gram Panchayats (Panchayati Raj Institutions), Kerala Total Sanitation and Health Mission (Suchitwa Mission)",
    "regulatory_model": (
        "Total Sanitation Campaign (TSC, Government of India, launched 1999) implemented through "
        "decentralized local-government institutions (Panchayati Raj Institutions/Gram Panchayats) "
        "responsible for programme delivery, combined with the Nirmal Gram Puraskar (NGP) fiscal-"
        "incentive scheme rewarding 'open defecation free' Panchayats"
    ),
    "population": "households, schools and anganwadis (child-care centres) in 7 Gram Panchayats, Kozhikode district",
    "sample_size": "496 households, 28 schools, 32 anganwadis across 7 Gram Panchayats",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "institutional_fragmentation": "FALSE",
    "bureaucratic_assistance": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "study_design": "mixed-methods primary field study (narrative + composite quantitative index; field survey, FGDs, direct observation)",
    "effect_measure": "composite Total Sanitation Index (TSI), 0-1 scale, unweighted average of 4 sub-indices",
    "effect_estimate": "TSI by Panchayat: Olavanna 0.73, Azhiyur 0.71, Nanmanda 0.65, Kodanchery 0.64, Perambra 0.63, Thikkody 0.63, Maniyur 0.62; household-sanitation coverage sub-index ranged 0.67-0.86 across the 7 Panchayats",
    "extraction_sample_size": "7 Gram Panchayats; 496 households, 28 schools, 32 anganwadis",
    "adjusted_or_unadjusted": "unadjusted",
    "model_type": "composite index (unweighted average of ordinal component scores), not regression",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "3",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": (
        "Moderate-high: the study uses original field-verified data (household survey, school/"
        "anganwadi facility audits, FGDs) across 7 Panchayats to construct a comparable sanitation-"
        "coverage index, finding meaningful variation across Panchayats linked in the narrative "
        "discussion to differing NGP fund utilization, physiography, and decentralized-governance "
        "capacity, but does not formally isolate the institutional/governance mechanism's effect via a "
        "controlled or regression-based test."
    ),
    "source_document": "Chathukulam & Devavrathan 2014, Journal of Health Management 16(4):509-526 (retrieved via Google Drive inbox)",
    "table": "Table 4 (Total Sanitation Index by Panchayat)",
    "page": "509-526",
    "section": "Discussion and Results: Empirical Evidence and the Panchayats' Performance",
    "exact_location": "Table 4 and Figures 2-7 (composite sanitation indices by Gram Panchayat)",
    "extraction_note": (
        "Extracted from full-text PDF (retrieved via Google Drive inbox). Primary field study of "
        "sanitation coverage under India's decentralized Panchayati Raj governance structure "
        "(TSC/NGP scheme), extending the established India rural water/sanitation institutional-"
        "governance precedent (cf. Singh 2006 PRI/ARWSP). Included per INCLUSION_EXCLUSION.md criteria "
        "1-9. Not effect_sizes eligible under the strict Family A/B/C framework: a descriptive "
        "composite index across 7 Panchayats, not a regression-based point estimate/CI isolating the "
        "institutional mechanism. quantitative_synthesis_eligible in evidence_map.csv. Extracted for "
        "record_id R3C9D8DD0859C."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
rows.append(r)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
