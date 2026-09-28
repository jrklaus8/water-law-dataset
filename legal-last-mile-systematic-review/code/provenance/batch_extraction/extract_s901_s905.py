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

# S901 - Larrain - Human Rights and Market Rules in Chile's Water Conflicts
add("S901",
    citation="Larrain S (2012). Human Rights and Market Rules in Chile's Water Conflicts: A Call for Structural Changes in Water Policy. Environmental Justice.",
    doi="10.1089/env.2011.0020",
    publication_year="2012",
    country="Chile",
    subnational_unit="national (Antofagasta, Atacama, Bio-Bio and other regions)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="privatized regional water/sewage companies (ESVAL, EMOS/Aguas Andinas, ESSBIO and others), operating under the 1981 Water Code and 1980 Constitution Article 24",
    regulatory_model="Documentary and statistical policy analysis of Chile's 1981 Water Code (enacted by the military regime, granting unlimited, free, perpetual and freely tradeable water rights) and the 1980 Political Constitution's Article 24 property-rights protection of water rights, tracing the concentration of water ownership among mining/energy/agribusiness sectors and the subsequent privatization of potable water and sewage utilities (1998-2000) to transnational corporations, documenting before/after rate increases and service-coverage statistics using Superintendency of Sanitary Services (SISS) administrative data",
    population="Chilean water-service utility customers, nationally",
    sample_size="national administrative/regulatory data (SISS), 1989-2008",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quality="TRUE",
    effect_measure="documentary/statistical policy analysis with administrative before/after comparison",
    effect_estimate="Following privatization of Chile's regional water utilities (1998-2000) under the 1981 Water Code's market-based legal framework, drinking-water and sewage rates rose from US$0.18/m3 (1989) to US$0.78/m3 (1998, pre-privatization) and then to US$1.10-2.60/m3 across regions post-privatization, an increase of up to 400% in some areas, while national drinking-water coverage barely changed (99.3% in 1998 to 99.8% in 2008) and sewage coverage rose modestly (91.6% to 95.3%), demonstrating that the legal/institutional privatization framework produced substantial rate increases without commensurate coverage-expansion gains, with private water companies achieving 14-33% annual returns on assets during the same period.",
    table="Tables 1-4 (water rights concentration, utility ownership, coverage 1998-2008, company profit rates 2005-2008)",
    study_design="documentary/statistical policy analysis of administrative regulatory data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary analysis directly linking Chile's 1981 Water Code/1980 Constitution legal framework and subsequent utility-privatization decisions to quantified before/after rate and coverage outcomes using official regulatory administrative data.",
    source_document="Larrain 2012, Environmental Justice (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-privatization/legal-framework inclusion precedent (S886 Brown Tanzania, S884 Estache & Grifell-Tatje Mali): documentary/statistical analysis directly linking a national water-rights legal code and utility-privatization framework to quantified rate/coverage outcomes. NOT effect_sizes eligible: descriptive before/after administrative-data comparison, no regression-based estimate isolating the mechanism. Extracted for record_id RABD874ECDC9D.",
    )

# S902 - Avidar - Half-hearted Devolution, Kenya
add("S902",
    citation="Avidar O (2018). Half-hearted Devolution: A view of Kenya's water governance from Siaya County, Kenya. The Journal of the Middle East and Africa.",
    doi="10.1080/21520844.2018.1528421",
    publication_year="2018",
    country="Kenya",
    subnational_unit="Siaya County",
    legal_system="common law",
    urban_rural="both",
    service_provider="Siaya County government water-governance institutions, under Kenya's 2010 Constitution devolution framework and Water Acts 2002/2016",
    regulatory_model="Mixed-methods documentary and field study (two field trips, July 2017-February 2018) analyzing Kenya's 2010 constitutional devolution reform and the Water Acts of 2002 and 2016, examining how devolution and compliance with the 2016 Water Act have functioned on the ground in Siaya County, documenting open-structured stakeholder interviews and direct observation of water-governance institutions to assess whether devolution legislation has translated into improved sustainable water access",
    population="Siaya County residents and water-governance stakeholders, Kenya",
    sample_size="documentary analysis plus open-structured interviews and field observation across two field trips",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="mixed-methods documentary and field study",
    effect_estimate="Kenya's 2010 constitutional devolution reform and the Water Act 2016 legal framework, intended to transfer water-governance authority and resources to county-level institutions, have produced inadequate governance and a host of implementation problems in Siaya County, with the transition to devolution and compliance with the 2016 Act failing to translate into meaningfully improved sustainable water access for local populations, demonstrating a gap between formal devolution legislation and actual on-the-ground institutional capacity and water-access outcomes.",
    study_design="mixed-methods documentary and field study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: mixed-methods documentary analysis combined with field interviews and observation directly connecting Kenya's constitutional devolution and Water Act legal framework to county-level water-access governance outcomes.",
    source_document="Avidar 2018, The Journal of the Middle East and Africa (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established devolution/legal-framework inclusion precedent: mixed-methods documentary and field analysis of a specific constitutional/statutory devolution reform's water-access implementation outcomes. NOT effect_sizes eligible: documentary/field study, no regression-based estimate. Extracted for record_id RAF5FDD222D54.",
    )

