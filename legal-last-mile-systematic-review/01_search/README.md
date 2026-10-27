# 01_search — how the records were found

**Start with:** `../SEARCH_PROTOCOL.md` (the plan and the exact search strings) and `database_strategies/` (one file per database, with the string as actually run).

| Folder or file | What it is |
|---|---|
| `database_strategies/` | Search strategy per database: Scopus, Web of Science, ProQuest Sociological Abstracts, JSTOR/Google Scholar, HeinOnline, CanLII, Rechtspraak, Brazilian legal databases, grey literature, PubMed, Westlaw/Lexis. Not every strategy was run: SSRN and Westlaw/Lexis were never searched |
| `raw_exports/` | The untouched exports, named `SEARCH_{NNN}_{DATABASE}_{date}.csv`. Never edited |
| `deduplicated/deduplicated_records.csv` | The unique records after merging duplicates |
| `deduplicated/merge_log.csv` | Every merge, so a reader can see why two records became one |
| `deduplicated/*_audit_2026-09-28.md` | Two audits of the de-duplication (DOI variants; title/author) |
| `cowork_instructions_*`, `EXECUTION_CHECKLIST.md` | The instructions given to the AI browser assistant that relayed some database searches the researcher ran through institutional access |

**Disclosed gaps:** SSRN and Westlaw/Lexis were never searched; HeinOnline produced one usable record; only part of the JSTOR results was exported. Searching was closed on 2026-09-11 by researcher decision. See `../README.md` → "Known limitations".

**Who did it:** the researcher ran every database search; scripts in `../code/search/` did the matching and merging.
