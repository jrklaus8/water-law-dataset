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

# S838 - Derman - Cultures of Development and Indigenous Knowledge, Zimbabwe water reform
add("S838",
    citation="Derman B (2003). Cultures of Development and Indigenous Knowledge: The Erosion of Traditional Boundaries. Africa Today.",
    doi="10.1353/at.2004.0007",
    publication_year="2003",
    country="Zimbabwe",
    subnational_unit="Mid-Zambezi Valley and national catchment councils",
    legal_system="common law (post-colonial, Roman-Dutch derived)",
    urban_rural="rural",
    service_provider="Zimbabwe National Water Authority (ZINWA), catchment councils",
    regulatory_model="Ethnographic study (1989-2003 fieldwork, interviews with law drafters, Catchment Council minutes, household surveys) of Zimbabwe's Water Act of 1998 and companion ZINWA Act, examining the statutory distinction between permit-requiring 'commercial water' (agriculture, mining, industry, municipal works) and unregulated 'primary water' (defined in section 32(1) as water for domestic human needs, animal life, and other small-scale household uses), and how the formal water-reform/permit system institutionally marginalizes communal/customary domestic water access relative to commercial permit-holders, with the reform process ultimately aborted by land invasions and loss of ZINWA funding capacity",
    population="rural communal-area households in Zimbabwe dependent on primary (domestic) water use",
    sample_size="14 years of ethnographic fieldwork; interviews with water-law drafters; Catchment Council Minutes (Mazowe, Manyame, Sanyati, 2000); CASA/BASIS household survey data from two villages",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE", documentation="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="ethnographic case study (interviews, catchment-council minutes, household survey data)",
    effect_estimate="Zimbabwe's Water Act 1998 (section 32(1)) statutorily exempts 'primary water' (including domestic household needs) from the permit system required for 'commercial water' (agriculture, mining, industry, municipal works), but the water-reform process and its supporting institutions (ZINWA, catchment councils) focus overwhelmingly on commercial-permit administration, treating primary/domestic water supplies as peripheral to 'development institutions'; communal areas are institutionally regarded as underdeveloped due to their low commercial-permit uptake even though their primary domestic water use is formally unregulated, and the broader reform effort ultimately collapsed when land invasions undermined ZINWA's funding base (previously financed by commercial-farmer water payments)",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: extended ethnographic fieldwork (14 years) combined with direct interviews of the Water Act's own drafters and catchment-council administrative records, directly documenting the statutory primary/commercial water distinction and its institutional marginalization of domestic-water-dependent communal areas.",
    source_document="Derman 2003, Africa Today (retrieved via Google Drive)",
    section="Water Act of 1998 and primary/commercial water distinction; catchment council institutional analysis",
    exact_location="Throughout, especially the water-reform discussion",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: ethnographic study directly documenting a specific national statutory water-classification scheme (Water Act 1998 s.32(1), primary vs. commercial water) and its institutional effects on communal/customary household water access, paralleling the established Indigenous/customary-water-rights inclusion precedent (S823 Alvez Marin Chile, Bakker et al. Canada). NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R85E320C718A8.",
    )

