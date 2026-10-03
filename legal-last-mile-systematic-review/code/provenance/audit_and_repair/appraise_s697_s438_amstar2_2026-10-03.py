"""2026-10-03: S697 (Narayanan, Rajan, Jebaraj & Elayaraja 2017, Utilities Policy 44:50-62; record from the screening database) and S438 (Majuru, Suhrcke & Hunter 2016,
Int J Environ Res Public Health 13:1222) appraised with AMSTAR 2 from the full-text PDFs the researcher put in the shared Drive folder (main.pdf; ijerph-13-01222 2.pdf; PDFs not
committed; text extractor used -- Figure 1 flow diagrams, forest-plot images and the appendix inclusion-criteria table were NOT read).
Eligibility: both state a search, selection, appraisal and synthesis -> real (S697: a meta-analysis) systematic reviews; both keep AMSTAR 2.
Ratings: both Critically Low under the AMSTAR 2 algorithm (critical items 2 and 7 flawed in each), although S697 is the more rigorous of the reviews appraised so far.
Not changed: include decisions, flags, effect_sizes. S697's extraction was already full-text-based, so the abstract-only count (62) is unchanged. Run from legal-last-mile-systematic-review/."""
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
S['S697'] = dict(
    ans={1: ('Yes', 'population (urban poor in LMIC slums), intervention (bottom-up approaches), comparison (top-down), outcomes (four access dimensions) all stated'), 2: ('No', 'no protocol or registration stated'),
         3: ('Partial Yes', 'inclusion and exclusion criteria in Appendix 1 (an image table, not read); designs not discussed in the text'),
         4: ('Yes', 'hand search of journals, ScienceDirect/EBSCO/ProQuest, ~20 agency websites, reference lists, author correspondence; 21,919 + 3,580 records; search dates and string not given in the text'),
         5: ('No', 'multi-stage screening in EPPI-Reviewer; duplicate selection not stated'), 6: ('No', 'duplicate extraction not stated'), 7: ('No', 'record counts only; no list of excluded studies'),
         8: ('Yes', 'Appendix 2 lists the 21 studies; Table 1 classifies the 71 findings by dimension, sector, region, slum type and participation'),
         9: ('Partial Yes', 'critical appraisal tool (Annamalai et al. 2016) scored out of 72, two independent appraisers, high/medium/low bands; confounding handling not described'),
         10: ('No', 'funding of included studies not reported'),
         11: ('Yes', 'random-effects (DerSimonian-Laird) on log odds ratios, SMD converted by a stated formula, separate analyses for different metrics, I2; caveat: 71 findings from 21 studies'),
         12: ('No', 'no analysis of the effect of study quality on pooled results seen'), 13: ('Yes', '20 of 21 studies rated high or medium; evidence base described as good quality in the interpretation'),
         14: ('Yes', 'I2 and subgroup analyses by sector, facility type, region, slum type and community participation'), 15: ('Yes', 'funnel-plot asymmetry, Egger and Begg tests; no bias indicated (Appendix 4)'),
         16: ('Yes', 'DFID funding (Contract 40077696) disclosed; no conflicts statement seen in the text read')},
    rating='Critically Low', basis='critical items 2 (no protocol) and 7 (no list of excluded studies) are flawed; the rest of the critical items are met or partly met',
    upd=dict(
        publication_type='journal article (systematic review and meta-analysis, Utilities Policy)', country='multi-country (low- and middle-income countries; urban slums: Asia, Africa, South America, Central/North America)',
        population='urban slum and low-income populations in LMICs; electricity, water and sanitation services',
        sample_size='21 studies yielding 71 findings (49 connectivity, 14 affordability, 4 adequacy, 4 effort and time; 45 water, 21 sanitation, 5 electricity; 36 Asia, 27 South America, 4 Africa, 4 Central/North America); 25,499 records screened (21,919 hand/database + 3,580 websites, references, author contact)',
        effect_measure='random-effects (DerSimonian-Laird) pooled odds ratios (all findings converted to log odds ratio); subgroup analyses; Egger and Begg tests',
        effect_estimate=("Pooled effect of bottom-up (NGO/CBO) versus top-down approaches on connectivity: OR 1.05, not statistically significant; no significant effect on any access dimension (connectivity, affordability, adequacy, effort and time). "
                         "Subgroups: significant improvement only for individual toilets (not significant in Africa); more effective in water and sanitation than electricity; most effective in formal (notified) slums; significantly positive where bottom-up approaches involve active community participation. "
                         "Publication-bias tests did not indicate bias; 20 of 21 studies rated high or medium quality."),
        study_design='systematic review and meta-analysis (secondary; 21 primary studies, 71 findings)', model_type='random-effects meta-analysis on log odds ratios with subgroup analyses',
        section='Methods; Results and discussion; Appendices (full text)', exact_location='Abstract; Methods 2.2 (study identification, screening, quality appraisal) p3-4; 2.3 data description and Table 1 p4; 2.4 meta-analysis incl. bias tests p4-5; Results 3.1 p5-6; Appendices 1-4'),
    note='AMSTAR 2-appraised 2026-10-03 from the full-text PDF supplied by the researcher via the shared Drive folder (main.pdf, 13 pp; PDF not committed). Figures (forest plots), the Appendix 1 criteria table and Appendix 3-4 tables not read. The earlier "exact k not extracted" gap is closed (k = 21 studies, 71 findings).')
