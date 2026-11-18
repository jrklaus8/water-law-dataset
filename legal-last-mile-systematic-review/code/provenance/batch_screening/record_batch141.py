import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

ids = [
    "R32CC5C530F76", "R33B987ACF787", "R2BEFD559FD67", "R2EE2734753C2",
    "R3A5206FB2852", "R39FC015AF6E0", "R2CD3ADF81E21", "R29F08D523D16",
    "R2829FD9C762C", "R26A228051D15",
]
for rid in ids:
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# ---- INCLUDES ----

r = by_id["R32CC5C530F76"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Institutional/legal case study of Spanish urban water privatization, covering the "
    "municipal concession regime, AGBAR's expansion, and the 'Barcelona Water War' of the "
    "1990s -- a documented legal dispute over water taxation in which four families won a "
    "Higher Court of Catalonia ruling requiring prices to account for household size, and "
    "~80,000 families withheld tax portions of their bills as fiscal objection. Reports "
    "coverage/pricing outcomes by ownership model (49% private / 32% public / 12% PPP "
    "nationally). Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S694."
)

r = by_id["R2BEFD559FD67"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Qualitative institutional case study of water utility pricing-setting practices in "
    "Lilongwe, Malawi, documenting how formal and informal negotiations over subsidies, "
    "tariff increases and profit distribution within two service modalities produce uneven "
    "water pricing/access regimes, with poor urban dwellers paying more for lower-quality "
    "service. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S695."
)

r = by_id["R3A5206FB2852"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Large-N panel regression study (112 developing countries, 1991-2010) testing how "
    "political regime type (democratization) interacts with industrialization pressure to "
    "shape urban-rural clean-water-access allocation by government; finds rural areas are "
    "disadvantaged under industrialization in non-democracies, and that foreign aid "
    "accentuates pro-urban bias in industrializing non-democracies. Direct institutional/"
    "political mechanism (regime type) tied to a water-access outcome with regression "
    "estimates. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S696; "
    "regression results checked for effect_sizes.csv eligibility during extraction."
)

r = by_id["R39FC015AF6E0"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Meta-analysis synthesizing evidence on the effectiveness of bottom-up (NGO/CBO-led) "
    "service-delivery approaches for improving urban-poor access to water, sanitation and "
    "electricity, across the specific access dimensions of connectivity, affordability, "
    "adequacy and effort/time; finds no significant average effect except where active "
    "community participation is present. This is itself a secondary quantitative synthesis "
    "(study_design_class = systematic_review_secondary per established convention), not an "
    "independent primary observation for pooling. Included per INCLUSION_EXCLUSION.md "
    "criteria 1-9. Extracted as S697; not added to effect_sizes.csv (secondary synthesis, "
    "per established project convention excluding meta-analyses/systematic reviews from "
    "independent pooling)."
)

r = by_id["R2CD3ADF81E21"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Historical-institutional case study of the Kumbo Water Authority, Cameroon: in 1991 the "
    "community forcibly expelled the national water corporation and took over piped-water "
    "provision, claiming community ownership. Using archival evidence against the popular "
    "'community management' narrative, documents the political context/consequences of this "
    "state-to-community institutional transition and shows commodification of water "
    "accelerated afterward. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as "
    "S698."
)

r = by_id["R2829FD9C762C"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Empirical case study of common property resource management (CPRM) governing access to "
    "land and water in the Zamfara Forest Reserve, northwest Nigeria, documenting the "
    "relationship between traditional/customary access rights and present-day practices "
    "across different pastoralist user-groups and stakeholders. Included per "
    "INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S699."
)

r = by_id["R26A228051D15"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Empirical study (principal-agent framework, gender lens) of the impact of Tanzanian "
    "decentralisation reforms on service users' participation in decision-making for water "
    "and health service delivery at the village level; finds decentralization created "
    "participation spaces but men gained more leverage than women, with strategic gender "
    "needs left largely unaddressed. Included per INCLUSION_EXCLUSION.md criteria 1-9. "
    "Extracted as S700."
)

# ---- EXCLUDES ----

exclusions = [
    dict(
        rid="R33B987ACF787",
        title="The value of scarce water: Measuring the inefficiency of municipal regulations",
        authors="Mansur, Erin T; Olmstead, Sheila M",
        year="2012",
        code="E01",
        detail=(
            "Welfare-economics analysis comparing command-and-control drought rationing to "
            "market-based pricing for urban water demand management, using panel data on "
            "already-connected households in 11 North American cities; estimates price "
            "elasticities and welfare/efficiency gains from switching to a market-clearing "
            "drought price. No legal/institutional access-barrier or exclusion mechanism is "
            "examined -- the object of study is demand-management policy efficiency among "
            "connected households, not who gains or loses access. Fails inclusion criterion 4."
        ),
    ),
    dict(
        rid="R2EE2734753C2",
        title="Environmental Justice and the Politics of Risk: Water Resource Controversies in Taiwan",
        authors="Fan, Mei-fang",
        year="2016",
        code="E01",
        detail=(
            "Macro-level environmental-justice case study of the Tseng-Wen Reservoir "
            "Transbasin Water Diversion Project, examining EIA process exclusion of an "
            "indigenous (Bunun) community from decision-making over a water-transfer "
            "megaproject. No household-level water/sanitation service-access outcome is "
            "examined; the object of study is environmental/procedural justice in resource-"
            "allocation and infrastructure-siting decisions. Extends the established "
            "macro-water-resource-project exclusion precedent (cf. Banerjee 2001). Fails "
            "inclusion criteria 1 and 4."
        ),
    ),
    dict(
        rid="R29F08D523D16",
        title="All That Glitters Is Not Gold; Resettlement, Vulnerability, and Social Exclusion in the Pehuenche Community Ayin Mapu, Chile",
        authors="González-Parra, Claudio; Simon, Jeanne",
        year="2008",
        code="E01",
        detail=(
            "Case study of indigenous resettlement following hydroelectric dam construction; "
            "potable water and a sewage system are mentioned only as two incidental material "
            "improvements among many (new house, electricity, land, agricultural loans) in a "
            "broader compensation package. The paper's actual object of study is social and "
            "cultural disarticulation, community atomization and loss of self-determination, "
            "not water/sanitation service access. Extends the established resettlement/"
            "compensation-study exclusion precedent (cf. Agnihotri 2008). Fails inclusion "
            "criteria 1-2."
        ),
    ),
]

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

for ex in exclusions:
    r = by_id[ex["rid"]]
    r["full_text_status"] = "retrieved"
    r["full_text_location"] = "Google Drive (Antigravity retrieval batch)"
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["exclusion_reason"] = ex["code"]
    r["exclusion_reason_detail"] = ex["detail"]
    r["reviewer_1"] = REVIEWER

    ex_rows.append({
        "record_id": ex["rid"],
        "title": ex["title"],
        "authors": ex["authors"],
        "year": ex["year"],
        "stage": "full_text",
        "exclusion_code": ex["code"],
        "exclusion_reason_detail": ex["detail"],
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ex_fieldnames)
    w.writeheader()
    w.writerows(ex_rows)
os.replace(tmp, EXLOG)

print("Batch 141 recorded: 7 includes, 3 excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
