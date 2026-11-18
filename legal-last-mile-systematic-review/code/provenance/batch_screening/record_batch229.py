#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R111EFC29F4F6": "Ban, Das Gupta & Rao 2010 (Journal of Development Studies), 'The Political Economy of Village Sanitation in South India: Capture or Poor Information?' Rigorous regression study (linear probability models with village- and block-level fixed effects, road-level unit of observation, n=5,276 villages/10,000+ roads, 4 South Indian states) directly testing whether elite/political capture explains poor sanitation infrastructure outcomes under India's Gram Panchayat (village council) constitutional mandate for sanitation service provision. Finds strong evidence of political capture (Gram Panchayat head's village and roads with resident politicians have significantly better paving/drainage/cleanliness) but not traditional social-elite capture, and documents citizens' poor information about local-government sanitation responsibilities. A rigorous regression-based institutional-mechanism study directly isolating a legal/administrative accountability mechanism's (political capture of a constitutionally mandated local-government sanitation function) effect on differential sanitation infrastructure access.",
    "R128F4F59CC33": "Shah, Joshi, Prasad, Chettiparamb, Sekher, Kumar, Singh, Samanta & Mathur 2010 (Vikalpa), 'The Globalizing State, Public Services and the New Governance of Urban Local Communities in India: A Colloquium.' Multi-state comparative field-research colloquium (Gujarat, Rajasthan, Andhra Pradesh, Kerala, Orissa, West Bengal) documenting how post-liberalization urban governance reforms -- decentralization, outsourcing, public-private partnerships, and central urban-renewal schemes (JNNURM, RUIDP) -- produced starkly differential sanitation-service outcomes across paired cities (e.g., Surat: slum access to toilets rose from 20% to 97% between 1991-2006 via a well-resourced, accountable municipal reform model; Junagadh: sanitation and drainage infrastructure unchanged since the 1930s under an under-resourced, poorly monitored model). A rigorous multi-jurisdiction institutional-mechanism comparative case study directly documenting how differing governance-reform/outsourcing institutional models produce differential sanitation-access outcomes for poor urban residents.",
    "R1573575F847B": "Habich-Sobiegalla 2018 (The China Quarterly), 'How Do Central Control Mechanisms Impact Local Water Governance in China? The Case of Yunnan Province.' Rigorous institutional case study (65 interviews, 2011-2014 fieldwork, 2 Yunnan counties with differing economic development) documenting China's 'project mechanism' -- a specific administrative funding-allocation institution requiring local water bureaus to compete for earmarked central-government water-infrastructure investment -- and how it systematically channels funding to localities with existing bureaucratic connections and application capacity, leaving poorer, more remote, dispersed-population counties (West Mountain) persistently underserved relative to better-connected counties (Wild Grass), despite comparable underlying water scarcity. A rigorous institutional/legal-mechanism case study directly documenting an administrative funding-allocation mechanism's effect on differential water-infrastructure access.",
    "REC463A5AE1B2": "Kazora & Mourad 2018 (Sustainability/MDPI), 'Assessing the Sustainability of Decentralized Wastewater Treatment Systems in Rwanda.' Rigorous mixed-methods sustainability assessment (site surveys, laboratory effluent testing, structured questionnaires, and document analysis of national sanitation policy, law, and regulations) of semicentralized sewerage systems in Kigali, explicitly scoring a legal/institutional dimension alongside technical/environmental/socioeconomic dimensions. Finds the legal dimension is the weakest (no sanitation law yet exists in Rwanda, score 1.33/10 among implementers and 1.2/10 among policy-makers/regulators; institutional-framework average 3.87-4.1/10), directly linking documented legal/institutional gaps (absence of enforceable sanitation law, weak inter-agency institutional collaboration) to unsustainable, unreliable sanitation-service delivery. A rigorous institutional/legal-mechanism assessment directly documenting how legal-instrument and institutional-framework gaps undermine sustainable sanitation-service access.",
}

