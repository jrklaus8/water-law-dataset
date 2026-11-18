#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-28"
DATE = "2026-09-28"

# RC8E1C6959D2C was flagged wrong_file_retrieved in Batch 236 (delivered content
# was an unrelated Kampala, Uganda paper). During reconciliation of a large new
# Sep-26-2026 Drive delivery, the file delivered under a DIFFERENT record_id,
# R023B3A0D827A, was found -- by direct full-text reading -- to actually contain
# RC8E1C6959D2C's real target citation (Samano Romero & Chavez-Mejia 2025,
# "Water Access in Mexico City: A Review of Local Research Approaches"). This is
# a cross-contamination/mislabeling in the delivery tool's own retrieval process,
# not a mapping error on this pipeline's end (confirmed via each result's own
# .viewUrl/.title fields). RC8E1C6959D2C is corrected to INCLUDE here, using the
# content found under R023B3A0D827A's fileId; R023B3A0D827A itself is flagged
# wrong_file_retrieved below for ITS OWN target citation (a different paper,
# Pablos et al. 2014, Sonora river watershed management), which remains
# unretrieved.
INCLUDES = {
    "RC8E1C6959D2C": (
        "Samano Romero & Chavez-Mejia 2025 (Wiley Interdisciplinary Reviews: Water), "
        "'Water Access in Mexico City: A Review of Local Research Approaches.' Genuine "
        "literature review/research synthesis covering historical, sociospatial, and "
        "quantitative domains of academic literature on water access in Mexico City, "
        "addressing water governance, infrastructure development, tariff/affordability "
        "issues, and spatially/socially stratified water-supply inequality (98.8% official "
        "connection rate vs. documented pressure/continuity/quality/affordability "
        "shortfalls). Genuine institutional/governance-relevant empirical-literature "
        "synthesis of water-service access. CORRECTION NOTE: this record was previously "
        "flagged wrong_file_retrieved (Batch 236) after a different, unrelated Kampala/"
        "Uganda paper was delivered under this record_id. The correct target content was "
        "subsequently found -- by direct full-text reading during a later delivery's "
        "reconciliation -- mislabeled under an unrelated record_id, R023B3A0D827A, in the "
        "Sep-26-2026 Drive delivery. Confirmed via the read tool's own .viewUrl/.title "
        "fields that this was a genuine content-labeling error in the delivery tool's "
        "output, not a mapping error on this pipeline's end. Screened and included using "
        "that content; R023B3A0D827A is separately flagged wrong_file_retrieved below for "
        "its own, still-unretrieved target citation."
    ),
}

EXCLUDES = {}

