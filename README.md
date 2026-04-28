# Water Law Judicial Decisions Dataset

A collection of scrapers for building a comparative dataset of water law judicial decisions across Brazil (27 state courts), Canada (federal + provincial courts via CanLII), and the Netherlands (Raad van State + CBb via Rechtspraak.nl).

**Scope:** 2016–2026 | **Cases collected:** 8,368 Brazilian decisions (8 courts) + Netherlands

---

## Repository Structure

```
water-law-dataset/
├── scrapers/
│   ├── brazil/            # One scraper per accessible TJ court
│   │   ├── tjac_scraper.py   (TJAC – Acre,        ESAJ POST)
│   │   ├── tjdft_scraper.py  (TJDFT – Brasília,   Elasticsearch REST)
│   │   ├── tjpi_scraper.py   (TJPI – Piauí,       Rails GET)
│   │   ├── tjrj_scraper.py   (TJRJ – Rio de Janeiro, ASP.NET WebForms)
│   │   ├── tjrr_scraper.py   (TJRR – Roraima,     ESAJ POST)
│   │   ├── tjsc_scraper.py   (TJSC – Santa Catarina, ESAJ AJAX)
│   │   └── tjto_scraper.py   (TJTO – Tocantins,   PHP+Solr GET)
│   ├── canada/
│   │   └── canlii_scraper.py  (CanLII REST API — requires free API key)
│   └── netherlands/
│       └── rechtspraak_scraper.py  (Rechtspraak Open Data — no auth)
├── utils/
│   ├── merge_national.py      # Merges per-court JSON files into national CSV/XLSX
│   └── make_progress_charts.py
├── data/                      # Output directory (gitignored — add your JSON/CSV here)
├── .env.example
├── requirements.txt
└── README.md
```

---

## Quick Start

### 1. Clone and configure

```bash
git clone https://github.com/YOUR_USERNAME/water-law-dataset.git
cd water-law-dataset
cp .env.example .env
# Edit .env and set OUTPUT_DIR and any API keys you need
```

### 2. Run a scraper

All scrapers use only the Python standard library (Python 3.8+). No `pip install` needed for scraping.

```bash
# Set output directory (or edit .env)
export OUTPUT_DIR=./data        # Linux/Mac
set OUTPUT_DIR=.\data           # Windows

# Run any scraper
python scrapers/brazil/tjsc_scraper.py
python scrapers/brazil/tjdft_scraper.py
python scrapers/netherlands/rechtspraak_scraper.py
```

Output is written to `$OUTPUT_DIR/<court>_cases_2016_2026.json`.

### 3. CanLII (Canada) — requires API key

```bash
# Register free at https://developer.canlii.org/
export CANLII_API_KEY=your_key_here
python scrapers/canada/canlii_scraper.py
```

### 4. Merge into national dataset

```bash
pip install pandas openpyxl          # only needed for merge + charts
export DATA_DIR=./data
python utils/merge_national.py
python utils/make_progress_charts.py
```

---

## Brazilian Courts — Access Status

| UF | Court | Cases | Method | Status |
|----|-------|-------|--------|--------|
| SP | TJSP | 574 | ESAJ POST | ✅ Done |
| SC | TJSC | 1,224 | ESAJ AJAX | ✅ Done |
| RR | TJRR | 21 | ESAJ POST | ✅ Done |
| AC | TJAC | 33 | ESAJ POST | ✅ Done |
| PI | TJPI | 15 | Rails GET | ✅ Done |
| TO | TJTO | 17 | PHP+Solr GET | ✅ Done |
| DF | TJDFT | 5,265 | Elasticsearch REST | ✅ Done |
| RJ | TJRJ | 1,219 | ASP.NET WebForms | ✅ Done |
| MG | TJMG | — | DWR + CAPTCHA | ❌ Blocked |
| BA | TJBA | — | GraphQL (server 500) | ❌ Blocked |
| PR | TJPR | — | Full-text too broad (334K results) | ❌ Blocked |
| CE | TJCE | — | ESAJ TLS error | ❌ Blocked |
| SE | TJSE | — | JSF + Turnstile CAPTCHA | ❌ Blocked |
| ES | TJES | — | JSF + Turnstile CAPTCHA | ❌ Blocked |
| AM | TJAM | — | CAS SSO required | ❌ Blocked |
| GO | TJGO | — | React SPA, no public API | ❌ Blocked |
| RO | TJRO | — | Angular SPA, no public API | ❌ Blocked |
| MT | TJMT | — | SPA, requires JS | ❌ Blocked |
| MS | TJMS | — | ESAJ timeout | ❌ Blocked |
| RS | TJRS | — | DNS/timeout | ❌ Blocked |
| PB | TJPB | — | Cloudflare 520 | ❌ Blocked |
| AP | TJAP | — | HTTP 403 | ❌ Blocked |
| RN | TJRN | — | HTTP 403 | ❌ Blocked |
| PE | TJPE | — | Timeout/DNS | ❌ Blocked |
| PA | TJPA | — | Timeout/DNS | ❌ Blocked |
| AL | TJAL | — | Timeout/DNS | ❌ Blocked |
| MA | TJMA | — | No jurisprudência endpoint | ❌ Blocked |

**Total collected:** 8,368 cases from 8 courts (TJSP + TJSC + TJDFT + TJRJ + TJRR + TJAC + TJPI + TJTO)

---

## Search Queries Used

**Primary:** `água abastecimento fornecimento saneamento`  
**Secondary:** `corte suspensão fornecimento água`  
**Tertiary:** `proteção manancial recursos hídricos ambiental`

---

## Output JSON Schema

Each case record contains:

```json
{
  "tribunal": "TJSC",
  "estado": "SC",
  "num_processo": "0001234-56.2022.8.24.0001",
  "data_julgamento": "2022-03-15",
  "ano": 2022,
  "classe": "Apelação Cível",
  "camara_orgao": "1ª Câmara de Direito Público",
  "relator": "Des. João Silva",
  "ementa": "DIREITO À ÁGUA. Fornecimento. ...",
  "url": "https://..."
}
```

---

## Legal Note

These scrapers query publicly accessible jurisprudência portals. All decisions are public court records. This dataset is intended for academic comparative law research.

---

## License

MIT
