# Research Context — The Legal Last Mile

## Preliminary Research

**Title:** The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance  
**Author:** Claudio Klaus  
**Citation style:** OSCOLA  
**Method:** Most Different Systems Design (MDSD) — Netherlands · Canada (Ontario) · Brazil

This preliminary research investigates how administrative law frameworks condition access to sanitation infrastructure at the *point of connection* across three jurisdictions that diverge profoundly in legal tradition and institutional architecture yet converge on a shared outcome: the administrative exclusion of marginalized households from services that are, in physical terms, within reach.

---

## Core Theory

### The Legal Last Mile
The legal/administrative gap between the physical existence of infrastructure and effective household connection. The barrier is not engineering — it is bureaucratic eligibility.

### The Gatekeeper Thesis
Administrative law transforms access from a physical possibility into a **conditional legal status** through four dimensions:
1. **Legal eligibility barriers** — formal requirements to qualify for connection
2. **Administrative burden** — procedural and compliance costs borne by the applicant
3. **Discretion and flexibility** — capacity of administrators to accommodate non-standard cases
4. **Enforcement and sanctions** — response to non-compliance

### The Administrative Ghost
Individuals physically present and need-bearing but legally invisible to the administrative system. Their absence from litigation *is* the evidence of exclusion — bureaucratic barriers prevent them from reaching courts even to claim the initial connection right.

### Two Models of Accommodation
| Model | Jurisdiction | Mechanism |
|---|---|---|
| Pre-litigation absorption | Netherlands | Institutional flexibility (proportionality, protective rules, ombudsman) absorbs non-standard cases before courts |
| Post-litigation accommodation | Brazil | Courts (via Ministério Público, constitutional adjudication) become the primary accommodation forum — produces mass litigation over *symptoms* |
| Intermediate (hypothesis) | Canada / Ontario | Opaque discretion, fragmented procedural protections |

---

## The Dataset as Empirical Instrument

This repository contains the scrapers and data for the jurimetric backbone of the preliminary research: **83,596 judicial decisions** from Brazil, the Netherlands, and Canada, coded via regex on decision summaries to test the Legal Last Mile theory.

### Preliminary Findings

**Brazil (11,724 decisions):**

| Theme | Share |
|---|---|
| Tariffs / billing disputes | 48.52% |
| Connection refusal | 10.88% |
| Irregular settlements / favelas | 0.75% |

Courts process the *symptoms* of exclusion; the root matrix of ineligibility is almost never litigated. This validates the Administrative Ghost: the 0.75% irregular settlement rate and 10.88% connection-refusal rate reveal the tip of a much larger excluded population that never reaches courts at all.

**Netherlands (68,654 decisions):**  
The vast majority of cases (98.56%) were absorbed before litigation. The court concentrates on macro-level permits (zoning, construction, water management), with only 989 genuine water decisions and merely 8 connection refusal cases (0.012%). Household-level connection disputes are virtually absent — confirming the pre-litigation absorption model.

---

## Jurimetric Coding Framework

Applied via regex to the `summary` column of the merged dataset (`water_law_global.csv`).

### Brazil (ementa field)
```python
TEMAS_BR = {
    'tarifa_cobranca':    r'tari[f]a|cobran[cç]a|fatura|débito|inadimpl',
    'interrupcao':        r'interrup[cç]|corte|suspens[aã]o|desligament',
    'danos':              r'dano moral|dano material|indeniza[cç]',
    'conexao_recusa':     r'ligan[cç]|conex[aã]o|acesso[^\w]*rede|negat[^\w]*ligan',
    'irregular':          r'irregular|favela|invas[aã]o|sem escritura|[aá]rea[^\w]*risco',
    'tutela_urgencia':    r'tutela[^\w]*urg|liminar|antecipa[cç]',
    'ministerio_publico': r'minist[eé]rio p[uú]blico|MP[^\w]|ACP|a[cç][aã]o civil p',
    'consumidor':         r'c[oó]d[^\w]*consumidor|CDC|rela[cç][aã]o[^\w]*consumo',
}
```

