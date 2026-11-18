#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "R221EA3C5B171": {
        "decision": "include",
        "notes": (
            "Mugambe, Tumwesigye & Larkan 2013, Journal of Public Health, "
            "qualitative study (6 focus group discussions/49 participants, 12 "
            "key-informant interviews) of WASH access barriers among people "
            "living with HIV/AIDS in Gomba and Mpigi districts, Uganda, "
            "documenting a genuine institutional/administrative barrier "
            "(flat-rate public-latrine and water-vendor fee structures with no "
            "pro-poor/vulnerable-group consideration, and exclusion of PLWHA "
            "from water-user-committee management/non-functional facility "
            "management committees) alongside financial, social, physical, "
            "attitudinal and knowledge barriers. Extracted as S645. Not "
            "effect_sizes eligible (qualitative FGD/KII study)."
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

    for rid, d in DECISIONS.items():
        r = by_id[rid]
        r["full_text_decision"] = d["decision"]
        r["final_decision"] = d["decision"]
        r["full_text_status"] = "retrieved"
        r["reviewer_1"] = REVIEWER
        r["notes"] = d["notes"]

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Batch 115 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
