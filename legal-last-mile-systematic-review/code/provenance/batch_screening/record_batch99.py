#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "RE081EB767D08": {
        "decision": "include",
        "notes": (
            "Jana, Sarkar, Thomas, Krishna Priya, Bandyopadhyay, Crosbie, Abi Ghanem, "
            "Waller, Pillai & Newbury-Birch 2021, 'Rethinking water policy in India with the "
            "scope of metering towards sustainable water future' (Clean Technologies and "
            "Environmental Policy). Documentary/institutional policy analysis of 12 Indian "
            "national water supply policies (1949-2012) chronologically assessed against 20 "
            "SDG-6-derived sustainability indicators, with real government service-level "
            "benchmark data (household piped-water coverage %, cost recovery %, non-revenue "
            "water %, metering extent % across six major Indian cities), tariff/subsidy "
            "structures (increasing block tariffs, flat-rate ARV-based charges, slum vs "
            "non-slum subsidized rates), and willingness-to-pay case studies. Legal/"
            "institutional exposure: National Water Policy (1987, 2002, 2012), Five-Year Plan "
            "water programmes, state water regulatory authorities, tariff/metering regulatory "
            "gaps. Outcome: household piped-water connection coverage, tariff/subsidy "
            "affordability, water metering institutional-framework gaps. Included via the "
            "Legal Institutional Evidence Appraisal Framework, consistent with the Rout & "
            "Kattumuri India book and Theodory Tanzania precedent for documentary policy-"
            "analysis studies with real tracked government data. Not effect_sizes eligible: "
            "narrative/documentary chronological policy synthesis with descriptive tables, no "
            "single regression-based legal-exposure-vs-comparator effect estimate."
        ),
    },
    "R4D207458780C": {
        "decision": "include",
        "notes": (
            "Sohns, Ford, Adamowski & Robinson 2021, 'Participatory Modeling of Water "
            "Vulnerability in Remote Alaskan Households Using Causal Loop Diagrams' "
            "(Environmental Management). Qualitative participatory-modeling study: 14 water "
            "policy stakeholders (federal/state agencies, NGOs, academia) individually "
            "interviewed (~85 min each) to construct causal loop diagrams of household water "
            "vulnerability in rural Alaska, merged into a validated collective model with five "
            "sub-models (environmental, economic, infrastructure, social, health). Legal/"
            "institutional exposure directly examined: water quality/quantity regulations "
            "(EPA standards), water rights permits (intake/outtake), state revenue-sharing and "
            "federal operations-and-maintenance funding policy, and regulatory reform "
            "proposals -- stakeholders explicitly describe how 'the impact of regulations on "
            "the economics of water infrastructure' constrains household water access. Real "
            "empirical/quantitative grounding: documented rate disparities ($4.98/1000gal "
            "metered Anchorage vs $50/1000gal hauled Eek), per-capita water-use data, "
            "hospitalization statistics tied to lack of piped water. Outcome: household water "
            "access/availability/affordability in remote rural Alaskan communities. Satisfies "
            "core inclusion criteria via qualitative stakeholder-elicitation empirical "
            "evidence, consistent with prior qualitative-institutional-analysis includes. Not "
            "effect_sizes eligible: qualitative causal-loop-diagram synthesis, no quantitative "
            "exposure-comparator regression."
        ),
    },
    "RAFE7B383AF05": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Gordon & Byron 2021, 'Sweeping the city: infrastructure, informality, and the "
            "politics of maintenance' (Cultural Studies). A cultural-studies/urban-theory "
            "essay analyzing homeless-encampment 'sweeps' (forced removal, seizure, and "
            "destruction of tents and belongings) as acts of municipal infrastructure "
            "maintenance and governance in Toronto and San Francisco, drawing on Call 311 "
            "encampment-removal data and case vignettes (Dinner With a View/Bentway, DPW "
            "sweeps). The paper's theoretical lens uses 'infrastructure' broadly to encompass "
            "housing, tents, and informal survival networks; it references 'the right to "
            "sanitation' and a UN special rapporteur report on water/sanitation rights only in "
            "passing. No household-level water or sanitation SERVICE-ACCESS outcome is "
            "empirically examined -- the actual outcome measured is homeless-encampment "
            "removal/dispossession, a housing and policing topic outside this review's "
            "water/sanitation access scope. Wrong topic per E01."
        ),
    },
    "R0F2F1A4CDE94": {
        "decision": "include",
        "notes": (
            "Gonzalez Rivas 2023, 'Addressing the impossible triad - high inequality, "
            "decentralized policy and low local capacity - challenges for drinking water "
            "policy in Mexico' (International Planning Studies). Mixed-methods institutional "
            "analysis combining Mexican census data (INEGI, household piped-water-connection "
            "rates by municipality, 1950-2010) with 15 in-depth interviews (2011-2013) of "
            "federal/state water-agency officials, plus document analysis of the 1972 Federal "
            "Waters Law, decentralization reform (1976, 1980s-90s), and CONAGUA/PROII funding-"
            "programme eligibility rules. Legal/institutional exposure: decentralization of "
            "water policy from national to municipal governments, and the cumulative social/"
            "legal/technical permit requirements (water-use permits, environmental-impact "
            "rulings, water-quality testing) that disadvantaged low-capacity municipalities "
            "must meet to access federal water-infrastructure funding. Outcome: household "
            "piped-water connection rates by municipality, cross-tabulated against local "
            "institutional/technical capacity and socio-economic disadvantage (Table 1: e.g. "
            "33% of municipalities have <26% household water connection, concentrated among "
            "high-dirt-floor, high-indigenous-share, low-technical-capacity municipalities; "
            "only 10% of Oaxaca's federal funding proposals accepted due to technical-capacity "
            "barriers). Included via the Legal Institutional Evidence Appraisal Framework, "
            "consistent with prior decentralization/institutional-capacity includes. Not "
            "effect_sizes eligible: author explicitly states the descriptive cross-tabulation "
            "is not intended to establish a causal driver relationship ('I am not claiming "
            "that these variables might be the drivers... rather the goal... is to portray the "
            "characteristics'), so there is no locatable regression-based exposure-comparator "
            "effect estimate."
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

    print("Batch 99 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
