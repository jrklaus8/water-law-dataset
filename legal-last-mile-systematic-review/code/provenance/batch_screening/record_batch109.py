#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "RFC8814ED1AC1": {
        "decision": "include",
        "notes": (
            "Ablo & Yekple 2018, 'Urban water stress and poor sanitation in Ghana: "
            "perception and experiences of residents in the Ashaiman Municipality' "
            "(GeoJournal). A mixed-methods study (200-household survey with chi-square "
            "analysis, in-depth interviews, key informant interviews with Municipal "
            "Planning Officer and Ghana Water Company Limited officials) across 4 "
            "communities in Ashaiman, Ghana. Documents genuine legal/administrative "
            "barriers: lack of legal land documents in squatter settlements and lack "
            "of building permits preventing Ghana Water Company Limited from extending "
            "municipal water services, against real household-level access outcomes "
            "(63.5% lack pipe connection overall; 66-81% in slum communities; type of "
            "community statistically significantly predictive of in-house pipe "
            "connection and domestic-toilet presence, though exact chi-square/p-values "
            "not reported). Extracted as S623. Not effect_sizes eligible: narrative "
            "'statistically significant' association reported without exact "
            "chi-square statistic or p-value."
        ),
    },
    "R23C975B9CAD2": {
        "decision": "include",
        "notes": (
            "Muchadenyika & Williams 2018, 'Politics, Centralisation and Service "
            "Delivery in Urban Zimbabwe' (Journal of Southern African Studies). A "
            "30-interview qualitative study documenting the central government's 2005 "
            "directive centralizing water/sanitation functions from urban local "
            "authorities to ZINWA, explicitly noted as contravening the still-standing "
            "Urban Councils Act (Sections 168, 183, which continue to mandate local "
            "council water provision), against real tracked household-level outcomes: "
            "water charges increased tenfold with no service improvement, rationing to "
            "two days/week in several suburbs, a cholera outbreak (4,000 deaths); after "
            "reversion to local-authority control in 2009, City of Harare water supply "
            "improved 76.67% (300 to 530 megalitres/day) and access to potable water "
            "increased 70% (2 million to 3.4 million people). Extracted as S624. Not "
            "effect_sizes eligible: qualitative case study with narrative before/after "
            "percentage comparisons, no regression or confidence intervals."
        ),
    },
    "RCAC17563F65F": {
        "decision": "include",
        "notes": (
            "Filcak, Szilvasi & Skobla 2018, 'No water for the poor: the Roma ethnic "
            "minority and local governance in Slovakia' (Ethnic and Racial Studies). "
            "Extensive fieldwork (17 municipalities, semi-structured interviews with "
            "mayors/officials and Roma residents) documenting genuine legal/"
            "administrative barriers: municipalities and water companies explicitly "
            "stating they have no obligation to provide water/sewage to Roma "
            "households lacking land titles and/or construction permits, and "
            "municipal-debt-based conditionality (disconnection over unpaid municipal "
            "waste/water arrears) used to withhold service, against real household-"
            "level access/quality/affordability outcomes: only 39% of households in "
            "Roma settlements connected to public water supply (per the national Atlas "
            "of Roma Communities), disconnections for entire settlements (e.g. a "
            "60-person settlement in Castice cut off over disputed arrears), lab-"
            "tested water samples showing nitrate exceedances of Slovak/EU legal "
            "limits. Extracted as S625. Not effect_sizes eligible: qualitative "
            "multi-site case study, no regression."
        ),
    },
    "R77D2791283C1": {
        "decision": "include",
        "notes": (
            "Abubakar 2018, 'Strategies for coping with inadequate domestic water "
            "supply in Abuja, Nigeria' (Water International). A 60-household in-depth "
            "interview study (12 residential districts) of coping strategies for "
            "inadequate piped water. Documents a genuine legal/administrative "
            "mechanism: the Federal Capital Development Authority's ban on local "
            "wells/boreholes and the Abuja Environmental Protection Board's ban on "
            "street hawking and informal water vendors (mairuwas) in the central city, "
            "explicitly identified by the author as one of five factors shaping "
            "household coping-strategy choice, against real detailed household-level "
            "coping-strategy utilization percentages (water storage 90%, vendors 78%, "
            "boreholes 23% despite the ban, etc.) and access context (only 24.4% of "
            "Abuja households have piped connections per 2006 census; 40% reported "
            "'regular' supply in 2009). Extracted as S626. Not effect_sizes eligible: "
            "qualitative interview study with descriptive percentages, no regression."
        ),
    },
    "RCAC30132C5F4": {
        "decision": "exclude",
        "exclusion_reason": "E05",
        "exclusion_reason_detail": (
            "Silva Rodriguez de San Miguel, Trujillo Flores & Lambarry-Vilchis 2018, "
            "'Improving urban water supply in Mexico: a systematic review' (Management "
            "of Environmental Quality). A PRISMA-guided systematic review synthesizing "
            "21 secondary documents (2000-2016) on Mexico's federal/municipal urban "
            "water-supply legal and institutional framework (decentralization, private-"
            "sector participation, water pricing), explicitly self-described as "
            "'Paper type: General review.' No original empirical data collection by "
            "the authors; a general national-level policy synthesis rather than an "
            "institutional-arrangement-vs-outcome comparative analysis with real "
            "tracked data (distinguishing it from the Adams/Sambu/Smiley S618 "
            "precedent). PRISMA-style systematic review of secondary literature with "
            "no original data collection per E05, the same rationale as the Hlongwa/"
            "Nkomo Sub-Saharan Africa WASH-barriers mini-review exclusion."
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

    print("Batch 109 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
