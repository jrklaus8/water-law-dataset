#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R102EBEF65059": "Shrestha 2013 (Journal of Public Administration Research and Theory), 'Self-Organizing Network Capital and the Success of Collaborative Public Programs.' Rigorous logistic-regression study (Hubert-White robust SEs, hierarchical clustering for network dependency) of Nepal's collaborative Rural Water Supply and Sanitation Program (RWSSP), directly testing how village communities' self-organized network capital (number of organizational partners, indirect bridging reach to other communities, subgroup cohesion among partners) determines their success in securing RWSSP infrastructure funding. Finds all three network-capital measures significantly and substantially increase funding-success probability (e.g., increasing partners from 1 to 16 raises predicted funding probability from 0.02 to 0.99), while remote communities are significantly less likely to be funded. A rigorous regression-based institutional/administrative-mechanism study directly isolating a network-capital/bureaucratic-assistance mechanism's effect on differential access to water/sanitation infrastructure funding.",
}

EXCLUDES = {
    "RDC5BD0E41BEE": ("E06", "Hajek & Petruzela 2016 (Scientia Agriculturae Bohemica), 'Sustainability of the public water supply and sewerage services operating system: A case study on the example of the Czech Republic.' An economic/tariff-regulation study analyzing price elasticity of demand and 'social acceptability' (affordability threshold) of water/sewerage tariffs using household billing data, 2005-2012. An economic/tariff-pricing analysis of existing-customer consumption behavior, not a legal/institutional water-access-eligibility mechanism; extends the established engineering/economic-optimization exclusion precedent (Ojha et al. 2018, Batch 226)."),
    "R00CA19ACF0B3": ("E12", "Kayser, Rao, Jose & Raj 2019 (Bulletin of the World Health Organization), 'Water, sanitation and hygiene: measuring gender equality and empowerment.' A perspectives/commentary article reviewing existing literature and proposing four priority areas for future WASH gender-equality indicator development, without presenting an original empirical case study of a specific institutional/legal mechanism. Extends the established methodological/index-development exclusion precedent (Sullivan & Meigh 2003, Batch 226; Willetts et al. 2013, Batch 227)."),
    "R03FCE2E0674E": ("E01", "Hannah, Giroux, Krell, Lopus, McCann, Zimmer, Caylor & Evans 2021 (World Development), 'Has the vision of a gender quota rule been realized for community-based water management committees in Kenya?' A mixed-methods study of Kenya's constitutional two-thirds gender quota applied to Water Resource Users' Association committees, examining women's representation and leadership participation (chair/treasurer roles, meeting facilitation) rather than documenting differential household water-access outcomes. A governance-representation/leadership-equity study without documented water-access outcomes for affected populations; extends the established governance/stakeholder-theory exclusion precedent (Stewart & Gray 2006, Batch 227)."),
    "R0CCBF382E07C": ("E01", "Agarwal 2011 (Environment and Urbanization), 'The state of urban health in India; comparing the poorest quartile to the rest of the urban population in selected states and cities.' A broad wealth-quartile health-disparities analysis (child mortality, immunization, maternal health, stunting, with water/sanitation access as 2 of 7 outcome indicators) using National Family Health Survey data, without analyzing a specific legal/institutional access-eligibility mechanism as its analytical focus. Extends the established broad-socioeconomic-determinants exclusion precedent (Li/Cohen/Li/Zhang 2019, Batch 226)."),
    "R1D80BF6FC64D": ("E06", "Berk, Cooley, LaCivita, Parker, Sredl & Brewer 1980 (Social Science Research), 'Reducing Consumption in Periods of Acute Scarcity: The Case of Water.' A time-series econometric study of water-conservation programs (moratoriums, drought appeals, price increases) and their effects on domestic/agricultural consumption in four California communities during the 1976-77 drought. An economic/demand-management conservation study of existing consumers' behavior, not a legal/institutional water-access-eligibility mechanism; extends the established engineering/economic-optimization exclusion precedent (Ojha et al. 2018, Batch 226)."),
    "R133156D538B6": ("E01", "Kane 2012 (Human Organization), 'Water Security in Buenos Aires and the Parana-Paraguay Waterway.' An ethnographic essay presenting three narratives of regional hydrological imbalance (river sedimentation and shipping, indigenous terracing history, and aquifer flooding following a privatized water company's well closures), framed around 'scalar mismatches' in water governance decision-making. A broad hydropolitics/disaster-narrative essay, not a focused analysis of a legal/institutional household water-access-eligibility mechanism; extends the established water-resource-vs-water-service exclusion precedent (Perez 2002, Batch 227)."),
    "R153375378313": ("E01", "Wutich 2011 (Journal of Anthropological Research), 'The Moral Economy of Water Reexamined: Reciprocity, Water Insecurity, and Urban Survival in Cochabamba, Bolivia.' An ethnographic/regression study of informal reciprocal water-sharing networks among households in a squatter settlement excluded from the municipal water system, examining social-insurance norms of give-and-take rather than the legal/administrative mechanism producing municipal exclusion itself. An informal social-coping/reciprocity-institution study, not a documented legal/institutional access-eligibility mechanism; extends the established wrong-topic exclusion precedent for informal coping-strategy content outside the review's institutional-access-mechanism scope."),
}

WRONG_FILE = {
    "R0A1ED1B5B51E": "Target record per new_batch_pool.json / Drive filename: 'AFRICA: Barriers to investment in water are lowering' (2011, no author listed). Delivered PDF content (verified via both extracted .title metadata and full-text content) is an entirely different document: Cotula, Vermeulen, Leonard & Keeley 2009, 'Land grab or development opportunity? Agricultural investment and international land deals in Africa' (IIED/FAO/IFAD) -- different authors, title, publisher, year, and topic (large-scale agricultural land acquisitions, not water-sector investment). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
}

# R12A082B16D4D (Ananga 2015, "The Role of Community Participation in Water Production and
# Management... Kisumu, Kenya") is NOT included here: title/author confirmed correct via
# metadata, but the Google Drive extraction delivered only the front matter, abstract, and
# Chapters 1-3 (through page 67 of the dissertation) -- Chapters 4-7 containing the actual
# empirical logistic-regression results (RQ1/RQ2/RQ3 findings) were not retrieved. Per the
# undecided-record rule, this record is left open/undecided and the Drive file is not moved.


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
        # R12A082B16D4D: intentionally untouched (undecided, partial extraction)

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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 9
    decided, _ = process_db()
    assert len(decided) == 8
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 230 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved, 1 left undecided (R12A082B16D4D).")
