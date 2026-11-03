import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "RC1CB10DA729E": {
        "exclusion_reason": "E01",
        "exclusion_reason_detail": "Schiedek, Gabrielsson, Jimenez, Gine, Roaf & Swain (2021), 'Assessing national WaSH targets through a water governance lens: a case study of the Sanitation and Water for All partnership commitments,' Journal of Water, Sanitation and Hygiene for Development 11(5):805-813. A deductive content analysis of 291 voluntary policy commitments submitted by governments and other constituencies to the Sanitation and Water for All (SWA) partnership's Mutual Accountability Mechanism online database (2019-2020), coded against a governance-framework taxonomy (building blocks, functions, attributes, outcomes, SMART criteria). No original household, community, or applicant-level data collection; no examination of any specific country's legal-administrative water-access mechanisms (permitting, connection, tariff, enforcement). The unit of analysis is the wording quality of international-partnership commitment texts, not a primary empirical study of legal-administrative water access -- the same macro/cross-national governance-analysis rationale applied to the earlier Nkiaka, Shadabi & Ward, and Laitinen exclusions.",
    },
}

includes = {
    "R9FA1C1004C69": "Extracted as S561. Dwipayanti et al. (2022), qualitative case study (20 semi-structured interviews, 6 focus groups, August 2020 fieldwork) of Inclusive WASH in the 'super-premium' tourism destination of Labuan Bajo, Indonesia. Documents genuine legal-institutional content: the municipal water utility (PDAM) supplying piped water only twice a week amid a 10 L/s deficit; Indonesia's Ministry of Public Works Regulation No. 14/Prt/M/2010 minimum water-requirement service standard (60 L/person/day); a differential/tiered tariff system charging hotels more than households, with the unintended effect of preferential delivery to paying commercial users; up to 5,000 households effectively rationed via reduced PDAM allocation since 2015 despite population growth; and the multi-stakeholder POKJA AMPL government working group coordinating (but rarely convening on) WASH governance. CASP Qualitative Studies Checklist (qualitative).",
    "R07131CF3EAEE": "Extracted as S562. Akpabio & Ozoh (2026), mixed-methods study (800-household cross-sectional survey, 751 retrieved, 93.9% response rate, plus key-informant interviews, observation, and narrative collection) of household WaSH access in Calabar Municipality, Ikom, and Ogoja, Cross River State, Nigeria. Documents genuine legal-institutional content: Cross River State's new Water Supply and Sanitation Law (2025) establishing a statutory right to basic WaSH services and a regulatory framework; the State Ministry of Water Resources' newly inaugurated WaSH regulatory department; the 2025 WaSH Policy's financing, citizen-accountability dashboard, and differentiated service-delivery mechanisms; and documented community task groups (e.g. Obubra LGA) institutionalized within state policy alongside persistent funding/institutional-fragmentation constraints. MMAT (Mixed Methods Appraisal Tool).",
    "RC1E784D9D197": "Extracted as S563. Nkolola & Phiri (2024), mixed-methods study (122 household/community-leader interviews via the mWater tool, Empowerment in WASH Index survey, 2023-2024 fieldwork) of gender dynamics in water access and Water Point Committee (WPC) governance in rural Mbala, Zambia. Documents genuine legal-institutional content: WPCs as the community-level governance body responsible for WAP (water access point) management, user-fee collection, and repair-funding decisions; formal eligibility criteria for WPC membership (age, literacy, community trust); WPC election cycles and their frequent disruption; and quantified empowerment/disempowerment ratios showing women are not structurally excluded from WPC leadership, with WAP sustainability instead undermined by inadequate community financial-contribution enforcement. MMAT (Mixed Methods Appraisal Tool).",
    "R8FFC351CC113": "Extracted as S564. Mandara, Butijn & Niehof (2013), mixed-methods study (221-household survey, focus group discussions, semi-structured interviews with village leaders and District Council officials, plus documentary review of national water-policy frameworks, 2011-2012 fieldwork) of community management and sustainability of rural water facilities in Kondoa and Mpwapwa districts, Dodoma region, Tanzania. Documents extensive genuine legal-institutional content directly on point for the review's 'legal last mile' framework: Tanzania's 2002 National Water Policy (NAWAPO) and 2008 National Water Sector Development Strategy (NWSDS) and their failure to explicitly define Village Water Committee (VWC) and household-level roles; the 'subsidiarity principle' shifting full operation-and-maintenance cost-recovery to user fees; District Water Department (DWD) technical/staffing capacity deficits (41-50% below required staffing); documented private-operator tender processes handled without district legal-unit oversight; and detailed household-level user-fee schedules, water-fund bank accounts, and VWC gender-parity composition requirements under national guidelines. MMAT (Mixed Methods Appraisal Tool).",
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
