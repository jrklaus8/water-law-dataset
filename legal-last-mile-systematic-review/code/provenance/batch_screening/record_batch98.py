#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCL = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

DECISIONS = {
    "R59468F0C4D5B": {
        "decision": "include",
        "notes": ("Meredith, MacDonald, Kwach, Waikuru & Alabaster 2021, book chapter in Land Issues "
                   "for Urban Governance in Sub-Saharan Africa (Springer). Case study of the Kenya Slum "
                   "Upgrading Program (KENSUP) Soweto East Project in Kibera, Nairobi, documenting the "
                   "Settlement Executive Committee (SEC) as a formal institutional arrangement for "
                   "community water/sanitation infrastructure delivery (K-WATSAN project). Field survey "
                   "(N=407 known-age respondents) found sanitation among the top-ranked community "
                   "concerns; the SEC's institutional formalization is linked to a concrete access outcome "
                   "(822 families gained formal housing/property ownership plus water and sanitation "
                   "infrastructure). record_id R59468F0C4D5B."),
    },
    "RF8C06439B2CA": {
        "decision": "include",
        "notes": ("Zhou & Liang 2021, J. Environmental Policy & Planning. Panel fixed-effects regression "
                   "(290 Chinese prefectural cities, 2008-2014) testing China's household registration "
                   "system (hukou) -- a legal/administrative status determining permanent vs. temporary "
                   "urban residency -- against per-capita wastewater and solid-waste treatment "
                   "infrastructure provision. Cities with a higher percentage of hukou-unregistered "
                   "temporary residents have significantly lower wastewater and solid-waste treatment "
                   "capacity (p<0.01), controlling for city and year fixed effects; also added to "
                   "effect_sizes.csv as a Family C candidate (legal/administrative exclusion mechanism "
                   "and access-relevant infrastructure-provision inequality). record_id RF8C06439B2CA."),
    },
    "R4A2516BE7A0A": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Biswas, Arya, Fernandes & Shah 2020, Information, Communication & Society. Mobile-app "
            "design/usability-evaluation study ('Find A Loo') tested with 33 evaluators using System "
            "Usability Scale and Potential Capability Scale Likert-scale surveys. The outcome measured is "
            "app usability/capability score (SUS/PCS), not a household or population-level sanitation "
            "access, connection, coverage, affordability, or reliability outcome; the paper's contribution "
            "is a technology-design/methodology paper, not an empirical study of a legal/institutional "
            "access mechanism. Same rationale as prior methodological-tool exclusions (Post/Agnihotri/Hyun "
            "crowd-sourced-data methodology; Porse et al. GIS-modeling methodology)."
        ),
    },
    "RF92EF484E8E6": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Jeil & Abass 2021, Local Environment. Mixed-methods cross-sectional study (86 household "
            "interviews, Northern Ghana) examining household water CHOICE determinants (accessibility, "
            "taste, traditional beliefs about rainwater, burial-site proximity) and hygiene practices from "
            "a risk-perception-theory lens. No legal/administrative/institutional/regulatory/governance "
            "factor is examined as an exposure in the empirical analysis; the paper's core findings concern "
            "individual risk perception and socio-cultural/traditional belief systems shaping water-source "
            "choice, not a legal-institutional access mechanism. Policy/enforcement recommendations appear "
            "only in the discussion/conclusion as forward-looking suggestions, not as something tested."
        ),
    },
    "R7D6CA19199B3": {
        "decision": "include",
        "notes": ("Romano, Nelson-Nuñez & LaVanchy 2021, Water International. Comparative documentary/"
                   "policy review of community-based water management (CBWM) legal frameworks across "
                   "Nicaragua (2010 Special CAPS Law/Law 722), Honduras (2003 General Framework Law for "
                   "Water and Sanitation/JAAs), and Costa Rica (1939 Law of Associations/ASADAS), "
                   "documenting how legal recognition/registration status determines rural water "
                   "committees' access to funding, technical support, and institutional standing, with "
                   "reported registration rates (e.g. 30% of Nicaraguan CAPS registered within 5 years of "
                   "Law 722) and persistent institutional-fragmentation/under-resourcing outcomes. Legal "
                   "Institutional Evidence Appraisal Framework applies. record_id R7D6CA19199B3."),
    },
    "R7F86482382FC": {
        "decision": "include",
        "notes": ("Basu, DasGupta, Hashimoto & Hoshino 2020, Environment, Development and Sustainability. "
                   "Multi-actor qualitative study (282 community FGD participants + 33 Gram Panchayat "
                   "heads + Block officials, Purulia district, West Bengal, India) examining India's "
                   "decentralized rural-water-governance institutional framework (Panchayati Raj three-tier "
                   "system, National Rural Drinking Water Programme). Documents governance-mediated "
                   "inequity in water-point access (e.g. a village where lower-caste households are barred "
                   "from a handpump located in an upper-caste area) and funding-allocation discretion "
                   "favoring new-construction over maintenance, linked to hand-pump functionality/water-"
                   "point access outcomes across 16 villages. record_id R7F86482382FC."),
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

    print("Batch 98 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})

if __name__ == "__main__":
    main()
