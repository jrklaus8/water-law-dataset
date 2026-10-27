# Contributing

Contributions are welcome — whether you're a developer, legal researcher, or simply someone who spotted an issue.

---

## Ways to Contribute

### Add a New Brazilian Court Scraper
Many state courts are still blocked or untested (see the [access status table](https://github.com/jrklaus8/water-law-dataset#brazilian-courts--access-status)). If you can build a scraper for TJMG, TJBA, TJRS, or other courts, that would significantly expand the dataset.

**Template:** Copy any existing scraper in `scrapers/brazil/` — they all follow the same output schema.

### Improve the Jurimetric Coding Engine
The regex patterns in `utils/jurimetric_coding.py` can always be improved:
- Add missing Portuguese/Dutch/English/French patterns
- Reduce false positives in any variable
- Add new variables relevant to water governance research

### Fix a Bug / Improve a Scraper
Open an issue or submit a PR. All scrapers use only the Python standard library (no `pip install` needed for scraping).

### Audit or Challenge the Systematic Review
The review is built to be checked. Start with `AI_USE_STATEMENT.md` and `AUDITING_GUIDE.md` in the `legal-last-mile-systematic-review/` folder ([[Systematic Review]]). You can re-run the 189 repository checks with `python3 code/analysis/verify_repository.py`, trace one study from search record to synthesis, or verify the 31 synthesis studies against their source papers using the verification dossier. Corrections to the AI's extraction are especially valuable because no second extractor has checked it.

### Report Data Quality Issues
If you find systematic errors in the data — wrong dates, duplicate cases, encoding problems — open a [GitHub issue](https://github.com/jrklaus8/water-law-dataset/issues).

---

## Coding Standards

- Python 3.8+, standard library only (for scrapers); `pandas` and `openpyxl` for merging and coding
- Output schema: see [[Dataset Overview]]
- All court JSON files follow the naming convention: `{court_code}_cases_2016_2026.json`

---

## Related: worldwidelaw/legal-sources

This project has contributed to the [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources) community repository:
- Issues #74–77: CanLII API quirks, Rechtspraak sub-classification, ESAJ scraping constraints
- PR #78: Brazil/TJDFT Elasticsearch scraper
- PR #79: Canada/CanLII extended database script

If you're building legal data infrastructure for any country, consider contributing there too.
