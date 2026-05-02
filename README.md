# Water Law Judicial Decisions Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19836413.svg)](https://doi.org/10.5281/zenodo.19836413)
[![Harvard Dataverse](https://img.shields.io/badge/Harvard%20Dataverse-doi%3A10.7910%2FDVN%2FC9PEFS-blue)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/C9PEFS)
[![DANS](https://img.shields.io/badge/DANS%20SSH-doi%3A10.17026%2FSS%2FRVDBUF-orange)](https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/SS/RVDBUF)
[![OSF](https://img.shields.io/badge/OSF-osf.io%2Fadmrq-teal)](https://osf.io/admrq)
[![PyPI version](https://badge.fury.io/py/water-law-dataset.svg)](https://pypi.org/project/water-law-dataset/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A collection of scrapers for building a comparative dataset of water law judicial decisions across Brazil (27 state courts), Canada (federal + provincial courts via CanLII), and the Netherlands (Raad van State + all 11 district courts via Rechtspraak.nl).

**Scope:** 2016–2026 | **Cases collected:** 33,511 decisions across Brazil, Canada, and Netherlands

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
│   │   ├── canlii_scraper.py          (CanLII REST API — requires free API key)
│   │   ├── canada_canlii_extra.py     (113 extra CanLII databases not in main scraper)
│   │   └── canada_ldh_scraper.py      (Legal Data Hunter semantic search — requires API key)
│   └── netherlands/
│       ├── rechtspraak_scraper.py     (Rechtspraak Open Data — no auth)
│       └── rechtspraak_expanded.py   (RvS/CBb/GHARL/HR extended crawl)
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
python scrapers/canada/canlii_scraper.py       # main CanLII keyword search
python scrapers/canada/canada_canlii_extra.py  # 113 additional CanLII databases
```

### 4. Legal Data Hunter (Canada, semantic search) — requires API key

The `canada_ldh_scraper.py` uses [Legal Data Hunter](https://legaldatahunter.com) to run semantic and keyword searches across the full CanLII corpus (94,502+ Canadian legal documents). This supplements the title-based CanLII API by surfacing cases where water law is the substance of the decision, not just the title.

```bash
export LDH_API_KEY=your_key_here
python scrapers/canada/canada_ldh_scraper.py
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

## Acknowledgements

### Scholarly Inspiration

I would like to acknowledge that this research is inspired by the work of **Professor LaDawn Haglund** in the fields of comparative water law, water governance, and the judicialization of water and sanitation. Her scholarship, including *Water Governance and Social Justice in São Paulo, Brazil* and her broader work on human rights and urban water systems, has been central in shaping how I understand the relationship between law, policy, and access to essential resources.

I had the privilege of working with her as a research assistant some years ago, and that experience played an important role in directing my interest toward this area. I am especially grateful for her early encouragement to study water law in Brazil and to approach these challenges from a comparative and global perspective.

Her research and publications remain essential references for this project. I strongly recommend her work to anyone interested in water law, governance, and the role of legal institutions in addressing complex social and environmental challenges.

Selected publications:
- Haglund, L. (2014). [Water Governance and Social Justice in São Paulo, Brazil](https://ui.adsabs.harvard.edu/abs/2014WaPol..16S..78H/abstract). *Water Policy*, 16(S2), 78–97.
- Haglund, L. (2019). [Can Human Rights Challenge Neoliberal Logics? Evidence from Water and Sanitation Rulings in São Paulo, Brazil](https://www.cambridge.org/core/books/abs/economic-and-social-rights-in-a-neoliberal-world/can-human-rights-challenge-neoliberal-logics-evidence-from-water-and-sanitation-rulings-in-sao-paulo-brazil/CA46C96661D045816C8173F6CC6116DC). In *Economic and Social Rights in a Neoliberal World*. Cambridge University Press.
- Haglund, L. (2019). [Sustainable Urban Water Governance and Human Rights](https://www.mdpi.com/2071-1050/11/19/5314). *Sustainability*, 11(19), 5314.

---

### Tools and Platforms

**[Legal Data Hunter](https://legaldatahunter.com)** — semantic legal search across 18M+ decisions from 110+ countries. An outstanding tool for comparative legal research that goes well beyond keyword matching. The Canadian component of this dataset was significantly enriched through LDH's semantic search over the full CanLII corpus. If you're building a legal dataset or doing cross-jurisdictional research, Legal Data Hunter is genuinely worth checking out.

**[CanLII](https://www.canlii.org)** — the Canadian Legal Information Institute, whose free public API made systematic collection of Canadian case law possible.

**[Rechtspraak.nl](https://www.rechtspraak.nl)** — the Dutch courts' open data portal, which provides structured XML access to published decisions.

If you use it in your own work, please cite:

> Klaus, C. (2026). *Global Water Law Judicial Decisions Dataset* (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19836413

Also archived at:
- Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/C9PEFS
- DANS Data Station SSH: https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/SS/RVDBUF
- OSF: https://osf.io/admrq

---

## License

MIT
