#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-28"
DATE = "2026-09-28"

INCLUDES = {}
EXCLUDES = {}

WRONG_FILE = {
    "R09FC86C2B2A1": "Target: Garcia-Rubio, Gonzalez-Gomez & Guardiola 2009, 'Performance and ownership in the governance of urban water.' Delivered: Allaire & Ignacio 2026, 'Do water board elections matter for utility performance?' -- different authors/year/topic.",
    "R0AD017809DBB": "Target: Mamokhere & Kgobe 2023, District Development Model, South Africa. Delivered: Nunbogu, Harter & Mosler 2019, latrine completion/use factors, Northern Ghana -- different authors/year/country.",
    "R13199AD17D84": "Target: Galindo & Palerm 2016, rural drinking water systems, Mexico. Delivered: Hanjabam 2018, 24x7 water supply case study, Manipur, India -- different author/year/country.",
    "R127DF8827EFF": "Target: de Cisneros de Britto 2010, water policy in Spain. Delivered: Araujo, Gold, Lau, Reed & Alves, water-supply-investment-pathway equity study, Federal District of Brazil -- different authors/country.",
    "R102FC970D831": "Target: Thompson & Nleya 2008, MDGs and water service delivery. Delivered: Mdee et al. 2025, citywide-inclusive-sanitation political economy, container-based sanitation -- different authors/year/topic.",
    "R10CA5829EDAB": "Target: Ries 2016, sustainability at US urban water utilities. Delivered: MacArthur, Basnet et al. 2025, gender-equality/WASH interventions, rural Nepal -- different authors/year/country.",
    "R189CE1C67FCB": "Target: Krishnamurthy 1977, 'The Challenge of Africa's Water Development.' Delivered: book chapters from 'Environmental Justice in Nepal' (Sherpa, Awale) -- unrelated Nepal climate-justice content.",
    "R144A499B49EF": "Target: Sainz Santamaria 2014, 'Elections, protests, and the provision of public goods.' Delivered: a Canadian law-firm client reporting letter about an Ontario corporate share reorganization -- not a research paper at all.",
    "R174328BEEE2D": "Target: Lenka, Chanchal & Sheemar 2026, urban India water-supply-policy review. Delivered: Zaunda, Holm, Itimu-Phiri, Malota & White 2018, disability-friendly WASH facilities in primary schools, Rumphi, Malawi -- different authors/year/country.",
    "R168B474EA513": "Target: Olivieri, Koop, Van Leeuwen & Hofman 2022, governance capacity for water supply, Windhoek, Namibia. Delivered: Atigaku et al. 2026, community governance and drinking-water access, semi-urban Togo -- different authors/country.",
    "R1646F0221608": "Target: Mogues, Cohen, Birner et al. 2009, rural water supply governance, Ethiopia. Delivered: DuChanois et al. 2019, a short journal Correction notice to an unrelated multi-country water-continuity paper -- not even a full paper, and not the target.",
    "R21CEABEE31CB": "Target: Parker, Kirkpatrick & Figueira-Theodorakopoulou 2005, infrastructure regulation and poverty reduction. Delivered: Adeoti 2023, systematic review of water-infrastructure sustainability challenges, Nigeria -- different author/year/scope.",
    "R3574A06B83AA": "Target: Velasco, Diokno-Sicat, Castillo & Maddawin 2018, Philippine local water sector institutional issues. Delivered: Whaley & Cleaver 2017, community-management-model functionality, Sub-Saharan Africa -- different authors/region.",
    "R33F51CB30C14": "Target: Bywater 2010, 'Water for life, not for profit... India.' Delivered: van Welie & Romijn 2018, NGOs fostering sustainable urban sanitation transitions, low-income countries -- different authors/year/scope.",
    "R3C453AC209FD": "Target: Carrera 2015, 'Sanitation and social power in the United States.' Delivered: Chidambaram 2020, institutions/infrastructure and collective-action mobilization around public toilets/piped water, Delhi slums, India -- different author/year/country; confirmed NOT Carrera's paper resurfacing (a second, independent wrong delivery for this target, distinct from the wrong content already delivered for a different record_id, RCF2C8A8C45DD, in Batch 238).",
    "R2A9751DFEE49": "Target: Stopnitzky 2012, 'Household Sanitation, Social Norms, and Public Policy in India.' Delivered: Shah & Badiger 2020, institutional-economics analysis of water-scarcity narratives, Darjeeling, India -- different author/year/specific topic (water scarcity vs. sanitation/social norms); confirmed NOT Stopnitzky's paper resurfacing (a second, independent wrong delivery for this target, distinct from the wrong content already delivered for a different record_id, RBFC70108EBEE, in Batch 238).",
    "R24C96DE6980C": "Target: Brooks 2002, 'Water; Local-Level Management.' Delivered: Komakech, Kwezi & Ali 2020, prepaid water technologies and inclusive rural water services, Tanzania -- different authors/year/country.",
    "R2281812753A2": "Target: Tietz 2008, 'Functions and Spatial Structures of Local Utility Systems.' Delivered: Dobbin & Fencl, institutional diversity and safe drinking-water provision, United States (California water-system governance types) -- different authors/scope.",
    "R22B644A91DD0": "Target: Brown 2013, 'Can Participation Change the Geography of Water? ... South Africa.' Delivered: Bruns, Meisch, Ahmed, Meissner & Romero-Lankao, water-energy-food nexus/infrastructure perspective, Sub-Saharan Africa -- different authors/scope.",
    "R1316230566E0": "Target: Nicholas 2018, governance and service delivery, Makana Local Municipality. Delivered: Pugel, Javernick-Will et al. 2022, collaborative water/sanitation-system-strengthening case comparison, Kenya/Ethiopia/Uganda -- different authors/countries.",
    "R3EC82F2544AC": "Target: Galvao Junior, Nishio, Bouvier & Turolla 2009, state regulatory frameworks for basic sanitation, Brazil. Delivered: Calderon-Villarreal et al., environmental structural violence/water contamination among deportees, US-Mexico border (Tijuana River) -- different authors/country/topic.",
    "R139D522CD1BC": "Target: Pacheco-Vega 2015, 'Bottled Water in Mexico.' Delivered: Igbinedion's book review of Thompson's 'Liquid Asset' (Stanford University Press, 2023), published in Hungarian Geographical Bulletin 2025 -- a book review, not the target research paper.",
    "R25CA44C49907": "Target: Arbues, Garcia-Valinas & Martinez-Espineira 2003, residential water-demand estimation review. Delivered: an Ontario Superior Court of Justice decision, Taheripouresfahani v. Dormer Bond Inc., 2025 ONSC 5833, a real-estate breach-of-contract dispute -- not a research paper at all.",
}


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def process_db():
    with open(PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    decided = []

    for row in rows:
        rid = row["record_id"]
        if rid in INCLUDES:
            detail = INCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "include"
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "include"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in EXCLUDES:
            code, detail = EXCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "exclude"
            row["exclusion_reason"] = code
            row["exclusion_reason_detail"] = detail
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "exclude"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in WRONG_FILE:
            detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["reviewer_1"] = REVIEWER
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail

    atomic_write(PATH, fieldnames, rows)
    return decided, fieldnames


def append_exclusion_log(decided):
    with open(EXCLOG_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in decided:
        if row["final_decision"] != "exclude":
            continue
        rows.append({
            "record_id": row["record_id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": row["exclusion_reason"],
            "exclusion_reason_detail": row["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(EXCLOG_PATH, fieldnames, rows)


if __name__ == "__main__":
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 23, len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE)
    decided, _ = process_db()
    assert len(decided) == 0
    append_exclusion_log(decided)
    print(f"Batch 239 processed: 0 includes, 0 excludes, {len(WRONG_FILE)} wrong_file_retrieved (full wash).")
