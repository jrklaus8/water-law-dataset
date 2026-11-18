# Drive inbox, fourth batch (2026-10-09): twelve PDFs after the browser-agent round

The researcher dropped twelve PDFs in the Drive inbox folder (`Sep 26 2026`) after the retrieval brief (`PDF_RETRIEVAL_AGENT_BRIEF_2026-10-09.md`). The AI read each in the session and moved it to the Drive folder `Processed`, renaming it with its study or record id. Two of them (`content (2).pdf`, `content (3).pdf`) are scanned images without a text layer; they were read page by page as images, so their table values are page-image readings, not machine extraction. No PDF is committed to the repository. Outputs: `process_drive_inbox_2026-10-09b.py` (this script), nine new JSONs in `reextract_2026-10-04/` and the rows listed below.

| Study or record | Tier | Drive file as dropped | Name in Processed | What it is | Pages | What was done |
|---|---|---|---|---|---|---|
| S513 | A | main.pdf | S513_McGranahan_2015_Realizing_the_right_to_sanitation_in_deprived_urban_communities.pdf | World Development 68:242-253 (2015), open-access journal PDF | 12 | A22 verdict: fails criterion 3 (conceptual; proposal only); extraction row filled in |
| RF5C6D981DB3B | A | s10113-022-01993-1.pdf | RF5C6D981DB3B__Inequality_water_accessibility_and_health_impacts_in_Chiapas_Mexico.pdf | Regional Environmental Change 23:3 (2023), Springer journal PDF | 13 | A19 verdict: exclusion confirmed (E04 fits better than E01; proposal only) |
| S352 | B | wamuchiru-2017-beyond-the-networked-city-situated-practices-of-citizenship-and-grassroots-agency-in-water.pdf | S352_Wamuchiru_2017_Beyond_the_networked_city_Chamazi_Dar_es_Salaam.pdf | Environment & Urbanization 29(2):551-566 (2017), journal PDF | 16 | abstract-only row re-extracted; CASP re-answered |
| S271 | B | joshi2011.pdf | S271_Joshi_2011_Health_hygiene_and_appropriate_sanitation.pdf | Environment & Urbanization 23(1):91-111 (2011), journal PDF | 21 | abstract-only row re-extracted; CASP re-answered |
| S304 | B | PDF_PersistantProblems2012.pdf | S304_Ioris_2012_Persistent_water_problems_of_Lima_author_final_draft.pdf | Singapore J Trop Geogr 33(3):335-350 (2012), the author's final draft from the Edinburgh repository |  | abstract-only row re-extracted; CASP re-answered; the typeset article was not read |
| S310 | B | content (2).pdf | S310_Flores_2013_Monitoring_access_to_water_Nicaragua_scanned_image.pdf | Int J Water Resources Development 29(4) (2013), scanned image PDF without a text layer | 17 | abstract-only row re-extracted from page images; MMAT not re-answered (tool fit arguable, A11) |
| S315 | B | content (3).pdf | S315_Jimenez_2010_Local_government_and_the_human_right_to_water_Tanzania_scanned_image.pdf | Natural Resources Forum 34(2):93-105 (2010), scanned image PDF without a text layer | 13 | abstract-only row re-extracted from page images; CASP re-answered |
| S416 | C | 1573062X.2012.709254.pdf | S416_Roy_2013_Negotiating_marginalities_right_to_water_in_Delhi.pdf | Urban Water Journal 10(2):97-104 (2013), journal PDF | 8 | extraction checked and fields filled; CASP re-answered (no methods section) |
| S393 | C | e001892.full.pdf | S393_Curtis_2019_Clean_India_campaign_BMJ_Global_Health_published_version.pdf | BMJ Global Health 4:e001892 (2019), published open-access version |  | matches the preprint checked earlier; CASP re-answered on the published text |
| S395 | C | bioconf_sage-grace2024_03002.pdf | S395_Lutfia_2024_Community_based_rural_water_supply_Jambon_Village.pdf | BIO Web of Conferences 144:03002 (2024), conference paper | 12 | extraction checked and fields filled; MMAT re-answered (5.5 = No; tables and text disagree) |
| S417 | C | pdf.pdf | S417_Hacker_2025_WASH_for_unsheltered_individuals_West_Coast_US.pdf | Environ. Res.: Infrastruct. Sustain. 5:025006 (2025), open-access journal PDF |  | extraction checked and fields filled; CASP re-answered |
| S415 | C | 23251042.2026.2666400.pdf | S415_Ward_2026_Values_at_the_tap_organizational_culture_and_water_unaffordability.pdf | Environmental Sociology (online 2 May 2026), journal PDF |  | extraction checked and fields filled; CASP re-answered |

## Two decisions the full texts raise (proposals only; screening is closed, A15)

- **A19, RF5C6D981DB3B (Chiapas, E01):** exclusion confirmed on the full text; E04 (wrong outcome) is the better code. Three of the nine A19 records still have no full text: R155FFF508359, RA1F6E143593E and R803988411D3E.
- **A22, S513 (McGranahan 2015):** a conceptual and policy argument with no stated data or method; fails criterion 3. Three A22 includes still need a full text: S264, S314, S340.

## Things worth a human look

- S310 (17-page scan) and S315 (13-page scan) were read from images: their numbers are an AI reading of table images.
- S310 and S285 (same Nicaraguan national study, same research group) and S315 and S311 (Same District, Tanzania; same research group) probably share underlying data. They were not added to `linked_reports_2026-09-28.csv`; that is a researcher decision.
- S395 (Jambon Village): the paper's own tables disagree (Table 6 against Table 7 dimension totals; tariff and water-quantity percentages differ between text and Conclusion), so its figures should be quoted with care.
- S304 is the author's final draft, not the typeset article.
