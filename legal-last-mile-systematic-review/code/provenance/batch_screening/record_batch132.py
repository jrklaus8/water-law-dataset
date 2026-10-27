#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "RDE671123A010": "Political-ecology study of decentralized local institutions in Mali, "
        "documenting how administrative-territory legal codification under successive governments "
        "(the size/reach of officially recognized administrative units) drives real village-level "
        "disparities in access to improved drinking water sources, via archival sources, "
        "20th-century census data, a 44-municipality field survey, cartographic geospatial analysis, "
        "and a regression model showing administrative reach is a significant predictor "
        "(R2 0.53->0.63, p<0.05) of hamlet proliferation excluded from officially funded water "
        "infrastructure. Extracted for record_id RDE671123A010.",
    "R3520D2BF6FB3": "Documentary/historical institutional case study of post-apartheid Durban water "
        "and sanitation policy, documenting the Free Basic Water policy (6 to 9 kl/household/month), "
        "real disconnection statistics (1,000/day; 40,000 more disconnected than connected in "
        "2002-2003), a real litigated disconnection case (Manquele v. eThekwini), means-testing "
        "indigence policy, and household-level water-price-elasticity data by wealth band tied to "
        "real consumption outcomes. Extracted for record_id R3520D2BF6FB3.",
    "R8645861E4624": "Qualitative institutional case study of water-supply-solution narratives "
        "(formalization, enhanced informality, green infrastructure) in two informal settlements in "
        "Xochimilco, Mexico City, documenting Mexico City's 2017 Sustainable Water Law (prohibiting "
        "public-service provision to informal settlers in the Conservation Zone) as a real legal "
        "barrier, via 27 key-informant interviews and a 41-resident questionnaire tied to real "
        "household-level water-access coping-strategy and cost outcomes. Extracted for record_id "
        "R8645861E4624.",
    "R59B2D594C94F": "Political-ecology case study of rural water-supply-network expansion (Indira "
        "Gandhi Canal) in Rajasthan, India, documenting intervillage and intragender/caste "
        "differentiation in water access via a real 180-household survey with caste-disaggregated "
        "data (General/OBC/SC/ST/Muslim), interviews with water users and government engineers, and "
        "participant observation, tied to real household-level water-collection-time and access "
        "outcomes. Extracted for record_id R59B2D594C94F.",
    "RF456013643C2": "Ethnographic/historical institutional case study of household water-rights "
        "evolution in a rural Northern Ghana village (1965-2012), documenting Ghana's real statutory "
        "legal framework (1992 constitution Article 257/6, Water Resources Commission Act 522/1996) "
        "in dissonance with customary/project water rights, via primary ethnographic and archival "
        "data (2004-2006 survey of all water user groups/communities in an 8,000-inhabitant village) "
        "tied to real household-level water-access outcomes across four historical periods. "
        "Extracted for record_id RF456013643C2.",
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

for rid in INCLUDES:
    assert rid in by_id, f"record_id {rid} not found"
    r = by_id[rid]
    assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

for rid, note in INCLUDES.items():
    r = by_id[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = note

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"Batch 132 recorded: {len(INCLUDES)} includes, 0 excludes.")
