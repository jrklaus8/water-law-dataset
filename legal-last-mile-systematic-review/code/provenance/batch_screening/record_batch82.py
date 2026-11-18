import csv, tempfile, os

db_path = "02_screening/full_text/full_text_screening_database.csv"
log_path = "02_screening/exclusion_log/exclusion_log.csv"

with open(db_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

excludes = {
    "RBEBE0BACCD18": {
        "exclusion_reason": "E01",
        "exclusion_reason_detail": "Wagaba et al., study of small NGOs' access to geological/hydrogeological data for water-point siting and planning purposes in eastern Africa. The unit of analysis and concept of 'access' here is a practitioner/NGO organization's access to technical scientific data (borehole records, aquifer maps) for infrastructure-planning purposes -- an entirely different exposure and population than this review's target of household- or applicant-level legal-administrative access to water services. No legal-institutional water-rights, permitting, connection, or service-delivery content for households is examined.",
    },
    "RE8D979932979": {
        "exclusion_reason": "E01",
        "exclusion_reason_detail": "Blanchon, analysis of South Africa's 1998 National Water Act 'Reserve' mechanism (the statutory allocation of water for basic human needs and ecological/environmental flows), with an Orange River case study. The paper is a policy/hydrological-geography analysis of environmental-flow and river-basin allocation law, drawn from government hydrological reports and secondary academic sources with no original empirical data collection on households (no interviews, surveys, or fieldwork). The exposure examined -- statutory environmental-flow reservation for ecosystems and river basins -- is a different unit of analysis than this review's target of household-level legal-administrative water access; the paper does not examine applicant- or household-level access, permitting, or connection processes.",
    },
    "R81549C4709FC": {
        "exclusion_reason": "E01",
        "exclusion_reason_detail": "Two book chapters (Sherpa, 'Climate Change in Nepal through an Indigenous Environmental Justice Lens,' and Awale, 'Women, Water, and Weather: Kavre Villages Adapt to the Increasing Impacts of the Climate Crisis,' from an edited volume's Climate Justice section). Both are ethnographic/qualitative studies of climate-change adaptation, Indigenous Environmental Justice framing, and gendered climate-driven water scarcity coping strategies (rainwater harvesting, traditional pond networks, drip irrigation) in Nepal. Neither examines legal-administrative water access -- no water-rights law, permitting, utility connection, tariff, or institutional service-delivery content for households is discussed; the focus throughout is on climate-policy critique, Indigenous cosmology/spirituality, and climate-adaptation coping practices, a different topic than this review's household-level legal-administrative water access target.",
    },
}

includes = {
    "RD1E30397691A": "Extracted as S559. Boucher-Hedenström & Rutherford, 'Services d'eau et d'assainissement et dispersion «urbaine» dans le comté de Stockholm,' Flux 2010/1-2 n°79-80, pp.54-68. Qualitative case study (interviews with named municipal/regional officials including Bertil Rusk, Håkan Jonsson, and the Bureau de planification régionale) of water/sanitation service provision amid urban sprawl in Stockholm County, Sweden, with a Norrtälje municipality case study. Documents genuine legal-institutional content: Sweden's 2007 Water Services Act (Lag om allmänna vattentjänster) establishing municipal responsibility to provide water/sanitation service within a defined 'verksamhetsområde' (service area) and the cost-price (self-financing, no-profit) tariff principle; four distinct service-configuration types (A-D) ranging from full municipal connection to individual on-site solutions; an estimated ~90,000 Stockholm County households relying on individual/alternative (non-municipal) water and sanitation solutions outside the formal service area; municipal permit and connection requirements governing extension of the service-area boundary; municipal enforcement authority over substandard individual installations; and a mini-network (samfällighet) model requiring unanimous consent among neighboring households to jointly connect to the municipal network. CASP Qualitative Studies Checklist (qualitative).",
    "R1197785426F6": "Extracted as S560. Baron & Bonnassieux (2013), 'Gouvernance hybride, participation et accès à l'eau potable: Le cas des associations d'usagers de l'eau (AUE) au Burkina Faso,' Annales de géographie 2013/5 n°693, pp.525-548. Qualitative case study (field studies conducted under the ANR Sud II APPI research project, 2011-2014, in rural/semi-urban Burkina Faso) of hybrid water governance and the legal-institutional role of Water Users' Associations (AUE) following Burkina Faso's 2000 rural/semi-urban water-sector Reform and 2009 decentralization decree. Documents genuine legal-institutional content directly on point for the review's 'legal last mile' framework: the 2001 Water Law (Loi n°002-2001/AN) recognizing a right to water without specifying volumes; the 2009 decree transferring water-infrastructure ownership and management competence from the State to communes; AUE legal homologation/licensing criteria (30-80 members, gender parity, youth quotas, elected 6-member bureau); AUE's formal role fixing water tariffs, controlling point-of-service operators (fontainiers/gestionnaires de pompes), and mediating conflicts; delegation of AEPS (simplified water-network) management to private operators or associative structures via affermage contracts; and documented tension/exclusion dynamics (women and migrants marginalized from AUE decision-making despite bearing primary water-fetching labor) within this formal participatory governance structure. CASP Qualitative Studies Checklist (qualitative).",
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
