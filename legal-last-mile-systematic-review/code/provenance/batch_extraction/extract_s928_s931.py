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

# S928 - Golooba-Mutebi - public/private/community water provision Rwanda & Uganda
add("S928",
    citation="Golooba-Mutebi F (2012). In Search of the Right Formula: Public, Private and Community-Driven Provision of Safe Water in Rwanda and Uganda. Public Administration and Development.",
    doi="10.1002/pad.1638",
    publication_year="2012",
    country="Rwanda; Uganda",
    subnational_unit="Nyamagabe district, Rwanda; Masaka district, Uganda",
    legal_system="mixed (civil and common law jurisdictions)",
    urban_rural="rural",
    service_provider="decentralized district/sector local governments contracting private operators and engaging community structures for rural safe-water provision, under each country's respective decentralization and public-private-partnership legal frameworks",
    regulatory_model="5-6 month ethnographic fieldwork (participant/non-participant observation, formal and informal interviews, document review) comparing rural water-service delivery arenas in Masaka district, Uganda and Nyamagabe district, Rwanda, examining how decentralization and public-private partnerships mediate water provision between the decentralized state and communities, and identifying the institutional determinants (vertical/horizontal coordination, inspection, supervision, accountability-enforcement mechanisms) of effective service delivery",
    population="rural households in Masaka district, Uganda and Nyamagabe district, Rwanda",
    sample_size="two-district comparative ethnographic fieldwork (6 study areas, multiple villages)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE", political_coordination="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="comparative ethnographic fieldwork analysis",
    effect_estimate="Across both Rwanda and Uganda, decentralization and the introduction of private contractors to mediate between the decentralized state and communities in rural water provision did not by themselves resolve maladministration and service-delivery failures; the analysis demonstrates that effective public water-goods provision instead depends on the strength of vertical and horizontal institutional coordination, inspection and supervision capacity, and accountability-enforcement mechanisms, with Rwanda's Nyamagabe district (benefiting from strong performance-contract accountability structures between district mayors and the presidency) outperforming Uganda's Masaka district in translating decentralization and privatization into reliable rural water service.",
    study_design="comparative ethnographic fieldwork (two-district, cross-country)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original multi-month ethnographic fieldwork directly documenting how specific decentralization and public-private-partnership institutional arrangements determine rural water-service delivery outcomes across two countries.",
    source_document="Golooba-Mutebi 2012, Public Administration and Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-narrative/comparative-fieldwork inclusion precedent (Kotsila & Saravanan; Nyarko Ghana PPP): original multi-month fieldwork directly documenting how decentralization/PPP institutional arrangements and accountability mechanisms determine rural water-access outcomes. NOT effect_sizes eligible: qualitative comparative ethnographic case study, no regression-based estimate. Extracted for record_id R7EE9044E5204.",
    )

# S929 - Obeta - Rural water supply in Nigeria: policy gaps
add("S929",
    citation="Obeta MC (2018). Rural water supply in Nigeria: policy-gaps and future directions. Water Policy.",
    doi="10.2166/wp.2018.129",
    publication_year="2018",
    country="Nigeria",
    subnational_unit="nationwide (rural communities)",
    legal_system="common law",
    urban_rural="rural",
    service_provider="community-based service providers and government water-supply agencies operating under Nigeria's rural water-sector policy and institutional framework",
    regulatory_model="Investigative/qualitative study using primary data (interviews/consultations with prior workers and agencies in the sector) and secondary data to characterize the rural water-supply landscape in Nigeria and identify the policy-gaps constraining community-based service providers and the weak institutional framework underlying widespread rural water-supply-scheme failure",
    population="rural communities across Nigeria served or unserved by rural water-supply schemes",
    sample_size="investigative qualitative study drawing on primary and secondary data from sector workers/agencies",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_continuity="TRUE",
    effect_measure="qualitative investigative/policy-gap analysis",
    effect_estimate="The study identifies a weak institutional framework as the central driver of Nigeria's high rate of rural water-supply-scheme failure, characterizing multiple, mutually reinforcing policy-gaps constraining community-based service providers (unclear institutional responsibility, weak coordination among the large array of water-sector agencies, inadequate community-management support); the paper concludes that sustainable rural water-supply outcomes require simultaneously addressing these institutional policy-gaps rather than any single factor in isolation, since addressing individual gaps alone has not resolved chronic scheme failure in the country.",
    study_design="qualitative investigative study with primary and secondary data collection",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original qualitative investigation (interviews with sector workers/agencies) directly linking institutional/policy-gap characteristics to rural water-supply-scheme failure and sustainability outcomes, though without a quantified comparative estimate.",
    source_document="Obeta 2018, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-policy-gap inclusion precedent (national rural water-sector institutional-strengthening studies): original qualitative investigation directly linking institutional/policy weaknesses to rural water-access sustainability outcomes. NOT effect_sizes eligible: qualitative investigative study, no regression-based estimate. Extracted for record_id R7EE2F2CC79B7.",
    )

