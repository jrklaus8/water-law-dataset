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

# S949 - Nelson-Nunez, Walters & Charpentier - Chile rural water services, Law No. 20.998
add("S949",
    citation="Nelson-Nunez J, Walters JP, Charpentier D (2019). Exploring the challenges to sustainable rural drinking water services in Chile. Water Policy.",
    doi="10.2166/wp.2019.120",
    publication_year="2019",
    country="Chile",
    subnational_unit="nationwide (rural water services)",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="community-managed rural water organizations (Comites/Cooperativas de Agua Potable Rural, APR) operating under Chile's new Law No. 20.998 (2017), which strengthens central-government regulatory capacity and responsibility over rural water organizations relative to private and local-government actors",
    regulatory_model="Delphi study (2016, prior to the law's passage) of Chilean rural water-sector experts identifying factors influencing rural water-service sustainability, used to assess the implications of Chile's newly passed Law No. 20.998 (2017), which departs from other Latin American countries' decentralization trend by weakening the role of private actors and building central-government regulatory capacity and responsibility over rural water organizations, with a 3-year implementation window",
    population="Chilean rural water-service users under the new Law No. 20.998 governance framework",
    sample_size="Delphi panel of Chilean rural water-sector experts (2016)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE", service_continuity="TRUE",
    effect_measure="Delphi expert-consensus study assessing a newly enacted national legal reform",
    effect_estimate="Chile's rural water-service coverage rose substantially under the prior community-managed governance model, but service quality, tariff collection equity, and sustainability challenges persisted even at near-universal coverage; the 2016 Delphi study of rural water experts identified disparate views on which actors (central government, private sector, or community organizations) should take the lead role in addressing these deficiencies, informing the design of the 2017 Law No. 20.998, which took the notable step of strengthening central-government regulatory capacity and conferring more responsibility on rural water organizations rather than following the region's typical decentralization/privatization trend; the study concludes that successfully implementing this sweeping institutional/legal reform within its 3-year window poses significant governance-transition challenges even in a country close to universal rural water coverage.",
    study_design="Delphi expert-consensus study with policy-implementation analysis of a national legal reform",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original Delphi expert-consensus study directly examining expert perspectives on a specific, newly enacted national legal reform's (Law No. 20.998) implications for rural water-service governance and sustainability outcomes.",
    source_document="Nelson-Nunez, Walters & Charpentier 2019, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national legal-reform institutional-analysis inclusion precedent (Guidi Gutierrez Sucre Bolivia; Larrain Chile Water Code): original expert-consensus study directly examining a specific national legal reform's design and implementation challenges for rural water-service governance. NOT effect_sizes eligible: Delphi expert-consensus study, no regression-based estimate. Extracted for record_id R6727B5865609.",
    )

# S950 - O'Reilly & Dhanju - Rajasthan caste public taps/private connections
add("S950",
    citation="O'Reilly K, Dhanju R (2014). Public taps and private connections: the production of caste distinction and common sense in a Rajasthan drinking water supply project. Transactions of the Institute of British Geographers.",
    doi="10.1111/tran.12064",
    publication_year="2014",
    country="India",
    subnational_unit="rural Rajasthan",
    legal_system="common law",
    urban_rural="rural",
    service_provider="village-scale water-governance institutions administering a drinking-water-supply project combining public taps and payment for water, operating under state power and neoliberal-reform water-sector policy",
    regulatory_model="Longitudinal ethnography (construction and post-construction phases) of a rural Rajasthan drinking-water-supply project explicitly designed to create greater cross-caste equality through public taps and universal water payment, examining how upper-caste, wealthy households and the village-scale institutions supporting them deployed counter-technologies (private connections, altered water-governance norms) in the post-construction phase to undermine the project's equity goals and re-produce caste-based water-access distinctions",
    population="rural Rajasthan village residents across caste groups served by the water-supply project",
    sample_size="single-project longitudinal ethnography across construction and post-construction phases",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="longitudinal ethnographic analysis of village water-governance institutions",
    effect_estimate="Although the drinking-water-supply project was deliberately designed to promote caste equality through a combination of shared public taps and universal payment for water, in the post-construction phase upper-caste, wealthier households successfully leveraged village-scale water-governance institutions and state power to establish private household connections and to redefine the meaning of 'proper' water access and payment, undermining both the project's social equity goals and its physical shared-tap infrastructure; the study demonstrates how neoliberal water-governance reforms, rather than being caste-neutral, become mutually constituted with and deepen pre-existing caste inequalities through village-institutional processes operating after formal project completion.",
    study_design="longitudinal ethnography (construction and post-construction phases) of a single water-supply project",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original longitudinal ethnographic fieldwork directly documenting how village-scale water-governance institutions and state power produced caste-differentiated water-access outcomes over the construction and post-construction phases of a specific water-supply project.",
    source_document="O'Reilly & Dhanju 2014, Transactions of the Institute of British Geographers (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established caste/institutional-discrimination inclusion precedent (Johnson et al Mebane NC racial apartheid, this same segment): original longitudinal ethnography directly documenting how village-scale water-governance institutions and state power produced caste-differentiated water-access outcomes. NOT effect_sizes eligible: longitudinal ethnographic case study, no regression-based estimate. Extracted for record_id R662825EA0EAA.",
    )

