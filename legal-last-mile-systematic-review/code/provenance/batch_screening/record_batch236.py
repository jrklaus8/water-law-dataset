#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "RED01AD3DE1C0": "Beall, Crankshaw & Parnell 2000 (Journal of Southern African Studies), 'Victims, Villains and Fixers: The Urban Environment and Johannesburg's Poor.' Empirical case study of municipal governance (Greater Johannesburg Metropolitan Council) and historical racial/housing-type determinants of water, sanitation, and electricity access disparities in Johannesburg townships and informal settlements post-apartheid, including a pro-poor service-delivery/redistributive-strategy analysis. A genuine institutional/administrative-mechanism study of water/sanitation access inequality.",
    "RD5A2982CF41B": "Marra 2008 (Rural Society), 'Bearing the Cost: An Examination of the Gendered Impacts of Water Policy Reform in Malawi.' Empirical study of Malawi's water-policy reform (decentralization, privatization, user-pays, since the mid-1990s) and its gendered impacts on water access/affordability at the household level; documents how 'community'-framed policy design obscures gender-differentiated ability to pay user charges. A genuine institutional/legal-mechanism study of water-policy reform's effect on access.",
    "RD2B443A67F95": "Das & Takahashi 2014 (International Development Planning Review), 'Non-participation of low-income households in community-managed water supply projects in India.' Empirical household-survey study (three cities in central India) with binary logistic regression analyzing income/caste/socio-demographic determinants of household participation in a community-managed water-supply program; genuine empirical analysis of an administrative program-design mechanism (mandatory community participation/labor contribution) and household resource constraints as a barrier to program access. Dependent variable is participation/labor-contribution, not a direct water-access/connection outcome, so this does not produce an effect_sizes.csv-eligible row under the strict access-outcome requirement, but is a genuine qualitative/quantitative-adjacent institutional-mechanism study eligible for the qualitative synthesis.",
    "RCBBF97B6D984": "Marumahoko, Afolabi, Sadie & Nhede 2020 (Strategic Review for Southern Africa), 'Governance and Urban Service Delivery in Zimbabwe.' Empirical mixed-methods study (open- and closed-ended questionnaires, focus group discussions) of the effects of Zimbabwe's 2013 constitutional devolution of local government on urban water, waste-management, and health-service delivery across four urban areas; finds national government policy, not local-council inefficiency alone, a major driver of service-delivery decline. A genuine institutional/legal-mechanism study of devolution's effect on water/sanitation service delivery.",
    "R24E101DAAFF3": "Oumar & Tewari 2012 (Global Journal of Developing Areas / similar), 'The development of water management institutions and the provision for water delivery in Cameroon: history and futures.' Historical-institutional case study of Cameroon's water-management institutions and water-policy/water-law development from the pre-colonial period to present, based on secondary sources and personal observation; documents the absence of a coherent water policy/law as a structural cause of poor water provisioning. A genuine institutional/legal-mechanism history of water access.",
    "R58CA7A40C336": "Goldman 2007 (Geoforum), 'How ''Water for All!'' policy became hegemonic: The power of the World Bank and its transnational policy networks.' Empirical political-economy case study (Orange Farm, South Africa prepaid water meters; national cutoff/cholera-outbreak data; World Bank/transnational policy-network documentary analysis) of how World Bank-driven water-privatization policy diffused globally and its direct effects on household water/electricity access (documented cutoffs affecting over 10 million South Africans, linked to a national cholera outbreak). A genuine institutional/legal-mechanism study of global water-policy diffusion's effect on household access.",
}

EXCLUDES = {}

