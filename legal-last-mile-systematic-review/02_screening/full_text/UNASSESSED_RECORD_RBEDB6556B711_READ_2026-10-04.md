# Unassessed record read from page images — Olmstead 2004, "Thirsty Colonias" (RBEDB6556B711), 2026-10-04

*Status: **assessment proposal only; no database was changed.** Screening closed on 2026-09-28, so adding this record is a researcher decision (`00_admin/DECISIONS_AND_OPEN_ITEMS.md` A15).*

**What happened.** The screening database lists this record as `not_retrievable` with a note that the retrieved PDF was only JSTOR terms boilerplate. The file in the researcher's Drive (`RBEDB6556B711__Thirsty colonias Rate regulation and the provision of water service.pdf`, 2.2 MB, 16 pages) is in fact the complete article (Land Economics 80(1):136-150, 2004) as scanned page images with no text layer. The AI downloaded it, rendered the pages and read pages 2, 4, 6-8 and 11-15 (introduction, institutions, Tables 1 and 4-6, data limitations, conclusion) as images; pages 3, 5, 9 and 10 (data description and the model specification) were **not** read, so every number below is as printed on the pages read. `R0908697F9FE5` (156 MB) cannot be downloaded through the available Drive tool (10 MB limit).

**Eligibility against the criteria (AI judgement).** Water access: yes (probability that a colonia has obtained drinking-water service). Legal/administrative factor: yes (price regulation of the provider's rates by a municipality or the state regulator; county enforcement of the model subdivision rules; legal service-area certificates of convenience and necessity; no mandatory universal service). Empirical: yes (probit models on 781 colonias in four Texas border counties). Recommendation: **include**; it would be a strong Family-C-type row (administrative/regulatory barriers and price) and the clearest US evidence on rate regulation and service extension.

**Proposed extraction (from the pages read).**

| Field | Value |
|---|---|
| Design | cross-sectional observational probit analysis of colonias merged from the Texas Water Development Board and Attorney General databases; subset of available data; sample-selection and omitted-variable limits acknowledged by the author |
| Setting / n | Cameron, El Paso, Hidalgo and Webb counties, Texas; 781 colonias (267,384 residents in 1996; 18.9% without water service) |
| Outcome | colonia had obtained water service by 1996 (an upper bound on safe access; water quality not measured) |
| Model A (provider type vs for-profit private) | non-profit water supply corporation -0.3795 (p = 0.535); municipal -1.9433 (p = 0.051); district/county -1.1105 (p = 0.035); wells/unknown -2.3819 (p = 0.007) |
| Model B, rate regulation | provider subject to price regulation (pricereg): coefficient -1.1858, SE 0.4163, p = 0.004, marginal effect -0.2718 (27 percentage points lower probability of service); rural-development funding access not significant (0.2162, p = 0.401) |
| County enforcement | county cited for lax enforcement of the model subdivision rules (Hidalgo): coefficient -7.5722, p = 0.004, marginal effect -0.6943 (the text says 69% less likely than in the three enforcing counties) |
| Other | income +0.1410 (p = 0.001), population (ln) +0.3776, per-capita income effect about 2.1 points per $1,000 (Model B marginal 0.0208) |
| Author's conclusion | rate regulation, intended to make service affordable, may reduce coverage for the poor in the absence of a universal-service mandate; pricing flexibility matters more than public infrastructure subsidies |
| Proposed appraisal tool | JBI Cross-Sectional (observational; not an intervention study) with limitations: data subset, no water-quality data, omitted political variables; rating to be answered after reading pages 3, 5, 9, 10 |
| Direction (Family C coding) | negative (price regulation associated with lower service coverage) |

**If the researcher approves.** Add the record to the full-text decision table as `include` with a dated note, extract it with a dated script (the AI can do this in the usual way), add an `effect_sizes.csv` Family C row, and regenerate every figure; every count (1,159 included, 1,383 unassessed, 62 effect-size rows, Family C k) changes by one.