# S951 - Ennis-McMillan - Suffering from Water, Mexico
add("S951",
    citation="Ennis-McMillan MC (2001). Suffering from Water: Social Origins of Bodily Distress in a Mexican Community. Medical Anthropology Quarterly.",
    doi="10.1525/maq.2001.15.3.368",
    publication_year="2001",
    country="Mexico",
    subnational_unit="La Purificacion, a foothill community in the Valley of Mexico",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="community drinking-water management system administered by local civil and religious officials in La Purificacion",
    regulatory_model="Critical medical anthropology ethnography combining participant-observation of domestic water use and community drinking-water management with interviews of local civil and religious officials who monitor the water-distribution system, examining how residents' local discourse of 'suffering from water' reflects the social and institutional conditions -- including community water-governance and distribution-management practices -- that limit residents' access to an adequate domestic water supply in a semiarid, water-scarce setting",
    population="residents of La Purificacion, a foothill community in the Valley of Mexico",
    sample_size="single-community ethnography with participant-observation and interviews of local water-management officials",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", discretion="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="ethnographic participant-observation and interviews with local water-management officials",
    effect_estimate="Residents of La Purificacion experience chronic water scarcity as a form of embodied social suffering shaped directly by the community's local drinking-water management institutions -- administered by civil and religious officials responsible for water distribution -- and by individual and collective struggles to obtain adequate domestic water within this local governance system; the study documents specific institutional and social strategies residents employ (individually and collectively) to address the community-level governance and distribution conditions underlying their water-access hardship, demonstrating that the local water-management institution's decisions and practices, not merely physical water scarcity, directly determine differential household water-access outcomes.",
    study_design="single-community ethnography with participant-observation and interviews of local water-management officials",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original ethnographic fieldwork, including interviews with local water-management officials, directly linking community water-governance institutional practices to differential household water-access hardship, though framed primarily through a medical-anthropology lens.",
    source_document="Ennis-McMillan 2001, Medical Anthropology Quarterly (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-narrative ethnographic inclusion precedent (Hellberg eThekwini; Kotsila & Saravanan): original ethnographic fieldwork including interviews with local water-management institutional officials directly linking community water-governance practices to household water-access outcomes. NOT effect_sizes eligible: single-community ethnography, no regression-based estimate. Extracted for record_id R6D53C0A6E3A4.",
    )

# S952 - Rammelt et al - Toxic injustice Bangladesh arsenic
add("S952",
    citation="Rammelt C, Masud Z, Boes J, Masud F (2014). Toxic injustice in the Bangladesh water sector: a social inequities perspective on arsenic contamination. Water Policy.",
    doi="10.2166/wp.2013.184",
    publication_year="2014",
    country="Bangladesh",
    subnational_unit="rural communities served by the Arsenic Mitigation and Research Foundation",
    legal_system="common law",
    urban_rural="rural",
    service_provider="the Arsenic Mitigation and Research Foundation (AMRF), an NGO implementing drinking-water-supply and health-support schemes with marginalized communities, framed against the backdrop of governance failure by state public-health programs",
    regulatory_model="Case study and program-implementation analysis of the Arsenic Mitigation and Research Foundation's (AMRF) efforts to implement drinking-water supplies and health-support schemes with marginalized rural Bangladeshi communities facing arsenic-contaminated groundwater, examining the arsenic crisis as a governance failure and structural injustice, and analyzing the implications of framing the response in terms of social justice and human rights versus AMRF's actual social-mobilization and fundamental-human-needs-based approach",
    population="rural Bangladeshi communities affected by arsenic-contaminated groundwater, served by AMRF programs",
    sample_size="program case study of AMRF's drinking-water and health-support scheme implementation with marginalized communities",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE", bureaucratic_assistance="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="NGO program-implementation case study with governance/rights-based policy analysis",
    effect_estimate="Public health programs addressing arsenic contamination of groundwater in Bangladesh -- described as one of the worst mass poisonings in history -- were found to be short-lived and unevenly distributed, reflecting a governance failure and structural injustice of global dimensions; the Arsenic Mitigation and Research Foundation's alternative approach, focused on social mobilization and securing fundamental human needs rather than an explicit rights-based framing, is shown to implement effective drinking-water-supply and health-support schemes with marginalized communities, with the study arguing that this social-mobilization approach creates the political and social space necessary for pursuing formal human-rights claims to safe water, demonstrating how institutional/governance design choices (state program failure versus NGO social-mobilization implementation) directly determine differential water-access outcomes for marginalized arsenic-affected communities.",
    study_design="NGO program-implementation case study with governance and social-justice policy analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: program-implementation case study directly linking institutional/governance design (state public-health program failure vs. NGO social-mobilization implementation) to differential water-access outcomes for marginalized communities, though without a quantified comparative estimate.",
    source_document="Rammelt, Masud, Boes & Masud 2014, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established governance-failure/rights-based-implementation inclusion precedent (Grimes-type human-rights-water-governance studies distinguished by original program documentation; Mallick Bangladesh participatory action-research, this segment): original NGO program-implementation case study directly linking governance/institutional design to marginalized-community water-access outcomes. NOT effect_sizes eligible: program-implementation case study, no regression-based estimate. Extracted for record_id R61C9559AE0A2.",
    )

