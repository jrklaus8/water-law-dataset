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

# S826 - Anand - PoliTechnics of Water Supply, Mumbai
add("S826",
    citation="Anand N (2011). PRESSURE: The PoliTechnics of Water Supply in Mumbai. Cultural Anthropology.",
    doi="10.1111/j.1548-1360.2011.01111.x",
    publication_year="2011",
    country="India",
    subnational_unit="Mumbai",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Mumbai Municipal Corporation water department",
    regulatory_model="22 months of ethnographic fieldwork in a northern Mumbai settlement and the city water department's field offices, documenting the city's formal water-connection eligibility policy (a politically-mediated cutoff date of January 1995: structures built before that date are formally eligible for water connections, while structures built after obtain access through forged ration cards, informal negotiation, and 'federations' of residents formally registered for group connections), and the discretionary, socially- and politically-mediated ('hydraulic citizenship') ways that settlers actually access water despite formal ineligibility",
    population="settlers in informal settlements comprising 60% of Mumbai's population",
    sample_size="22 months of ethnographic fieldwork (interviews, participant observation with settlers and water department engineers)",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    eligibility="TRUE", documentation="TRUE", discretion="TRUE", discretion_accommodation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="ethnographic case study (interviews, participant observation)",
    effect_estimate="Mumbai's water department applies a formal eligibility rule restricting legal water connections to settlements existing before a January 1995 cutoff date; settlers in later, formally 'unauthorized' structures nonetheless obtain water through forged ration cards, informal negotiation with engineers, and department-sanctioned 'federations of 15 [households]' group-connection arrangements; department officials confirm that eligibility is not limited by ability to pay (\"the slum dwellers are good paymasters\") or utility financial capacity, but by politically-mediated cutoff dates, physical topography, and discretionary departmental practice -- what the author terms 'hydraulic citizenship,' access to the city produced through social and material claims to water infrastructure rather than formal legal entitlement alone",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: extended ethnographic fieldwork with both settlers and water-department officials directly documenting a specific formal eligibility rule (1995 cutoff date), its systematic circumvention via forged documentation and discretionary departmental accommodation, and the resulting informal-but-tolerated access regime.",
    source_document="Anand 2011, Cultural Anthropology (retrieved via Google Drive)",
    section="Introduction; hydraulic citizenship framework",
    exact_location="Opening interview with Patkar and subsequent analysis",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: extended ethnographic study directly documenting a specific formal legal eligibility rule (1995 settlement cutoff date) for water connections, its systematic circumvention (forged ration cards, discretionary departmental accommodation), and the resulting 'hydraulic citizenship' access regime. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R7D0B0BE35E0D.",
    )

# S827 - Schnegg & Kiaka - Namibia CBM water governance
add("S827",
    citation="Schnegg M, Kiaka RD (2019). The economic value of water: The contradictions and consequences of a prominent development model in Namibia. Economic Anthropology.",
    doi="10.1002/sea2.12152",
    publication_year="2019",
    country="Namibia",
    subnational_unit="rural pastoral communities, northwestern Namibia (Kunene region)",
    legal_system="common law (post-apartheid)",
    urban_rural="rural",
    service_provider="communal water-point committees, Ministry of Agriculture, Water, and Forestry",
    regulatory_model="Ethnographic study tracing Namibia's post-independence institutional transformation of rural water governance from state-maintained (colonial-era, effectively free) infrastructure to Community-Based Management (CBM), under which the government transferred financial and management responsibility for boreholes/pumps/reservoirs to local water-point committees and introduced water pricing as an economic good, examining the resulting conflicts, committee dissolutions, and contradictions between the CBM model's promised sustainability/empowerment outcomes and its actual effects",
    population="pastoral communities in rural, arid Namibia dependent on communal groundwater points",
    sample_size="ethnographic fieldwork including direct observation of a government-community CBM handover meeting and community member interviews",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE", discretion="TRUE", political_coordination="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="ethnographic case study (fieldnotes, participant observation, interviews)",
    effect_estimate="Namibia's post-1990s policy shift transferring financial/management responsibility for rural water infrastructure to local Community-Based Management committees, framed internationally as a sustainability and empowerment 'win-win,' instead produced a 'win-lose' outcome in observed pastoral communities: water-point committees dissolved due to conflicts over money, debts, and management burdens (one community's committee was defunct at the time of a government field visit, with the community continuing to self-repair infrastructure without formal governance structure), and treating water as an economic/priced good made it 'the most conflict-ridden social field throughout rural Namibia'",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: direct ethnographic observation of a specific institutional policy transfer (Community-Based Management devolving water infrastructure responsibility with pricing) and documented resulting community-level institutional breakdown (committee dissolution) and conflict.",
    source_document="Schnegg & Kiaka 2019, Economic Anthropology (retrieved via Google Drive)",
    section="Introduction; the Grootvlakte case",
    exact_location="Opening vignette and subsequent analysis",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: ethnographic case study directly documenting a specific rural water-governance institutional reform (CBM devolution with pricing) and its resulting community-level institutional breakdown. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R7ECF02CF6B42.",
    )

