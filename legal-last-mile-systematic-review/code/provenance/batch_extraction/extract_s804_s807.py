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

# S804 - Kalulu & Hoko - Blantyre Water Board, Malawi
add("S804",
    citation="Kalulu K, Hoko Z (2010). Assessment of the performance of a public water utility: A case study of Blantyre Water Board in Malawi. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2010.07.017",
    publication_year="2010",
    country="Malawi",
    subnational_unit="Blantyre",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Blantyre Water Board (BWB), a parastatal utility mandated by the Water Works Act No. 17 of 1995",
    regulatory_model="Documentation review (national legal/policy documents, BWB policy documents and reports) plus interviews with utility staff (Internal Audit Manager, Zone Manager, Projects and Planning Engineer) and 100 randomly-selected low-income domestic customers, assessing utility performance (working ratio, revenue collection, tariffs, unaccounted-for water, staffing) against developing-country best-practice targets under the Water Works Act 1995's full-cost-recovery mandate",
    population="Blantyre Water Board service-area customers, particularly low-income areas (Chilobwe, Misesa, Nancholi)",
    sample_size="100 domestic customers interviewed plus 3 utility staff; documentation review 2001-2009",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", disconnection="TRUE", reconnection="TRUE",
    water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="descriptive performance-indicator analysis (documentation review) with structured customer/staff interviews",
    effect_estimate="Water bills for house connections in low-income areas accounted for 4.4% of household income, a figure the utility itself and 70% of interviewed customers deemed high; despite the statutory full-cost-recovery mandate, the utility ran net losses from 2002 onward, had a working ratio up to 1.3 (above the 0.68 developing-country target), collected only 70% of billed revenue in an average 340 days (against a 90-day target), and eight of 100 interviewed customers reported being disconnected despite having already paid through a bank; 17 of 100 customers cited the reconnection fee (MK1000) as exorbitant; water-service coverage was 49% in low-income areas versus 96% in formal medium/high-income areas",
    study_design="descriptive utility-performance case study (documentation review plus structured interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: primary interview data from 100 low-income customers and utility staff directly documenting tariff burden, disconnection despite payment, and reconnection-fee barriers under the utility's statutory full-cost-recovery mandate, though the paper's primary framing is utility financial/technical performance benchmarking rather than a dedicated legal/institutional access-barrier analysis.",
    source_document="Kalulu & Hoko 2010, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    table="Tables 1-7",
    section="Results and discussion (financial sustainability, tariffs)",
    exact_location="Sections 4.1.2-4.1.3 (revenue collection, tariffs)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary customer-interview data (100 low-income households) and utility-staff interviews documenting tariff burden, disconnection despite payment, and reconnection-fee barriers under a statutory full-cost-recovery mandate (Water Works Act 1995). NOT effect_sizes eligible: descriptive performance-indicator analysis, no regression-based estimate. Extracted for record_id RCF31FA5B9CF9.",
    )

# S805 - Begolli & Lajci - Kosova water sector reform
add("S805",
    citation="Begolli B, Lajci A (2016). Water services sector reform: the Kosova experience. Water Science & Technology: Water Supply.",
    doi="10.2166/ws.2015.104",
    publication_year="2016",
    country="Kosova",
    subnational_unit="28 municipalities served by 7 Regional Water Companies (RWCs)",
    legal_system="civil law (post-UNMIK transitional/statutory framework)",
    urban_rural="both",
    service_provider="7 Regional Water Companies (RWCs), consolidated from 30 municipal water utilities",
    regulatory_model="Institutional/legal case study of Kosova's 2000-2016 water-sector reform: consolidation of 30 municipal utilities into 7 regional companies via a series of UNMIK Regulations and Laws (UNMIK Reg. 2000/45, 2000/49, 2002/05, 2002/12, 2004/49, 2005/15; Law No. 03/L-040, 03/L-086, 03/L-087, 04/L-111), establishment of the independent economic regulator (Water and Waste Regulatory Office, WWRO), the Kosova Trust Agency, and an Inter-Ministerial Water Council for coordination across seven ministries",
    population="Kosova residents in the seven RWC service areas",
    sample_size="national institutional/legislative case study; RWC-level administrative coverage data",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE",
    effect_measure="institutional/legal case study with administrative coverage data",
    effect_estimate="Consolidation of 30 fragmented municipal water utilities into 7 Regional Water Companies under a completed legal and institutional framework (by 2008) increased water-supply coverage: the RWCs served 1.23 million people (72.1% of the population within their service areas) as of the study, versus 52% of the population connected to water services nationally before the 2000 reforms; establishment of the independent WWRO regulator improved tariff-setting, licensing, and customer-rights protection",
    study_design="institutional/legal case study (legislative and administrative-history analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed statutory/regulatory case study (multiple named laws and regulations) directly tracing water-utility consolidation and independent-regulator establishment to documented service-coverage improvements (52% pre-reform to 72.1% RWC-area coverage).",
    source_document="Begolli & Lajci 2016, Water Science & Technology: Water Supply (retrieved via Google Drive)",
    table="Table 1",
    figure="Figures 1-4",
    section="Post-war state of the sector; Conceptualization of water sector reforms; Results",
    exact_location="Sections on RWC consolidation and results of the reforms",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed legal/institutional case study of water-utility consolidation and independent-regulator establishment (named UNMIK Regulations and Laws), with coverage data before/after reform. NOT effect_sizes eligible: descriptive institutional case study with administrative coverage figures, no regression-based estimate. Extracted for record_id RCF1AD58436DF.",
    )

