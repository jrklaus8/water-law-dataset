#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
TODAY = "2026-09-22"

DECISIONS = {
    "RC4A4206BDF16": {
        "decision": "include",
        "notes": (
            "Appelblad Fredby & Nilsson 2013, Journal of Eastern African Studies, "
            "historical-institutional case study of Kampala, Uganda's pro-poor "
            "water provision, documenting the 2004 NWSC connection policy, "
            "performance-contract governance reforms, land-tenure/property-"
            "rights barriers to piped connections in informal settlements, and "
            "the 2006-onward 'Water to the Urban Poor' pre-paid-meter pilot "
            "project, against real connection statistics (170,000 national "
            "connections vs. only 6,000 in poor urban areas in 2007) and "
            "interview data. Extracted as S643. Not effect_sizes eligible "
            "(historical/interview-based case study, no regression-based "
            "effect estimate)."
        ),
    },
    "R2033EDC2AA88": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Erhard, Degabriele, Naughton & Freeman 2013 examines WASH policy "
            "and facility provision for children with disabilities in schools "
            "in Malawi and Uganda; the unit of analysis is the school "
            "(institutional, non-household) setting, the same rationale as the "
            "Chatterley et al. and Abu/Elliott/Karanja school/healthcare-"
            "facility WASH exclusion precedents."
        ),
    },
    "R14B39B9D52E2": {
        "decision": "include",
        "notes": (
            "Vasquez & Franceschi 2013, Water Resources Management, a 690-"
            "household contingent-valuation survey in Leon, Nicaragua testing "
            "household willingness-to-pay and preferences for centralized "
            "(ENACAL, national utility) versus decentralized (municipal) water-"
            "service governance under Nicaragua's law of municipalities and "
            "2005-2015 National Water Strategy decentralization policy, using "
            "censored logistic regression (Cameron 1988) and split-sample "
            "experimental design. Extracted as S644. Not effect_sizes eligible: "
            "the CITY (centralization) coefficient itself is not statistically "
            "significant in the pooled WTP regression model, though a "
            "categorical preference distribution favoring the centralized "
            "provider is significant via binomial tests."
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

    print("Batch 114 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})
    print("exclusion_log.csv new rows:", len(excl_rows))


if __name__ == "__main__":
    main()
