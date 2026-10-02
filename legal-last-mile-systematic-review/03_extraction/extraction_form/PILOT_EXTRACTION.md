# Pilot Extraction (Phase 7) — Start Here

`PROTOCOL.md` §6 and `PRISMA_WORKFLOW.md` Phase 7 both require piloting
the extraction form/codebook on **~10 studies** before full extraction
begins. The point of a pilot isn't to extract 10 studies faster than the
rest — it's to catch problems with `CODEBOOK.md`, `EXTRACTION_FORM.md`,
and the `extraction_database.csv` schema itself while the cost of fixing
them is still low (10 re-extractions, not hundreds).

## Why this can't run yet

Pilot studies have to be drawn from the pool that has actually cleared
full-text screening — records with `final_decision == "include"` in
`02_screening/full_text/full_text_screening_database.csv`. As of this
writing that file has **3,659 seeded records and zero decisions** (Phase
6 tooling is built, but no retrieval or full-text screening has happened
yet — see `02_screening/full_text/FULL_TEXT_README.md`). There is
nothing to pilot on until that changes.

`code/extraction/select_pilot_sample.py` (below) is ready to run the
moment there are enough included records — it will tell you plainly if
there aren't, rather than picking a sample too small to be meaningful.

## Selecting the ~10 studies

Run:

```
python3 code/extraction/select_pilot_sample.py \
    --full-text-db 02_screening/full_text/full_text_screening_database.csv \
    --screening-db 02_screening/title_abstract/screening_database.csv \
    --pilot-out 03_extraction/extraction_form/pilot_sample.csv \
    --n 10
```

This draws a **fixed-seed random sample stratified by source database**
(proportional, rounding to keep totals near `--n`) from every record with
`final_decision == "include"` in the full-text database. Stratifying by
database, not
hand-picking, keeps the pilot from being unconsciously skewed toward
whichever database happens to be easiest to retrieve full text for
(e.g. don't let it become 10/10 Scopus articles just because those PDFs
were easiest to get). The seed is fixed and printed in the script's
output so the exact sample is reproducible and auditable later, the same
practice already used for `exclude_spotcheck_sample.csv`
(`DATA_DICTIONARY.md`).

If fewer than `--n` records are currently `include`, the script refuses
to draw a sample rather than silently returning a small one — see the
script's own output for exactly how many are available and what to do
(either extract what's available if the researcher judges it enough, or
wait for more full-text decisions).

## What "piloting" actually means here

For each of the ~10 sampled studies:

1. Extract it fully per `EXTRACTION_FORM.md`, into
   `03_extraction/extracted_data/extraction_database.csv` as normal —
   pilot rows are **not** a separate file; they're real data, just the
   first data, extracted under extra scrutiny.
2. Where feasible, have it extracted independently a second time
   (`PROTOCOL.md` §6's two-reviewer principle, applied to extraction the
   same way it's applied to screening). Compare the two extractions
   field by field.
3. **The goal of a disagreement is not just resolving that one study's
   numbers — it's asking whether the disagreement reveals an ambiguity in
   `CODEBOOK.md` or `EXTRACTION_FORM.md` that will recur across hundreds
   of future studies.** A vague field definition, a code that doesn't
   cleanly cover a mechanism this literature actually contains, or a
   provenance requirement that's unclear in practice are all pilot
   findings worth fixing now.
4. If the pilot surfaces a real codebook/schema change, that's a protocol
   amendment: log it in `CHANGELOG.md` with the rationale
   (`PROTOCOL.md` §12), update `CODEBOOK.md`/`DATA_DICTIONARY.md`/
   `EXTRACTION_FORM.md` together so they never drift apart, and re-check
   whether any already-extracted pilot rows need revisiting under the
   revised definition.
5. Once the pilot studies are extraction-stable (no further codebook
   changes triggered), record that in `PRISMA_WORKFLOW.md` Phase 7 and
   move to full extraction (Phase 8) on the remaining included studies —
   full extraction does not require re-running the pilot studies, they
   already count.

## After the pilot

`pilot_sample.csv` (the working list of which `record_id`s were sampled)
is not itself part of the extraction schema — once used, it's a disposable
audit artifact, kept for reproducibility of the pilot-selection process,
not consulted by any downstream script.
