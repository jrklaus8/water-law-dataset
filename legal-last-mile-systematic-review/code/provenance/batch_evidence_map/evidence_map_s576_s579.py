#!/usr/bin/env python3
"""Evidence map rows for the 4 includes in the eighty-second full-text screening batch (S576-S579)."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EM_FILE = os.path.join(BASE, "05_analysis/descriptive/evidence_map.csv")

ROWS = [
    {
        "study_id": "S576",
        "study_design_class": "qualitative",
        "evidence_level": (
            "Qualitative study (53 semi-structured interviews plus field observation and route "
            "mapping) of informal pit emptiers in Mukuru and Kibera informal settlements, Nairobi, "
            "Kenya. Documents institutional exclusion of pit emptiers from legal recognition under "
            "Kenya's Water Act 2016, cartel violence, NEMA enforcement threats, and a private "
            "transfer-station formalisation model; provisional confidence: moderate -- triangulated "
            "interviews across pit emptiers, residents, entrepreneurs, and officials, though evidence "
            "is descriptive rather than a measured exposure-comparator effect."
        ),
        "mechanism_family": "informal_sector_legal_exclusion",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water_act_2016_devolution",
        "institutional_context": (
            "Kenya's Water Act 2016 devolved sanitation provision to counties, but non-sewered "
            "sanitation and informal pit emptiers remain outside any licencing or legal-recognition "
            "framework; the study documents cartel-controlled disposal territories, NEMA-backed "
            "enforcement threats against pit emptiers, and Sanergy's private transfer-station model "
            "as a partial route to formalisation and workplace safety."
        ),
    },
    {
        "study_id": "S577",
        "study_design_class": "quantitative",
        "evidence_level": (
            "Quantitative study (household-level tariff/consumption microdata across 35 service areas "
            "and a binary logistic regression on household survey data) of water-tariff subsidy "
            "regressivity and affordability in the Federal District, Brazil. Documents demographic "
            "predictors of water-poverty risk (female household head OR=2.78; brown race OR=2.84; "
            "children OR=1.49) under Brazil's 2020 New Legal Framework for Basic Sanitation; "
            "provisional confidence: moderate-high -- genuine regression with reported ORs, CIs, and "
            "p-values, though predictors are demographic rather than a direct legal-mechanism exposure."
        ),
        "mechanism_family": "tariff_subsidy_design",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "law_14026_2020_basic_sanitation_framework",
        "institutional_context": (
            "Brazil's Law 14,026/2020 New Legal Framework for Basic Sanitation reoriented utility "
            "tariff policy toward economic/financial sustainability and private-sector participation "
            "rather than an explicit human-right-to-water framing; the study finds the increasing-"
            "block-tariff subsidy structure regressive (higher-income service areas capture a "
            "disproportionate share of subsidised water) and identifies household demographic "
            "characteristics significantly associated with water-poverty risk under this tariff regime."
        ),
    },
    {
        "study_id": "S578",
        "study_design_class": "mixed-methods",
        "evidence_level": (
            "Mixed-methods case study (90-respondent survey + 9 semi-structured interviews) of hybrid "
            "formal/informal water supply in Queimados, Rio de Janeiro Metropolitan Region, Brazil. "
            "Documents CEDAE's 30-year concession contract, centralised utility decision-making, "
            "clientelist-politics dynamics in spring/infrastructure siting, and complete institutional "
            "non-recognition of grassroots natural springs; provisional confidence: moderate -- "
            "triangulated survey (MCA, 75.69% variance explained) and interview data, though the "
            "legal/institutional analysis is largely descriptive."
        ),
        "mechanism_family": "concession_contract_institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "cedae_concession_contract",
        "institutional_context": (
            "Queimados municipality delegates water-service provision to CEDAE (State of Rio de "
            "Janeiro Water and Sewage Company) through a 30-year concession contract, centralising "
            "infrastructure and management decisions at the state level to the detriment of peripheral "
            "areas; grassroots natural-spring sources used by residents lacking network access receive "
            "no municipal, state, or CEDAE legal recognition or water-quality monitoring, and "
            "clientelist patronage (e.g., a mayoral candidate funding a spring's concrete structure) "
            "shapes what limited infrastructure does exist."
        ),
    },
    {
        "study_id": "S579",
        "study_design_class": "mixed-methods",
        "evidence_level": (
            "Mixed-methods comparative case study (household surveys n=95/96; semi-structured "
            "interviews n=90+90+19) of urban water insecurity across three Ethiopian cities (Akaki "
            "Kality, Harar, Wenji). Documents Ethiopia's WASH Implementation Framework, a nationally "
            "illegal informal water-vending sector serving as the de facto primary source for many "
            "households, a formal Addis Ababa rationing policy, and the 2013 tariff-setting guideline, "
            "with quantified cost-ratio findings (20x-76x formal-price multiples); provisional "
            "confidence: moderate-high -- large triangulated multi-site sample with quantified "
            "financial-burden comparisons, though analysis remains descriptive/correlational."
        ),
        "mechanism_family": "informal_vendor_illegality_tariff_rationing",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "wash_implementation_framework_tariff_guideline",
        "institutional_context": (
            "Ethiopia's WASH Implementation Framework/One WASH National Programme and the 2013 "
            "National Guideline for Urban Water Utilities Tariff Setting govern formal urban water "
            "provision, while the small-scale private/informal water-vending sector that fills the gap "
            "left by intermittent formal supply remains illegal nationwide; the study documents a "
            "formal city-wide rationing policy in Addis Ababa and quantifies the financial burden this "
            "illegality/intermittency imposes on households (informal water up to 20x, bottled water "
            "up to 76x the formal tariff)."
        ),
    },
]


def main():
    with open(EM_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {row["study_id"] for row in rows}
    for row in ROWS:
        assert row["study_id"] not in existing_ids, f"{row['study_id']} already exists"
        assert set(row.keys()) == set(fieldnames), f"field mismatch for {row['study_id']}"

    rows.extend(ROWS)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(EM_FILE), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, EM_FILE)

    print(f"done, evidence_map rows now {len(rows)}")


if __name__ == "__main__":
    main()
