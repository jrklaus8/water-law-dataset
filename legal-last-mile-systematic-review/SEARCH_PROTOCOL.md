# Search Protocol

Status: **strategy defined; no search executed.** Every string below is a
starting strategy to be adapted, piloted, and logged — not a final query.
Every actual execution must be recorded in
`01_search/search_logs/search_log.csv` with the fields listed in §6, and its
raw export preserved, unedited, in `01_search/raw_exports/` (never
overwritten — see `REPRODUCIBILITY.md`).

## 1. Databases

**Tier 1 (academic):** Scopus, Web of Science, HeinOnline, Westlaw, Lexis,
ProQuest, Sociological Abstracts.

**Tier 2 (academic):** JSTOR, Google Scholar, SSRN, institutional repositories.

**Sector-specific:** PubMed, Global Health, relevant water/sanitation
bibliographic databases.

**Legal and primary-source repositories:** CanLII, Rechtspraak.nl, Brazilian
court databases, Brazilian regulatory databases (ANA, SNIS), relevant
municipal/provincial sources.

The academic databases answer *what does scholarship say?* The legal/
institutional databases answer *what legal and administrative evidence
exists?* **Do not mix these two populations in the statistical
meta-analysis** — code `database_source` and `peer_reviewed` per study
(`CODEBOOK.md` §1) so the distinction survives into extraction.

Per-database adapted strings live in `01_search/database_strategies/`:

| File | Databases |
|---|---|
| `scopus.md` | Scopus |
| `wos.md` | Web of Science |
| `pubmed.md` | PubMed, Global Health (Ovid) |
| `heinonline.md` | HeinOnline |
| `westlaw_lexis.md` | Westlaw, Lexis |
| `proquest_sociological_abstracts.md` | ProQuest, Sociological Abstracts |
| `jstor_google_scholar_ssrn.md` | JSTOR, Google Scholar, SSRN |
| `canlii.md` | CanLII |
| `rechtspraak.md` | Rechtspraak.nl |
| `brazil_legal_databases.md` | Brazilian state court databases, ANA, SNIS |
| `grey_literature.md` | Grey literature sources (§5 below) |

## 2. Core search concepts

Do not search only for "administrative law" — relevant literature may use
legal recognition, land tenure, formalization, service eligibility,
administrative/bureaucratic barriers, documentation, informal settlement,
municipal service access, service delivery, or regulatory governance
instead. Four concept blocks, combined with AND (within each block, OR):

**Block A — Service**
```
sanitation | "wastewater" | sewerage | "sewer connection*" | "water supply" |
"piped water" | "municipal water" | "water connection*" | "water service*" |
"sanitation service*" | WASH
```

**Block B — Legal and administrative mechanism**
```
"administrative law" | "administrative burden" | "administrative barrier*" |
"legal barrier*" | eligibility | "legal status" | "legal recognition" |
"land tenure" | "property title" | documentation | "identity document*" |
"building permit*" | zoning | formalization | formalisation |
regularization | regularisation | "service area" | "administrative
discretion" | discretion | accommodation | enforcement | regulation |
"regulatory governance" | governance | institutional* | bureaucratic |
"public administration" | "procedural barrier*"
```

**Block C — Outcome**
```
access | connection | coverage | formalization | formalisation |
availability | reliability | continuity | affordability | inequality |
inequity | exclusion | inclusion | "service delivery"
```

**Block D — Context (do NOT require in the main search)**
```
"informal settlement*" | slum* | "low income" | poverty | marginali* |
"urban poor" | periurban | "peri urban" | rural | migrant* | undocumented |
Indigenous | tenant*
```
Requiring Block D in the main search risks excluding relevant studies (e.g.
a formal, non-marginalized-population study of administrative eligibility
rules is still in scope). Use Block D only for a supplementary sensitivity
search and for post-hoc tagging of retrieved records.

Main search logic: **(A) AND (B) AND (C)**.

## 3. Jurisdiction-specific vocabulary

Mechanical translation is not sufficient — each jurisdiction's literature
uses its own legal and policy terminology.

### Brazil (Portuguese)
```
"saneamento básico" · "abastecimento de água" · "esgotamento sanitário" ·
"ligação domiciliar" · "ligação predial" · "ligação de água" · "ligação de
esgoto" · "acesso à água" · "acesso ao saneamento" · "universalização" ·
"regularização fundiária" · "assentamento informal" · "assentamentos
informais" · "ocupação irregular" · "aglomerado subnormal" · "favela" ·
"barreira administrativa" · "barreiras administrativas" · "barreira legal" ·
"barreiras legais" · "elegibilidade" · "exigência documental" ·
"licenciamento" · "regularização"
```
Brazilian literature may discuss *regularização fundiária* or connection
terminology without ever using "administrative law" as a phrase — do not
require the English legal-terminology block for Portuguese-language sources.

