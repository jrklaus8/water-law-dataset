#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "R2D5B15E9481A": {
        "decision": "include",
        "notes": (
            "Adams, Sambu & Smiley 2019, 'Urban water supply in Sub-Saharan Africa: "
            "historical and emerging policies and institutional arrangements' "
            "(International Journal of Water Resources Development). A comprehensive "
            "documentary/narrative synthesis of historical (International Hydrological "
            "Decade, Water Decade, MDGs) and emerging institutional arrangements "
            "(delegated management models, community-public partnerships, community "
            "self-help initiatives) for urban water supply across Sub-Saharan Africa, "
            "with extensive real tracked outcome data drawn from underlying primary "
            "studies: city-specific household piped-connection rates (4% Greater Accra, "
            "9% Lilongwe, 23% Ouagadougou, 29% Dar es Salaam, 61% Nairobi/Mombasa/"
            "Kakamega), delegated management model (DMM) outcomes in Kisumu, Kenya "
            "(expanded network, reduced tariffs, reduced non-revenue water), and "
            "community-public partnership outcomes in Malawi (improved technical/"
            "financial management, stabilized pricing) documented against specific "
            "institutional mechanisms (utility-community contracts, water user "
            "association governance). Included via the Legal Institutional Evidence "
            "Appraisal Framework, consistent with the Mariwah, Sullivan Lemaitre & "
            "Stoler, and Romano et al. precedent for narrative/documentary reviews with "
            "genuine institutional analysis and real tracked outcome data (not merely "
            "discussion-section policy recommendations). Not effect_sizes eligible: "
            "narrative synthesis of multiple studies, no single regression-based "
            "exposure-comparator effect estimate."
        ),
    },
    "RC0A48E1C4D35": {
        "decision": "exclude",
        "exclusion_reason": "E03",
        "exclusion_reason_detail": (
            "Thoradeniya, Pinto & Maheshwari 2019, 'Perspectives on impacts of water "
            "quality on agriculture and community well-being -- a key informant study "
            "from Sri Lanka' (Environmental Science and Pollution Research). A "
            "35-key-informant qualitative study examining perceptions of how water "
            "QUALITY degradation (groundwater hardness, fluoride, agro-chemical "
            "contamination linked to chronic kidney disease of unknown aetiology) "
            "affects agriculture and community well-being in Sri Lanka's dry zone. "
            "While the paper briefly references governance gaps (absence of irrigation-"
            "water-quality standards, uneven distribution from a government irrigation "
            "scheme), its core exposure and outcome are environmental "
            "contamination/water-quality effects on crop yields and health, not a "
            "legal/administrative water/sanitation ACCESS mechanism. Wrong exposure/"
            "water-quality-only per E03."
        ),
    },
    "R1B918BF54680": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Hailu, Tolossa & Alemu 2019, 'Water security: stakeholders' arena in the "
            "Awash River Basin of Ethiopia' (Sustainable Water Resources Management). "
            "A basin-level multi-stakeholder institutional-coordination study (29 key "
            "informant interviews, 16 focus group discussions) examining water "
            "RESOURCES governance across competing uses -- irrigation, industry, "
            "hydropower, pastoralism, ecosystem services, and domestic water supply -- "
            "in the Awash River Basin. The unit of analysis and empirical focus is "
            "basin-level stakeholder coordination/institutional fragmentation across "
            "all water uses collectively, not a specific legal/administrative mechanism "
            "tested against household-level water/sanitation service-access outcomes. "
            "Wrong topic/unit of analysis per E01, the same macro water-resources-"
            "governance rationale as the Wang Shenzhen exclusion."
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

    print("Batch 104 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
