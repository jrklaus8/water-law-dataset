#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R033442B63D00": "Salazar Adams, Haro Velarde & Loera Burnes (Gestion y Politica Publica / similar), 'Capacidad institucional de los organismos de agua de Saltillo y Hermosillo, Mexico.' Comparative institutional-capacity case study (2001-2015) of two Mexican municipal water utilities, analyzing political, administrative, and human-resource-management factors and correlating them with performance outcomes (management autonomy, metering coverage, tariff indexation, staff training). Finds Saltillo's greater institutional capacity produced better service-delivery results than Hermosillo's. A genuine comparative institutional-mechanism case study of water-utility governance affecting service performance.",
    "R01210FAAED72": "Martinez-Fernandez, Neto, Hernandez-Mora, Del Moral & La Roca 2020 (Water Alternatives), 'The role of the Water Framework Directive in the controversial transition of water policy paradigms in Spain and Portugal.' Institutional/regulatory-reform case study of the EU Water Framework Directive's role in shifting Iberian water governance from a dominant 'hydraulic paradigm' toward a new water-governance approach. A genuine institutional/legal-mechanism analysis of EU-level regulatory reform's effect on national water-governance paradigms.",
    "R1C1A13D65727": "World Bank & Inter-American Development Bank 2018, 'Transforming Karachi into a Livable and Competitive Megacity: A City Diagnostic and Transformation Strategy' (Directions in Development). Comprehensive city diagnostic documenting Karachi's severe institutional/legal fragmentation across water/sanitation governance (~20 federal/provincial/local agencies with separate legal and administrative frameworks, minimal coordination), the Karachi Water & Sewerage Board's specific legal framework (KWSB Act 1996), and the formal/informal-settlement status of over 50% of the population (informal katchi abadis) as a structural determinant of water/sanitation service access, with detailed institutional history and service-coverage data (1.13 million domestic connections against a substantial unmet demand). A genuine, detailed institutional/legal-mechanism case study of water/sanitation access.",
}

EXCLUDES = {
    "RC0F997C39416": ("E03", "European Environment Agency & WHO Regional Office for Europe, 'Water and health in Europe: A joint report.' A broad technical/environmental-health report on water pollution sources (agricultural, industrial), drinking-water quality standards, waterborne disease, and transboundary water-quality agreements across Europe. A water-quality/public-health report, not a study of legal/administrative water-SERVICE-access-eligibility mechanisms; extends the established water-quality-vs-water-access exclusion criterion (INCLUSION_EXCLUSION.md exclusion 3)."),
}

WRONG_FILE = {
    "R0EF03089DEC3": "Target per database record: 'Ecological Sanitation in the U.S.: Barriers and Opportunities in Water...' Delivered PDF content is an entirely different document: Sichone & Mwalimu 2006, 'Gender Disparity in Water Sanitation and Hygiene Education Strategies Among Primary School Girls in Dar-es-Salaam Slums, Tanzania' -- different author, year, country, and topic; also an abstract-only publication from an apparent predatory-journal source (PARJ, 'request full paper' notice). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R0E7A7452FD2B": "Target per database record: 'Mapping Cholera Vulnerability in Delhi: An Ecosocial Perspective.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Bahmad, Ghssein, Bahmad et al., 'Paleopathology Meets Public Health: Deep-Time Syndemics and the Ecology of Emerging Infections' -- a medical-anthropology review with no relation to Delhi or cholera vulnerability. Content-behind-filename mismatch (same failure mode identified in Batch 234), verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R0999DC7092C9": "Target per database record: 'Water and bureaucracy in colonial Puebla de los Angeles.' Delivered PDF content is an entirely different document: Kuswati, Kusmayadi & Hartati 2023, 'The Role of Bureaucracy on the Effectiveness of Public Services' (International Journal of Social Science and Human Research, Indonesia) -- different author, year, country, and specific study (general Indonesian bureaucracy essay, not colonial Puebla water history). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R08432C1433E1": "Target per database record: 'El derecho humano al agua: una deuda del estado con la poblacion panamena...' Delivered PDF content is an entirely different document: Rodriguez Garcia 2024, 'Agua, justicia y migracion en Mexico: una reflexion desde el derecho humano al agua' -- different author, year, and country (Mexico vs. Panama); this is the identical wrong content already flagged for record R13BB56FEF2D1 in Batch 234, now confirmed delivered a second time under a different record_id. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R0142AEB4AB16": "Target per database record: 'Os Problemas Ambientais em Cabo Verde: Politicas e Medidas de Proteccao...' Delivered PDF content is an entirely different document: Lipu & Monzilar 2025, 'Aldeias Indigenas e a Problematica Ambiental: Estudo dos Impactos do Desmatamento das Matas Ciliares na Aldeia Limao Verde - Aquidauana/MS' (Brazil, indigenous-village riparian-forest deforestation) -- different author, year, and country (Brazil vs. Cabo Verde). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R7C6EB2B41FD4": "Target per database record: 'Meeting the Water Reform Challenge.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: WHO Regional Office for South-East Asia 2004, 'HIV/AIDS: meeting the challenge' -- a public-health report on HIV/AIDS in South-East Asia with no relation to water reform. Content-behind-filename mismatch (same failure mode identified in Batch 234), verified by full-text review. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 10
    decided, _ = process_db()
    assert len(decided) == 4
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 235 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