### Netherlands (Dutch)
```
drinkwater · wateraansluiting · aansluiting · aansluitplicht · riolering ·
rioolaansluiting · sanitatie · afvalwater · waterdienst ·
drinkwatervoorziening · toegang · vergunning · omgevingsvergunning ·
omgevingsplan · woonadres · inschrijving · BRP · BSN · bestuursrecht ·
administratieve lasten · beleidsregels · discretionaire bevoegdheid ·
evenredigheid · handhaving · kwetsbare huishoudens · informele bewoning
```
**Important:** do not assume a registration system or identifier (BRP, BSN)
is a *direct* water-connection requirement. The review must distinguish (1)
what legislation formally requires, (2) what utilities require in practice,
and (3) what indirect administrative systems make necessary — code this
distinction explicitly at extraction (`CODEBOOK.md`, `mechanism_certainty`).

### Canada / Ontario
```
"water connection" · "sewer connection" · "municipal water" · "municipal
sewer" · "public utility" · "water service" · "sewage service" · "service
area" · "building permit" · "planning approval" · "zoning" · "municipal by
law" · "municipal discretion" · "connection refusal" · "service refusal" ·
"water access" · "sewer access" · "administrative burden" · "procedural
fairness" · "regulatory governance" · "land tenure" · "informal settlement" ·
"Indigenous water" · "First Nations"
```
**Jurisdictional discipline:** do not automatically treat First Nations water
governance as an Ontario municipal administrative law problem. Separate at
extraction: Ontario municipal water/sewer connection; provincial regulation;
communities outside municipal service areas; First Nations systems; federal/
provincial/First Nations coordination.

## 4. Grey literature

Search government reports, regulatory decisions, municipal reports, utility
policies, NGO reports, international organization publications, court
databases, regulator databases, parliamentary reports, official consultation
documents, and institutional repositories — see `grey_literature.md` for
source-specific notes. Grey literature is included in the systematic
evidence map where relevant, and coded `peer_reviewed = false`, but is not
automatically pooled into the primary quantitative meta-analysis alongside
peer-reviewed evidence.

## 5. Search sequencing

1. Pilot Block A+B+C in Scopus; refine based on precision/recall against the
   preliminary source papers in `SOURCES.md` (all four must be retrievable
   by the finalized string before the search is run in earnest).
2. Adapt and run in each remaining Tier 1/Tier 2/sector database.
3. Run jurisdiction-specific vocabulary searches (§3) in the relevant
   national/legal databases.
4. Run grey literature searches.
5. Backward citation search on all included studies.
6. Forward citation search (via Scopus/Web of Science/Google Scholar
   citation tracking) on all included studies, where feasible.
7. Deduplicate (`01_search/deduplicated/`, method logged in
   `REPRODUCIBILITY.md`).

Do not claim the search is exhaustive until every step above is complete and
documented — see `PROJECT_SPEC.md` §12.

## 6. Reproducible search-log schema

Every individual search execution is one row in
`01_search/search_logs/search_log.csv`:

```
search_id, database, platform, date, researcher, exact_search_string,
filters, date_range, language_filters, results_returned, export_filename,
notes
```

Never overwrite an original search export. File naming convention:
`SEARCH_{NNN}_{DATABASE}_{YYYY-MM-DD}.csv` in `01_search/raw_exports/`, e.g.
`SEARCH_001_SCOPUS_2026-08-25.csv`, `SEARCH_002_WOS_2026-08-25.csv`.

## 7. Current status

**No Tier 1/Tier 2/legal-repository database has been searched natively.**
This environment has no credentials for Scopus, Web of Science, HeinOnline,
Westlaw, Lexis, ProQuest, or Sociological Abstracts — and, as of 2026-08-25,
it turns out it also cannot directly reach PubMed, Google Scholar, SSRN,
CanLII, or Rechtspraak.nl either: this environment's outbound network
egress policy blocks essentially all direct HTTP(S) access to the open web
(confirmed by testing `WebFetch` and a direct API call against a wide,
representative sample of these domains — every one was denied by the
egress proxy). The strings in `01_search/database_strategies/` remain
ready to run by a researcher (or a tool run with the appropriate access) —
running them and logging the results per §6 is still the way Phase 3
actually gets done.

**What *was* done:** an explicitly non-systematic, exploratory pilot using
Claude's `WebSearch` tool (a first-party search capability that, unlike
`WebFetch`, is not subject to the same egress block) — six queries drawn
from this protocol's terms, logged as `SEARCH_003`–`SEARCH_008` in
`01_search/search_logs/search_log.csv`, yielding 25 candidate records now
sitting in `02_screening/title_abstract/screening_database.csv` with no
screening decision made yet. This is not a substitute for Phase 3 and must
never be described as one in any manuscript output: it has weaker recall
than a platform-native search, no guaranteed stable/reproducible result
set, and no full-text access to verify anything beyond what a search
snippet shows. See the `notes` field on each of those search-log rows for
the full caveat, restated on every row so it survives independent of this
paragraph.
