# CanLII search strategy

CanLII's search supports `AND`/`OR`/`NOT`, phrase quotes, and `*`
truncation. This is a **legal/institutional repository** search (per
`SEARCH_PROTOCOL.md` §1), not an academic-literature search — it surfaces
primary case law and, via CanLII Connects, secondary commentary. Records
found here feed the doctrinal/jurimetric side of the project and the
existing judicial dataset (`../../RESEARCH_CONTEXT.md`), not the
household-level empirical evidence base — do not merge CanLII hits directly
into the systematic-review screening database without first classifying
them as `study_design_class = doctrinal` or `jurimetric` (never
`observational`/`experimental`) per `PRISMA_WORKFLOW.md` §"Evidence
classification matrix".

```
("water connection" OR "sewer connection" OR "municipal water" OR
"municipal sewer" OR "water service" OR "sewage service") AND ("service
area" OR "building permit" OR "planning approval" OR zoning OR "municipal
by law" OR "municipal discretion" OR "connection refusal" OR "service
refusal" OR "administrative burden" OR "procedural fairness")
```

Run a second, separate query for the First Nations / federal jurisdiction
strand, kept distinct per the jurisdictional-discipline rule in
`SEARCH_PROTOCOL.md` §3:

```
("First Nations" OR "Indigenous water" OR "drinking water advisory") AND
("water connection" OR "water service" OR "safe drinking water")
```

## Notes

- CanLII is separate from the CanLII data already used for the Global Water
  Law Judicial Decisions Dataset (`../../scrapers/canada/`). Any case found
  through this search that is *also* being used as an evidence source in the
  systematic review (e.g. a decision containing empirical findings about
  administrative practice, or a decision whose reasons are being extracted
  as a legal-institutional evidence source per `RISK_OF_BIAS.md`) must be
  recorded with its own `study_id`, distinct from its row in the judicial
  dataset — the two datasets are never merged (`PROJECT_SPEC.md` §9).
- Status: **not yet executed.**
