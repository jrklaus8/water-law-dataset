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

# S873 - Kim - Malaysian Water Sector Reform
add("S873",
    citation="Kim CT (2012). Malaysian Water Sector Reform: Policy and Performance. PhD Dissertation, Wageningen University.",
    doi="",
    publication_year="2012",
    publication_type="dissertation",
    country="Malaysia",
    subnational_unit="national, with Penang (PBAPP, private) and Kedah (SADA, public) case studies",
    legal_system="common law",
    urban_rural="both",
    service_provider="state water corporations/departments, private concessionaires, and (post-2006) the National Water Services Commission (NWSC) and Pengurusan Aset Air Berhad (PAAB)",
    regulatory_model="Mixed-methods PhD dissertation (53 in-depth semi-structured interviews with water operators, government officials, consumer associations and environmental organizations; document/policy analysis; direct observation) analyzing Malaysia's 2006 water-sector reform -- introduction of the Water Services Industry Act (WSIA) and Suruhanjaya Perkhidmatan Air Negara Act (SPANA), a Federal Constitution amendment, and creation of a central regulator (NWSC) and sector financier (PAAB) -- using a policy-arrangement approach, and comparing operational-efficiency and environmental-effectiveness indicators between a private (PBAPP, Penang) and public (SADA, Kedah) water utility",
    population="water utility customers across Malaysia, with detailed comparative case studies of Penang and Kedah state water services",
    sample_size="53 in-depth interviews; utility-level operational data 2000s-2010s; two comparative case studies",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE",
    effect_measure="mixed-methods policy-arrangement case study with quantified operational-efficiency/environmental-effectiveness indicators",
    effect_estimate="Malaysia's 2006 legal/institutional water-sector reform (WSIA, SPANA, creation of NWSC and PAAB) restructured regulatory authority and financing away from fragmented state-level control, with the dissertation documenting quantified non-revenue water, billing-collection efficiency, unit production cost, and drinking-water-quality-compliance indicators before and after reform across public and private operators; the private utility (PBAPP) consistently outperformed the public utility (SADA) on non-revenue water and collection efficiency, while regulatory information-disclosure remained constrained by the Official Secrets Act 1972 and Banking and Financial Institutions Act 1989, illustrating how the specific legal/institutional reform structure shaped both performance outcomes and residual barriers to regulatory transparency",
    study_design="mixed-methods policy-arrangement case study (dissertation)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: doctoral dissertation combining 53 stakeholder interviews, document analysis and quantified utility performance data directly documenting a specific national legal/institutional water-sector reform (WSIA, SPANA, NWSC, PAAB) and comparative public/private outcomes.",
    source_document="Kim 2012, Wageningen University dissertation (retrieved via Google Drive)",
    section="Chapters 3-6 (reform process, policy arrangement analysis, operational efficiency, environmental effectiveness)",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national water-sector-reform case-study inclusion precedent (RE6E898E698B5 Malaysia parallels S828 Brazil WatSan law, S865 South Africa CGE): dissertation directly documenting a specific national legal/institutional reform and its quantified performance effects via mixed methods. NOT effect_sizes eligible: policy-arrangement case study with descriptive comparative indicators, no regression-based estimate. Extracted for record_id RE6E898E698B5.",
    )

