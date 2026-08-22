# Brazilian legal and regulatory database strategies

Covers Brazilian state court databases (TJ e-SAJ / PJe / Elasticsearch
portals, already used by `../../scrapers/brazil/`), and the regulatory/
administrative-data sources ANA (Agência Nacional de Águas e Saneamento
Básico) and SNIS (Sistema Nacional de Informações sobre Saneamento). As with
CanLII and Rechtspraak.nl, court-database hits feed the doctrinal/jurimetric
strand, not the household-level empirical evidence base by default.

## State court portals

```
("ligação domiciliar" OR "ligação predial" OR "ligação de água" OR
"ligação de esgoto" OR "acesso à água" OR "acesso ao saneamento") AND
("regularização fundiária" OR "assentamento informal" OR "assentamentos
informais" OR "ocupação irregular" OR "aglomerado subnormal" OR favela OR
"barreira administrativa" OR "barreiras administrativas" OR "barreira
legal" OR elegibilidade OR "exigência documental" OR licenciamento)
```

## ANA / SNIS (regulatory and administrative data, not case law)

ANA and SNIS are primarily **administrative datasets** (coverage,
investment, tariff, and service-quality indicators reported by utilities),
not searchable literature databases in the Scopus/WoS sense. Treat them as
candidate **grey-literature / administrative-record sources**:

- Search ANA's regulatory reports and SNIS's annual diagnostic reports
  (*Diagnóstico dos Serviços de Água e Esgotos*) for any analysis that ties
  legal/administrative eligibility conditions (documentation, land-tenure
  regularization, service-area definitions) to household- or
  municipality-level coverage outcomes.
- Any quantitative table extracted from ANA/SNIS reports is
  municipality-level administrative data, not a peer-reviewed study — code
  `peer_reviewed = false`, `unit_of_analysis = municipality`, and do not
  treat it as interchangeable with a household-level primary study when
  assessing quantitative-synthesis feasibility (`ANALYSIS_PLAN.md`).

## Notes

- "saneamento básico" in Brazilian law is a defined term covering water
  supply, sewage, drainage, and solid waste — confirm at screening which
  specific service (water supply vs. sewage vs. drainage vs. waste) a given
  source actually addresses, per the scope-discipline rule
  (`PROJECT_SPEC.md` §2).
- Status: **not yet executed.**
