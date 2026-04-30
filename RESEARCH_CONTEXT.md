# Research Context — The Legal Last Mile

## Dissertation

**Title:** The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance  
**Author:** Claudio Klaus  
**Citation style:** OSCOLA  
**Method:** Most Different Systems Design (MDSD) — Netherlands · Canada (Ontario) · Brazil

This dissertation investigates how administrative law frameworks condition access to sanitation infrastructure at the *point of connection* across three jurisdictions that diverge profoundly in legal tradition and institutional architecture yet converge on a shared outcome: the administrative exclusion of marginalized households from services that are, in physical terms, within reach.

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

This repository contains the scrapers and data for the jurimetric backbone of the dissertation: **12,310+ judicial decisions** from Brazil and the Netherlands (Canada in progress), coded via regex on decision summaries to test the Legal Last Mile theory.

### Published Findings (UNIARP 2026 Conference)

**Brazil (11,524 decisions):**

| Theme | Share |
|---|---|
| Tariffs / billing disputes | 59% |
| Moral and material damages | 41% |
| Service interruptions | 31% |
| Connection refusal | 9% |
| Irregular settlements / favelas | 1.3% |
| Urgency injunctions granted | 29% |

Courts process the *symptoms* of exclusion; the root matrix of ineligibility is almost never litigated. This validates the Administrative Ghost: the 1.3% irregular settlement rate and 9% connection-refusal rate reveal the tip of a much larger excluded population that never reaches courts at all.

**Netherlands (786 decisions, Raad van State):**  
The RvS concentrates on macro-level permits (zoning, construction, water management). Household-level connection disputes are virtually absent — confirming the pre-litigation absorption model.

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

### Canada / Ontario (to be applied when CanLII data available)
Key themes to look for: connection refusal, Indigenous water rights, municipal utility disconnection, environmental tribunal decisions, Safe Drinking Water Act (Ontario), Ontario Water Resources Act.

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

## Open Access

- **Dataset DOI:** [10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413)
- **PyPI package:** [water-law-dataset](https://pypi.org/project/water-law-dataset/)
- **GitHub:** [jrklaus8/water-law-dataset](https://github.com/jrklaus8/water-law-dataset)
