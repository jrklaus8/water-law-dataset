#!/usr/bin/env python3
"""Batch 95: 1 exclude (oil/gas siting-regulation editorial)."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")
EXCL_LOG = os.path.join(BASE, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

EXCLUDES = {
    "R2F0303FF9A77": {
        "code": "E01",
        "detail": "A short (~3-page) American Journal of Public Health editorial commenting on two other studies' findings about oil and gas extraction siting near persistently marginalized/redlined communities in Los Angeles County, California, and reviewing the regulatory timeline (setback-distance rules, fracking moratoria/bans) for oil and gas development in California and New York; the paper's subject is oil/gas extraction environmental-justice regulation, not water/sanitation service access. 'Community water supply contamination' is mentioned once in passing as one health-hazard pathway addressed by a different cited study (Berberian et al.), not examined empirically here.",
        "note": "Wrong topic; oil/gas extraction siting-regulation editorial with no original empirical data and no water/sanitation service-access content of its own.",
    },
}

def main():
    with open(FT_DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {row["record_id"]: row for row in rows}

    for rid in EXCLUDES:
        assert rid in by_id, f"record_id {rid} not found in full-text DB"
        row = by_id[rid]
        assert not row["full_text_decision"], f"{rid} already has full_text_decision={row['full_text_decision']!r}"
        assert not row["final_decision"], f"{rid} already has final_decision={row['final_decision']!r}"

    exclusion_rows_to_append = []

    for rid, info in EXCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["full_text_status"] = "retrieved"
        row["exclusion_reason"] = info["code"]
        row["exclusion_reason_detail"] = info["detail"]
        row["reviewer_1"] = REVIEWER
        row["notes"] = info["note"]
        exclusion_rows_to_append.append({
            "record_id": rid,
            "title": row["title"],
            "authors": row.get("authors", ""),
            "year": row.get("year", ""),
            "exclusion_code": info["code"],
            "exclusion_reason_detail": info["detail"],
            "stage": "full_text",
            "reviewer": REVIEWER,
            "date": "2026-09-22",
        })

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(FT_DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, FT_DB)

    with open(EXCL_LOG, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        log_fieldnames = reader.fieldnames
        log_rows = list(reader)

    for entry in exclusion_rows_to_append:
        log_row = {k: entry.get(k, "") for k in log_fieldnames}
        log_rows.append(log_row)

    fd2, tmp_path2 = tempfile.mkstemp(dir=os.path.dirname(EXCL_LOG), suffix=".csv")
    with os.fdopen(fd2, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=log_fieldnames)
        writer.writeheader()
        for row in log_rows:
            writer.writerow(row)
    os.replace(tmp_path2, EXCL_LOG)

    print(f"done, db changed {len(EXCLUDES)}, log rows now {len(log_rows)}")


if __name__ == "__main__":
    main()
