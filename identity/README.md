# Entity identity layer

Machine-readable identity for the author, Claudio Klaus, so search engines can tie this
repository's public pages to one person. It does not change what this project is.

- `entity.json` is the single source of truth: person, identifiers, profiles, podcast, works, and an `unresolved` list.
- `utils/entity_identity.py` builds JSON-LD and writes it into `docs/index.html` (the dashboard) between `entity-jsonld` markers.
- `tests/test_entity_identity.py` checks the canonical `@id`, separation of person and podcast, unique profile URLs, the ORCID checksum, JSON validity and that the page is in sync.

```bash
python utils/entity_identity.py --print    # inspect
python utils/entity_identity.py --inject   # update docs/index.html
python utils/entity_identity.py --check    # CI-style staleness check
python -m unittest discover -s tests
```

## Status policy

Each entry carries a `status`. Only `fetched_verified`, `user_asserted` and `search_corroborated` are published.
Candidates are kept out of production output; add them with status `candidate` or list them under `unresolved`.
`user_asserted` means supplied by the author but not fetched by the tool that wrote the file.

## Scope

The canonical person `@id` is `https://claudioklaus.com/#person`. This repo does not depend on that site.
The dataset page is the only page with markup. It declares the person as `creator` of the Dataset
(the page footer names the author). `docs/atlas/` names no author, so it carries no person markup.
Valid markup does not guarantee a Knowledge Panel. Validate with https://validator.schema.org/ and Google's Rich Results Test after deployment.
