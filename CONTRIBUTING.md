# Extending This Dataset

Written for whoever picks this up next, including the author in three years.

The dataset is built to be extended in four directions: more courts, more
jurisdictions, better coding, and outcome data. Each has a different cost and a
different risk of quietly breaking the findings. Read §1 before touching
anything.

---

## 1. The one rule

**Changing a coding pattern changes the findings.** The regex tables in
`utils/jurimetric_coding.py` are research instruments, not implementation
details. A one-word change to a pattern can move thousands of decisions between
categories and silently alter every number in the thesis.

So, always:

```bash
python -m pytest tests/ -q                     # before you change anything
# ... make your change ...
python -m pytest tests/ -q                     # see exactly what moved
python utils/audit_trail.py --csv data/water_law_global_coded.csv
#   then diff audit_rule_coverage.csv against the previous run
```

A failing test is not automatically a bug. It means behaviour changed, and the
change needs a sentence in the commit message saying why the new behaviour is
correct. Silent expected-value updates are how a dataset loses its integrity.

If your change moves more than a few hundred decisions, it is a new dataset
version: bump `CITATION.cff` and `pyproject.toml`, and deposit a new DOI
version so the code and the deposited CSV stay in step.

---

## 2. Adding a Brazilian court

Nineteen of twenty-seven *Tribunais de Justiça* are unscraped. The status table
in `README.md` records why each one failed, which is the first thing to check:
several were blocked by transient problems (timeouts, TLS errors, HTTP 403) that
may since have resolved.

Each tribunal runs one of a handful of platforms, and a scraper for one is
usually adaptable to another on the same platform:

| Platform | Working example | Notes |
|---|---|---|
| ESAJ (POST) | `scrapers/brazil/tjac_scraper.py` | Most common. TJSP, TJSC, TJRR, TJAC |
| ESAJ (AJAX) | `scrapers/brazil/tjsc_scraper.py` | Same backend, JSON responses |
| Elasticsearch REST | `scrapers/brazil/tjdft_scraper.py` | Cleanest to work with |
| ASP.NET WebForms | `scrapers/brazil/tjrj_scraper.py` | Requires viewstate handling |
| Rails / PHP+Solr | `tjpi_scraper.py`, `tjto_scraper.py` | Simple GET |

The genuinely blocked ones need a different approach, not a better scraper:
CAPTCHA (TJMG, TJSE, TJES), SSO (TJAM), or a JavaScript SPA with no public API
(TJGO, TJRO, TJMT). For those, the *Diário da Justiça Eletrônico* or a formal
request to the tribunal under the Lei de Acesso à Informação (Lei 12.527/2011)
is a more realistic route than scraping.

A new scraper must:

1. Use only the standard library. Scrapers deliberately have no dependencies.
2. Read `OUTPUT_DIR` from the environment and write
   `$OUTPUT_DIR/<court>_cases_2016_2026.json`.
3. Emit the field names `utils/merge_national.py` expects. Check
   `normalize_brazil()` there; anything else is silently dropped.
4. Rate-limit. These are public services funded by the courts. 5 requests per
   second is the convention used throughout this repository.
5. Identify itself in the `User-Agent` with a contact address.
6. Leave TLS verification on. If a portal has a broken chain, run once with
   `INSECURE_TLS=1` rather than editing the default.
7. Use the same three search queries as the existing scrapers (`README.md`,
   "Search Queries Used"). **A different query makes the new court
   incomparable to the other eight.** If you change the query, you must
   re-scrape everything.

Then add the court to the status table in `README.md` and update the totals
there, in `CITATION.cff`, `datapackage.json` and `CODEBOOK.md`.

---

## 3. Adding a jurisdiction

Bigger than it looks. A fourth country needs:

1. **A scraper**, as above.
2. **A normaliser** in `utils/merge_national.py`, mapping the source's fields
   onto the thirteen canonical columns.
3. **A resolver branch** in `utils/resolve_case.py`, so decisions stay reachable.
   Check first whether the jurisdiction uses ECLI: most of the EU does, and the
   existing ECLI branch will then work unchanged.
