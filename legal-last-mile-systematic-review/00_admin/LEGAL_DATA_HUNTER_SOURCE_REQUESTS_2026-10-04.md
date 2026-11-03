# Legal Data Hunter: what we needed from them, and a reply you can paste

*Written 2026-10-04 from the git history and a live check of their catalogue. The history is not in this session's chat (it was an earlier session): it is in commits `e0b56ba` and `5cf0f37` (2026-09-17) of this repository and in `dissertation_agent/currency-notes.json` at commit `5cf0f37`.*

## What happened earlier

- The thesis currency check ("Direito, Saneamento e Sustentabilidade") needed to confirm two **Santa Catarina state laws**: Lei 14.675/2009 (state environmental code) and Lei 17.717/2019 (state sanitation policy).
- Legal Data Hunter's `resolve_reference` returned `resolved: false` for both, and a full-text search returned only federal and municipal-gazette noise. `discover_sources` showed why: **no Santa Catarina state legislature source and no TJSC (state court) case law**.
- A coverage-gap report was filed on 2026-09-17, `report_id fd50ee7d-72b0-42c1-8d25-7022d5a1d084`, asking for ALESC legislation and TJSC case law. (The Lei 17.717/2019 citation was later confirmed wrong by reading ALESC's own portal, so that part no longer depends on them.)
- The Canada work used their semantic search over CanLII and is acknowledged in the README; nothing is outstanding there.
- The systematic review (`legal-last-mile-systematic-review/`) uses peer-reviewed literature, not court data, so it needs nothing from them.

## Live check, 2026-10-04 (their Brazil catalogue, `discover_sources BR`)

- Still **no** Santa Catarina legislature (ALESC) and **no** TJSC. Also absent: TJSP, TJRJ, TJRR, TJPI, TJTO and the Supreme Federal Court (STF). TJAC and TJAM hold 15 documents each (2024-2026); TJDFT, TJPR, TJBA, STJ, TCU and the federal regional courts are well covered.
- **Federal legislation (`BR/Planalto`) starts in 2022** (1,541 documents, 2022-2026), so pre-2022 federal laws are missing.
- `resolve_reference` returned not found for **Lei 11.445/2007** (national sanitation law) and for **Lei 14.675/2009 (SC)**.

## Reply to their four questions (paste)

**Which source, and the official link**

| # | Source | Official link | Years we need | What we look for there |
|---|---|---|---|---|
| 1 | Santa Catarina state legislation, ALESC (Assembleia Legislativa) | https://leis.alesc.sc.gov.br/ | 2009 and 2019 at minimum; ideally all state laws and decrees | State sanitation policy and the state environmental code (Lei 14.675/2009) with their amendments; which law number actually holds the state sanitation policy |
| 2 | TJSC case law (Tribunal de Justiça de Santa Catarina) | https://busca.tjsc.jus.br/jurisprudencia/ | 2016-2026 (we hold 1,224 TJSC water-law decisions from this portal) | Water and sewage connection, tariff, concession and disconnection disputes, e.g. the CASAN versus BRK Ambiental concession for Caçador, upheld by TJSC in March 2022 |
| 3 | Federal legislation before 2022 (`BR/Planalto` already has 2022-2026) | https://www.planalto.gov.br/ccivil_03/leis/ | 1990-2021 | Lei 11.445/2007 (sanitation law), Lei 9.433/1997 (water resources policy), Lei 14.026/2020 (sanitation framework update) and their regulations |
| 4 | State courts of São Paulo, Rio de Janeiro, Roraima, Piauí, Tocantins | TJSP https://esaj.tjsp.jus.br/cjsg/ · TJRJ https://www3.tjrj.jus.br/ejuris/ConsultarJurisprudencia.aspx · TJRR https://jurisprudencia.tjrr.jus.br/ · TJPI https://jurisprudencia.tjpi.jus.br/ · TJTO https://jurisprudencia.tjto.jus.br/ | 2016-2026 (TJSP also 1997-2015) | Water and sanitation cases (connection refusal, tariffs, concessions, public civil actions on supply); these are the other courts of our Brazil collection of 11,724 decisions |

**Source already there but years missing:** `BR/Planalto` (federal legislation) covers only 2022-2026; `BR/TJAC` and `BR/TJAM` hold 15 documents each.

**Existing report to link:** `fd50ee7d-72b0-42c1-8d25-7022d5a1d084` (filed 2026-09-17, still unresolved for #1 and #2).

**Suggested short version (one message):**
> Brazil / water and sanitation law. Missing sources: (1) Santa Catarina state legislation, ALESC, https://leis.alesc.sc.gov.br/ (need 2009 and 2019 at least); (2) TJSC case law, https://busca.tjsc.jus.br/jurisprudencia/ (2016-2026); (3) federal legislation before 2022 on planalto.gov.br (BR/Planalto starts in 2022; I need Lei 11.445/2007, 9.433/1997, 14.026/2020); (4) TJSP, TJRJ, TJRR, TJPI and TJTO jurisprudence portals (2016-2026). I look for water and sanitation connection, tariff and concession disputes and the laws behind them. Earlier report id: fd50ee7d-72b0-42c1-8d25-7022d5a1d084.
