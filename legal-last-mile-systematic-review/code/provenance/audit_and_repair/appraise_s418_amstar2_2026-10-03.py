"""2026-10-03: S418 (Brown et al. 2023, Lancet Global Health 11:e606-e614; record R79E038D49B1A) AMSTAR 2-appraised from the full-text PDF the researcher put in the
shared Drive folder (PIIS2214109X23000062.pdf; 9 pp; PDF not committed; appendix pp 1-3 with the search terms is NOT in the PDF and was not read).

Finding: a 17-author expert 'Review' whose only method statement is a Lancet-format box: PubMed, Web of Science and Scopus searched (terms in the appendix, no date or language
limits) plus key reports and UN documents, and 'informed by our collective experiences'. No selection procedure, counts, screening, extraction, appraisal or synthesis method is stated.
It is therefore a NARRATIVE review with a stated database search -- the same hybrid class as S329 -- not a systematic review in the AMSTAR 2 sense. Kept under AMSTAR 2 for
consistency with S329 and with the 2026-09-28 rule ('never claims a systematic search' -> NONE), but flagged: reclassifying S418 to NONE alongside the 13 narrative reviews is a researcher decision.
Rating: Critically Low (critical items 2, 7, 9 and 13 flawed; item 4 only partly met). Not changed: include decision, flags, effect_sizes, study_design_class.
The extraction was already full-text-based (not abstract-only), so the abstract-only count (62) is unchanged. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
DATE = '2026-10-03'
SID = 'S418'
ANS = {1: ('No', 'broad aims; no PICO'), 2: ('No', 'no protocol or registration'), 3: ('No', 'no selection of designs explained; case studies, reports and primary studies mixed'),
       4: ('Partial Yes', 'PubMed, Web of Science, Scopus; no date or language limits; key reports and UN documents added; terms are in an appendix not read; no reference checking or expert-contact statement'),
       5: ('No', 'no screening process described'), 6: ('No', 'no data extraction process described'), 7: ('No', 'no list of excluded studies, no counts'),
       8: ('Partial Yes', 'five illustrative panels (underbounded communities, Roma, homelessness, Indigenous Australia, migrants) describe populations and settings'),
       9: ('No', 'no risk-of-bias or quality appraisal'), 10: ('No', 'not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'), 13: ('No', 'no appraisal to account for'),
       14: ('No', 'not applicable to a narrative argument; heterogeneity not examined'), 15: ('N/A', 'no quantitative synthesis'),
       16: ('Yes', 'authors\' funding and interests declared individually; no financial support for the manuscript')}
ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
RATING = ('Critically Low (appraised 2026-10-03 against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/S418_AMSTAR2.md; critical items 2 (no protocol), 7 (no list of excluded studies), 9 (no appraisal) and 13 are flawed and item 4 only partly met). '
          'Supersedes the abstract-level "Not ratable" entry. Eligibility is a hybrid judgment: a narrative expert review with a stated three-database search (like S329), kept under AMSTAR 2 pending the researcher\'s decision on narrative reviews.')
raw = open(ED, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(ED, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
assert len(rows) == 1159
r = [x for x in rows if x['study_id'] == SID][0]
assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'] == 'AMSTAR 2'
r['risk_of_bias_rating'] = RATING
r['study_design'] = 'narrative expert review (17 authors) with a stated PubMed/Web of Science/Scopus search (terms in an appendix); no selection process, counts, appraisal or synthesis method stated; secondary evidence'
r['model_type'] = 'narrative review with a stated database search (hybrid; not systematic)'
r['publication_type'] = 'journal article (narrative review, Lancet Global Health)'
r['sample_size'] = 'not stated (no counts of records or included studies)'
na = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/S418_AMSTAR2.md (full text, ' + DATE + ')'
for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
    r[k] = na
r['extraction_note'] = ('AMSTAR 2-appraised 2026-10-03 from the full-text PDF supplied by the researcher via the shared Drive folder (9 pp; PDF not committed; appendix with the search terms not read). '
                        'Hybrid: narrative expert review with a stated database search. record_id ' + r['record_id'] + '.')
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ED), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, ED)
L = [f"# AMSTAR 2 appraisal (full text) — {SID}", "",
     f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF supplied by the researcher (not committed). The online appendix (pp 1–3, search terms) is not in the PDF and was not read. Supersedes the abstract-level entry. Appraised by the AI; not independently verified.", "",
     "**Overall confidence: Critically Low** — critical items 2, 7, 9 and 13 are flawed and item 4 is only partly met. **Eligibility caveat:** this is a narrative expert review with a stated three-database search (the Lancet's \"Search strategy and selection criteria\" box), not a systematic review; it is kept under AMSTAR 2 like S329, but moving it to NONE with the 13 narrative reviews is open for the researcher.", "",
     "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
for i, name in ITEMS.items():
    a, b = ANS[i]
    L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a} | {b} |")
L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention)."]
open(f'04_quality/appraisal_forms/{SID}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print('S418 appraised: Critically Low (hybrid narrative review); abstract-only count unchanged')
