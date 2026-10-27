# Dataset Overview

## Scope

The Global Water Law Judicial Decisions Dataset is a comparative jurimetric corpus covering:

- **Time period:** 2016–2026 (primary) + 200 historical TJSP decisions 1997–2015 (included in the Brazil total)
- **Countries:** Brazil, Canada, Netherlands
- **Total cases:** **83,596** decisions (Brazil 11,724 · Netherlands 68,654 · Canada 3,218)
- **Version:** 0.3.0 (May 2026)
- **Variables:** 7 jurimetric variables, with a 21-value governance category (see [[Jurimetric Coding]])
- **Water relevance:** 67,703 decisions are coded `not_water_related` because the broad keyword searches deliberately favoured recall; see [[Validation]]

## Data Sources

### Brazil

| Court | State | Method | Cases |
|-------|-------|--------|-------|
| TJDFT | Brasília (DF) | Elasticsearch REST API | 8,421 |
| TJSC | Santa Catarina | ESAJ AJAX | 1,224 |
| TJRJ | Rio de Janeiro | ASP.NET WebForms | 1,219 |
| TJSP | São Paulo | ESAJ POST | 574 |
| TJRR | Roraima | ESAJ POST | 21 |
| TJAC | Acre | ESAJ POST | 33 |
| TJPI | Piauí | Rails GET | 15 |
| TJTO | Tocantins | PHP+Solr GET | 17 |
| TJSP (historical) | São Paulo | Hand-coded 1997–2015 | 200 |

**Search queries used:**
- Primary: `água abastecimento fornecimento saneamento`
- Secondary: `corte suspensão fornecimento água`
- Tertiary: `proteção manancial recursos hídricos ambiental`

### Canada

| Source | Method | Cases |
|--------|--------|-------|
| CanLII REST API (main) | Keyword search | 228 |
| CanLII Extra (113 databases) | Extended keyword search | 157 |
| Superior/appellate courts | Expanded keyword run | 2,833 |

**Total: 3,218 cases.** The project README attributes the total to the CanLII keyword search, the extra CanLII databases, Legal Data Hunter semantic search (`canada_ldh_scraper.py`) and the superior and appellate courts; the per-source rows above are the original run counts. Data collected via the [CanLII REST API](https://developer.canlii.org/) (free registration required) and [Legal Data Hunter](https://legaldatahunter.com). About 86.9% of Canadian records are title-only, which limits coding; the recommended route to full texts is the A2AJ Canadian Legal Data project (see `FUTURE_WORK.md`).

### Netherlands

| Source | Method | Cases |
|--------|--------|-------|
| Appellate courts (RvS + CBb + GHARL) | Expanded crawler (`rechtspraak_expanded.py`) | 50,871 |
| District courts (all 11 Rechtbanken) | Rechtspraak API (`rechtspraak_scraper.py`) | 17,783 |
| **Total** | | **68,654** |

Data collected via the [Rechtspraak Open Data API](https://data.rechtspraak.nl/) — fully open, no authentication required.

## Unified Schema

Every case in the merged CSV/XLSX has these columns:

| Column | Description |
|--------|-------------|
| `country` | Brazil / Canada / Netherlands |
| `tribunal` | Court abbreviation (e.g., TJDFT, CanLII, RvS) |
| `court_name` | Full court name |
| `case_id` | Process number / ECLI / CanLII citation |
| `title` | Case title (Canada/NL) |
| `date` | Decision date (YYYY-MM-DD) |
| `year` | Decision year |
| `case_type` | Procedural class (e.g., Apelação Cível) |
| `chamber` | Chamber/panel name |
| `judge` | Reporting judge (relator) |
| `legal_area` | Legal domain (rechtsgebied) |
| `summary` | Case summary / ementa / inhoudsindicatie |
| `url` | Source URL |

## Deduplication

Cases are deduplicated per country using:
- **Brazil:** `num_processo` (unique process number)
- **Canada:** `citation` (CanLII citation string)
- **Netherlands:** `ecli` (European Case Law Identifier)

## Known limitations

- **Outcome coding.** Only Brazil carries (AI-assisted) outcome coding. The Netherlands sub-dataset classifies dispute *type* but not who won; see `FUTURE_WORK.md` for the roadmap.
- **Canada coverage.** The Canadian sub-dataset concentrates on reported decisions from CanLII and omits unreported tribunal decisions (for example Environmental Review Tribunal and Licence Appeal Tribunal), which may carry a disproportionate share of access-to-water disputes.
- **Brazil coverage.** Nineteen of 27 state courts were blocked or untestable (CAPTCHAs, SPAs without public APIs, TLS errors, timeouts); the Brazilian corpus covers eight courts. See [[Scrapers]].

## Related project

The AI-assisted systematic review of the research literature on the same question is described on [[Systematic Review]]; it is a separate evidence base and does not use this dataset's court decisions.
