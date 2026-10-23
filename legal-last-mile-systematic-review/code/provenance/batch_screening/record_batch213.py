#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R4BCCFE408D51": "Sahu 2008 (Development) qualitative case study (interviews with 115 households, 4 villages, Nabarangpur and Jagatsinghpur districts, Orissa, India) of Pani Panchayat (PP), a statutory water-user-association institution created by the Orissa PP Act 2002 and Orissa PP Rules 2003 to transfer irrigation operation/maintenance to farmer institutions. Documents that access to water depends on paying capacity of users (fee-based) and that marginal farmers or landless cultivators who cannot afford operating-expense contributions are excluded from benefits of state capital spending on irrigation infrastructure, while elite/dominant members capture disproportionate benefits -- 'Under this situation PP excludes marginal groups.' A genuine legal/institutional mechanism (statutory WUA fee-based access, ill-defined property rights) with documented differential access-exclusion outcomes for marginal and landless households.",
    "R4E5E7EA9AF31": "Jacobs 1978 (Human Organization) case study (Social Impact Assessment for the US Bureau of Reclamation, Espanola Valley, New Mexico, 1975) of the acequia system -- a traditional Hispanic/Chicano irrigation-ditch legal-political institution governed by elected mayordomos, protected under the Treaty of Guadalupe Hidalgo (1848) -- threatened by top-down federal/state water-rights adjudication that would extinguish traditional farmers' inherited water rights and dissolve the acequia's dual role as water-management and local-governance institution. A genuine legal/institutional mechanism (water-rights adjudication vs. treaty-protected traditional water-governance institution) study documenting the threatened loss of water access/rights for a specific marginalized community.",
    "R4DCB1F867CA2": "Menon 2013 (Ethics and Social Welfare) theoretical-empirical case study of pavement-dwelling and squatter communities in Mumbai, documenting how legal citizenship-subject status ('citizen' vs. 'squatter') determines access to public infrastructure including water and sanitation -- pavement dwellers rely on illegal water connections procured through pre-election political patronage, pay informal vendors far above the municipal tariff (Rs. 30/month for 80-100 litres/day vs. 50 paise/1,000 litres for housed residents), and lack functioning access to public toilets. A legal/institutional mechanism (citizenship/legal-subject status determining infrastructure eligibility) study with documented differential water/sanitation-access and affordability outcomes for a marginalized urban population.",
    "R4D89B36E51A9": "Motiram & Osberg 2010 (Economic Development and Cultural Change) econometric study using the Indian Time Use Survey (1998-99) microdata, examining correlations between community/group-level social capital, land inequality, and caste with household water-collection burden and community-level water-supply organization in India, within a collective-action-problem model of water provision. Finds statistically significant correlations between social capital, land inequality, caste, and community water-supply outcomes (authors caveat these as correlational, not causal, given cross-sectional data). An institutional/social-structural mechanism (caste-based exclusion, social capital, land inequality) study of community water-provision organization with a documented water-collection-burden outcome.",
    "R4DBF12B4A327": "Isham & Kahkonen 2001/2002 (World Bank working paper) econometric study (OLS, multivariate probit, and IV/2SLS estimation; 288-381 households across 16-20 communities per site) of community-based rural water services in Sri Lanka and two Indian states (Karnataka, Maharashtra), finding household-level design participation and local decision-making significantly predict community design satisfaction (Table 4), and that community design satisfaction significantly predicts household-level water-collection time-savings (Table 3: Sri Lanka 1.63*, Karnataka 2.92***, Maharashtra 1.06***, log of household time-saving), with social capital shown (via IV estimation with community-activity instruments) to be a significant determinant of these service-level institutions. A genuine regression-based estimate directly isolating an institutional/participatory mechanism's (community design participation) effect on a water-access-relevant outcome (household water-collection time-savings); qualifies for effect_sizes.csv under the Family A framework.",
    "R4E8ECECC23D8": "Cheng 2013 (Environment and Urbanization) case study of Manila's two private water concessionaires' differentiated non-payment/revenue-recovery mechanisms, documenting that payment-recovery targeted at low-income consumers relies on increased policing and shifting responsibility onto communities/individuals, while payment recovery targeted at high-volume (wealthier) customers involves technical improvements and arrears settlement -- an asymmetric institutional/administrative-enforcement mechanism resulting in higher effective costs and continued under-visibility of the unserved/underserved poor despite aggregate coverage-improvement statistics. A genuine institutional/administrative-enforcement mechanism (differentiated non-payment policing) study with documented differential water-service-access and affordability outcomes between poor and non-poor consumers.",
}

EXCLUDES = {
    "R4D3FA2134902": ("E01", "Wong 2016 (Geoforum) case study of the Volta River Basin trans-boundary water governance committee (West Africa), examining how participatory governance structures built on traditional chieftaincy authority are vulnerable to elite capture and how quota-based gender-representation rules interact with old institutions to reinforce inequalities. A trans-boundary water-RESOURCE governance study (river-basin management committee), not a household water/sanitation SERVICE-access study, extending the Abers & Keck (Batch 209) water-resource-vs-water-service-access distinction. Wrong-topic water-resource-governance study."),
    "R4E68BD8F3368": ("E01", "Strauch & Almedom 2011 (Human Ecology) qualitative and quantitative study of traditional resource management (TRM) among the Sonjo people in rural northern Tanzania, comparing traditionally-managed and formally government-managed water sources for catchment forest protection and water QUALITY outcomes (bacterial water quality, seasonal variation). A water-resource-management and water-quality-comparison study; no legal/institutional eligibility or access-barrier mechanism affecting household water-service access is examined. Wrong-topic water-resource/quality-management study."),
    "R4D3EE9BBEA3C": ("E07", "Njeri, Moitui, Mberu & Simiyu (2026, Health Policy and Planning) Health Policy Triangle analysis (11 key-informant interviews, review of 20 policy instruments) of Kenya's national hand hygiene policy landscape, identifying fragmented policy presence, weak inter-sectoral coordination, and inadequate financing as governance barriers to hand hygiene (handwashing) practice. Hand hygiene is a distinct WASH sub-service (handwashing behavior/products) from water or sanitation service access per se; this is a policy-governance-gap analysis of hygiene promotion infrastructure, not a household water or sanitation SERVICE-access eligibility/barrier mechanism study. Wrong service."),
    "R4D3518D8ACB3": ("E12", "Aiyer 2007 (Cultural Anthropology) exploratory essay on the Plachimada community's struggle against a Coca-Cola bottling plant's groundwater extraction in Kerala, India, situating it within a broader political-economy analysis of transnational corporations, neoliberal globalization, and India's agrarian crisis. The author explicitly characterizes the piece as 'very exploratory and quite incomplete'; it is a conceptual/political-economy essay on corporate water-resource extraction and agrarian crisis, not an empirical study of a legal/institutional mechanism's effect on household water/sanitation service access. Conceptual/exploratory essay, not a rigorous empirical access-mechanism study."),
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
    print(f"Batch 213 processed: {n_inc} includes, {n_exc} excludes.")
