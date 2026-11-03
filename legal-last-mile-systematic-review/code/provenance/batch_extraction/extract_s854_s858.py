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

# S854 - Razavi - Social control and water remunicipalization, Cochabamba
add("S854",
    citation="Razavi NS (2019). 'Social Control' and the Politics of Public Participation in Water Remunicipalization, Cochabamba, Bolivia. Water.",
    doi="10.3390/w11071455",
    publication_year="2019",
    country="Bolivia",
    subnational_unit="Cochabamba",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="SEMAPA (municipal public water utility)",
    regulatory_model="Doctoral-fieldwork-based institutional case study of Cochabamba's post-Water War (2000) water remunicipalization, examining the 'social control' participatory-governance model for SEMAPA and building a typology of participation types (intentionality, outcomes, tools, practices) to explain why transformative participation failed to take hold, documenting how the northern/central-zone SEMAPA service area suffers chronic shortages from an obsolete distribution network while the marginalized southern zone remains largely unconnected to the municipal network and relies on autonomous, self-governed small-scale water providers",
    population="Cochabamba residents, particularly marginalized southern-zone peri-urban communities",
    sample_size="doctoral fieldwork (interviews and participant observation) with SEMAPA officials, participation-committee members, and peri-urban residents",
    household_level="TRUE", community_level="TRUE",
    participation="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", sanitation_access="TRUE",
    effect_measure="institutional/political-governance case study",
    effect_estimate="Nearly two decades after Cochabamba's Water War remunicipalized SEMAPA, the promised participatory 'social control' governance model remains largely unrealized; SEMAPA-connected residents in the north/center face chronic shortages from an obsolete distribution network, while the most marginalized southern-zone peri-urban populations are largely not directly connected to the municipal network at all and rely instead on autonomous small-scale water providers, with correspondingly higher rates of pollution and water-borne illness, demonstrating that the specific institutional/participatory governance design of the remunicipalized utility has failed to resolve underlying access inequality",
    study_design="institutional/political-governance case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: doctoral fieldwork directly documenting the specific participatory-governance ('social control') institutional design of a remunicipalized water utility and its persistent failure to resolve documented connection disparities between service zones.",
    source_document="Razavi 2019, Water (retrieved via Google Drive)",
    section="Introduction; typology of participation applied to Cochabamba",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional/political-governance case study directly documenting a specific participatory-governance design (SEMAPA 'social control') and its persistent failure to resolve zone-based water-connection disparities. NOT effect_sizes eligible: institutional case study, no regression-based estimate. Extracted for record_id RFEE77DC1C510.",
    )

# S855 - Kumasi & Agbemor - Tracking user satisfaction of rural water services, Ghana
add("S855",
    citation="Kumasi TC, Agbemor BD (2018). Tracking user satisfaction of rural water services in northern Ghana. Journal of Water, Sanitation and Hygiene for Development.",
    doi="10.2166/washdev.2018.140",
    publication_year="2018",
    country="Ghana",
    subnational_unit="Bongo, Gushiegu, and Wa East districts",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Water and Sanitation Management Teams (WSMT-SC/WSMT-ST) under district assemblies (legal owners) and Community Water and Sanitation Agency (CWSA) national standards",
    regulatory_model="Household survey (1,181 households, filtered to 1,010 handpump-using households) comparing user satisfaction against actual service-monitoring data, within Ghana's decentralized Community Ownership and Management (COM) model under which legal ownership of rural water infrastructure is vested in district assemblies (service authorities) who hold assets in trust for communities, with WSMTs as service providers responsible for tariff-setting, maintenance, and financial management per CWSA national norms and benchmarks",
    population="rural households using handpump water services in three northern Ghana districts",
    sample_size="1,181 household surveys (1,010 after filtering to handpump users)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    water_access="TRUE", service_quantity="TRUE", service_reliability="TRUE", affordability="TRUE",
    effect_measure="comparative household survey vs. service-monitoring benchmark data",
    effect_estimate="Under Ghana's decentralized Community Ownership and Management model, WSMTs (community-level service providers accountable to district assemblies as legal asset owners) failed to meet the majority of CWSA financial-management benchmarks (e.g., only 0-12% met tariff-setting and financial-management indicators across the three districts), and only 10% of handpumps had established a formal water tariff at all; despite this, 87% of users were unwilling to pay for water and a large majority expressed satisfaction with service-provider performance even where WSMTs failed most institutional benchmarks, indicating a persistent gap between the decentralized legal/institutional accountability structure and actual community water-governance capacity",
    study_design="comparative household survey with institutional benchmark data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: large household survey (1,010-1,181 respondents) directly compared against a specific national institutional benchmark framework (CWSA WSMT performance indicators) tied to a documented legal decentralization structure (district assemblies as trustee-owners).",
    source_document="Kumasi & Agbemor 2018, Journal of Water, Sanitation and Hygiene for Development (retrieved via Google Drive)",
    table="Table 3 (WSMT benchmark compliance); Table 4 (dissatisfaction reasons)",
    section="Results and Discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: large household survey directly documenting a specific decentralized legal/institutional community-water-management structure (district assemblies as trustee-owners, WSMT service providers, CWSA national benchmarks) and its performance gaps. NOT effect_sizes eligible: descriptive comparative survey, no regression-based estimate. Extracted for record_id RB57945A09D4B.",
    )

