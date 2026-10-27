"""2026-10-04: S328 (Ali, Asmoni, Shaarani & Misnan 2026, Int J Built Environ Sustain 13(2):237-251) appraised with AMSTAR 2 from the full-text PDF found in the researcher's Drive
(record RE8F43EAB1543; text extractor used -- Figures 1-7 were NOT read; no supplementary files exist in the text). It states a search, a selection process and a meta-analysis -> genuine
systematic review with meta-analysis; AMSTAR 2 kept. Rating: Critically Low (critical items 7 and 13 flawed, item 11 judged flawed as well; item 2 borderline). The paper is also internally
inconsistent: the abstract and results give a pooled functionality of 52.3% (95% CI 47.8-56.8, I2 78.2%) from 51 studies, Table 2 attributes the same estimate to 23 studies (and again to
'handpumps' with 23 studies), the conclusion gives CI 48.7-55.9 and I2 87%, the forest plot shows 16 'representative' studies, and a 1-10 'community participation score' used in the
meta-regression is never defined. The pooled numbers are therefore NOT extracted as results. Not changed: include decision, boolean flags, effect_sizes (none), evidence_map.
Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
DATE = '2026-10-04'
NA = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/{sid}_AMSTAR2.md (full text, ' + DATE + ')'
ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
S = {}
S['S328'] = dict(
    ans={1: ('Partial Yes', 'objectives, population (Nigerian water supply projects), outcome (functionality, sustainability) and Table 1 criteria stated; no comparator'),
         2: ('Partial Yes', 'BORDERLINE: text says an a priori protocol was established (questions, search syntax, eligibility, extraction codes, statistical models) but gives no registration, no access and no deviations statement; unverifiable'),
         3: ('No', 'designs of included studies not explained; inclusion spans empirical or conceptual analyses, conference papers, systematic reviews and grey literature'),
         4: ('Partial Yes', 'Google Scholar, PubMed, SciSpace and arXiv plus grey literature, World Bank/UNICEF/WaterAid repositories, citation tracking; search string given in the text; English only, 2015-2025; no regional or engineering databases (Scopus, Web of Science, AJOL); relevance of arXiv questionable'),
         5: ('Yes', 'two reviewers independently screened titles/abstracts and full texts, third reviewer for disagreements'),
         6: ('No', 'standardised extraction form described; duplicate extraction not stated'),
         7: ('No', '464 records, 324 after de-duplication, 140 excluded at title/abstract, 184 full texts, 43 excluded; no list of excluded studies or reasons'),
         8: ('No', 'only aggregated descriptions (frequencies by factor); no table or per-study description of the 141 included studies in the text read'),
         9: ('Partial Yes', 'Newcastle-Ottawa Scale for observational studies and custom criteria for grey literature are named; no results of the appraisal are reported anywhere in the text'),
         10: ('No', 'funding of included studies not reported'),
         11: ('No', 'JUDGEMENT CALL: DerSimonian-Laird random effects on functionality proportions, I2, meta-regression, funnel plots; but study counts for the same estimate differ (51, 23, 16, 41, 35), the headline estimate is repeated for a 23-study subgroup, the conclusion reports a different CI and I2, and the 1-10 participation score and the Cohen d for pre/post proportions are not defined, so the combination cannot be judged appropriate'),
         12: ('No', 'no risk-of-bias results reported, so none examined for effect on the meta-analysis'),
         13: ('No', 'quality assessment results are not reported or used when interpreting findings; limitations list publication bias, heterogeneity and observational designs but not appraised quality'),
         14: ('Yes', 'I2, tau2 and Q reported; heterogeneity discussed and subgroup and meta-regression analyses run'),
         15: ('Yes', 'funnel plot, Egger, Begg and trim-and-fill reported and discussed (although the counts behind them are inconsistent)'),
         16: ('No', 'no funding statement for the review (the acknowledgements thank World Bank, EU, USAID project offices and a Ministry for institutional support); competing interests: none declared')},
    rating='Critically Low', basis='critical items 7 (no list of excluded studies), 13 (quality not accounted for) and 11 (inconsistent meta-analytic reporting; judgement call) are flawed; two flaws suffice without item 11',
    upd=dict(
        publication_type='journal article (systematic literature review and meta-analysis, International Journal of Built Environment and Sustainability)',
        population='water supply projects, mainly rural handpumps and other systems, in Nigeria; 141 included studies (51 said to contribute functionality data)',
        sample_size='464 records (441 databases, 23 other), 324 after de-duplication, 184 full texts, 43 excluded, 141 included in qualitative synthesis and 51 in meta-analysis (stated); 12,847 rural water systems (stated; counts for this figure vary across the paper)',
        effect_measure='thematic inventory of 23 success factors in 5 domains; frequency of mention; random-effects pooling of functionality rates; meta-regression on a 1-10 community participation score (not defined); no pooled effect estimate of a legal or institutional exposure',
        effect_estimate=("Reported (not independently credible -- see note): pooled functionality of rural water systems 52.3% (reported 95% CI 47.8-56.8 in results, 48.7-55.9 in the conclusion; I2 78.2% vs 87%). 23 success factors; community participation mentioned in 98% of studies, clear institutional mandates 92%, O&M 89%, regulatory enforcement 34%, policy framework effectiveness 78%, inter-agency coordination 45%. "
                         "Community participation reported as explaining 67.3% of between-study variance (beta 8.7 per point on an undefined 1-10 score); VLOM programmes +16.7 percentage points, Cohen d 0.89 (8 studies); north-south gap 46.1% vs 58.4% (p = 0.031). Authors list institutional mandates and policy strength (r = 0.78) among the top three factors."),
        study_design='systematic review and meta-analysis (secondary; 141 studies; Google Scholar/PubMed/SciSpace/arXiv plus grey literature; two-reviewer screening; NOS quality assessment not reported)',
        model_type='systematic review with random-effects meta-analysis and meta-regression (reported inconsistently)',
        section='Abstract; Method 2.1-2.6; Results 3.1-3.7 and Table 2; Discussion; Conclusion (full text)',
        exact_location='Abstract p1; Method p238-241 (design, search, Table 1 eligibility, extraction, statistics); Results 3.1-3.7 p241-246 (flow, 23 factors, criticality, Table 2 p246); Conclusion p248 (different CI and I2 from results)'),
    note=("Full-text appraisal 2026-10-04 from the PDF in the researcher's Drive (record RE8F43EAB1543; Figures 1-7 not read). Replaces the citation-level entry of 2026-09-15. "
          "INTERNAL INCONSISTENCIES (do not cite the pooled numbers without the paper's data): 51 vs 23 vs 16 studies for the pooled functionality estimate; the same 52.3% (47.8-56.8) is also given for 'handpumps' (n = 23); CI and I2 differ between abstract/results and conclusion; the 1-10 community participation score is never defined; Cohen d and an odds ratio are attached to percentage differences. "
          "Legal/institutional content: institutional mandates, policy framework, RUWASSA performance, inter-agency coordination and regulatory enforcement are among the 23 factors (frequency of mention only)."))

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
    r['researcher'] = 'Claude-AI-extraction-2026-10-04 (full-text appraisal)'; r['date_extracted'] = DATE
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(ED), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, ED)
cit = {r['study_id']: r['citation'] for r in rows if r['study_id'] in S}
for sid, d in S.items():
    L = [f"# AMSTAR 2 appraisal (full text) — {sid}", "", f"**Citation:** {cit[sid]}", "",
         f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF in the researcher's Drive (not committed). Figures (flow diagrams, charts) and all supplementary files were **not read**. Supersedes the earlier abstract-level entry. Appraised by the AI; not independently verified.", "",
         f"**Overall confidence: {d['rating']}** — {d['basis']}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
         "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
    for i, name in ITEMS.items():
        a, b = d['ans'][i]
        L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a} | {b} |")
    L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). AMSTAR 2 rating rule: no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low. A 'Partial Yes' is not a flaw."]
    open(f'04_quality/appraisal_forms/{sid}_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print('appraised', ', '.join(S))