# S953 - De & Nag - Local self-governance, ethnic division, Kolkata slums
add("S953",
    citation="De I, Nag T (2016). Local self-governance, ethnic division in slums and preference for water supply institutions in Kolkata, India. Water Policy.",
    doi="10.2166/wp.2015.127",
    publication_year="2016",
    country="India",
    subnational_unit="Kolkata slums",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Kolkata Municipal Corporation local self-governance (municipal councilors), operating under India's 74th Constitutional Amendment establishing local self-governance for basic-service delivery, with formal notified vs. informal non-notified (NN) slum legal status as a key institutional distinction",
    regulatory_model="Household survey study investigating slum dwellers' preferences for alternative institutional arrangements for water supply (privatization vs. paid public delivery) across ethnic communities (Hindu general caste, Muslim, Scheduled Caste/Scheduled Tribe) in Kolkata slums, and a logit regression analysis of household perceptions of municipal councilor accountability/awareness regarding water-supply conditions, examining how formal slum notification status (notified vs. non-notified, NN) and ethnic identity affect access to local self-governance accountability mechanisms under India's 74th Constitutional Amendment",
    population="households in notified and non-notified (NN) slums across ethnic communities in Kolkata, India",
    sample_size="household survey across ethnically diverse notified and non-notified Kolkata slums",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", documentation="TRUE", administrative_review="TRUE", complaint="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="household survey with logit regression of councilor-accountability perception on slum legal status and ethnic identity",
    effect_estimate="Institutional preferences for water supply differ systematically by ethnic community: Muslim households prefer privatized water supply over paid public delivery, backward-caste households prefer both paid public delivery and privatization, while residents of non-notified (NN, i.e., legally unrecognized) slums prefer paid public delivery over privatization; access to local-government accountability mechanisms -- measured as household perception of municipal councilor awareness of water-supply conditions -- is significantly lower for residents of Muslim-dominated regions and non-notified slums, and the logit regression confirms that NN legal status, ethnic identity (Muslim, SC/ST), and councilor political affiliation are significant determinants of this accountability-perception outcome, leading the authors to recommend formal notification of NN slums, greater local-body revenue autonomy and capacity, and scale-neutral technological innovations as institutional reforms to improve marginalized communities' access to water supply.",
    table="logit regression results (AWARE outcome regressed on NN slum legal status, ethnic identity, migration status, literacy, councilor party affiliation, and interaction terms)",
    study_design="household survey with logit regression analysis across ethnically diverse notified/non-notified slums",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original household survey with logit regression directly isolating the effect of formal slum legal-notification status and ethnic identity on local-government water-supply accountability outcomes.",
    source_document="De & Nag 2016, Water Policy (retrieved via Google Drive)",
    section="Section 8; Table (regression results)",
    exact_location="Section 8.1",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established slum-legal-status/ethnic-discrimination institutional inclusion precedent (Wahby Cairo; Kujinga Botswana gazetted/ungazetted, this segment): original household survey with logit regression directly linking formal slum notification legal status and ethnic identity to local-government water-supply accountability outcomes. NOT effect_sizes eligible: the regression outcome is household perception of councilor accountability/awareness, not a direct connection/access/quantity/reliability outcome under the Family A/B/C framework -- an accountability-perception measure, not an access outcome. Extracted for record_id R5DEA9225B1BF.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
