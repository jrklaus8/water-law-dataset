#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R46096F5F6F6C": "Narzetti & Marques 2021 (Water, MDPI), 'Access to Water and Sanitation Services in Brazilian Vulnerable Areas: The Role of Regulation and Recent Institutional Reform.' Documents that slums and other informal settlements are typically excluded from urban-area WSS statistics ('nobody's land') and analyzes how Brazil's recent institutional/regulatory reform (Lei 14.026/2020) affects economic access to water/sanitation for vulnerable populations, finding public authorities have resigned their proactive role and regulation must be strengthened for universalization. A rigorous institutional/regulatory-mechanism case study directly documenting how the regulatory/institutional framework shapes water-access outcomes for Brazil's poor and informal-settlement population.",
    "R2428752DF562": "Safari, Mohamed, Dimoso, Akyoo, Odhiambo, Mpete, Massa & Mwakitalima 2019 (Journal of Water, Sanitation and Hygiene for Development), 'Lessons learned from the national sanitation campaign in Njombe district council, Tanzania.' Qualitative case study documenting how village-level WASH by-laws enacted by local government, enforced via 'SMART enforcement' (a graduated mix of warnings, fines, and prosecutions, with fine proceeds used to fund latrine construction for the fined household), drove household improved-latrine coverage from 7.5% (2011, pre-intervention) to 99.8% (September 2018). A rigorous institutional/legal-enforcement-mechanism case study directly documenting how local sanitation law and its enforcement produce large differential increases in sanitation access.",
    "R01025F73B0E2": "Danert, Carter, Rwamwanja, Ssebalu, Carr & Kane 2003 (Journal of International Development), 'The Private Sector in Rural Water and Sanitation Services in Uganda: Understanding the Context and Developing Support Strategies.' Institutional/policy analysis based on extensive interviews with all major stakeholders across 8 of Uganda's 56 districts, examining private-sector water/sanitation delivery under Uganda's decentralization and privatization policies, covering corruption, community participation, role of NGOs, local-government procurement procedures, and business viability. A rigorous multi-district institutional case study directly documenting how decentralization/privatization policy and local-government procurement procedures shape private-sector rural water/sanitation service delivery.",
    "R800E2F068095": "Mottelson 2020 (Land, MDPI), 'A New Hypothesis on Informal Land Supply, Livelihood, and Urban Form in Sub-Saharan African Cities.' Comparative empirical study of informal urban land use across four major East African cities, finding that government repression of informal urban development decreases informal land supply, increases informal-land-market competition and accommodation costs, and produces lower household access to water and sanitation. A rigorous institutional/legal-mechanism comparative case study directly documenting how state repression of informal settlement formation (a legal/administrative land-use enforcement mechanism) produces differential water/sanitation access outcomes for the urban poor.",
    "R235E42D59F53": "Amaechina, Amoah, Amuakwa-Mensah, Amuakwa-Mensah, Bbaale, Bonilla, Bruhl, Cook, Chukwuone, Fuente, Madrigal-Ballestero, Marin, Nam, Otieno, Ponce, Saldarriaga, Vasquez Lavin, Viguera & Visser 2020 (Water Economics and Policy), 'Policy Note: Policy Responses to Ensure Access to Water and Sanitation Services during COVID-19: Snapshots from the Environment for Development (EfD) Network.' Documents specific, dated, quantified legal/institutional water-access mechanisms across 14 Global South countries during the COVID-19 pandemic: disconnection moratoriums (Costa Rica Decree 076-S, Uganda NWSC, South Africa), reconnection programs (Colombia: 250,000+ households, cost waived), income/property-value-based subsidy eligibility criteria (Chile decile-based subsidy, Cape Town indigent program at R300,000 property-value threshold, Colombia socioeconomic-strata system), and free-water policies (Ghana, funded by government reimbursement to the utility). A rigorous multi-country comparative documentation of specific institutional/legal water-access mechanisms and their differential effects on connected vs. unconnected/informal-settlement households.",
    "RA5E555B4E7F8": "Mawani 2019 (Water, MDPI), 'Unmapped Water Access: Locating the Role of Religion in Access to Municipal Water Supply in Ahmedabad.' Empirical institutional/legal-mechanism study examining how implementation of Ahmedabad's 'town planning scheme' (a formal urban-planning mechanism), premised on the legal status of constructions as 'illegal,' mediates water-access outcomes in the city's Muslim-majority areas, and how religious difference and contestation among influential state and non-state legal actors shape technical planning outcomes. A rigorous case study directly documenting how a specific planning-law mechanism, intersecting with legal-status (illegality) determinations, produces differential municipal water access along religious lines.",
    "R89B77B5F6948": "Silvestri, Wittmayer, Schipper, Kulabako, Oduro-Kwarteng, Nyenje, Komakech & van Raak 2018 (Sustainability, MDPI), 'Transition Management for Improving the Sustainability of WASH Services in Informal Settlements in Sub-Saharan Africa.' Mixed empirical study combining a literature review with original fieldwork (57 interview summaries and two inter-/transdisciplinary workshops, 2015-2018) in Arusha (Tanzania), Dodowa (Ghana) and Kampala (Uganda), identifying landownership, governance capacity, and socio-economic inequalities as key institutional dimensions governing WASH access; documents specific institutional exclusion (e.g., Kampala Capital City Authority excluding an informal settlement from a community water well) and landownership-based differential water pricing in Dodowa. A rigorous multi-city institutional case study grounded in original interview/workshop data, directly documenting land-tenure and governance-capacity mechanisms shaping differential WASH access in informal settlements.",
    "R001780FF5AE4": "Yeboah 2006 (Geographical Journal), 'Subaltern Strategies and Development Practice: Urban Water Privatization in Ghana.' Rigorous institutional/political-economy case study of Ghana's 1990s-2000s urban water privatization process (Halcrow and Berger consultant reports, GWSC/GWCL restructuring, Water Sector Restructuring Secretariat), documenting a specific institutional service-area-classification mechanism: reclassification of towns up to 15,000 population from 'urban' (GWSC/commercial) to 'rural' (Community Water and Sanitation Division) service, justified explicitly on an 'ability to pay' criterion, requiring communities to cover at least 5% of system cost. A rigorous institutional-mechanism case study directly documenting how service-area/eligibility classification, justified by income-based criteria, produces differential water-access and cost-sharing burdens by geography and class.",
}

