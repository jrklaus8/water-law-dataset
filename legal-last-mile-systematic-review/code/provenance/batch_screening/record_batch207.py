#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R2E81D8F6358D": "Nastar 2014 (Cities) comparative case study examining government 'world city' development-plan rhetoric versus documented water-access reality in Johannesburg, South Africa and Hyderabad, India. Analyzes government initiatives inspired by world-city visions and demonstrates a documented disparity in water access, arguing that the promises of city development plans for social integration and 'world-class' service provision have not been fulfilled for the urban poor, while opening new avenues for wealth accumulation among financial/political elites. A comparative institutional-policy case study documenting a specific urban-development-strategy mechanism's differential water-access effects.",
    "R309188806D95": "Russ & Takahashi 2013 (Urban Studies) logistic-regression study (survey n=300) of the Ahmedabad Slum Networking Project (SNP), a municipal-NGO-community infrastructure partnership in India, examining predictors of resident complaints about specific public services including water. Finds that institutional redress-seeking mechanisms significantly predict water-complaint outcomes: contacting the municipal corporation (amc_com, OR=0.60, p<0.05) and contacting an NGO (ngo_com, OR=0.56, p<0.05) are both associated with reduced odds of water complaints, alongside area wealth (OR=0.07, p<0.01) and distance from central municipal offices (OR=1.44, p<0.10). A genuine regression-based estimate directly isolating institutional/administrative redress mechanisms' effects on a water-service outcome within a specific slum-upgrading infrastructure programme; qualifies for effect_sizes.csv under the Family C framework.",
    "R32B0F0E2A2CA": "Galaa & Bukari 2014 (Development in Practice) case study of a Tri-Water Sector Partnership (TWSP) -- comprising the Ghana Water Company Ltd (GWCL), private-sector development practitioners, and community water boards -- established in 2007 along the Dalun-Tamale corridor in northern Ghana to resolve water-tariff payment conflicts. Documents how the TWSP's combination of modern and indigenous conflict-resolution approaches, including the institution of chieftaincy, achieved positive mediation of water-tariff conflicts and improved payment compliance, contrasted with the prior conflict-ridden arrangement in which local communities' perceived ownership of the water source clashed with GWCL's cost-recovery mandate.",
}

EXCLUDES = {
    "R2B97C2298327": ("E01", "Chappells, Medd & Shove 2011 (Social & Cultural Geography) qualitative study of household gardening practices and routines during the 2006 UK drought. Examines domestic behavioral/practice dynamics around garden watering during water scarcity; no legal/institutional eligibility, permitting, or tariff mechanism producing documented differential household water-access outcomes. Reapplies the established drought-resilience/household-practices E01 precedent (Chappells & Medd, Batch 206)."),
    "R6230EBC4E809": ("E12", "Kobayashi, Syabri, Ari & Jeong (eds.), 'Community Based Water Management and Social Capital' -- a full multi-chapter edited book compiling numerous distinct case-study chapters by different authors across different countries. Not screenable as a single coherent original empirical study at the record level; individual chapter content, if relevant, is not extractable from a single undifferentiated record. Wrong study design/format for record-level screening."),
    "R2CF326CC85CB": ("E01", "Ferro, Romero & Covelli 2011 (Utilities Policy) stochastic-frontier econometric study estimating technical production efficiency of water and sanitation utilities across 16 Latin American countries (ADERASA survey data, 2003-2008). A utility operational-efficiency/production-benchmarking study; the outcome is technical efficiency of water production (dispatched water volume relative to labor/capital inputs), not household-level differential water-access outcomes tied to a specific legal/institutional eligibility or barrier mechanism. Reapplies the established governance/efficiency-benchmarking E01 precedent."),
    "R30DC77EED2DA": ("E01", "Gomez-Temesio 2019 (Critique of Anthropology) reflexive ethnographic-methodology essay on the author's embodied and emotional experience of apprenticing with corrupt water-ministry street-level bureaucrats in Senegal. Per its own framing, the article 'addresses ethnography not only as a method but as a positionality'; its core contribution is methodological/phenomenological reflection on the ethnographer's own feelings rather than a rigorous documented account of institutional corruption's measured effect on differential water access. Wrong-topic reflexive-methodology essay."),
    "R04FDCEFB8D34": ("E01", "Khan & Yang 2014 (Science of the Total Environment) institutional-stakeholder-opinion survey study of arsenic-contamination mitigation measures and challenges in Bangladesh. Focus is on water QUALITY (arsenic contamination) and stakeholder opinions on technical/institutional mitigation options, not a legal/institutional mechanism producing documented differential household water-access outcomes. Wrong-topic water-quality/contamination-mitigation study."),
    "R07BEDF2412B5": ("E01", "Moretto 2015 (Habitat International) study adapting and applying the UN-Habitat 'Urban Governance Index' governance-assessment tool to water service co-production arrangements in Venezuela, critiquing the index's ability to capture informal governance arrangements. A governance-assessment-tool critique/application study; reapplies the established governance-benchmarking-tool-application E01 precedent (cf. Okumura Rio de Janeiro City Blueprint, Batch 201; Chang et al China City Blueprint, Batch 202)."),
    "R33DFBC17F664": ("E12", "Castro 2007 (Journal of Comparative Social Welfare), a self-labeled 'Overview Article' providing a conceptual sociological exploration of global trends and systemic conditions affecting water and sanitation service universalisation. Conceptual/synthesis overview article with no original empirical data collection; wrong study design, reapplying the established literature-review/synthesis E12 precedent (Mugagga & Nabaasa, Batch 206)."),
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
    print(f"Batch 207 processed: {n_inc} includes, {n_exc} excludes.")
