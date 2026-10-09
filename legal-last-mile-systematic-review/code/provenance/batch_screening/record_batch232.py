#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R34A37671F4E3": "Jones, Greenberg, Kaufman & Drew 1978 (Journal of Politics), 'Service Delivery Rules and the Distribution of Local Government Services: Three Detroit Bureaucracies.' Rigorous OLS-regression study of three Detroit municipal bureaucracies (Environmental Enforcement, Sanitation Division, Parks & Recreation), directly testing how formal/informal administrative 'service delivery rules' (e.g., the Sanitation Division's 'weight rule' allocating garbage-collection resources by neighborhood-generated tonnage, later supplemented by an explicit center-city equity rule) produce differential distribution of sanitation and other municipal services across census tracts by neighborhood social well-being (housing age, distance from CBD) and racial composition. A genuine regression-based institutional/administrative-mechanism study directly isolating administrative rules' effect on differential sanitation-service resource allocation.",
    "R3DB2F9D0CE7E": "Tukahirwa 2011 (Wageningen University doctoral thesis; Chapter 3 published as Tukahirwa, Mol & Oosterveer 2011, Habitat International 35:582-591), 'Access of urban poor to NGO/CBO-supplied sanitation and solid waste services in Uganda: The role of social proximity.' Rigorous logit-regression study (192/189 observations, Kampala slum households) of the determinants of urban poor households' access to NGO- and CBO-provided sanitation services, finding social-proximity trust to be the strongest and most significant predictor of access (marginal effect far exceeding spatial-proximity, perception, and socio-economic factors). A genuine regression-based institutional/administrative-assistance-mechanism study directly isolating a social-network/trust-based access mechanism's effect on differential sanitation-service access among the urban poor.",
}

EXCLUDES = {
    "R372282DE211B": ("E12", "Krueger, Rao & Borchardt 2019 (Global Environmental Change), 'Quantifying urban water supply security under global change.' A methodological index/framework-development paper (Capital Portfolio Approach) that quantifies urban water supply security via a composite scoring of five 'capitals' (water resources, infrastructure, financial, management/political, community adaptation), applied descriptively to seven case-study cities without isolating a specific legal/institutional access-eligibility mechanism's effect. Extends the established methodological/index-development exclusion precedent (Sullivan & Meigh 2003, Batch 226; Willetts et al. 2013, Batch 227; Kayser et al. 2019, Batch 230)."),
}

WRONG_FILE = {}


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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 3
    decided, _ = process_db()
    assert len(decided) == 3
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 232 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
