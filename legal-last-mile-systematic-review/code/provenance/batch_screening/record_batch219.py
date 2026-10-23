#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R0B902066E9BE": "Rajaraman, Travasso & Heymann 2013 (Journal of Water, Sanitation and Hygiene for Development) qualitative interview study (48 semi-structured interviews) of access to sanitation at the workplace amongst low-income working women in Bangalore, India, across four occupation groups (construction, domestic, street vending, garment factory work). Finds access to sanitation at work is governed by employer practices and the legal/regulatory framework -- domestic workers have essentially no legal protection (no legislation requiring employers to provide latrine access), while the Factories Act (1948) and Building and Other Construction Workers Act (1996) mandate toilet provision but were found to be well-implemented in factories and non-existent on construction sites. A genuine institutional/legal mechanism study documenting how the presence or absence of specific labour-law coverage produces differential workplace sanitation access by occupation/employment-sector.",
    "R186BCFDEF64B": "Javed & Farhan 2020 (Springer book chapter) mixed institutional-analysis and household-survey study (low-income areas of Lahore and Peshawar, Pakistan) of structural and institutional barriers to political and social inclusion, including access to basic urban services (water supply, sanitation, electricity, healthcare). Documents institutional fragmentation between provincial and local government under Pakistan's Local Government Ordinance/Act framework, and a case study of the Badar Colony Water Supply and Sewerage Initiative, in which an NGO formed by residents contributed 38% of capital investment and entered a bulk-purchase/distribution agreement with the city water utility (WASA) after the utility had no funds for service extension. A genuine institutional/legal mechanism study of decentralized governance structure and NGO-utility partnership models directly affecting water-service access for low-income urban communities.",
    "R16F5F8144871": "Colbran 2017 (Cambridge University Press book chapter) legal-historical case study of piped water supply in Jakarta, Indonesia, by a legal advisor at the Norwegian Centre for Human Rights, examining how water has been treated as a political, economic, and social good across successive administrations and the resulting gap between law and practice. Documents that 'the government has put in place legal obstacles that mean many of the city's lowest income residents do not qualify for household water supply services,' disproportionate tariff increases for low-income households (63% increase in 2005) versus upper-income/commercial customers (under 11%), changing eligibility criteria for lower-tariff customer groups, and a 2004 court ruling suspending a 40% tariff increase. A rigorous legal/institutional mechanism study directly documenting formal eligibility barriers and discriminatory tariff structures excluding the urban poor from formal water-service access.",
    "R178232D887EC": "Mukherjee, Kumar, Cardosi & Singh 2009 (Waterlines) programme-evaluation case study of the Total Sanitation and Sanitation Marketing (TSSM) project's 'enabling environment' (EE) framework across India, Indonesia and Tanzania, examining eight institutional dimensions (policy/strategy, institutional arrangements, programme methodology, implementation capacity, product/tool availability, financing, cost-effective implementation, and monitoring/evaluation) determining sustainable scale-up of rural sanitation access. Documents concrete institutional changes, including Indonesia's 2008 National Community-Based Total Sanitation strategy that 'unequivocally forbids the use of subsidies for household sanitation facilities.' A genuine institutional/policy mechanism study directly examining the policy and financing environment enabling or constraining rural sanitation-access scale-up.",
    "R1C6169322694": "Singh, Upadhyay & Mittal 2005 (ASCE EWRI conference proceedings) policy-analysis study of Indian municipal water tariff structures and their socio-economic sustainability, documenting that connection charges (e.g., Rs. 12,000 for domestic and up to Rs. 42,000 for commercial connections in Guntur, Andhra Pradesh) are 'a major obstacle for the poor households in getting connection to water supply systems,' that approximately 50% of the Indian poor population remains unconnected and therefore receives no subsidy benefit, and that unconnected poor households pay more than ten times per cubic metre what connected households pay via private vendors. A rigorous institutional/legal mechanism study directly examining connection-fee and tariff-structure barriers to formal water-service access for the poor in India.",
    "R6E2CA3E33C37": "Loftus & McDonald 2001 (Environment and Urbanization) critical political-ecology case study of the 1993 privatization of water and sanitation services in Buenos Aires, Argentina (Aguas Argentinas concession). Documents a regressive 'infrastructure charge' (US$43-600 for water, up to US$1,000 for sewerage) levied specifically on newly-connected households -- disproportionately affecting those without prior connections, i.e., the poor -- plus an additional connection-acceleration charge (OPCT) that in practice delayed connections until paid, disconnections of poor households in payment arrears, and repeated national-government intervention overriding the independent regulator (ETOSS) to grant tariff increases (e.g., a 1998 increase from a proposed 1.6% to an imposed 4.6%). A rigorous institutional/regulatory mechanism study directly documenting connection-fee and regulatory-capture barriers to affordable formal water-service access for the urban poor.",
}

EXCLUDES = {
    "R13DCD030A31C": ("E01", "Danso-Appiah, Utzinger, Liu & Olliaro 2008 (Cochrane Database of Systematic Reviews) systematic review of pharmaceutical drug treatments for urinary schistosomiasis, a parasitic infection. A clinical/medical drug-treatment review entirely unrelated to water-service access-eligibility mechanisms; the apparent keyword overlap is with 'water-borne disease' rather than any legal/institutional water-access topic. Wrong-topic clinical-treatment review."),
    "R18B4875CC0DD": ("E12", "Nelson & Murray 2008 (Annual Review of Environment and Resources) broad conceptual/technical review of sanitation technologies for unserved populations, covering toilet types, faecal sludge management, and wastewater treatment, with only secondary and general discussion of institutional capacity and legal tenure as implementation barriers. A conceptual/technology review with no original empirical data collected by the authors; extends the established review-paper exclusion precedent (Aiyer 2007; Sternlieb & Laituri 2010, Batch 216; Sommer et al. 2014, Batch 218)."),
    "R1DAB2ADE242E": ("E01", "Postel & Thompson 2005 (Natural Resources Forum) study of watershed protection programmes (Quito, Costa Rica, New York City) as institutional mechanisms for safeguarding hydrological/ecosystem services that supply drinking water. A water-RESOURCE/ecosystem-services governance study, not a household water-SERVICE access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction (Wong 2016; Zawahri 2006; Moore 2014, among others). Wrong-topic watershed/ecosystem-services study."),
    "R16A3197AFC75": ("E01", "Grigg 2017 (ASCE Journal of Infrastructure Systems) institutional-analysis case study of the 2015 Flint, Michigan drinking-water crisis, examining institutional arrangements, governance failures, and regulatory decision-making (state emergency management, corrosion-control lapses) that produced lead contamination of the water supply. An institutional-capacity/regulatory-compliance study concerning a utility's failure to meet water-quality/safety obligations, distinct from a legal/institutional eligibility mechanism governing access to service; extends the established regulatory-compliance exclusion precedent (Teodoro & Switzer; Kot/Gagnon/Castleden 2015, Batch 214)."),
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
    print(f"Batch 219 processed: {n_inc} includes, {n_exc} excludes.")
