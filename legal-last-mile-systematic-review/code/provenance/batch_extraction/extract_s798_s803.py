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

# S798 - Mulwafu & Msosa - Malawi IWRM
add("S798",
    citation="Mulwafu WO, Msosa HK (2005). IWRM and poverty reduction in Malawi: A socio-economic analysis. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2005.08.043",
    publication_year="2005",
    country="Malawi",
    subnational_unit="national, with river-basin catchment focus",
    legal_system="common law",
    urban_rural="both",
    service_provider="Ministry of Water Development, proposed Catchment Management Authorities, National Water Resources Authority",
    regulatory_model="Document review and key-informant interviews with Ministry of Water Development officials examining Malawi's 2004 National Water Policy, 2002 Poverty Reduction Strategy Paper, and 1999 Local Government Act decentralization framework, and the institutional obstacles (absence of enabling legislation) blocking establishment of proposed river-basin Catchment Management Authorities under an integrated water resources management (IWRM) approach",
    population="Malawian water users, rural and urban, particularly the poor",
    sample_size="document review plus key-informant interviews with Ministry of Water Development officials",
    household_level="TRUE", community_level="TRUE",
    documentation="TRUE", institutional_fragmentation="TRUE",
    water_access="TRUE", service_coverage="TRUE",
    effect_measure="qualitative policy-document analysis with key-informant interviews",
    effect_estimate="Malawi's 2004 National Water Policy and 2002 PRSP articulate pro-poor IWRM commitments and 1999 Local Government Act decentralization, but implementation stalled: proposed river-basin Catchment Management Authorities intended to devolve water-resource governance remained unestablished because of the absence of the necessary enabling legislation, leaving water-resources governance centralized despite the decentralization policy framework",
    study_design="qualitative policy-document analysis with key-informant interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: direct documentation of a specific legislative gap (absence of enabling legislation) blocking the intended institutional decentralization of water-resources governance, combined with primary key-informant interviews from the responsible ministry.",
    source_document="Mulwafu & Msosa 2005, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    section="Policy and institutional framework analysis",
    exact_location="Sections on National Water Policy, PRSP, and Catchment Management Authorities",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct legal/institutional analysis identifying an absence-of-enabling-legislation barrier blocking decentralized river-basin water governance, with primary key-informant interview data. NOT effect_sizes eligible: qualitative policy-document analysis, no regression-based estimate. Extracted for record_id RD6FBE5C6BF3B.",
    )

# S799 - Roy, Akshintala & Sharma - Delhi/JNNURM
add("S799",
    citation="Roy D, Akshintala V, Sharma R (2013). Water Governance and Supply in Urban Areas. Social Change.",
    doi="10.1177/0049085713493045",
    publication_year="2013",
    country="India",
    subnational_unit="Delhi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="municipal government, Delhi Jal Board, under JNNURM urban renewal program",
    regulatory_model="Policy analysis of India's Jawaharlal Nehru National Urban Renewal Mission (JNNURM) mandatory and optional reform conditions -- including repeal of the Urban Land Ceiling and Regulation Act, Rent Control Act reform, property tax reform, 74th Constitutional Amendment participatory-law implementation, and public disclosure law -- combined with resettlement-colony water-quality sampling data documenting the link between property/documentation status and access to safe piped water",
    population="resettlement-colony residents, urban poor, Delhi",
    sample_size="water-quality sampling across resettlement colonies by source type (Figures 4, 6-9)",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE", documentation="TRUE",
    tenure="TRUE", property="TRUE", eligibility="TRUE",
    water_access="TRUE", service_quality="TRUE", service_coverage="TRUE",
    effect_measure="policy-document analysis combined with descriptive water-quality sampling data",
    effect_estimate="Formal property-ownership documentation functions as the key access-control mechanism determining whether urban-poor households can obtain a legal piped-water connection in Delhi; resettlement colonies lacking secure land tenure show markedly higher rates of unsafe water sources (elevated fecal coliform, fluoride, and arsenic contamination) compared to formally-connected areas, and JNNURM's mandated land/tenure and governance reforms (Urban Land Ceiling repeal, participatory 74th Amendment implementation) were identified as key levers for improving water access for the urban poor",
    study_design="policy-document analysis with descriptive water-quality sampling data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed statutory/policy analysis (JNNURM reform conditions, Urban Land Ceiling repeal, tenure documentation requirements) directly linked to empirical water-quality/source-type sampling data showing the tenure-documentation access-control mechanism in resettlement colonies.",
    source_document="Roy, Akshintala & Sharma 2013, Social Change (retrieved via Google Drive)",
    figure="Figures 4, 6-9",
    section="JNNURM reform analysis and resettlement-colony water-quality findings",
    exact_location="Sections on JNNURM reforms and water-quality sampling results",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct statutory/policy analysis of tenure-documentation as a water-access-control mechanism, supported by primary water-quality sampling data across resettlement colonies. NOT effect_sizes eligible: descriptive sampling data by source type, no regression-based estimate isolating a legal/institutional mechanism's effect. Extracted for record_id RD601DD13E14F.",
    )

