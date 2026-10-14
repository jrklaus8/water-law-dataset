#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R0DF9468FC154": "Gopakumar 2012 (Routledge Contemporary South Asia Series), 'Transforming Urban Water Supplies in India: The role of reform and partnerships in globalization.' A book-length comparative institutional case study of water-supply reform politics in three Indian metropolitan cities (Bangalore, Chennai, Kochi), documenting the process of public-private-partnership-driven reform, state-society relations, and the roles of specific institutional actors (Bangalore Water Supply and Sewerage Board, Chennai Metrowater, Kerala Water Authority, slum-dweller federations, village water-supply committees) at state, city, and neighborhood levels. A genuine qualitative institutional-mechanism case study of water-supply governance reform affecting access.",
    "RD768BF81FBAA": "Breen & Gillanders 2024 (Governance), 'Money down the drain: Corruption and water service quality in Africa.' Rigorous probit-regression study (N=44,778, Afrobarometer round 7, country fixed effects, region-clustered standard errors) directly testing regional utilities-sector corruption's effect on the likelihood a household reports access to enough clean water. Finds a statistically significant negative marginal effect, robust to individual bribery experience and to an ordered-probit specification; effect holds specifically in areas with piped water systems. A rigorous regression-based institutional/administrative-barrier study directly isolating a corruption mechanism's effect on differential water access.",
    "R27F510DA4541": "Romero 2022 (Ingeniería y Competitividad), 'Private and public management of urban water supply and sanitation systems: From privatization to remunicipalisation.' A qualitative institutional/regulatory history documenting Colombia's water-service provision models over time -- concession contracts (Barranquilla 1880, Bogotá 1886, etc.), the creation and 1986 liquidation of the national municipal-development institute INSFOPAL, and subsequent decentralization reforms transferring water utilities to departments/municipalities. A genuine institutional/legal-history case study of the regulatory model governing water-service provision.",
}

EXCLUDES = {
    "R4FF1B9A43E90": ("E01", "Amis & Kumar 2000 (Environment and Urbanization), 'Urban Economic Growth, Infrastructure and Poverty in India: Lessons from Visakhapatnam.' A broad study of urban economic growth, infrastructure investment (water, power, roads), and participatory poverty research, including impact evaluation of a DFID-funded slum physical-infrastructure improvement project (water pipes, drains, latrines, roads). Infrastructure investment and poverty broadly, not a focused legal/administrative water-access-eligibility mechanism; extends the established broad-infrastructure/economic-development exclusion precedent (Okpala 1980, Batch 231)."),
    "R1C05E6CC38E3": ("E05", "Santana, Rocha, Santos, de Alcantara, Lisboa & Oliveira 2023 (Revista de Gestão Social e Ambiental), 'Unequal Territories and Water Access Policies in the Brazilian Northeast.' A theoretical geography paper applying territorial/power-relations theory (Foucault, Haesbaert, Raffestin, Saquet) to Brazil's federal Cisterns Program, using only secondary descriptive statistics (cistern counts by state) and general discussion of political patronage ('drought industry') without any comparator, eligibility-criteria analysis, or empirical test of a specific administrative-access mechanism's differential effect. A theoretical/documentary discussion, not a rigorous empirical mechanism study; extends the established no-empirical-evidence exclusion precedent."),
}

WRONG_FILE = {
    "R180DB01E1A79": "Target per database record: Araujo, Sanchez & Veiga 2011, 'The impact of a new regulatory framework upon water management in Spain. The company Aguas de La Coruna S.A. (1975-2008).' Delivered PDF content (verified via full-text review) is an entirely different document: Kodelashvili 2025, 'Challenges of Compliance Risk Management in the Georgian Banking Sector' (Norwegian Journal of development of the International Science) -- unrelated author, year, country, and topic (banking compliance risk, not water regulation). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R1F37F14B3722": "Target per database record: Beausejour 2009, 'Alternatives a l'assainissement centralise dans les pays en developpement: Le cas des zones periurbaines du Vietnam' (sanitation alternatives, peri-urban Vietnam). Delivered PDF content is an entirely different document: Ramde 2023, 'Qualite des institutions et croissance economique dans l'espace UEMOA' (institutional quality and economic growth in the West African Monetary Union) -- unrelated author, year, country, and topic (macroeconomic growth econometrics, not sanitation). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R1F2EDC030C66": "Target per database record: Anjum 2016, 'Decentralization and the Delivery of Basic Services in a Developing Country: Institutional Challenges of Providing Water and Sanitation to Urban Consumers in Addis Ababa, Ethiopia.' Delivered PDF content is an entirely different document: Shaikh et al. 2026, 'Governance reforms for Pakistan's National Institute of Health: Addressing challenges in disease surveillance and emergency management' (PLOS Global Public Health) -- unrelated author, year, country (Pakistan vs. Ethiopia), and topic (public-health disease-surveillance institute governance, not water/sanitation decentralization). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R1ECC532A797B": "Target per database record: Kumar 2013, 'Hydrological politics in megacity: rethinking water governance in Delhi.' Delivered PDF content is an entirely different document: Nalubega, Mugisha, Okello & Turyamureeba 2022, 'Hydrological Governance and Conflict Mitigation: A Survey of Community Perspectives on Nile Basin Water Scarcity in Uganda' -- unrelated author, year, city/country (Delhi vs. Nile Basin Uganda), and content. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R1D27DF36A4B5": "Target per database record: Syal 2025, 'Overregulated and Underserved: Regulatory overlap in infrastructure/service provision in Delhi's 'informal' settlements.' Delivered PDF content is an entirely different document: Mensah, Celestin, El Mansouri & Anderson 2013, 'The role of public-private partnerships in financing hospital infrastructure in Rwanda' -- unrelated author, year, country, and topic (hospital-infrastructure PPP financing, not regulatory overlap in Delhi informal settlements). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
    assert len(decided) == 5
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 233 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
