import csv, tempfile, os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

def blank_row():
    return {k: "" for k in fieldnames}

new_rows = []

# --- S532: Workshopping Water Justice (Cape Town), record_id RB8BD27638F17 ---
s = blank_row()
s.update(dict(
    study_id="S532",
    citation="Murray A, Meyer F, Fourie E (2023). Workshopping Water Justice: linking struggles from the Cape Flats to the rest of the Continent. Globalisation, Societies and Education, 21(5), 705-719.",
    doi="10.1080/14767724.2023.2165478",
    publication_year="2023",
    publication_type="journal article",
    language="English",
    peer_reviewed="TRUE",
    country="South Africa",
    subnational_unit="Cape Town (Cape Flats), Western Cape",
    legal_system="common law (mixed, post-apartheid constitutional)",
    urban_rural="urban",
    service_provider="City of Cape Town (CoCT), municipal water services department",
    regulatory_model=(
        "City of Cape Town water demand-management regime built around eligibility for "
        "'indigent' status (a 'difficult process' in itself, required to receive the higher "
        "350L/day free allocation via Water Management Devices rather than the standard 200L/day) "
        "combined with disconnection/flow-restriction enforcement: WMDs (2007-2021) dispensed a "
        "fixed daily volume before cutting off entirely; their 2021 replacement, a 'drip system', "
        "requires customers to self-manage usage to 15kL/month or face escalating punitive "
        "restriction (flow reduced to a 6kL/month trickle after three consecutive months over the "
        "cap, with the city manager empowered to unilaterally place a household on a prepaid meter "
        "after two such cycles), alongside a steeply regressive block tariff structure."
    ),
    population="working-class residents of Cape Town informal settlements, backyard/frontyard dwellings and formal housing, organised through the African Water Commons Collective/Housing Assembly",
    household_level="TRUE",
    community_level="TRUE",
    income_group="low-income",
    tenure_status="mixed (formal housing, backyard/frontyard informal structures, informal settlements)",
    eligibility="TRUE",
    burden="TRUE",
    discretion_accommodation="TRUE",
    enforcement="TRUE",
    documentation="TRUE",
    fees="TRUE",
    disconnection="TRUE",
    participation="TRUE",
    institutional_fragmentation="TRUE",
    water_access="TRUE",
    affordability="TRUE",
    service_continuity="TRUE",
    effect_measure="participatory-action-research/activist ethnography (decade of organising, 'revolutionary water workshops'/'water mapping' methodology) with documentary/policy analysis of municipal tariff and metering records",
    effect_estimate=(
        "Water Management Devices (installed 2007-2021) dispensed 200L/day at no charge before "
        "cutting off entirely, or 350L/day (87.5L per person per day for a modal working-class "
        "household of 4, but only 23L per person per day for the authors' documented modal "
        "household size of 15) if the household held 'indigent' status -- itself 'a difficult "
        "process' requiring registration and re-verification, bundled with a one-time arrears "
        "write-off after six months that was attractive to highly indebted households but also "
        "intensified state surveillance and criminalisation around 'indigent' status. WMDs were "
        "frequently installed improperly, without valid consent, or on the wrong property, and "
        "when they failed an 'unresponsive municipality' directed residents to sub-contractors and "
        "back again. Tariffs rose steeply and regressively: by 2017 the lowest consumption block "
        "(0-6kL, formerly free) had risen 556% while the top block saw a 104% increase, and more "
        "than two-thirds of WMDs were installed in working-class communities at the peak of the "
        "2017-2018 Day Zero crisis. In April 2021 the City of Cape Town replaced WMDs with a 'drip "
        "system': households ('Customers', not 'residents') must self-manage usage below 15kL/month "
        "(500L/day average); exceeding this for three consecutive months triggers a flow-restricting "
        "disc limiting supply to a 6kL/month trickle (the FBW minimum) for 12 months, and after two "
        "such cycles the city manager can unilaterally place the household on a prepaid meter. The "
        "authors document that 'the bureaucratic process for indigent status and exclusionary "
        "eligibility requirements remains' under the new system, framing it as a continuation rather "
        "than resolution of water-access injustice, disproportionately affecting racialised, "
        "low-income and women-headed households who perform most water-related social-reproductive "
        "labour."
    ),
    extraction_sample_size="qualitative participatory-action-research case study; decade (2014-2022) of organising across Cape Town informal settlements and formal housing communities",
    adjusted_or_unadjusted="not applicable (qualitative/documentary case study)",
    model_type="participatory-action-research ethnography with municipal policy-document analysis",
    study_design="qualitative case study (activist-academic participatory action research)",
    risk_of_bias_tool="CASP",
    selection_bias="Moderate (single city case study; authors are also the organisers/subjects of the intervention described, a reflexive activist-academic methodology)",
    measurement_bias="Low-moderate (direct organising experience over a decade, corroborated by cited municipal tariff/policy documents and prior published scholarship on Cape Town WMDs)",
    confounding="Not applicable (qualitative case-study design)",
    attrition="Not applicable",
    reporting_bias="Low (the persistence of exclusionary eligibility requirements and punitive metering under the 2021 'drip system' reform is reported directly, not minimised)",
    legal_measurement_quality="high (specific documented municipal metering policy -- WMD/FBW indigent-status rules, the 2021 domestic-metering policy's flow-restriction and prepaid-meter escalation clauses -- directly quoted from City of Cape Town policy documents)",
    outcome_measurement_quality="moderate (participatory organising experience and documentary tariff/policy analysis, not an independent household survey)",
    mechanism_certainty="2",
    source_document="Murray, Meyer & Fourie 2023, Globalisation, Societies and Education",
    section="Weapons of mass destruction; The Cape Town water crisis; Back to the future?",
    exact_location="WMD/indigent-status eligibility mechanism and 2021 drip-system flow-restriction/prepaid-meter escalation policy",
    extraction_note="record_id RB8BD27638F17.",
    researcher="Claude-AI-fulltext-2026-21",
    date_extracted="2026-09-21",
    evidence_status="OBSERVED",
))
new_rows.append(s)