# S800 - Lewis - Kenya public infrastructure
add("S800",
    citation="Lewis BD (1998). The impact of public infrastructure on municipal economic development: Empirical results from Kenya. Regional Urban and Regional Development Studies.",
    doi="10.1111/j.1467-940X.1998.tb00092.x",
    publication_year="1998",
    country="Kenya",
    subnational_unit="32-35 municipalities",
    legal_system="common law",
    urban_rural="urban",
    service_provider="central government water authority vs. local municipal government",
    regulatory_model="OLS and 2SLS regression analysis of 32-35 Kenyan municipalities testing whether local (vs. central) government administrative authority over water infrastructure (dummy variable D2) affects infrastructure quantity and quality, plus a separate comparison of water-access time and service-reliability ratings by administrative-authority type",
    population="residents of 32-35 Kenyan municipalities",
    sample_size="32-35 municipalities",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    water_access="TRUE", service_reliability="TRUE",
    effect_measure="OLS/2SLS regression (Table 1, infrastructure quantity/quality on local-vs-central authority dummy D2) and difference-of-means comparison (Table 3, water-access time and reliability by authority type)",
    effect_estimate="Table 1: local-vs-central administrative authority (D2) was not a statistically significant predictor of water infrastructure quantity in the OLS/2SLS models. Table 3: municipalities with local government authority over water infrastructure had shorter average water-access time (5.4 minutes) than centrally-administered municipalities (21.4 minutes), significant at the 0.04 level, and a higher share of residents rating supply as reliable (87.2% local vs. 72.4% central), significant at the 0.07 level",
    lower_CI="", upper_CI="", standard_error="",
    p_value="0.04 (Table 3 access-time comparison); 0.07 (Table 3 reliability comparison); not significant (Table 1 D2 coefficient)",
    extraction_sample_size="32-35 municipalities",
    adjusted_or_unadjusted="unadjusted (Table 3 difference-of-means); adjusted (Table 1 OLS/2SLS with municipal covariates)",
    covariates="municipal population, revenue base, and other infrastructure-determinant controls (Table 1 models)",
    model_type="OLS/2SLS regression (Table 1); difference-of-means comparison (Table 3)",
    study_design="cross-sectional municipal-level regression and comparison analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: direct empirical test of local-vs-central administrative authority (a legal/institutional mechanism) on water-access outcomes across Kenyan municipalities; the multivariate regression (Table 1) found no significant infrastructure-quantity effect, while the significant access-time/reliability findings (Table 3) rest on an unadjusted difference-of-means comparison rather than a full regression.",
    source_document="Lewis 1998, RURDS (retrieved via Google Drive)",
    table="Tables 1, 3",
    section="Empirical results",
    exact_location="Table 1 (OLS/2SLS results) and Table 3 (access-time/reliability comparison)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct empirical test of local-vs-central administrative authority as an institutional mechanism affecting water-infrastructure and access outcomes. NOT effect_sizes eligible: Table 1's regression finds D2 not significant for infrastructure quantity, and Table 3's significant access-time/reliability findings are an unadjusted difference-of-means comparison, not a full regression-based estimate isolating the mechanism -- consistent with the established precedent (S724, S761) excluding simple chi-square/ANOVA/t-test comparisons from effect_sizes eligibility. Extracted for record_id RD460C6C5BA82.",
    )

# S801 - Townsend & Eyles - Tijuana Mexico
add("S801",
    citation="Townsend K, Eyles J (2004). Capacity and transparency of potable water regulation in Tijuana, Mexico: Challenges for ensuring water quality at community level. Health Promotion International.",
    doi="10.1093/heapro/dag406",
    publication_year="2004",
    country="Mexico",
    subnational_unit="Tijuana",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Ministry of Public Health, CESPT (Tijuana municipal water utility)",
    regulatory_model="Qualitative key-informant study (30 interviews) examining institutional capacity gaps between Ministry of Public Health and CESPT water-utility departments, documenting clientelism and political favoritism circumventing formal bureaucratic procedures for water-bill reductions, and describing unregulated private water-truck distribution serving unconnected communities",
    population="Tijuana residents, including unconnected communities served by informal water-truck distribution",
    sample_size="30 key-informant interviews",
    household_level="TRUE", community_level="TRUE",
    discretion="TRUE", discretion_accommodation="TRUE", bureaucratic_assistance="TRUE",
    institutional_fragmentation="TRUE", formal_connection="TRUE",
    water_access="TRUE", service_quality="TRUE",
    effect_measure="qualitative key-informant interview study (30 interviews)",
    effect_estimate="Institutional capacity gaps and poor coordination between the Ministry of Public Health and CESPT undermine effective potable-water regulation in Tijuana; clientelism and political favoritism, rather than formal bureaucratic procedure, determine which households obtain water-bill reductions, while unconnected communities rely on unregulated private water-truck vendors outside formal regulatory oversight",
    study_design="qualitative key-informant interview study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: 30 key-informant interviews directly documenting discretionary/clientelistic administrative practice (vs. formal bureaucratic procedure) as the mechanism determining water-bill relief and access, plus institutional fragmentation between health and utility regulators.",
    source_document="Townsend & Eyles 2004, Health Promotion International (retrieved via Google Drive)",
    section="Findings from key-informant interviews",
    exact_location="Results and discussion sections",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary key-informant interview study directly documenting discretionary/clientelistic administrative practice as an access-control mechanism, and institutional fragmentation between health and water-utility regulators, plus informal water-truck distribution to unconnected communities. NOT effect_sizes eligible: qualitative interview study, no regression-based estimate. Extracted for record_id RD1C3B399E90B.",
    )

