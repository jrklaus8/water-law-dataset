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

# S1130 -- Rahaman, Everett & Neu 2007
r = blank_row(fieldnames)
r.update({
    "study_id": "S1130",
    "citation": "Rahaman AS, Everett J, Neu D (2007). Accounting and the move to privatize water services in Africa. Accounting, Auditing & Accountability Journal 20(5):637-670.",
    "doi": "10.1108/09513570710778992",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "national (Ghana Water Company)",
    "legal_system": "common law (Ghana); World Bank/IMF lending conditionality",
    "urban_rural": "urban",
    "service_provider": "Ghana Water Company (GWC); proposed private lease operators",
    "regulatory_model": "proposed public-private-partnership/lease privatization; full-cost-recovery tariff mechanism",
    "population": "Ghanaian water consumers; policy-making stakeholders",
    "sample_size": "34 interviews; 2,300+ pages archival documents",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
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
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Documents how accounting technologies, vocabularies and experts were "
        "enlisted by the World Bank and Ghanaian Government (1994 Bank staff "
        "appraisal report; 1995-2003 privatization debate) to define GWC's "
        "'poor performance' and justify a 10-year lease privatization with an "
        "automatic tariff-adjustment mechanism, and how the Coalition Against "
        "the Privatization of Water (CAPW) contested the accounting numbers "
        "(e.g., inclusion of uncontrollable foreign-exchange losses) used to "
        "justify the reform; only about 35% of the Ghanaian population had "
        "access to potable water at the time of the 1995 assessment."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "34 interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "governmentality/institutional-sociology policy-process case study",
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
        "Moderate-high: rigorous archival- and interview-based documentation of "
        "the accounting and institutional mechanisms used to justify and contest "
        "a proposed market-based water-service institutional reform in Ghana."
    ),
    "source_document": "Rahaman, Everett & Neu 2007 (retrieved via Google Drive)",
    "page": "637-670",
    "table": "Table IV (GWSC financial performance 1989-1993)",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/policy-process "
        "case study of accounting mechanisms shaping a market-based water-service "
        "reform debate. No regression-based effect size directly isolating a legal/"
        "institutional mechanism's effect on a water-access outcome; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1131 -- Subramaniam 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1131",
    "citation": "Subramaniam M (2014). Neoliberalism and water rights: The case of India. Current Sociology 62(3):1-19.",
    "doi": "10.1177/0011392114523973",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Rajasthan (Alwar district, 70 villages along the Arvari river)",
    "legal_system": "common law (India); National Water Policy 1987/2002",
    "urban_rural": "rural",
    "service_provider": "Tarun Bharat Sangh (TBS, NGO); Neighborhood/village self-governance (Arvari Sansad)",
    "regulatory_model": "community self-governance/collective ownership vs. state/private commodification of water",
    "population": "village residents, Rajasthan, differentiated by caste, class, gender",
    "sample_size": "2007 water-parliament session (190 residents, 32 guests); embedded case study",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "",
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
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Documents TBS's Arvari Sansad ('water parliament'), an informal "
        "institution created after a 1996 conflict over state-issued fishing "
        "rights on a community-revived river, that governs collective water "
        "resource use and asserts residents' rights to water as common "
        "property against state/NGO commodification; participation in "
        "governance deliberations and benefits from water-harvesting "
        "structures (johads) is shown to vary systematically by caste, class "
        "and gender, with dominant upper-caste/large-landowner groups "
        "controlling discussions and disproportionately benefiting from "
        "volunteer (shramdan) labor contributed largely by lower-caste "
        "farmers and women."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "70 villages; 2007 parliament session",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative policy-document analysis and embedded institutional case study",
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
        "Moderate-high: documents a specific documented water-governance "
        "institution (Arvari Sansad) with differential participation and access "
        "outcomes by caste, class and gender, analyzed against national water "
        "policy documents."
    ),
    "source_document": "Subramaniam 2014 (retrieved via Google Drive)",
    "page": "1-19",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism "
        "case study of a documented water-governance institution with differential "
        "access implications by caste/class/gender. No regression-based effect size; "
        "not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1132 -- Manikutty 1997