# S903 - Allison - Balancing responsibility for sanitation, Cape Town
add("S903",
    citation="Allison MC (2002). Balancing responsibility for sanitation. Social Science & Medicine.",
    doi="10.1016/S0277-9536(01)00286-6",
    publication_year="2002",
    country="South Africa",
    subnational_unit="Cape Town",
    legal_system="common law",
    urban_rural="urban",
    service_provider="local government and community-based organizations (CBOs), within South Africa's post-apartheid bill-of-rights legal framework (right to a healthy living environment)",
    regulatory_model="Multiple-case study (embedded design, two CBOs, October 1996-March 1997) examining the extent of shared/joint responsibility between local government and community-based organizations for sanitation provision in Cape Town, applying a four-dimensional governance framework (political, institutional, technical, cultural) set against South Africa's constitutional bill-of-rights guarantee of a healthy living environment, identifying institutional and technical capacity, political will and cultural diversity as factors shaping the rights/responsibility balance",
    population="residents of two Cape Town communities served by community-based sanitation organizations",
    sample_size="multiple-case study of 2 CBOs (embedded design)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="multiple-case study with governance-framework analysis",
    effect_estimate="The extent of shared responsibility between local government and community-based organizations for sanitation provision in Cape Town was found to be shaped by institutional and technical capacity, political will and cultural diversity, set against the backdrop of South Africa's constitutional right to a healthy living environment; where institutional frameworks for joint responsibility were weak or unclear, community-based organizations bore disproportionate and often under-resourced responsibility for sanitation provision, demonstrating that formal governance/rights-framework design directly shapes the practical distribution of sanitation-service responsibility and, by extension, access outcomes for residents.",
    study_design="multiple-case study (embedded design, 2 CBOs)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: multiple-case-study analysis directly documenting how a constitutional rights framework and governance-responsibility arrangements shape sanitation-service provision and access.",
    source_document="Allison 2002, Social Science & Medicine (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established governance-framework/constitutional-rights inclusion precedent: multiple-case study directly documenting how governance-responsibility arrangements under a constitutional rights framework shape sanitation access. NOT effect_sizes eligible: qualitative multiple-case study, no regression-based estimate. Extracted for record_id RAAA3E8CD5A17.",
    )

