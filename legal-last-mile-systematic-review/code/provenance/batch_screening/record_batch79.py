import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "R8A34FFD0A52F": {
        "exclusion_reason": "E12",
        "exclusion_reason_detail": "A 'Defining Moments' reflective essay (Health Communication journal's personal-narrative/vignette section) built around unstructured focus-group anecdotes about lived experience of water access in southeastern Ohio, analyzed through communication/narrative theory (liminality, otherness) rather than legal-institutional mechanism analysis. No described sample size, sampling method, or systematic coding protocol -- the piece does not meet the review's standard for an appraisable empirical study design.",
    },
    "RC47ECBF4C9AF": {
        "exclusion_reason": "E04",
        "exclusion_reason_detail": "Quantitative study (multiple regression analysis of data from 160 Thai municipalities) of technical, financial, social, and institutional factors influencing faecal sludge management (FSM) service performance. The outcome variables (operational efficiency, service performance/complaint-rate, and treatment feasibility indicators) are municipality-level service-performance metrics, not household- or applicant-level access, connection, affordability, or reliability outcomes -- the same institutional/organizational-performance exclusion rationale applied to the prior DEA and PDAM-performance studies (R8821B3A63A95, REA26B447CC9E). Also concerns fecal sludge/septic management rather than water supply access.",
    },
}

includes = {
    "R5AB0C14E4E11": "Extracted as S551. Mixed-methods statistical study (487-household survey across four underserved settlements: Ashaiman and Teshie in Accra, Ghana; Khayelitsha and Philippi in Cape Town, South Africa) of gender-differentiated water access, uses, knowledges, governance, and experiences. Documents genuine legal-institutional content: Ghana's GWCL urban piped-supply mandate and the AVRL private-consortium management period (2006-2011); South Africa's Constitutional right to water and sanitation, the Free Basic Water policy (6kl/household/month regardless of household size), and apartheid-era racial/class-differentiated water infrastructure still shaping access via the ongoing RDP housing-formalization process. JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies (observational).",
    "R169602E7BE36": "Extracted as S552. Qualitative case study (18 semi-structured interviews with rural water committees plus interviews with NGO/multilateral/government staff, 12 months of fieldwork 2007-2010, plus 2014 follow-up) of the 'organic empowerment' of Nicaragua's community-based water committees (CAPS). Documents genuine legal-institutional content: the Special Law of Potable Water and Sanitation Committees (Law 722, 2010) that formally recognized over 5,000 previously unrecognized CAPS serving more than 1 million rural residents; the prior General Water Law (Law 620, 2007) that excluded CAPS; CAPS' lack of personeria juridica (legal personality) preventing legal receipt of constructed water systems; user-fee collection ($0.23-$2.85/household/month) with informally negotiated non-enforcement of shutoff rules for seasonal-labor households; and legal-gray-area negotiation of land/water-source access with private landowners. CASP Qualitative Studies Checklist (qualitative).",
    "R17B052404210": "Extracted as S553. Qualitative case study (48 semi-structured and focus-group interviews with commercial farmers, emerging farmers, and local community members, plus document analysis, fieldwork 2011 and 2015) of power asymmetries in the establishment of a Water User Association (WUA) in the Groot Marico catchment, South Africa. Documents genuine legal-institutional content: the National Water Act 1998's definition and establishment guidelines for WUAs as the local collaborative-governance vehicle for redressing apartheid-era water-access inequality; the 'existing lawful use' provision tying commercial-farmer water entitlements to land ownership from the 1996-1998 baseline period, continuing to advantage the white minority of commercial irrigation farmers despite the NWA's stated intent to separate water rights from land ownership; and a documented WUA-establishment meeting from which black rural community members and emerging farmers were functionally excluded via short notice, an inaccessible venue, and English-only proceedings, resulting in commercial farmers dominating the vote on WUA leadership and a pre-drafted constitution. CASP Qualitative Studies Checklist (qualitative).",
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
