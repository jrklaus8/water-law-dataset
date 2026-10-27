#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EXTR = f"{BASE}/03_extraction/extracted_data/extraction_database.csv"
TODAY = "2026-09-27"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"

with open(EXTR, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def blank_row(fieldnames):
    return {fn: "" for fn in fieldnames}

def add(sid, **kwargs):
    assert sid not in existing_ids, f"{sid} already exists"
    row = blank_row(fieldnames)
    row["study_id"] = sid
    row["researcher"] = RESEARCHER
    row["date_extracted"] = TODAY
    row["peer_reviewed"] = "TRUE"
    row["publication_type"] = "journal article"
    row["language"] = "English"
    row["evidence_status"] = "OBSERVED"
    row.update(kwargs)
    rows.append(row)

# S830 - Silva - Connectivity of Infrastructure Networks, Sao Paulo
add("S830",
    citation="Silva RT (2000). The Connectivity of Infrastructure Networks and the Urban Space of Sao Paulo in the 1990s. International Journal of Urban and Regional Research.",
    publication_year="2000",
    country="Brazil",
    subnational_unit="Sao Paulo metropolitan area",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="SABESP and municipal/state utility structures, under an evolving administrative-law and re-regulation framework",
    regulatory_model="Institutional and infrastructure-coverage analysis examining how formal, near-universal connectivity to water/sewerage networks in Sao Paulo (coverage rising from 45%/20% nationally in the early 1960s to much higher levels by the 1990s) masks qualitative disparities in service regularity, quality, and social control over network outputs, tracing the historical shift from nationalized, centrally-coordinated utilities to the 1990s' emerging privatized/re-regulated framework and its disruption of Brazil's administrative-law rules governing utilities",
    population="Sao Paulo metropolitan area residents, including poor urban peripheries",
    sample_size="institutional/infrastructure-coverage analysis using historical service-coverage statistics",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE", service_reliability="TRUE",
    effect_measure="institutional/historical infrastructure-coverage analysis",
    effect_estimate="Although formal water/sewerage network coverage in Sao Paulo and Brazil generally expanded dramatically after nationalization (national coverage rising from 45%/20% to 85%/37% for water/sewerage between the early 1960s and late 1980s), apparently homogeneous formal connectivity disguises qualitative differences in service regularity, quality, and the strategic location of network outputs that determine who is genuinely included versus excluded from adequate urban infrastructure; the 1990s shift toward privatized, re-regulated utilities has in practice disrupted the established rule of administrative law governing Brazilian utilities, creating new uncertainty in the institutional framework for connectivity and access",
    study_design="institutional/historical infrastructure-coverage case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: institutional and historical analysis directly tracing formal connectivity statistics alongside the administrative-law/regulatory-framework transformation (nationalized to privatized utilities) that shapes qualitative service exclusion beneath nominal universal coverage.",
    source_document="Silva 2000, International Journal of Urban and Regional Research (retrieved via Google Drive)",
    figure="Figure 1",
    section="Institutional framework and connectivity analysis",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional/administrative-law analysis of Brazilian utility regulation transformation (nationalized to privatized) and its relationship to formal-vs-qualitative water/sewerage access exclusion in Sao Paulo. NOT effect_sizes eligible: institutional/historical case study, no regression-based estimate. Extracted for record_id R812C5CF68631.",
    )

# S831 - Madrigal, Alpizar & Schluter - Costa Rica CBDWO
add("S831",
    citation="Madrigal R, Alpizar F, Schluter A (2011). Determinants of Performance of Community-Based Drinking Water Organizations. World Development.",
    doi="10.1016/j.worlddev.2011.02.011",
    publication_year="2011",
    country="Costa Rica",
    subnational_unit="four representative rural communities",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="community-based drinking water organizations (CBDWOs), over 1,000 of which serve 60% of Costa Rica's rural population",
    regulatory_model="Comparative qualitative institutional analysis (matched, comparable case selection) of four rural community-based drinking water organizations, examining how working rules for tariff collection and infrastructure maintenance, downward accountability to users, a demand-driven approach, and attributes of water-committee members determine organizational financial health, infrastructure condition, and user satisfaction",
    population="rural Costa Rican communities served by CBDWOs",
    sample_size="4 matched representative communities (qualitative comparative case study)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE", participation="TRUE", discretion="TRUE",
    water_access="TRUE", service_quality="TRUE", service_reliability="TRUE",
    effect_measure="comparative qualitative institutional case study (4 matched communities)",
    effect_estimate="Community-based drinking water organizations with clear working rules for tariff collection and infrastructure maintenance, strong downward accountability to users (a demand-driven approach), and capable water-committee-member attributes achieved substantially better financial health, infrastructure condition, and user satisfaction than organizations lacking these institutional features, despite Costa Rica's overall high (>95%) national drinking-water coverage masking significant disparities in service quality among rural community-managed systems",
    study_design="comparative qualitative institutional case study (matched communities)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous matched comparative case-study design directly isolating specific institutional working rules (tariff collection, accountability mechanisms, committee attributes) as determinants of water-organization performance and service outcomes across four communities.",
    source_document="Madrigal, Alpizar & Schluter 2011, World Development (retrieved via Google Drive)",
    section="Comparative case analysis of four CBDWOs",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous comparative institutional case study directly isolating working-rule and accountability-mechanism determinants of community water-organization performance. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id R7FB3A3D76F81.",
    )

# S832 - O'Reilly & Dhanju - Rajasthan hybrid governance
add("S832",
    citation="O'Reilly K, Dhanju R (2012). Hybrid drinking water governance: Community participation and ongoing neoliberal reforms in rural Rajasthan, India. Geoforum.",
    doi="10.1016/j.geoforum.2011.12.001",
    publication_year="2012",
    country="India",
    subnational_unit="Churu, Hanumangarh, and Jhunjhunu districts, Rajasthan",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Government of Rajasthan water supply project ('Our Water'), village-level community participation institutions, informal small-scale private vendors",
    regulatory_model="Longitudinal ethnographic follow-up study (3 years post-completion) of a rural drinking-water project designed around hybrid neoliberal governance reforms -- decentralization, marketization (payment for water), and community participation intended to shift citizens from welfare beneficiaries to consumers able to demand accountability from the state -- tracing how payment and community participation failed to compel reliable state water provision, leading villagers to independently adopt small-scale privatization that further undermined state provision of clean water",
    population="rural villagers in Churu, Hanumangarh, and Jhunjhunu districts, Rajasthan",
    sample_size="ethnographic fieldwork, longitudinal follow-up (original 1997-2002 study plus post-completion research)",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", participation="TRUE", discretion="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="longitudinal ethnographic case study",
    effect_estimate="Payment for water and community participation, intended by the hybrid neoliberal governance design to compel the Rajasthan state to provide clean, reliable water as a matter of consumer accountability, failed to achieve this: three years after project completion, the state supply remained unreliable and delivered contaminated water, leading villagers to independently adopt small-scale privatization as a coping response, which paradoxically further undermined the state's capacity/incentive to provide clean water, illustrating the contradictory local hybridization of neoliberal water-governance reforms",
    study_design="longitudinal ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: longitudinal ethnographic research directly tracing a specific institutional governance-reform design (payment plus community participation intended to enforce state accountability) to its actual failure and the resulting shift to small-scale privatization and continued unreliable/contaminated water delivery.",
    source_document="O'Reilly & Dhanju 2012, Geoforum (retrieved via Google Drive)",
    section="Findings on post-project community participation and privatization",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: longitudinal ethnographic case study directly tracing a specific hybrid governance-reform (payment/participation-for-accountability) mechanism's failure and resulting institutional hybridization. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R8277D5F60CD4.",
    )

# S833 - Aladuwaka & Momsen - Wanaraniya Water Project, Sri Lanka
add("S833",
    citation="Aladuwaka S, Momsen J (2010). Sustainable development, water resources management and women's empowerment: the Wanaraniya Water Project in Sri Lanka. Gender & Development.",
    doi="10.1080/13552071003600026",
    publication_year="2010",
    country="Sri Lanka",
    subnational_unit="Wanaraniya Gramasewa Niladhari Division, Rattota, Matale district",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Vishaka Women's Society (community-based organization registered with the District Secretariat), with technical assistance from an NGO (Sarvodaya Rural Technical Services) and the local government Pradeshiya Sabha",
    regulatory_model="Ethnographic case study of a women-initiated, women-managed rural piped-water project, examining the formal registration of a women's society with the District Secretariat, the role and limits of local government (Pradeshiya Sabha) support, the community's own connection-fee and tariff-setting governance (requiring villager consultation and consent), and disconnection as an enforcement mechanism against non-payment",
    population="283 households (964 residents) in Wanaraniya, Rattota, Matale district",
    sample_size="ethnographic fieldwork (key informant interviews, focus groups, field observation) plus descriptive household-level data tables",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", documentation="TRUE", disconnection="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="ethnographic case study with descriptive household-level tables",
    effect_estimate="A women-run community water project, formally registered with the District Secretariat and requiring villager consultation to set connection fees (1000 rupees down-payment) and monthly water-meter-based billing, successfully brought piped water to 189 of 283 households (up from only 3 wells/streams pre-project), leading to improved sanitation (240 of 283 households gained septic toilets), health, education, and income-generating outcomes, while the women's organization retained control against attempts by local politicians and the local government (Pradeshiya Sabha) to take over the project, and used disconnection threats to enforce payment discipline",
    study_design="ethnographic case study with descriptive household-level survey tables",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary ethnographic and household-level data directly documenting a formally-registered community organization's fee-setting, billing, and disconnection-enforcement institutional mechanisms and their effect on household water/sanitation access.",
    source_document="Aladuwaka & Momsen 2010, Gender & Development (retrieved via Google Drive)",
    table="Tables 1-4",
    section="The Wanaraniya Water Project; impact on health, livelihoods, education",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: ethnographic case study with household-level data directly documenting a formally-registered community water organization's fee/billing/disconnection institutional mechanisms and household-level water/sanitation access outcomes. NOT effect_sizes eligible: ethnographic case study with descriptive tables, no regression-based estimate. Extracted for record_id R850039CA750A.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