EXCLUDES = {
    "R14D92D589123": ("E01", "Bos & Brown 2012 (Technological Forecasting & Social Change), 'Governance experimentation and factors of success in socio-technical transitions in the urban water sector.' A Transition Management case study of a 10-year urban stormwater/river-health governance-innovation process in the Cooks River Catchment, Sydney, Australia, focused on environmental-governance experimentation, social learning and institutional adaptation for waterway sustainability, not household water/sanitation service access. Extends the established governance/stakeholder-theory exclusion precedent (Stewart & Gray 2006, Batch 227) for content lacking a documented water-access-eligibility mechanism."),
    "R142F0281D111": ("E01", "Hauck & Youkhana 2010 (Research in Rural Sociology and Development), 'Histories and continuities of water governance in Northern Ghana.' A historical/institutional case study of customary, colonial and post-independence water-resource governance in Ghana's Upper East Region, with an empirical case study specifically on fisheries-management institutions (Water User Associations) in two reservoir-adjacent villages -- a natural-resource/livelihood governance study, not household water/sanitation service access. Extends the established water-resource-vs-water-service exclusion precedent (Perez 2002, Batch 227; Ioris 2007, Batch 222)."),
    "R14F3D3927E11": ("E04", "Devnarain & Matthias 2011 (Agenda), 'Poor access to water and sanitation: Consequences for girls at a rural school.' A qualitative case study of a single rural South African school documenting the gendered educational, safety and health consequences (lost instruction time, rape risk while fetching water, menstruation-related stress) of inadequate on-site water/sanitation infrastructure, without documenting a legal/institutional access-eligibility mechanism. Extends the established education/gender-consequences wrong-outcome exclusion precedent, parallel to public-health-outcome exclusions (Imo State Evaluation Team 1989, Batch 227)."),
    "R14EE06D3195B": ("E12", "Kosa, Darago & Adany 2011 (European Journal of Public Health), 'Environmental survey of segregated habitats of Roma in Hungary: a way to be empowering and reliable in minority research.' A nationwide environmental-health survey methodology paper developing and applying a scoring system to identify and rank segregated Roma settlements ('colonies') by infrastructure deficits (including lack of water mains), without analyzing a specific legal/institutional mechanism producing the segregation or documenting differential access under an identifiable policy or eligibility rule. Extends the established methodological/survey-design exclusion precedent (Sullivan & Meigh 2003, Batch 226)."),
    "R002547F1FB80": ("E01", "Refulio Coronado 2025 (University of Rhode Island dissertation), 'Essays on Human Decisions Related to Water Quality Problems in the United States.' An environmental/natural-resource economics dissertation examining recreational beach-visitation responses to coastal water clarity, national PFAS awareness/water-filter adoption, and personalized-risk-information experiments -- a consumer-behavior and environmental-economics study of water-quality perceptions, not a legal/institutional water/sanitation-service access-eligibility mechanism. Extends the established perceptions/consumer-behavior wrong-topic exclusion precedent (McSpirit & Reid 2011, Batch 227)."),
    "R00844FA233FD": ("E01", "Barber & Jackson 2014 (Journal of the Royal Anthropological Institute), 'Autonomy and the intercultural: interpreting the history of Australian Aboriginal water management in the Roper River catchment, Northern Territory.' A historical/anthropological case study of Aboriginal customary weir-construction practices for subsistence fishing and pastoral cattle-watering, and the associated 1946 riparian-law court case restricting the practice -- a water-resource/customary-rights history, not household water/sanitation service access. Extends the established water-resource-vs-water-service exclusion precedent (Perez 2002, Batch 227; Ioris 2007, Batch 222)."),
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
    assert len(INCLUDES) + len(EXCLUDES) == 10
    decided, _ = process_db()
    assert len(decided) == 10
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 229 processed: {n_inc} includes, {n_exc} excludes.")
