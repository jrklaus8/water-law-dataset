# Data Access and Auditability

This document tells an external reviewer exactly what they can obtain, from
where, under what licence, and what is deliberately absent. Read it before
citing, replicating or auditing the dataset.

**Short version:** the 83,596 decisions are not in this repository. They are in
the archival deposits listed below. What is in this repository is the code that
produced them, the validation material, and the tooling to audit the coding.

For what each variable *means*, see [`CODEBOOK.md`](./CODEBOOK.md), which is
authoritative. For how to check any of it, see
[`VERIFICATION.md`](./VERIFICATION.md). To extend the dataset, see
[`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## 1. Where the data is

| What | Where | Format | Notes |
|---|---|---|---|
| Merged dataset, all 83,596 decisions | [Zenodo 10.5281/zenodo.19836413](https://doi.org/10.5281/zenodo.19836413) | CSV + XLSX | Primary citable deposit |
| Same, mirrored | [Harvard Dataverse doi:10.7910/DVN/C9PEFS](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/C9PEFS) | CSV + XLSX | |
| Same, mirrored | [DANS SSH doi:10.17026/SS/RVDBUF](https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/SS/RVDBUF) | CSV + XLSX | Netherlands-facing archive |
| Same, mirrored | [OSF osf.io/admrq](https://osf.io/admrq) | CSV + XLSX | |
| Scrapers, coding engine, validation | this repository | Python + CSV | `data/` is intentionally empty |
| Inter-coder reliability material | `validation/` in this repository | CSV + MD | 207-case sample, both coders' labels |

The `data/` directory in this repository is a working output folder and is
gitignored. Nothing is missing from it: the decisions are in the deposits.

---

## 2. What a record contains

Thirteen columns, produced by `utils/merge_national.py`:

```
country, tribunal, court_name, case_id, title, date, year,
case_type, chamber, judge, legal_area, summary, url
```

After `utils/jurimetric_coding.py`, each record additionally carries the coded
variables (`hr_language`, `sust_language`, `governance_cat`, `win_loss`,
`mp_involvement`, `indigenous_water`, `public_interest`) and the audit columns
`gov_matched_rule` and `gov_matched_span` described in section 5.

### What `summary` is, and is not

`summary` holds the court's own headnote: the *ementa* for Brazil, the
*inhoudsindicatie* for the Netherlands, the case digest for Canada. It is not
the decision. It is an editorial artefact written by the court or its registry,
and its length and quality vary considerably, particularly in the Netherlands
where an `inhoudsindicatie` is sometimes a single sentence.

**The full text of the decisions is not in the dataset and never was.** Section
3 explains why, and section 4 explains how to get it.

This matters more than it first appears, because the classifier never saw full
text either. `utils/jurimetric_coding.py` builds its searchable field from
metadata plus the headnote. A reviewer auditing a classification therefore does
not need the judgment: they need the same string the regex saw, which is in the
deposited CSV, plus the rule that fired, which section 5 provides.

---

## 3. Why the full text is not redistributed

The three jurisdictions sit under three different regimes, and the dataset
follows each one rather than adopting a single posture.

| Jurisdiction | Share | Redistribution posture | Basis |
|---|---:|---|---|
| Netherlands | 68,654 (82%) | Redistributable, and retrievable in bulk | Rechtspraak.nl publishes its case law as Open Data for reuse |
| Canada | 3,218 (4%) | Link only | CanLII licenses content from publishers; its API and site terms restrict bulk redistribution of decision text |
| Brazil | 11,724 (14%) | Headnote only, link for the rest | Lei 9.610/1998 art. 8, III excludes judicial decisions from copyright, so copyright is not the barrier. LGPD and *segredo de justiça* are: tribunals publish *ementas* in anonymised form but do not uniformly do so for full texts |

The asymmetry is legal, not methodological. Before depositing any Netherlands
full-text corpus, confirm the current terms at
<https://www.rechtspraak.nl/Uitspraken/paginas/open-data.aspx>.

---

## 4. Reaching the text of any decision

### 4.1 Stable permalinks

The `url` column was captured at scrape time and points at live court portals,
several of which rewrite or expire URLs. `utils/resolve_case.py` maps a
decision's *identifier* to the most durable address available:

```bash
# one decision
python utils/resolve_case.py ECLI:NL:RVS:2019:2481
python utils/resolve_case.py 0001234-56.2022.8.26.0100 --tribunal TJSP --country Brazil

# a whole dataset — adds permalink, permalink_kind, identifier, fulltext_url
python utils/resolve_case.py --csv data/water_law_global.csv
```

Durability differs by jurisdiction, and the `permalink_kind` column says which
you are looking at:

| `permalink_kind` | Meaning | Durability |
|---|---|---|
| `ecli_deeplink` | Official Rechtspraak ECLI resolver | Permanent |
| `canlii_citation` | CanLII decision URL | Stable, maintained by CanLII |
| `canlii_search` | CanLII search, decision URL not held | Findable |
| `court_search` | Tribunal jurisprudence search, number pre-filled | Best effort |
| `court_record_id` | TJSP ESAJ *acórdão* key | Best effort |
| `court_form` | Tribunal search form, paste the number | Best effort |
| `scraped_url` | Original scraped URL, no resolver available | May rot |

For Brazil, the durable identifier is the normalised CNJ process number
(`NNNNNNN-DD.AAAA.J.TR.OOOO`, Res. CNJ 65/2008), not the URL. It can be entered
into any Brazilian court portal. A subset of TJSP records, chiefly in the
historical 1997–2015 slice, predate that numbering and carry only an ESAJ
internal key; those resolve as `court_record_id` and are the least durable
records in the dataset.

> The ECLI and Rechtspraak content endpoints are the ones used by
> `scrapers/netherlands/rechtspraak_scraper.py`, so they are confirmed working.
> The Brazilian portal URL templates are best-effort reconstructions and should
> be spot-checked against a live portal before being relied on in print.

### 4.2 Netherlands full text, in bulk

`scrapers/netherlands/rechtspraak_fulltext.py` retrieves the `<uitspraak>` body
for every ECLI. The existing scraper already fetches this XML and discards the
body; this script keeps it.

```bash
export OUTPUT_DIR=./data
python scrapers/netherlands/rechtspraak_fulltext.py --from-csv data/water_law_global.csv --resume
```

Output is one JSON file per decision under `$OUTPUT_DIR/nl_fulltext/`, plus a
manifest recording which decisions have a body and which do not. Roughly two
hours for the full corpus at the default 5 requests per second.

Not every published decision has a body: Rechtspraak publishes many as metadata
plus summary only. Those appear as `no_body` in the manifest, and that ratio is
a real ceiling on Netherlands outcome coding which should be reported alongside
any outcome results.

### 4.3 Canada and Brazil

Follow the permalink. Neither corpus is redistributed, for the reasons in
section 3.

---

## 5. Auditing the coding

Classification is not a black box in this dataset. `utils/jurimetric_coding.py`
records, for every decision, which rule assigned its `governance_cat` and the
substring that rule matched:

- `gov_matched_rule` — e.g. `GOV_CATS:tariff_dispute#18`, `RESCUE:connection`,
  `FILTER:no_water_vocabulary`
- `gov_matched_span` — the text the rule fired on

`explain_governance()` is the single source of truth; `code_governance()`
delegates to it, so the audit trail cannot drift from the labels.

To produce a readable audit bundle:

```bash
export DATA_DIR=./data          # folder holding water_law_global.csv
python utils/jurimetric_coding.py
python utils/audit_trail.py --csv data/water_law_global_coded.csv
```

This writes `AUDIT_TRAIL.md` (evidence sample per category, rule concentration,
diagnostics), `audit_sample.csv` (the same sample as data, with permalinks) and
`audit_rule_coverage.csv` (every rule and how many decisions it decides).

Start with rule concentration. Where one pattern decides a large share of a
category, that pattern is doing the analytical work and should be checked first.

---

## 6. Known limits on auditability

Stated plainly, because a reviewer will find them anyway.

1. **Coding runs on headnotes, not judgments.** Classification quality is capped
   by the quality of the court's own summary. Dutch `inhoudsindicatie` fields are
   frequently a single sentence.

2. **The Dutch water gate cannot see compound nouns.** `_WATER_CORE_RE` gates the
   entire classifier and is written with `\b` word boundaries, which is correct
   for Portuguese and English and wrong for Dutch, which compounds nouns without
   spaces. `\bwater\b` does not match `waterwet` or `watervergunning`;
   `\bgrondwater\b` does not match `grondwateronttrekking`. In
   `validation/second_coder_sample_raw.csv`, 65 of the 100 decisions in the
   `NL_broad_water` stratum carry such a compound, and the human coder labelled 61
   of them WATER. This is the mechanism behind the 0.3579 precision recorded for
   that stratum in `validation/precision_recall_results.json`. `audit_trail.py`
   quantifies the effect across the whole dataset without changing any label.

3. **The 99.79% figure is stratum-weighted.** The population-weighted filter
   precision reported for `not_water_related` is arithmetically sound, but the
   mass sits in the `NL_plain` stratum, where precision is 1.0. Where water
   vocabulary is present, precision is 0.3579. Cite both numbers or neither.

4. **Inter-coder agreement depends on which decision rule you apply, and the
   figure most often quoted is not reproducible.** The raw three-label baseline
   is κ = 0.5684 (n=91), moderate agreement. Resolving the *mananciais* protocol
   ambiguity lifts it to between 0.7975 and 0.8506 depending on how broadly the
   rule is scoped; `validation/README.md` reports 0.832, which sits inside that
   range but was never produced by any committed script. The binary
   WATER/NOT_WATER figure, κ = 0.9321 (n=59), is exact.
   `python validation/apply_decision_rules.py` reproduces all of them and prints
   the sensitivity. Cite a variant by name, or cite the baseline; do not cite
   0.832 without saying which rule produced it. See `CODEBOOK.md` §5.

5. **Netherlands decisions carry no outcome coding.** Dispute type is coded;
   who won is not. See `FUTURE_WORK.md` and section 4.2.

6. **Blocked courts are missing, not empty.** Nineteen Brazilian tribunals could
   not be scraped (see the status table in `README.md`). The Brazilian sub-dataset
   is a convenience sample of accessible courts, not a national census, and the
   accessible courts skew toward those with modern search infrastructure.

7. **Some TJSP records are weakly identified.** A subset carries an ESAJ internal
   key and no CNJ number or URL, making independent verification harder than for
   the rest of the corpus.

---

## 7. Citation

> Klaus, C. (2026). *Global Water Law Judicial Decisions Dataset* (v0.3.0).
> Zenodo. https://doi.org/10.5281/zenodo.19836413

Cite the deposit, not this repository, for the data. Cite the repository for the
scrapers and coding engine. See `CITATION.cff`.