### Netherlands (inhoudsindicatie field)
```python
TEMAS_NL = {
    'aansluiting':        r'aansluit|aansluitleiding|huisaansluiting',
    'vergunning':         r'vergunning|omgevingsvergunning|watervergunning',
    'heffing':            r'heffing|belasting|waterschapsbelasting|zuiveringsheffing',
    'handhaving':         r'handhaving|dwangsom|last[^\w]*bestuursdwang',
    'drinkwater':         r'drinkwater|drinkwaterleidin|waterbedrijf|waterleidingbedrijf',
    'waterschap':         r'waterschap|hoogheemraadschap|waterkering|dijkgraaf',
    'overstroming':       r'overstroming|inundatie|wateroverlast|dijkdoorbraak',
}
```

### Canada / Ontario (applied — CanLII API + Legal Data Hunter, v0.3.0)
Key themes identified in the 3,218-decision sub-dataset: fisheries and riparian rights (federal resource governance), municipal water service, Safe Drinking Water Act (Ontario), Ontario Water Resources Act. Connection-refusal cases are absent from the coded record — whether this reflects pre-litigation absorption or incomplete text retrieval (86.9% of records are title-only) cannot be determined from current data.

**Future data source:** The **A2AJ Canadian Legal Data** project (Sean Rehaag and Simon Wallace, 2025, \<https://github.com/a2aj-ca/canadian-legal-data\>; API: \<https://github.com/a2aj-ca/a2aj-api-public\>; MCP server: \<https://mcp.a2aj.ca/mcp\>), maintained by Access to Algorithmic Justice (A2AJ) at York University's Osgoode Hall Law School and Toronto Metropolitan University's Lincoln Alexander School of Law (funded by the Law Foundation of Ontario and SSHRC), would allow the 21-category coding engine to be applied to full Canadian decision texts rather than titles. This is the recommended first step for any researcher seeking to extend the Canadian arm of the MDSD into household-access disputes. See `FUTURE_WORK.md` Priority 3A for full implementation notes.

---

## Dataset Schema

Unified schema across all jurisdictions (`water_law_global.csv`):

| Field | Description |
|---|---|
| `country` | Brazil / Netherlands / Canada |
| `tribunal` | Court/tribunal code |
| `court_name` | Full court name |
| `case_id` | ECLI (NL), processo number (BR), citation (CA) |
| `title` | Case title or ECLI |
| `date` | Decision date (YYYY-MM-DD) |
| `year` | Decision year (integer) |
| `case_type` | Procedure type (NL) / class (BR) |
| `chamber` | Reporting chamber / órgão julgador |
| `judge` | Relator / reporting judge |
| `legal_area` | Rechtsgebied (NL) / area (BR) |
| `summary` | Inhoudsindicatie (NL) / ementa (BR) / snippet (CA) |
| `url` | Source URL |

---

## Key Abbreviations

| Abbreviation | Meaning |
|---|---|
| Awb | Algemene wet bestuursrecht (NL General Administrative Law Act) |
| CF/88 | Constituição Federal do Brasil (1988) |
| OWRA | Ontario Water Resources Act |
| SDWA | Safe Drinking Water Act (Ontario) |
| TAC | Termo de Ajustamento de Conduta (Brazil — MP enforcement tool) |
| ANA | Agência Nacional de Águas e Saneamento Básico (Brazil) |
| SNIS | Sistema Nacional de Informações sobre Saneamento (Brazil) |
| RvS | Raad van State (NL Council of State — main administrative appeals court) |
| MDSD | Most Different Systems Design |
| MP | Ministério Público (Brazil) |
| SDG 6 | Sustainable Development Goal 6 — universal water and sanitation |

---

## AI Methodology Statement (final — for preliminary research)

This study integrates Claude (Anthropic) and Antigravity (Google DeepMind) as technical tools within the empirical data collection and processing pipeline. Their roles were clearly defined and limited to verifiable computational tasks, while all substantive legal analysis remained the responsibility of the author. The purpose of using AI in this context was to enable the construction and handling of a large, cross-jurisdictional dataset in a consistent and replicable manner. Antigravity additionally performed a comprehensive repository audit to identify and resolve data contradictions, maintaining dataset consistency.

Claude was primarily used to support the design, implementation, debugging, and iterative refinement of Python-based web scrapers used to collect judicial decisions across Brazil, the Netherlands, and Canada. In Brazil, data collection required interaction with eight State Courts of Justice operating on different technological infrastructures. These included ESAJ systems (São Paulo, Santa Catarina, Acre, and Roraima), Elasticsearch and Angular-based systems (TJDFT), ASP.NET WebForms (TJRJ), PHP and Solr architectures (TJTO), and Rails-based platforms (TJPI). Because documentation was often incomplete or inconsistent, each system required reverse engineering of API endpoints, request parameters, and pagination structures. Across these eight courts, the scraping process produced a total of approximately 8,368 judicial decisions, all related to water law disputes within the defined temporal scope of the study.

For the Netherlands, data was collected through the Rechtspraak Open Data API. A structured scraping process was developed to iterate across ECLI identifiers for nineteen courts, including eleven district courts, four courts of appeal, and the highest administrative and judicial bodies. To ensure relevance, subject-matter filters were applied within administrative law domains, particularly environmental law, using classifications such as bestuursrecht_omgevingsrecht. This allowed the dataset to focus on environmental and water-related disputes within very large corpora that in some instances exceeded 160,000 decisions per court.

In Canada, data collection relied on the CanLII API (version 1). A multi-stage scraping pipeline was constructed to systematically query all available databases, which totalled 409 at the time of collection. The process prioritised appellate and superior courts before extending to specialised tribunals. In addition, a pattern-based approach was used to identify and include twenty-three water, environmental, and energy-related tribunals based on their institutional names. Across all jurisdictions, Claude assisted in diagnosing technical issues, including undocumented API behaviour. One example was the absence of decision dates in certain CanLII API responses, which required deriving the year from citation formats. Claude also supported the implementation of checkpoint and resume functions, which were essential to ensure stability and continuity during long-running scraping processes.

Following data collection, Claude contributed to the design of a unified cross-jurisdictional schema that standardised key variables across all cases. The final structure included fields such as country, tribunal, court name, case identifier, title, date, year, case type, chamber, judge, legal area, summary, and source URL. A dedicated merging script was developed to integrate all datasets into a single format. This process involved harmonising variable names, applying temporal filters for the period between 2016 and 2026, and removing duplicate entries using jurisdiction-specific identifiers, including ECLI codes in the Netherlands, process numbers in Brazil, and citation formats in Canada. The output consisted of consolidated datasets in both CSV and Excel formats.

Claude also supported the development of a jurimetric coding framework based on regular expression matching. This framework was applied to case summaries, including the Brazilian ementa and the Dutch inhoudsindicatie, to classify decisions into thematic categories. These categories included tariff and billing disputes, service interruptions, refusals of infrastructure connection, disputes involving informal settlements, urgent injunctions, and cases involving public prosecutors. The coding dictionaries were adapted to account for linguistic variation, including orthographic differences in Portuguese and compound legal terminology in Dutch. This ensured that the classification process remained consistent across jurisdictions with distinct legal and linguistic characteristics.

The role of AI in this study was strictly limited to data-related functions. Claude did not generate legal interpretations, assess doctrinal questions, or contribute to the development of theoretical frameworks. All analytical components of the research, including the application of the Legal Last Mile framework, the Gatekeeper Thesis, and the Most Different Systems Design methodology, were carried out independently by the author. The AI system functioned solely as a tool to scale data collection, improve consistency, and reduce manual processing constraints in a dataset of 83,596 judicial decisions (v0.3.0, May 2026).

To ensure transparency and replicability, all scraping scripts, data processing code, and final datasets have been made publicly available. This allows the entire data pipeline to be independently reproduced without reliance on AI assistance. The repository is accessible at https://github.com/jrklaus8/water-law-dataset, with an associated DOI of 10.5281/zenodo.19836413.

**Final dataset totals (v0.3.0, May 2026):** Brazil 11,724 decisions (8 Tribunais de Justiça, 2016–2026, including 200 historical TJSP cases 1997–2015), Canada 3,218 decisions (CanLII API + Legal Data Hunter), Netherlands 68,654 decisions (Rechtspraak Open Data — all district courts, Raad van State, CBb, and GHARL). Global total: **83,596 decisions**. Deposited at Harvard Dataverse (doi:10.7910/DVN/C9PEFS) and Zenodo (doi:10.5281/zenodo.19836413).

---

## Open Access

- **Dataset DOI:** [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413)
- **PyPI package:** [water-law-dataset](https://pypi.org/project/water-law-dataset/)
- **GitHub:** [jrklaus8/water-law-dataset](https://github.com/jrklaus8/water-law-dataset)
