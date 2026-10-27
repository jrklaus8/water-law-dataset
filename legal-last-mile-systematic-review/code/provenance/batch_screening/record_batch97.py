#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "RD6A4E2B98389": {
        "decision": "include",
        "notes": ("Theodory 2022, Norsk Geografisk Tidsskrift. Mixed-methods study (129-household "
                   "survey + 6 FGDs + 18 KIIs, 3 villages) of formal (National Water Policy, Water "
                   "Resources Management Act 2009, Water Supply and Sanitation Act 2019) and informal "
                   "(COBWSO community water organization) institutions governing water access in the "
                   "Mgeta subcatchment, Tanzania. Reports household-level improved/unimproved water "
                   "source access and satisfaction by village, tied directly to presence/absence of an "
                   "effective COBWSO. record_id RD6A4E2B98389."),
    },
    "R68EEE02D1AF5": {
        "decision": "include",
        "notes": ("Rout & Kattumuri 2022, 'Urban Water Supply and Governance in India' (Springer "
                   "book). Household survey (n=3,714) across 4 Indian cities (Ahmedabad, Bengaluru, "
                   "Hyderabad, Kochi) examining domestic water access/usage/expenditure and quantitative "
                   "institutional-performance comparison (efficiency/effectiveness/customer-satisfaction "
                   "ANOVA by institutional-arrangement type: departmental, parastatal, corporatized "
                   "utility). Directly on-topic for legal/institutional mechanisms of water-service "
                   "connectivity/exclusion. record_id R68EEE02D1AF5."),
    },
    "R805217DA7537": {
        "decision": "include",
        "notes": ("Twani & Soyapi 2022, South African Journal on Human Rights (case note). Jurimetric "
                   "analysis of 4 South African cases (Nokotyana, Beja, Kenton, Msunduzi) on municipal "
                   "legal accountability for sanitation-service-delivery failures, documenting concrete "
                   "real-community outcomes (e.g. Beja: court ordered enclosure of 1,316 toilets in "
                   "Khayelitsha's Silvertown project; Msunduzi: court ordered VIP-toilet construction "
                   "for named farm-occupier households) resulting from litigation/structural interdicts. "
                   "Legal Institutional Evidence Appraisal Framework applies (jurimetric). "
                   "record_id R805217DA7537."),
    },
    "R97E03B20C00D": {
        "decision": "include",
        "notes": ("Sullivan Lemaitre & Stoler 2023, Water International. Narrative literature review "
                   "(no systematic-review search protocol) applying an urban water security territory "
                   "framework to Cartagena, Colombia's 1991-2019 water governance history: 1994 "
                   "privatization (Law 142), land-use zoning law (POT, Decree 0977/2001) systematically "
                   "excluding slums from official service zones, and 11 mayors in 9 years of political "
                   "instability blocking POT renewal. Reports concrete coverage-rate discrepancies "
                   "(96.35%/86.32% recalculated vs. official 99.91%/93.6%) and an estimated "
                   "25,898-70,000 un-serviced rural-zone residents. Legal Institutional Evidence "
                   "Appraisal Framework applies. record_id R97E03B20C00D."),
    },
    "R4B1669E987E0": {
        "decision": "include",
        "notes": ("Dakyaga, Schramm & Kyessi 2023, Urban Geography. Mixed-methods case study (292-"
                   "household survey + 45 water-operator interviews, 3 peri-urban settlements) of "
                   "self-governed off-utility-grid water provision in Dar es Salaam, Tanzania, examining "
                   "Section 11(3) of the Water Resources Management Act 2009 (permit-free domestic "
                   "shallow-well exemption vs. commercial-extraction permit requirement, unenforced "
                   "against market-oriented operators) and its relationship to reliability/distance/"
                   "affordability disparities by income group and provider-registration status. "
                   "record_id R4B1669E987E0."),
    },
    "R6103D8CFE42F": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Aluko, Esan, Agboola, Ajibade, John, Obadina & Afolabi 2022, Int. J. Environ. Health Res. "
            "Descriptive cross-sectional study (420 inmates, logistic regression) of sanitation/hygiene "
            "conditions and predictors of handwashing/toilet-cleaning behavior in a maximum-security "
            "Nigerian prison. Population is institutionalized (incarcerated) individuals, not a household "
            "or community-level unit of analysis; predictors are individual-level (religion, education, "
            "gender, toilet type) rather than a legal/administrative access mechanism. Same institutional "
            "(non-household) unit-of-analysis rationale as prior WASH-in-healthcare-facilities and "
            "WASH-in-schools exclusions (R7863774753EC, R3B73F903D49F)."
        ),
    },
    "RF0B06784A547": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Wang, Man, Xu & Shi 2022, Progress in Geography (Chinese-language; read and evaluated in "
            "the original Chinese, translation feasible per INCLUSION_EXCLUSION.md criterion 10). "
            "Urban-political-ecology documentary/secondary-data analysis (government reports, "
            "statistical yearbooks, water-bureau bulletins, municipal regulations) of Shenzhen's "
            "city-scale water-resource commodification/governance evolution across 3 periods "
            "(1979-2005, 2006-2015, 2016-present). Outcomes examined are aggregate city-level water "
            "consumption, wastewater discharge volumes, and river/coastal water-quality classifications "
            "-- macro/city-level water-RESOURCES governance, not a household or population-level "
            "water-SERVICE ACCESS outcome (connection, coverage, affordability, reliability). Same "
            "macro/basin-level rationale as prior Nkiaka and Nigeria-OECD-water-governance-principles "
            "exclusions."
        ),
    },
    "R7E87780D0891": {
        "decision": "include",
        "notes": ("Mariwah 2022, book chapter in 'Democratic Decentralization, Local Governance and "
                   "Sustainable Development' (Springer). Rapid review (not a systematic review -- no "
                   "described search protocol) plus author's own facilitator/verification-team "
                   "observations, examining Ghana's 1992 Constitution, Local Government Act 1993/2016, "
                   "Environmental Sanitation Policy 1999/2010, and CWSA Act 1998 as legal/institutional "
                   "determinants of sanitation-service delivery; documents a genuine 'institutional "
                   "dilemma' (overlapping MSWR/MLGRD ministerial responsibility), by-law "
                   "non-enforcement/non-gazetting, and political interference undermining EHO "
                   "prosecutions, alongside real tracked outcome data (national sanitation-access trend "
                   "1990-2017, Table 1; GAMA World Bank project's 21,091 household toilets completed by "
                   "district, Table 2). Legal Institutional Evidence Appraisal Framework applies. "
                   "record_id R7E87780D0891."),
    },
}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    found = {rid: False for rid in DECISIONS}
    for row in rows:
        rid = row["record_id"]
        if rid in DECISIONS:
            spec = DECISIONS[rid]
            assert row["full_text_decision"] in ("", None), f"{rid} already decided: {row['full_text_decision']}"
            row["full_text_decision"] = spec["decision"]
            row["final_decision"] = spec["decision"]
            row["full_text_status"] = "retrieved"
            row["reviewer_1"] = REVIEWER
            if spec["decision"] == "include":
                row["notes"] = spec["notes"]
            else:
                row["exclusion_reason"] = spec["exclusion_reason"]
                row["exclusion_reason_detail"] = spec["exclusion_reason_detail"]
                row["notes"] = spec["exclusion_reason_detail"]
            found[rid] = True

    missing = [rid for rid, ok in found.items() if not ok]
    assert not missing, f"Records not found in DB: {missing}"

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    with open(EXCL, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        excl_fieldnames = reader.fieldnames
        excl_rows = list(reader)

    for rid, spec in DECISIONS.items():
        if spec["decision"] == "exclude":
            db_row = next(r for r in rows if r["record_id"] == rid)
            excl_rows.append({
                "record_id": rid,
                "title": db_row["title"],
                "authors": db_row["authors"],
                "year": db_row.get("year", ""),
                "stage": "full_text",
                "exclusion_code": spec["exclusion_reason"],
                "exclusion_reason_detail": spec["exclusion_reason_detail"],
                "reviewer": REVIEWER,
                "date": "2026-09-22",
            })

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCL) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=excl_fieldnames)
        writer.writeheader()
        writer.writerows(excl_rows)
    os.replace(tmppath, EXCL)

    print("Batch 97 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})

if __name__ == "__main__":
    main()
