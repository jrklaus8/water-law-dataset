#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "R43A5C339BB4D": {
        "decision": "include",
        "notes": (
            "Button 2017, 'Domesticating water supplies through rainwater harvesting "
            "in Mumbai' (Gender & Development). A qualitative study (site visits to "
            "22 apartment buildings and 1 informal settlement, interviews with 33 "
            "professionals/officials, 16 residents, 3 servants) examining Mumbai's "
            "mandatory rainwater-harvesting ordinance (compulsory since 2003 for new "
            "buildings over 1,000 sq m, since 2007 for those over 300 sq m), which "
            "shifts formal legal responsibility for water provision from the "
            "municipal corporation to individual households. Documents real "
            "household/servant-level access disparities (e.g. maids from informal "
            "settlements reporting queuing for a single tap with two hours of supply, "
            "versus middle-class buildings' secured rainwater-harvesting supply) and "
            "the municipality's explicit acknowledgment of using self-supply "
            "regulation to reduce mains-supply obligations. Extracted as S630. Not "
            "effect_sizes eligible: qualitative case-study/ethnographic research, no "
            "regression."
        ),
    },
    "R1CA3290F50A5": {
        "decision": "include",
        "notes": (
            "Lewis 2017, 'Does local government proliferation improve public service "
            "delivery? Evidence from Indonesia' (Journal of Urban Affairs). A "
            "quasi-experimental panel-data study (generalized difference-in-"
            "differences and dynamic panel GMM, standard errors clustered at the "
            "district level, parallel-trends falsification tests) exploiting the "
            "plausibly exogenous timing of local-government proliferation (pemekaran "
            "-- the legal/administrative splitting of district jurisdictions) using "
            "national household-survey data (BPS/SUSENAS) across 336 districts "
            "(2,714 district-year observations for the infrastructure model). Finds "
            "that new-district creation reduces household access to protected water "
            "and sanitation by about 1.35 percentage points in the short run (lag-1 "
            "year), implying a long-run reduction of about 1.75% (p=.023), relative "
            "to original (non-split) districts; no significant effect relative to "
            "split-off districts or on education access. Extracted as S631. "
            "EFFECT_SIZES ELIGIBLE: a clean legal/administrative jurisdictional-"
            "restructuring exposure tested via a well-identified quasi-experimental "
            "panel design against a directly measured household-level water/"
            "sanitation access-percentage outcome, with a reported point estimate, "
            "p-value, and robust clustered standard errors (Family C)."
        ),
    },
    "RD67971FB4FB1": {
        "decision": "include",
        "notes": (
            "Fonjong & Fokum 2017, 'Water Crisis and Options for Effective Water "
            "Provision in Urban and Peri-Urban Areas in Cameroon' (Society & Natural "
            "Resources). A mixed-methods study (49 household interviews plus 15 "
            "public/water-official interviews across 5 municipalities) examining the "
            "impact of Cameroon's 2005 water-sector privatization (SNEC dissolved, "
            "replaced by parastatal CamWater and private operator CDE) against "
            "household-level water access. Documents privatization as running "
            "'contrary to the spirit of Law 98/005 of April 14, 1998, on the water "
            "sector, which makes the state responsible for access to water by all "
            "Cameroonians,' against real survey data: only 39% of peri-urban "
            "residents surveyed have pipe-borne access (Table 1, by municipality), "
            "61% rate privatization's effect on water provision negatively (Table 2), "
            "and a successful legal challenge (with Human Rights Watch/INTERIGHTS) "
            "against billing residents for unconsumed water. Extracted as S632. Not "
            "effect_sizes eligible: descriptive survey percentage tables by "
            "municipality, no regression or confidence intervals."
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

    print("Batch 111 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
