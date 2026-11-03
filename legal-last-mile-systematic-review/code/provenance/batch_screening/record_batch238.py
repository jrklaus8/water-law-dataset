#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-28"
DATE = "2026-09-28"

INCLUDES = {
    "R430C429810BF": "Behnke, Cronk, Shackelford, Cooper, Tu, Heller & Bartram 2020 (Science of the Total Environment), 'Environmental health conditions in protracted displacement: A systematic scoping review.' Scoping review of 213 studies on WASH/environmental-health conditions among displaced populations; institutional/political factors identified as the most-cited barriers to service access. Genuine empirical evidence synthesis of water/sanitation access barriers. Qualitative synthesis only; no regression-based effect estimate.",
    "RF658E0A799E3": "de Lima, Silva, Neto, Fontana & Silva 2026, 'Expert group decision-making on ESG strategies for water public sanitation utilities under fiscal and budgetary constraints in Brazil.' Nominal Group Technique qualitative study (researchers/utility staff/service users, Maceio, Brazil) identifying ESG strategies for sanitation utilities facing fiscal/governance constraints. Genuine institutional/governance/fiscal-policy study of sanitation-service delivery. Qualitative only; no effect_sizes.csv entry.",
    "R12A082B16D4D": "Ananga 2015 (USF PhD dissertation), 'The Role of Community Participation in Water Production and Management: Lessons From Sustainable Aid in Africa International Sponsored Water Schemes in Kisumu, Kenya.' Mixed-methods study of four NGO-sponsored water/sanitation schemes in Kisumu informal settlements; logistic regression and chi-square tests on household survey data test whether community-participation variables predict beneficiary satisfaction with water-management committees and water-handling hygiene, plus qualitative FGDs on institutional/participatory factors. Genuine institutional/participatory-governance study of water-scheme management. The regression's outcome is participation-linked satisfaction/hygiene behavior, not a water-access outcome itself, so it does not qualify for effect_sizes.csv under this project's strict access-outcome requirement (same treatment as S1153, Das & Takahashi, Batch 236). Qualitative-synthesis-eligible only.",
    "R5EDAB88CC052": "Ikeda 2024 (Master's dissertation, Universidade do Estado de Santa Catarina, Portuguese), '(Des) governanca da agua e desastre: um estudo de caso sobre o rompimento da barragem da Lagoa da Conceicao em Florianopolis.' Qualitative case study (document analysis + interviews) of institutional/regulatory failure around a 2021 sewage-dam-rupture disaster; documents that only 65.71% of the city has sanitation-service access and analyzes public-agency/civil-society interaction through institutional/adaptive water-governance theory. Genuine institutional/regulatory-mechanism study of sanitation access. Qualitative only; no effect_sizes.csv entry.",
    "R66871E6DA5D1": "Subramanyam 2020 (Water Policy), 'A small improvement: Small cities lag in expanding household water coverage across urban India.' Quantitative multilevel linear regression (N=3,547 urban local governments, 21 states, 2001-2011) modeling city- and state-level governance factors associated with growth in household water-supply coverage. Local government administrative category is a statistically significant predictor: municipalities (b=-4.062, SE=1.254, p<0.01) and town panchayats (b=-4.034, SE=1.540, p<0.01) show significantly lower water-coverage growth than municipal corporations (reference category), controlling for population, density, growth rate, and initial coverage. Genuine institutional/administrative-mechanism study directly isolating an effect on a water-access outcome; added to effect_sizes.csv as Family C (administrative-capacity/access inequality across local-government categories).",
    "R8C288AFDD095": "Cronk, Guo, Fleming & Bartram 2021 (Science of the Total Environment), 'Factors associated with water quality, sanitation, and hygiene in rural schools in 14 low- and middle-income countries.' Multilevel mixed-effects logistic regression (N=2,677 schools, 13 countries) modeling institutional/programmatic factors associated with schools having at least basic, continuously-available on-premises water service. Externally-funded/supported WaSH programs are a statistically significant positive predictor (OR=1.4, p=0.021); absence of a parent-teacher association is a significant negative predictor (OR=0.6, p=0.001). Genuine institutional/administrative-assistance-mechanism study directly isolating an effect on a school-level water-access outcome; added to effect_sizes.csv as Family B (administrative assistance/access), using the externally-funded-WaSH-program effect estimate.",
    "R975C44396921": "Kurian & McCarney (eds.) 2010 (Springer), 'Peri-urban Water and Sanitation Services: Policy, Planning and Method.' Edited volume of comparative institutional/governance case studies (Africa, Asia, South America, Netherlands) on peri-urban water and sanitation service-delivery arrangements. Genuine institutional/governance-focused comparative case-study collection with empirical evidence. Qualitative only; no single effect_sizes.csv entry (edited multi-case volume, not a single regression).",
}

EXCLUDES = {}

