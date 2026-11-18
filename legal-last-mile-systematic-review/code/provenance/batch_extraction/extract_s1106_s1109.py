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

# S1106 -- Baijius & Patrick 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1106",
    "citation": "Baijius W, Patrick RJ (2019). \"We Don't Drink the Water Here\": The Reproduction of Undrinkable Water for First Nations in Canada. Water 11(5):1079.",
    "doi": "10.3390/w11051079",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Canada",
    "subnational_unit": "Canadian Prairie (multiple First Nation case studies, source water protection planning)",
    "legal_system": "common law (Canada); Indian Act statutory framework",
    "urban_rural": "rural",
    "service_provider": "federal government (Indigenous Services Canada); First Nation band water operators",
    "regulatory_model": "federal fiduciary/constitutional responsibility for on-reserve water under the Indian Act; provincial water regulation excluded from reserves",
    "population": "First Nation communities, Canadian Prairie region",
    "sample_size": "",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
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
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
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
    "effect_measure": "",
    "effect_estimate": (
        "In 2011, 30% of First Nation water systems nationally classified as high risk for "
        "contamination. In 2016, 134 water systems in 85 First Nation communities under a "
        "boil water advisory (approximately 1 in 8 communities at any one time); boil water "
        "advisories 2.5x more frequent for First Nation than non-First Nation communities; "
        "waterborne infections 26x the Canadian national average."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "political ecology case study (multiple case studies of source water protection planning)",
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
        "High: documents that colonial institutional arrangements rooted in the Indian Act "
        "(band/reserve system, federal jurisdiction over on-reserve water disconnected from "
        "provincial regulatory regimes applicable to non-First Nation communities) "
        "structurally exclude First Nations from water governance decision-making, "
        "reproducing persistent contamination risk and boil-water-advisory disparities "
        "relative to non-First Nation communities."
    ),
    "source_document": "Baijius & Patrick 2019 (retrieved via Google Drive)",
    "page": "1-18",
    "table": "",
    "figure": "",
    "section": "Introduction; Colonial water governance; Case study results; Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism case "
        "study documenting colonial jurisdictional-exclusion mechanisms affecting First "
        "Nations water access and quality. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1107 -- Katomero & Georgiadou 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1107",
    "citation": "Katomero J, Georgiadou Y (2018). The Elephant in the Room: Informality in Tanzania's Rural Waterscape. ISPRS International Journal of Geo-Information 7(11):437.",
    "doi": "10.3390/ijgi7110437",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Hai and Siha districts",
    "legal_system": "civil law (Tanzania)",
    "urban_rural": "rural",
    "service_provider": "Community Owned Water Supply Organizations (COWSOs); informal actors/grassroots associations",
    "regulatory_model": "National Water Policy decentralization framework; formal COWSO governance complemented by informal programs/sanctions",
    "population": "rural water users, Hai and Siha districts, Tanzania",
    "sample_size": "20 key informants (bureaucrats, politicians, village and religious leaders)",
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
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
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
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Qualitative case-study finding: in Hai and Siha districts, complementary "
        "interaction of formal COWSO programs with informal programs and informal "
        "sanction/reward systems (e.g., councillor personal financial contributions, "
        "grassroots-association reporting channels) is associated with superior rural "
        "water access outcomes relative to the national pattern, in which about 52% of "
        "Tanzania's rural population (21.1 million people) lacks improved water access."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional case study (semi-structured key informant interviews)",
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
        "Moderate-high: qualitative institutional-theory analysis (Helmke & Levitsky "
        "typology) of how formal and informal institutional programs and sanction/reward "
        "systems interact to shape rural water-access outcomes; not a quantitative "
        "regression-based effect but a rigorously theorized and interview-grounded "
        "institutional-mechanism case study."
    ),
    "source_document": "Katomero & Georgiadou 2018 (retrieved via Google Drive)",
    "page": "1-21",
    "table": "",
    "figure": "",
    "section": "Introduction; (In)formality theory; Case study results",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional-arrangement case study "
        "directly documenting how formal/informal institutional complementarity shapes "
        "rural water-access outcomes, tied to SDG Target 6.1. No regression-based effect "
        "size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1108 -- Patrick, Grant & Bharadwaj 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1108",
    "citation": "Patrick RJ, Grant K, Bharadwaj L (2019). Reclaiming Indigenous Planning as a Pathway to Local Water Security. Water 11(5):936.",
    "doi": "10.3390/w11050936",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Canada",
    "subnational_unit": "Muskowekwan First Nation, Treaty 4, Saskatchewan",
    "legal_system": "common law (Canada); Indian Act 1876; Constitution Act 1982",
    "urban_rural": "rural",
    "service_provider": "Muskowekwan First Nation (community-based source water protection planning); federal government",
    "regulatory_model": "federal jurisdiction over on-reserve water under the Indian Act, disconnected from provincial water-resource authority under the Constitution Act 1982",
    "population": "Muskowekwan First Nation (Saulteaux/Ojibway), population ~1800 (~500 on-reserve)",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
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
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "As of June 2018, 85 concurrent drinking/boil-water advisories on First Nation "
        "reserves nationally; approximately 1 in 7 reservations advised not to drink tap "
        "water at any time. In Saskatchewan specifically, only 74% of on-reserve homes "
        "serviced by piped community water distribution, 21% by truck delivery (prone to "
        "contamination), and the remainder by private wells -- attributable to federal/"
        "provincial jurisdictional fragmentation under the Indian Act and Constitution Act "
        "1982, which excludes reserve lands from provincial infrastructure planning."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/legal case study (community-based source water protection planning)",
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
        "High: documents that the Indian Act's 1876 reservation system created lands "
        "administratively disconnected from provincial infrastructure planning, while the "
        "Constitution Act 1982 assigns water-resource responsibility to provinces but "
        "leaves First Nations reserves under federal jurisdiction -- a jurisdictional "
        "fragmentation directly linked to the documented 74%/21%/remainder piped/truck/"
        "well service-type split for Muskowekwan First Nation and Saskatchewan reserves "
        "generally, with a five-stage community-based source-water-protection planning "
        "framework (risk-ranked contaminant table, management-action table) implemented "
        "as an institutional/self-governance response."
    ),
    "source_document": "Patrick, Grant & Bharadwaj 2019 (retrieved via Google Drive)",
    "page": "1-20",
    "table": "Table 1 (contaminant risk ranking); Table 2 (management actions/responsible agencies/funding)",
    "figure": "",
    "section": "Introduction; Indigenous water governance in Canada; Muskowekwan case study",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous jurisdictional/institutional-"
        "mechanism case study directly documenting differential water-service-type access "
        "attributable to federal/provincial governance fragmentation under the Indian Act. "
        "No regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1109 -- Jama & Mourad 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1109",
    "citation": "Jama AA, Mourad KA (2019). Water Services Sustainability: Institutional Arrangements and Shared Responsibilities. Sustainability 11(3):916.",
    "doi": "10.3390/su11030916",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Somalia",
    "subnational_unit": "Garowe, Puntland",
    "legal_system": "civil law (Somalia); Natural Water Resources Law 1984",
    "urban_rural": "urban",
    "service_provider": "Nugal Water Company (NUWACO), public-private partnership under concession with PSAWEN",
    "regulatory_model": "public-private partnership (PPP) concession arrangement between Puntland State Water and Energy (PSAWEN) and NUWACO, with overlapping/uncoordinated mandates between PSAWEN and the Ministry of Environment",
    "population": "households in seven zones of Garowe, Puntland, Somalia (population ~200,000)",
    "sample_size": "20 household interviews; 7 key informant interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
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
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Household connection fee $180; treated/untreated tap water priced ~$1.3/m3; "
        "low-income households (~$150/month) spend up to 10% of household income on "
        "drinking water versus ~5% for higher-income households ($300/month). Only 32% of "
        "the Somali population nationally has access to safe drinking water. Overlapping, "
        "uncoordinated mandates between PSAWEN and the Ministry of Environment ('nobody "
        "should believe other governmental agencies who claim water related roles') "
        "documented via 7 key-informant interviews as a driver of poor and over-priced "
        "domestic water service."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "20 households; 7 key informants",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional case study (thematic analysis of key-informant and household interviews)",
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
        "High: documents overlapping and uncoordinated statutory mandates between PSAWEN "
        "and the Ministry of Environment producing poor water-sector governance, combined "
        "with a PPP concession-based pricing structure (NUWACO) that makes water 'an "
        "economic good rather than a right that every citizen should enjoy,' directly "
        "affecting affordability for low-income households and children."
    ),
    "source_document": "Jama & Mourad 2019 (retrieved via Google Drive)",
    "page": "1-15",
    "table": "Table 1 (household water zones); Table 2 (household income/water expenditure); Table 3 (key informants)",
    "figure": "",
    "section": "Introduction; Methodology; Results and Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional-fragmentation/PPP-"
        "arrangement case study directly documenting how uncoordinated institutional "
        "mandates and a concession-based pricing structure produce differential water-"
        "affordability/access outcomes for the poor. No regression-based effect size; not "
        "added to effect_sizes.csv."
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
