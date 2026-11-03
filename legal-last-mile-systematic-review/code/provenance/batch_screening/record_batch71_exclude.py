import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

decisions = {
    "R8821B3A63A95": {
        "decision": "exclude",
        "exclusion_reason": "E04",
        "exclusion_reason_detail": "Double-bootstrap DEA (data envelopment analysis) benchmarking study of South African water-utility technical/operational efficiency (144 WSAs, 2010-2014 panel). Population and exposures are utility-level (WSA status, water-board use, outsourcing, political competition, urban/rural location), but the outcome variable is a DEA efficiency/inefficiency score (input-output productivity: operating cost and length of mains vs. authorized consumption and water quality) -- not household/applicant access, connection, service availability, reliability, quantity, affordability, or exclusion as defined by this review's scope. No household- or applicant-level legal-administrative access mechanism is examined.",
    },
}

reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in decisions:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        d = decisions[rid]
        r["full_text_decision"] = d["decision"]
        r["final_decision"] = d["decision"]
        r["reviewer_1"] = reviewer
        if d["decision"] == "exclude":
            r["exclusion_reason"] = d["exclusion_reason"]
            r["exclusion_reason_detail"] = d["exclusion_reason_detail"]
        changed += 1

assert changed == len(decisions), f"expected {len(decisions)} changes, got {changed}"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

with open(log_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    log_fieldnames = reader.fieldnames
    log_rows = list(reader)

id_to_row = {r["record_id"]: r for r in rows}
for rid, d in decisions.items():
    r = id_to_row[rid]
    log_rows.append({
        "record_id": rid,
        "title": r["title"],
        "authors": r["authors"],
        "year": r["year"],
        "stage": "full_text",
        "exclusion_code": d["exclusion_reason"],
        "exclusion_reason_detail": d["exclusion_reason_detail"],
        "reviewer": reviewer,
        "date": "2026-09-21",
    })

fd, tmp = tempfile.mkstemp(dir="02_screening/exclusion_log")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=log_fieldnames)
    writer.writeheader()
    writer.writerows(log_rows)
os.replace(tmp, log_path)

print("done, db changed", changed, "log rows now", len(log_rows))
