import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "R546EB2436B96": "Historical legal-institutional case study (primary archival sources: city council minutes, water company records, newspaper accounts, 1860-1890) of whether working-class suburbs of Norrkoping and Linkoping, Sweden received piped water connections from the municipal water system. Documents genuine household/property-level legal-institutional content: the distinction between a city's formally 'planned area' (where national building, fire, and public-health codes applied) and adjoining rural-district suburbs where they did not; City Council and Waterworks Board discretionary decisions on extending water pipes (Norrkoping 1886 debate; Linkoping 1881 Ladugardsbacke request denied until 1921); the '10 percent rule' financing criterion for extensions; and fee-based connection arrangements. Extracted as S583.",
}

EXCLUDES = {
    "R6E292C80B16D": ("E06", "GIS/water-point-mapping (WPM) technical analysis of 5,921 rural water points across 15 Tanzanian districts, evaluating coverage-estimation methodology, technology-type functionality decay over time, and Rural Water Supply and Sanitation Program (RWSSP) design assumptions; no legal-administrative access mechanism (eligibility, connection procedure, tenure, fees, disconnection, discretion) examined -- matches the established infrastructure/technical-methodology precedent (e.g., Delhi hydrological IDW-interpolation study)."),
}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}
    all_ids = set(INCLUDES) | set(EXCLUDES)
    for rid in all_ids:
        assert rid in by_id, f"record_id {rid} not found in DB"
        row = by_id[rid]
        assert row["full_text_decision"] == "", f"{rid} already has a decision: {row['full_text_decision']!r}"

    log_rows = []

    for rid, notes in INCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["notes"] = notes

    for rid, (code, detail) in EXCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["exclusion_reason"] = code
        row["exclusion_reason_detail"] = detail
        log_rows.append({
            "record_id": rid,
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": code,
            "exclusion_reason_detail": detail,
            "reviewer": REVIEWER,
            "date": DATE,
        })

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    with open(LOG, newline="", encoding="utf-8") as f:
        log_reader = csv.DictReader(f)
        log_fieldnames = log_reader.fieldnames
        existing_log = list(log_reader)

    existing_log.extend(log_rows)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(LOG), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=log_fieldnames)
        writer.writeheader()
        writer.writerows(existing_log)
    os.replace(tmp_path, LOG)

    print(f"done, db changed {len(all_ids)}, log rows now {len(existing_log)}")

if __name__ == "__main__":
    main()
