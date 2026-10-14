"""2026-10-03: S052 (Muoghalu, Semiyaga & Manga 2023, Front Environ Sci 11:1097716) and S327 (Ezezika et al. 2023, PLOS Glob Public Health 3(4):e0001720) appraised with AMSTAR 2
from the full-text PDFs the researcher supplied in chat (14 pp and 23 pp; PDFs not committed; text extractor used -- Figure 1 flow diagrams, Figures 2-5, and every supplementary
file (S052 Supplementary Tables S1-S2; S327 S1-S5 Files) were NOT read). Both state a search, a selection process and a synthesis -> genuine systematic reviews; both keep AMSTAR 2.
Ratings: S052 Critically Low (critical items 2, 7, 9, 13 flawed); S327 Low (one critical flaw, item 7; BORDERLINE -- it hinges on item 13, which is a judgement call; if item 13 were
scored No the rating would be Critically Low). S327 is the first review appraised so far that is not Critically Low (PROSPERO-registered, duplicate screening and extraction, MMAT appraisal).
Corrections to the earlier abstract-level extraction of S052 (the full text does not support them): (a) "illegal FS dumping outlawed in India, Kenya, Ghana" -- the paper says MANUAL EMPTYING is
deemed illegal in India, Kenya, Ghana and Bangladesh (one cited source, Zaqout et al. 2020); (b) "mechanical emptying up to 4x more costly than manual (Jenkins 2015, Tanzania)" -- the paper says
mechanical is more costly in most studies (Bhaluka: 13 vs 5 USD) and the 4x figure is the REVERSE, formal manual emptying costing 4x mechanical in Kisumu (Peletz 2020); Jenkins 2015 is cited for
accessible plots being 23x more likely to use a higher hygienic service. S327 citation corrected from 3(1) to 3(4) (the PDF header reads 3(4)).
Not changed: include decisions, boolean flags (S052 sanction=TRUE rests on "rules and sanctions should apply to all operators" and the illegality of manual emptying -- still supportable; S327's single
flag water_access=TRUE, no legal/institutional flags -- see the scope question in DECISIONS_AND_OPEN_ITEMS.md), effect_sizes, evidence_map. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
DATE = '2026-10-03'
NA = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/{sid}_AMSTAR2.md (full text, ' + DATE + ')'
ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
S = {}
S['S052'] = dict(
    ans={1: ('Partial Yes', 'three review questions stated; inclusion/exclusion criteria are in Supplementary Table S1 (not read); no comparator'), 2: ('No', 'no protocol or registration stated; PRISMA 2009 guideline followed'),
         3: ('No', 'designs not explained; included studies classed afterwards as 17 observational, 10 practitioner papers, 10 case studies, no experimental'),
         4: ('Partial Yes', 'five databases (Web of Science, Environmental Complete, Scopus, Global Health, PubMed), English, Jan 2002-Dec 2021, search terms in Supplementary Table S2 (not read); no grey literature or reference-list search; language and date limits not justified (a strict reading could score No -- the rating is unaffected)'),
         5: ('No', 'screening described but duplicate selection not stated'), 6: ('No', 'duplicate extraction not stated'),
         7: ('No', '974 records, 843 excluded (333 duplicates), 131 full texts, 94 excluded, 37 included; no list of excluded studies (Figure 1 not read)'),
         8: ('Partial Yes', 'country, setting (26 urban / 10 peri-urban / 1 rural), design and method per study summarised in Figure 3 and text; no table of included studies in the main text'),
         9: ('No', 'no risk-of-bias or quality appraisal of the included studies is described'), 10: ('No', 'funding of included studies not reported'),
         11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'),
         13: ('No', 'no risk of bias assessed, so none accounted for when interpreting results'), 14: ('No', 'results counted by theme; discordant findings noted (e.g. cost) but not explored'),
         15: ('N/A', 'no quantitative synthesis'), 16: ('Partial Yes', 'no conflict of interest declared; no funding statement found in the text read')},
    rating='Critically Low', basis='critical items 2 (no protocol), 7 (no list of excluded studies), 9 (no appraisal of included studies) and 13 (so none accounted for) are flawed',
    upd=dict(
        publication_type='journal article (systematic review, Frontiers in Environmental Science)',
        sample_size='37 studies from 25 countries (974 records from 5 databases; 333 duplicates; 131 full texts assessed; 94 excluded); 26 urban, 10 peri-urban, 1 rural; 23 sub-Saharan Africa, 11 South Asia, 6 South-East Asia (some studies span regions)',
        effect_measure='count of studies by theme (narrative thematic synthesis; no pooled estimate)',
        effect_estimate=("Accessibility discussed in 18 of 37 studies as a factor in choosing an emptying method, cost in 14, service quality in 13, sludge thickness in 8. Challenges grouped as financial, technical and institutional (14 studies each), health (12) and social (8). "
                         "Mechanical emptying reported as more costly than manual in most studies (e.g. Bhaluka, Bangladesh: 13 vs 5 USD), but one study (Peletz 2020, Kisumu) found formal manual emptying about four times more costly than mechanical. "
                         "Institutional challenges (14 studies): no or poorly enforced institutional frameworks, regulators lacking capacity to enforce, inadequate sanitation regulation, informal fees and bribes (Yaounde), uneven taxation of company versus individual emptiers; manual emptying deemed illegal in India, Kenya, Ghana and Bangladesh (one cited source) yet most widely used. "
                         "Improvement initiatives (13 studies) limited by cost/affordability and access to finance."),
        study_design='systematic review (secondary; 37 studies; PRISMA-guided multi-database search; no quality appraisal; thematic counts)', model_type='systematic review, narrative thematic synthesis with counts by theme',
        section='Results and discussion 3.1-3.5 (full text)',
        exact_location=("3.3.1 Accessibility (p4-5: municipal emptying 'lengthy and bureaucratic' in Dhaka; Jenkins 2015 Tanzania: accessible plots 23x more likely to use a higher hygienic service); 3.3.2 Cost (p5: Balasubramanya 13 vs 5 USD; Peletz 2020 Kisumu: formal manual emptying ~4x mechanical); "
                        "3.4.1 Social (p6: manual emptying deemed illegal in India, Kenya, Ghana, Bangladesh); 3.4.5 Institutional (p8-9: no or unenforced frameworks, enforcement capacity, bribes and unofficial fees in Yaounde, licences and permits as one of five framework aspects, Accra WMD monitoring)")),
    note=("Full-text appraisal 2026-10-03 from the PDF supplied by the researcher (14 pp; PDF not committed); Figures 1-5 and Supplementary Tables S1-S2 not read. CORRECTS the earlier abstract-level extraction: the paper says manual emptying (not 'FS dumping') is deemed illegal in India, Kenya, Ghana and Bangladesh, "
          "and the '4x more costly' figure is formal MANUAL emptying costing 4x mechanical in Kisumu (Peletz 2020), not mechanical costing 4x manual. Belongs to the faecal-sludge-management cluster with S015, S019 and S027."))
S['S327'] = dict(
    ans={1: ('Partial Yes', 'research question and Table 1 give population, intervention, outcome, setting; no comparator'), 2: ('Partial Yes', 'protocol registered on PROSPERO (CRD42020221210); the text does not discuss deviations'),
         3: ('No', 'primary research of any design accepted; no explanation of the choice, designs reported afterwards (31 interventional, 15 non-interventional)'),
         4: ('Partial Yes', 'four databases (Ovid Medline, Ovid Embase, Web of Science, Scopus), librarian-designed strategy, search strings in S1 File (not read); searched 11 June 2020, English, 1970-2020; no grey literature or reference-list search; search roughly three years old at publication'),
         5: ('Yes', 'titles/abstracts and full texts screened independently by two reviewers, conflicts resolved by a third (Covidence)'), 6: ('Yes', 'two reviewers piloted then independently extracted; a third checked discrepancies'),
         7: ('No', '11,696 records, 7,177 after de-duplication, 156 full texts, 46 included; reasons for the 110 full-text exclusions are not listed (Figure 1 and S1-S5 Files: no excluded-studies list among the listed supporting files)'),
         8: ('Partial Yes', 'country, type, year and participants summarised in the text; per-study characteristics are in S3 File (not read)'),
         9: ('Partial Yes', 'Mixed Methods Appraisal Tool applied to all 46 (45 passed; one retained despite failing the screening questions); MMAT does not fully cover confounding or selective reporting'),
         10: ('No', 'funding of included studies not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'),
         13: ('Yes', 'BORDERLINE (judgement call): limitations note that non-interventional studies may be less rigorous because of confounding and selection bias and that findings may be too specific; MMAT results (S4 File, not read) are not used to weight the findings. A stricter reading scores No, which would make the rating Critically Low'),
         14: ('Yes', 'variation in methods, measures and settings discussed as limiting generalisability'), 15: ('N/A', 'no quantitative synthesis'),
         16: ('Yes', 'funding (Flourish Collective, University of Toronto Scarborough) and no competing interests declared')},
    rating='Low', basis='one critical flaw: item 7 (no list of excluded studies); item 13 is a borderline Yes -- scored No it would become Critically Low',
    upd=dict(
        publication_type='journal article (systematic review, PLOS Global Public Health)', country='multi-country (26 countries; commonest Bangladesh 7, India 6, Kenya 4; also UK, USA, Australia, South Korea and others)',
        population='community members and school students of any age in community or school settings; handwashing with soap and water (health-care and food-service settings excluded)',
        sample_size='46 studies (2003-2020; 11,696 records retrieved, 7,177 screened after de-duplication, 156 full texts); 31 interventional and 15 non-interventional',
        effect_measure='narrative synthesis of barriers and facilitators coded to the Theoretical Domains Framework plus inductive thematic analysis; no pooled estimate',
        effect_estimate=("21 barriers and 23 facilitators to community handwashing with water and soap, spanning 12 of 14 Theoretical Domains Framework domains; most frequent domains environmental context and resources, goals and knowledge. "
                         "Nine themes: resource availability, cost and affordability, handwash-station design and infrastructure, accessibility, gender roles, champions, health promotion, time management, knowledge/beliefs/behaviours. "
                         "Content is behavioural and programmatic; legal or institutional content is incidental (e.g. school management committees operating 'to government mandate'; unwillingness to follow hygiene mandates in a camp setting)."),
        study_design='systematic review (secondary; 46 studies; registered protocol; duplicate screening and extraction; MMAT appraisal; TDF-coded thematic synthesis)', model_type='systematic review, TDF-coded narrative thematic synthesis (no meta-analysis)',
        section='Methods; Results; Discussion; Limitations (full text)',
        exact_location='Abstract; Registration statement p2; Methods (search, eligibility Table 1, data extraction) p2-4; Quality assessment p5; Results p5-17; Limitations p19'),
    note=("Full-text appraisal 2026-10-03 from the PDF supplied by the researcher (23 pp; PDF not committed); Figures 1-3 and S1-S5 Files not read. The earlier entry was citation/summary-level only (not caught by the abstract-only note-prefix check). "
          "Citation volume/issue corrected from 3(1) to 3(4) (PDF header). SCOPE QUESTION for the researcher: this is a behavioural-determinants review of handwashing with almost no legal or institutional content; it is kept (decision unchanged) but listed in DECISIONS_AND_OPEN_ITEMS.md."))

raw = open(ED, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(ED, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
assert len(rows) == 1159
for r in rows:
    sid = r['study_id']
    if sid not in S:
        continue
    d = S[sid]
    assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'].replace(' ', '').startswith('AMSTAR2'), sid
    for k, v in d['upd'].items():
        assert k in r, k
        r[k] = v
    if sid == 'S327':
        assert '3(1):e0001720' in r['citation']
        r['citation'] = r['citation'].replace('3(1):e0001720', '3(4):e0001720')
    r['risk_of_bias_rating'] = (f"{d['rating']} (appraised {DATE} against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/{sid}_AMSTAR2.md; {d['basis']}). "
                                "Supersedes the earlier 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text.")
    for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
        r[k] = NA.format(sid=sid)
    r['extraction_note'] = d['note'] + ' record_id ' + r['record_id'] + '.'
    r['researcher'] = 'Claude-AI-extraction-2026-10-03 (full-text appraisal)'; r['date_extracted'] = DATE
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ED), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, ED)
cit = {r['study_id']: r['citation'] for r in rows if r['study_id'] in S}
for sid, d in S.items():
    L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "", f"**Citation:** {cit[sid]}", "",
         f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF supplied by the researcher in chat (not committed). Figures (flow diagrams, charts) and all supplementary files were **not read**. Supersedes the earlier abstract-level entry. Appraised by the AI; not independently verified.", "",
         f"**Overall confidence: {d['rating']}** — {d['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
         "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
    for i, name in ITEMS.items():
        a, b = d['ans'][i]
        L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a} | {b} |")
    L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). AMSTAR 2 rating rule: no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low. A 'Partial Yes' is not a flaw."]
    open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print('appraised', ', '.join(S))
