import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}
assert "S685" not in existing_ids

def blank_row(fieldnames):
    return {f: "" for f in fieldnames}

r = blank_row(fieldnames)
r.update({
    "study_id": "S685",
    "citation": "Sawchuk LA, Burke SDA, Padiak J (2002). A Matter of Privilege: Infant Mortality in the Garrison Town of Gibraltar, 1870-1899. Journal of Family History 27(4):399-429.",
    "doi": "10.1177/036319902236626",
    "publication_year": "2002",
    "publication_type": "journal article",
    "language": "English",
    "peer_reviewed": "TRUE",
    "country": "United Kingdom",
    "subnational_unit": "Gibraltar (British crown colony)",
    "legal_system": "common law (British colonial)",
    "urban_rural": "urban",
    "service_provider": "British colonial military administration (Governor/General Officer Commanding); Royal Engineers",
    "regulatory_model": ("1884 order by Governor Adye (following Governor Lord Napier's 1882 condenser "
                          "initiative) granting military personnel and their families free access to newly "
                          "installed condenser-distilled water, while civilians were required to pay (6 gallons "
                          "per penny) for the same water; formal military water-rationing schedule by rank "
                          "(commanding officers 7 gal/day; NCOs/rank and file/wives 2.5 gal/day; children 1 "
                          "gal/day)"),
    "population": "civilian and military-family populations of Gibraltar, 1870-1899",
    "sample_size": "full-population vital registration data, 1870-1899 (compulsory birth/death registration from 1869); n=15 annual IMR observations per group for KS test",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "legal_status": "TRUE",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "fees": "TRUE",
    "water_access": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "study_design": "historical demographic case study (primary vital-registration archival data, comparative inferential statistics)",
    "effect_measure": "Kolmogorov-Smirnov two-sample test",
    "effect_estimate": "Phase I (1870-1884): civilian IMR 171.6 vs. military IMR 156.5, KS=0.730, n=15, p=.66 (not significant). Phase II (1885-1899, post water-privilege policy): civilian IMR 160.4 vs. military IMR 124.2, KS=1.461, n=15, p=.028 (significant)",
    "extraction_sample_size": "15 annual observations per phase per group",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "legal_measurement_quality": "4",
    "outcome_measurement_quality": "4",
    "mechanism_certainty": ("High: the study documents, via primary vital-registration archival data and formal "
                             "inferential statistical testing, that a specific 1884 gubernatorial policy "
                             "decision - granting free condenser-distilled water to military families while "
                             "requiring civilians to pay per bucket, layered on a pre-existing formal military "
                             "rank-based water-rationing schedule - produced a measurable, statistically "
                             "significant divergence in infant mortality between the two populations beginning "
                             "in the period immediately following the policy's implementation, where none had "
                             "existed in the prior period. The natural-experiment structure (two populations "
                             "sharing identical housing quality, sanitary infrastructure, and physical "
                             "environment, differing only in legal/institutional status) makes this an unusually "
                             "clean historical test of a status-based water-access-privilege mechanism."),
    "source_document": "Sawchuk, Burke & Padiak 2002, Journal of Family History 27(4):399-429 (retrieved via Google Drive inbox)",
    "figure": "Figure 2 (infant mortality by group, 1870-99)",
    "page": "399-429",
    "section": "An Insufficient and Questionable Water Supply; Infant Mortality, 1885-1899",
    "exact_location": "Section on the 1884 Governor Adye condenser-water policy and its association with Phase II infant-mortality divergence",
    "extraction_note": ("Extracted from full-text PDF (retrieved via Google Drive inbox). Historical demographic "
                         "case study with an unusually clean natural-experiment design (shared environment, "
                         "differing only in legal/institutional military-vs-civilian status) directly testing a "
                         "documented 1884 colonial policy granting differential free water access by status, "
                         "with a real inferential-statistics outcome (Kolmogorov-Smirnov test on infant "
                         "mortality). Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes "
                         "eligible under the strict Family A/B/C framework: this is a two-group nonparametric "
                         "distributional comparison (KS test) over time-series IMR data, not a regression-based "
                         "estimate with a locatable point effect/CI isolating the mechanism at the individual "
                         "level. Extracted for record_id R0AFB571151F8."),
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-23",
    "evidence_status": "OBSERVED",
})
rows.append(r)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
