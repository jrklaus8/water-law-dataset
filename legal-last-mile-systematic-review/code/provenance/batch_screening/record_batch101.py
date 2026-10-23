#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "R7CD58D2E7BE3": {
        "decision": "include",
        "notes": (
            "Agbemor & Smiley 2021, 'Tensions between Formal and Informal Water Providers: "
            "Receptivity toward Mechanised Boreholes in the Sunyani West District, Ghana' "
            "(Journal of Development Studies). Case-study survey: census of 98 mechanised "
            "boreholes, interviews with 89 private operators + 2 Water and Sanitation "
            "Management Teams, and 2,439 water-user interviews, examining privately managed "
            "informal boreholes operating in legal defiance of Ghana's groundwater-abstraction "
            "regulations (Water Resources Commission L.I. 1692, 2001; CWSA regulations, L.I. "
            "2007, 2011) -- none of the private operators sought approval from the District "
            "Authority or WRC permits, and no enforcement action was taken against them. "
            "Outcome: household water access/reliability (91 of 93 assessed boreholes "
            "functioned >=347 days/year), quantity (>=25 L/person/day, above CWSA's 20 L "
            "minimum), distance/time, and affordability (comparable tariffs to formal GWCL "
            "standpipes). Satisfies core inclusion criteria via a genuine legal-status "
            "exposure (informal/'illegal' vs regulated water provision) tested against "
            "household-level access outcomes. Not effect_sizes eligible: descriptive survey "
            "statistics, no regression-based exposure-comparator effect estimate."
        ),
    },
    "R77355A6C9E10": {
        "decision": "include",
        "notes": (
            "Tantoh & McKay 2020, 'Rural self-empowerment: the case of small water supply "
            "management in Northwest, Cameroon' (GeoJournal). Household survey (108 "
            "households, 18 per village across 6 villages/3 districts) examining "
            "community-based water management (CBWM) under Cameroon's 1998 water law (which "
            "authorized private individuals and community groups as water-development "
            "actors), against real household-level access/consumption/affordability "
            "outcomes: 34% of households achieved private connections vs 66% relying on "
            "communal taps (Water Management Committee-set upfront cash-eligibility "
            "requirements determined who could afford a private connection); mean water "
            "consumption of 35.6 L/capita/day for private-connection households vs 24.7 "
            "L/capita/day for communal-tap households (both below the WHO/UHCHR 100 L/c/d "
            "standard); 71 of 108 surveyed households could not afford connection fees, and "
            "54% were unable to regularly pay the monthly USD1 communal-tap fee. Satisfies "
            "core inclusion criteria via a genuine legal/institutional exposure (CBWM legal "
            "authorization and WMC-set eligibility/fee requirements) tested against "
            "household-level water access and consumption outcomes. Not effect_sizes "
            "eligible: descriptive per-village means with no reported significance test or "
            "regression, and small per-village samples (n=18)."
        ),
    },
    "R96A74867D7C2": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Sandoval & Sarmiento 2020, 'A neglected issue: informal settlements, urban "
            "development, and disaster risk reduction in Latin America and the Caribbean' "
            "(Disaster Prevention and Management). Macro/national-level comparative content "
            "analysis of 17 Habitat III National Reports (Argentina through Uruguay), "
            "examining urban informal-settlement prevalence and 'risk governance'/'disaster "
            "resilience' policy discourse under the New Urban Agenda and Sendai Framework. "
            "Access to drinking water and sewerage appears only as an aggregate national-level "
            "statistic, one of the UN-Habitat's five 'deprivations' used to define informal "
            "settlements, not as an outcome tested against any specific legal/administrative "
            "mechanism -- the paper's actual empirical focus and unit of analysis is national "
            "governance-discourse content analysis, not household-level water/sanitation "
            "access. Wrong topic/unit of analysis per E01, the same macro cross-national "
            "governance-index rationale as the Nkiaka, Shadabi & Ward, Laitinen, and Schiel "
            "et al. exclusions."
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

    print("Batch 101 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