r = blank_row(fieldnames)
r.update({
    "study_id": "S1132",
    "citation": "Manikutty S (1997). Community Participation: So What? Evidence from a Comparative Study of Two Rural Water Supply and Sanitation Projects in India. Development Policy Review 15:115-140.",
    "doi": "",
    "publication_year": "1997",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Kerala (8 villages/wards, 4 matched pairs)",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "Kerala Water Authority (KWA); Ward Water Committees (WWCs)",
    "regulatory_model": "community-participation institutional mechanism (WWCs) vs. no-participation standard delivery",
    "population": "rural households, Kerala",
    "sample_size": "160 households (80 per project); 2 leaders/village interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
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
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Comparative survey (n=80 per project) of otherwise-similar Dutch/"
        "Danish-assisted (Project I, with Ward Water Committees) vs. KWA-only "
        "(Project II, no community participation) rural water/sanitation "
        "schemes finds: % taps working 92% vs. 74% (p<0.01); complete "
        "switch-over to piped water for drinking 40% vs. 25%; latrine usage "
        "94% vs. 34% among households with latrines; cost recovery 25% vs. "
        "<10%; overall satisfaction 75% vs. 30%. Differences attributed to "
        "the WWC participatory-governance mechanism (transparent site "
        "selection, eligibility determination for subsidized latrines, "
        "complaint/follow-up procedures) rather than differences in capital "
        "cost (software inputs were <2% of total project cost)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "significance levels reported per outcome (0.01, 0.05, 0.10 levels) in Tables 2-5",
    "extraction_sample_size": "160 households (80 per project, 4 matched village pairs)",
    "adjusted_or_unadjusted": "unadjusted (descriptive/chi-square/t-test comparisons)",
    "covariates": "",
    "model_type": "",
    "study_design": "matched comparative case study with household survey",
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
        "High: rigorous matched comparative design directly isolating the "
        "effect of a participatory-governance institutional mechanism (WWCs) "
        "on documented water/sanitation access and service outcomes, with "
        "statistically significant differences reported."
    ),
    "source_document": "Manikutty 1997 (retrieved via Google Drive)",
    "page": "115-140",
    "table": "Tables 1-5",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional-mechanism "
        "comparative case study. Outcome comparisons are descriptive/chi-square/"
        "t-test based (not regression coefficients isolating the mechanism), so "
        "per ANALYSIS_PLAN.md Family A/B/C framework this does not qualify for "
        "effect_sizes.csv (regression-based estimate required); not added."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1133 -- McFarlane & Desai 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1133",
    "citation": "McFarlane C, Desai R (2015). Sites of entitlement: claim, negotiation and struggle in Mumbai. Environment and Urbanization 27(2):441-454.",
    "doi": "10.1177/0956247815583635",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Mumbai (Rafinagar and Khotwadi informal settlements)",
    "legal_system": "common law (India); Maharashtra Slum Areas (Improvement, Clearance and Redevelopment) Act 1971",
    "urban_rural": "urban",
    "service_provider": "Municipal Corporation of Greater Mumbai (MCGM/BMC); private toilet-block operators; CBOs",
    "regulatory_model": "notified vs. non-notified slum legal status; pre-1995-residency eligibility cutoff",
    "population": "informal-settlement residents, Mumbai",
    "sample_size": "9-month ethnographic study, 2 settlements",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
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
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": (
        "Documents that an informal settlement must be legally notified as a "
        "slum under the 1971 Act to qualify for water, toilets, streetlights "
        "and drainage; in the non-notified settlement (Rafinagar), water "
        "cannot legally be provided to residents who arrived after 1 January "
        "1995, and only an estimated 1,500 of 4,000 households can prove "
        "pre-1995 residency; a 2009 municipal 'water theft' crackdown cut "
        "both legal and illegal connections in Rafinagar/Shivajinagar. In "
        "the notified settlement (Khotwadi), even legally entitled residents "
        "face fraught, fee-paying negotiations with elected representatives "
        "to obtain shared water connections; Khotwadi has 24 toilet blocks/"
        "180 seats for ~2,000 households vs. Rafinagar's 6 blocks/76 seats "
        "for ~4,000 households."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "2 informal settlements (~2,000 and ~4,000 households)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "ethnographic institutional/legal case study",
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
        "High: rigorous ethnographic documentation of a codified legal-status "
        "eligibility mechanism (notified/non-notified slum status; pre-1995 "
        "residency cutoff) directly producing differential water/sanitation "
        "access and entitlement outcomes between two comparable settlements."
    ),
    "source_document": "McFarlane & Desai 2015 (retrieved via Google Drive)",
    "page": "441-454",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-status "
        "case study directly documenting a codified eligibility mechanism's effect "
        "on differential access. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1134 -- Das 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1134",
    "citation": "Das P (2015). The urban sanitation conundrum: what can community-managed programmes in India unravel? Environment and Urbanization 27(2):505-524.",
    "doi": "10.1177/0956247815586305",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Madhya Pradesh (Gwalior and Indore)",
    "legal_system": "common law (India); 74th Constitutional Amendment Act (decentralization)",
    "urban_rural": "urban",
    "service_provider": "municipal corporations; Community Water and Sanitation Committees (CWASC)",
    "regulatory_model": "notified-slum eligibility status; cost-recovery/user-committee community-management model",
    "population": "informal-settlement residents, Gwalior and Indore",
    "sample_size": "36 in-depth interviews; household survey n=422",
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
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "",
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
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Community Managed Sewerage Scheme access was restricted to "
        "'notified slums' that had already received the earlier Community "
        "Managed Water Supply Scheme under the same cost-recovery model. "
        "Cross-case comparison finds the CMSS unfolded very differently by "
        "socioeconomic status and local-government responsiveness: in "
        "Gwalior CMWSS settlements, 63% of households reported open "
        "defecation and only 13% were willing to pay for sewerage "
        "connections, versus 21% open defecation and 100% willingness to "
        "pay for connections in Indore's better-off CMWSS settlements; 92% "
        "of Gwalior households still held the municipal corporation "
        "responsible for service delivery vs. only 6% in Indore, where the "
        "user committee had built a stronger institutional relationship "
        "with local government (via a District Urban Development Agency "
        "community officer)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "422 households (survey); 36 in-depth interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "comparative institutional case study with household survey",
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
        "High: rigorous comparative case study directly documenting how a "
        "formal eligibility (notified-slum) and cost-recovery institutional "
        "mechanism produces sharply differential sanitation-access outcomes "
        "across two comparable city contexts."
    ),
    "source_document": "Das 2015 (retrieved via Google Drive)",
    "page": "505-524",
    "table": "Tables 1-3",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional-mechanism "
        "comparative case study of a formal eligibility/cost-recovery mechanism's "
        "differential effect on sanitation access. No regression-based effect "
        "size directly isolating the mechanism; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1135 -- Wutich 2009
