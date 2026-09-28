#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R0C54E2A3F77C": "Gowlland-Gualtieri 2010 (book chapter, Water Governance in Motion) doctrinal/policy analysis of South Africa's water law framework: the constitutional right to water (Sec. 27), the National Water Act 1998 and Water Services Act 1997, the Free Basic Water Policy (2001, 6 kl/household/month), and cost-recovery mechanisms (block tariffs, disconnection procedures, pre-paid water meters). Documents, via statutory text, government data (2000-01 cholera outbreak; national access-coverage statistics) and case law (Mazibuko/Phiri litigation, Residents of Bon Vista Mansions, Manquele, Highveldridge), how disconnection and pre-paid-meter mechanisms directly and measurably deprive poor households of even the free basic water entitlement, with documented individual testimony and health/social consequences. Extends the legal-institutional-mechanism-with-documented-outcome precedent to statutory/case-law-based analysis (cf. Romano 2012 Nicaragua legislative analysis, S1011).",
    "R21570E47C3A1": "Njoh 2011 (Development) comparative case study of two community self-help water supply projects in Cameroon's Southwest Region (Mpundu, Muyuka -- failure; Bonadikombo, Limbe -- success). Documents a formalized, differentiated eligibility/fee structure for the successful project (100,000 frs CFA one-time connection fee + 5,000 frs CFA yearly maintenance fee for private domestic connection; gender-differentiated construction-labor levies of 2,500 frs CFA for men vs. 1,300 frs CFA for women; 7,000 frs CFA for absentee business owners; 3,000 frs CFA for committee members) directly tied to documented divergent connection/coverage outcomes: Bonadikombo succeeded (1,000 domestic subscribers, 25 public standpipes serving a population of 10,000, gaining 27 new subscribers/year since 2007) while Mpundu failed (discontinued in the early 1980s having raised only 14,000 of an expected 500,000 frs CFA, with only a few trenches dug). Extends the community-committee-mediated-connection and differentiated-fee-structure precedent (Ratner & Rivera Gutierrez, S1013).",
    "RBCF8A8901239": "Muller 2008 (Environment and Urbanization) policy-evaluation study, authored by the former Director-General of South Africa's Department of Water Affairs and Forestry, of the country's 2001 Free Basic Water (FBW) policy's implementation and outcomes from 1997 to 2005. Documents, via national coverage statistics (access-deprivation declining from 12 million of 36 million in 1994 to 3.7 million of 48.1 million by 2005) and a specific documented sub-case (the Shemula pre-payment water-kiosk project in KwaZulu-Natal, where only 323 of 7,500 households used the metered system at an average consumption of six litres/person/day, most reverting to traditional water sources), how the payment-for-operations/pre-payment tariff mechanism directly produced severe under-consumption and access deprivation among the poor prior to the FBW policy's introduction, and evaluates the FBW policy's subsequent effect on equity and coverage. Extends the legal/institutional-tariff-mechanism-with-documented-outcome precedent (Gowlland-Gualtieri, this batch); both examine the same South African Free Basic Water policy from complementary methodological angles (statutory/case-law analysis vs. programmatic policy evaluation).",
    "R21CCF27E55E5": "Zlolniski 2011 (Cultural Anthropology) ethnographic study of water politics in the San Quintin Valley, Baja California, Mexico. Documents how Mexico's 1992 National Water Law (Ley de Aguas Nacionales) institutionalized a differential subsidy structure -- subsidized desalination-plant construction, electricity, and well-meter costs for export agribusiness vs. no equivalent subsidies for domestic users -- and how the state water utility (CESPE)'s tariff and quota policies (a 115% flat-fee increase in 2007, a $227/household meter-installation cost, and a fixed five-barrels/week household quota irrespective of household size) directly produced documented differential price and access outcomes for poor colonia residents relative to agribusiness (e.g., the Juana Gallego case study documenting a household forced to split purchases between the subsidized utility and a more expensive private vendor; the Colonia Arbolitos case documenting a price drop from Mex$300 to Mex$40/month upon obtaining a municipal connection). Extends the institutional-rationing/quota-mechanism precedent (Ruiz Rosado, S1012) and the differential-legal-subsidy-structure precedent.",
}

EXCLUDES = {
    "RBA18C893F671": ("E01", "Ormerod & Scott 2013 (Science, Technology & Human Values) survey-based study (n>250 Tucson, Arizona residents) of public trust in professional institutions and its relationship to willingness to drink reclaimed (potable-reuse) water. A public-perception/technology-acceptance study of indirect potable reuse; no legal/institutional mechanism governing differential water access is examined. Wrong-topic public-trust/technology-acceptance study."),
    "RBD738547CB4C": ("E01", "Ibem 2013 (Urban Forum) household-survey study (n=452) of accessibility to services and facilities -- water, electricity, refuse disposal, transport, education, healthcare, recreation, shopping -- for residents of nine public housing estates in Ogun State, Nigeria. A multi-service (7+ domain) accessibility study in which water is one of many services measured, not a focused water-access legal/institutional-mechanism study. Reapplies the broad multi-domain-accessibility-study E01 precedent (cf. Kapuria Delhi Quality of Life, Batch 202)."),
    "RBA346FCF6A8C": ("E05", "Meinzen-Dick & Pradhan 2001 (IDS Bulletin) conceptual/theoretical article applying legal-pluralism theory to natural-resource property rights, illustrated with secondary water-rights examples drawn entirely from other researchers' prior published and unpublished studies (Nepal, Sri Lanka, Bali, Haiti, Mozambique). No original empirical data collection by the authors themselves. Reapplies the established conceptual/theoretical-framework-with-secondary-examples E05 precedent (Cleaver & Hamada, Batch 202; Zakiya, Batch 201)."),
    "R0A22230BEAC5": ("E01", "Lopez Porras, Stringer & Quinn 2019 (Science of the Total Environment) qualitative case study (27 semi-structured interviews) of corruption and conflict as barriers to adaptive water governance in the Rio del Carmen watershed, Mexico. Focus is on agricultural/watershed water-ecosystem-services governance (irrigation, grassland loss, aquifer management), not household/domestic water access. Reapplies the established agricultural/watershed-scale water-governance E01 precedent."),
    "R209F0EDBD5C8": ("E01", "Bisung, Elliott, Schuster-Wallace, Karanja & Bernard 2014 (Social Science & Medicine) household-survey case study (n=485) of social capital and collective action for community-based water/sanitation initiatives in a lakeshore village in Western Kenya. A social-capital-theory application study measuring trust/network/participation variables and their association with collective action; no specific legal/institutional mechanism producing documented differential water access is tested. Reapplies the established social-theory/community-cohesion E01 precedent."),
    "R21FFE47FADB8": ("E12", "McGeough 2013 (Text and Performance Quarterly) performance-studies/rhetorical-analysis essay examining Indian 'toilet festivals' in Mumbai and Pune slums as embodied civic-participation performances, based on secondary documents and prior researchers' interview data rather than the author's own empirical fieldwork or data collection. Wrong study design: rhetorical/performance-studies textual analysis, not an empirical social-science study of a legal/institutional water-access mechanism."),
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
    print(f"Batch 203 processed: {n_inc} includes, {n_exc} excludes.")
