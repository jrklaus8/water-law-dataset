#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "RAF735D6E9B6F": "Rusca, Boakye-Ansah, Loftus, Ferrero & van der Zaag 2017 (Geoforum) interdisciplinary political ecology of drinking water quality in Lilongwe, Malawi. Documents that the Waterworks Act (1995, s.12.16a) grants the Lilongwe Water Board legal authority to disconnect/withhold water, and that infrastructure investment, maintenance response times, and water-quality monitoring are systematically prioritized toward higher-income in-house-connection areas over low-income kiosk-served areas -- a legal/institutional mechanism (utility governance decisions plus statutory disconnection authority) directly producing documented, measured (microbiological/physico-chemical) differential water access/quality by income area. Extends the Bakker/Kooy Jakarta institutional-governance-failure precedent (S1000, Batch 198) and the colonial urban-planning-legacy precedent (Kooy & Bakker S1001, Batch 198): Lilongwe's dual in-house/kiosk network traces to the post-colonial 'garden city' planning project that segregated low-income areas.",
    "R2BB90F5F4034": "Matsinhe, Juizo, Macheve & dos Santos 2008 (Physics and Chemistry of the Earth) regulation of formal and informal water service providers in peri-urban Maputo, Mozambique. Documents the institutional/legal framework (1998 delegated-management decrees creating FIPAG and CRA, the lease contract between FIPAG and private operator AdeM) and its explicit non-extension to informal small-scale independent providers (SSIPs) and household water resellers, who serve 32-45% of surveyed peri-urban residents -- a lack of legal/regulatory status directly tied to documented unregulated pricing (unconnected consumers pay ~3x more per m3) and unprotected service quality for the peri-urban poor. Extends the established Chidya et al Malawi Water Works Act/informal-provider precedent (R330A544EACCE, S991, Batch 196).",
    "R2A58025F1A28": "Torres-Rouff 2006 (Pacific Historical Review) historical case study of water use, ethnic conflict, and infrastructure in nineteenth-century Los Angeles. Documents the legal transition from Spanish/Mexican communal pueblo water rights to U.S. individual-property-rights doctrine, and the specific legal/administrative mechanisms (city-council ordinances, special-assessment funding requiring landowner petition -- which structurally excluded the renter-majority Mexican and Chinese neighborhoods -- versus eminent domain and general-fund financing used elsewhere) that produced documented, mapped disparities in sewer/pipe infrastructure access by ethnicity through 1891. A strong Family C (legal/administrative-barrier) case directly analogous to the colonial/postcolonial institutional-legacy precedent line (Njoh & Akiwumi S969; Kooy & Bakker S1001).",
}