WRONG_FILE = {
    "R000DF300E5DF": "Target: Palleschi 2013, 'EPA Plans Talks with Cities on Water Costs but Resists Call for Overhaul' (news article). Delivered: Wang & Li, 'Governance and Finance: Availability of Community and Social Development Infrastructures in Rural China' (2018) -- unrelated paper.",
    "R0024ADA0FEB9": "Target: Pigden 2018, 'Are water firms delivering?'. Delivered: Atem et al. 2026, 'Barriers to Effective Water Resource Management in Foumbot, Cameroon' -- content-behind-filename mismatch (filename matched exactly).",
    "R0086649A35D6": "Target: Walker 2011, 'Enclosing the commons? A political ecology of access to land and water in Sussundenga, Mozambique'. Delivered: Mdee et al. 2025, 'On a journey to citywide inclusive sanitation (CWIS)?...' -- content-behind-filename mismatch.",
    "R00BD4C269672": "Target: Rivera 2011, 'The business of water: going the corporate way -- the case of Manila water'. Delivered: Mashingaidze 2013, 'Beyond the Kariba Dam Induced Displacements: The Zimbabwean Tonga's Struggles for Restitution' -- unrelated paper.",
    "R00F911D1EF6E": "Target: Schiff 2010, 'Integrated Water Resources Management: A theoretical exploration...'. Delivered: Garrett et al. 2025, 'REACHing for PFAS solutions: how two communities responded to drinking water contamination' -- content-behind-filename mismatch.",
    "R00FB49388689": "Target: 'The Classification of Drinking Water between Public Administration and Rural Communities in South Kordofan, Sudan' (2012). Delivered: Doyle et al., 'Challenges and Opportunities for Tribal Waters...Crow Reservation, Montana' -- content-behind-filename mismatch.",
    "R0131B1D0A1D8": "Target: Bell & Franceys 1995, 'Improving Human Welfare through Appropriate Technology...'. Delivered: Fonta, Gordon & Toumpakari, cross-comparative analysis of child poverty in Anglophone/Francophone sub-Saharan Africa -- unrelated paper.",
    "R0181A040A1F4": "Target: da Silva et al. 2015, environmental conflicts and the waters of the Sao Francisco river, Brazil. Delivered: Lobao et al. 2025, 'Water security evaluation in small-sized cities in Paraiba, Brazil' -- different specific paper.",
    "R01EC667EA2B2": "Target: Kumar 2015, 'Rural Households' Access to Basic Amenities in India'. Delivered: Turren-Cruz, Garcia-Rodriguez & Lopez Zavala, 'Evaluation of Sanitation Strategies and Initiatives Implemented in Mexico...' -- content-behind-filename mismatch.",
    "R023B3A0D827A": "Target: Pablos, Vaquez, Adams & Ley 2014, 'Water rights and watershed management in Mexico. The Sonora river case'. Delivered: Samano Romero & Chavez-Mejia 2025, 'Water Access in Mexico City: A Review of Local Research Approaches' -- this is a genuine paper, but it is the target citation for a DIFFERENT record_id (RC8E1C6959D2C, corrected to include above), delivered here under the wrong record_id. The Sonora river watershed-management paper targeted by this record_id remains unretrieved.",
    "R024A1DA6ECCE": "Target: Jiao 2024, 'Residents' Willingness to Participate in Domestic Sewage Treatment in Rural China...'. Delivered: Hove et al. 2021, 'Developing stakeholder participation to address lack of safe water...rural province in South Africa' -- unrelated paper.",
    "R0358B81545C7": "Target: Saavedra-Costas 2009, 'A Study of the Impact of Decentralization on Access to Service Delivery'. Delivered: Habermehl & McFarlane, 'In Desperate Need: Public Sanitation in Contemporary London' -- unrelated paper.",
    "R03D388B03A8D": "Target: Achuo & Asongu 2025, WASH public-spending governance-thresholds paper. Delivered: Ogunbode 2026, 'The State of SDG 6 in Nigeria (2016-2024)...' -- different author/paper.",
    "R03D7439F873C": "Target: 'Water and Health in the Nandamojo Watershed of Costa Rica'. Delivered: Patel et al. 2020, 'Drinking Water in the United States: Implications of Water Safety, Access, and Consumption' -- US review, not Costa Rica.",
    "R050B1AB16546": "Target: 'Approaches in Drinking Water Provision in Developing Countries'. Delivered: Majuru, Suhrcke & Hunter 2016, 'How Do Households Respond to Unreliable Water Supplies? A Systematic Review' -- different specific paper.",
    "R05315EFB334C": "Target: 'Mutual aid as community development: Accessing potable water...'. Delivered: Sisay, Gari & Ambelu 2024, 'Fecal Sludge Management and Sanitation Safety...Addis Ababa, Ethiopia' -- unrelated topic/country.",
    "R056D4E19E04C": "Target: 'Norwich officials consider sewer fee change' (news article). Delivered: Van Lier 2025, 'From Degradation to Reproduction: Environmental Justice...Detroit' -- unrelated academic article.",
    "R058C9273C2A0": "Target: 'Socio-technical Transitions in the Water Sector'. Delivered: Kasper 2025, 'From Dams to Tanks to Jerry Cans: Storage as a Multi-Scalar Analytic', Nairobi -- different paper/author.",
    "R05A5348ECB82": "Target: 'The Economic Impact of Public Private Partnerships...'. Delivered: Cohim Silva & Naval 2015, 'A Contribution to Develop Strategies to Support the Social Control of Sanitation Activities', Brazil -- content-behind-filename mismatch.",
    "R060118F9EC4B": "Target: 'THE REAL MOLDOVA: DIRTY WATER, GLOBAL ENVIRONMENTAL...' (news/report). Delivered: Sengupta & Benjamin 2016, 'Countdown 2015: an assessment of basic provision to migrant families...Ludhiana, North India' -- unrelated.",
    "R061246D9E7F9": "Target: 'Public Policies In the Water Sector: Water Safety Plans...'. Delivered: Lopes 2020, 'Affordability and Disconnections Challenges in Implementing the Human Right to Water in Portugal' -- different specific paper.",
    "R062509D0652A": "Target: 'Features of the drinkable water sector in Venezuela'. Delivered: Jabari, Shahrour & El Khattabi 2020, 'Assessment of the Urban Water Security in a Severe Water Stress Area...Palestinian Cities' -- Palestine, not Venezuela.",
    "R07553B7C3E18": "Target: 'WATER AND SANITATION PROGRAM IN DECENTRALISED EAST...'. Delivered: Tesfaye et al. 2026, 'Access to safe sanitation services and factors associated with PPE utilisation among sanitation workers in Ethiopia' -- different paper.",
    "R076AC687A7CA": "Target: 'Water restriction rules give businesses a break' (news article). Delivered: D'Odorico, Dell'Angelo & Rulli 2024, 'Appropriation Pathways of Water Grabbing' -- academic paper, not the news article.",
    "R077E94B13A48": "Target: 'Water Access Challenges and Coping Strategies in I...' (India). Delivered: Mottelson & Venerandi 2020, 'A Fine-Grain Multi-Indicator Analysis of the Urban Form of Five Informal Settlements in East Africa' -- unrelated.",
    "R083F3250F8E0": "Target: 'The political economy of community management: a st...'. Delivered: Frempong, Stadelmann & Thiam, mining-activities/water-security/health/economic-opportunities paper -- different specific study.",
    "R090C6103AD6B": "Target: 'Reforms Toward Integrated Management of Water in E...' (Egypt). Delivered: Gomes et al. 2018, 'Capacity Building for Water Management in Peri-Urban Communities, Bangladesh: A Simulation-Gaming Approach' -- Bangladesh, not Egypt.",
    "R09137E1E91C7": "Target: 'Housing and Water Insecurity in Nairobi's Informal...'. Delivered: Dipura, Monstadt, Frank & Smith 2026, 'Governing infrastructure heterogeneity: an intraurban analysis of sewerage infrastructures in Cape Town' -- Cape Town, not Nairobi.",
    "R09556CBA9907": "Target: 'The Rule of Law and the Right to Water: Social and...'. Delivered: book chapters from 'Environmental Justice in Nepal' (Sherpa ch.19; Awale ch.20) -- unrelated Nepal climate-justice book.",
    "R096943083833": "Target: 'Evaluation des captages futurs en eau souterraine...' (French, groundwater). Delivered: Lillo et al., renewable-energy/sanitation integral-management model, Pucara, Peru -- unrelated paper.",
    "R09F94E3DD04D": "Target: 'The impact of population density and racial compos...'. Delivered: Ribeiro et al. 2026, 'Does cooperation pay off over time? Evidence from water and wastewater services', Brazil -- different paper/topic.",
    "R0A2594540DD4": "Target: 'Colonias in the Lower Rio Grande Valley of South T...'. Delivered: Howard, Bartram et al. 2020, 'COVID-19: urgent actions, critical reflections and future relevance of WaSH' -- unrelated global review.",
    "R0A4D9728FDBA": "Target: 'Accessing Water: Channeling Power -- Class, Gender, an...'. Delivered: Nagheeby, Mdee et al. 2026, 'Escaping the Capitalist Black Hole: dethroning Mammon and liberating water' -- different paper/authors.",
    "R0AA26166D6FD": "Target: 'Institutions, urban governance, and leadership: A s...'. Delivered: Kharmylliem & Kipgen 2021, 'Assessing the Sustainability of Urban Water Supply Systems in Shillong, India' -- different specific title/authors.",
    "R0B2F89A503C5": "Target: 'National Initiative for Human Development and Soli...' (Morocco). Delivered: Yanquiling, Dressler & Smith 2026, 'Water, pipes and the cholera pathogen: The colonial politics of germs and water infrastructures in the Philippines' -- unrelated.",
    "R0B45001AA9BF": "Target: 'Critical Success Factors for the Community Managem...'. Delivered: Singh, Ibrahim & Pandey, climate-change/WASH-perception survey, Nepal -- different specific study.",
    "R0B53702535FD": "Target: 'Managing Water for All'. Delivered: Willetts et al. 2022, 'Co-developing evidence-informed adaptation actions for resilient citywide sanitation...Indonesia' -- different paper.",
    "R0B60D81754F1": "Target: 'Assessing the potential for community-based waste...'. Delivered: Amissah Asokwah et al. 2026, 'The water and sanitation sector of Ghana -- what is missing from a governance perspective?' -- different paper/focus.",
    "R0B8D73D4EBE3": "Target: 'The Ministry of Dry Taps: The Department of Water A...'. Delivered: Mazingisa, Wiysonge & Kgware, WASH-in-schools evaluation, eThekwini, South Africa -- different paper.",
    "R0C08277D7877": "Target: 'Johannesburg's model white housing scheme in the c...'. Delivered: Williams et al., groundwater availability/access/contamination-risk study, Arizona -- unrelated.",
    "R0C0F7458F5B6": "Target: 'Public-Private-Community Partnerships in Managemen...'. Delivered: Abdulhadi, Bailey & Van Noorloos 2024, 'Access inequalities to WASH and housing in slums in LMICs: A scoping review' -- different paper.",
    "R0DBA3B0816C9": "Target: 'Informal rules! Using institutional economics to u...'. Delivered: Ozen Inam, study on physical/psychosocial problems of women after the 2023 Kahramanmaras earthquake, Turkey -- completely unrelated.",
    "R0DBD35259609": "Target: 'The dynamics of a piped-water and sewer developmen...'. Delivered: Schramm & Ibrahim, 'Hacking the pipes: Hydro-political currents in a Nairobi housing estate' -- different specific paper.",
    "R0DD7699D458F": "Target: 'Water Poverty'. Delivered: Beker & Kansal, 'Complexities of the urban drinking water systems in Ethiopia and possible interventions for sustainability' -- different paper.",
    "R0E116D99D106": "Target: 'Public things, excremental politics, and the infra...'. Delivered: Wright-Contreras 2018, 'A Transnational Urban Political Ecology of Water Infrastructures...Hanoi' -- different paper.",
    "R0E6CFD632882": "Target: 'Assessment of the current and future water balance...'. Delivered: Hellberg 2023, 'What constitutes the social in (social) sustainability? Community, society and equity in South African water governance' -- different paper.",
    "R0E97835651DC": "Target: 'Assessing Sanitary Mixtures in East African Cities'. Delivered: Foellmer et al. 2026, 'Lived sanitation experiences in informal and formal settlements in Nairobi, Kenya' -- different specific paper (single-city, not multi-city).",
    "R0E9F299E7E3D": "Target: 'Cooperation in common property resource management...'. Delivered: Habermehl & McFarlane 2025, 'In Desperate Need: Public Sanitation in Contemporary London' -- unrelated (also delivered wrong for R0358B81545C7).",
    "R0EADB40410CF": "Target: 'Sustainable Provision of Water Services in the Uni...' (US). Delivered: Ward et al. 2026, 'Values at the tap: how organizational culture shapes water unaffordability and environmental justice in U.S. cities' -- different specific paper despite topical/geographic overlap.",
    "R0F96663F118E": "Target: Jha 2005, 'Institutions, performance, and the financing of infrastructure services in the Caribbean'. Delivered: Sakaya et al. 2025, 'Political economy barriers on the integration of water, sanitation, and solid waste management services in Ugandan towns' -- Uganda, not the Caribbean; different author/year.",
    "R108940A0C546": "Target: 'Challenges in water and sanitation services: Do nat...'. Delivered: Zvobgo & Do 2020, 'COVID-19 and the call for Safe Hands...Chitungwiza, Zimbabwe' -- different specific paper.",
    "R1099FEF98B3B": "Target: 'From cash flows to water flows: an assessment of fi...'. Delivered: Singh, Laker et al. 2022, 'Evaluation of Business Models for Fecal Sludge Emptying and Transport in Informal Settlements of Kampala, Uganda' -- different paper.",
    "R11F8F3CCA5C9": "Target: 'New Rules Could Triple Sewage Disposal Costs for S...' (news article). Delivered: Hughes et al. 2024/25, 'Understanding the Cost of Basic Drinking Water Services in the United States: A National Assessment' -- academic paper, not the news article.",
    "R191679B5A6DC": "Target: 'Partnerships between water sector institutions and...'. Delivered: Sylvester & Mdee 2023, 'Defining and acting on water poverty in England and Wales' -- different paper.",
    "R31F7BB4FD2AD": "Target: 'Life-cycle costs approach for private piped water...'. Delivered: Burt, Sklar & Murray 2019, 'Costs and Willingness to Pay for Pit Latrine Emptying Services in Kigali, Rwanda' -- different paper.",
    "R567DAF227DB7": "Target: 'Strategy formulation for accelerating safe sanitat...'. Delivered: Amorim et al., 'The effect of the regulation and regulatory enforcement on the implementation of the social tariff in the water sector...Brazil' -- different paper.",
    "R5F07B2DC4BA6": "Target: 'Water cooperatives in La Paz and El Alto, Bolivia'. Delivered: Wamuchiru 2017, 'Beyond the networked city: situated practices of citizenship and grassroots agency in water infrastructure provision...Dar es Salaam' -- Tanzania, not Bolivia.",
    "R643AC2D2A6A8": "Target: 'The viability of decentralized water and sanitatio...'. Delivered: Cooper, Behnke, Cronk et al. 2021, 'Environmental health conditions in the transitional stage of forcible displacement: A systematic scoping review' -- unrelated refugee-displacement review.",
    "R69151C02A363": "Target: 'Water Context in Latin America and the Caribbean D...'. Delivered: Vargas Falla et al. 2025, 'Decentralisation and Legal Pluralism in Small Towns in Uganda' -- Uganda, not Latin America/Caribbean.",
    "R6A68A9A48B08": "Target: 'Jozini Dam Infrastructure and Its Role on Local Ec...'. Delivered: Frempong, Stadelmann & Thiam, mining-activities/water-security paper -- same wrong content also delivered for R083F3250F8E0, not the Jozini Dam study.",
    "R6ED6084F5486": "Target: 'Corruption and SDG 6 -- Clean Water and Sanitation fo...'. Delivered: Choque-Quispe et al., 'Drinking Water Service Diagnosis in a High-Elevation Andean City of Peru' -- water-quality/engineering study, not a corruption/governance paper.",
    "R7EB1309DA47D": "Target: 'WATER PRICING AND ITS DETERMINANTS IN NAMIBIA'. Delivered: Alzahrani & Tawfik, 'Regional Heterogeneity in Urban Water Consumption in Saudi Arabia' -- Saudi Arabia, not Namibia.",
    "R80C0C7C65752": "Target: 'Policy implementation considerations for basic ser...'. Delivered: Rasweswe, Mothiba & Bopape, 'Menstrual hygiene practices in African correctional services: a narrative synthesis of barriers' -- completely unrelated topic.",
    "R909EC228A5A0": "Target: 'Performance Assessment for Increasing Connection R...'. Delivered: Marcillo, Krometis & Krometis 2021, 'Approximating Community Water System Service Areas to Explore the Demographics of SDWA Compliance in Virginia' -- different paper.",
    "R91BF40E95289": "Target: 'Guarding the sons of empire: Military-state-society...'. Delivered: Muller, 'Adapting to climate change: water management for urban resilience', sub-Saharan Africa -- unrelated to the military/empire history paper.",
    "R93C610A0FADB": "Target: 'Sanitation in Mexico: An Overview of Its Realizatio...'. Delivered: Alam et al. 2025, 'Behaviour change interventions to promote household connectivity to sewer: a scoping review', Bangladesh-based team -- different paper, not Mexico-specific.",
    "RBE126A48DC78": "Target: 'A local public service: The action of small-scale p...'. Delivered: Andrews, Beynon & Baafi 2025, 'Access to Basic Infrastructure Services in Ghanaian Local Government: A Contextual Approach' -- different specific paper/authors.",
    "RF98D06B8E550": "Target: 'An assessment tool to improve rural groundwater ac...'. Delivered: Aigbavboa, Addo, Ebekozien, Thwala & Arthur-Aidoo, 'Appraising institutional management of urban water supply in Ghana...' -- urban Ghana study, not the rural-groundwater assessment-tool paper.",
}


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def process_db():
    with open(PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    decided = []

    for row in rows:
        rid = row["record_id"]
        if rid in INCLUDES:
            detail = INCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "include"
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "include"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in EXCLUDES:
            code, detail = EXCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "exclude"
            row["exclusion_reason"] = code
            row["exclusion_reason_detail"] = detail
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "exclude"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in WRONG_FILE:
            detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["reviewer_1"] = REVIEWER
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail

    atomic_write(PATH, fieldnames, rows)
    return decided, fieldnames


def append_exclusion_log(decided):
    with open(EXCLOG_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in decided:
        if row["final_decision"] != "exclude":
            continue
        rows.append({
            "record_id": row["record_id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": row["exclusion_reason"],
            "exclusion_reason_detail": row["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(EXCLOG_PATH, fieldnames, rows)


if __name__ == "__main__":
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 69, len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE)
    decided, _ = process_db()
    assert len(decided) == 1
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 237 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
    print("Note: R0908697F9FE5 left untouched (empty/unreadable extraction, undecided).")