r = blank_row(fieldnames)
r.update({
    "study_id": "S1135",
    "citation": "Wutich A (2009). Water Scarcity and the Sustainability of a Common Pool Resource Institution in the Urban Andes. Human Ecology 37:179-192.",
    "doi": "10.1007/s10745-009-9227-4",
    "publication_year": "2009",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Bolivia",
    "subnational_unit": "Cochabamba (Villa Israel squatter settlement)",
    "legal_system": "civil law (Bolivia)",
    "urban_rural": "urban",
    "service_provider": "community-run tapstand system (Neighborhood Council / Junta Vecinal)",
    "regulatory_model": "community-membership eligibility institution (landowner/proxy-member vs. renter status)",
    "population": "squatter-settlement households, Cochabamba",
    "sample_size": "72 households (panel survey, 5 rounds over 10 months)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
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
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "descriptive proportions; repeated-measures ANOVA; t-test",
    "effect_estimate": (
        "Only community members (53%) and proxy community members (29%, "
        "e.g., anticretico loan-collateral occupants) are formally eligible "
        "to access the community tapstand system and participate in "
        "Neighborhood Council governance; renters (18% of residents) are "
        "formally excluded from water rights and discouraged from voting, "
        "despite often being long-time residents. Across 5 seasonal survey "
        "rounds, 81-87.5% of tapstand water recipients were legitimate "
        "community members vs. 12.5-19% non-community-member free-riders "
        "(Table 4); community members' social-network size was "
        "significantly larger than non-community members' (t(55)=3.17, "
        "p=0.002), and Neighborhood Council attendance was ~85-90% "
        "community members in normal periods. During severe dry-season "
        "water scarcity, daily allotment was cut uniformly from 40 to 20 "
        "liters per household (the 'regularity' rule), applied equally "
        "across all community-member households."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "0.002 (t-test, community vs. non-community member network size); 0.009 (ANOVA, seasonal water insecurity)",
    "extraction_sample_size": "72 households, 5 seasonal survey rounds",
    "adjusted_or_unadjusted": "unadjusted (descriptive/ANOVA/t-test comparisons)",
    "covariates": "season (wet/dry/transition)",
    "model_type": "repeated-measures ANOVA; split-plot repeated-measures ANOVA; t-test",
    "study_design": "ethnographic panel-survey institutional case study",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "25% non-response at initial sampling (72/96 households)",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: rigorous panel-survey (5 rounds, 72 households) documentation "
        "of a formal community-membership eligibility institution directly "
        "determining differential water access (legitimate beneficiaries vs. "
        "excluded renters) with statistically tested seasonal variation."
    ),
    "source_document": "Wutich 2009 (retrieved via Google Drive)",
    "page": "179-192",
    "table": "Tables 1, 4-8",
    "figure": "Figures 1-4",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-"
        "eligibility-mechanism case study with quantitative (ANOVA, t-test) "
        "documentation of differential access by community-membership status. "
        "Not regression-based (ANOVA/t-test/descriptive proportions, not a "
        "regression coefficient isolating the mechanism's effect on an outcome), "
        "so per ANALYSIS_PLAN.md Family A/B/C framework does not qualify for "
        "effect_sizes.csv; not added."
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