# --- S533: Infrastructures of Overlordship (US farm labor camps), record_id R589F244C9832 ---
s = blank_row()
s.update(dict(
    study_id="S533",
    citation="Ghertner DA (2023). Infrastructures of Overlordship: Law, Labor Camps, and the Material Geographies of Servitude. Annals of the American Association of Geographers, 113(6), 1483-1500.",
    doi="10.1080/24694452.2023.2187340",
    publication_year="2023",
    publication_type="journal article",
    language="English",
    peer_reviewed="TRUE",
    country="United States",
    subnational_unit="New York State (rural migrant labor camps)",
    legal_system="common law (US federal/state)",
    urban_rural="rural",
    service_provider="private farm operators/labor contractors; Orange County Department of Health (OCDH) as local sanitary-code regulator; New York Sanitary Code Part 15",
    regulatory_model=(
        "Legal-geographic case-law analysis of three paradigmatic New York Unified Court System "
        "cases (1970-2018) documenting how migrant farmworker housing is excluded from ordinary "
        "tenancy protections (occupancy deemed 'incidental to employment'), how a two-tier sanitary-"
        "code enforcement regime (Part 15 of the NY Sanitary Code, requiring biannual inspection of "
        "farm labor camps for water quality, sanitation and safety) is discretionarily under-"
        "enforced by the local health authority, and how utility/water service is directly weaponised "
        "for eviction and banishment of racialised workers."
    ),
    population="migrant and racialised farmworkers housed in employer-provided labor camps, New York State",
    household_level="TRUE",
    community_level="TRUE",
    indigenous_population="FALSE",
    migrant_population="TRUE",
    tenure_status="excluded from tenancy protection (occupancy 'incidental to employment')",
    legal_status="mixed (undocumented and documented/guest-worker migrants; also historically Black domestic migrant workers)",
    eligibility="TRUE",
    discretion_accommodation="TRUE",
    enforcement="TRUE",
    documentation="TRUE",
    disconnection="TRUE",
    institutional_fragmentation="TRUE",
    water_access="TRUE",
    service_reliability="TRUE",
    service_quality="TRUE",
    effect_measure="legal-geographic case-law analysis (three paradigmatic New York Unified Court System cases, 1970-2018) supplemented by 20+ interviews with farmworker activists, farm operators, retired labor inspectors and lawyers (2020-2022)",
    effect_estimate=(
        "In Ramirez v. Orange County Department of Health (1995), the court found OCDH had "
        "systematically failed to enforce sanitary code -- 22 of 36 permitted labor camps had "
        "unabated code violations across multiple growing seasons, including drinking-water "
        "contamination, flooded wells and unmonitored/untested well chlorine residual, which the "
        "county's own assistant commissioner for environmental health characterised as a "
        "'respective condition' of migrant housing rather than a public-health hazard; despite "
        "documenting 515 code violations across the 1991-1992 seasons, the court found 'no real "
        "harm' once the plaintiffs had moved farms, leaving the underlying water/sanitation "
        "violations unremedied. In Gabriel v. Johnston's L.P. Gas Service (2016), triggered by a "
        "propane explosion in a converted, windowless farm-labor barrack that killed one worker and "
        "severely burned seven others, the court found 'no case law directly on point' regarding a "
        "propane supplier's duty to warn farmworker occupants (as opposed to the farm-owner "
        "'customer') of safety hazards, and the state's Workers' Compensation Law exclusivity "
        "provision absorbed the farm owner's documented neglect of health/safety hazards into "
        "ordinary workplace risk, precluding tenant-landlord liability for seven of nine injured "
        "workers. In Mack v. Jim-Cor (1971-1972), the new owner of a Black migrant-worker labor camp "
        "used the county health department's discretionary sanitary-code enforcement -- requested "
        "and granted the same day a rent strike began -- to declare the camp non-compliant and "
        "order eviction, then had the municipal water meter pulled and water/gas utilities shut off "
        "entirely as a direct eviction tool; a federal HUD grant that would have provided permanent "
        "replacement housing was subsequently refused by the Village of Medina, with the Urban "
        "Renewal Agency director publicly attributing the refusal to racism. Across all three cases, "
        "farmworker housing's exclusion from ordinary tenancy law and health/safety code enforcement "
        "is documented as a structural mechanism -- 'infrastructures of overlordship' -- producing "
        "systematically differentiated (racialised) standards of water, sanitation and utility "
        "access and security."
    ),
    extraction_sample_size="three paradigmatic New York Unified Court System cases (1970-2018) selected from a review of 15+ substantive cases; 20+ interviews (2020-2022)",
    adjusted_or_unadjusted="not applicable (qualitative legal-case and interview analysis)",
    model_type="legal-geographic doctrinal case-law analysis with qualitative interview corroboration",
    study_design="doctrinal/legal case-study analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    selection_bias="Moderate (three cases purposively selected from >15 reviewed for thematic fit; single US state)",
    measurement_bias="Low (direct analysis of primary court records, fire-investigation reports, and archival documentation; corroborated by 20+ stakeholder interviews)",
    confounding="Not applicable (doctrinal case-law analysis)",
    attrition="Not applicable",
    reporting_bias="Low (the racialised, structurally differentiated character of enforcement is the paper's central, explicitly argued finding, not an incidental observation)",
    legal_measurement_quality="high (specific statutory and case-law mechanisms -- NY Sanitary Code Part 15, Workers' Compensation Law exclusivity, common-law tenancy exclusion for 'incidental' farm occupancy -- directly documented from primary legal sources)",
    outcome_measurement_quality="high (direct analysis of court records, fire-investigation reports and inspection documentation, not self-report alone)",
    mechanism_certainty="1",
    source_document="Ghertner 2023, Annals of the American Association of Geographers",
    section="Incidental Risk; Coding Risk; Infrastructural Banishment",
    exact_location="Ramirez v. OCDH (1995) water-quality non-enforcement; Gabriel v. Johnston's L.P. Gas (2016) duty-to-warn/Workers' Comp exclusivity; Mack v. Jim-Cor (1971-1972) utility-shutoff eviction",
    extraction_note="record_id R589F244C9832.",
    researcher="Claude-AI-fulltext-2026-21",
    date_extracted="2026-09-21",
    evidence_status="OBSERVED",
))
new_rows.append(s)