# S874 - Morvaridi - Maharashtra water supply/sanitation
add("S874",
    citation="Morvaridi B (1994). Management of Water Supply and Sanitation Projects in Maharashtra State, India. Journal of International Development.",
    doi="",
    publication_year="1994",
    country="India",
    subnational_unit="Nasik district, Maharashtra State",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Overseas Development Administration (ODA)-funded Integrated Rural Water Supply Sanitation and Health Education Project; village water committees",
    regulatory_model="Field-report fieldwork study (participant observation and interviews at village, household and individual levels, three research groups) examining household-level access to a specific ODA-funded rural water/sanitation entitlement scheme (40 litres per capita daily for stand-post users, 70 LPCD for household connections, with additional stand-posts allocated to scheduled castes and tribal populations), documenting how the formal entitlement standard is undermined by institutional structure and caste-based asset-ownership patterns, and examining financial-sustainability/cost-recovery tariff design",
    population="rural households in Nasik, Dhule and Jalgaon districts, Maharashtra, India (project serving 210 villages and one town)",
    sample_size="fieldwork across multiple villages (in-depth study of two per research group) via participant observation and interviews",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", tenure_status="TRUE", fees="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="fieldwork case study with quantified consumption/entitlement data",
    effect_estimate="Despite a formal government entitlement standard of 40 litres per capita daily for stand-post users, actual mean household water consumption in the study villages was only about 24 litres per person -- below the prescribed minimum -- with landless labourers and other low-socioeconomic-status households consuming the least and travelling furthest; the study found that 'access to water is determined by the institutional structure and asset ownership pattern within each village,' meaning caste and land-ownership status, not formal entitlement, determined actual access, while only 5% of surveyed households had access to any latrine (sanitary or otherwise)",
    study_design="fieldwork case study (field report)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: participant-observation fieldwork directly documenting how a formal government water-entitlement standard is mediated by caste-based institutional structure and asset ownership to produce unequal actual household water access.",
    source_document="Morvaridi 1994, Journal of International Development (retrieved via Google Drive)",
    section="Results; Water Supply",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established genuine-fieldwork field-report inclusion precedent (Cleaver 1994 Nkayi Zimbabwe, same journal/format): brief field report with real multi-village participant-observation fieldwork directly documenting how caste-based institutional structure mediates a formal water-entitlement standard. NOT effect_sizes eligible: field report with descriptive fieldwork data, no regression-based estimate. Extracted for record_id R82AEE5CC7ACC.",
    )

# S875 - Hanchett, Akhter & Khan - WaterAid Bangladesh urban slums
add("S875",
    citation="Hanchett S, Akhter S, Khan MH (2003). Water, sanitation and hygiene in Bangladeshi slums: an evaluation of the WaterAid-Bangladesh urban programme. Environment & Urbanization.",
    doi="",
    publication_year="2003",
    country="Bangladesh",
    subnational_unit="Dhaka and Chittagong slums",
    legal_system="common law",
    urban_rural="urban",
    service_provider="WaterAid-Bangladesh and seven local NGO partners (e.g., DSK), providing legal connections to metropolitan Water and Sewerage Authority mains via community-managed water points and sanitation blocks",
    regulatory_model="External programme evaluation combining a household survey (1,130 households, roughly half programme beneficiaries and half non-beneficiaries, matched by area) with qualitative observation, group discussions and key-informant interviews, documenting a specific institutional mechanism -- interest-free NGO loans to construct community water points/sanitation blocks with legal connections to the municipal water-authority mains, repaid via a full-cost-recovery tariff collected by resident management committees -- and comparing water/sanitation access and defecation-behavior outcomes between beneficiary and non-beneficiary slum households",
    population="slum households in Dhaka and Chittagong, Bangladesh (very poor, medium poor, and solvent socioeconomic strata)",
    sample_size="1,130 households surveyed (approximately half beneficiaries, half non-beneficiaries), 46 sites for qualitative assessment",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    fees="TRUE", documentation="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="mixed-methods program-evaluation household survey with comparison group",
    effect_estimate="98.4% of programme-beneficiary households had access to safe water sources (metropolitan-authority mains supply or tubewell) inside their slum, compared to 77.3% of non-beneficiary households -- a 27% improvement in access -- with the largest gains among the very poor (98.7% vs. 71.5%, a 38% improvement); however, full-cost-recovery tariff requirements (roughly Tk 30-107/month) excluded the poorest households from consistent use, and defecation-behavior data showed 37% of beneficiary very-poor households still practiced high-risk (unhygienic) defecation versus 54% of non-beneficiary very-poor households, demonstrating that a specific NGO-facilitated legal water-authority-connection mechanism produced substantial but incomplete household-level water/sanitation-access gains, constrained by its own cost-recovery design",
    study_design="mixed-methods program-evaluation household survey",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: large (n=1,130) matched beneficiary/non-beneficiary household survey combined with qualitative fieldwork directly documenting a specific institutional water/sanitation-access mechanism (NGO-facilitated formal connection to municipal water-authority mains via a cost-recovery loan scheme) and its quantified household-level access outcomes.",
    source_document="Hanchett, Akhter & Khan 2003, Environment & Urbanization (retrieved via Google Drive)",
    table="Table 2 (main drinking water sources), Table 3 (defecation places)",
    section="Findings on access to safe water; Findings on access to environmental sanitation",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established NGO-facilitated formal-connection mechanism inclusion precedent (S860 Singh, Madhya Pradesh poverty mapping; S864 Chng, Manila bulk-water POs): large matched-comparison household survey directly documenting a specific formal water-authority-connection mechanism and its quantified access outcomes. NOT effect_sizes eligible: descriptive comparative survey (beneficiary vs. non-beneficiary percentages), no regression-based estimate isolating the mechanism controlling for confounders. Extracted for record_id R74AD122FBBD1.",
    )

