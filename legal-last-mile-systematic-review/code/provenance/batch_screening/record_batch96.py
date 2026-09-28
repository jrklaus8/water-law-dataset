#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "R7A9FA4B1B749": {
        "decision": "include",
        "notes": ("Ko 2024, J. Korea Water Resources Assoc. Tobit regression of Coulter "
                   "inequity coefficients for 6 water-supply variables across 152 South Korean "
                   "local governments, 3 years (2010/2016/2021), against political/administrative/"
                   "financial determinants. Directly examines institutional/administrative/financial "
                   "governance determinants of water-service equity; empirical, population/exposure/"
                   "outcome identifiable; record_id R7A9FA4B1B749."),
    },
    "RB0165DA1B47D": {
        "decision": "include",
        "notes": ("Linn, Robbins-Panko, Perry & Seibel 2023, Human Organization. Ethnographic "
                   "fieldwork 2016-2018, 46 older-adult Flint MI participants. Documents Emergency "
                   "Manager law, state water-safety declarations, and court-ordered lead pipe "
                   "replacement deadline as legal/institutional mechanisms shaping household water "
                   "insecurity. record_id RB0165DA1B47D."),
    },
    "RF563E44C5B3E": {
        "decision": "include",
        "notes": ("Mokoena 2023, Human Organization. Qualitative fieldwork, Khayelitsha township "
                   "Cape Town, 10 households + 3 officials. Documents South African Constitution "
                   "water-right, Free Basic Water policy, Mazibuko v. Johannesburg litigation, Water "
                   "Management Devices, and formal/informal settlement classification as legal/"
                   "institutional determinants of service access during Day Zero crisis. "
                   "record_id RF563E44C5B3E."),
    },
    "R238F15C4814B": {
        "decision": "include",
        "notes": ("Kashem, Tahsin, Subah, Murshed, Nowreen & Mondal 2023, GeoJournal. Mixed-methods "
                   "study of 3 Dhaka slums (150-household survey + 9 FGDs/12 IDIs/3 KIIs). Examines "
                   "Bangladesh National Water Policy, Water Act 2013, Water Rules 2018, and DWASA "
                   "land-title/building-plan connection requirement as legal/institutional barriers; "
                   "eviction/tenure insecurity linked to loss of legal water connection; reports "
                   "water security index and price/affordability outcomes by legal-connection status. "
                   "record_id R238F15C4814B."),
    },
    "R6022ED0189EC": {
        "decision": "include",
        "notes": ("Kouassi, Andrianisa, Traoré, Sossou, Nguematio & Djambou 2023, Environ. Sci. "
                   "Pollut. Res. Qualitative content-analysis study (257 interviewees, household "
                   "surveys, FGDs) of CLTS sanitation-program abandonment in Central-Western Burkina "
                   "Faso. Governance/institutional factors (subsidy-policy ambiguity, lack of "
                   "inter-agency coordination, agent transfers, absence of implementation-guide "
                   "enforcement) account for 26.28% of abandonment cases; reports sanitation-access "
                   "(ODF-status) outcome by responsibility category. record_id R6022ED0189EC."),
    },
    "R8D6F4AD1EAA6": {
        "decision": "include",
        "notes": ("Aluko, Oloruntoba, Ana, Afolabi & Okon 2023, Environ. Monit. Assess. "
                   "Population-based cross-sectional study, 548 households, Osun State Nigeria. "
                   "Explicitly tests whether EU/AfDB-funded WASH institutional and governance "
                   "reforms affected household water security (conclusion: reforms did not "
                   "significantly change water security status); binary logistic regression "
                   "identifies age, wealth and improved-toilet-facility as significant predictors "
                   "of water security. record_id R8D6F4AD1EAA6."),
    },
    "RADF284366C3F": {
        "decision": "exclude",
        "exclusion_reason": "E06",
        "exclusion_reason_detail": (
            "Hamdan, Libanio & Costa 2023, Environ. Sci. Pollut. Res. Methodological/engineering "
            "paper proposing and validating a Regulatory Index of Quality of Water Supply Service "
            "(RIQS) for triaging on-site regulatory inspections across 591 Minas Gerais, Brazil "
            "municipalities. Unit of analysis is the municipality/utility, not a household or "
            "population; no exposure-outcome test of a legal/institutional factor's effect on "
            "population-level water access -- outcome is an AHP-weighted engineering/operational "
            "index score used for inspection prioritization. No population/exposure/access-outcome "
            "framework meeting core inclusion criteria 2/4/5."
        ),
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

    # append excludes to exclusion_log.csv
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

    print("Batch 96 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})

if __name__ == "__main__":
    main()
