#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "RB27F53708057": {
        "decision": "include",
        "notes": (
            "Chapman, Merceron, Myers & Wood 2020, 'Women's lived-experiences of water "
            "infrastructure in Gressier, Haiti' (Water International). Qualitative "
            "ethnographic study: 32 in-depth semi-structured interviews (drawn from a "
            "304-participant base sample) with women in Gressier, Haiti, examining household "
            "water access, infrastructure barriers, and community-led solutions. Documents "
            "informal, unregulated neighbor-to-neighbor pipe-installation networks operating "
            "without formal government documentation or oversight (no accessible records of "
            "existing infrastructure; DINEPA, Haiti's national water/sanitation directorate, "
            "and international NGOs/relief agencies are the nominal but largely absent formal "
            "authorities), informal payment schemes with service-restriction consequences for "
            "non-payment (an estimated 40% of households with piped water access have "
            "services restricted monthly for non-payment), and informal source-management "
            "disputes. Outcome: household water access, service reliability/continuity "
            "(scheduled-day water cutoffs), and cost/affordability (parts/labour up to US$100 "
            "for pipe installations that never functioned, against a population where 59% "
            "earn <US$3/day). Satisfies core inclusion criteria via qualitative ethnographic "
            "empirical evidence documenting the legal/institutional vacuum around informal "
            "water infrastructure governance. Not effect_sizes eligible: qualitative "
            "interview-based study, no quantitative exposure-comparator regression."
        ),
    },
    "R70C06383A22C": {
        "decision": "include",
        "notes": (
            "McCulligh, Arellano-Garcia & Casas-Beltran 2020, 'Unsafe waters: the hydrosocial "
            "cycle of drinking water in Western Mexico' (Local Environment). Mixed-methods "
            "study: semi-structured interviews with municipal/state water officials and "
            "industry representatives, plus a 293-household survey across 4 Jalisco "
            "municipalities (including El Salto, n=89), examining drinking water quality, "
            "regulation, and access in three case-study areas (El Salto/Toluquilla aquifer, "
            "Guadalajara Metropolitan Area/Santiago River, San Juan de los Lagos). Genuine "
            "legal/institutional exposure directly documented: Mexico's 1992 National Waters "
            "Law concession system, CONAGUA's near-nonexistent enforcement (an average of only "
            "269 inspections/year across 41,116 water extraction/discharge concessions in "
            "Jalisco -- would take 150+ years to inspect all users), the weak NOM-127-SSA1-1994 "
            "drinking-water standard (scoring second-worst of 6 countries compared against WHO "
            "guidelines), and the 1983 constitutional decentralization of water services to "
            "under-resourced municipalities. Outcome: household water-service intermittency "
            "(household survey: only 34.1% of respondents receive water daily, 38.6% every "
            "third day, 27.3% twice a week or less) and affordability (48% of surveyed "
            "households resorted to tanker-truck water at 358% higher cost than piped supply). "
            "Satisfies core inclusion criteria. Not effect_sizes eligible: descriptive survey "
            "statistics embedded in a qualitative case-study narrative, no regression-based "
            "exposure-comparator effect estimate."
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

    print("Batch 100 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