# S839 - Odeku & Konanani - Poor Water Service Delivery, Phiri/Mazibuko case analysis
add("S839",
    citation="Odeku KO, Konanani RH (2014). Poor Water Service Delivery: An Exposition of the Plight of the Phiri Community in Soweto, South Africa. Studies of Tribes and Tribals.",
    doi="10.1080/0972639X.2014.11886697",
    publication_year="2014",
    country="South Africa",
    subnational_unit="Phiri, Soweto, Johannesburg",
    legal_system="common law (post-apartheid constitutional)",
    urban_rural="urban",
    service_provider="City of Johannesburg, Johannesburg Water (Operation Gcin'amanzi)",
    regulatory_model="Legal-doctrinal case analysis of Mazibuko and Others v City of Johannesburg and Others (Constitutional Court, High Court, and Supreme Court of Appeal decisions), examining South Africa's Free Basic Water policy (6 kilolitres/household/month), the lawfulness of pre-paid water meters installed under Operation Gcin'amanzi, section 27 of the Constitution (right to sufficient water), the National Water Act 36 of 1998, the Water Services Act 108 of 1997, and the Indigent Persons/Registration Policy, situating the litigation within the broader South African jurisprudence on justiciable socio-economic rights (Grootboom, Soobramoney, Fose)",
    population="Phiri community residents, Soweto, Johannesburg",
    sample_size="doctrinal case analysis of three court judgments (High Court, Supreme Court of Appeal, Constitutional Court) and statutory/constitutional text",
    household_level="TRUE", community_level="TRUE", tenure_status="",
    fees="TRUE", disconnection="TRUE", judicial_review="TRUE", administrative_review="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quantity="TRUE",
    effect_measure="legal-doctrinal case analysis (constitutional/statutory text and appellate case law)",
    effect_estimate="The Constitutional Court in Mazibuko upheld the City of Johannesburg's Free Basic Water policy (6 kilolitres/household/month) as reasonable under section 27's progressive-realisation standard, and held that installation of pre-paid water meters under Operation Gcin'amanzi was authorised by national legislation and municipal by-laws (reversing the High Court and Supreme Court of Appeal, which had found the meters unlawful/discriminatory and set free-water amounts at 50 and 42 litres/person/day respectively); the authors critique the outcome, noting billed pre-Gcin'amanzi consumption averaged 67 kilolitres/household/month against only 6 kilolitres free, and that pre-paid meters function as an automatic, non-administrative suspension of service upon exhaustion of the free allowance -- with a documented cholera outbreak in KwaZulu-Natal linked to a comparable prepaid-meter/affordability failure elsewhere",
    study_design="legal-doctrinal case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: close doctrinal analysis of the full Mazibuko litigation history (three court levels) and the specific statutory/constitutional provisions and municipal by-laws governing free basic water and pre-paid meter lawfulness.",
    source_document="Odeku & Konanani 2014, Studies of Tribes and Tribals (retrieved via Google Drive)",
    section="Mazibuko's Case in Context; Comments (prepaid meters; free basic water policy; discrimination based on means)",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established doctrinal/legal-scholarship inclusion precedent (S825 Perumal's Mazibuko analysis, S823 Alvez Marin): independent legal-doctrinal case analysis of the same Mazibuko v. City of Johannesburg litigation from a different analytical angle (indigent registration policy, comparative critique of the free-water allowance vs. actual consumption), providing substantive legal-mechanism analysis distinct from S825's feminist-legal framing. NOT effect_sizes eligible: doctrinal case analysis, no regression-based estimate. Extracted for record_id R8609FE411A88.",
    )

# S840 - Grant - Urban and Suburban Nashville, metropolitan water fragmentation
add("S840",
    citation="Grant DR (1955). Urban and Suburban Nashville: A Case Study in Metropolitanism. The Journal of Politics.",
    doi="",
    publication_year="1955",
    country="United States",
    subnational_unit="Nashville and Davidson County, Tennessee",
    legal_system="common law",
    urban_rural="both",
    service_provider="City of Nashville municipal water system; four suburban special utility districts (First Suburban/Radnor, Nashville Suburban/Belle Meade, Madison, Old Hickory) and private water companies",
    regulatory_model="Institutional case study of metropolitan water-service fragmentation in Nashville/Davidson County under Tennessee's State Utility District Act of 1937, which permits self-perpetuating, unelected utility-district boards (exempt from taxation, not subject to popular vote or public regulatory oversight) to operate water/sewer/fire-protection systems, examining how suburban consumers receive water through a patchwork of direct city service (at nearly triple the in-city rate), wholesale-purchase-and-resale special districts, independently-sourced special districts, and private water companies",
    population="suburban Davidson County residents outside Nashville city limits (combined population ~114,000 across districts in 1951)",
    sample_size="institutional/documentary case study with 1951 population and rate data for city and four suburban utility districts",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE", service_area="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="institutional/documentary case study with quantified rate and population-served data",
    effect_estimate="Under Tennessee's State Utility District Act of 1937, unaccountable, tax-exempt special water-utility districts create 'substantially uncontrolled monopolies': suburban residents receiving water directly from Nashville's city pipelines pay a rate almost three times the in-city rate, while other suburban residents are served by special districts that either buy water wholesale from the city for resale or maintain fully independent sources, producing a fragmented 'scrambled eggs' metropolitan water-supply arrangement with no unified rate structure or public regulatory accountability across roughly 114,000 suburban residents",
    study_design="institutional/regulatory case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed documentary analysis of a specific state statute (Tennessee State Utility District Act of 1937) and its institutional structure, with quantified rate-differential and population-served data across the fragmented metropolitan water-supply system.",
    source_document="Grant 1955, The Journal of Politics (retrieved via Google Drive, JSTOR)",
    section="Water Supply",
    exact_location="pp. 89-90",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional case study of a specific state statutory scheme (special water utility districts) directly causing quantified metropolitan tariff/access fragmentation, paralleling the institutional-fragmentation mechanism established this batch in S837 (Scott, Moldogaziev & Greer, Houston). NOT effect_sizes eligible: institutional/documentary case study, no regression-based estimate. Extracted for record_id R513E53E45833.",
    )

# S841 - Addai & Pokimica - Trust and Material Hardship in Ghana, institutional trust/water deprivation
add("S841",
    citation="Addai I, Pokimica J (2012). An Exploratory Study of Trust and Material Hardship in Ghana. Social Indicators Research.",
    doi="10.1007/s11205-011-9909-3",
    publication_year="2012",
    country="Ghana",
    subnational_unit="national",
    legal_system="common law",
    urban_rural="both",
    service_provider="not applicable (national household survey of water deprivation, not a specific utility)",
    regulatory_model="Quantitative analysis of the 2008 Afrobarometer national survey, using five separate multinomial logistic regression models (one per material-hardship outcome: food, water, medical care, cooking fuel, cash income) to isolate the association between interpersonal (thick/thin) and institutional (legislative, executive, judicial) trust and frequency of going without each necessity, with a stepwise forward-entry variable-selection method and socioeconomic/cultural controls (education, ethnicity)",
    population="nationally representative sample of Ghanaian adults (2008 Afrobarometer respondents)",
    sample_size="2008 Afrobarometer national survey sample",
    household_level="TRUE", community_level="",
    institutional_fragmentation="",
    water_access="TRUE", affordability="TRUE",
    effect_measure="multinomial logistic regression, odds ratios",
    effect_estimate="In the water-deprivation model (isolated from the other four hardship outcomes), respondents with only 'a little' trust in judicial institutions (courts) were significantly more likely to have gone without water 'several times' relative to 'never' than those with 'a lot' of judicial trust (OR = 1.789, p <= .05), with a similar pattern for the 'many times' category; those with no executive trust 'at all' were also significantly more likely to report frequent water deprivation (OR = 2.703, p <= .01); trust in courts was identified as a unique predictor of water deprivation specifically, distinct from the predictors significant for the other four hardship outcomes (e.g., parliamentary trust for food, police trust for cash income)",
    study_design="national survey-based quantitative study (multinomial logistic regression)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: a nationally representative survey with a rigorously isolated (non-composite) water-deprivation regression model and statistically significant institutional-trust (particularly judicial) predictors, though the exposure (subjective institutional trust) is a perceptual/attitudinal proxy for institutional legitimacy rather than a documented legal/institutional mechanism (specific rule, policy, contract, or barrier).",
    source_document="Addai & Pokimica 2012, Social Indicators Research (retrieved via Google Drive)",
    table="Table 3 (water deprivation model results)",
    section="7.2 DV2: Water Deprivation",
    exact_location="pp. 421-423",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous national-survey regression study isolating water deprivation as its own dependent variable (not composite with other hardship types) with institutional-trust predictors (judicial trust uniquely significant for water). NOT effect_sizes eligible per the strict Family A/B/C framework (PROJECT_SPEC.md Section 8): the exposure is subjective/perceptual institutional trust, not a documented legal/institutional mechanism (legal recognition, tenure, documentation, administrative assistance, or barrier) as Family A/B/C require -- paralleling this batch's S837 exclusion (outcome mismatch) but here reflecting an exposure-side mismatch. Extracted for record_id R899DB35753C8.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
