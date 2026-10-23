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

# S895 - Kotsila & Saravanan - Biopolitics Gone to Shit?, Mekong Delta Vietnam
add("S895",
    citation="Kotsila P, Saravanan VS (2017). Biopolitics Gone to Shit? State Narratives versus Everyday Realities of Water and Sanitation in the Mekong Delta. World Development.",
    doi="10.1016/j.worlddev.2017.01.008",
    publication_year="2017",
    country="Vietnam",
    subnational_unit="Can Tho City, Mekong Delta",
    legal_system="civil law (socialist)",
    urban_rural="both",
    service_provider="Vietnamese state water supply and sanitation (WSS) development programs and local cadre administration",
    regulatory_model="Mixed-methods (qualitative and quantitative social/health data, 10-month fieldwork) biopolitical analysis of state WSS development-program implementation, documenting false success narratives constructed by local cadres (misleading reporting tactics, misplaced faith in technical indicators) that mask persistently unequal and problematic WSS access, using biopolitics as a governance framework to show how state narratives function as tools of governance independent of actual service outcomes",
    population="households in Can Tho City, Mekong Delta, Vietnam",
    sample_size="10-month mixed-methods fieldwork (qualitative and quantitative social and health data)",
    household_level="TRUE", community_level="TRUE",
    documentation="TRUE", discretion="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="mixed-methods biopolitical/governance-narrative analysis",
    effect_estimate="State WSS success narratives in Can Tho City -- built on misleading local-cadre reporting tactics, portrayals of rurality/poverty as backward, and misplaced faith in technical coverage indicators -- legitimize the state as a successful modernizing actor while access to sustainable, safe WSS remains highly unequal and problematic on the ground; the gap between official reported WSS coverage statistics and everyday household realities of access and disease risk demonstrates that state bureaucratic narrative-production is itself an institutional mechanism obscuring and perpetuating unequal water/sanitation access.",
    study_design="mixed-methods ethnographic/documentary fieldwork study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: 10-month original mixed-methods fieldwork directly documenting how state bureaucratic reporting/narrative practices function as a governance mechanism obscuring unequal water/sanitation access.",
    source_document="Kotsila & Saravanan 2017, World Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established bureaucratic-narrative/institutional-mechanism inclusion precedent (Truelove Delhi, Kornberg Detroit): original mixed-methods fieldwork documenting state governance narratives as a mechanism producing/masking unequal WSS access. NOT effect_sizes eligible: ethnographic/documentary analysis, no regression-based estimate. Extracted for record_id RAF4ED0F28A15.",
    )

# S896 - Crow, Swallow & Asamba - Community Organized Household Water, Kenya
add("S896",
    citation="Crow B, Swallow B, Asamba I (2012). Community Organized Household Water Increases Not Only Rural Incomes, but Also Men's Work. World Development.",
    doi="10.1016/j.worlddev.2011.08.002",
    publication_year="2012",
    country="Kenya",
    subnational_unit="Nyando basin, western Kenya",
    legal_system="common law",
    urban_rural="rural",
    service_provider="community self-organized spring-protection and piped homestead-connection systems, under Kenya's Water Act 2002 sector reform framework",
    regulatory_model="Comparative field study of seven communities in the Nyando basin, comparing water use, labor use, income and collective-action conditions across three groups: communities with protected springs and piped homestead connections; communities with protected springs but no homestead connection; and communities drawing water from unprotected springs, set against the institutional backdrop of Kenya's 1974 National Water Master Plan (unmet target of universal household connection by 2000) and the Water Act 2002 reforms",
    population="households in seven communities in the Nyando basin, western Kenya",
    sample_size="seven communities, comparative household-level field study",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", formal_connection="TRUE",
    water_access="TRUE",
    effect_measure="comparative field study with quantified water use, labor, and income outcomes",
    effect_estimate="Communities with community-organized, piped homestead water connections showed reduced women's and girls' water-collection labor and facilitated home-garden and livestock production, which together led to increased household incomes, compared to communities relying on unprotected springs or protected-but-unconnected springs; however, piped homestead connection also increased men's labor involvement in home garden and livestock activities enabled by the freed-up water access, complicating simple narratives of gendered benefit; the study situates these findings against Kenya's persistent national failure (since the 1974 Water Master Plan) to achieve widespread household water connection despite the 2002 Water Act reforms.",
    study_design="comparative field study across seven communities",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: comparative field study directly measuring differential outcomes (labor, income, water use) by household formal-connection status against Kenya's national water-access legal/institutional framework.",
    source_document="Crow, Swallow & Asamba 2012, World Development (retrieved via Google Drive)",
    section="Introduction; Results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established household-connection-status inclusion precedent (S882 Mason Philippines): comparative field study directly measuring outcomes by formal water-connection status under a national legal reform framework. NOT effect_sizes eligible: comparative case-study design, no regression-based estimate isolating the mechanism. Extracted for record_id RB1BD766758CF.",
    )

