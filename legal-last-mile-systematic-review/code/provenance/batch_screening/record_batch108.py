#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "R046A5EB2D8C0": {
        "decision": "include",
        "notes": (
            "Yadav 2018, 'A market-based solution to a sanitation issue in a "
            "marginalised area' (Development in Practice). A case study of the Center "
            "for Urban and Regional Excellence's (CURE) water and sanitation "
            "improvement project in an informal settlement (Sectors 8-10, ~11,300 "
            "households/56,374 people) in NOIDA, Uttar Pradesh, India. Documents "
            "genuine legal/administrative barriers: the township authority's Water "
            "Department 'often refused to supply water and sanitation to illegal and "
            "unauthorised settlements' and 'denied requests to improve water "
            "infrastructure due to the illegal nature of housing in the colony'; "
            "residents self-installed private bore wells and illegally extended city "
            "water lines in response. Real household-level baseline survey data "
            "(CURE 2015, n=1,127 households): 85% dependent on bottled/filtered water "
            "for consumption, 88% have private toilets, 11% rely solely on community "
            "toilets, 0.6% (11 households) have no sanitation access at all. Tracks "
            "real project outcomes: community-funded drain-cleaning contracts (165 "
            "households across 6 streets), 75+ drain patches improved, negotiated "
            "local-authority refuse pick-up. Extracted as S622. Not effect_sizes "
            "eligible: descriptive case-study/NGO program evaluation with real survey "
            "percentages, no regression testing legal-status exposure against access "
            "outcome."
        ),
    },
    "RB4C18930C3CC": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Mansur, Brondizio, Roy, de Miranda Araujo Soares & Newton 2018, 'Adapting "
            "to urban challenges in the Amazon: flood risk and infrastructure "
            "deficiencies in Belem, Brazil' (Regional Environmental Change). A mixed-"
            "methods study of urban flood-risk adaptive capacity in Belem, Brazil, "
            "using a conceptual framework distinguishing 'generic capacity' (bundling "
            "water supply, sanitation, waste management, and storm drainage into a "
            "single composite infrastructure index) and 'specific capacity' (flood "
            "response/risk-mitigation behavior). The paper's core research questions "
            "and exposure/outcome are about flood-risk adaptive capacity, not water/"
            "sanitation access as such; water and sanitation infrastructure are "
            "bundled together with paved roads and drainage into one composite index "
            "rather than analyzed as an isolated access outcome against a legal/"
            "institutional exposure. Wrong topic per E01 -- core focus is climate-"
            "adaptation/flood-risk vulnerability, with water/sanitation as one of "
            "several tangentially-bundled infrastructure components."
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

    # R33E4CEE682AC: content-completeness retrieval issue, leave open
    r33 = by_id["R33E4CEE682AC"]
    assert not r33.get("full_text_decision"), "R33E4CEE682AC already has full_text_decision"
    r33["full_text_status"] = "wrong_file_retrieved"
    r33["notes"] = (
        "Correct title/author match (Mabiza 2013 PhD dissertation, 'Integrated Water "
        "Resources Management, Institutions and Livelihoods under Stress: Bottom-Up "
        "Perspectives from Zimbabwe'), but the delivered PDF is a truncated/preview "
        "edition containing only front matter, Chapter 1 (Introduction), and the "
        "References list -- the empirical Chapters 2-9 body text (including Chapter "
        "4's Ward 1 waterpoint-committee case study, Chapter 7's Bulawayo urban-water "
        "contestation case, and Chapter 8's river basin planning case) is entirely "
        "absent from the extracted content. Confirmed via two independent extraction "
        "methods (Google Drive read_file_content and a raw-PDF download + pypdf "
        "page-by-page extraction across all 51 pages of the delivered file), both "
        "yielding the same ~145-150K-character content ending at the references list "
        "with no chapter-body text in between. Left open pending a complete/full-text "
        "re-retrieval of this dissertation -- not screened on the basis of incomplete "
        "content, per PROJECT_SPEC.md's rule against estimated/illustrative "
        "placeholder data."
    )

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

    print("Batch 108 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})
    print("R33E4CEE682AC left open, flagged wrong_file_retrieved (incomplete content)")


if __name__ == "__main__":
    main()