# S802 - Brady & Gray - Ireland water pricing
add("S802",
    citation="Brady J, Gray NF (2013). Analysis of water pricing in Ireland and recommendations towards a more efficient water sector. Water Policy.",
    doi="10.2166/wp.2013.051",
    publication_year="2013",
    country="Ireland",
    subnational_unit="34 local authorities and 104 Group Water Schemes (GWSs)",
    legal_system="common law",
    urban_rural="both",
    service_provider="34 local authorities (public supply) and 104 Group Water Schemes (community/private supply)",
    regulatory_model="Survey-based analysis of 104 Group Water Schemes and 34 local authorities documenting Ireland's fragmented, decentralised rural water sector, in which unregulated, locally-set GWS volumetric tariffs average 35% lower than public local-authority supply charges, and recommending consolidation toward a proposed national water authority to address the fragmentation and pricing inconsistency",
    population="rural and public-supply water users, Ireland",
    sample_size="104 Group Water Schemes and 34 local authorities surveyed",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE",
    water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="survey-based descriptive comparison of tariff-setting practices across 104 GWSs and 34 local authorities",
    effect_estimate="Ireland's decentralised, unregulated tariff-setting produces a 35% average gap between lower Group Water Scheme volumetric charges and higher public local-authority supply charges, reflecting institutional fragmentation across 34 local authorities and 104 community-managed schemes with no unified national pricing or regulatory authority; the authors recommend establishing a national water authority to harmonise pricing and improve sector efficiency",
    study_design="cross-sectional survey of water-sector governance and pricing structures",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: original survey data across 104 Group Water Schemes and 34 local authorities directly documenting institutional fragmentation in water-sector governance and its consequence for unregulated, inconsistent tariff-setting.",
    source_document="Brady & Gray 2013, Water Policy (retrieved via Google Drive)",
    section="Survey results and sector-fragmentation analysis",
    exact_location="Sections on GWS/local-authority survey and pricing comparison",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original survey-based empirical analysis of institutional fragmentation (104 GWSs, 34 local authorities) and its effect on unregulated, inconsistent water tariff-setting in Ireland. NOT effect_sizes eligible: descriptive survey comparison of average tariff levels, no regression-based estimate isolating the fragmentation mechanism's effect. Extracted for record_id RD17D28844F71.",
    )

# S803 - Vasquez - Guatemala official perceptions
add("S803",
    citation="Vasquez WF (2011). Municipal water services in Guatemala: exploring official perceptions. Water Policy.",
    doi="10.2166/wp.2010.211",
    publication_year="2011",
    country="Guatemala",
    subnational_unit="municipalities",
    legal_system="civil law",
    urban_rural="both",
    service_provider="municipal water utilities",
    regulatory_model="Semi-structured interviews with government water-service officers examining official perceptions of the institutional determinants of low municipal water-service quality, including political will, institutional development, investment levels, regulatory compliance, and citizen participation",
    population="municipal water-service officials, Guatemala",
    sample_size="semi-structured interviews with government water-service officers",
    household_level="", community_level="TRUE",
    discretion_accommodation="TRUE", participation="TRUE", political_coordination="TRUE",
    water_access="TRUE", service_quality="TRUE", service_reliability="TRUE",
    effect_measure="qualitative semi-structured interview study with government officials",
    effect_estimate="Municipal water officials identify insufficient political will, weak institutional development, inadequate investment, poor regulatory compliance, and low citizen participation as the primary institutional determinants of low municipal water-service quality in Guatemala's fragmented water sector, corroborating findings from the companion household-survey study (Vasquez 2015) documenting divergent household satisfaction across municipal and community-managed systems",
    study_design="qualitative semi-structured interview study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: primary interview data directly from government water officials identifying specific institutional determinants (political will, compliance, participation) of water-service quality, complementing the companion household-level study (S794) with an official-perspective institutional account.",
    source_document="Vasquez 2011, Water Policy (retrieved via Google Drive)",
    section="Findings from official interviews",
    exact_location="Results and discussion sections",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary semi-structured interview study with government water officials directly identifying institutional determinants of water-service quality, companion study to the already-included S794 Vasquez 2015 household WTP/WTW paper. NOT effect_sizes eligible: qualitative interview study, no regression-based estimate. Extracted for record_id RD0D63BD0DF34.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