# S930 - Diaz-Cayeros, Magaloni & Ruiz-Euler - traditional governance Oaxaca Mexico
add("S930",
    citation="Diaz-Cayeros A, Magaloni B, Ruiz-Euler A (2014). Traditional Governance, Citizen Engagement, and Local Public Goods: Evidence from Mexico. World Development.",
    doi="10.1016/j.worlddev.2013.01.008",
    publication_year="2014",
    country="Mexico",
    subnational_unit="Oaxaca state municipalities",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="indigenous municipalities governed under usos y costumbres (traditional customary-law participatory governance, given full legal standing by a 1995 Oaxaca state reform) versus municipalities governed by political-party representative democracy",
    regulatory_model="Kernel-density propensity-score-matching quasi-experimental design (matching on municipal characteristics and long-term settlement patterns to address selection, plus first-differences analysis) estimating the average treatment effect on the treated (ATT) of choosing usos y costumbres traditional governance (versus party-based governance) on municipal public-goods provision, including sewerage, water, and electricity access, following the 1995 constitutional reform granting usos full legal status in Oaxaca",
    population="Oaxaca state municipal households, 1990-2010",
    sample_size="418 treated / 146 control municipalities over common support (kernel matching)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", participation="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="kernel-density propensity-score matching, average treatment effect on the treated (ATT)",
    effect_estimate="Municipalities governed by usos y costumbres traditional participatory governance showed a statistically significant increase in sewerage access relative to party-governed municipalities: ATT = 0.086 (p<0.01) in levels and 9.05 percentage points (p<0.01) in rate of change for 1995-2005 (immediately following the 1995 legal reform granting usos full legal standing), with a smaller but still positive effect in 2000-10; effects on piped-water access itself were small and not statistically significant, while electricity access showed a significant positive effect in levels (0.036, p<0.1) and rate of change; the authors conclude that legal recognition of traditional participatory governance improves local public-goods provision, including sanitation infrastructure, relative to party-based representative government, operating through stronger vertical/horizontal accountability rather than authoritarian local-boss capture.",
    lower_CI="", upper_CI="", standard_error="0.034 (sewerage ATT, level, 1995-2005)",
    p_value="<0.01 (sewerage ATT, 1995-2005)",
    extraction_sample_size="418 treated / 146 control municipalities",
    adjusted_or_unadjusted="adjusted (matched on municipal characteristics and settlement patterns)",
    covariates="lag usos, fragmentation, distance to city, distance to road, indigenous population share, income, religious fragmentation, ethnic fragmentation, altitude",
    model_type="kernel-density propensity-score matching with first-differences",
    table="Table 3 (balance tests); Table 4 (ATT for public goods: water, sewerage, electricity, illiteracy)",
    study_design="quasi-experimental propensity-score-matched difference-in-differences design, municipal panel 1990-2010",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: quasi-experimental kernel-matching design directly isolating the causal effect of a specific 1995 legal reform (constitutional recognition of usos y costumbres traditional governance) on municipal sewerage/sanitation access outcomes, with matching addressing endogenous governance-choice selection.",
    source_document="Diaz-Cayeros, Magaloni & Ruiz-Euler 2014, World Development (retrieved via Google Drive)",
    section="Results; Table 4",
    exact_location="pp. 88-89",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. Genuine Family A (legal recognition/formal institutional-governance-model and access) effect_sizes candidate -- see effect_sizes.csv addition this batch (sewerage/sanitation-access outcome; the water-specific ATT itself was non-significant and is not the basis for the effect_sizes entry). Extracted for record_id R7DF2A5059A76.",
    )

# S931 - Mallick - Amplifying community voices for drinking water access, Bangladesh
add("S931",
    citation="Mallick DL (2010). Chapter 5: Amplifying the community voices for greater access to drinking water in Bangladesh. In Water Communities (Community, Environment and Disaster Risk Management, Vol. 2), Emerald Group Publishing.",
    doi="10.1108/S2040-7262(2010)0000002008",
    publication_year="2010",
    country="Bangladesh",
    subnational_unit="hard-to-reach riverine charland and coastal communities",
    legal_system="common law",
    urban_rural="rural",
    service_provider="local government institutions and development agencies, engaged through a participatory action-research and social-mobilization project connecting marginalized communities to relevant government departments under Bangladesh's national water policy framework",
    regulatory_model="Book chapter based on project documents (concept papers, progress/annual reports, thematic papers), field observations, and stakeholder consultations, documenting a participatory action-research and social-mobilization project that built local institutional links between poor, women-led, and marginalized communities in remote/hard-to-reach areas and government departments/development agencies responsible for drinking-water and sanitation service delivery, against the backdrop of Bangladesh's national water policy and weak local implementing-agency capacity",
    population="poor, women, and marginalized communities in remote riverine charland and coastal areas of Bangladesh",
    sample_size="participatory action-research project documentation and field observation across multiple project communities",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="participatory action-research project documentation and field observation",
    effect_estimate="Despite Bangladesh's national water policy articulating progressive goals for increasing the poor's access to water, weak and under-resourced local implementing institutions left remote riverine and coastal communities effectively unreached; the participatory action-research and social-mobilization project built collective community awareness of drinking-water risks (salinity, arsenic, seasonal scarcity) and established local institutional links between marginalized communities and government departments/development agencies, motivating collective local action that increased communities' access to drinking water, sanitation facilities, and health services from relevant government institutions, demonstrating that bridging the institutional gap between weak local implementing agencies and marginalized communities -- not policy design alone -- is central to translating national water-policy goals into actual household access gains.",
    study_design="participatory action-research project case documentation with field observation and stakeholder consultation",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original project-based documentation and field observation directly linking a specific community-government institutional-linkage intervention to household drinking-water and sanitation access outcomes in marginalized communities, though without a quantified comparative estimate.",
    source_document="Mallick 2010, Water Communities, Emerald Group Publishing (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-narrative/participatory-governance inclusion precedent (Kotsila & Saravanan; Wahby Cairo; Hossain Dhaka bosti): original participatory action-research project documentation directly linking a community-government institutional-linkage intervention to household water/sanitation access outcomes in marginalized communities. NOT effect_sizes eligible: qualitative project case documentation, no regression-based estimate. Extracted for record_id R7C16D234F08C.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