# --- S534: Co-producing household water insecurity (rural West Bengal), record_id RE955C8795F4F ---
s = blank_row()
s.update(dict(
    study_id="S534",
    citation="Saha S, Chakma N (2026). Co-producing household water insecurity: environmental constraints, socio-economic inequalities, and local water governance in rural Puruliya, Eastern India. SN Social Sciences, 6, 371.",
    doi="10.1007/s43545-026-01660-w",
    publication_year="2026",
    publication_type="journal article",
    language="English",
    peer_reviewed="TRUE",
    country="India",
    subnational_unit="Baghmundi CD Block, Puruliya District, West Bengal",
    legal_system="common law (federal/state)",
    urban_rural="rural",
    service_provider="Public Health Engineering Department (PHED); Panchayati Raj Institutions (Gram Panchayat); Village Water and Sanitation Committees; Jal Jeevan Mission (national programme)",
    regulatory_model=(
        "Multi-level rural drinking-water governance chain (household/village -> Gram Panchayat -> "
        "Block administration -> PHED) in which infrastructure requests are assessed for technical "
        "feasibility, fund availability and departmental approval, producing documented delays, "
        "unequal infrastructure siting, and caste-differentiated public-water-point access "
        "(reported social dominance/untouchability at communal taps), alongside household financial "
        "capacity determining ability to self-finance private borewells as an alternative to reliance "
        "on public provision."
    ),
    population="rural households across 6 villages, Baghmundi CD Block, Puruliya District, West Bengal, India",
    household_level="TRUE",
    community_level="TRUE",
    income_group="low-income (predominantly agrarian/wage-labour livelihoods)",
    indigenous_population="TRUE",
    eligibility="FALSE",
    discretion_accommodation="TRUE",
    institutional_fragmentation="TRUE",
    bureaucratic_assistance="TRUE",
    fees="TRUE",
    delay="TRUE",
    water_access="TRUE",
    service_reliability="TRUE",
    affordability="TRUE",
    effect_measure="mixed-methods (structured household survey, n=240, chi-square/Cramer's V and binary logistic regression; 10 KIIs, 12 FGDs, field observations, 2023-2024 follow-up investigation with thematic coding)",
    effect_estimate=(
        "Household income showed the strongest association with both self-financed in-home water "
        "access (Cramer's V=0.476, p<0.001) and reliance on public water provision (Cramer's "
        "V=0.466, p<0.001); households earning <INR10,000/month had significantly lower odds of "
        "self-financing private water access than those earning >INR20,000/month (OR=0.075, "
        "p=0.001) and significantly higher odds of relying on public water service provision "
        "(OR=8.319, p=0.004), after adjusting for education, household size, occupation and caste. "
        "Caste-group differences in social dominance/untouchability perceptions at public water "
        "collection points were statistically significant (Kruskal-Wallis p<0.001, ε²=0.127), and "
        "OBC/SC households travelled significantly longer distances and spent significantly more "
        "time collecting water than General-caste households (Dunn-Bonferroni p<0.05). Qualitatively, "
        "a Scheduled Caste (Kalindi) respondent reported: 'being outside the mainstream of society, "
        "we have limited and unreliable access to public access points... Many times, we complained "
        "to our local leader, but they provide only assurance, no solution.' The institutional "
        "decision-making chain (household report to Gram Panchayat -> Block administration -> PHED "
        "technical assessment -> infrastructure implementation) was documented as producing repeated "
        "tube-well siting failures, unequal infrastructure distribution, and delayed or undelivered "
        "funding; a 2023-2024 follow-up documented an adaptive solar-powered community-tap "
        "intervention that reduced collection time and conflict at communal points for a previously "
        "excluded SC community but did not eliminate gendered water-collection burdens or spatial "
        "inequality, with residents still lacking household tap connections."
    ),
    lower_CI="",
    upper_CI="",
    p_value="p<0.001 (income association with water-access outcomes); p=0.004 (income OR for public-provision reliance)",
    extraction_sample_size="240 households (structured survey, 2019-2020); 10 KIIs, 12 FGDs (7-10 participants each), 8 informal discussions, plus 2023-2024 follow-up (16 additional interviews, 10 informal discussions)",
    adjusted_or_unadjusted="adjusted (binary logistic regression controlling for income, education, household size, occupation, caste)",
    covariates="income, occupation, caste group, education level, household size",
    model_type="binary logistic regression (adjusted odds ratios) and Kruskal-Wallis H tests with Dunn-Bonferroni post-hoc pairwise comparisons",
    study_design="mixed methods (cross-sectional household survey + qualitative KII/FGD + follow-up field investigation)",
    risk_of_bias_tool="MMAT",
    selection_bias="Moderate (purposive sampling of 6 villages and households for contextual diversity rather than probability-based representativeness, as explicitly acknowledged by the authors)",
    measurement_bias="Low-moderate (structured survey questionnaire combined with multiple qualitative methods for cross-validation; self-reported water-access and caste-discrimination experiences)",
    confounding="Partially controlled (adjusted logistic regression for key socioeconomic covariates; caste not modelled as an intersectional interaction with gender/age/disability, an explicitly acknowledged limitation)",
    attrition="Not applicable (cross-sectional design)",
    reporting_bias="Low (persistent caste-based exclusion and unresolved infrastructure inequality are reported as central findings even after a follow-up intervention)",
    legal_measurement_quality="moderate (the PHED/Gram Panchayat/Jal Jeevan Mission institutional governance chain and its funding/approval process are directly documented via KIIs with GP and Block officials, though not tied to a specific eligibility statute)",
    outcome_measurement_quality="high (structured survey with formal statistical testing, triangulated with independent qualitative KII/FGD evidence and field observation)",
    mechanism_certainty="2",
    source_document="Saha & Chakma 2026, SN Social Sciences",
    table="Table 1 (in-home financial water access determinants); Table 2 (reliance on public water sources); Table 6-7 (institutional role and social dominance)",
    figure="Figure 7 (stakeholder-informed institutional decision-making process)",
    section="Results; Household water access insecurity and local governance process: qualitative findings",
    exact_location="income/caste determinants of public-vs-private water access; institutional decision-making chain (Gram Panchayat-Block-PHED); caste-based social dominance at public water points",
    extraction_note="record_id RE955C8795F4F.",
    researcher="Claude-AI-fulltext-2026-21",
    date_extracted="2026-09-21",
    evidence_status="OBSERVED",
))
new_rows.append(s)

