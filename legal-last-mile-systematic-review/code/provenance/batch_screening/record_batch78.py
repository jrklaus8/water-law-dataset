import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "REA26B447CC9E": {
        "exclusion_reason": "E04",
        "exclusion_reason_detail": "Explanatory quantitative study (PLS structural equation modeling survey of PDAM managing directors across 60 regional water companies in Sulawesi, Indonesia) of the moderating effect of efficiency and non-market capability in the relationship between government involvement/resources and company performance. The outcome variable ('Performance', a company-level PLS construct) is a corporate/organizational performance measure, not a household- or applicant-level water-access, connection, affordability, or reliability outcome -- the same technical/organizational-efficiency exclusion rationale applied to the prior DEA study (R8821B3A63A95).",
    },
}

includes = {
    "R9BAE8BE9ADB8": "Extracted as S550. Mixed-methods case study (document analysis plus 104 household interviews in Dodowa, Ghana, and 56 household interviews plus 120 water-point interviews in Arusha, Tanzania) of power dynamics and participatory governance affecting groundwater access. Documents genuine legal-administrative content: Ghana's Community Water and Sanitation Agency Act and GWCL urban water-supply mandate, alongside a GWCL tank-connection application/inspection process and a 10x price markup for tank-resold water versus the regulated GWCL tariff; Tanzania's Water Resource Management Act and Pangani Basin Water Board regulatory function, alongside Arusha City Council issuance of land permits in groundwater recharge areas found to be illegal under that Act, and pervasive unregistered/unmonitored borehole drilling; and household-level exclusion from community water governance structures (WATSAN committees, Balozi) correlated with tenure status (renters), kinship ties, and land ownership. MMAT (mixed methods).",
}

reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in excludes:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        d = excludes[rid]
        r["full_text_decision"] = "exclude"
        r["final_decision"] = "exclude"
        r["reviewer_1"] = reviewer
        r["exclusion_reason"] = d["exclusion_reason"]
        r["exclusion_reason_detail"] = d["exclusion_reason_detail"]
        changed += 1
    elif rid in includes:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = includes[rid]
        changed += 1

assert changed == len(excludes) + len(includes), f"expected {len(excludes)+len(includes)}, got {changed}"

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
for rid, d in excludes.items():
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
