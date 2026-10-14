# Adding new thesis material

Nothing here needs an AI. Do the steps in order and stop at any failure.

## 1. A new file (chapter, article, dataset, method note)
```
python3 pipelines/ingest/register_source.py path/to/file --title "Chapter 2 draft" --kind chapter --copyright own_work_unpublished
```
Creates `research/sources/SRC-*.json` with checksum, format and extraction status. The file is only read. Private files: add `--private`. Never place restricted files in this repository.

## 2. Record what it says
Add claims under `research/claims/CLM-*.json` (text, source, exact locator, chapter, `review_status: "unreviewed"`). Add methods under `research/methods/`. Add the chapter to `research/thesis/thesis.json`. Use stable ids, not file names.

## 3. A dataset
Put the file in `data/public/` (redistribution allowed) or `data/synthetic/`. Create `data/metadata/DS-*.json` with licence, privacy status, permitted uses, variables and the SHA-256. Pseudonymise identifiers when needed (see `pipelines/ingest/import_water_law_validation.py`).

## 4. A new experiment
1. Copy `experiments/EXP-001/` to the next number. Edit `manifest.json`: question, sources, dataset ids, runner, parameters, honest `reproducibility_status`, limitations.
2. Use an existing runner (`descriptive_table`, `coder_agreement`) or add one in `app/src/research/runners.ts`.
3. Write `tests/reference_impl.py` as an independent implementation and `references/reference_outputs.json` with tolerances and provenance. Prefer original published or generated values.
4. `npm run validate:schemas && npm run validate:experiments`. The experiment appears in the site automatically. No navigation code changes.

## 5. After any change
`npm run changes` lists stale validations and changed sources. `npm run validate:experiments` regenerates reports for what changed. Review the diff of `validation/reports/`. Then `npm run build`.

## 6. Human sign-off and release
A reviewer writes `validation/reviews/EXP-nnn.json` with the current `inputs_digest`. Then `npm run release:prepare -- 0.2.0` drafts a release; a researcher sets `status: approved` and `approved_by`.
