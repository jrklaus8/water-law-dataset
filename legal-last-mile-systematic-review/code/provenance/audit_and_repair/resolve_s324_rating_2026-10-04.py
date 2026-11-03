"""2026-10-04: S324 (Pu et al. 2022, PLOS ONE 17(7):e0270847) AMSTAR 2 rating made final. The 2026-10-02 rating was 'Critically Low (provisional)' because the PRISMA flow diagram (Figure 1) and the
S1-S11 Tables had not been read. Figure 1 was read on 2026-10-04 (page 4 of the researcher's PDF, rendered as an image). It gives COUNTS of full-text exclusions by reason (68 did not evaluate maintenance
outcomes, 16 not LMIC, 14 not peer-reviewed, 8 not in schools; 106 excluded of 125 assessed) but no list of the excluded studies, so item 7 stays No. The S1-S11 Tables are online supplements that are NOT
in the PDF; the PDF's supporting-information list shows them to be quality-assessment tables and indicator/outcome tables (S1-S6 quality appraisals, S7-S11 indicators/outcomes), a protocol and a PRISMA
checklist -- no excluded-studies list. The main text never uses the appraisal results when interpreting findings (its only stated limitation is English-only, peer-reviewed literature), so item 13 stays No on
the main text. Result: critical items 7 and 13 flawed -> Critically Low, no longer provisional. Not changed: include decision, flags, effect_sizes. Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
FORM = '04_quality/appraisal_forms/S324_AMSTAR2.md'
raw = open(ED, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(ED, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
for r in rows:
    if r['study_id'] != 'S324':
        continue
    assert r['risk_of_bias_rating'].startswith('Critically Low (provisional)')
    r['risk_of_bias_rating'] = ("Critically Low (appraised 2026-10-02 against the official AMSTAR 2 checklist on the full text; made final 2026-10-04 after Figure 1 was read; item-level answers in 04_quality/appraisal_forms/S324_AMSTAR2.md; "
                                "critical items 7 (no list of excluded studies: Figure 1 gives counts of exclusion reasons only) and 13 (appraisal results not used when interpreting findings) are flawed). "
                                "Supersedes the abstract-only 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text (see the form).")
    r['extraction_note'] = r['extraction_note'].replace('Figure 1 (PRISMA flow) and supplementary S1-S11 Tables not read.',
        'Figure 1 (PRISMA flow) read 2026-10-04 (5,774 database records + 1 from authors; 1,934 duplicates; 3,841 screened; 125 full texts; 106 excluded: 68 no maintenance outcome, 16 not LMIC, 14 not peer-reviewed, 8 not schools; 19 included); the S1-S11 Tables are online supplements not in the PDF and were not read.')
    assert 'read 2026-10-04' in r['extraction_note']
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ED), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, ED)
t = open(FORM, encoding='utf-8').read()
t = re.sub(r'\*\*Overall confidence: Critically Low \(provisional\)\*\*.*?\n', "**Overall confidence: Critically Low (final, 2026-10-04)** — critical items 7 (no list of excluded studies) and 13 (appraisal not used in interpretation) are flawed. Critical items: 2, 4, 7, 9, 11, 13, 15 (11 and 15 not applicable: no meta-analysis). "
           "*Update 2026-10-04:* Figure 1 was read: it gives counts of full-text exclusions by reason (68 / 16 / 14 / 8) but no list of studies, so item 7 stays No. The S1–S11 Tables are online supplements not in the PDF; the PDF's supporting-information list shows quality-assessment and indicator tables, a protocol and a PRISMA checklist, none an excluded-studies list. Item 13 is judged on the main text, which never uses the appraisal when interpreting findings.\n", t, count=1, flags=re.S)
t = t.replace("| 7 | **Yes** | List of excluded studies with justification | No | text says reasons for exclusion are in Fig 1 (not read); no list of excluded studies in the text |",
              "| 7 | **Yes** | List of excluded studies with justification | No | Figure 1 (read 2026-10-04) gives counts of exclusions by reason (68 / 16 / 14 / 8), not a list of excluded studies |")
t = t.replace("| 13 | **Yes** | Risk of bias accounted for when interpreting results | No | the text read does not use the appraisal results when interpreting findings; S1-S6 Tables not read |",
              "| 13 | **Yes** | Risk of bias accounted for when interpreting results | No | the main text does not use the appraisal results when interpreting findings; the S1–S6 quality tables are online supplements not in the PDF |")
assert 'final, 2026-10-04' in t and 'counts of exclusions by reason' in t and 'online supplements not in the PDF |' in t
open(FORM, 'w', encoding='utf-8').write(t)
print('S324 rating final: Critically Low')