# S856 - Spencer, Meng, Nguyen & Guzinsky - Innovations in Local Governance, Southeast Asia
add("S856",
    citation="Spencer JH, Meng B, Nguyen H, Guzinsky C (2008). Innovations in Local Governance: Meeting Millennium Development Goal number 7 in Southeast Asia. Development.",
    doi="10.1057/dev.2008.16",
    publication_year="2008",
    country="Vietnam; Cambodia; Indonesia",
    subnational_unit="Can Tho and Ha Noi (Vietnam); Phnom Penh (Cambodia); Gresik (Indonesia)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Can Tho City Water Company; Ha Noi Water Business Company (HWBC) and community Water Management Units (WMU); Phnom Penh Water Supply Authority (PPWSA); PDAM (Indonesia) and community-financed deep wells",
    regulatory_model="Comparative documentation of four institutional/contractual innovations for extending water access to the urban poor: Can Tho's landowner-Water Company-People's Committee well-digging/connection contract; Ha Noi's bulk-water lease contract between HWBC and the Co Nhue People's Committee with a community-selected Water Management Unit retailing water; Phnom Penh's PPWSA cross-subsidy program (30/50/70/100% subsidy tiers with amortized installment payments) for poor households' connection costs; and Gresik's community-financed deep-well systems funded by residents, religious institutions, and village government where PDAM does not extend service",
    population="urban poor households in peri-urban Vietnam, Cambodia, and Indonesia lacking formal piped-water connections",
    sample_size="four detailed institutional case studies with original interview and documentary data (including Director General of PPWSA interview, June 2007)",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="comparative institutional case study with quantified programme outcomes",
    effect_estimate="Phnom Penh's PPWSA cross-subsidy connection programme had provided subsidized connections to 14,872 poor households by May 2007, alongside education and local cashier stations to reduce transaction costs for the poor, but coverage remained restricted to households within 10 m of PPWSA's main distribution pipes; in Ha Noi's Co Nhue community, poor institutional/financial management by the community Water Management Unit produced a high non-revenue-water rate (42-59%) such that only 1,500 of roughly 3,500 registered households had intermittent piped access by mid-2007, while paying more than double the wholesale tariff; in Can Tho, a landowner-utility-government contracting arrangement successfully extended well access to new peri-urban areas by aligning landowner, utility, and local-government incentives",
    study_design="comparative institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: four detailed, original-source institutional case studies directly documenting specific contractual/subsidy mechanisms and their quantified household-level connection and reliability outcomes.",
    source_document="Spencer, Meng, Nguyen & Guzinsky 2008, Development (retrieved via Google Drive)",
    section="Innovations in local water governance in Southeast Asia (Can Tho, Ha Noi, Phnom Penh, Gresik case studies)",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original documentary/interview-based case studies (not a secondary review) directly documenting specific institutional/contractual mechanisms (cross-subsidy programmes, bulk-water lease contracts, landowner-utility contracts) and their quantified household-level water-access outcomes. NOT effect_sizes eligible: comparative case study, no regression-based estimate. Extracted for record_id R9432B4531BC0.",
    )

