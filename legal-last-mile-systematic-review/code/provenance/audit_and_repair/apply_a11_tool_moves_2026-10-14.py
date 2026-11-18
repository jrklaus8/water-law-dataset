"""2026-10-14: open item A11 (approved by the PI): five appraisal-tool moves proposed on 2026-10-04 (S345 and S231 to CASP Qualitative, S333 and S334 to MMAT, S310 to JBI Cross-Sectional) plus S480 from NONE to the
Legal Institutional Evidence Appraisal Framework. For each study the rating is re-answered with the SAME rule-based batch method as the 2026-09-28 batches (04_quality/appraisal_forms/*_batch_2026-09-28.md), applied to the
extraction fields (and, for the two MMAT moves, to the item-level text of the superseded CASP rating, which was written from the full text on 2026-10-04). They are rule-based re-answers, not a fresh signalling-question read of each paper.
The old tool and rating (which belonged to the wrong instrument) are kept in each row's extraction_note. The moves and every item are listed in 04_quality/appraisal_forms/A11_TOOL_MOVES_2026-10-14.md. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '03_extraction/extracted_data/extraction_database.csv'
MARK = 'A11 tool move 2026-10-14'
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
           f". Per CASP's own guidance no composite score is computed -- see 04_quality/appraisal_forms/CASP_Qualitative_batch_2026-09-28.md (rule-based re-answer after the A11 tool move, {D}).")
    return 'CASP Qualitative Checklist', txt, a


def mmat(r, extra=''):
    s12 = 'Yes' if r['population'].strip() else "Can't tell"
    integ = 'Yes' if INTEGRATION.search(r['extraction_note'] + ' ' + r['exact_location'] + ' ' + extra) else "Can't tell"
    txt = (f"MMAT screening: S1={s12}, S2={s12}. Mixed-methods criteria: 5.1(rationale)=Can't tell, 5.2(integration)={integ}, 5.3(meta-inference)=Can't tell, 5.4(divergence)=Can't tell, 5.5(component quality)=Can't tell. "
           f"Per MMAT's own guide, no composite score is computed -- see per-criterion answers above and 04_quality/appraisal_forms/MMAT_batch_2026-09-28.md (rule-based re-answer after the A11 tool move, {D}).")
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
           + ','.join(i[k] for k in range(1, 9)) + f"; {y}/8 Yes; re-answered after the A11 tool move)")
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
    txt = (f"Legal Institutional Evidence Appraisal Framework (condensed appraisal, re-answered {D} after the A11 tool move): 2(jurisdictional specificity)={c2}; 3(exposure definition)={c3}; 4(outcome definition)={c4}; "
           f"8(causal identification)=mechanism_certainty={r['mechanism_certainty']} (project's own scale, see DATA_DICTIONARY.md); 10(institutional context)={c10}; "
           "1(legal source accuracy),5(sampling transparency),6(selection process),7(measurement transparency),9(confounding treatment),11(replication potential),12(coding transparency),13(researcher reflexivity)=not assessable at this pass (extraction depth). "
           "See 04_quality/appraisal_forms/LegalFramework_batch_2026-09-28.md.")
    return 'Legal Institutional Evidence Appraisal Framework', txt


raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
by = {r['study_id']: r for r in rows}
log = []
for sid, kind in (('S345', 'casp'), ('S231', 'casp'), ('S333', 'mmat'), ('S334', 'mmat'), ('S310', 'jbi'), ('S480', 'framework')):
    r = by[sid]
    if MARK in r['extraction_note']:
        continue
    old_tool, old_rating = r['risk_of_bias_tool'], r['risk_of_bias_rating']
    new_bias = {}
    if kind == 'casp':
        tool, rating, items = casp(r); detail = ', '.join(f'{k}={v}' for k, v in items.items() if v == 'Yes') + ' Yes; the rest Can\'t tell'
        new_bias = dict(selection_bias='', measurement_bias='', confounding='', attrition='', reporting_bias='')
    elif kind == 'mmat':
        tool, rating, items = mmat(r, old_rating); detail = ', '.join(f'{k}={v}' for k, v in items.items())
        new_bias = dict(selection_bias='', measurement_bias='', confounding='', attrition='', reporting_bias='')
    elif kind == 'jbi':
        tool, rating, items, new_bias = jbi(r); detail = rating.split('(')[0].strip() + '; items ' + ','.join(items[k] for k in range(1, 9))
    else:
        tool, rating = framework(r); detail = 'condensed 5-domain appraisal'
    r['extraction_note'] = r['extraction_note'].rstrip() + (f" [{MARK} (PI ruling A11): risk_of_bias_tool '{old_tool[:200]}' -> '{tool}'. The previous rating belonged to the wrong instrument and is kept here: {old_rating[:900]}. "
                                                              "The new rating is the rule-based batch method applied to the extraction fields, not a fresh signalling-question read of the paper.]")
    r['risk_of_bias_tool'], r['risk_of_bias_rating'] = tool, rating
    r.update(new_bias)
    log.append((sid, old_tool.split(' (')[0].split(' --')[0][:40], tool, detail))
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
os.replace(tmp, P)
for l in log:
    print(l)
if log:
    L = ['# A11 appraisal-tool moves — 2026-10-14', '',
         "Approved by the PI on 2026-10-14 (open item A11): S345 and S231 to CASP Qualitative, S333 and S334 to MMAT, S310 to JBI Cross-Sectional, and S480 from NONE to the Legal Institutional Evidence Appraisal Framework. "
         "Each rating was re-answered with the rule-based batch method of 2026-09-28 (see the batch files in this folder) on the extraction fields; S333 and S334 also use the item-level text of their superseded CASP ratings (full text read on 2026-10-04). "
         "These are rule-based re-answers, not a fresh signalling-question read of each paper. The old tool and rating are kept in each row's `extraction_note`.", '',
         '| Study | From | To | New answers |', '|---|---|---|---|']
    L += [f'| {s} | {a} | {b} | {c} |' for s, a, b, c in log]
    open('04_quality/appraisal_forms/A11_TOOL_MOVES_2026-10-14.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
