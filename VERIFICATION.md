# Verification Recipe

A reviewer should be able to check this dataset without taking anything on
trust. This file is the shortest path from "I have doubts" to "I have checked".

Three levels, from ten minutes to a full replication. See `DATA_ACCESS.md` for
where the data lives and what it contains.

---

## Level 1 — Spot-check twenty decisions (ten minutes, no software)

The twenty decisions below are drawn from the stratified validation sample in
`validation/second_coder_sample_raw.csv` (seed 7). Every one was classified
`not_water_related` by the coding engine, and every one was independently
reviewed by a human coder whose label is shown.

Open any of them and ask: is the engine's `not_water_related` defensible?

| # | Case | Country | Court | Human label | Permalink |
|---:|---|---|---|---|---|
| 1 | `ECLI:NL:CBB:2016:219` | Netherlands | CBb | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:CBB:2016:219) |
| 2 | `ECLI:NL:RBGEL:2025:4999` | Netherlands | RBGEL | WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RBGEL:2025:4999) |
| 3 | `ECLI:NL:RVS:2017:1757` | Netherlands | RvS | UNCERTAIN | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RVS:2017:1757) |
| 4 | `ECLI:NL:RVS:2025:1447` | Netherlands | RvS | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RVS:2025:1447) |
| 5 | `ECLI:NL:RBDHA:2020:11282` | Netherlands | RBDHA | WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RBDHA:2020:11282) |
| 6 | `ECLI:NL:CBB:2023:364` | Netherlands | CBb | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:CBB:2023:364) |
| 7 | `ECLI:NL:CBB:2021:1040` | Netherlands | CBb | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:CBB:2021:1040) |
| 8 | `ECLI:NL:RBMNE:2020:4807` | Netherlands | RBMNE | WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RBMNE:2020:4807) |
| 9 | `ECLI:NL:RVS:2022:1997` | Netherlands | RvS | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RVS:2022:1997) |
| 10 | `ECLI:NL:RVS:2024:690` | Netherlands | RvS | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RVS:2024:690) |
| 11 | `ECLI:NL:RBDHA:2025:7356` | Netherlands | RBDHA | WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RBDHA:2025:7356) |
| 12 | `ECLI:NL:RVS:2024:167` | Netherlands | RvS | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RVS:2024:167) |
| 13 | `ECLI:NL:RBDHA:2025:22736` | Netherlands | RBDHA | WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:RBDHA:2025:22736) |
| 14 | `ECLI:NL:CBB:2016:287` | Netherlands | CBb | NOT_WATER | [link](https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:CBB:2016:287) |
| 15 | `4076755` | Brazil | TJSP | UNCERTAIN | [link](https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=4076755) |
| 16 | `00079338620088260505` | Brazil | TJSP | NOT_WATER | [link](https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor=0007933-86.2008.8.26.0505) |
| 17 | `01888384920088260000` | Brazil | TJSP | NOT_WATER | [link](https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor=0188838-49.2008.8.26.0000) |
| 18 | `7593185` | Brazil | TJSP | UNCERTAIN | [link](https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=7593185) |
| 19 | `7594325` | Brazil | TJSP | UNCERTAIN | [link](https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=7594325) |
| 20 | `5373185` | Brazil | TJSP | NOT_WATER | [link](https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao=5373185) |

**What you should find.** The rows labelled WATER are genuine water cases that
the engine missed. That is not hidden: it is the false-negative mechanism
documented in `DATA_ACCESS.md` §6.2 and quantified by `utils/audit_trail.py`.
Dutch compounds nouns without spaces, and the engine's water gate is written
with `\b` word boundaries, so `waterwet` and `watervergunning` are invisible to
it.

The rows labelled UNCERTAIN are mostly Brazilian records whose *ementa* is too
thin to classify from the headnote alone. That is the headnote ceiling described
in `DATA_ACCESS.md` §2.

If the engine were being oversold, this table would not be in the repository.

---

## Level 2 — Audit the coding (half an hour, Python)

Every decision carries the rule that classified it and the text that rule
matched, so no classification has to be taken on faith.

```bash
# 1. Download the deposited dataset
#    https://doi.org/10.5281/zenodo.19836413  ->  ./data/water_law_global.csv

# 2. Re-run the coding engine (emits gov_matched_rule + gov_matched_span)
export DATA_DIR=./data
python utils/jurimetric_coding.py

# 3. Build the audit bundle
python utils/audit_trail.py --csv data/water_law_global_coded.csv
```

You get:

| File | What it answers |
|---|---|
| `AUDIT_TRAIL.md` | For a sample of each category: which rule fired, on what text, linked to the decision |
| `audit_sample.csv` | The same, as data, with a permalink per row |
| `audit_rule_coverage.csv` | Every rule and how many decisions it decides |

**Start with `audit_rule_coverage.csv`.** Sort by `n_decisions`. Where a single
regex decides a large share of a category, that regex is carrying the finding,
and it is the first thing worth disputing.

Then read `AUDIT_TRAIL.md` §4, the Dutch compound diagnostic. It reports how
many Netherlands decisions were gated out by a filter that could not see their
water vocabulary. It changes no labels; it measures the problem.

---

## Level 3 — Replicate from source (hours to days)

```bash
# Netherlands — no authentication required
export OUTPUT_DIR=./data
python scrapers/netherlands/rechtspraak_scraper.py
python scrapers/netherlands/rechtspraak_expanded.py

# Canada — free API key from https://developer.canlii.org/
export CANLII_API_KEY=...
python scrapers/canada/canlii_scraper.py

# Brazil — one script per accessible tribunal
python scrapers/brazil/tjsc_scraper.py        # etc.

# Merge and code
python utils/merge_national.py
python utils/jurimetric_coding.py
```

Expect drift. Courts publish decisions retroactively and occasionally withdraw
them, so a fresh scrape will not reproduce 83,596 exactly. The deposited
snapshot at the DOI is the citable artefact; a re-scrape is a check on method,
not a bit-for-bit reproduction.

Nineteen Brazilian tribunals could not be scraped at all (status table in
`README.md`). Any replication inherits that gap.

### Retrieving decision text

```bash
# Netherlands full text (open data, redistributable)
python scrapers/netherlands/rechtspraak_fulltext.py --from-csv data/water_law_global.csv --resume

# Any single decision, any jurisdiction
python utils/resolve_case.py ECLI:NL:RVS:2019:2481
python utils/resolve_case.py --csv data/water_law_global.csv   # whole dataset
```

Canada and Brazil are link-only. `DATA_ACCESS.md` §3 explains why, per
jurisdiction.

---

## What cannot be verified from this dataset

Be clear about the boundary:

- **Netherlands outcomes.** Dispute type is coded; who won is not. Any claim
  about whether Dutch administrative litigation expands or delays water access
  is inferential until the full-text corpus is built and coded.
- **Brazilian national representativeness.** Eight of twenty-seven tribunals are
  present. The eight are those with modern search infrastructure, which is not a
  random property.
- **Anything resting on the headnote alone.** Where an *ementa* or
  `inhoudsindicatie` is a single sentence, neither the engine nor a human coder
  can classify reliably from the deposited text. `UNCERTAIN` in the validation
  labels marks exactly these.
