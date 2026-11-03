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

# S965 - Nakyagaba et al - Power, politics and a poo pump, Kampala gulper technology
add("S965",
    citation="Nakyagaba GN, Lawhon M, Lwasa S, Silver J, Tumwine F (2021). Power, politics and a poo pump: Contestation over legitimacy, access and benefits of sanitation technology in Kampala. Singapore Journal of Tropical Geography.",
    doi="10.1111/sjtg.12381",
    publication_year="2021",
    country="Uganda",
    subnational_unit="Kampala",
    legal_system="common law",
    urban_rural="urban",
    service_provider="registered small private-entrepreneur businesses (gulper operators) trained by NGO Water for People, regulated by Kampala Capital City Authority (KCCA), coordinated through the Kampala Water and Sanitation Forum",
    regulatory_model="Ethnographic/interview-based study (21-household follow-along participant observation, 2-month participant observation of gulper operators, in-depth interviews with KCCA, NWSC, Water for People and community leaders, 2017-2018) of the introduction and legitimization of the 'gulper' pit-emptying pump technology in Kampala, tracing KCCA's initial criminalization and later regulatory accommodation of gulper operators, the creation of the Kampala Water and Sanitation Forum to formalize sludge-transport permits and treatment-plant access, and the role of Local Council leaders in mediating community adoption",
    population="households and gulper-pump sanitation-service operators in Kampala informal settlements (Kawempe and other divisions)",
    sample_size="21-household follow-along participant observation; 2-month participant observation of gulper operators from 2 pit-emptying companies; in-depth interviews with households, operators, institutions and community leaders",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE", fees="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE",
    effect_measure="ethnographic/interview-based case study of regulatory legitimization and institutional accommodation of an informal sanitation technology",
    effect_estimate="KCCA initially criminalized gulper pit-emptying operators as 'manual emptying' subject to police apprehension; following NGO (Water for People) engagement demonstrating the technology's suitability for dense informal settlements (portability, lower cost, solid-waste removal capacity relative to septic trucks charging USD 50-100 per pit versus USD 5-7 per 200L barrel for the gulper), KCCA created the Kampala Water and Sanitation Forum (2016) which secured operators legal permits to transport sludge and access to the public sewage treatment plant (previously requiring costly transfer-tank fees that made a 1,000L transfer cost USD 6 versus USD 2 at the treatment plant directly); this regulatory legitimization directly expanded low-income households' effective access to affordable pit-emptying sanitation services, though local council leaders' use of threats of KCCA enforcement action to coerce adoption, and unresolved gender-conditionality disputes in donor funding, complicate the equity of the resulting access.",
    study_design="ethnographic case study with follow-along participant observation, operator participant observation, and in-depth interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original ethnographic case study directly tracing a specific regulatory-legitimization process (KCCA's shift from criminalization to permitted, coordinated accommodation of gulper technology) to expanded and more affordable household sanitation-service access.",
    source_document="Nakyagaba et al 2021, Singapore Journal of Tropical Geography (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established regulatory-legitimization/informal-technology inclusion precedent: original ethnographic case study directly linking a municipal regulatory-accommodation process to expanded household sanitation access. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R4D48C6031F04.",
    )

