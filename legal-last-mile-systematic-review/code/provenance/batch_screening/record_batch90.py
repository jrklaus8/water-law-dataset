import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

EXCLUDES = {
    "RFE07661F24F1": ("E01", "Qualitative study of state-civil society partnership dynamics (24 interviews, 16 CSO-District Assembly collaborations) for W&S service delivery in Ghana; the studied outcome is partnership drivers/nature/successes/challenges at the institutional CSO-local government level, not a household-level legal-administrative water/sanitation access, connection, or affordability outcome -- matches the established governance-process/partnership-dynamics precedent."),
    "R46ADCD34A830": ("E01", "Qualitative ethnographic study of power/control dynamics in cross-sector partnerships between Malawian District Councils and development partners (NGOs/donors) in rural water supply; the studied outcome is the level of local-government involvement in service delivery (coordinate/partake/lead), an institutional governance-process outcome, not a household-level water access mechanism -- matches the established governance-process/partnership-dynamics precedent."),
}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}

    for rid in EXCLUDES:
        assert rid in by_id, f"record_id {rid} not found in DB"
        row = by_id[rid]
        assert row["full_text_decision"] == "", f"{rid} already has a decision: {row['full_text_decision']!r}"

    log_rows = []
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

    print(f"done, db changed {len(EXCLUDES)}, log rows now {len(existing_log)}")

if __name__ == "__main__":
    main()