# S828 - dos Santos, Gupta, Pouw & Schwartz - Brazil WatSan inclusive development
add("S828",
    citation="dos Santos R, Gupta J, Pouw NRM, Schwartz K (2019). Public water supply and sanitation policies and inclusive development of the urban poor in Brazil. Water Policy.",
    doi="10.2166/wp.2019.025",
    publication_year="2019",
    country="Brazil",
    subnational_unit="national (comparison of two national WatSan laws)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="national/municipal water and sanitation service providers under Brazilian WatSan law",
    regulatory_model="Policy discourse analysis developing and applying a six-indicator Inclusive Development (ID) framework (access to minimum WSS; access to WSS even without formal housing; domestic wastewater collection/treatment; water availability; participation; WSS subsidies for low-income people) to compare Brazil's current and previous national water supply and sanitation (WatSan) laws, assessing whether formal-housing/tenure requirements and other legal-design features enable or block urban-poor access to formal WSS",
    population="urban poor in Brazil, particularly those without formal housing tenure",
    sample_size="comparative policy-text analysis of two national WatSan laws using a six-indicator framework",
    household_level="", community_level="TRUE", tenure_status="TRUE",
    tenure="TRUE", legal_status="TRUE", documentation="TRUE", participation="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="comparative policy discourse analysis using an original six-indicator framework",
    effect_estimate="Comparison of Brazil's current and previous WatSan laws shows the current law scores higher on Inclusive Development than the previous one, but both laws neglect key social, environmental, and relational ID dimensions, including specifically whether the urban poor can access formal WSS even when they lack formal housing tenure -- a legal design gap identified as a structural barrier (alongside institutional, technical, and financial barriers) to urban-poor WSS access",
    study_design="comparative policy/legal-text discourse analysis with an original analytical framework",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: original comparative analysis of two national WatSan laws' formal legal provisions (or absence thereof) for extending service access to residents lacking formal housing tenure, using a purpose-built indicator framework, though the analysis is of legal text/policy design rather than observed outcomes.",
    source_document="dos Santos, Gupta, Pouw & Schwartz 2019, Water Policy (retrieved via Google Drive)",
    table="Indicator framework table",
    section="Introduction; comparison of the two Brazilian WatSan laws",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original comparative legal/policy-text analysis of two national WatSan laws specifically examining formal-housing-tenure requirements as a legal-design barrier to urban-poor water/sanitation access. NOT effect_sizes eligible: policy discourse analysis, no regression-based estimate. Extracted for record_id R7FBDF527DD60.",
    )

# S829 - Wutich, Brewis, York & Stotts - cross-cultural justice in water institutions
add("S829",
    citation="Wutich A, Brewis A, York AM, Stotts R (2013). Rules, Norms, and Injustice: A Cross-Cultural Study of Perceptions of Justice in Water Institutions. Society & Natural Resources.",
    doi="10.1080/08941920.2012.723302",
    publication_year="2013",
    country="Bolivia; Fiji; United States (Arizona); New Zealand",
    subnational_unit="four community field sites",
    legal_system="mixed (civil law Bolivia, common law US/Fiji/New Zealand)",
    urban_rural="both",
    service_provider="local water institutions (varying by site: municipal, communal, and informal)",
    regulatory_model="Cross-cultural qualitative analysis of 135 ethnographic interviews in Bolivia, Fiji, Arizona, and New Zealand, testing for shared conceptions of institutional justice (distributive, procedural, and interactional) in water access and allocation, and examining how political-ecological factors (resource scarcity, development status) shape perceptions of institutional rules versus norms as sources of water injustice",
    population="water users across four community sites with varying water scarcity and development status",
    sample_size="135 ethnographic interviews across four sites",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", discretion="TRUE", participation="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="cross-cultural qualitative interview analysis (135 interviews)",
    effect_estimate="Institutional rules were a common concern in justice evaluations of water access across all four sites, but institutional norms were a prominent justice concern only in the Bolivia site, where water-access problems were most acute; distributive and procedural justice concerns were widely shared across sites, while interactional justice concerns were salient only in Bolivia, suggesting that resource scarcity and development-status conditions shape which dimensions of institutional (in)justice communities emphasize in evaluating water access",
    study_design="cross-cultural qualitative interview study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: systematic cross-cultural qualitative analysis of 135 interviews directly examining how institutional rules and norms shape water-access-related justice perceptions across four sites varying in scarcity and development status.",
    source_document="Wutich, Brewis, York & Stotts 2013, Society & Natural Resources (retrieved via Google Drive)",
    section="Results: institutional rules, norms, and justice dimensions across sites",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: systematic cross-cultural qualitative study (135 interviews, 4 sites) directly examining institutional rules and norms as determinants of water-access justice perceptions. NOT effect_sizes eligible: qualitative cross-cultural interview study, no regression-based estimate. Extracted for record_id R7F994C395052.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