# S966 - Jimenez, Mtango & Cairncross - local government sanitation promotion, Tanzania
add("S966",
    citation="Jimenez A, Mtango FF, Cairncross S (2014). What role for local government in sanitation promotion? Lessons from Tanzania. Water Policy.",
    doi="10.2166/wp.2014.203",
    publication_year="2014",
    country="Tanzania",
    subnational_unit="six districts across three regions",
    legal_system="common law",
    urban_rural="rural",
    service_provider="district councils (local government authorities) under the Prime Minister's Office for Regional Administration and Local Government (PMO-RALG), implementing the National Sanitation Campaign under the 2011 draft Sanitation and Hygiene Policy",
    regulatory_model="Problem-driven governance and political economy analysis (PGPE) methodology applying structural, institutional and stakeholder variable analysis to the district-council-level implementation of Tanzania's National Sanitation Campaign (NSC), examining planning, budgeting, coordination, implementation and monitoring functions against the 1998 decentralization-by-devolution policy and its fiscal/accountability limitations",
    population="rural households in six districts, targeted for the National Sanitation Campaign's 100,000-household first-year rollout across 42 districts nationally",
    sample_size="81 interviews/group discussions across 3 regions, 6 districts, 9 wards and 15 villages",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", procedural_steps="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE",
    effect_measure="problem-driven governance and political economy analysis (PGPE) of local-government institutional capacity and budget allocation",
    effect_estimate="Tanzania's National Sanitation Campaign devolved direct implementation responsibility to district councils under a decentralization policy that, despite formal devolution, retains roughly 90% of local government spending as centrally directed intergovernmental transfers with rigid project-based budgeting; district health departments showed strong ownership and commitment to sanitation promotion (a marked improvement over prior programs), but per-household budgets received were only 4.5-5 USD against a planned 10 USD target, funds arrived 6 months into the fiscal year, and critical downstream activities (village follow-up committees, mason training/supply support) received minimal or no budget/training, resulting in only a marginal (~10%) increase in sanitation coverage in a predecessor pilot with no detectable reduction in open defecation despite significant awareness gains; the study demonstrates that the specific institutional design of decentralized implementation -- not merely the existence of decentralization policy -- determines whether local government capacity translates into household sanitation-access gains.",
    table="Table 2 (functions at each government level in the NSC)",
    study_design="problem-driven governance and political economy analysis (PGPE) with document review and semi-structured interviews across national, regional, district, ward and village levels",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original PGPE institutional analysis directly tracing decentralization policy design and district-council budget/capacity constraints to household sanitation-coverage outcomes, citing quantified predecessor-program impact evaluation results.",
    source_document="Jimenez, Mtango & Cairncross 2014, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established local-government institutional-capacity inclusion precedent (Monney Ghana; Obeta Nigeria): original PGPE analysis directly linking decentralization policy design and local-government budget/capacity constraints to sanitation-coverage outcomes. NOT effect_sizes eligible: qualitative institutional analysis citing a separate predecessor impact evaluation's summary statistic, not this study's own regression estimate. Extracted for record_id R4D32E3F3E2E3.",
    )

# S967 - Balazs & Lubell - Social learning, environmental justice, IRWM, California
add("S967",
    citation="Balazs CL, Lubell M (2014). Social learning in an environmental justice context: a case study of integrated regional water management. Water Policy.",
    doi="10.2166/wp.2014.101",
    publication_year="2014",
    country="United States",
    subnational_unit="Kings Basin, California",
    legal_system="common law",
    urban_rural="both",
    service_provider="Kings Basin Water Authority, under California's Integrated Regional Water Management (IRWM) program and the Disadvantaged Community (DAC) Pilot Project Study authorized by California Water Code Section 79505.5",
    regulatory_model="Case study (interviews, focus groups, survey) of the Kings Basin Water Authority's Disadvantaged Community Pilot Project Study, examining how the California Water Code's statutory definition and mandated outreach requirements for 'disadvantaged communities' in regional water planning generate social learning among state, local and community stakeholders, and how that learning affects procedural and distributive justice in water governance outcomes",
    population="disadvantaged communities (median household income below 80% of state median, per Cal. Water Code Section 79505.5(a)) in the Kings Basin region of California",
    sample_size="interviews, focus groups, and survey of stakeholders participating in the Kings Basin DAC Pilot Project Study",
    household_level="FALSE", community_level="TRUE",
    eligibility="TRUE", legal_status="TRUE", participation="TRUE", bureaucratic_assistance="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="interview, focus-group and survey-based case study of statutorily mandated stakeholder participation and social learning",
    effect_estimate="California's statutory requirement (Water Code Section 79505.5) that Integrated Regional Water Management planning identify and involve disadvantaged communities produced short- and medium-term social learning effects -- increased information access, broadened stakeholder participation, and initial foundations for structural changes to water governance among both DAC representatives and government/regional agency staff -- but long-term structural change to IRWM institutions remained, at best, in early phases at the time of study; the study demonstrates that a specific statutory participation mandate can catalyze institutional learning that begins to link procedural inclusion to distributive water-access equity for disadvantaged communities, though the transformation of formal water-governance structures lags behind the participatory gains.",
    study_design="case study with interviews, focus groups and stakeholder survey",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original interview/focus-group/survey case study directly tracing a specific statutory participation mandate to social-learning and nascent institutional-change outcomes for disadvantaged-community water access, though without a quantified comparative access estimate.",
    source_document="Balazs & Lubell 2014, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original case study directly linking a specific California statutory participation mandate (Water Code Section 79505.5) to institutional-learning and water-governance-equity outcomes for disadvantaged communities. NOT effect_sizes eligible: qualitative interview/focus-group/survey case study, no regression-based estimate. Extracted for record_id RA32AC23D7C25.",
    )