WRONG_FILE = {
    "R202A61E0248F": "Target: Svahn 2011, women's role in water supply management, Ghana. Delivered: Crow & Odaba 2010, 'Access to water in a Nairobi slum: women's work and institutional learning' -- different author, country (Kenya vs. Ghana), year.",
    "R3B987F73842E": "Target: Santosa, Atmoko & Mudjanarko 2020, sanitation-risk-index modelling. Delivered: Sofiyah et al. 2025, 'Community Participation in Urban Sanitation Programs at Koja, Jakarta, Indonesia' -- different authors/year/methodology.",
    "RCF2C8A8C45DD": "Target: Carrera 2014, 'Sanitation and social power in the United States.' Delivered: an OJEN 'Landmark Case' teaching package on the Canadian Supreme Court's Reference re Secession of Quebec -- completely unrelated constitutional-law topic; content-behind-filename mismatch.",
    "RD033530EB729": "Target: De Barcellos 2014, sanitation-rights litigation case study, Brazil. Delivered: a 2026 comparative dissertation (Erasmus University Rotterdam) on administrative law and sanitation-infrastructure connection across the Netherlands, Ontario, and Brazil -- a different, much newer multi-country work despite an identical-looking filename.",
    "RD30EA40D7E40": "Target: Lopez 2011, 'Community culture and rural water management.' Delivered: an Ontario government volunteer-award nomination form -- completely unrelated.",
    "RE8E6A91987B2": "Target: Concha 2012, right to water for indigenous communities. Delivered: UNESCO 'Youth for Peace' leadership-programme terms and conditions -- completely unrelated.",
    "R524A6753EA93": "Target: Herath, Wijesinghe & Thathsara 2026, shanty dwellers in Sri Lanka. Delivered: Tantoh, McKay & Leonard 2026, 'Local power dynamics of rural water supply in Bambili, Northwest Cameroon' -- different authors/country.",
    "R2B81E70A4BB1": "Target: Anbarci, Escaleras & Register 2006, corruption and water/sanitation access. Delivered: Ngefor 2011 (French), community water-supply projects in Kumbo, Cameroon -- different author/year/language/country.",
    "R28696F973EF4": "Target: Grant 2016, water governance in Phnom Penh. Delivered: Robina Ramirez & Sanudo-Fontaneda, water management in impoverished Doornkop, Soweto settlements -- different author/country.",
    "R33F8E5CB09A4": "Target: Mercado 2012, newspaper opinion column. Delivered: Tremolet & Smith 2026, OECD Working Paper on economic regulation of water supply/sanitation services -- unrelated.",
    "R43DE424922CB": "Target: Mubangizi & Mubangizi 2010, service delivery for the poor, South Africa. Delivered: Rodrigues 2024, bibliometric analysis of public policies on human rights to water in informal settlements -- different author/year/methodology.",
    "R4851AD373CCF": "Target: Brettenny 2017, efficiency evaluation of South African water services. Delivered: Kachenje 2024/2025, institutional-coordination challenges in Dar es Salaam water supply, Tanzania -- different author/country.",
    "R4459E55C5E6C": "Target: Delia Montero 2020, water supply in Iztapalapa (Spanish). Delivered: Dominguez Serrano & Castillo Perez 2018, community water organizations in Veracruz -- different author/location/year.",
    "R4BEB10EF5D32": "Target: Maruve 2019, water infrastructure management, Harare, Zimbabwe. Delivered: Zvobgo & Do 2020, COVID-19/'Safe Hands' study, Chitungwiza, Zimbabwe -- same country but different city/authors/year/focus.",
    "R495876E390CD": "Target: Lee 1979, water conservation policy during drought. Delivered: Joshua, Tompkins, Schreckenberg et al., water-policy resilience of potable infrastructure to climate risk, rural Malawi -- different author/country/year.",
    "R40CD1DA5FB19": "Target: Duran Juarez & Torres Rodriguez 2006, adequate safe water in a medium-size city. Delivered: Kusi-Appiah & Mkandawire, political ecology of urban-poor household water security, Malawi -- different author/country.",
    "R8D23BFC1BBD4": "Target: Yoon & Song 1997, interest-structure study of water-resource-conflict regions. Delivered: a Rutgers University Environmental Law and Policy course syllabus -- completely unrelated teaching document.",
    "R45B89503C5F5": "Target: Kim 1995, public attitudes on environmental problems, Taegu City, Korea. Delivered: Padowski, Gorelick, Thompson, Rozelle & Fendorf 2015, global freshwater-supply-vulnerability index study -- different authors/year/scope.",
    "R41B5B87B13D6": "Target: Okeola & Sule 2020, hydro-economic diagnostic of urban water supply system. Delivered: Womble, Gorelick, Thompson & Hernandez-Suarez 2025, strategic environmental water-rights market for Colorado River reallocation -- different authors/year/geography.",
    "R463964EDEB15": "Target: Plous 2016, water economics/policy in developing countries. Delivered: a law-firm business-development newsletter article -- completely unrelated, not about water.",
    "R430CCDE976C8": "Target: Hansen 2021, politics of local service provision, US. Delivered: an Ontario Real Estate Association commercial lease agreement template -- completely unrelated legal form.",
    "R5390D778E0EC": "Target: Lukito 2000, water service delivery, Greater Bandung, Indonesia. Delivered: Suyeno 2024, water-governance actors in Riau Province, Indonesia -- different author/year/location within Indonesia.",
    "R58C1D17BBFB9": "Target: Spence & Walters 2012, risk perception and drinking water in a vulnerable population. Delivered: Cumming et al. 2019, water-service continuity determinants, Bangladesh/Pakistan/Ethiopia/Mozambique -- different authors/countries/topic.",
    "R553639A6DDDE": "Target: Kloster & De Alba 2007, water in Mexico City and political fragmentation. Delivered: Giner & Pavon, retrospective analysis of first-time wastewater infrastructure in Texas colonias, 1995-2017 -- different authors/location/topic.",
    "R516D860293B8": "Target: Catalan 2013, community-based innovation in water supply/sanitation. Delivered: an Ontario government AI data-centre electricity-policy media backgrounder -- completely unrelated.",
    "R59116AA8FE3A": "Target: Wilder, Austria, Romero & Ayala 2020, human right to water, Mexico. Delivered: Moroz & Madzivanyika 2026, bibliometric analysis of SDG 6 research landscape -- different authors/topic.",
    "R6B1C512A548D": "Target: Bik 2004, costs/affordability/regulatory compliance in small midwestern US community water systems. Delivered: Hughes, Kirchhoff, Lee & Switzer, national US drinking-water-cost assessment (2023-2025) -- topically adjacent but different, later, differently-scoped paper.",
    "R790D58E6A659": "Target: Garcia 2009, environmental-sanitation policy implementation challenges. Delivered: Martin Velasco, Calderon et al. 2023, OECD Water Governance Indicator Framework implementation, Buenos Aires Province, Argentina -- different authors/year/country.",
    "R257F6C3344C9": "Target: Mukarram et al. 2023, coastal citizens' perception of community rainwater harvesting. Delivered: Hoque, Hope et al. 2019, social-ecological analysis of drinking-water risks, coastal Bangladesh -- different authors/year/topic.",
    "R6A02BABD8F82": "Target: Vyasulu 2011, government financing of health, India. Delivered: an Equitable Life Insurance Company of Canada mortgage/customer-verification form -- completely unrelated.",
    "R8F74892813E3": "Target: Tshimanga et al. 2021, climate-water-migration-conflict information system, Congo Basin. Delivered: Dhaundiyal 2026, water-infrastructure design challenges, Indian Himalayan Region -- different author/year/country.",
    "R00C2AB20F1B8": "Target: Blakeney 2000, 'Walkerton: a risk management nightmare.' Delivered: Galway 2016, drinking-water advisories in First Nations communities, Ontario, Canada -- different author/year; both concern Canadian drinking-water safety but are different papers, content-behind-filename mismatch.",
    "R2A9AE8845B0B": "Target: Kouame 2023, 'Three Essays on Education Outcomes and Institutions.' Delivered: Arimah 2017, 'Infrastructure as a Catalyst for the Prosperity of African Cities' -- different author/year/topic.",
    "R9FF2AB833738": "Target: Boehm & Suarez 2011, anti-corruption in water-provision regulation, Colombia. Delivered: Wang & Li, governance/finance of rural community infrastructure, China -- different authors/country/topic.",
    "R9D6052350868": "Target: Schur 1994, cost of rural water supply, South Africa. Delivered: Zaunda, Holm, Itimu-Phiri, Malota & White 2018, disability-friendly WASH facilities in primary schools, Rumphi, Malawi -- different authors/year/country/topic.",
    "R9DF784217B95": "Target: Rao & Merchant 2006, people's participation and water management, Gujarat. Delivered: a Middlesex Law Association (Ontario) legal-community newsletter -- completely unrelated.",
    "RA3532680FF7E": "Target: Goyal 2004, 'Getting water from public private partnerships.' Delivered: an Ontario government limited-partnership-declaration filing-instructions form -- completely unrelated legal/administrative form.",
    "RAC011418EF02": "Target: Frimpong et al. 2021, review of Ghana's National Water Policy (2007). Delivered: Garn, Sclar, Freeman et al. 2017, global systematic review/meta-analysis of sanitation interventions on latrine coverage/use -- different authors/year/scope.",
    "RBFC70108EBEE": "Target: Stopnitzky 2013, household sanitation/social norms/public policy, India. Delivered: Hosseini & Yadav 2024, traditional legal framework regulating groundwater rights, Iran -- different authors/year/country/topic.",
    "RBC57AD90ACFB": "Target: Amaya Ventura 2009, institutional analysis of Mexico's water-sector reform. Delivered: a New York City Bar Association Latin America Summit conference agenda -- completely unrelated.",
    "R2FE56A7F0F98": "Target: Botton & Blanc 2014, small private water operators serving peripheral African neighborhoods. Delivered: Dektar, McConnell & Kasekende 2022, private water operators in rural Karamoja, Uganda -- thematically adjacent but a different paper/authors/year/specific region.",
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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 48, len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE)
    decided, _ = process_db()
    assert len(decided) == 7
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 238 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
    print("Note: R0908697F9FE5 (empty extraction) and RBEDB6556B711 (bibliographic match only, body unreadable) left untouched, undecided.")