WRONG_FILE = {
    "R117905075AEC": "Target per database record: Palanca-Tan 2015, 'Unraveling Sanitation and Sewerage Concerns in a Developing Country Metropolis: The Case of Metro Manila, Philippines.' Delivered PDF content is an entirely different document: Oyebode 2018, 'A Comparative Assessment of Water Corporations in Nigeria with Water Management in a Typical Developed Country' (Nigeria/Australia) -- different author, year, and country. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R116235C8172D": "Target per database record: Louis 2013, 'The capacity for collective action in marginalized populations...Cite de l'Eternel in Port-au-Prince (Haiti) and Sierra Santa Catarina in Iztapalapa (Mexico).' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: de Oliveira et al. 2026 (BMC Public Health), 'PrEP public policies for HIV prevention in South America: an intersectional analysis' -- a public-health/HIV-prevention-policy paper with no relation to water/sanitation or the target's Haiti/Mexico case studies. Content-behind-filename mismatch. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R16E56D8BCECE": "Target per database record: Vijayanthi 2002, 'Women's Empowerment through Self-Help Groups: A Participatory Approach.' Delivered PDF content is a different document: Gaurav 2024, 'Women Empowerment through Self Help Groups: An Analytical Study' -- similar general topic but different author, year (2024 vs. 2002), and specific study/journal. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "R746C33035455": "Target per database record: Allouche 2014, 'The role of informal service providers in post-conflict reconstruction and state building.' Delivered PDF content is an entirely different document: Opdyke et al. 2025/2026 (International Journal of Disaster Resilience in the Built Environment), 'Displacement, infrastructure deficits and public health risks in post-conflict Marawi during the COVID-19 pandemic' (Philippines) -- different author, year, and specific conflict/country context. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "RA38256CBC26F": "Target per database record: Khan, Guan, Khan & Khan 2020, 'A comprehensive index for measuring water security in an Urbanizing World: The case of Pakistan's capital.' Delivered PDF content is an entirely different document: Thiliepan, Thennakoon & Madurapperuma 2025, 'Influence of Morphological Characteristics on the Sustainability of Underserved Settlements: A Case Study in Jaffna Municipality...Sri Lanka' -- different author, year, and country. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "RC8E1C6959D2C": "Target per database record: Samano Romero & Chavez-Mejia 2025, 'Water Access in Mexico City: A Review of Local Research Approaches.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Nastar, Isoke, Kulabako & Silvestri 2019 (Local Environment), 'A case for urban liveability from below: exploring the politics of water and land access for greater liveability in Kampala, Uganda' -- different author, year, and country (Uganda vs. Mexico). Content-behind-filename mismatch. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "RD08AB246F841": "Target per database record: Chumo, Kabaria, Muindi, Elsey, Phillips-Howard & Mberu 2022, 'Informal social accountability mechanisms for water sanitation and hygiene (WASH) in childcare centres in Nairobi City County's informal settlements.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Kadiri 2026 (Urban Studies), 'Toxic waters and broken promises: The struggle for health equity in informal settlements' (Film Nagar Basti, Hyderabad, India) -- different author, year, and country (India vs. Kenya). Content-behind-filename mismatch. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "RD7C03A60934A": "Target per database record: Kasper 2025, 'From dams to tanks to jerry cans: Storage as a multi-scalar analytic.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Dhaundiyal 2026 (Policy Design and Practice), 'Reconciling heritage and modern water infrastructures: design challenges from the Indian Himalayan Region' -- different author, year, and specific study. Content-behind-filename mismatch. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
    "RD841349D5ED3": "Target per database record: Borja-Vega, Grabinsky & Klove 2022, 'Introducing a Framework for Analyzing Weaknesses in Institutional Service Delivery and the Human Rights to Water and Sanitation: Case Studies from the Democratic Republic of Congo, Haiti, Mozambique, and Niger.' Delivered PDF's own filename matches this title exactly, but the actual extracted PDF content is a different document: Ogunbode 2026 (Environmental Health Insights), 'The State of SDG 6 in Nigeria (2016-2024): A Critical Review of Progress and Future Strategies' -- different author, year, and country (Nigeria vs. the four target countries). Content-behind-filename mismatch. Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 15
    decided, _ = process_db()
    assert len(decided) == 6
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 236 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