# S968 - Lea - Housing for Health, Indigenous Australia
add("S968",
    citation="Lea T (2008). Housing for Health in Indigenous Australia: Driving Change when Research and Policy are Part of the Problem. Human Organization.",
    doi="10.17730/humo.67.1.62v54527u037t604",
    publication_year="2008",
    country="Australia",
    subnational_unit="Pipalyatjara, South Australia; remote Northern Territory Aboriginal communities",
    legal_system="common law",
    urban_rural="rural",
    service_provider="state and territory Water Authorities and public housing agencies, funding fragmented across departments with no single agency responsible for infrastructure maintenance",
    regulatory_model="Anthropological fieldwork and documentary/interview analysis of the 'Housing for Health' program's applied empirical methodology for testing and fixing household health-hardware (water supply, sanitation, electricity) functionality in remote Aboriginal communities, tracing the institutional/bureaucratic resistance encountered -- including a Water Authority's explicit written refusal to install a community water meter -- against racially stereotyped assumptions attributing infrastructure failure to Aboriginal 'vandalism' or wastefulness rather than construction/maintenance defects",
    population="residents of remote Aboriginal communities in South Australia and the Northern Territory, Australia",
    sample_size="one-year empirical trial in Pipalyatjara testing nine 'Healthy Living Practices' across housing hardware; interviews with program founders (Paul Pholeros, Paul Torzillo, Stephan Rainow)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", discretion_accommodation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="ethnographic/documentary case study of infrastructure-maintenance institutional fragmentation and bureaucratic racial bias",
    effect_estimate="Empirical testing found that 80% of health-hardware failures (water supply, sanitation, electrical systems) in the studied Aboriginal communities were due to faulty initial construction and lack of supervision (e.g., unconnected septic tanks, drainpipes leading nowhere), with only one documented case of vandalism found across the fieldwork, directly refuting the prevailing government/bureaucratic assumption that infrastructure failure resulted from Aboriginal residents' vandalism or wastefulness; the responsible Water Authority formally refused, in writing, to install a community water meter to measure actual usage, citing an unexamined assumption that Aboriginal residents wasted water by leaving taps running, when subsequent data-collection efforts proved actual per-capita water use was only about one-quarter of Sydney's; further, no single government department held funding responsibility for infrastructure maintenance, leaving essential water/sanitation hardware in remote communities to deteriorate absent routine repair programs, demonstrating that institutional fragmentation of funding responsibility combined with racially biased bureaucratic decision-making, not household behavior, was the primary driver of water/sanitation infrastructure dysfunction.",
    study_design="ethnographic fieldwork with documentary analysis and interviews with program practitioners",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original ethnographic/documentary case study directly linking institutional funding fragmentation and documented bureaucratic racial bias (Water Authority's refusal to meter, unfounded vandalism assumptions) to water/sanitation infrastructure access failure, supported by the program's own empirical usage and construction-defect data.",
    source_document="Lea 2008, Human Organization (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established environmental-justice/discriminatory-infrastructure-denial inclusion precedent (Johnson et al Mebane NC; Carrera & Flowers Lowndes County): original case study directly linking institutional funding fragmentation and documented bureaucratic racial bias to water/sanitation infrastructure access failure for Indigenous residents. NOT effect_sizes eligible: ethnographic/documentary case study, no regression-based estimate. Extracted for record_id RA0E245C18B33.",
    )

# S969 - Njoh & Akiwumi - colonization impact on water/sanitation access, African cities
add("S969",
    citation="Njoh AJ, Akiwumi FA (2011). The impact of colonization on access to improved water and sanitation facilities in African cities. Cities.",
    doi="10.1016/j.cities.2011.04.005",
    publication_year="2011",
    country="multi-country (43 African countries)",
    subnational_unit="national (urban)",
    legal_system="mixed (civil and common law, per colonizing power)",
    urban_rural="urban",
    service_provider="varies by country; colonial-era and post-independence municipal/national water and sanitation authorities",
    regulatory_model="Cross-national quantitative study using CIA World Factbook, World Bank and national government data (2008) to test whether the duration of the colonial era and the identity of the colonizing power (British versus other) predict contemporary urban access to improved water and sanitation facilities across 43 African countries, via OLS multiple regression and chi-square/Phi-coefficient bivariate analysis",
    population="urban populations of 43 African countries",
    sample_size="43 African countries (2008 cross-national data)",
    household_level="FALSE", community_level="FALSE",
    legal_status="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="OLS regression coefficient",
    effect_estimate="ACCESS = 41.956 + 0.322*YRSCOL + 2.420*COLONIZER; the duration of the colonial era (YRSCOL) is a statistically significant positive predictor of the composite water-and-sanitation access index (b=0.322, t=4.500, p<0.000), while colonizer identity (British=1) is positively but not significantly associated (t=0.649); the model explains 34% of cross-national variance in urban water/sanitation access (Adj. R2=0.34, F=11.545, p<0.000). Bivariate chi-square analysis confirms: 87.5% of countries with a 'long' colonial duration have 'high' urban water access versus 48.1% of countries with a 'short' colonial duration (Chi-square=6.659, p=0.010, Phi=0.394); a similarly significant relationship holds for sanitation access. The authors interpret longer colonial tenure as a proxy for greater accumulated institutional/infrastructural investment (including racially motivated colonial-era water/sanitation infrastructure originally built to protect European enclaves, later expanded under demand from indigenous populations), directly and significantly predicting present-day urban water/sanitation access levels.",
    table="Table 3 (OLS regression); Table 4 (colonial duration x water access contingency table); Table 5 (colonial duration x sanitation access contingency table)",
    study_design="cross-national quantitative regression analysis, 43 African countries",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: cross-national OLS regression directly isolating the effect of a historical-institutional legal/administrative variable (colonial governance duration) on a quantified urban water/sanitation access outcome, with statistically significant results replicated via an independent bivariate chi-square test.",
    source_document="Njoh & Akiwumi 2011, Cities (retrieved via Google Drive)",
    section="Main findings",
    exact_location="Table 3, p. 457",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. EFFECT_SIZES ELIGIBLE (Family A): clean cross-national OLS regression directly isolating colonial-era institutional/administrative duration's effect on a quantified water/sanitation access index, statistically significant (p<0.000), added to effect_sizes.csv as S969. Extracted for record_id RA1C04D0EBE47.",
    )

# S970 - Terhorst, Olivera & Dwinell - Social Movements Left Governments Water Sector Latin America
add("S970",
    citation="Terhorst P, Olivera M, Dwinell A (2013). Social Movements, Left Governments, and the Limits of Water Sector Reform in Latin America's Left Turn. Latin American Perspectives.",
    doi="10.1177/0094582X13484294",
    publication_year="2013",
    country="multi-country (Uruguay, Bolivia, Ecuador)",
    subnational_unit="Cochabamba, Bolivia; national-level water sector reforms in Uruguay and Ecuador",
    legal_system="civil law",
    urban_rural="both",
    service_provider="Obras Sanitarias del Estado (Uruguay national water utility), Servicio Municipal de Agua Potable y Alcantarillado (SEMAPA, Cochabamba, Bolivia), national water ministries",
    regulatory_model="Comparative political-economy case-study analysis of water-sector legal/constitutional reforms in Uruguay, Bolivia and Ecuador during Latin America's 'left turn,' tracing the 2004 Uruguayan constitutional referendum establishing the human right to water and public ownership, Bolivia's 2000 Cochabamba water-war-driven cancellation of privatization and subsequent constitutional water-rights provisions, and Ecuador's constitutional recognition of water as a fundamental right, against the practical institutional and structural-economic limits constraining social movements' ability to achieve community control of water governance",
    population="water users and social movement participants in Uruguay, Bolivia and Ecuador",
    sample_size="comparative qualitative case-study analysis of three national water-sector reform trajectories",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="comparative political-economy case-study analysis of constitutional/legal water-rights reforms and their institutional implementation",
    effect_estimate="Despite constitutional entrenchment of the human right to water in Uruguay (2004 referendum) and Bolivia and Ecuador's 'plurinational' constitutions, and the 2000 cancellation of Cochabamba's water privatization contract following mass protest, the study finds that these formal legal victories produced only limited and contradictory material water-governance changes: in Cochabamba, the reformed public utility SEMAPA remained an ill-performing, poorly governed organization a decade after the water war despite social-movement board representation, because entrenched local elites, weak trade-union support, and continued central-government underinvestment blocked deeper institutional transformation; in Uruguay, the Frente Amplio government's corporatist-statist tradition limited citizen/union participation mechanisms created by the constitutional reform to weak consultation rather than substantive co-governance; the authors conclude that constitutional/legal recognition of water rights is a necessary but insufficient condition for improved water access and governance equity absent complementary institutional reforms addressing local political-economic power structures.",
    study_design="comparative qualitative political-economy case-study analysis of three national water-sector legal reform trajectories",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original comparative case-study analysis directly tracing specific constitutional/legal water-rights reforms and their institutional implementation gaps to persistent water-governance and access limitations across three countries.",
    source_document="Terhorst, Olivera & Dwinell 2013, Latin American Perspectives (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established constitutional/legal water-rights-reform inclusion precedent (Diaz-Cayeros Mexico; Guidi Gutierrez Bolivia governance deficit): original comparative case study directly linking constitutional water-rights reforms to their institutional implementation gaps and resulting water-access/governance limitations. NOT effect_sizes eligible: qualitative comparative case-study analysis, no regression-based estimate. Extracted for record_id RA361E2E22F9C.",
    )

# S971 - Spaling, Brouwer & Njoka - Kenya community water supply sustainability
add("S971",
    citation="Spaling H, Brouwer G, Njoka J (2014). Factors affecting the sustainability of a community water supply project in Kenya. Development in Practice.",
    doi="10.1080/09614524.2014.944485",
    publication_year="2014",
    country="Kenya",
    subnational_unit="Kisayani community, Kathyaka Location, Makueni County",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Kisayani Community Water Supply Project (community-managed, 10-member elected committee), regulated by the Water Resources Management Authority (WRMA) and Tanathi Water Services Board under Kenya's Water Act 2002",
    regulatory_model="Qualitative case study (document review, 53 semi-structured interviews with 47 households, 3 local officials, 3 water-agency representatives; 3-month field residence) examining how Kenya's 2002 Water Act -- separating water-resource management (WRMA) from water-service provision (Water Services Boards), requiring new water permits, tariffs and Water Service Provider (WSP) licensing -- interacts with a decade-old community-managed water project's declining internal governance capacity and threatened water supply, drawing on the project's original 2002 Environmental Impact Assessment sustainability baseline",
    population="over 11,000 beneficiaries of the Kisayani Community Water Supply Project, Makueni County, Kenya",
    sample_size="53 semi-structured interviews (47 households, 3 local officials, 3 water-agency representatives)",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", fees="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative case-study analysis of water-sector legal reform compliance and community institutional governance capacity",
    effect_estimate="A decade after commissioning, the Kisayani project -- serving over 11,000 people via 53km of gravity-fed pipeline -- is found to be 'at the threshold of sustainability' due to the combined effect of declining rainfall/spring flow, new competing withdrawal permits (an eighth project would nearly double total withdrawals from the shared Umani Springs source), and, critically, resistance to compliance with Kenya's 2002 Water Act: the project has not become a licensed Water Service Provider (WSP) -- a status required to retain legal control of its own infrastructure assets, as confirmed when a court dismissed the project's ownership claim on the grounds that it was not a licensed WSP -- and has declined membership in the local Water Resource Users Association (WRUA) that channels regulatory influence and capacity-building funding, out of well-founded suspicion that new permits, tariffs, and asset inspections threaten local control; meanwhile, internal governance has deteriorated (no annual meetings held for years, a disbanded financial-oversight subcommittee, an unchanged committee chairman since 1994) and inequitable individual household connections (introduced in 2005, ~250 to date) have diverted flow from shared kiosks serving the poorest users, illustrating that a project's continued household water access depends jointly on compliance with the evolving legal/regulatory framework and on internal institutional accountability, neither of which the case-study project has adequately achieved.",
    table="Table 1 (estimated withdrawals from Umani Springs by project)",
    study_design="qualitative case study with document review, semi-structured interviews, and 3-month field residence",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original case study directly tracing a specific national legal reform (Kenya's 2002 Water Act, WSP licensing and WRUA membership requirements) and its interaction with community-level institutional governance deficiencies to threatened long-term household water-access sustainability.",
    source_document="Spaling, Brouwer & Njoka 2014, Development in Practice (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established community-based water-institution/national-legal-reform-compliance inclusion precedent: original case study directly linking Kenya's Water Act 2002 regulatory framework and community governance capacity to water-supply access sustainability. NOT effect_sizes eligible: qualitative case study, no regression-based estimate. Extracted for record_id RA1626402A233.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
