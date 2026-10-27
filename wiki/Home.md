# Legal Last Mile — Project Wiki

Welcome to the documentation wiki for the **Legal Last Mile** research project. It documents two connected pieces of work that share one research question — how administrative law conditions household access to water and sanitation:

1. the **Global Water Law Judicial Decisions Dataset** (83,596 court decisions from Brazil, Canada and the Netherlands), and
2. the **AI-assisted systematic review** *The Legal Last Mile* (1,072 included studies; preliminary, interim release).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19836413.svg)](https://doi.org/10.5281/zenodo.19836413)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Live resources

| Resource | Link |
|----------|------|
| Interactive dashboard (the dataset) | https://jrklaus8.github.io/water-law-dataset/ |
| **Legal Last Mile Atlas** (interactive preliminary results of the systematic review) | https://jrklaus8.github.io/water-law-dataset/atlas/ |
| Preliminary research PDF | [docs/The_Legal_Last_Mile_Research.pdf](https://github.com/jrklaus8/water-law-dataset/blob/main/docs/The_Legal_Last_Mile_Research.pdf) |
| Source code and scrapers | https://github.com/jrklaus8/water-law-dataset |

---

## 1. The dataset (version 0.3.0)

A comparative jurimetric corpus of **83,596 judicial decisions** addressing water law, sanitation access and water governance across three jurisdictions:

| Country | Cases | Period |
|---------|-------|--------|
| 🇧🇷 Brazil | 11,724 | 2016–2026 (includes 200 historical TJSP decisions 1997–2015) |
| 🇨🇦 Canada | 3,218 | 2016–2026 |
| 🇳🇱 Netherlands | 68,654 | 2016–2026 |

Since version 0.3.0 the coding engine separates genuine water-law decisions from broad-search false positives: **67,703 decisions are coded `not_water_related`** (98.56% of the Netherlands), and the genuine residual `other_water` category falls to 6,904 (8.3%). See [[Validation]] for the audit behind this and [[Key Findings]] for the results.

## 2. The systematic review (interim release 0.2.0-interim)

*The Legal Last Mile: an AI-assisted systematic review* is the companion project to the doctoral dissertation. It screened **34,594 records**, assessed **2,277 full texts** and includes **1,072 studies**; no effect could be pooled, so the evidence is synthesised by vote counting of direction (SWiM). It is **preliminary and only partly human-verified**: an AI did most of the screening, extraction and appraisal, and a human checked only part of it. See [[Systematic Review]].

---

## Quick navigation

| Page | Contents |
|------|----------|
| [[Systematic Review]] | The AI-assisted systematic review: status, flow, results, verification, limits |
| [[Dataset Overview]] | Scope, sources and data collection for the court-decisions dataset |
| [[Jurimetric Coding]] | The coded variables and the v0.3.0 engine |
| [[Validation]] | Residual audit, precision/recall and the LLM-assisted reproducibility audit |
| [[Scrapers]] | How the scrapers work per jurisdiction |
| [[Key Findings]] | Jurimetric results by country (v0.3.0) |
| [[Repositories]] | Where to download the data |
| [[AI Disclosure]] | How Claude (Anthropic) and Antigravity were used in this project |
| [[Contributing]] | How to contribute, audit or challenge a result |
| [[Citation]] | How to cite the dataset, the code and the review |

---

## Repository archives (dataset)

| Repository | Link | DOI |
|------------|------|-----|
| Zenodo | https://doi.org/10.5281/zenodo.19836413 | `10.5281/zenodo.19836413` |
| Harvard Dataverse | https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/C9PEFS | `10.7910/DVN/C9PEFS` |
| DANS Data Station SSH | https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/SS/RVDBUF | `10.17026/SS/RVDBUF` |
| OSF | https://osf.io/admrq | — |

The systematic review has **no DOI yet**; it is an interim, preliminary release on GitHub (see [[Citation]]).

---

*Maintained by Claudio Klaus Junior · [juniorklaus8@gmail.com](mailto:juniorklaus8@gmail.com)*