# S897 - Whittington - Possible Adverse Effects of Increasing Block Water Tariffs
add("S897",
    citation="Whittington D (1992). Possible Adverse Effects of Increasing Block Water Tariffs in Developing Countries. Economic Development and Cultural Change.",
    doi="10.1086/452001",
    publication_year="1992",
    country="Ghana",
    subnational_unit="Kumasi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Ghana municipal water utility, increasing block tariff (IBT) rate structure",
    regulatory_model="Household survey (November 1989, World Bank research project) and regression analysis of Kumasi's increasing block water tariff (IBT) rate structure, examining how the tariff design -- intended to protect low-income households via a low-cost 'lifeline' initial block -- interacts with shared/unmetered water connections common in dense low-income housing to produce regressive outcomes, in which poorer households sharing a single metered connection with many other households pay a higher average price per unit than wealthier households in low-density buildings",
    population="households in Kumasi, Ghana (89% tenants, high-density shared-connection housing)",
    sample_size="household survey sample (November 1989); regression analysis of 72 households sharing metered connections equally",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", formal_connection="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="regression analysis of average water price on number of households sharing a connection",
    effect_estimate="Regression of average price paid per gallon of water on the number of households sharing a single metered connection in a building found a positive and highly statistically significant relationship (parameter estimate 0.0006, t=6.6, p<0.0001; R2=0.38): the more households sharing a connection, the higher the average price paid per household, directly reversing the IBT structure's intended equity/lifeline-rate protection for the poor; poorer households (by three independent socioeconomic indicators) were significantly more likely to live in higher-density, more-expensive-per-unit shared-connection buildings, and the poorest group -- households buying water from neighbors by the bucket -- paid the highest average water bills of all groups studied.",
    study_design="household survey with regression analysis of administrative tariff/billing data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: household survey combined with regression analysis directly demonstrating how a specific institutional tariff-design mechanism (increasing block tariffs) produces regressive water-affordability outcomes for poorer households under shared-connection housing arrangements.",
    source_document="Whittington 1992, Economic Development and Cultural Change (retrieved via Google Drive)",
    table="Tables 2-6 (household water use/price by building size; regression results; socioeconomic status by building size; water bills by connection type)",
    section="Evidence from Kumasi, Ghana",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: household survey with regression analysis directly documenting a specific institutional tariff-design mechanism's regressive effect on water affordability for poorer households. NOT effect_sizes eligible on strict review: the regression's exposure variable (number of households sharing a connection, a housing-density characteristic) does not itself isolate the legal/institutional tariff mechanism in the Family A/B/C sense, even though the outcome (price paid under the IBT rate schedule) is institutional -- an exposure-side mismatch analogous to the Jocoy S893 precedent (Batch 177). Extracted for record_id RB0D2ED9C835F.",
    )

