# Grey literature search notes

Source types to search: government reports; regulatory decisions; municipal
reports; utility policies; NGO reports; international-organization
publications (e.g. World Bank, UN-Habitat, WHO/UNICEF JMP); court databases
(see `canlii.md`, `rechtspraak.md`, `brazil_legal_databases.md`);
regulator databases (ANA/SNIS — see `brazil_legal_databases.md`);
parliamentary/legislative reports; official consultation documents;
institutional repositories (university theses/dissertations, think-tank
publications).

## Search approach

- Use each organization's own search interface with the Block A/B/C terms
  from `SEARCH_PROTOCOL.md` §2, simplified to short phrases (most grey-lit
  search tools do not support nested Boolean).
- For international organizations, prioritize country-specific pages for
  Brazil, the Netherlands, and Canada rather than a single global search.
- Use Google's `site:` operator against known institutional domains (e.g.
  `site:worldbank.org`, `site:un-habitat.org`) as a supplementary technique,
  logged as its own `search_id`.

## Coding requirement

Every grey-literature record that is included must be coded
`peer_reviewed = false` and `publication_type` set to its actual type
(government report, NGO report, working paper, thesis, etc.) in the
extraction database. Grey literature is eligible for the systematic
evidence map and the qualitative/mechanism synthesis; it is **not**
automatically eligible for quantitative pooling alongside peer-reviewed
evidence — that determination is made per synthesis family in
`ANALYSIS_PLAN.md`, not assumed here.

## Status

Not yet executed. No grey-literature sources have been searched.
