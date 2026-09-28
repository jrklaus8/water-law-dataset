import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "RC6B24320D282": {
        "exclusion_reason": "E06",
        "exclusion_reason_detail": "Single-house (N=1) building-code compliance survey of housing type 45 in Panorama Indah residence, Pekanbaru, Indonesia, assessed against the Indonesian Directorate General of Human Settlements 1986 housing-health standard. Water supply is one of six inspected physical criteria (lighting, ventilation, water supply, wastewater disposal, humidity, air pollution) in a single-dwelling engineering/health-code inspection, not a legal-administrative water-access mechanism study, and the population is a single house, not a study population.",
    },
}

includes = {
    "R55F012C376B7": "Extracted as S546. Mixed-methods study (350-household survey: 208 Damauli + 142 Tansen, plus FGDs) of water users' associations (WUAs) in municipal Nepal. Documents Nepal's legal framework (Constitution of Nepal 2015 Art 25(4); Essential Commodity Protection Act 1955; Water Resource Act 1992; Water Resource Regulation 1993; Drinking Water Regulation 1998; Nepal Water Supply Corporation Act 1989; Local Self Governance Act 1999) and concrete household-level access/burden mechanisms: NPR 50,000 new-connection cost, waits up to 11 years, paying double (NPR 100,000) to jump the queue, WUA-committee/private-repair-agency corruption and collusion, political capture of WUA committees, exclusion of women (taps registered only to male household heads; 6-7 hrs/day water collection in dry season), tanker-water costs (~Rs 357/1,000L), inequitable spring-water price hikes (NPR 20 to 80 per 6,000L), and larger WUAs buying out smaller committees' water sources. MMAT (mixed methods).",
    "REB0B1F68FC00": "Extracted as S547. Mixed-methods study (73 stakeholder interviews, incl. 42 household-level: 22 farmers, 10 fish farmers, 10 non-agricultural villagers; 7 villages/dusun; 1-month 2013 fieldwork) of adaptive water governance on Merapi volcano's southern slopes, Central Java, Indonesia. Documents genuine legal-institutional content: 1987 irrigation reforms and 1998/1999 decentralization (Indonesian Local Autonomy Act 1972 framework), the 'Turnover Program' transferring irrigation governance from Ulu-Ulu customary rights-holders to formal Water Users Associations (WUA) and WUA Federations, institutional pluralism/fragmentation across Ministry of Public Works, Ministry of Agriculture & Environment, regional water agencies (Perusahaan Daerah Air Minum), the Irrigation Committee, and informal Ulu-Ulu customary authorities -- producing documented coordination failures and an undelivered 2013 WUA subvention payment -- plus post-2010-eruption lahar damage to sabo-dams/irrigation canals causing drinking- and irrigation-water crises, unequal government emergency-water-tank distribution, and reliance on informal Gotong Royong mutual aid for canal repair. MMAT (mixed methods).",
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
