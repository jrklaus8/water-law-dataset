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

# S1069 -- Bond 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1069",
    "citation": "Bond P (2012). South African People Power since the mid-1980s: two steps forward, one back. Third World Quarterly 33(2):243-264.",
    "doi": "10.1080/01436597.2012.666011",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Johannesburg (Soweto, Orange Farm), other townships",
    "legal_system": "common law (South Africa)",
    "urban_rural": "urban",
    "service_provider": "Johannesburg Water",
    "regulatory_model": "Free Basic Water policy; prepaid water metering; convex-block tariff structure",
    "population": "township/urban poor residents, South Africa",
    "sample_size": "national/city-level political-historical analysis",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
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
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "political-historical case study",
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
        "High: documents Johannesburg Water's Free Basic Water policy (nominally 6,000 "
        "litres/household/month free) whose sharply convex second-tier tariff block "
        "disproportionately burdened poor households using more than 6,000 litres/month "
        "(the second block price rose 32% versus <10% overall in one period), while "
        "wealthy high-volume users faced a flat rate after 40 kilolitres with minimal "
        "increases; documents mass water disconnections (officially affecting 1.5 million "
        "people/year), prepaid-meter rollout beginning in Orange Farm sparking the Orange "
        "Farm Crisis Water Committee, and a documented infant death directly linked to a "
        "water cutoff in Amersfoort."
    ),
    "source_document": "Bond 2012 (retrieved via Google Drive)",
    "page": "243-264",
    "table": "",
    "figure": "",
    "section": "Water tariff and disconnection sections",
    "exact_location": "Throughout, especially the Free Basic Water tariff-design and disconnection discussion",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism (Free "
        "Basic Water tariff design, prepaid metering, disconnection enforcement) study "
        "with extensively documented differential water-access/affordability outcomes for "
        "the poor. Political-historical case study, no regression-based effect size; not "
        "added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1070 -- Ducrot & Bourblanc 2017
r = blank_row(fieldnames)
r.update({
    "study_id": "S1070",
    "citation": "Ducrot R, Bourblanc M (2017). Promoting equity in water access: the limits of fairness of a rural water programme in semi-arid Mozambique. Natural Resources Forum 41(3):131-144.",
    "doi": "10.1111/1477-8947.12128",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Mozambique",
    "subnational_unit": "a semi-arid district",
    "legal_system": "civil law (Mozambique)",
    "urban_rural": "rural",
    "service_provider": "rural water and sanitation programme",
    "regulatory_model": "pro-poor equity strategy in rural water-program design, planning, and implementation",
    "population": "rural households, semi-arid Mozambique",
    "sample_size": "case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
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
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative case study",
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
        "Moderate: examines contradictions in the conceptualization of equity in the "
        "design, planning and implementation of a rural water and sanitation programme "
        "in semi-arid Mozambique, finding that even an explicitly pro-poor strategy can "
        "fall short of delivering genuine equity, and that overlooking local perceptions "
        "of equity has a direct impact on communities' ability to maintain their water "
        "points -- underlining the gap between institutional design intent and delivered "
        "access outcomes."
    ),
    "source_document": "Ducrot & Bourblanc 2017 (retrieved via Google Drive)",
    "page": "131-144",
    "table": "",
    "figure": "",
    "section": "Equity considerations in programme design, planning and implementation",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-design "
        "mechanism study directly examining a rural water-access program's equity "
        "outcomes. Qualitative case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1071 -- Galaz 2004
r = blank_row(fieldnames)
r.update({
    "study_id": "S1071",
    "citation": "Galaz V (2004). Stealing from the Poor? Game Theory and the Politics of Water Markets in Chile. Environmental Politics 13(2):414-437.",
    "doi": "10.1080/0964401042000209649",
    "publication_year": "2004",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Chile",
    "subnational_unit": "national",
    "legal_system": "civil law (Chile)",
    "urban_rural": "both",
    "service_provider": "tradable water-rights market participants",
    "regulatory_model": "Chilean Water Code tradable water-rights market",
    "population": "underprivileged/poor water-rights holders, Chile",
    "sample_size": "game-theoretic model combined with empirical evidence",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
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
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "game-theoretic model (not a statistical regression)",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "game theory",
    "study_design": "theoretical/game-theoretic model combined with empirical case evidence",
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
        "Moderate: using game theory combined with empirical evidence, argues that the "
        "introduction of Chile's tradable water-rights market (a legal institution "
        "promoted by the World Bank as a scarcity-management model) has created 'an "
        "obvious incentive to violate the water rights of underprivileged users,' "
        "contradicting official claims that the market's negative social consequences "
        "have been limited -- documenting a legal/institutional mechanism (water-rights "
        "trading) with a theorized and empirically-supported differential risk to poor "
        "water-rights holders."
    ),
    "source_document": "Galaz 2004 (retrieved via Google Drive)",
    "page": "414-437",
    "table": "",
    "figure": "",
    "section": "Game-theoretic model and empirical evidence on water-rights violation incentives",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism "
        "(tradable water-rights market) study directly documenting differential water-"
        "access/rights-security risk for poor water users. Game-theoretic/empirical "
        "study, not a regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1072 -- Shandra, Shandra & London 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1072",
    "citation": "Shandra CL, Shandra JM, London B (2012). The International Monetary Fund, Structural Adjustment, and Infant Mortality: A Cross-National Analysis of Sub-Saharan Africa. Journal of Poverty 16(2):194-219.",
    "doi": "10.1080/10875549.2012.667059",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (30 Sub-Saharan African nations)",
    "subnational_unit": "national",
    "legal_system": "mixed (multi-country, Sub-Saharan Africa)",
    "urban_rural": "both",
    "service_provider": "national governments under IMF structural-adjustment conditionality",
    "regulatory_model": "IMF structural adjustment programs",
    "population": "national populations, 30 Sub-Saharan African countries",
    "sample_size": "30 nations, 1990-2005 (panel)",
    "household_level": "",
    "community_level": "",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
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
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "two-way fixed-effects regression coefficients",
    "effect_estimate": "Higher levels of IMF structural adjustment correspond with higher infant mortality in Sub-Saharan Africa; this effect operates indirectly via multiple mediating pathways including access to an improved water and sanitation source (along with HIV prevalence, female educational attainment, debt service, foreign investment, international trade, and GNP per capita). Specific numeric coefficient for the structural-adjustment-to-water/sanitation-access mediation path was not extracted from the available text.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "30 nations, 1990-2005",
    "adjusted_or_unadjusted": "adjusted (multiple mediating covariates)",
    "covariates": "HIV prevalence, female educational attainment, debt service, foreign investment, international trade, GNP per capita",
    "model_type": "two-way fixed-effects regression (mediation analysis)",
    "study_design": "quantitative cross-national panel regression study",
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
        "Moderate: rigorous cross-national fixed-effects regression finds IMF structural "
        "adjustment increases infant mortality in Sub-Saharan Africa, with access to an "
        "improved water and sanitation source confirmed as one of several statistically "
        "supported mediating pathways of this effect (alongside HIV prevalence, female "
        "education, debt service, foreign investment, trade, and GNP per capita) -- water/"
        "sanitation access is a mediator in a broader health-outcome model, not the sole "
        "or primary dependent variable."
    ),
    "source_document": "Shandra, Shandra & London 2012 (retrieved via Google Drive)",
    "page": "194-219",
    "table": "",
    "figure": "",
    "section": "Results: mediation pathways of IMF structural adjustment's effect on infant mortality",
    "exact_location": "Results section",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/economic-policy mechanism "
        "(IMF structural adjustment conditionality) study documenting water/sanitation "
        "access as one of several confirmed mediating pathways to a health outcome. NOT "
        "added to effect_sizes.csv: water/sanitation access is a mediating variable in a "
        "multi-path model for infant mortality (the study's primary outcome), and the "
        "specific structural-adjustment-to-water-access path coefficient was not "
        "extractable from available text, so this does not cleanly satisfy the strict "
        "Family A/B/C requirement of a regression directly isolating a mechanism's effect "
        "on a water-access outcome specifically."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1073 -- Birkenholtz 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1073",
    "citation": "Birkenholtz T (2010). 'Full-cost recovery': producing differentiated water collection practices and responses to centralized water networks in Jaipur, India. Environment and Planning A 42(9):2238-2253.",
    "doi": "10.1068/a4366",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Jaipur, Rajasthan",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "Jaipur public water-supply utility; private water-tanker vendors",
    "regulatory_model": "'full-cost-recovery' reform of a centralized urban water-supply network",
    "population": "households in six Jaipur neighborhoods stratified by class",
    "sample_size": "2007 household survey (six neighborhoods); follow-up interviews 2007 and 2009",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
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
    "procedural_steps": "",
    "delay": "TRUE",
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
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "six Jaipur neighborhoods stratified by class",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "political-ecological mixed-methods case study (household survey, interviews)",
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
        "High: documents that the transformation of Jaipur's centralized water-supply "
        "network into a full-cost-recovery system, combined with spatially uneven network "
        "expansion and intermittent flow, produces class-differentiated adaptive "
        "responses (waiting on water, private tubewell construction, private water-"
        "tanker purchases) that are exacerbating disparities in access to drinking water; "
        "also finds the reform has left the public utility unable to actually recover "
        "costs, undermining the reform's own stated rationale."
    ),
    "source_document": "Birkenholtz 2010 (retrieved via Google Drive)",
    "page": "2238-2253",
    "table": "",
    "figure": "",
    "section": "Findings on differentiated water-collection practices by class",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative "
        "mechanism (full-cost-recovery tariff reform) study with documented class-"
        "differentiated water-access outcomes. Mixed-methods case study, no regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
