# Fresh-clone reproduction run, 2026-10-27

A recorded attempt to reproduce the derived outputs of the review from a clean checkout. It tests levels 1 and 2 of `REPRODUCE.md` only.

## Set-up

| Item | Value |
|---|---|
| What was cloned | `git clone` of the review branch at commit `4da7303` ("Transparency package: study audit trail, AI-use ledger, weakness register ...") |
| Where | A new empty directory, with a new Python virtual environment |
| Python | 3.11.17 (Linux container) |
| Who ran it | The AI that wrote the code, so this is **not** an independent reproduction |
| Source PDFs | Not present (they are not in the repository) |

## Stage 1: verifier, standard library only (no optional packages installed)

```
NOTE: openpyxl is not installed, so the .xlsx sheet sync check was skipped (pip install openpyxl)
204 checks passed, 0 failed          (29 s)
```

## Stage 2: install the optional packages, verify again

Installed `openpyxl 3.1.5`, `python-docx 1.2.0` (with `lxml 6.1.3`, `typing_extensions 4.16.0`) and `matplotlib 3.11.2` (with `numpy 2.4.6`, `pillow 13.0.0`).

```
206 checks passed, 0 failed          (29 s)
```

## Stage 3: `bash code/analysis/regenerate_all.sh`

Ran every generator in dependency order, then 25 unit-test files, then the verifier: all tests reported OK (one file skipped 3 tests that need the source PDFs, which are not present), and the verifier reported `206 checks passed, 0 failed`. Wall time 1 minute 29 seconds.

After regeneration, `git status` showed seven modified tracked files and no others:

```
06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx               (binary; 137,774 -> 166,079 bytes)
06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.html      (embeds the SVG figures)
06_outputs/figures/fig1_design_mix.svg
06_outputs/figures/fig2_publication_years.svg
06_outputs/figures/fig3_countries.svg
06_outputs/figures/fig4_direction_by_family.svg
06_outputs/figures/fig5_appraisal_tools.svg
```

For `fig1`, the visible text elements (27) are identical before and after; only path coordinates and clip-path ids change. The Word file differs in size because it embeds the figures. Everything else, including all 477 files in `DATA_MANIFEST.csv`'s scope, the atlas, START_HERE's figures and every register, was byte-identical.

## Not tested

- Windows or macOS, other Python versions (only 3.11 was run), and Windows line endings.
- Any run by someone other than the author of the code.
- Levels 3 to 5 of `REPRODUCE.md`.

The run predates the weakness-register panel in the atlas (added to the working tree afterwards), so the atlas bytes compared here are those of commit `4da7303`.
