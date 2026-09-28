#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "R83FCFEB8D3DB": {
        "decision": "include",
        "notes": (
            "Akpabio & Udofia 2017, 'Unsafe water, sanitation and hygiene in "
            "Nigeria's public spaces: the political economy angle' (International "
            "Journal of Water Resources Development). A field study (20 public "
            "spaces visited, 100 interviews) in Ikot Ekpene, Nigeria, examining WASH "
            "conditions in public spaces (abattoir, market, motor park, schools, "
            "eateries, worship places) through a political-economy lens. Documents a "
            "genuine institutional/regulatory factor: 'weak or non-existent "
            "regulation and enforcement of necessary standards' as a central finding, "
            "corroborated by interviews with local council and State Ministry of "
            "Environment officials on regulation/enforcement/monitoring practices, "
            "against real toilet-to-user ratios and water-supply-source data across "
            "20 public places (Table 3), and city-wide statistics (only 1.4% of Ikot "
            "Ekpene's urban population served by the water company per Udom 2011). "
            "Extracted as S627. Not effect_sizes eligible: descriptive field-study "
            "tabulation, no regression."
        ),
    },
    "RA1B1F2182B55": {
        "decision": "include",
        "notes": (
            "Pierce 2017, 'Why is basic service access worse in slums? A synthesis "
            "of obstacles' (Development in Practice). A mixed-methods study (26 "
            "semi-structured interviews, a 789-household survey, and 500 programme "
            "representation records) across 4 slum settlements in Hyderabad, India, "
            "developing a typology of economic/spatial/social/institutional/political "
            "obstacles to basic service access. Documents a genuine institutional/"
            "legal exposure: government recognition/notification status affecting "
            "tenure security and service extension (e.g. Rasoolpura's contested "
            "jurisdictional boundary between two local agencies denying "
            "responsibility for water/sanitation provision), against real "
            "household-level access outcomes (Anna Nagar residents receive piped "
            "water for only 60 minutes every 8-10 days; a 2009 E. coli contamination "
            "incident killed at least 14 people in Bholakpur). Extracted as S628. Not "
            "effect_sizes eligible: qualitative/typological synthesis study, no "
            "regression presented in this paper."
        ),
    },
    "R8C684502F84D": {
        "decision": "include",
        "notes": (
            "Eichelberger 2018, 'Household water insecurity and its cultural "
            "dimensions: preliminary results from Newtok, Alaska' (Environmental "
            "Science and Pollution Research). An ethnographic study (23 "
            "semi-structured interviews) of household water access in a remote Yupik "
            "village lacking in-home plumbing. While centrally framed through a "
            "cultural/relational lens, the study documents genuine institutional/"
            "administrative factors -- village-government revenue constraints "
            "limiting infrastructure operations and maintenance, State of Alaska "
            "Village Safe Water program storage tanks installed but left unused due "
            "to ground-settling issues, and a school-district administrative rule "
            "rationing residents to a maximum of 10 gallons of treated water per day "
            "during water-plant shutdowns -- against real quantified household-level "
            "water-access outcomes (community per-capita treated-water consumption "
            "of 1.91 gal/person/day per water-plant records; 37 of 53 households have "
            "a dedicated honey-bucket room). Extracted as S629. Not effect_sizes "
            "eligible: ethnographic qualitative study with descriptive consumption "
            "statistics, no regression."
        ),
    },
    "R3F81DA1627AD": {
        "decision": "exclude",
        "exclusion_reason": "E04",
        "exclusion_reason_detail": (
            "de Carvalho, Cunha Marques & Cordeiro Netto 2018, 'Regulatory Impact "
            "Assessment (RIA): an Ex-Post Analysis of Water Services by the Legal "
            "Review in Portugal' (Water Resources Management). An ex-post regulatory "
            "impact assessment of Portugal's Law no.194/2009 (public-private "
            "partnership water-sector reform) using Delphi expert elicitation and "
            "TOPSIS multicriteria decision analysis across 11 concessionaires. The "
            "outcome criteria assessed (coverage of total costs, equity-to-assets "
            "ratio, mains replacement rate, affordability level as a financial-"
            "sustainability indicator) are utility/concessionaire-level financial and "
            "governance performance metrics drawn from ERSAR regulator data, not "
            "household/applicant-level connection, access, or affordability "
            "outcomes. Wrong outcome per E04, the same rationale as the prior DEA-"
            "efficiency utility-performance exclusions (Nithammer, Gidion, Armah & "
            "Rodrigues)."
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

    print("Batch 110 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
