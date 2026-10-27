#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "RD7BE4A2810FC": {
        "decision": "include",
        "notes": (
            "Poonia & Punia 2019, 'Associates and determinants of drinking water "
            "supply: a case study along urban-rural continuum of semi-arid cities in "
            "India' (Urban Water Journal). A 280-household survey (chi-square test + "
            "seven-predictor binary logistic regression) across core/outskirts/village "
            "locations along the urban-rural continuum of two Rajasthan cities. Among "
            "the tested predictors, 'payment per month for water' is explicitly "
            "interpreted by the authors as a proxy for institutional (municipal) vs. "
            "private water-supply arrangement ('this group is associated with "
            "institutional (municipal) water supply'; 'payment which is more than 300 "
            "Rs. per month is associated with private water suppliers... no "
            "institutional arrangement for drinking water supply'), with real odds "
            "ratios and 95% CI against a dichotomous 'good drinking water supply' "
            "outcome (piped water within premises, sufficiency, daily supply, no "
            "quality defect). Location along the urban-rural continuum (differential "
            "institutional/municipal coverage between city core and villages) is also a "
            "significant determinant. Extracted as S620. Not effect_sizes eligible: the "
            "institutional-arrangement variable is an indirect proxy (payment-amount "
            "category) embedded among several socioeconomic covariates (caste, "
            "education, occupation, income) in a combined regression, not a single "
            "directly-coded legal/institutional exposure variable in the Family A/B/C "
            "sense."
        ),
    },
    "RBF205A6C9F47": {
        "decision": "include",
        "notes": (
            "Reddy 2018, 'Techno-institutional models for managing water quality in "
            "rural areas: case studies from Andhra Pradesh, India' (International "
            "Journal of Water Resources Development). A mixed-methods comparative case "
            "study (FGDs, village transect walks, 240-household survey across 8 "
            "villages) examining public-private-community institutional partnership "
            "arrangements (gram panchayat, private foundations Byrraju/Naandi/Sai Oral "
            "Health, government RWSSD) governing water treatment plant service "
            "delivery. Documents real empirical outcome data: household coverage rates "
            "by land-ownership/socioeconomic group (18-43% across landless to large "
            "farmers), quantity limitation (treated water meeting only ~10% of "
            "household demand under RO/UV models vs. full domestic needs under "
            "microfilter models), pricing/affordability by institutional model, and "
            "inclusiveness gaps by socioeconomic group. Goes beyond water-quality-only "
            "framing to examine institutional governance structures (panchayat "
            "resolutions, tripartite agreements, village development councils) "
            "directly tested against service coverage/access/affordability outcomes. "
            "Extracted as S621. Not effect_sizes eligible: comparative case-study "
            "design with descriptive coverage percentages and financial-viability "
            "metrics (NPV/benefit-cost ratio) across 8 villages, no regression testing "
            "institutional arrangement against a household-level access outcome."
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

    print("Batch 107 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