# S898 - Monstadt & Schramm - Toward The Networked City, Dar es Salaam
add("S898",
    citation="Monstadt J, Schramm S (2017). Toward The Networked City? Translating Technological Ideals and Planning Models in Water and Sanitation Systems in Dar es Salaam. International Journal of Urban and Regional Research.",
    doi="10.1111/1468-2427.12436",
    publication_year="2017",
    country="Tanzania",
    subnational_unit="Dar es Salaam",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Dar es Salaam Water and Sewerage Authority (DAWASA) and associated planning institutions",
    regulatory_model="Postcolonial/science-and-technology-studies field study examining the translation of the 'networked city' planning ideal into Dar es Salaam's formal water/sanitation institutions, planning documents and strategies, documenting the contradiction between formal institutional aspirations toward universal centralized network access and the hybrid, unequal arrangements that actually shape access on the ground, analyzing the negotiations over this translation and the scope for alternative urban modernities",
    population="Dar es Salaam residents across formal and informal settlement areas",
    sample_size="field study with document analysis and stakeholder interviews (German Research Foundation-funded field study)",
    household_level="TRUE", community_level="TRUE",
    documentation="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="documentary and field-based institutional/planning analysis",
    effect_estimate="While Dar es Salaam's formal institutions, planning documents and strategies reflect and reproduce the ideal of a universally networked, centralized water and sanitation system, the city's actual urban environments are shaped by hybrid technical-institutional arrangements that manifest persistent unequal access to water and sanitation services; the gap between the formal planning ideal (embedded in law, policy and utility strategy) and hybrid on-the-ground access arrangements demonstrates that the translation of a hegemonic formal planning model is itself a contested institutional process producing differentiated access outcomes.",
    study_design="documentary and field-based institutional/planning case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: field-based documentary analysis directly connecting formal institutional planning models/strategies to hybrid, unequal water/sanitation access outcomes.",
    source_document="Monstadt & Schramm 2017, IJURR (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-planning/formal-vs-hybrid-access inclusion precedent: field-based documentary analysis of formal planning institutions producing unequal water/sanitation access. NOT effect_sizes eligible: documentary/field-based institutional analysis, no regression-based estimate. Extracted for record_id RB020C12A06CA.",
    )

# S899 - Nyarko, Oduro-Kwarteng & Owusu-Antwi - Local authorities/PO partnerships, Ghana
add("S899",
    citation="Nyarko KB, Oduro-Kwarteng S, Owusu-Antwi P (2011). Local Authorities, Community and Private Operators Partnerships in Small Towns Water Service Delivery in Ghana. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2011.08.007",
    publication_year="2011",
    country="Ghana",
    subnational_unit="Bekwai, Atebubu, Mim (Brong-Ahafo/Ashanti Regions); Wenchi, Kuntenanse (controls)",
    legal_system="common law",
    urban_rural="both",
    service_provider="District Assemblies, Water and Sanitation Development Boards (WSDBs), and Private Operators (POs), under Ghana's Local Government Act 462 (1993) legal framework",
    regulatory_model="Comparative case study of five small-town piped water systems in Ghana -- three under public-private-operator management-contract partnerships and two under direct Community Ownership and Management by Water and Sanitation Development Boards (used as controls) -- examining performance under Ghana's Local Government Act 462 (1993), which legally delegates water-supply infrastructure responsibility to District Assemblies, assessing technical (unaccounted-for water, service reliability, revenue collection efficiency, financial self-sufficiency) and governance (political interference, contract-conflict, accountability-reporting) outcomes via document review, key-informant interviews, and 100 household surveys (20 per system)",
    population="households in five small towns in Ghana (Bekwai, Atebubu, Mim, Wenchi, Kuntenanse)",
    sample_size="5 case-study water systems; 100 household surveys (20 per system); key-informant interviews",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE",
    effect_measure="case-study comparison with quantified technical/governance performance indicators",
    effect_estimate="Public-private-operator (PO) managed systems showed lower unaccounted-for water and more frequent water-quality monitoring than the directly WSDB-managed control systems, consistent with private operators' profit-driven incentive to minimize losses; however, all five systems -- both PO-managed and WSDB-managed -- experienced significant political interference (WSDB dissolution after government changes, arbitrary tariff-review reversals contrary to contract provisions) under the Local Government Act 462 legal framework, and one PO contract (Mim) was cancelled entirely following unresolved contractual ambiguity over maintenance-responsibility division between the District Assembly and the private operator, illustrating how specific legal/contractual and governance-structure design features directly shape water-service-delivery performance and reliability outcomes for households.",
    study_design="comparative case study (5 water systems, household surveys, key-informant interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: comparative case-study analysis directly documenting how specific institutional governance/contract-design features under a national legal framework (Local Government Act 462) shape water-service-delivery performance and reliability.",
    source_document="Nyarko, Oduro-Kwarteng & Owusu-Antwi 2011, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    table="Tables 1-4 and Figs 4-7 (system descriptions, roles/responsibilities, performance indicators by system)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-governance/PPP-contract inclusion precedent: comparative case study directly documenting how legal/contractual and governance-structure design shapes water-service-delivery performance under a national legal framework. NOT effect_sizes eligible: case-study indicator comparison across 5 systems, no regression-based estimate. Extracted for record_id RAD75F64031CA.",
    )

