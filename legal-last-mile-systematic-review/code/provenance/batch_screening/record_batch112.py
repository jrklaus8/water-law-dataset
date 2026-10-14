#!/usr/bin/env python3
import csv, os, tempfile
from datetime import date

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
TODAY = "2026-09-22"

DECISIONS = {
    "RF63F0202ABB5": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Macro/city-level comparative analysis of urban water availability "
            "and a 12-metric Institutional Complexity Assessment (ICA) index "
            "across 108 large cities (US/Africa); outcome variable is total "
            "city-wide hydrologic+captured water volume (lpcd) vs GDP and ICA "
            "score, not household- or individual-level access/connection/"
            "affordability data."
        ),
    },
    "RC0FCB69ED597": {
        "decision": "include",
        "notes": (
            "Qualitative case study of 4 Pamsimas (community-based rural water "
            "supply) villages in Indonesia (in-depth interviews, FGDs), "
            "documenting village-government policy/decrees, program "
            "governance, and BPSPAMS community-body legal status (one village's "
            "BPSPAMS lacked legal status, coinciding with program collapse) as "
            "institutional determinants of service-delivery sustainability, "
            "against real village-level tracked access outcomes (e.g. full "
            "population access achieved in one village vs ~40 households vs "
            "zero functioning access in others). Extracted as S633. Not "
            "effect_sizes eligible (qualitative multi-case comparison, no "
            "quantitative effect estimate)."
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
        if d["decision"] == "include":
            r["notes"] = d["notes"]
        else:
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

    if excl_rows:
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

    print("Batch 112 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})
    print("exclusion_log.csv new rows:", len(excl_rows))


if __name__ == "__main__":
    main()
