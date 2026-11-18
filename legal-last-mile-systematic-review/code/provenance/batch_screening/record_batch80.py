import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "RA1EBB350D5D3": {
        "exclusion_reason": "E05",
        "exclusion_reason_detail": "Burdon, Drew, Stubbs, Webster & Barber (2015), 'Decolonising Indigenous water rights in Australia: flow, difference, and the limits of law,' Settler Colonial Studies 5(4):334-349. A doctrinal/legal-theoretical analysis of Australian water law and Indigenous water rights, drawing on historical records, case law (e.g. Mabo v Queensland), and existing legal/anthropological scholarship, with no original empirical data collection (no interviews, surveys, or fieldwork of its own) -- pure legal-philosophical commentary and critique, the same rationale applied to the earlier Viljoen doctrinal-commentary exclusion (R397656949E83).",
    },
    "RBE33CDE5272C": {
        "exclusion_reason": "E01",
        "exclusion_reason_detail": "Lanz & Provins (2015), 'Using discrete choice experiments to regulate the provision of water services: do status quo choices reflect preferences?', Journal of Regulatory Economics 47:300-324. A stated-preference/discrete-choice-experiment survey-methodology paper examining whether 'status quo' choices in willingness-to-pay surveys reflect genuine consumer preferences for a regulated English water utility's investment planning. The paper's actual contribution is methodological (validity of DCE elicitation for price regulation), not a primary empirical study of legal-administrative water access; no household-level access, connection, or affordability outcome is examined, only WTP for service-quality attributes.",
    },
    "R23EE2449CF6B": {
        "exclusion_reason": "E04",
        "exclusion_reason_detail": "Nakhla (2016), 'Innovative regulations, incomplete contracts and ownership structure in the water utilities,' European Journal of Law and Economics 42:445-469. A theoretical incomplete-contracts economic model of public-private-partnership contract design (concession/affermage/public-ownership modes), illustrated with secondary published performance statistics from Senegalese (SONES/SDE) and Burkinabe (ONEA) water utilities. The outcome variables discussed (network yield/rendement, number of connections, staff labour productivity per 1,000 connections, customer-payment percentage) are utility/company-level performance metrics from published reports, not a household- or applicant-level access outcome measured through original data collection -- the same institutional/organizational-performance exclusion rationale applied to the prior DEA, PDAM, and Thai FSM studies (R8821B3A63A95, REA26B447CC9E, RC47ECBF4C9AF).",
    },
}

includes = {
    "RB51DE5CBDEE4": "Extracted as S554. Mixed-methods case study (39 interviews, 2 focus groups, 110 tourist surveys, 2010 fieldwork) of tourism-driven water inequity in Canggu, Bali, Indonesia, using Ostrom's social-ecological systems framework. Documents genuine legal-institutional content: 11 fragmented, poorly coordinated government departments sharing water-management responsibility; Bali's 1999 regency-level decentralization producing intense inter-Regency competition over water resources; the traditional subak irrigation-governance system administered by a democratically elected Pekaseh; widespread non-enforcement of building-coverage restrictions (40% of plot) and of water-metering/tariff-payment regulations against the tourism industry; and up to 5,000 households in Denpasar on a waitlist for a public water connection, with those unconnected paying unlicensed private-vendor prices as high as Rp50,000 (~US$5.80) per gallon. MMAT (Mixed Methods Appraisal Tool).",
    "RF78C62C99387": "Extracted as S555. Mixed-methods ethnographic study (155 participant-observation site visits, 10 informal interviews, 7 semi-structured interviews, water-quality monitoring at 5 sites, 2012-2013 fieldwork) of ecosystem services and disservices accessed by people experiencing homelessness via informal urban waterways and wetlands along the Salt River in Phoenix, Arizona. Documents genuine legal-institutional content: Phoenix's 2004 anti-camping ordinances criminalizing sleeping, storing belongings, and food preparation in public spaces; public water fountains and bathrooms closed and locked at night, limiting formal access; the Phoenix Heat Relief Network's insufficient hydration/cooling-station capacity and limited operating hours; and the illegality of accessing state/federal-owned unplanned waterways, exposing users to Park Ranger enforcement and threatened arrest -- documenting an extra-legal informal water-access strategy adopted by a legally excluded vulnerable population, alongside the serious health-risk trade-off (E. coli concentrations exceeding EPA drinking-water standards in 21-100% of measurements). MMAT (Mixed Methods Appraisal Tool).",
    "R3D2D360577A3": "Extracted as S556. Qualitative ethnographic case study (24 months of fieldwork, 2006-2014, extended participant-observation and interviews) of everyday negotiation of state water, electricity, and building-permission access in Delhi's informal slum settlements (Shiv Camp) and middle-class unauthorized colonies (Chattarpur), India. Documents genuine legal-institutional content directly on point for the review's 'legal last mile' framework: low-income slum residents securing illegal electricity/water reconnections through direct personal negotiation (bribes, threats) with low-level bureaucrats rather than formal legal channels; unauthorized colonies (housing 20%+ of Delhi's population) categorically barred from official municipal water/sewerage connections because they fall outside the city master plan despite residents holding valid property-transaction documents; Delhi Jal Board officials installing and operating at least 15 unregistered 600-foot-deep borewells in direct violation of a 2010 state government ban on new borewell drilling, paid via an MLA's discretionary fund rather than official Jal Board funds; and Resident Welfare Associations acting as state-recognized but formally non-state intermediaries controlling informal water-delivery and construction-approval access. CASP Qualitative Studies Checklist (qualitative).",
}

reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in excludes:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        d = excludes[rid]
        r["full_text_decision"] = "exclude"
        r["final_decision"] = "exclude"
        r["reviewer_1"] = reviewer
        r["exclusion_reason"] = d["exclusion_reason"]
        r["exclusion_reason_detail"] = d["exclusion_reason_detail"]
        changed += 1
    elif rid in includes:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = includes[rid]
        changed += 1

assert changed == len(excludes) + len(includes), f"expected {len(excludes)+len(includes)}, got {changed}"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

with open(log_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    log_fieldnames = reader.fieldnames
    log_rows = list(reader)

id_to_row = {r["record_id"]: r for r in rows}
for rid, d in excludes.items():
    r = id_to_row[rid]
    log_rows.append({
        "record_id": rid,
        "title": r["title"],
        "authors": r["authors"],
        "year": r["year"],
        "stage": "full_text",
        "exclusion_code": d["exclusion_reason"],
        "exclusion_reason_detail": d["exclusion_reason_detail"],
        "reviewer": reviewer,
        "date": "2026-09-21",
    })

fd, tmp = tempfile.mkstemp(dir="02_screening/exclusion_log")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=log_fieldnames)
    writer.writeheader()
    writer.writerows(log_rows)
os.replace(tmp, log_path)

print("done, db changed", changed, "log rows now", len(log_rows))
