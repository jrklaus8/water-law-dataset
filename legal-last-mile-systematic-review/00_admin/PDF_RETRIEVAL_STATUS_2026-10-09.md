# Full-text retrieval round, 2026-10-09: what the browser agent found and what is left for the researcher

Source: the agent's own tracker (`ZZ_TRACKER_retrieval_status_all_34_2026-10-09.txt` and `ZZ_TRACKER_outcome_to_record_2026-10-09.csv`, in the Drive inbox); per-paper outcomes are in `02_screening/full_text/PDF_RETRIEVAL_OUTCOMES_2026-10-09.csv`. Nothing was sent: the agent drafted six author requests and two interlibrary-loan requests (in its session output, `DRAFT_emails_and_browser_checklist.md`).

## Done

- **S027** (Fanaian 2025, WIREs Water): published open-access version retrieved; AMSTAR 2 appraised, Critically Low. All 23 reviews are now rated.
- **S393** (Curtis 2019): the browser agent supplied the medRxiv **preprint**; the researcher later dropped the **published** BMJ Global Health version. Both were read and match the extraction; the item-level CASP rating was re-answered on the published text.
- **RAB6AA06D8E9D** (Carranza 2025): settled without a file. Europe PMC PMC12848418 is an abstract with no body; no full article exists; the E09 exclusion stands.
- **Second round, later on 2026-10-09: the researcher dropped twelve PDFs in the Drive inbox** (list and per-file actions: `02_screening/full_text/PDF_RETRIEVAL_RECEIVED_2026-10-09.csv`, `00_admin/DRIVE_INBOX_BATCH4_LOG_2026-10-09.md`):
  - **A19 RF5C6D981DB3B** (Chiapas): exclusion confirmed on the full text (E04 fits better than E01); a proposal row, no decision changed.
  - **A22 S513** (McGranahan 2015): a conceptual argument with no stated data or method; fails criterion 3 (proposal only).
  - **Re-extracted from full text:** S271, S304, S310, S315, S352 (abstract-only rows; S310 and S315 are scanned images, read page by page) and S395, S415, S416, S417 (extracted before without a read full text). The abstract-only list fell from 16 to 11.

## Left for the researcher (all in a normal browser; the agent was blocked only by bot checks). 20 papers: 5 + 2 + 4 + 9

**Group 1: free at the publisher (no login or payment needed; stop if payment is asked), 5 still to fetch**

- S280 https://doi.org/10.1007/978-3-319-28643-3_6
- S401 https://www.tandfonline.com/doi/pdf/10.1080/23311886.2023.2208934
- S391 https://www.matec-conferences.org/articles/matecconf/pdf/2018/18/matecconf_ijcaet-isampe2018_01023.pdf
- RCB78D4EF3652 https://www.cairn.info/revue-flux-2009-2-page-26.htm
- S400 https://www.cairn.info/revue-flux-2009-2-page-94.htm

**Group 2: repository copy exists; open the page and click the file, 2 still to fetch**

- S390 https://hdl.handle.net/10362/15612 (submitted)
- S284 https://hdl.handle.net/10072/392162 (submitted)

(Received and read since the first version of this file: S513, RF5C6D981DB3B, S352, S416, S415, S395, S417 and the published S393 from Group 1; S304, S315, S310 and S271 from Group 2.)

**Group 3: no open copy anywhere; interlibrary loan or an author request (drafts exist)**

- S340 Mubecua & Nojiyeza 2025 (author emails drafted)
- R803988411D3E, the Routledge edited book (chapter level; ILL drafted)
- S380 Baron & Maillefert 2011 and S365 Kharmylliem & Kipgen 2021 (Unpaywall: closed; ILL needed)

**Group 4: do not chase.** The "green open access" flag at research.wur.nl (also in OpenAlex and Semantic Scholar) is a false positive: those records carry no file. Affected: S264, S314, R155FFF508359, RA1F6E143593E, R803988411D3E (tier A) and S300, S317, S256, S290, S301 (tier B). The publisher or an author request is the only route; UvA DARE for S264 is metadata-only too.

Upload each file to the Drive inbox with the name in `PDF_RETRIEVAL_TARGETS_2026-10-09.csv` (`file_name_to_use`).