EXCLUDES = {
    "R000FED66EADD": ("E05", "Akiwumi 2015 (Politics, Groups, and Identities, 'Dialogue: Environmental Justice' section), 'Analyzing Sierra Leone's water reform efforts: law, environment, and sociocultural justice issues.' A doctrinal legal-text analysis comparing Sierra Leone's draft National Water Resources Management Bill 2013, Mines and Minerals Act 2009, and 1991 Constitution against African regional legal instruments (African Charter, ACRWC, Maputo Protocol, Resolution 244), explicitly framed as an essay with no original data collection (no interviews, surveys, or fieldwork). A doctrinal/comparative-legal-text analysis with no independent empirical research methodology; matches the established doctrinal-analysis-no-empirical-evidence exclusion precedent (Mpanga 2016, Batch 221)."),
    "R006EEFF9CD0E": ("E01", "Taylor & Trentmann 2011 (Past & Present), 'Liquid Politics: Water and the Politics of Everyday Life in the Modern City.' A social/legal history of consumer activism and legal disputes over water rate assessments, 'extra' charges (baths, water closets) and disconnections among propertied ratepayers in Victorian London and Sheffield (1870s-1900s). Documents legal/tariff mechanisms but concerns propertied middle- and working-class ratepayer politics over billing/tariff fairness in historical Britain, not administrative-law exclusion of a marginalized or informal-status population from water access as the review's inclusion criteria require; extends the established wrong-topic/wrong-population exclusion precedent for content outside the review's institutional-exclusion-of-vulnerable-populations scope."),
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
    assert len(INCLUDES) + len(EXCLUDES) == 10
    decided, _ = process_db()
    assert len(decided) == 10
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 225 processed: {n_inc} includes, {n_exc} excludes.")
