import csv, os, tempfile, sys
csv.field_size_limit(sys.maxsize)

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

assert len(rows) == 62

REPLACEMENTS = {
    "S930": "adjusted (matched on municipal characteristics and settlement patterns)",
    "S947": "adjusted (GDP per capita, trade openness, FDI, urban population share, lagged dependent variable)",
    "S969": (
        "adjusted (colonizer identity [British=1] included as a covariate in the OLS "
        "model alongside colonial-era duration; no other confounders controlled -- "
        "derived from this row's own effect_estimate equation, ACCESS = 41.956 + "
        "0.322*YRSCOL + 2.420*COLONIZER, since extraction_database.csv's own "
        "adjusted_or_unadjusted/covariates fields were left blank for this study)"
    ),
    "S1020": "adjusted (propensity score matched: land quartile, income quartile, social group [SC/ST vs. other], prior water-collection-time quartile)",
    "S1032": "adjusted (area wealth, distance from central municipal offices, project density, community-meeting attendance, gender, language, redress-seeking contact type)",
    "S1038": "adjusted (long-run marginal cost [estimated via total variable cost and fixed cost regressions], price elasticity of demand [Foster & Beattie regional coefficients])",
    "S1042": "adjusted (school quality, healthcare, streets maintenance, waste management as competing public-goods outcomes; municipality controls)",
    "S1057": "adjusted (hygiene class, household size, household assets [Table 3]; local initiation, design participation, local decision-making, community fixed effects [Table 4])",
    "S1062": "adjusted (controls: initial coverage, public expenditure, Non-Revenue Water, ODA, regional dummies)",
    "S1102": "adjusted (propensity score matching: wealth, literacy, household size, village size)",
    "S1121": "adjusted (fixed-effects and random-effects panel regression, controlling for MSA price growth, prime rate, pre-1990 housing stock, other growth controls)",
    "S1122": "adjusted (Cox regression with residence status, zone of residence, migration origin, gender, education, employment type as covariates)",
    "S1136": "adjusted (village/block fixed effects, caste, road-length, institution controls)",
    "S1140": "adjusted (controls for project size, remoteness, time savings, social inclusion, regional dummies)",
    "S1143": "adjusted (OLS regressions control for demographic covariates: housing age/distance from CBD, percent black)",
    "S1144": "adjusted (controls for age, gender, competence, attitude, education, income, spatial-proximity distance measures)",
    "S1146": "adjusted (controls for piped-water-system presence, urban location, gender, individual bribery experience, country fixed effects)",
    "S1162": "adjusted (multilevel linear regression, controlling for population, population growth, initial coverage, density, distance to metro, intergovernmental aid, state income, urbanization, decentralization index)",
    "S1163": "adjusted (multilevel mixed-effects logistic regression)",
}

assert len(REPLACEMENTS) == 19

touched = 0
for row in rows:
    sid = row["study_id"]
    if sid in REPLACEMENTS:
        assert row["adjusted"].strip() == "TRUE", (sid, row["adjusted"])
        row["adjusted"] = REPLACEMENTS[sid]
        touched += 1

assert touched == 19, touched
assert len(rows) == 62

fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(PATH), suffix=".tmp")
with os.fdopen(fd, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp_path, PATH)

print("OK, touched", touched, "rows")
