import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

includes = {
    "RE7ECD35103C3": "Extracted as S557. Qualitative institutional ethnographic case study (40 in-depth interviews with women peasant farmers, plus 8 project staff and 65 water-management stakeholder interviews, participant observation, and analysis of ~400 institutional documents, 2011 fieldwork) of a foreign-funded participatory Water User Association (WUA) project in 'Chaika' village, Uzbekistan. Documents genuine legal-institutional content: the Uzbek government's institutionalization of WUAs to organize village-level water management after decollectivization; 1994 formalization of individual household peasant-farm land rights (0.13 hectares, permanent and inheritable); private farmers' long-term state lease contracts requiring annual cotton/wheat quota submission at state-set prices with fines for shortfall; and 'community mobiliser' selection criteria (public visibility/authority, free time) that discursively and structurally excluded women -- the majority of household farmers -- from the WUA project despite their extensive unrecognized labor negotiating scarce irrigation-water access (walking kilometers to check canal flow, queuing, informal monitoring strategies) and self-organized water-user groups operating entirely outside the formal WUA structure. CASP Qualitative Studies Checklist (qualitative).",
    "RC61ECDAD14A5": "Extracted as S558. Qualitative case study (14 in-depth exploratory interviews with sugarcane/ethanol industry stakeholders, June-August 2012, plus additional interviews with an agricultural researcher and displaced small-scale-farming residents) of land and water access in the Valle del Cauca sugarcane region, Colombia, applying Ribot & Peluso's theory of access. Documents genuine legal-institutional content: Colombia's water-concession regulatory regime (Decree 1541/78, Agreement 042/2010) administered by the Cauca Valley Corporation (CVC), described by interviewees as captured by the sugar industry; the sugar industry holding 64% of surface-water and 88% of underground-water concessions in the Valle del Cauca (versus 26%/2% for household use) at lower rates than other users; industry lobbying to reclassify high-quality groundwater as non-potable specifically to free it from household-use protections for irrigation; and the Bonsucro multi-stakeholder certification's 'obey the law' land/water standard shown to legitimize this disproportionate access without addressing underlying inequitable distribution, weak land-title enforcement, or historical violent dispossession of peasant, indigenous, and Afro-Colombian communities. CASP Qualitative Studies Checklist (qualitative).",
}

reviewer = "Claude-AI-fulltext-2026-09-21"
changed = 0
for r in rows:
    rid = r["record_id"]
    if rid in includes:
        assert r["full_text_decision"] == "" and r["final_decision"] == "", f"{rid} already decided"
        r["full_text_decision"] = "include"
        r["final_decision"] = "include"
        r["reviewer_1"] = reviewer
        r["notes"] = includes[rid]
        changed += 1

assert changed == len(includes), f"expected {len(includes)}, got {changed}"

fd, tmp = tempfile.mkstemp(dir="02_screening/full_text")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, db_path)

print("done, db changed", changed)
