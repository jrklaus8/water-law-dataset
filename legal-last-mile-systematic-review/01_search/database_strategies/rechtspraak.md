# Rechtspraak.nl search strategy

Rechtspraak.nl (and its Open Data API, already used by
`../../scrapers/netherlands/`) supports `AND`/`OR`, phrase quotes, and `*`
truncation in its search interface. As with CanLII (`canlii.md`), this is a
legal/institutional repository search feeding the doctrinal/jurimetric
strand, not the household-level empirical evidence base — classify any hit
used as review evidence as `study_design_class = doctrinal` or `jurimetric`.

```
(wateraansluiting OR aansluiting OR aansluitplicht OR rioolaansluiting OR
drinkwater OR drinkwatervoorziening) AND (vergunning OR
omgevingsvergunning OR bestuursrecht OR "administratieve lasten" OR
beleidsregels OR "discretionaire bevoegdheid" OR handhaving OR toegang)
```

Secondary query for the vulnerable-household / informal-occupation strand:

```
(kwetsbare huishoudens OR "informele bewoning" OR woonadres OR
inschrijving OR BRP OR BSN) AND (drinkwater OR aansluiting OR riolering)
```

## Notes

- As documented in `../../RESEARCH_CONTEXT.md` and
  `../../SUPERVISOR_REPORT_v0.3.0.md`, the existing Dutch judicial corpus
  (68,654 collected decisions) already has known filtering issues; do not
  assume this search's hit set is clean, and do not simply reuse the
  existing scraped corpus as a stand-in for a fresh, protocol-driven search
  — run this search independently and log it under its own `search_id`.
- Per `SEARCH_PROTOCOL.md` §3, distinguish at extraction whether a decision
  concerns (1) a formal legal requirement, (2) a utility's practical
  requirement, or (3) an indirect administrative-system requirement (BRP/BSN
  registration) — do not treat a registration-system dispute as a direct
  water-connection eligibility dispute without checking which of the three
  it actually is.
- Status: **not yet executed.**
