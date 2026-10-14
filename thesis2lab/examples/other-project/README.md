# Adopting Thesis2Lab for another project

1. Copy the repository. Delete `research/`, `experiments/EXP-*` and `data/{public,synthetic,metadata}` content.
2. Replace `project.config.json` with your own (see this folder's example; the labels map your jurisdictions, topics and categories to display names).
3. Edit `research/thesis/thesis.json` with your chapters (any number).
4. Register sources, add datasets, then experiments, following `docs/ADDING_RESEARCH.md`.
5. `npm run build`. Nothing in `app/src` names a thesis, discipline, jurisdiction or chapter.

`project.config.json` here is validated by `npm run validate:schemas`, so it cannot silently drift from the schema.
