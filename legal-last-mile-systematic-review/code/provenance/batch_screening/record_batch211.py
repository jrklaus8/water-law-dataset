#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R41AA7F6D888B": "Jimenez, Cortobius & Kjellen 2014 (Water International) systematic literature review of 185 peer-reviewed articles on water, sanitation, hygiene and indigenous peoples. Unlike Novotny et al. (Batch 209, excluded E01 as institutional factors were a minor 4.4% subcategory), legal/institutional content here is a central, substantial organizing theme, not a minor subcategory: a dedicated 'Legislative frameworks and indigenous rights' category (18/185 articles) synthesizes international legal instruments, domestic recognition of indigenous water rights, joint management agreements (e.g., New Zealand's Waikato River Settlement co-management model), and pluralistic legal systems reconciling customary/statutory law; the 'Planning, participation and traditional knowledge' category (81/185) further documents institutional-governance mechanisms (adaptive governance, hybrid governance institutions, deliberative tools) shaping indigenous peoples' water/sanitation access, alongside a direct WaSH-service-access results section identifying tariff-system barriers specific to indigenous communities. Qualifies as a systematic empirical synthesis directly addressing legal/institutional mechanisms' effect on water/sanitation access for a specific marginalized population, per INCLUSION_EXCLUSION.md criterion 3.",
    "R41CA30F1CDC0": "Alda-Vidal, Kooy & Rusca 2018 (Urban Geography) qualitative empirical study (38 semi-structured interviews with Lilongwe Water Board employees, participant observation, four months of fieldwork, 2014) documenting how utility staff's everyday administrative/operational maintenance practices produce differential water-supply continuity and quantity outcomes between low-income areas/informal settlements (kiosk-served) and high-end residential areas (in-house connections) within the same nominally 'connected' centralized network in Lilongwe, Malawi. A genuine institutional/administrative-practice mechanism study with a documented differential-access outcome for poorer areas within an ostensibly universal service network.",
    "R4298BDB00D8D": "Haglund 2014 (Water Policy) qualitative case study based on historical/archival data and 40 semi-structured key-informant interviews (lawyers, litigants, judges, water/sanitation experts, public administrators, activists) examining how legal adjudication through Brazilian courts, with the Ministerio Publico (Public Prosecutor's Office) as a key rights-based advocate, is reshaping water/sanitation governance and access equity in metropolitan Sao Paulo. A genuine institutional/legal mechanism (litigation-based rights advocacy) study documenting effects on water/sanitation service access equity, closely following the Hoogesteger (S1043, Batch 210) legal-advocacy-mechanism precedent.",
}

EXCLUDES = {
    "R411507C514D3": ("E03", "McDonald & Jones 2018 (American Journal of Public Health) multivariable logistic regression study (n=58,018-59,595 US counties, 2011-2015) finding county-level race/ethnicity and socioeconomic covariates (notably proportion uninsured) predict initial and repeat Safe Drinking Water Act violations. The exposure/outcome is water-quality regulatory-compliance violations experienced by already-connected community water systems, not a legal/institutional mechanism's effect on water-service access, connection, or affordability. Wrong exposure -- water-quality-only study."),
    "R4142F316A241": ("E06", "Baffrey & Adis 2012 (Water Practice & Technology) practitioner case study authored by Manila Water Company's own Wastewater Operations Department staff, narrating the technical/operational strategies (communal septic tank upgrades, septage management, combined sewer-drainage systems, power-efficiency improvements) used to expand sewerage coverage in Metro Manila's East Zone after 1997 privatization. Primarily an engineering/operational-strategy case study; no isolated legal/institutional eligibility or access-barrier mechanism is analyzed. Engineering-only study."),
    "R41631C8B1BBE": ("E01", "Wong & Sharp 2009 (Environmental Politics) single case study proposing a 'subjectivity-institution-structure' theoretical framework for environmental citizenship, applied to social-housing tenants subjected to an imposed sustainable water-management/innovation project in north-west England. Concerned with power dynamics in citizen participation in environmental-technology adoption, not with a legal/institutional eligibility or barrier mechanism's differential effect on water/sanitation service access. Wrong-topic environmental-citizenship/participation-theory study."),
    "R41D39ACE327D": ("E12", "Belzer 2020 (Journal of Benefit-Cost Analysis) normative regulatory-design essay arguing USEPA should redefine Safe Drinking Water Act 'economic feasibility' as marginal-benefit-exceeds-marginal-cost rather than the current 'affordability' doctrine (2.5% of national median household income), critiquing the inequities of the current doctrine for rural/low-income communities. A conceptual/normative benefit-cost-theory argument and regulatory-design proposal; no original empirical data collection on actual household-level access or affordability outcomes. Conceptual/normative essay, no original empirical data."),
    "R43232F8A444B": ("E01", "McFarlane 2008 (International Journal of Urban and Regional Research) historical/discursive political-ecology analysis of sanitation infrastructure 'governmentality' in colonial (1850s-1860s) and post-colonial (contemporary) Bombay/Mumbai, examining discourses of the 'contaminated city,' bourgeois environmentalism, and 'world city' framings. Primarily a discursive/theoretical analysis of governmental rationalities and urban political ecology, not an empirical measurement of a specific institutional/legal eligibility mechanism's differential household-access effect. Extends the Neri Serneri (S39990BF4F869, Batch 210) macro-infrastructure-history exclusion precedent. Wrong-topic discursive/governmentality history."),
    "R44AC6ADF1E28": ("E01", "Cole 2014 (Journal of Sustainable Tourism) multi-method stakeholder-mapping study of tourism-driven water scarcity in Bali, Indonesia, identifying government as the primary legal duty-bearer for water provision and examining why/how tourism businesses should conduct human-rights due-diligence impact assessments. Fundamentally a tourism-industry water-resource-competition and business-advisory/CSR study (what tourism businesses should do), not an empirical study of a legal/institutional mechanism's effect on a household water/sanitation SERVICE-access outcome; extends the Abers & Keck (Batch 209) water-RESOURCE-governance-vs-water-SERVICE-access distinction. Wrong-topic resource-competition/business-advisory study."),
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
    assert len(INCLUDES) + len(EXCLUDES) == 9
    decided, _ = process_db()
    assert len(decided) == 9
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 211 processed: {n_inc} includes, {n_exc} excludes (1 record left undecided: R430C429810BF).")