# S904 - Wahby - Urban informality and the state, Cairo
add("S904",
    citation="Wahby NM (2021). Urban informality and the state: Repairing Cairo's waters through Gehood Zateya. Environment and Planning E: Nature and Space.",
    doi="10.1177/25148486211025262",
    publication_year="2021",
    country="Egypt",
    subnational_unit="Cairo",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Egyptian state water utility and informal community/individual repair practices (gehood zateya), amid a transition to water privatization",
    regulatory_model="Two-case-study ethnographic analysis of water governance and infrastructure repair in Cairo, examining how the state's hegemonic legal/institutional control over water governance is contested and supplemented by informal individual and community repair practices (gehood zateya) that cross boundaries of class, legality and space, comparing a marginalized informal settlement (where residents maintain state relations through community water systems and 'cultures of repair') against elite/middle-class gated communities (which rely on 'private governance' schemes), set against Cairo's transition toward water privatization",
    population="residents of an informal settlement and a gated community, Cairo",
    sample_size="two-case-study ethnographic fieldwork",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="two-case-study ethnographic institutional analysis",
    effect_estimate="Water access and infrastructure repair in Cairo operate through a plurality of formal state and informal (gehood zateya) practices that vary sharply by socioeconomic status and legal standing: residents of marginalized informal areas maintain water access primarily through community-organized self-repair and negotiated relations with the state, while elite/middle-class residents in gated communities access privately-governed, more reliable water infrastructure through networks of privilege, demonstrating that the state's formal water-governance legal authority is unevenly experienced and supplemented by class-stratified informal/private governance arrangements amid an ongoing transition to water privatization.",
    study_design="two-case-study ethnographic institutional analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: two-case-study ethnographic fieldwork directly documenting how formal state water-governance authority and informal/private repair practices jointly and unevenly shape water access across socioeconomic groups.",
    source_document="Wahby 2021, Environment and Planning E (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established state/informal-governance inclusion precedent: two-case-study ethnographic fieldwork directly documenting how formal and informal water-governance arrangements produce class-stratified access outcomes. NOT effect_sizes eligible: ethnographic case-study analysis, no regression-based estimate. Extracted for record_id RA88CE2AB8E94.",
    )

# S905 - Akumuntu, Wehn, Mulenga & Brdanovic - Enabling sustainable FSM, Kigali
add("S905",
    citation="Akumuntu JB, Wehn U, Mulenga M, Brdanovic D (2017). Enabling the sustainable Faecal Sludge Management service delivery chain -- A case study of dense settlements in Kigali, Rwanda. International Journal of Hygiene and Environmental Health.",
    doi="10.1016/j.ijheh.2017.05.001",
    publication_year="2017",
    country="Rwanda",
    subnational_unit="Kigali",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Rwanda Water & Sanitation Corporation (WASAC) and relevant government sanitation institutions",
    regulatory_model="Case study applying the normative 'FSM enabling environment' governance framework to gather empirical evidence from densely populated low-income settlements of Kigali, examining current fecal sludge management (FSM) practices and the extent to which government institutional conditions (bylaws, government focus, staff turnover, institutional responsibilities) enable or hinder sustainable FSM, identifying specific institutional constraints including limited government focus on the sanitation sector, high government-staff turnover, absence of pit-sludge management from sanitation project agendas, non-pro-poor-oriented bylaws, and unclear institutional responsibilities",
    population="residents of densely populated low-income settlements, Kigali, Rwanda",
    sample_size="case-study empirical evidence gathering (stakeholder perceptions) in Kigali's dense settlements",
    household_level="TRUE", community_level="TRUE",
    documentation="TRUE", institutional_fragmentation="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="case study with normative institutional 'enabling environment' framework analysis",
    effect_estimate="Sustainable fecal sludge management (FSM) in Kigali's dense low-income settlements is directly constrained by specific government institutional deficiencies -- limited government focus on the sanitation sector, high staff turnover in relevant government institutions, the absence of pit-sludge management from the sanitation policy agenda, existing bylaws that are not pro-poor oriented, and a lack of clear institutional responsibilities among actors in the FSM service-delivery chain -- demonstrating that specific, identifiable institutional/regulatory governance gaps, rather than purely technical or market factors, are a primary driver of inadequate sanitation-service access for residents of dense low-income urban settlements.",
    study_design="case study with normative institutional-governance-framework analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: case study directly documenting specific government institutional/regulatory deficiencies (bylaws, staff turnover, unclear responsibilities) constraining sanitation-service access in dense low-income settlements.",
    source_document="Akumuntu, Wehn, Mulenga & Brdanovic 2017, IJHEH (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: case study directly documenting specific government institutional/regulatory deficiencies constraining sanitation-service access, distinguished from the excluded Frenoux/Tsitsikalis Cambodia FSM paper (RA8A5580EBB31, this batch) by its central institutional/governance-enabling-environment framing rather than private-market-efficiency framing. NOT effect_sizes eligible: case-study institutional analysis, no regression-based estimate. Extracted for record_id RA78F7A82EE77.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
