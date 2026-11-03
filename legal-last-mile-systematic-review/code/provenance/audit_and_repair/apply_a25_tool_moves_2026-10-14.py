"""2026-10-14: open item A25 (PI rulings of 2026-10-14): two of the five studies kept in the E05 recheck change appraisal tool.
S335 (Piura, Peru: targeted 40-document review plus institutional data) moves from CASP Qualitative to the Legal Institutional Evidence Appraisal Framework, as the PI asked; S288 (Baghdad household survey, n = 300) moves from MMAT to JBI
Cross-Sectional, because the PI ruled that its weak reporting belongs in its JBI rating rather than in an exclusion (its household survey, stakeholder survey and GIS work are all quantitative, so MMAT's mixed-methods criteria do not fit).
S267, S181 and S281 keep the tools they have (Legal Framework, JBI Cross-Sectional, Legal Framework). Ratings are re-answered with the same rule-based batch method as 2026-09-28 / the A11 moves (functions copied from
apply_a11_tool_moves_2026-10-14.py); they are not a fresh signalling-question read. The old tool and rating stay in the row's extraction_note. evidence_map.csv `study_design_class` is kept in step where the verifier requires it
(S288 mixed_methods -> observational). Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
MARK = 'A25 tool move 2026-10-14'
D = '2026-10-14'
CASP_METHODS = re.compile(r'interview|focus.group|ethnograph|documentary|archival|narrative|grounded theory|discourse|documents|observation', re.I)
STAT_METHODS = re.compile(r'regression|logit|probit|OLS|GLM|GMM|ANOVA|chi-square|structural equation|SEM', re.I)
ADMIN_OUTCOME = re.compile(r'administrative|census|billing|regulatory|register|records', re.I)
INTEGRATION = re.compile(r'triangulat|informed by|combined with|cross-validat|integrat', re.I)


def casp(r):
    a = {1: 'Yes' if r['population'].strip() else "Can't tell",
         2: 'Yes' if re.search(r'qualitative', r['study_design'], re.I) else "Can't tell",
         3: "Can't tell", 4: "Can't tell",
         5: 'Yes' if CASP_METHODS.search(r['study_design']) else "Can't tell",
         6: "Can't tell", 7: "Can't tell", 8: "Can't tell",
         9: 'Yes' if r['effect_estimate'].strip() else "Can't tell", 10: "Can't tell"}
    names = {1: 'aims', 2: 'qual approach', 3: 'design', 4: 'recruitment', 5: 'data collection', 6: 'researcher-participant', 7: 'ethics', 8: 'analysis rigor', 9: 'findings', 10: 'value'}
    txt = ('CASP Qualitative per-item: ' + '; '.join(f'{i}({names[i]})={a[i]}' for i in range(1, 11)) +
           f". Per CASP's own guidance no composite score is computed -- see 04_quality/appraisal_forms/CASP_Qualitative_batch_2026-09-28.md (rule-based re-answer after the A25 tool move, {D}).")
    return 'CASP Qualitative Checklist', txt, a


def mmat(r, extra=''):
    s12 = 'Yes' if r['population'].strip() else "Can't tell"
    integ = 'Yes' if INTEGRATION.search(r['extraction_note'] + ' ' + r['exact_location'] + ' ' + extra) else "Can't tell"
    txt = (f"MMAT screening: S1={s12}, S2={s12}. Mixed-methods criteria: 5.1(rationale)=Can't tell, 5.2(integration)={integ}, 5.3(meta-inference)=Can't tell, 5.4(divergence)=Can't tell, 5.5(component quality)=Can't tell. "
           f"Per MMAT's own guide, no composite score is computed -- see per-criterion answers above and 04_quality/appraisal_forms/MMAT_batch_2026-09-28.md (rule-based re-answer after the A25 tool move, {D}).")
    return 'MMAT', txt, {'S1': s12, 'S2': s12, '5.2': integ}


def jbi(r):
    i = {1: 'Yes' if r['population'].strip() and r['sample_size'].strip() else 'Unclear', 2: 'Yes' if r['population'].strip() and r['country'].strip() else 'Unclear', 3: 'Unclear',
         4: 'Yes' if ADMIN_OUTCOME.search(r['study_design']) else 'Unclear', 5: 'Yes' if r['covariates'].strip() else 'Unclear'}
    i[6] = 'Yes' if r['covariates'].strip() and STAT_METHODS.search(r['study_design'] + ' ' + r['model_type']) else 'Unclear'
    i[7] = i[4]
    i[8] = 'Yes' if STAT_METHODS.search(r['study_design'] + ' ' + r['model_type']) else 'Unclear'
    y = sum(v == 'Yes' for v in i.values())
    overall = 'Low concern' if y >= 6 else ('Some concern' if y >= 3 else 'High concern (sparse extraction, not necessarily a weak study)')
    txt = (f"{overall} (appraised {D} against the official JBI Cross Sectional checklist; rule-based batch appraisal, see 04_quality/appraisal_forms/JBI_CrossSectional_batch_2026-09-28.md -- items 1-8: "
           + ','.join(i[k] for k in range(1, 9)) + f"; {y}/8 Yes; re-answered after the A25 tool move)")
    bias = dict(selection_bias=f"Item 1 (inclusion criteria): {i[1]}; Item 2 (subjects/setting): {i[2]}",
                measurement_bias=f"Item 3 (exposure validity): {i[3]}; Item 4 (outcome objectivity): {i[4]}; Item 7 (outcome validity): {i[7]}",
                confounding=f"Item 5 (confounders identified): {i[5]}; Item 6 (confounders addressed): {i[6]}", attrition='', reporting_bias='Not independently assessed (JBI checklist has no dedicated selective-reporting item)')
    return 'JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies', txt, i, bias


def framework(r):
    country, ls = r['country'].strip(), r['legal_system'].strip()
    c2 = f'adequate (country recorded: {country})' if country else 'not assessable (no country)'
    c3 = r['legal_measurement_quality'].strip() or 'not assessable (legal_measurement_quality not populated at extraction)'
    c4 = r['outcome_measurement_quality'].strip() or 'not assessable (outcome_measurement_quality not populated at extraction)'
    c10 = f'adequate ({ls} legal system, {country})' if country and ls else 'not assessable'
    txt = (f"Legal Institutional Evidence Appraisal Framework (condensed appraisal, re-answered {D} after the A25 tool move): 2(jurisdictional specificity)={c2}; 3(exposure definition)={c3}; 4(outcome definition)={c4}; "
           f"8(causal identification)=mechanism_certainty={r['mechanism_certainty']} (project's own scale, see DATA_DICTIONARY.md); 10(institutional context)={c10}; "
           "1(legal source accuracy),5(sampling transparency),6(selection process),7(measurement transparency),9(confounding treatment),11(replication potential),12(coding transparency),13(researcher reflexivity)=not assessable at this pass (extraction depth). "
           "See 04_quality/appraisal_forms/LegalFramework_batch_2026-09-28.md.")
    return 'Legal Institutional Evidence Appraisal Framework', txt



EXTRA = {'S288': " Reporting weaknesses recorded at the 2026-10-04 full-text re-extraction and not captured by the rule: the methods text describes planned rather than conducted steps, and the tables do not reconcile with the stated n (the earlier MMAT rating was 1 of 5)."}
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
by = {r['study_id']: r for r in rows}
log = []
for sid, kind in (('S335', 'framework'), ('S288', 'jbi')):
    r = by[sid]
    if MARK in r['extraction_note']:
        continue
    old_tool, old_rating = r['risk_of_bias_tool'], r['risk_of_bias_rating']
    new_bias = {}
    if kind == 'jbi':
        tool, rating, items, new_bias = jbi(r); detail = rating.split('(')[0].strip() + '; items ' + ','.join(items[k] for k in range(1, 9))
    else:
        tool, rating = framework(r); detail = 'condensed 5-domain appraisal'
    rating += EXTRA.get(sid, '')
    r['extraction_note'] = r['extraction_note'].rstrip() + (f" [{MARK} (PI ruling A25): risk_of_bias_tool '{old_tool[:200]}' -> '{tool}'. The previous rating belonged to the other instrument and is kept here: {old_rating[:900]}. "
                                                              "The new rating is the rule-based batch method applied to the extraction fields, not a fresh signalling-question read of the paper.]")
    r['risk_of_bias_tool'], r['risk_of_bias_rating'] = tool, rating
    r.update(new_bias)
    log.append((sid, old_tool.split(' (')[0].split(' --')[0][:40], tool, detail))
if log:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, P)
    L = ['# A25 appraisal-tool moves, 2026-10-14', '',
         "PI ruling of 2026-10-14 (open item A25): of the five studies kept in the E05 recheck, S335 moves from CASP Qualitative to the Legal Institutional Evidence Appraisal Framework and S288 from MMAT to JBI Cross-Sectional (weak reporting goes into its JBI rating, not into an exclusion). "
         "S267, S181 and S281 keep their tools. Ratings are the rule-based batch method re-answered on the extraction fields, not a fresh signalling-question read; the old tool and rating are kept in each row's `extraction_note`.", '',
         '| Study | From | To | New answers |', '|---|---|---|---|'] + [f'| {s} | {a} | {b} | {c} |' for s, a, b, c in log]
    L += ['', "`study_design_class` in `evidence_map.csv` was kept in step where the verifier requires it: S288 `mixed_methods` -> `observational` (a JBI tool must sit with an observational design). S335 stays `qualitative`."]
    open('04_quality/appraisal_forms/A25_TOOL_MOVES_2026-10-14.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
for l in log:
    print(l)
raw = open(EM, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(EM, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); ef = rd.fieldnames; erows = list(rd)
n = 0
for r in erows:
    if r['study_id'] == 'S288' and r['study_design_class'] != 'observational':
        r['study_design_class'] = 'observational'; n += 1
if n:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=ef, lineterminator=eol); w.writeheader(); w.writerows(erows)
    os.replace(tmp, EM)
print(n, 'design class(es) updated')