# S857 - Akpabio - Water and People, Akwa Ibom Nigeria
add("S857",
    citation="Akpabio EM (2011). Water and People: Perception and Management Practices in Akwa Ibom State, Nigeria. Society & Natural Resources.",
    doi="10.1080/08941920903496945",
    publication_year="2011",
    country="Nigeria",
    subnational_unit="Akwa Ibom State (Ikono, Essien Udim, Oron local government areas)",
    legal_system="common law (customary law pluralism)",
    urban_rural="rural",
    service_provider="traditional/customary institutions (village councils, traditional rulers) and Cross River Basin Development Authority (CRBDA), a state water development agency",
    regulatory_model="Ethnographic study (60 household interviews, 12 key informants, 18 focus groups across six villages) documenting seven types of customary land-holding systems affecting water-source access and traditional (nonstate, socially-embedded) water-governance institutions, contrasted with the bureaucratic/formal water-management principles (cost recovery, private water rights) of the state CRBDA, examining documented conflicts between the CRBDA and host communities at Abak and Itu over modern water-supply and irrigation projects",
    population="rural residents of six villages across three ethnic domains in Akwa Ibom State",
    sample_size="60 household interviews, 12 key informants, 18 focus groups across 6 villages",
    household_level="TRUE", community_level="TRUE", legal_status="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE", discretion="TRUE",
    water_access="TRUE",
    effect_measure="ethnographic case study (household interviews, key informant interviews, focus groups)",
    effect_estimate="Customary land-tenure systems (seven distinct traditional land-holding categories) directly determine water-source access rights (individual land holdings confer groundwater rights, while surface water remains communal regardless of land-holding type), and traditional institutions enforce access rules via spiritual/customary sanctions rather than state law; where the state's CRBDA has attempted to impose modern cost-recovery and private-water-rights principles at Abak and Itu, this has directly conflicted with communities' customary 'free gift from nature' water norms, producing persistent, unresolved conflict and undermining state water-project goals",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: structured ethnographic fieldwork (interviews, key informants, focus groups across six villages) directly documenting customary land-tenure/water-rights institutions and their conflict with a specific state water-development authority's cost-recovery/private-rights framework.",
    source_document="Akpabio 2011, Society & Natural Resources (retrieved via Google Drive)",
    section="Study Approach; Results; Implications for State Institutions",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established customary/Indigenous water-governance inclusion precedent: ethnographic study directly documenting customary land-tenure water-rights institutions in conflict with a state water-development authority's formal legal/regulatory framework. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R960A96145969.",
    )

# S858 - Cleaver & Toner - Community water governance in Uchira, Tanzania
add("S858",
    citation="Cleaver F, Toner A (2006). The evolution of community water governance in Uchira, Tanzania: The implications for equality of access, sustainability and effectiveness. Natural Resources Forum.",
    doi="10.1111/j.1477-8947.2006.00115.x",
    publication_year="2006",
    country="Tanzania",
    subnational_unit="Uchira village",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Uchira Water Users Association (UWUA)",
    regulatory_model="Longitudinal ethnographic case study of the Uchira Water Users Association's institutional evolution under Tanzania's national water policy (2002), which devolves water management responsibility, ownership, and cost-sharing to community-owned institutions without specifying accountability mechanisms or means of protecting the poorest and most vulnerable users, examining the resulting contested nature of 'community ownership' and tensions between equity and sustainability principles in practice",
    population="Uchira village residents, Tanzania",
    sample_size="longitudinal ethnographic fieldwork with the Uchira Water Users Association",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", participation="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="longitudinal ethnographic case study",
    effect_estimate="Tanzania's 2002 water policy assumes local communities are homogeneous and equally able to pay, devolving water management to community-owned institutions without specifying mechanisms for accountability to users or protection of the poorest and most vulnerable; the Uchira Water Users Association case demonstrates that 'community ownership' is contested and unevenly realized in practice, undermining assumptions that decentralized community management automatically delivers equitable and sustainable access, with equity and sustainability goals found to be in tension rather than mutually reinforcing",
    study_design="longitudinal ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: longitudinal ethnographic fieldwork directly documenting a specific national water-policy decentralization mandate (Tanzania 2002) and its institutional implementation and equity consequences in a single well-studied community water association.",
    source_document="Cleaver & Toner 2006, Natural Resources Forum (retrieved via Google Drive)",
    section="Towards understanding water management in Uchira",
    exact_location="Section 5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: longitudinal ethnographic case study directly documenting a specific national water-policy decentralization mandate and its institutional/equity consequences for a community water-management association. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R706C98313920.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
