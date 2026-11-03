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

# S1136 -- Ban, Das Gupta & Rao 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1136",
    "citation": "Ban R, Das Gupta M, Rao V (2010). The Political Economy of Village Sanitation in South India: Capture or Poor Information? Journal of Development Studies 46(4):685-700.",
    "doi": "10.1080/00220380903002962",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Andhra Pradesh, Karnataka, Kerala, Tamil Nadu (7 districts, 201 Gram Panchayats)",
    "legal_system": "common law (India); 73rd Constitutional Amendment (Panchayati Raj Institutions)",
    "urban_rural": "rural",
    "service_provider": "Gram Panchayats (elected village councils)",
    "regulatory_model": "constitutionally mandated local-government sanitation responsibility (PRI Act)",
    "population": "rural villages, 4 South Indian states",
    "sample_size": "5,276 villages/wards; 10,408 roads",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "linear probability model, village/block fixed effects",
    "effect_estimate": (
        "Political capture of sanitation infrastructure: roads in the Gram "
        "Panchayat head's village are significantly more likely to be paved "
        "(coef. 0.053***), have drains (0.037**), be moderately clean "
        "(0.028*) and be free of garbage (0.060***); roads where a "
        "politician resides are more likely to have drains (0.078***) and "
        "be paved (0.055***, moderately clean 0.052*). Roads inhabited by "
        "Scheduled Castes/Tribes are significantly less likely to be paved "
        "(-0.051**) and more likely to have garbage (-0.032*) than upper-"
        "caste roads, but oligarchic village structures and upper-caste "
        "land control show no significant infrastructure disadvantage. "
        "Villagers show poor awareness of GP sanitation responsibilities "
        "for garbage disposal (61%) and water-accumulation clearing (73%) "
        "specifically, versus 80-86% awareness for road/drain/water-tank "
        "tasks; sanitation ranked among the top-3 village problems in only "
        "25% of villages and as the top problem in only 5%."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "clustered at colony level (see Tables 5-6)",
    "p_value": "*10%, **5%, ***1% significance reported per coefficient",
    "extraction_sample_size": "5,276 villages/wards; 10,408 roads",
    "adjusted_or_unadjusted": "adjusted (village/block fixed effects, caste, road-length, institution controls)",
    "covariates": "literacy rate, population density, fraction SC/ST, oligarchy, upper-caste land share, GP head's/HQ village, road length, institution roadside, politician road, caste of road",
    "model_type": "linear probability model with fixed effects",
    "study_design": "quantitative regression-based institutional-mechanism study",
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
        "High: rigorous regression-based study with village- and road-level "
        "fixed effects directly isolating political capture of a "
        "constitutionally mandated local-government sanitation function as "
        "the mechanism producing differential sanitation infrastructure "
        "access, using both survey and direct-observation outcome measures."
    ),
    "source_document": "Ban, Das Gupta & Rao 2010 (retrieved via Google Drive)",
    "page": "685-700",
    "table": "Tables 1-6",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based "
        "institutional-mechanism study directly isolating political capture's "
        "effect on differential sanitation-infrastructure access. Added to "
        "effect_sizes.csv as Family C (administrative/legal barriers/access "
        "inequality)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1137 -- Shah et al 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1137",
    "citation": "Shah G, Joshi A, Prasad P, Chettiparamb A, Sekher M, Kumar M, Singh L, Samanta G, Mathur N (2010). The Globalizing State, Public Services and the New Governance of Urban Local Communities in India: A Colloquium. Vikalpa 35(1):75-104.",
    "doi": "",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Gujarat, Rajasthan, Andhra Pradesh, Kerala, Orissa, West Bengal (paired cities per state)",
    "legal_system": "common law (India); 74th Constitutional Amendment",
    "urban_rural": "urban",
    "service_provider": "Municipal Corporations; special-purpose vehicles; private/NGO contractors under PPP",
    "regulatory_model": "post-liberalization urban governance reform (decentralization, outsourcing, PPP, JNNURM/RUIDP central schemes)",
    "population": "urban residents, incl. slum populations, 6 Indian states",
    "sample_size": "field research, 12 paired cities across 6 states",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
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
    "procedural_steps": "",
    "delay": "",
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
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Cross-city comparisons document sharply differential sanitation "
        "outcomes tied to governance-reform capacity: in Surat (Gujarat), "
        "slum-dweller access to public toilets rose from 20% (1991) to "
        "97% (2006) under a well-resourced, accountable, decentralized "
        "reform model with private-sector collaboration; in Junagadh "
        "(Gujarat), drainage/sewage infrastructure has been unchanged "
        "since the 1930s, with the District Collector finding the "
        "municipality had failed to provide even 'primary facilities' as "
        "of 2001. In Rajasthan, sanitation service delegation to Urban "
        "Local Bodies under the 74th Amendment remained largely "
        "unimplemented over a decade, with 88% of 156 surveyed towns/"
        "cities lacking door-to-door solid-waste collection. In Andhra "
        "Pradesh, outsourcing/contractorization of sanitation to Resident "
        "Welfare Associations led to fund embezzlement and underpaid, "
        "overworked sanitation workers, with new governance systems found "
        "to 'discriminate against the poor and focus more on the richer "
        "parts of cities.'"
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "12 paired cities, 6 states",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "multi-jurisdiction qualitative institutional comparative case study",
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
        "Moderate-high: rigorous multi-jurisdiction field-research "
        "comparison directly documenting how differing governance-reform/"
        "outsourcing institutional models (well-resourced/accountable vs. "
        "under-resourced/unmonitored) produce differential sanitation-"
        "access outcomes for the urban poor across six Indian states."
    ),
    "source_document": "Shah et al. 2010 (retrieved via Google Drive)",
    "page": "75-104",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous multi-jurisdiction "
        "institutional-mechanism comparative case study of governance-reform "
        "models' differential effect on sanitation access. No regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1138 -- Habich-Sobiegalla 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1138",
    "citation": "Habich-Sobiegalla S (2018). How Do Central Control Mechanisms Impact Local Water Governance in China? The Case of Yunnan Province. The China Quarterly, 1-19.",
    "doi": "10.1017/S0305741018000450",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "China",
    "subnational_unit": "Yunnan province (2 counties: 'Wild Grass' and 'West Mountain')",
    "legal_system": "civil law (China); central-local administrative fiscal transfer system",
    "urban_rural": "mixed",
    "service_provider": "county/provincial Water Resources Bureaus (WRBs)",
    "regulatory_model": "'project mechanism' (xiangmu zhi) -- competitive earmarked-fund allocation for water infrastructure",
    "population": "residents of two Yunnan counties differing in economic development",
    "sample_size": "65 interviews, 2011-2014",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
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
    "affordability": "",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": (
        "The project mechanism requires local water bureaus to compete for "
        "earmarked central/provincial funding via a bureaucratic application "
        "process; localities with strong personal ties to provincial "
        "officials and prior track records of successful applications "
        "(Wild Grass) received disproportionate funding (824 million yuan "
        "in water-infrastructure grants within 9 months of a 2011 central "
        "policy document, a 45% increase) and early notice of funding "
        "calls, while a poorer, more dispersed-population county (West "
        "Mountain) with weaker bureaucratic ties struggled to gain project "
        "approval (only 2 of 10 applications succeeded) and lacked the "
        "matching funds required to qualify, despite comparably low water "
        "utilization ratios (3.4% for the shared prefecture vs. 16% "
        "national average)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "2 counties, 65 interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional/administrative-mechanism case study",
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
        "Moderate-high: rigorous comparative interview-based case study "
        "directly documenting an administrative funding-allocation "
        "institutional mechanism's effect on differential water-"
        "infrastructure access between two comparable counties."
    ),
    "source_document": "Habich-Sobiegalla 2018 (retrieved via Google Drive)",
    "page": "1-19",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/"
        "administrative-mechanism case study of a funding-allocation "
        "institution's differential effect on water access. No regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1139 -- Kazora & Mourad 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1139",
    "citation": "Kazora AS, Mourad KA (2018). Assessing the Sustainability of Decentralized Wastewater Treatment Systems in Rwanda. Sustainability 10(12):4617.",
    "doi": "10.3390/su10124617",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Rwanda",
    "subnational_unit": "Kigali (4 sampling sites, 19 semicentralized sewerage systems)",
    "legal_system": "civil law (Rwanda); absence of a national sanitation law (in formulation)",
    "urban_rural": "urban",
    "service_provider": "estate developers; WASAC (Water and Sanitation Corporation); business owners",
    "regulatory_model": "semicentralized sewerage systems (SCSSs) assessed against national sanitation policy/regulations/law",
    "population": "urban estate residents and businesses, Kigali",
    "sample_size": "17 DWWT plant sites; 19 recognized collective sewage treatment plants",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
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
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "0-10 multi-criteria sustainability scoring system",
    "effect_estimate": (
        "Sustainability assessment across technical, socioeconomic, "
        "environmental, legal and institutional dimensions finds legal and "
        "institutional dimensions among the weakest (average 3.87-4.1/10, "
        "'Less Sustainable'): Sanitation Law scored only 1.33/10 "
        "(implementers) and 1.2/10 (policy-makers/regulators) because no "
        "enforceable sanitation law yet exists in Rwanda (one was 'under "
        "formulation' at time of study); Sanitation Policy scored 4.13-"
        "4.76/10; Institutional Framework scored 4.1-4.78/10, reflecting "
        "weak accountability for mismanagement/failures and inconsistent "
        "inter-agency collaboration among WASAC, MININFRA, REMA, RURA and "
        "MoH. Technical (3.77/10) and socioeconomic (3.53/10) dimensions "
        "were also 'Less Sustainable,' while environmental quality scored "
        "higher (5.75/10). The paper concludes the absence of sustainable "
        "legal instruments for planning, developing and managing SCSSs "
        "will cause operational failure and less-supportive institutional "
        "frameworks going forward."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "4 sampling sites, 19 SCSSs",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "multi-criteria weighted scoring assessment",
    "study_design": "mixed-methods institutional/legal sustainability assessment",
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
        "Moderate: rigorous mixed-methods multi-criteria assessment "
        "explicitly scoring a legal/institutional dimension and "
        "documenting how the absence of an enforceable sanitation law and "
        "weak institutional collaboration undermine sustainable sanitation-"
        "service delivery; scoring system is not a regression isolating a "
        "single mechanism's causal effect."
    ),
    "source_document": "Kazora & Mourad 2018 (retrieved via Google Drive)",
    "page": "1-15",
    "table": "Tables 1-5",
    "figure": "Figures 3-5",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-"
        "mechanism sustainability assessment documenting legal-instrument "
        "and institutional-framework gaps undermining sanitation-service "
        "sustainability. Not regression-based (multi-criteria weighted "
        "scoring, not a coefficient isolating a mechanism's causal effect), "
        "so per ANALYSIS_PLAN.md Family A/B/C framework does not qualify "
        "for effect_sizes.csv; not added."
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