S['S438'] = dict(
    ans={1: ('Partial Yes', 'review questions and four inclusion criteria stated; no formal PICO'), 2: ('No', 'no protocol or registration stated'), 3: ('No', 'designs not discussed; all included studies cross-sectional'),
         4: ('Yes', 'seven databases (CINAHL, Embase, PubMed Central, Scopus, ScienceDirect, Scirus, Web of Knowledge) with the full string, Google and Google Scholar (first 50 hits), reference lists; English only (acknowledged)'),
         5: ('No', 'duplicate selection not stated; the search was performed by one author'), 6: ('No', 'duplicate extraction not stated'),
         7: ('No', '1,643 records, 357 duplicates, 4 added from references, 28 included; no list of excluded studies (Figure 1 not read)'), 8: ('Yes', 'Table 2 describes each study (objectives, setting, supply, methods, findings)'),
         9: ('Partial Yes', 'framework adapted from Hellebrandt et al. (Cochrane/EPPI domains), six scored criteria combined into low/moderate/high risk of bias; number of appraisers not stated; confounding not a named domain'),
         10: ('No', 'not reported'), 11: ('N/A', 'no meta-analysis'), 12: ('N/A', 'no meta-analysis'),
         13: ('Yes', '12 studies low, 13 moderate and 3 high risk of bias; common bias sources (unclear methods, convenience or snowball sampling) discussed in the results'),
         14: ('Yes', 'diversity of methods, disciplines and outcomes explained; thematic synthesis because pooling was not appropriate'), 15: ('N/A', 'no quantitative synthesis'),
         16: ('Partial Yes', 'no conflict of interest declared; funding for the review not stated in the text read')},
    rating='Critically Low', basis='critical items 2 (no protocol) and 7 (no list of excluded studies) are flawed; items 4 and 13 are met',
    upd=dict(
        publication_type='systematic review (journal article, IJERPH)', country='multi-country (developing countries; 9 South Asia, 8 Africa, 7 Americas and Caribbean studies)',
        population='households in developing countries coping with unreliable domestic water supply (22 urban, 3 rural, 2 mixed, 1 unspecified)',
        sample_size='28 included studies (1,643 database records, 357 duplicates removed, 4 added from reference lists); all cross-sectional',
        effect_measure='thematic narrative synthesis of coping strategies, coping costs and their determinants; no pooled estimate',
        effect_estimate=("Common coping strategies are drilling wells, storing water and collecting from alternative sources; choice is influenced by income, education, land tenure and the extent of unreliability. "
                         "Low-income households carry a disproportionate coping burden (time- and labour-intensive collection, smaller and lower-quality supply). Land tenure and the regulatory environment for poor and vulnerable consumers shape the choice, and illegal connections are a documented accommodative strategy. "
                         "Study quality: 12 low, 13 moderate, 3 high risk of bias."),
        study_design='systematic review (structured multi-database search; 28 cross-sectional studies; adapted-Cochrane/EPPI quality appraisal; thematic synthesis)', model_type='systematic review, thematic narrative synthesis (no meta-analysis)',
        section='Methods; Results; Discussion (full text)', exact_location='Abstract; Methods 2.2 literature search and selection criteria p3-4; 2.3 quality appraisal; Results p4-5 (1,643 -> 28), Tables 1-2; Discussion (limitations: English only, dispersed literature)'),
    note='AMSTAR 2-appraised 2026-10-03 from the full-text PDF supplied by the researcher via the shared Drive folder (ijerph-13-01222, 20 pp; PDF not committed). Figure 1 (flow diagram) not read.')

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
for sid, d in S.items():
    L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "",
         f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF supplied by the researcher via the shared Drive folder (not committed). Figures (flow diagrams, forest plots) and image tables/appendices were **not read**. Supersedes the earlier abstract-level entry. Appraised by the AI; not independently verified.", "",
         f"**Overall confidence: {d['rating']}** — {d['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
         "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
    for i, name in ITEMS.items():
        a, b = d['ans'][i]
        L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a} | {b} |")
    L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). The algorithm counts critical flaws only, so a review can be methodologically careful yet rate Critically Low for lacking a protocol and an excluded-study list."]
    open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print('appraised', ', '.join(S))
