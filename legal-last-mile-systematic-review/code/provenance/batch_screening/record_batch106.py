#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

DECISIONS = {
    "RAFC08D21DB57": {
        "decision": "include",
        "notes": (
            "Robina Ramirez, De Clercq & Jackson 2019, 'Human Water Governance: A "
            "Social Innovation Model to Reduce the Inequalities of Water Services in "
            "South African Informal Settlements' (book chapter, New Paths of "
            "Entrepreneurship Development). A PLS-SEM survey of 124 randomly-selected "
            "informal dwellers in Kayamandi and Enkanini, Stellenbosch Municipality, "
            "South Africa, testing a 'Human Water Governance' model built from UNESCO "
            "Water Principles. The study documents genuine legal/institutional exposure "
            "variables: the Municipality's application-based water-service-connection "
            "requirement under its Credit Control and Debt Collection By-laws ('No "
            "person shall be provided with access to water services unless an "
            "application has been made to, and approved by, the Municipality'), the "
            "National Water Act (36 of 1998) and Water Services Act (1997) minimum "
            "free-basic-water entitlement (25 L/person/day), the legally-required "
            "community-participation process under the Municipal Systems Act/Municipal "
            "Structures Act, and Enkanini's contested illegal-settlement status (zoned "
            "for conservation, a 2006 court eviction order never enforced), against "
            "household-level outcomes: communal-tap vs. individual-yard-connection "
            "service type, water/sanitation service equality between Kayamandi and "
            "formal Stellenbosch neighbourhoods, and willingness/ability to pay for "
            "services. Reports quantitative PLS path-coefficient results (Principles of "
            "Water Governance -> Human Water Management, beta=0.265, t=3.523, "
            "p<0.001), though as a composite multi-item SEM construct model rather than "
            "a single well-defined legal-mechanism-vs-access-outcome regression. "
            "Extracted as S619. Not effect_sizes eligible: the exposure and outcome are "
            "each multi-item latent SEM constructs (Principles of Water Governance; "
            "Human Water Management), not a single identifiable legal/institutional "
            "exposure tested against a single identifiable access/outcome measure in "
            "the Family A/B/C sense."
        ),
    },
    "RE370E2BDE97A": {
        "decision": "exclude",
        "exclusion_reason": "E06",
        "exclusion_reason_detail": (
            "Sengupta, Misra, Chaudhary & Prakash 2019, 'Role of Technology in Success "
            "of Rural Sanitation Revolution in India' (ICEGOV2019 conference "
            "proceedings). A self-described 'experience paper' describing the ICT/"
            "e-Governance tools (web portal, mobile apps for geotagged toilet-"
            "construction verification, GIS dashboards, social media/WhatsApp outreach) "
            "used to implement India's Swachh Bharat Mission-Gramin rural sanitation "
            "programme. The paper's central topic and exposure is technology/engineering "
            "infrastructure supporting programme monitoring and citizen engagement, not "
            "a legal/administrative/regulatory access mechanism; it reports aggregate "
            "national programme statistics (94% coverage) without testing any "
            "legal/institutional exposure variable against household-level access "
            "outcomes. Engineering/technology-only exposure per E06, the same rationale "
            "as the Foster/McSorley/Willetts handpump-technology and Jimenez/"
            "Perez-Foguet GIS-mapping exclusions."
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

    print("Batch 106 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})


if __name__ == "__main__":
    main()
