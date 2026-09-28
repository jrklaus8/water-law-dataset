#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {}
EXCLUDES = {}

WRONG_FILE = {
    "R1D096BB71916": "Target per database record: Dobbin, Mcbride & Pierce 2023, 'Panacea or Placebo? The Diverse Pathways and Implications of Drinking Water System Consolidation.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is an entirely different document: Song 2026, 'Mitochondrial ecosystem restoration in Alzheimer's disease: from mechanisms to multi-target therapeutic strategies' (Frontiers in Cell and Developmental Biology) -- a neuroscience paper with no relation whatsoever to water systems. This is a content-behind-filename mismatch (the Drive file's displayed title/filename is correct, but the actual file content stored at that fileId is wrong), verified by direct full-text review, not merely a title check. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R19D28505FC8A": "Target per database record: Hegazi 2019, 'Authoritarian Governance and the Provision of Public Goods: Water and Wastewater Services in Egypt.' Delivered PDF content is an entirely different document: Uwimana 2025, 'Umuganda and Communal Governance: Assessing Social Cohesion and Public Goods Provision in Kigali's Nyarugenge District' (Rwanda) -- different author, year, country, and specific topic; also an abstract-only publication from a predatory-journal pattern (PARJ, 'request full paper' notice) rather than a complete article. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R198209A1D839": "Target per database record: McKinney, Weiner & Vigil 2023, 'First in Time: The Place of Tribes in Governing the Colorado River System.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Wall, Compton, Coble et al., 'Post-wildfire water quality and aquatic ecosystem response in the U.S. Pacific Northwest: science and monitoring gaps' (Environmental Research: Water, 2026) -- different authors and different specific topic (post-wildfire water-quality monitoring gaps, not tribal water-rights governance of the Colorado River). Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R189CB69DDE8B": "Target per database record: Diaz Valdivia, Cordova Quenta & Munoz Flores 2019, 'Propuesta de mejora de la administracion del servicio publico de agua potable en el Distrito de Yanaquihua' (Peru). Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Huaraca Aparco, Delgado Laime, Tapia Tadeo & Agreda Cerna 2021, 'Sostenibilidad del servicio de agua potable y disposicion del cliente a pagarla' (Revista Venezolana de Gerencia) -- different authors, different year, different specific study location (Andahuaylas vs. Yanaquihua, Peru), different journal. Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R155835EF1B8F": "Target per database record: Kemp 2020, 'Variables Influencing Service Delivery in Protea Glen, Johannesburg.' Delivered PDF content is an entirely different document: Hassan, El-Sayed, Mousa & Shaarawi, 'Big Data Analytics in Urban Planning and Service Delivery in Cairo, Egypt: An African Perspective' -- different author, year, and country (Cairo vs. Johannesburg); also an abstract-only publication from the same predatory-journal pattern (PARJ). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R16D87BB47C02": "Target per database record: Ross 2010, 'A virtuous cycle: Tracing democratic quality though equality.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Marion, Storhaug, Lee et al. 2026, 'The Effects of Land Management Policies on the Environment and People in Low- and Middle-Income Countries: A Systematic Review' (Campbell Systematic Reviews) -- different authors, year, and topic entirely. Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R14569CA54EA8": "Target per database record: Onda & Tewari 2021, 'Water systems in California: Ownership, geography, and affordability.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Tilahun, Tassaw, Zhou et al. 2026, 'Acceptability of insecticide treated nets in an urban setting in a malarious area' (PLOS Global Public Health, Ethiopia) -- a malaria-prevention study with no relation to water systems. Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R13BB56FEF2D1": "Target per database record: Garcia & Ituarte 2020, 'El derecho humano al agua en Espana en el contexto europeo (2010-2020)' (Spain, human right to water). Delivered PDF content is an entirely different document: Rodriguez Garcia 2024, 'Agua, justicia y migracion en Mexico: una reflexion desde el derecho humano al agua' -- different author, year, and country (Mexico vs. Spain). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R131D44D2032B": "Target per database record: Taye, Getachew, Gizaw & Kaba 2020, 'Vulnerability to housing and the environment in urban settings: Implications for residents and places.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Arowolo, Oguntokun & Ayodele 2026, 'Trend Analysis of Residential Properties Rental Values in Informal Settlements of Ibadan Metropolis' (Nigeria) -- different authors, year, and specific study (rental-value trend analysis, not housing/environment vulnerability). Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R1261BA60DC49": "Target per database record: Sebake 2025, 'The Collapse of Developmental Local Government in South Africa with reference to Service Delivery, Corruption and Financial Lapses.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Alanazi, Alanazi & Benlaria 2025, 'Balancing costs and care: a healthcare cost analysis for families of children with Down syndrome in Saudi Arabia' (Frontiers in Public Health) -- a healthcare-economics paper with no relation to South African local government. Content-behind-filename mismatch, verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
        if rid in WRONG_FILE:
            detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["reviewer_1"] = REVIEWER
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail

    atomic_write(PATH, fieldnames, rows)
    return decided, fieldnames


if __name__ == "__main__":
    assert len(WRONG_FILE) == 10
    decided, _ = process_db()
    print(f"Batch 234 processed: 0 includes, 0 excludes, {len(WRONG_FILE)} wrong_file_retrieved (all 10 records this batch had content-behind-filename mismatches).")
