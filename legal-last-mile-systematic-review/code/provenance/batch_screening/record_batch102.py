#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "R7DF720007123": {
        "decision": "include",
        "notes": (
            "Reniko & Kolawole 2020, \"'They don't read metres, they only bring bills': Issues "
            "surrounding the installation of prepaid water metres in Karoi town, Zimbabwe\" "
            "(South African Geographical Journal). Qualitative case study: document analysis, "
            "unstructured interviews, focus group discussions, and observations with 35 "
            "purposively/convenience-sampled residents across 5 high-density residential "
            "areas (Chiedza B, Chiedza D, Garikai, Claudia, Chikangwe), plus interviews with "
            "Karoi Town Council (KTC) and Zimbabwe National Water Authority (ZINWA) officials, "
            "examining the proposed installation of prepaid water meters (PWMs) as a "
            "legal/institutional shift from Zimbabwe's traditional post-paid block-tariff "
            "billing system. Genuine legal/institutional exposure: residents and a "
            "school-teacher interviewee explicitly frame PWMs as violating the Zimbabwean "
            "Constitution's right to water and the UN ICESCR human right to water, given "
            "PWMs' automatic disconnection upon exhausted credit (removing dispute-resolution "
            "safeguards available under post-paid billing). Outcome: household water access/ "
            "affordability/disconnection risk, plus real revenue-collection data (Table 2: "
            "actual vs possible monthly revenue collected by residential area, ranging 1.6%-"
            "26.8% of possible revenue collected under the existing post-paid system). "
            "Satisfies core inclusion criteria via qualitative case-study empirical evidence "
            "directly engaging a legal/constitutional exposure against household-level access "
            "outcomes. Not effect_sizes eligible: PWMs had not yet been installed at the time "
            "of study (captures pre-implementation stakeholder perceptions/debate), so no "
            "exposure-comparator outcome regression exists."
        ),
    },
    "R77FE93587FBF": {
        "decision": "exclude",
        "exclusion_reason": "E05",
        "exclusion_reason_detail": (
            "Grigg 2020, 'Smart water management: can it improve accessibility and "
            "affordability of water for everyone?' (Water International). A conceptual/"
            "theoretical discussion paper examining how emerging smart-water-management (SWM) "
            "information and control technologies could hypothetically improve water utility "
            "access and affordability. The paper explicitly describes its central "
            "demonstration as conceptual ('The approach is conceptual, but it builds on "
            "recent research') -- an illustrative, non-empirical scenario of extending water "
            "service to condominium housing, not an original empirical study with real data "
            "collection. No original empirical evidence per E05, the same rationale as the "
            "Saadi & Johns 'Governing smart water cities' conceptual-scoping-paper exclusion."
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
        assert rid in by_id, f"{rid} not found in DB"
        r = by_id[rid]
        assert not r.get("full_text_decision"), f"{rid} already has full_text_decision"
        assert not r.get("final_decision"), f"{rid} already has final_decision"

    exclusion_rows = []
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
            r["notes"] = d["exclusion_reason_detail"]
            exclusion_rows.append({
                "record_id": rid,
                "title": r.get("title", ""),
                "authors": r.get("authors", ""),
                "year": r.get("year", ""),
                "stage": "full_text",
                "exclusion_code": d["exclusion_reason"],
                "exclusion_reason_detail": d["exclusion_reason_detail"],
                "reviewer": REVIEWER,
                "date": DATE,
            })

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    if exclusion_rows:
        with open(EXCL, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            excl_fieldnames = reader.fieldnames
            excl_rows = list(reader)
        excl_rows.extend(exclusion_rows)
        fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCL))
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=excl_fieldnames)
            writer.writeheader()
            writer.writerows(excl_rows)
        os.replace(tmppath, EXCL)

    print("Batch 102 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
