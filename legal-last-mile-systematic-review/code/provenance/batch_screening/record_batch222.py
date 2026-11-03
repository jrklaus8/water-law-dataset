#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R737AA21A56E8": "Debbane & Keil 2004 (Space and Polity) comparative case study of urban water environmental justice in Toronto, Canada and Hermanus, South Africa. Documents the Greater Hermanus Water Conservation Programme's tiered tariff structure, in which Zwelihle (poor) residents 'have not had access to' the lower/indigent tariff subsidy for which the majority qualify, and finds that strict credit-control mechanisms led to about 60% of Zwelihle residents being affected by water cut-offs due to accruing arrears -- while the same tariff structure generated a 20% revenue surplus during peak holiday season for the municipality. A rigorous institutional/legal mechanism case study directly documenting a tariff/credit-control mechanism producing differential water-service disconnection outcomes by income and geography.",
    "R76BD2052C008": "Prokopy 2009 (Journal of Development Studies) quantitative study (45 villages, rural India) of determinants and benefits of household-level participation (meeting attendance, capital-cost contribution) in community-based rural drinking-water projects. Using propensity score matching, finds that capital-cost contribution is associated with significantly higher water-improvements-index outcomes (encompassing distance to source, collection time, reliability, quality, pressure, adequacy and perceived access) and satisfaction, with no evidence of elite capture (both poor and wealthy households benefit). A rigorous quasi-experimental study directly isolating a participatory/administrative institutional mechanism's causal effect on a composite water-access outcome.",
    "R7814DEF7ACC8": "Wu & Malaluan 2008 (Urban Studies) natural-experiment comparative case study of the two water concessionaires (Maynilad, Manila Water) operating under identical concession-contract terms in Metro Manila following the 1997 MWSS privatization. Documents each concessionaire's 'Water for the Community' programme -- institutional mechanisms for extending service via shared/bulk connections and community-entry-point billing to low-income areas -- finding the two concessions increased connections by 30% in their first five years (a feat that would have taken MWSS 30 years at its historical rate), with much of that expansion occurring in economically distressed areas, and that Manila Water's territory-management structure achieved markedly better non-revenue-water reduction (58%->35%) than Maynilad's system-wide approach (64%->69%). A rigorous natural-experiment institutional-arrangement study directly documenting differential water-access-expansion outcomes for the poor attributable to internal corporate-governance/management-model differences under an identical external regulatory and contractual framework.",
    "R75D9E25CA71A": "Franceys & Weitz 2003 (Journal of International Development) empirical study of 20 case studies across 10 Asian countries (including focus-group discussions with low-income slum residents) investigating public-private-community partnership institutional arrangements for extending water, sanitation and solid-waste service to the urban poor. Documents specific institutional/legal mechanisms across cases: waiver of land-title requirements for water connections (Maynilad's Bayan Tubig programme), installment-based connection-fee payment plans (Palyja, Jakarta: 12 monthly installments), group-tap/shared-connection schemes requiring formal registration, and community-managed master-connection arrangements. A rigorous multi-country comparative case-study analysis directly documenting formal eligibility, fee-structure and connection-requirement mechanisms shaping water/sanitation access for the urban poor.",
    "R78C1CB0A4FC9": "Trepied 2012 (Social Identities) ethnographic case study of a 2004 political conflict in the commune of Kone, New Caledonia, between FLNKS-elected municipal officials and the customary Council of Elders of the Kanak tribe of Neami over the Adduction d'eau potable Grombaou water-conveyance project. Documents that the pipeline, sourced from Neami's own territory, was planned to bypass Neami and serve three other tribes first (based on their more urgent drought-driven need), triggering a customary-authority protest and negotiated resolution. A genuine institutional/political case study documenting how municipal water-infrastructure sequencing decisions, contested through customary Indigenous governance structures, determine which communities receive water-service connections and in what order.",
}

EXCLUDES = {
    "R76E257E7F829": ("E12", "Kooy, Furlong & Lamb (International Development Planning Review), explicitly labeled 'Viewpoint,' a conceptual essay proposing how Nature Based Solutions (NBS) principles could be adapted to address water vulnerability in Asian cities, drawing on examples from other published studies (Jakarta, Ghaziabad) rather than original fieldwork by these authors. A conceptual/opinion viewpoint article with no original empirical data collected by the authors; extends the established review/conceptual-paper exclusion precedent (Aiyer 2007; Wutich et al. 2021, Batch 221)."),
    "R771D41BC1584": ("E05", "Muller 2003 (Journal of International Development), 'Public-Private Partnerships in Water: A South African Perspective on the Global Debate,' a policy-advocacy essay authored by the Director-General of South Africa's Department of Water Affairs and Forestry, defending the department's PPP policy against critics and describing South Africa's free-basic-water and cost-recovery framework in narrative terms. A first-person policy-opinion/debate essay by the responsible government official, with no independent empirical research methodology, case study design, or data collection; matches exclusion code E05 (no empirical evidence)."),
    "R79CD54BC24BE": ("E01", "Ioris 2007 (Capitalism Nature Socialism), 'The Troubled Waters of Brazil: Nature Commodification and Social Exclusion,' a political-ecology critique centered on the Paraiba do Sul River Basin's industrial water-resource management, pollution control, and electricity-tariff commodification, with only a brief, non-specific passing reference to favela water-service exclusion unsupported by documented institutional-mechanism detail. A water-RESOURCE/political-economy critique, not a specific household water-SERVICE access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction."),
    "R77C65607B9D2": ("E12", "Subramaniam & Williford 2012 (Sociology Compass), 'Contesting Water Rights: Collective Ownership and Struggles against Privatization,' explicitly stating 'We review scholarly work to focus on four main aspects' of water-rights struggles, concluding with proposed future research questions. A literature-review article synthesizing existing scholarship with no original empirical data collected by the authors; extends the established review-paper exclusion precedent (Aiyer 2007; Gero et al. 2014, Batch 220)."),
    "R79A39D631DB8": ("E01", "Van Vugt & Samuelson 1999 (Personality and Social Psychology Bulletin), a field study and scenario study examining the effect of personal water metering on conservation behavior during a UK water-shortage crisis, framed as a social-dilemma/social-psychology analysis. A behavioral/consumption-conservation study concerning already-connected households' water-use response to metering, not a legal/institutional water-access eligibility mechanism study; extends the established water-demand/consumption-behavior exclusion precedent (Agthe & Billings 1987, Batch 220)."),
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
    print(f"Batch 222 processed: {n_inc} includes, {n_exc} excludes.")