# --- S535: Regulators as activists (road-transported sanitation, East/Southern Africa), record_id R3858447F3CCC ---
s = blank_row()
s.update(dict(
    study_id="S535",
    citation="Grisaffi C, Leinster P, Sipuma R, Owako E, Parker A (2026). New definitions for good practice: Regulators as activists for urban road-transported sanitation in eastern and southern Africa. PLOS Water, 5(1), e0000385.",
    doi="10.1371/journal.pwat.0000385",
    publication_year="2026",
    publication_type="journal article",
    language="English",
    peer_reviewed="TRUE",
    country="multi-country (Kenya, Mozambique, Tanzania, Uganda, Zambia)",
    subnational_unit="national and local (utility/municipal) sanitation regulators, 5 East/Southern African countries",
    legal_system="mixed common law (former British colonial administrations, East/Southern Africa)",
    urban_rural="urban",
    service_provider="national sanitation regulators (autonomous agencies/ministerial departments); utilities and municipalities acting as de-facto local regulators; formal and informal faecal-sludge emptying/transport service providers",
    regulatory_model=(
        "Multilayered national-and-local regulatory system governing safe emptying and transport of "
        "faecal sludge from onsite sanitation, in which the legal status of manual pit-latrine "
        "emptying varies by country (disallowed by some Kenyan county bylaws despite national "
        "guideline permission; legal if hygienic in Mozambique; legal with improved tools in "
        "Tanzania; at least semi-mechanised required in Uganda; legal and incorporated into national "
        "training in Zambia), with local regulators (utilities/municipalities) exercising informal "
        "discretionary enforcement -- issuing tacit amnesties, engaging informal/illegal manual "
        "emptiers rather than sanctioning them, and in some cases negotiating interim disposal sites "
        "involving other authorities 'turning a blind eye' -- to progressively formalise and scale "
        "safe service to low-income and informal areas."
    ),
    population="national and local sanitation regulators, service providers (formal and informal manual pit emptiers), and low-income/informal urban households relying on road-transported (non-sewered) sanitation, East and Southern Africa",
    household_level="TRUE",
    community_level="TRUE",
    income_group="low-income",
    eligibility="FALSE",
    discretion_accommodation="TRUE",
    enforcement="TRUE",
    institutional_fragmentation="TRUE",
    political_coordination="TRUE",
    bureaucratic_assistance="TRUE",
    sanitation_access="TRUE",
    service_coverage="TRUE",
    effect_measure="qualitative thematic analysis (19 semi-structured key-informant interviews with national/local regulators) combined with secondary-data review of prior WHO/ESAWAS transcripts (37 sources) and Delphi-study open-text responses (23 sources)",
    effect_estimate=(
        "All interviewed national and local regulators indicated that engaging informal manual "
        "pit emptiers -- rather than sanctioning or displacing them -- was essential to reaching "
        "universal access to safe sanitation in low-income areas, a finding the authors identify as "
        "novel for road-transported sanitation regulation globally. Local regulators described "
        "working 'in a legal grey zone,' negotiating interim disposal sites that required other "
        "authorities to informally tolerate non-compliant practice, and building relationships of "
        "trust with manual emptiers working 'illegally' to bring them 'on board' without 'crushing "
        "them.' One local regulator described the process: 'now we are at a stage where we can start "
        "to sanction... We've engaged them as much as we can... now let's start to identify what "
        "those penalties will be' -- illustrating a phased shift from tolerance/engagement toward "
        "eventual formal enforcement. National regulators described taking financial and political "
        "risks, including challenging International Financing Institutions and internal utility "
        "board resistance, to advance sector reform absent complete rules ('there was no regulatory "
        "framework and therefore everything was being done as pilot, or trial and error'). Regulators "
        "identified persistent gaps in requisite powers over household containment quality (pit "
        "latrine/septic tank design), overlapping and fragmented mandates with health, environment "
        "and labour departments enforcing sanctions on the same emptiers local regulators sought to "
        "engage, and inadequate resources and capacity across all five countries as barriers to "
        "consistent implementation. The authors frame utilities and municipalities acting in this "
        "capacity as de-facto 'local regulators' engaging in 'moral courage' -- a concept the study "
        "extends from regulatory-governance and business-ethics literature to the sanitation sector "
        "for the first time -- required to navigate incomplete rules, unclear mandates and limited "
        "resources while scaling access for the poorest and most stigmatised populations."
    ),
    extraction_sample_size="19 primary semi-structured key-informant interviews (10 national regulators, 9 local regulators across Kenya, Mozambique, Tanzania, Uganda, Zambia); secondary review of 37 prior transcripts and 23 Delphi open-text responses",
    adjusted_or_unadjusted="not applicable (qualitative thematic analysis)",
    model_type="qualitative thematic analysis (NVivo-coded) against a literature-derived good-practice regulatory framework",
    study_design="qualitative multi-country case study (semi-structured key-informant interviews)",
    risk_of_bias_tool="CASP",
    selection_bias="Moderate (purposive sampling of 'positive outlier' regulators in leading countries/organisations, explicitly limiting generalisability to current sectoral practice as acknowledged by the authors)",
    measurement_bias="Low-moderate (thematic analysis validated against secondary-data transcripts and a structured literature-derived coding framework; self-reported practice subject to social-desirability bias, explicitly acknowledged)",
    confounding="Not applicable (qualitative thematic-analysis design)",
    attrition="Not applicable",
    reporting_bias="Low (gaps in resources, powers and rules are reported directly alongside positive findings on regulator courage and informal-sector engagement)",
    legal_measurement_quality="high (specific national legal statuses of manual pit emptying across five countries directly documented and compared, e.g. Kenyan WASREB guidelines vs. county bylaws, Zambian NWASCO framework)",
    outcome_measurement_quality="moderate-high (draft manuscript shared with key informants for validation; >70% confirmed findings resonated with their experience)",
    mechanism_certainty="2",
    source_document="Grisaffi, Leinster, Sipuma, Owako & Parker 2026, PLOS Water",
    table="Table 1 (roles/characteristics of good-practice regulator); Table 2 (secondary data and primary KII summary); Table 3 (legal/regulatory frameworks by country)",
    section="3.3 Revisiting the concept of local regulators; 3.5 Beyond currently defined good practice",
    exact_location="informal-sector engagement/tacit-amnesty discretion findings; Table 3 cross-country legal status of manual pit-latrine emptying",
    extraction_note="record_id R3858447F3CCC.",
    researcher="Claude-AI-fulltext-2026-21",
    date_extracted="2026-09-21",
    evidence_status="OBSERVED",
))
new_rows.append(s)

rows.extend(new_rows)

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, DB)
print("done. total rows:", len(rows))