4. **Coding patterns in the new language.** This is the real work. The engine
   currently covers Portuguese, English, Dutch and French. Every one of the 19
   category tables needs vocabulary in the new language, plus the water-core gate.
5. **A validation pass.** A new language means a new false-positive profile.
   Draw a stratified sample, hand-code it, and report precision per stratum
   following `validation/second_coder_protocol.md`.

**Before writing any regex, read `CODEBOOK.md` §4.1.** The water-core gate uses
`\b` word boundaries, which breaks on compounding languages. Dutch is already
affected. German, Danish, Swedish, Norwegian, Finnish and Hungarian all compound
and would be affected the same way. Use substring matching, or explicit
compound alternatives, for any such language.

---

## 4. Fixing the Dutch compound defect

The highest-value single fix available, and deliberately left undone so it is
made as a research decision rather than a code change. See `CODEBOOK.md` §4.1.

The work:

1. Rewrite `_WATER_CORE_RE` so Dutch terms match as substrings rather than
   `\b`-bounded words, keeping the boundaries for Portuguese and English
   (`\bkade\b` and `\beau\b` are short enough to false-positive badly without
   them).
2. `tests/test_water_gate.py` marks the known-bad cases `xfail(strict=True)`.
   When your fix works they become **xpass**, which fails the suite. That is the
   signal: remove the xfail markers in the same commit.
3. Re-run the full pipeline and diff `audit_rule_coverage.csv`. Expect a large
   movement out of `not_water_related` for the Netherlands.
4. **Re-validate.** The existing precision and kappa figures were computed on the
   old gate and do not carry over. Draw a fresh stratified sample.
5. Deposit as v0.4.0 with a changelog entry saying plainly that Netherlands
   classifications changed and why. Do not overwrite v0.3.0: published work
   cites it.

---

## 5. Adding outcome coding

`win_loss` is Brazil-only. `FUTURE_WORK.md` has the full roadmap. The
prerequisite now exists: `scrapers/netherlands/rechtspraak_fulltext.py` retrieves
the decision bodies, which is what outcome coding needs and the
`inhoudsindicatie` cannot supply.

Sequence: retrieve the corpus, hand-code a stratified sample for ground truth,
then validate any automated classifier against that sample before trusting it.
Report the share of decisions Rechtspraak publishes without a body; that ratio
is a ceiling on coverage and belongs in any outcome result.

---

## 6. Repository conventions

- Scrapers: standard library only, `OUTPUT_DIR` from the environment.
- Analysis utilities may use pandas and openpyxl (`requirements.txt`).
- No hardcoded local paths. Read from the environment with a sensible default.
- No credentials in code. `.env.example` documents every variable.
- Generated data stays out of git (`.gitignore`); the deposits hold it.
- Documentation that states a number should say where the number comes from.

## 7. Where things are

| File | What it is |
|---|---|
| `CODEBOOK.md` | Every variable, category and known defect. Authoritative |
| `DATA_ACCESS.md` | Where the data is and how to reach decision text |
| `VERIFICATION.md` | Three-level recipe for checking the dataset |
| `datapackage.json` | Machine-readable schema (Frictionless) |
| `validation/` | Inter-coder reliability, residual audit, decision rules |
| `tests/` | Regression suite pinning classifier behaviour |
| `FUTURE_WORK.md` | Roadmap for outcome coding |

---

## 8. If you are taking this over

Start here, in order:

1. `CODEBOOK.md` §4, the known defects. Everything else assumes you know them.
2. `VERIFICATION.md` Level 1, twenty decisions, ten minutes. It will show you
   what the data actually looks like faster than any prose.
3. `python -m pytest tests/ -q`. If it passes, the engine behaves as documented.
4. `validation/README.md` for what has and has not been validated.

The dataset's weakest points, in order, are: the Dutch compound gate (§4 above),
the absence of category-level validation for the 21 governance categories, and
Brazilian coverage at eight of twenty-seven courts. Anyone looking for a
contribution should start with one of those three.
