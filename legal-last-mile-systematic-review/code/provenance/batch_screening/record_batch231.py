#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R20684C4B20E4": "Victor 2019 (Anthropology Southern Africa), '\"There is life in this place\": \"DIY formalisation,\" buoyant life and citizenship in Marikana informal settlement, Potchefstroom, South Africa.' Ethnographic case study of an informal settlement labeled 'too informal' to receive basic municipal service provision, whose residents self-organized (laying out stands/streets, installing water infrastructure, registering a residents' committee as an NPO) to politically claim legal recognition and municipal water/service provision from the city council. Directly documents how formal/informal legal-administrative status functions as a service-eligibility mechanism and how residents navigate/circumvent it to secure water access. A genuine legal/institutional access-mechanism case study.",
    "R34D4B693CF22": "Smith & Hanson 2003 (Urban Studies), 'Access to Water for the Urban Poor in Cape Town: Where Equity Meets Cost Recovery.' Case study of a five-year (1997-2001) local-government restructuring and commercialisation process in Cape Town's water sector, examining two cost-recovery policies -- underinvestment in low-income-area infrastructure and water disconnections/cutoffs (160,000 in 3 years) -- as institutional/administrative mechanisms reproducing apartheid-era territorial service inequities under a post-apartheid 'basic needs' framework. Directly documents a legal/administrative cost-recovery and disconnection mechanism's differential effect on urban-poor township residents' water access.",
}

EXCLUDES = {
    "R1B8FD401A58C": ("E01", "Sinha & Pokhriyal 2001 (Social Change), 'Rehabilitation in Tehri Dam: An evaluation.' A broad evaluation of dam-displacement resettlement and rehabilitation policy for Tehri Dam oustees in India (land compensation, resettlement-site adequacy, institutional coordination), with inaccessibility to drinking water mentioned only as one of several general critical problems in resettlement sites. A broad dam-displacement/resettlement-policy evaluation, not a focused legal/institutional water-service-access-eligibility mechanism; extends the established broad-governance/wrong-topic exclusion precedent."),
    "R1D9934EC161F": ("E01", "Okpala 1980 (Third World Planning Review), 'Water Supply Constraints on Nigeria's Economic Development: The Example of Anambra State.' A broad descriptive/economic-development essay reviewing water-supply infrastructure statistics, financing difficulties of the state Water Board, and general development-policy discussion, without analyzing a specific legal/institutional access-eligibility mechanism. Extends the established broad-topic/policy-essay exclusion precedent."),
    "R1C7B5A6466D9": ("E01", "Katani 2010 (Wageningen University doctoral thesis), 'The Role of Multiple Institutions in the Management of Micro Spring Forests in Ukerewe, Tanzania.' A legal-pluralism/institutional-bricolage study of customary and statutory tenure over land, water sources, and forest in micro-spring-forest commons, focused on natural-resource governance and control of access to water SOURCES (not municipal/piped water SERVICE access). A water-resource-governance case study; extends the established water-resource-vs-water-service exclusion precedent (Hauck & Youkhana 2010, Batch 229; Barber & Jackson 2014, Batch 229)."),
    "R215A46C61B6D": ("E01", "Staddon, Rogers, Warriner, Ward & Powell 2018 (Water International), 'Why doesn't every family practice rainwater harvesting? Factors that affect the decision to adopt rainwater harvesting as a household water security strategy in central Uganda.' A household-level mixed-methods study of factors (intermediary organizations, finance mechanisms, life-course dynamics, land tenure) affecting individual household adoption decisions for a coping technology, not a documented legal/institutional access-eligibility mechanism producing differential water-service access. Extends the established household-coping/adoption-determinant exclusion precedent."),
    "R21BC744CC726": ("E01", "Shrestha, Roth & Joshi 2018 (Ecology and Society), 'Flows of change: dynamic water rights and water access in peri-urban Kathmandu.' An ethnographic case study (following water sources/flows in two peri-urban communities) of informal, microlevel contestation and negotiation over irrigation wells and drinking-water sources among farmers, in-migrants, and water vendors amid urbanization -- a water-resource/informal-negotiation ethnography, not a documented legal/institutional water-service-access-eligibility mechanism. Extends the established water-resource-vs-water-service and informal-negotiation exclusion precedent (Wutich 2011, Batch 230)."),
    "R152C9FC53F5A": ("E01", "Roth, Khan, Jahan, Rahman, Narain, Singh, Priya, Sen, Shrestha & Yakami 2019 (Climate Policy), 'Climates of urbanization: local experiences of water security, conflict and cooperation in peri-urban South-Asia.' A multi-site (Khulna, Gurugram, Hyderabad, Kathmandu) qualitative synthesis critiquing the 'community resilience' discourse in peri-urban water-security/climate-change policy, without isolating a specific legal/institutional access-eligibility mechanism. A broad policy-discourse synthesis; extends the established governance/hydropolitics-without-institutional-mechanism exclusion precedent (Kane 2012, Batch 230)."),
    "R27165B30AE1C": ("E01", "Paerregaard 2013 (Mountain Research and Development), 'Governing Water in the Andean Community of Cabanaconde, Peru: From Resistance to Opposition and to Cooperation (and Back Again?).' An ethnographic study of the shift from a communal dual (Hanansaya/Urinsaya) irrigation-allocation model to a state-administered water-committee model in an Andean farming community, focused on IRRIGATION (agricultural water resource) governance, not household water-service access. Extends the established water-resource-vs-water-service exclusion precedent (Kane 2012, Batch 230; Hauck & Youkhana 2010, Batch 229)."),
}

WRONG_FILE = {
    "R31BD502FD038": "Target per new_batch_pool.json / Drive filename: Pederson 2009, 'Stream-flow bill bad for state' (a water-law opinion piece on streamflow legislation). Delivered PDF content (verified via full-text review) is an entirely different document: Hirzel, Soule, Schneider, Gedik & Grimm 2014, 'A Catalog of Stream Processing Optimizations,' ACM Computing Surveys -- a computer-science survey of software stream-processing-system optimizations, wholly unrelated in author, year, publisher, and subject matter (software engineering, not water law). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
    assert len(decided) == 9
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 231 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