# S900 - Tiwale - Materiality matters, Lilongwe Malawi
add("S900",
    citation="Tiwale S (2019). Materiality Matters: Revealing How Inequities Are Conceived and Sustained in the Networked Water Infrastructure -- The Case of Lilongwe, Malawi. Geoforum.",
    doi="10.1016/j.geoforum.2019.10.011",
    publication_year="2019",
    country="Malawi",
    subnational_unit="Lilongwe",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Lilongwe Water Board and associated centralized water-supply network institutions",
    regulatory_model="Socio-technical field study proposing and applying an 'unpacking' framework disaggregating Lilongwe's centralized water-distribution network into constituent physical elements (pipes, pumps, valves) and the institutions governing them -- norms, standards, design principles, regulations, and standard operating procedures shaping planning, design, implementation and everyday operation/maintenance -- to explain how differentiated (unequal) water-supply provision is produced and sustained within a nominally universal centralized system, revealing discriminatory engineering practices inscribed into and sustained by the network's institutional governance",
    population="Lilongwe, Malawi water-supply network users across differentiated service areas",
    sample_size="field study applying the unpacking framework to Lilongwe's water distribution network",
    household_level="FALSE", community_level="TRUE",
    documentation="TRUE", discretion="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="socio-technical field study of institutional/regulatory governance of network infrastructure",
    effect_estimate="Differentiated water-supply provisions within Lilongwe's nominally universal centralized water system are produced and sustained not only through social power relations but through the institutional governance (norms, standards, design principles, regulations, standard operating procedures) of the network's physical elements themselves, applied during planning, design, implementation and everyday operation/maintenance practices; this institutional-materiality analysis reveals engineering and regulatory practices that inscribe and sustain discriminatory water-access provisions across the city, demonstrating that formal technical/regulatory governance of infrastructure is itself a mechanism producing unequal water access, distinct from and complementary to purely social explanations (power, class, ethnicity).",
    study_design="socio-technical field study (institutional/materiality analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: field-based socio-technical analysis directly documenting how formal institutional governance (norms, standards, regulations, SOPs) of network infrastructure produces differentiated water-access outcomes.",
    source_document="Tiwale 2019, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-materiality/regulatory-governance inclusion precedent: field-based analysis directly documenting how formal institutional governance of network infrastructure produces differentiated water-access outcomes. NOT effect_sizes eligible: socio-technical field analysis, no regression-based estimate. Extracted for record_id RACB833F0F26E.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
