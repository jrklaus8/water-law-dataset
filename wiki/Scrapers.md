# Scrapers

All scrapers are in the `scrapers/` directory. They use Python 3.8+ with no external dependencies.

---

## Running a Scraper

```bash
# Set output directory
export OUTPUT_DIR=./data        # Linux/Mac
set OUTPUT_DIR=.\data           # Windows

# Run any scraper
python scrapers/brazil/tjdft_scraper.py
python scrapers/netherlands/rechtspraak_scraper.py
python scrapers/canada/canlii_scraper.py
```

Output: `$OUTPUT_DIR/{court_code}_cases_2016_2026.json`

---

## Brazil

### TJDFT (Brasília)
- **Method:** Elasticsearch REST API
- **Endpoint:** `https://pesquisajurisprudencial.tjdft.jus.br/`
- **Cases:** 8,421
- **Notes:** Supports date range filtering; uses `match_phrase` queries

### TJSC (Santa Catarina)
- **Method:** ESAJ AJAX
- **Endpoint:** `https://busca.tjsc.jus.br/jurisprudencia/`
- **Cases:** 1,224
- **Notes:** Returns paginated JSON; 50 results per page

### TJRJ (Rio de Janeiro)
- **Method:** ASP.NET WebForms
- **Endpoint:** `http://www1.tjrj.jus.br/gedcacheweb/`
- **Cases:** 1,219
- **Notes:** Requires `__VIEWSTATE` token parsing; fragile

### TJSP (São Paulo)
- **Method:** ESAJ POST
- **Endpoint:** `https://esaj.tjsp.jus.br/cjsg/`
- **Cases:** 574
- **Notes:** ESAJ limits to 250 results per query; multiple keyword variations needed

### Smaller courts (TJRR, TJAC, TJPI, TJTO)
- **Methods vary:** ESAJ POST, Rails GET, PHP+Solr
- **Combined cases:** 86
- **Notes:** Low case counts reflect small court sizes and narrow water law dockets

### Courts that could not be collected
Nineteen of the 27 state courts were blocked (for example TJMG: DWR + CAPTCHA; TJBA: GraphQL server error; TJSE and TJES: Turnstile CAPTCHA; TJGO and TJRO: single-page apps with no public API; TJRS, TJPE, TJPA, TJAL: DNS or timeouts). The full status table is in the [project README](https://github.com/jrklaus8/water-law-dataset#brazilian-courts--access-status). The Brazilian total is **11,724** (11,524 from eight courts plus 200 historical TJSP decisions).

---

## Netherlands

### rechtspraak_scraper.py — Base Scraper (RvS and district courts)
- **Source:** Rechtspraak Open Data API (`https://data.rechtspraak.nl/`)
- **Targets:** Raad van State (RvS) administrative law decisions and all 11 district courts (Rechtbanken)
- **Auth:** None required — fully open
- **Format:** Structured XML
- **Cases:** 17,783 (district courts)

### rechtspraak_expanded.py — Expanded Multi-Court Scraper
- **Targets:** RvS + CBb (College van Beroep voor het bedrijfsleven) + GHARL (Gerechtshof Arnhem-Leeuwarden)
- **Method:** Keyword search via Rechtspraak Open Data API with pagination
- **Output:** `netherlands_water_law_2016_2026.json`
- **Cases:** 50,871 (appellate); with the district courts the Netherlands total is **68,654**

---

## Canada

### canlii_scraper.py
- **Source:** [CanLII REST API](https://developer.canlii.org/) (free API key required)
- **Method:** Keyword search across all available databases
- **Cases:** 228

### canada_canlii_extra.py
- **Source:** 113 additional CanLII databases not covered in main scraper
- **Cases:** 157
- **Note:** Year extraction from citation string (CanLII's `caseBrowse` endpoint lacks `decisionDate`)

### canada_superior_expanded.py
- **Target:** 13 superior/appellate courts
- **Method:** Expanded keyword run
- **Cases:** 2,833

### canada_ldh_scraper.py
- **Source:** [Legal Data Hunter](https://legaldatahunter.com) semantic and keyword search across the CanLII corpus (API key required: `LDH_API_KEY`)
- **Purpose:** supplements the title-based CanLII API by surfacing cases where water law is the substance of the decision, not just the title
- **Canada total across all Canadian sources:** 3,218

---

## Merge and Coding

After scraping, run:

```bash
pip install pandas openpyxl          # only needed for merge + charts
python utils/merge_national.py       # merge all JSON → CSV + XLSX
python utils/jurimetric_coding.py    # apply 7 jurimetric variables
python validation/residual_audit.py  # reproduce the v0.3.0 residual audit
```

See [[Jurimetric Coding]] for variable definitions and [[Validation]] for the audit.

---

## Related tools

- **`research-assistant/`** — a Streamlit research assistant (built for the WashU Law International Vibe Coding Challenge, 2026) that answers plain-language questions about the 83,596-decision dataset using Claude. It needs an Anthropic API key and states that its answers reflect dataset patterns, not comprehensive legal research.
- **The systematic review's code** (`legal-last-mile-systematic-review/code/`) is separate from the scrapers; see [[Systematic Review]].