# S876 - Mumme & Ingram - Community Values in Southwest Water Management
add("S876",
    citation="Mumme SP, Ingram HM (1985). Community Values in Southwest Water Management. Policy Studies Review.",
    doi="",
    publication_year="1985",
    country="United States",
    subnational_unit="Papago (Tohono O'odham) Reservation, southern Arizona; Hispanic villages, upper Rio Grande watershed, New Mexico and Colorado",
    legal_system="common law (with Spanish-derived customary water law in Hispanic communities; tribal law on the Papago reservation)",
    urban_rural="rural",
    service_provider="Papago Tribal Council and Water Commissioners; Hispanic acequia (irrigation ditch) associations",
    regulatory_model="Original survey research (regional newspaper content analysis 1977-1980, plus original tribal-member surveys on water-rights-ownership preferences) examining how Papago and Hispanic upper-Rio-Grande communities' communal/customary water values and legal institutions (the Papago Tribal Constitution's declaration that water is a public resource held in common; centuries-old Spanish-law-derived acequia governance) diverge from and resist the market-based water-reallocation prescriptions of the New Resource Economics (NRE) policy paradigm, including analysis of the Papago tribe's 1982 Southern Arizona Water Rights Settlement Act water allocation",
    population="Papago tribal members (southern Arizona) and Hispanic residents of upper Rio Grande watershed communities (New Mexico/Colorado)",
    sample_size="original survey of Papago tribal members on water-rights-ownership preferences (n=67 reported in Table 3); newspaper content analysis (1,163 articles, 1977-1980, 5 regional newspapers)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", indigenous_population="TRUE", tenure="TRUE", property="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="original survey research with quantified attitudinal data",
    effect_estimate="92.5% of surveyed Papago tribal members preferred water rights to be owned at the tribal or district (collective) level rather than individually, and 70% opposed leasing tribal water assets, directly contradicting the New Resource Economics' individual-property-rights market model; under the Papago Tribal Constitution (Article XVIII, 1984), water is declared a public resource held in common, and the tribe's 1982 Southern Arizona Water Rights Settlement Act allocation of 76,000 acre-feet annually was strongly preferred (92.5% of respondents) for traditional agricultural/livestock use over market sale, even though off-reservation sale was a potentially lucrative option; Hispanic upper-Rio-Grande communities showed parallel resistance to market reallocation, grounded in centuries-old Spanish-law-derived acequia governance institutions, demonstrating that customary/tribal legal institutions directly override market-based legal-reform prescriptions in determining actual community water-rights allocation preferences and behavior",
    study_design="original survey research with newspaper content analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: original tribal-member survey data (with quantified percentages) combined with documentary analysis of specific tribal constitutional provisions and a federal water-rights settlement act, directly documenting customary/tribal institutional preferences in tension with market-based legal water-reform prescriptions.",
    source_document="Mumme & Ingram 1985, Policy Studies Review (retrieved via Google Drive)",
    table="Table 1 (newspaper index inventory), Table 2 (symbolic content crosstabulation), Table 3 (Papago water-rights-ownership preferences)",
    section="The Papago Case; The Upper Rio Grande Hispanic Case",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established customary/Indigenous-institutional-tension inclusion precedent (S872 Prieto, Chilean Atacameno water markets; Akpabio Nigeria; Derman Zimbabwe): original tribal-member survey data directly documenting customary/tribal water-rights institutions resisting a market-based legal-reform paradigm, including a specific federal water-rights settlement act. NOT effect_sizes eligible: descriptive attitudinal survey with percentages, no regression-based estimate. Extracted for record_id R3C8C664DF35D.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
