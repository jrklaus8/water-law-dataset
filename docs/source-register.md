# Source register

For every source the project collected from or tried to collect from: how it was reached, which script did it, what is recorded about it, and what is **not** known. The main gap is that **the terms of use, request limits, robots.txt rules and anonymisation practice of each source are not recorded anywhere in the repository**, and this audit did not retrieve them (no live requests were made). Every such field below says "awaiting confirmation". Nothing here asserts that collection or republication was permitted.

*Written by an AI assistant (Claude Code), 2026-10-27, from the README, the scrapers and the review's search records. Counts are the README's; they were not recomputed because the collected data are not in the repository. Not a legal opinion.*

**Fields that are the same for every court source (so they are not repeated in each row):**

| Field | Value |
|---|---|
| Collection dates | Not recorded in the repository (scrapers write no run log; finding F-23) |
| Terms of use / licence of the source | awaiting confirmation |
| robots.txt consulted | not recorded |
| Anonymisation of the published text, and whether decisions name parties | awaiting confirmation |
| Permission to republish decisions or summaries in the deposits | awaiting confirmation |
| Scope of years | 2016–2026 (the 200 historical TJSP cases cover 1997–2015) |

## 1. Court sources (the 83,596-decision dataset)

### Brazil (README: 11,724 decisions from 8 courts plus 200 hand-coded historical)

| Court | Access method (README) | Script | README count | Notes |
|---|---|---|---|---|
| TJSP (São Paulo) | ESAJ POST | **none in the repository** (F-30) | 574 | cannot be re-collected from the repository |
| TJSP 1997–2015 | hand-coded spreadsheet (2021), converted | `scrapers/brazil/tjsp_transformation_loader.py` | 200 | the spreadsheet is not in the repository; authorship and permission unstated (F-30) |
| TJSC (Santa Catarina) | ESAJ AJAX | `tjsc_scraper.py` | 1,224 | browser-style User-Agent (F-02) |
| TJRR (Roraima) | ESAJ POST | `tjrr_scraper.py` | 21 | browser-style User-Agent |
| TJAC (Acre) | ESAJ POST | `tjac_scraper.py` | 33 | browser-style User-Agent |
| TJPI (Piauí) | Rails GET | `tjpi_scraper.py` | 15 | browser-style User-Agent |
| TJTO (Tocantins) | PHP + Solr GET | `tjto_scraper.py` | 17 | browser-style User-Agent |
| TJDFT (Distrito Federal) | Elasticsearch REST | `tjdft_scraper.py` | 8,421 | browser-style User-Agent |
| TJRJ (Rio de Janeiro) | ASP.NET WebForms | `tjrj_scraper.py` | 1,219 | TLS verification disabled (F-01); browser-style User-Agent |

Search queries recorded in the README: primary `água abastecimento fornecimento saneamento`; secondary `corte suspensão fornecimento água`; tertiary `proteção manancial recursos hídricos ambiental`.

**Attempted and not collected (README "Access Status"): 19 of the 27 state courts** — MG, BA, PR, CE, SE, ES, AM, GO, RO, MT, MS, RS, PB, AP, RN, PE, PA, AL, MA — recorded as blocked by CAPTCHAs, single sign-on, server errors, timeouts or HTTP 403/520. Which courts could be collected therefore depended on technical accessibility, not on a sampling plan (see [`limitations.md`](limitations.md)). The repository does not document how any of the barriers were encountered, and none should be circumvented without checking the terms first.

### Canada (README: 3,218 decisions)

| Source | Access method | Script | Credentials | Notes |
|---|---|---|---|---|
| CanLII | REST API; the README says it returns metadata and requires a free key | `scrapers/canada/canlii_scraper.py` (2016–2026 window in the script) | `CANLII_API_KEY` from the environment | terms awaiting confirmation (the API terms and the site terms were not read; an earlier search summary indicated that CanLII's terms restrict systematic downloading, which has not been verified) |
| CanLII, 113 additional databases | same | `canada_canlii_extra.py` | `CANLII_API_KEY` | as above |
| CanLII superior and appellate courts | same | `canada_superior_expanded.py` | `CANLII_API_KEY` | as above; not listed in the README tree (F-31) |
| Legal Data Hunter (third-party semantic search over case law) | API | `canada_ldh_scraper.py` | `LDH_API_KEY` | a third-party service with its own terms; what it returns and its licence for reuse are awaiting confirmation |

The README does not break the 3,218 down by script.

### Netherlands (README: 68,654 decisions)

| Source | Access method | Script | README count | Notes |
|---|---|---|---|---|
| Rechtspraak.nl open data (data.rechtspraak.nl feed and content endpoints) | public XML; no authentication | `rechtspraak_scraper.py` (per its header: Raad van State and CBb); `rechtspraak_expanded.py` (RvS, CBb, GHARL, HR); `rechtspraak_district_courts.py` (11 Rechtbanken, 3 Gerechtshoven, CRvB, pre-filtered to the environmental/planning subject area) | 50,871 appellate and 17,783 district (README attributes them to different scripts than the headers do, F-31) | TLS verification disabled in all three (F-01); placeholder contact in `rechtspraak_scraper.py` (F-02); request limits of the service not recorded |

Inclusion filter in the Dutch scripts: a decision is kept when its summary or legal-area text contains a water-related term or its legal area is one of a short list (`is_water` in `rechtspraak_scraper.py`). A substring such as "water" also matches words like "Waterfront" (characterised in `tests/test_offline_helpers.py`). Later, the coding engine classifies 98.56% of the Dutch decisions as `not_water_related`, so the collection is much wider than the final water set (see F-10 on how that figure is read).

## 2. Sources of the systematic review

| Source | Access | What is recorded | Terms |
|---|---|---|---|
| Scopus (19 export files), Web of Science, HeinOnline, ProQuest (2 files), JSTOR | The researcher ran the searches through institutional access; some exports were relayed by an AI browser assistant (`AI_USE_LEDGER.md`) | Search strings and dates in `SEARCH_PROTOCOL.md` and the export file names; counts in the PRISMA flow | awaiting confirmation; exports are committed to the public repository (F-04) |
| SSRN, citation and grey-literature pilots, web-search pilots | researcher, with AI assistance | export files in `01_search/raw_exports/` | awaiting confirmation |
| Full texts of included and excluded articles | supplied by the researcher via a shared Drive folder | batch logs in `00_admin/DRIVE_INBOX_BATCH*_LOG_*.md` | publisher licences vary; PDFs are withheld from the repository |
| Legal Data Hunter source requests | `00_admin/LEGAL_DATA_HUNTER_SOURCE_REQUESTS_2026-10-04.md` | requests made to the service | not read |

## 3. How to complete this register

For each source, the researcher (or the library) should open the official terms and fill one row: the URL of the terms, the date read, what they say about automated access, rate limits, storage, republication of text and of derived data, and the personal-data position. Where the answer is unclear, ask the source or the library and record the question and the date, not confidential correspondence. A source whose terms forbid what was done is recorded as such: the correction is then a decision for the researcher, not a silent edit.
