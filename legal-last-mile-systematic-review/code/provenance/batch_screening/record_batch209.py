#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R35C9E7782B04": "Guardia, Rossello & Garriga 2014 (Urban History) historical case study of Barcelona's water supply system, 1867-1967. Documents an institutional/legal mechanism -- 18th-19th century municipal water concessions granted first by personal merit then, from 1791, solely by 'financial means' (fee per unit of flow); the de facto private monopoly of the Sociedad General de Aguas de Barcelona (SGAB) formed via 1881 merger with Societe Lyonnaise des Eaux and absorption of competitors by 1896; and landlord-controlled trickle-feed contracts (as opposed to metered contracts) that limited tenant consumption -- producing a clearly documented differential-access outcome: 'exclusion of large segments of society and complete urban districts' from the modern water network through the early 20th century, with peripheral working-class districts (e.g. Barrio Chino, La Barceloneta) reliant on public fountains/wash-houses into the 1960s while wealthier central districts received full metered/piped service. A genuine historical institutional-mechanism case study with a clearly documented differential water-access outcome.",
    "R082522E9FF13": "Rana & Piracha 2018 (Management of Environmental Quality) qualitative case study of the DSK Model, a community-based water governance partnership between the NGO Dushtha Shasthya Kendra (DSK), the Dhaka Water Supply and Sewerage Authority (DWASA), and community-based organizations (CBOs), applied to Karail slum, Dhaka, Bangladesh. Documents detailed institutional/legal eligibility mechanisms for formal water-meter access -- house ownership (informal but community-recognized), CBO membership, ability to pay a ~BDT 13,824 connection/meter/security fee, and access to social/political networks -- with a clearly quantified access outcome: only 28% (581 meters, ~31,374 people) of Karail's ~115,000 residents had formal DWASA-DSK water access by 2014, with tenants categorically excluded from applying for meters (only house-owners eligible) and informal/illegal connections mediated by ruling-party political patronage.",
    "R379A9E400957": "Greiner 2016 (Rural Sociology) cross-sectional logistic regression study (n=47,367 U.S. community water systems, 2012 EPA SDWIS-Fed + county census data) of the social/institutional drivers of water utility privatization in the United States. Finds county unemployment rate, racial minority population share, and a curvilinear median-household-income relationship (peaking near $70,846) all significantly predict the odds of a water system being privately owned/operated, and situates this institutional-ownership mechanism within a documented body of evidence (drawn from Food and Water Watch, Arnold 2009, and others) tying privatization to subsequent rate increases (up to 15%/year for 12 years post-privatization in the ten largest U.S. sales) and water-quality declines (e.g. Camden NJ, Atlanta GA), framing water utility privatization as a form of environmental/affordability inequality.",
}

EXCLUDES = {
    "R39832266BF9A": ("E01", "Nickum & Lee 2006 (Environmental Politics) comparative institutional-reform study of urban water management bureaucracy in Beijing and the Pearl River Delta, China -- transboundary water disputes, retail water pricing reform, and water services bureaux (WSB) coordination reforms. A supply-side institutional/bureaucratic-coordination and water-resource-quality-management study; does not report household-level differential water-access or connection outcomes tied to a specific eligibility or barrier mechanism. Wrong-topic institutional water-supply-management study."),
    "R392CC7A02A7C": ("E01", "Abers & Keck 2009 (Politics & Society) qualitative study of Brazilian river-basin committees (Alto Tiete, Litoral Norte, Itajai, Velhas) as participatory-governance arenas for water RESOURCE management (pollution control, flood control, permit allocation), examining state capacity-building rather than household water/sanitation SERVICE access. A water-resource/environmental-governance study, not a household water or sanitation service-access study. Wrong-topic water-resources-governance study."),
    "R0931F164C986": ("E01", "Novotny, Hasman & Lepic 2018 (Intl J of Hygiene and Environmental Health) systematic review of contextual factors and motivations (613 observations, 40 studies, 16 countries) affecting rural community sanitation outcomes in LMICs. The review's 12 identified determinant categories are overwhelmingly individual/household-level psychosocial, cultural, socioeconomic, and spatial-environmental factors (privacy/convenience, social pressure, health motivations, soil/terrain, etc.); 'institutional support' is only a minor subcategory (27 of 613 observations, 4.4%) within this much broader multi-factor review. The review's primary focus is not a legal/administrative/institutional/regulatory mechanism's effect on access. Wrong-topic broad-determinants review."),
    "R61DB3FC3D4FB": ("E12", "Nealer 2009 (TD: The Journal for Transdisciplinary Research in Southern Africa) conceptual SWOT-analysis essay on South African municipal governance and potable water supply management, discussing the National Water Act 1998 and municipal reorganization (800+ to 284 to 230 municipalities) in general normative/descriptive terms. No original empirical data collection or analysis; a conceptual policy-discussion essay using a strengths-weaknesses-opportunities-threats framework. Wrong study design -- conceptual/normative essay without empirical access evidence."),
    "R089ED6BEB7BE": ("E01", "Lowatanatrakul 1991 (Water Science and Technology) descriptive programme-progress report on Thailand's Provincial Waterworks Authority (PWA) coverage targets, financing, and tariff constraints during the International Drinking Water Supply and Sanitation Decade (1981-1990). An aggregate national infrastructure-coverage progress report without an isolated legal/institutional mechanism's differential effect on specific populations' access. Wrong-topic infrastructure-progress-report study."),
    "R088A6862CBAC": ("E07", "Traverso-Yepez 2009 (Critical Public Health) institutional-ethnographic study of Brazil's Family Health Program (FHP) primary health-care delivery in a low-income district of Natal, examining social inequities in HEALTH CARE service delivery. Water/sanitation access (e.g. 'lack of running water' as a favela characteristic) is mentioned only incidentally; the study's service focus is primary health care, not water or sanitation. Wrong service."),
    "R3974945F7707": ("E01", "Troeger, Pham & Van Arsdale 2015 (Human Organization) cross-sectional Rapid Assessment Process study of community perceptions and outcomes (health, education, economic) of 11 recently completed water-source development projects in Timor-Leste. Examines project-implementation and sustainability factors (needs assessments, water user groups, local OMR capacity) and perceived well-being outcomes, not a legal/institutional eligibility or barrier mechanism's differential effect on water access. Wrong-topic project-implementation/perception study."),
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
    print(f"Batch 209 processed: {n_inc} includes, {n_exc} excludes.")
