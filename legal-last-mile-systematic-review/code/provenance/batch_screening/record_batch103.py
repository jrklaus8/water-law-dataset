#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "RD0DFF88DB422": {
        "decision": "exclude",
        "exclusion_reason": "E06",
        "exclusion_reason_detail": (
            "Foster, McSorley & Willetts 2019, 'Comparative performance evaluation of "
            "handpump water-supply technologies in northern Kenya and The Gambia' "
            "(Hydrogeology Journal). A rigorous field-based engineering evaluation "
            "comparing handpump models (BluePump vs Afridev, India Mark II, PB Mark II) "
            "via univariable/multivariable logistic and linear regression against "
            "functionality, breakdown-frequency, and breakdown-duration outcomes across "
            "142 (Turkana) and 161 (Gambia) water points. The key explanatory variable "
            "tested is handpump technology/design type, a mechanical/engineering exposure, "
            "not a legal/administrative/institutional/regulatory factor -- handpump "
            "standardisation policy is noted only as background context, not the tested "
            "exposure. Engineering-only per E06, the same rationale as prior water-point-"
            "technology/GIS-mapping exclusions (Jimenez & Perez-Foguet)."
        ),
    },
    "R488CB489640F": {
        "decision": "exclude",
        "exclusion_reason": "E12",
        "exclusion_reason_detail": (
            "Venugopal, Foord & Singaram 2020, 'Lifting the Lid Off the Toilet -- "
            "Understanding the Indian Context and A Case on Samagra Empowerment "
            "Foundation' (book chapter in Socio-Tech Innovation). A business-school "
            "teaching case study (explicitly structured with a 'Brief Teaching Note,' "
            "'Assignment Questions,' and a class-process/timing table for MBA-style "
            "instruction) profiling a single social enterprise's (Samagra) self-reported "
            "impact metrics for its SmartLOO public-toilet IoT platform in Pune, India. "
            "No systematic sampling method, interview protocol, or data-collection "
            "methodology is described -- the case draws entirely on the company's own "
            "self-reported figures for pedagogical narrative purposes, not as an "
            "independent empirical study. Wrong study design per E12, the same rationale "
            "as the prior 'Defining Moments' reflective-narrative-essay exclusion "
            "(R8A34FFD0A52F) for lacking a described sample size, sampling method, or "
            "systematic coding protocol."
        ),
    },
    "REFA4001EDBED": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Ahmed 2020, 'Does state capacity matter for foreign aid effectiveness? Panel "
            "data evidence on water from 87 countries' (Water International). A macro/"
            "country-level panel-data study (87 aid-receiving countries, 2002-2015) testing "
            "whether state capacity (Bureaucratic Quality Index) mediates the effect of "
            "foreign aid on aggregate national-level 'percentage of population with access "
            "to an improved source of water' via random-effects, fixed-effects, and system "
            "GMM regression. The exposure (state capacity) and outcome (aggregate national "
            "water-access percentage) are both measured at the country level, with no "
            "household/applicant-level legal-administrative access mechanism examined. "
            "Wrong topic/unit of analysis per E01, the same macro cross-national governance-"
            "index rationale as the Nkiaka, Shadabi & Ward, Laitinen, Schiel et al., and "
            "Sandoval & Sarmiento exclusions."
        ),
    },
    "RE06ED02A63C7": {
        "decision": "include",
        "notes": (
            "Shuaib & Rana 2020, 'Assessing water supply for the urban poor in Rajshahi "
            "City, Bangladesh' (Management of Environmental Quality). Questionnaire "
            "survey (100 heads of household across 10 slums in 3 zones -- inner, middle, "
            "outer) applying a 6-dimension water-supply performance framework (biophysical, "
            "technical, political, institutional, economic, social) developed by Akbar "
            "et al. (2007). Genuine legal/institutional exposure directly examined: slum "
            "residents in 'unrecognized' communities lack the legal right to apply for "
            "formal water connections, resulting in widespread informal/illegal pipeline "
            "connections tolerated but only occasionally monitored by authorities (4 of 10 "
            "slums reported monitored vs 6 never monitored); documented institutional "
            "corruption in connection installation (BDT 2000-3000 bribes paid to Water and "
            "Sewerage Authority fieldworkers, with favoritism in tubewell placement). "
            "Outcome: household-level water access/quantity (61% receive only 10-20 L/"
            "person/day, below WHO minimums), reliability (79% receive water only 4-8 "
            "hours/day), distance/queuing, affordability (majority report water charges "
            "too high), and waterborne-disease incidence, all varying systematically by "
            "slum location/zone. Satisfies core inclusion criteria via a genuine legal-"
            "status/institutional-corruption exposure tested against household-level "
            "access outcomes. Not effect_sizes eligible: descriptive composite "
            "weighted-average performance indices by slum, no regression-based "
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

    print("Batch 103 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