EXCLUDES = {
    "RB1114E2BF515": ("E01", "Fisher 2008 (Development) 'Politics and Urban Water Supply' -- discourse/media analysis of the privatization-legitimacy debate over Bohol Water Utilities Inc. in Tagbilaran, Philippines (court cases on rate legitimacy, an unimplemented 2004 executive order against disconnections, and buy-back election politics). While regulatory/legal instruments (NWRB permitting, the disconnection executive order) are discussed, the paper's focus and evidence are the political rhetoric and media framing of the privatization debate as an election issue, not a documented analysis of differential water-access outcomes tied to legal/institutional status. General institutional-politics narrative without an access-inequality mechanism analysis, per the Fisher/Nallathiga precedent line."),
    "R1757CC18E1BA": ("E01", "Derman & Ferguson 2003 (Human Organization) political ecology of Zimbabwe's Water Act 1998 and National Water Authority Act 1998, focused on catchment/subcatchment council water-permit allocation among commercial farmers, communal-area farmers, and miners (irrigation/agricultural/mining water rights, the priority date allocation system, and the user-pays principle). This is a basin/catchment-scale water-RESOURCE-allocation and irrigation-rights governance study, not a household domestic water-access study -- reapplying the established Andersen 2016 Peru (Batch 195) / Kumasi et al Barekese catchment (Batch 193) E01 precedent."),
    "R15F48C29794A": ("E01", "Clark & Mondello 2003 (International Journal of Public Administration) theoretical/mathematical economic model (real-options, stochastic calculus) of delegation-contract auto-regulation between French municipalities and private water operators. Purely a contract-design/pricing-efficiency model with no empirical data on any social group's differential water access; extends the general institutional-reform/contract-design E01 precedent (Pinto/Da Cruz/Marques Portugal PPP, Batch 198; Herrala & Haapasalo Finland, Batch 194)."),
    "R29B8BB54C7ED": ("E06", "Sutton 2017 (Waterlines) technical/programmatic review of sub-Saharan rural water-supply coverage trends and the cost-effectiveness case for supporting household Self-supply (traditional wells) alongside community water supply to reach 2030 SDG targets. Financial/technical planning and infrastructure-cost-benchmarking analysis (life-cycle costs, population density, per-capita subsidy figures); no legal/institutional-mechanism analysis of access inequality. Reapplies the established E06 technical/financial-planning precedent (Hamed & Sannen Fayoum Egypt, Batch 194)."),
    "RB2CF65098BEF": ("E06", "Estache & Iimi 2011 (Journal of Utility Pricing) econometric auction-theory analysis of (un)bundling strategies in public procurement of water-supply and sewage infrastructure construction contracts in developing countries -- examines bidder cost structure, scope diseconomies, and competition effects in tender design. Pure procurement/engineering-cost economics with no water-access-inequality outcome or legal/institutional mechanism governing household access; reapplies the established E06 technical/efficiency precedent."),
    "R1B5292F08080": ("E01", "Mitra 2008 (Development) Foucauldian policy-discourse analysis of the World Bank-funded KUWASIP 24x7 pilot water project in Hubli-Dharwad, Karnataka, India -- examines competing 'lifestyle' vs 'lifeline' narratives, unaccounted-for-water (UFW) framing, and local governance-trust building. While it notes that targeting non-revenue water could disproportionately affect slum/unregularized-colony standpost users, the paper provides no documented empirical analysis of differential access outcomes tied to a specific legal/institutional mechanism -- it is a discourse/narrative case study of policy framing. Reapplies the established discourse/narrative-analysis E01 precedent (Fisher Tagbilaran, this batch; Ching et al Kathmandu, Batch 196)."),
}

WRONG_FILE = {
    "R162B7F22CF42": (
        "Amplifying the Poverty-Alleviation Impacts of Water Infrastructure Investments in Sub-Saharan Africa",
        "Pu, Christine Jiarui",
        "2024",
        "Google Drive/Antigravity retrieval delivered the wrong file: target record is 'Amplifying the Poverty-Alleviation Impacts of Water Infrastructure Investments in Sub-Saharan Africa' (Pu, Christine Jiarui, 2024), but the delivered PDF is an entirely different publication -- 'Drought tolerant maize for farmer adaptation to drought in sub-Saharan Africa: Determinants of adoption in eastern and southern Africa' by Monica Fisher, Tsedeke Abate, Rodney W. Lunduka, Woinishet Asnake, Yoseph Alemayehu & Ruth B. Madulu, Climatic Change (2015) 133:283-299, DOI 10.1007/s10584-015-1459-2 -- confirmed via full-text read (different authors, different journal, different year, unrelated topic: drought-tolerant maize adoption determinants, not water infrastructure). Not screened, not moved. Needs re-retrieval of the correct Pu 2024 article.",
    )
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
    touched = set(INCLUDES) | set(EXCLUDES) | set(WRONG_FILE)

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
        elif rid in WRONG_FILE:
            _, _, _, detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
        elif rid in touched:
            raise AssertionError(f"unexpected duplicate handling for {rid}")

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
            "doi": row["doi"],
            "exclusion_reason": row["exclusion_reason"],
            "exclusion_reason_detail": row["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(EXCLOG_PATH, fieldnames, rows)


if __name__ == "__main__":
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 10
    decided, _ = process_db()
    assert len(decided) == len(INCLUDES) + len(EXCLUDES)
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 199 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