# S806 - Guimaraes, Malheiros & Marques - Inclusive governance, Brazil
add("S806",
    citation="Guimaraes EF, Malheiros TF, Marques RC (2016). Inclusive governance: New concept of water supply and sanitation services in social vulnerability areas. Utilities Policy.",
    doi="10.1016/j.jup.2016.06.003",
    publication_year="2016",
    country="Brazil",
    subnational_unit="Sao Paulo Metropolitan Region (Baixada Santista)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="SABESP (Sao Paulo State Water and Wastewater Utility)",
    regulatory_model="Qualitative case study (documentary research, questionnaires, field observation) of SABESP's 'Se liga na Rede' (Connect to the Network) program, examining how Brazil's legal requirement that WS&S universal-access targets and connections apply only to legally-regularized (formal) land-tenure settlements excludes slum/favela residents from official coverage statistics and utility service, and how a state-subsidized connection program and new 'inclusive governance'/'inclusive access' indicators address this tenure-based legal barrier",
    population="residents of slums and informal settlements (favelas) in the Sao Paulo Metropolitan Region, particularly Baixada Santista",
    sample_size="household survey of program beneficiaries plus case-study documentary/field research",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    tenure="TRUE", property="TRUE", documentation="TRUE", eligibility="TRUE", legal_status="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="qualitative case study with descriptive program survey data",
    effect_estimate="Brazil's legal framework ties WS&S universal-access targets to land-tenure regularization: official coverage statistics count only consolidated (formal) settlements, so utilities are effectively prohibited from extending infrastructure to illegal/unregularized areas until land tenure is resolved, excluding slum residents (nearly 11 million people in Brazil) from official access; SABESP's 'Se liga na Rede' program, a legally-established state-utility cost-sharing partnership (80% state/20% utility financed), achieved 191,700 planned household connections benefiting about 800,000 people in regularized low-income areas, though the survey found 40% of targeted households remained unconnected, 23% of these citing connection cost as the barrier, and 51% of wastewater was still discharged directly into streams",
    study_design="qualitative institutional case study with descriptive program-survey data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: direct legal analysis of Brazil's tenure-regularization requirement as an access-control mechanism (official coverage statistics excluding illegal settlements, utilities barred from serving unregularized areas), combined with primary survey/case-study data from a targeted connection program.",
    source_document="Guimaraes, Malheiros & Marques 2016, Utilities Policy (retrieved via Google Drive)",
    table="Tables 1-2",
    figure="Figure 1",
    section="Legal barriers section; Results and experiences in Sao Paulo",
    exact_location="Section on legal barriers to universal service and SABESP program results",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct legal analysis of Brazil's land-tenure regularization requirement as a formal water/sanitation-access-control mechanism, combined with primary program-survey and case-study data (SABESP 'Se liga na Rede'). NOT effect_sizes eligible: qualitative case study with descriptive program-survey percentages, no regression-based estimate. Extracted for record_id RCD44792548EF.",
    )

# S807 - Gerlach & Franceys - Regulating water services for the poor, Amman
add("S807",
    citation="Gerlach E, Franceys R (2009). Regulating water services for the poor: The case of Amman. Geoforum.",
    doi="10.1016/j.geoforum.2008.11.002",
    publication_year="2009",
    country="Jordan",
    subnational_unit="Amman",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="private management contractor (LEMA) under a quasi-regulatory arrangement with Jordanian water authorities",
    regulatory_model="Household survey (June/July 2005) of poor and vulnerable consumers combined with institutional analysis of the economic-regulatory arrangements accompanying Amman's private management contract, identifying specific regulatory gaps (rationing, connection policy, tariff structure for the poor) not addressed by the acting quasi-regulator or water authorities despite Jordan's unusual near-100% urban connection rate",
    population="poor and vulnerable water consumers, Amman, Jordan",
    sample_size="targeted household survey, June/July 2005",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", eligibility="TRUE", discretion_accommodation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", affordability="TRUE",
    effect_measure="household survey with institutional/regulatory-gap analysis",
    effect_estimate="Despite Jordan achieving a nearly 100% urban water-connection rate and introducing a private management contractor with economic regulation in Amman, extreme water scarcity produces water rationing that disproportionately affects low-income households; the study identifies specific regulatory arrangements for poor/vulnerable consumers (connection policy, tariff structure, rationing schedules) that fell outside the remit of, or were not addressed by, the acting quasi-regulator and water authorities, leaving a regulatory gap despite near-universal formal connection",
    study_design="household survey with institutional/regulatory case-study analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: targeted household survey combined with direct institutional/regulatory analysis identifying specific gaps in economic-regulatory coverage of poor and vulnerable water consumers under a private-management/quasi-regulator arrangement.",
    source_document="Gerlach & Franceys 2009, Geoforum (retrieved via Google Drive)",
    section="Results (regulatory arrangements for poor and vulnerable consumers)",
    exact_location="Sections on household survey findings and regulatory gap analysis",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary household survey combined with direct institutional/regulatory-gap analysis of economic regulation and poor/vulnerable-consumer protections under a private water-management contract. NOT effect_sizes eligible: descriptive survey and regulatory-gap case study, no regression-based estimate. Extracted for record_id RC8FC125A9F16.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
