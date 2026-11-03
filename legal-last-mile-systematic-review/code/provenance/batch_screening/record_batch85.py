import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "R65E0D0F26A0A": {
        "exclusion_reason": "E05",
        "exclusion_reason_detail": "Celume, Donoso et al., 'Reform of the Chilean water code in 2022: shift from a neoliberal model to a more public interest model.' A PRISMA-style systematic review of 63 existing secondary legal-critique studies combined with comparative legal/policy text analysis of Law No. 21,435 versus the 1981 Water Code. No original household-level empirical data collection (no surveys, interviews, or fieldwork) -- matches the Viljoen/Burdon doctrinal-commentary exclusion precedent, extended to systematic reviews of secondary legal literature.",
    },
    "R73C7494E55DD": {
        "exclusion_reason": "E04",
        "exclusion_reason_detail": "Gidion, 'Ranking water utilities in a competitive scenario using two years of information and data envelopment analysis,' Water Practice & Technology 20(2):436-448. Network-DEA efficiency-benchmarking study of 40 Tanzanian urban water utilities (UWUs) on inputs (non-revenue water, personnel expenditure, staffing level) versus outputs (population serviced, hours of service, metered customers). Outcome is utility-level performance ranking, not household/applicant-level access -- matches established DEA-exclusion precedent from R8821B3A63A95, REA26B447CC9E, RC47ECBF4C9AF, R23EE2449CF6B.",
    },
    "R96593F742647": {
        "exclusion_reason": "E05",
        "exclusion_reason_detail": "Satpathy & Jha, 'Intermittent water supply in Indian cities: considering the intermittency beyond demand and supply,' AQUA -- Water Infrastructure, Ecosystems and Society 71(12):1395-1407. Explicitly a literature-review/secondary-data synthesis paper (authors' own stated limitation: 'The study is mostly relying on the review of literature to substantiate the claim... it is not providing any solution to the problem'). Uses only existing government/utility statistics (Census, municipal water-board reports) and a literature review of caste/class/gender/religion/region dimensions of intermittent water supply; no original household-level empirical data collection.",
    },
    "R3BF9C93DC6A9": {
        "exclusion_reason": "E05",
        "exclusion_reason_detail": "Saadi & Johns, 'Governing smart water cities for urban water resilience: international lessons and a Canadian policy framework,' Water Policy (2026). Explicitly self-described as a 'policy-oriented scoping review' (Section 2.1) synthesizing 51 secondary academic and policy/municipal sources across five international case studies and five Canadian examples; no original empirical data collection of any kind. Matches the systematic-review-of-secondary-literature E05 exclusion precedent.",
    },
}

includes = {
    "R3B336474D5A8": "Extracted as S565. Mbiza, Scholz, Dinka & Hweru (2026), mixed-methods study (150-household structured survey, environmental spot measurements, and secondary policy-document review, Southlea Park, Harare, Zimbabwe) developing and applying the Greywater Service Innovation Ladder (GSIL) governance framework for decentralised greywater services. Documents genuine legal-institutional content: Zimbabwe's National Water Policy governance vacuum for greywater (limited statutory recognition leaving peri-urban settlements to manage wastewater informally); Rural District Council (RDC)/ward-committee decision-making authority over Gate 1-2 service-transition thresholds; the Equity Safeguard Ratio (ESR) benchmarking household affordability against a 3-5% income threshold; and Policy Readiness Score (PRS) content-analysis of statutory instruments, local authority policies, and implementation guidelines. MMAT (Mixed Methods Appraisal Tool).",
    "RA1815DB6A8FD": "Extracted as S566. Abawari et al. (2026), qualitative photovoice study (10 teachers, 10 students, 6 facilitated group discussions, plus a 75-participant stakeholder advocacy event, two public primary schools in Jimma Town, Ethiopia) examining school WASH governance gaps. Documents genuine institutional-governance content: participant-identified systemic governance failures including weak monitoring/supervision, unclear institutional responsibilities among local government, health authorities, and school administrations, and absence of reporting mechanisms for deteriorated facilities; the advocacy event's function in bridging vertical bureaucratic-accountability structures between school communities and local officials. CASP Qualitative Studies Checklist (qualitative).",
    "R19F2163297EB": "Extracted as S567. Gashaw, Tessema, Temesgen, Bayu, Mekbib & Geremew (2025), mixed-methods study (400-household structured questionnaire survey across 120 sampled water points, plus key-informant interviews with technicians/engineers/water committees, Gursum District, Eastern Ethiopia) of rural community water supply scheme functionality and sustainability. Documents genuine legal-institutional content: community ownership and governance of water schemes (73.3% community-owned per national guidelines); WASHCO (Water, Sanitation and Hygiene Committee) financial-management and tariff-setting authority; District Water and Energy Resources Development Office (WWRDO) institutional support role; and government/NGO (UNICEF, PSNP) technology-selection authority versus low community involvement (11.2%) in technology choice. MMAT (Mixed Methods Appraisal Tool).",
    "R2A9D36D4B43E": "Extracted as S568. Azupogo, Dassah & Bisung (2023), participatory mixed-methods concept-mapping study (29 recruited / 22 participating stakeholders including policymakers, NGOs, educators, disability-group leaders, and students with physical disabilities; Upper West Region, Ghana) identifying strategies to promote inclusive school WASH access for students with physical disabilities. Documents genuine legal-institutional content: the UN Convention on the Rights of Persons with Disabilities as a normative baseline; Ghana's Inclusive Education Policy existing 'on paper' without implementation resources per stakeholder testimony; and a participant-proposed roadmap of punitive measures to sanction authorities/supervisors who deliberately deny students with disabilities access to WASH facilities. MMAT (Mixed Methods Appraisal Tool).",
    "RF35F2E5A319B": "Extracted as S569. Karim, Mohinuzzaman, Rafa, Uddin, Hosen & Ahmed (2024), mixed-methods study (150-household structured questionnaire survey, 7 key-informant interviews, 4 focus group discussions, transect walks, Noakhali Pourashava, Bangladesh) applying shit flow diagrams (SFD), city service delivery assessment (CSDA), and SWOT analysis to citywide sanitation governance. Documents genuine legal-institutional content: Bangladesh's National Strategy for Water Supply and Sanitation (2014) and its lack of any reference to fecal sludge management (FSM); CSDA-scored institutional/regulatory/financing gaps across off-site versus on-site sanitation policy domains; and named institutional actors (WASA, DPHE, Noakhali Pourashava, UNDP) addressed via key-informant interviews on statutory and regulatory responsibility gaps. MMAT (Mixed Methods Appraisal Tool).",
    "R78F5B66C5C9F": "Extracted as S570. Coultas et al. (2022), qualitative multi-case study (participatory case-study development combining Most Significant Change and outcome-harvesting methods; 18 key-informant interviews in Nyamagabe District, Rwanda, 13 in Siaya County, Kenya, plus document review and Moyo District, Uganda progress-report review; three participatory online analysis workshops) examining sub-national government leadership for sanitation programming across Kenya, Rwanda, and Uganda. Documents extensive genuine legal-institutional content directly on point for the review's 'legal last mile' framework: each country's constitutional/statutory decentralisation architecture assigning sanitation-provision mandates to specific sub-national tiers (Kenya counties, Rwanda/Uganda districts); Siaya County's governor's signed financial-commitment letter binding budget allocation to sanitation activities; Moyo District's mandatory linkage of livelihood-programme benefits to toilet ownership/use; and Rwanda's Human Security Issue Taskforce and district WASH investment-plan institutionalisation. CASP Qualitative Studies Checklist (qualitative).",
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
