#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
TODAY = "2026-09-22"

DECISIONS = {
    "RA53C02DDB780": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Larson, Alexander, Djalante & Kirono 2013 is a social network "
            "analysis of formal, informal and 'ideal' inter-agency governance "
            "networks among 6 government water-management agencies (PDAM, DKK, "
            "DPU, DINKES, PSDA, BLH) plus NGO/university collaborators in "
            "Makassar, Indonesia; the outcome measured is network centrality/"
            "degree of centralization among organizations, not any "
            "household-level water/sanitation access, connection, or outcome "
            "data -- same institutional-level governance-process rationale as "
            "the Hushie/Soublière-Cloutier/Kimbugwe exclusion precedent."
        ),
    },
}


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}
    for rid in DECISIONS:
        assert rid in by_id, f"{rid} not found"
        r = by_id[rid]
        assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

    excl_rows = []
    for rid, d in DECISIONS.items():
        r = by_id[rid]
        r["full_text_decision"] = d["decision"]
        r["final_decision"] = d["decision"]
        r["full_text_status"] = "retrieved"
        r["reviewer_1"] = REVIEWER
        r["exclusion_reason"] = d["exclusion_reason"]
        r["exclusion_reason_detail"] = d["exclusion_reason_detail"]
        excl_rows.append({
            "record_id": rid,
            "title": r["title"],
            "authors": r["authors"],
            "year": r["year"],
            "stage": "full_text",
            "exclusion_code": d["exclusion_reason"],
            "exclusion_reason_detail": d["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": TODAY,
        })

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    with open(EXCLOG, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        exc_fieldnames = reader.fieldnames
        exc_existing = list(reader)
    exc_existing.extend(excl_rows)
    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=exc_fieldnames)
        writer.writeheader()
        writer.writerows(exc_existing)
    os.replace(tmppath, EXCLOG)

    print("Batch 116 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})
    print("exclusion_log.csv new rows:", len(excl_rows))


if __name__ == "__main__":
    main()
