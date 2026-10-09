#!/usr/bin/env python3
"""Read-only data-quality audits that need no source papers. Nothing here changes a flag, a rating or a decision.

  1. Quantitative-synthesis-eligible flag audit: for each of the studies flagged TRUE, does the extraction show any inferential result?
       A  uncertainty present      CI, SE or p-value in the structured fields, or interval/p-value language in the estimate text
       B  model named, no uncertainty  an inferential design/model (regression, RCT, DiD, PSM, ...) but the extraction holds no interval/SE/p
       C  descriptive or unclear   percentages, case-study/survey statistics, or nothing numeric -> the flag looks overstated
     The categories are a heuristic to prioritise human review (the flag is a Phase 11 judgment; EVIDENCE_MAP_README).
  3. AMSTAR 2 narrative-review sweep: how strongly do the RECORDED fields (publication_type, study_design, effect_measure, model_type, sample_size)
     evidence a systematic method? Score = registration/PRISMA/JBI-method (+2), a stated count of included studies (+2), the word "systematic" (+1),
     scoping/realist/mapping/meta-analysis (+1), "narrative-review wording (-2, or -1 when a systematic element is also recorded; "narrative synthesis" is not penalised). Lowest first = least evidenced.
     The score is only a way to order which full texts to obtain first; recorded fields are the AI's own summaries, not the papers.
  2. Consistency scan of effect_sizes.csv: interval order; direction wording versus a stated interval (null vs excludes-null);
     effect-size rows for studies not flagged eligible; blank family without a reasoned non-fit; missing adjusted/reason fields.
Writes 05_analysis/descriptive/quantitative_flag_audit_2026-09-29.csv and DATA_QUALITY_AUDIT_2026-09-29.md. Run from the project root.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT_CSV = ROOT / '05_analysis/descriptive/quantitative_flag_audit_2026-09-29.csv'
OUT_MD = ROOT / '05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md'
OUT_AM = ROOT / '05_analysis/descriptive/amstar2_systematic_evidence_sweep_2026-09-29.csv'

INFERENTIAL = re.compile(r'regress|logit|probit|\bols\b|difference-in-difference|(?-i:\bDiD\b)|propensity|instrumental|\biv\b|panel|fixed.effect|random.effect|multilevel|mixed.effect|'
                         r'randomi[sz]|\brct\b|meta-analy|\bglm\b|\bcox\b|hazard|odds ratio|regression discontinuity|structural equation|\bsem\b|time.series|arima|'
                         r'poisson|negative binomial|tobit|matching|synthetic control|event.study|spatial|econometric|anova|t-test|chi-?square|mann-whitney|kruskal', re.I)
UNCERTAINTY_TEXT = re.compile(r'95\s?%\s?ci|confidence interval|\bci\b\s*[\[(:=\d]|\bp\s?[<=>]|p-value|standard error|\bs\.?e\.?\b\s*[=(:]|\bsig(nificant|nificantly)\b', re.I)
NUM = r'-?\d+(?:\.\d+)?'


def flag_audit():
    ed = {r['study_id']: r for r in cf.read('ed')}
    em = {r['study_id']: r for r in cf.read('em')}
    es = {r['study_id'] for r in cf.read('es')}
    rows = []
    for s in sorted((s for s, r in em.items() if r['quantitative_synthesis_eligible'] == 'TRUE'), key=lambda x: int(x[1:])):
        r = ed[s]
        has_ci = bool(r['lower_CI'].strip() or r['upper_CI'].strip())
        has_se, has_p = bool(r['standard_error'].strip()), bool(r['p_value'].strip())
        text_unc = bool(UNCERTAINTY_TEXT.search(r['effect_estimate']))
        model_txt = ' '.join([r['model_type'], r['effect_measure'], r['study_design']])
        inferential = bool(INFERENTIAL.search(model_txt))
        has_numbers = len(re.findall(NUM, r['effect_estimate'])) >= 1
        if has_ci or has_se or has_p or text_unc:
            cat, why = 'A', 'interval, SE, p-value or significance wording present'
        elif inferential:
            cat, why = 'B', 'inferential model/design named but no interval, SE or p-value extracted'
        else:
            cat, why = 'C', 'descriptive/unclear: no interval, SE or p-value and no inferential model named' + ('' if has_numbers else '; no numbers in the estimate text')
        rows.append({'study_id': s, 'category': cat, 'has_effect_size_row': s in es, 'has_CI': has_ci, 'has_SE': has_se, 'has_p_value': has_p,
                     'uncertainty_wording_in_estimate': text_unc, 'inferential_model_named': inferential, 'risk_of_bias_tool': cf.tool_of(r['risk_of_bias_tool']),
                     'effect_measure': r['effect_measure'][:120], 'model_type': r['model_type'][:100], 'why': why,
                     'abstract_only': r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)})
    return rows


def amstar_sweep():
    ed = {r['study_id']: r for r in cf.read('ed')}
    rows = []
    for s, r in ed.items():
        if cf.tool_of(r['risk_of_bias_tool']) != 'AMSTAR 2':
            continue
        txt = ' | '.join([r['publication_type'], r['study_design'], r['effect_measure'], r['model_type'], r['sample_size']]).lower().replace('systematic_review_secondary', '')
        sig, score = [], 0
        if re.search(r'prisma|prospero|jbi methodology|cochrane|registered', txt): score += 2; sig.append('registration/PRISMA/JBI method named')
        if re.search(r'\d+\s*(studies|documents|items|articles|sources|papers|records)|\(\d+\s|included studies|screened', txt): score += 2; sig.append('count of included studies stated')
        if 'systematic' in txt: score += 1; sig.append('word "systematic"')
        if re.search(r'scoping|realist|mapping|meta-analy', txt): score += 1; sig.append('scoping/realist/mapping/meta-analysis')
        if re.search(r'narrative (review|survey|overview)|narrative/', txt):  # "narrative synthesis" is normal in a systematic review and is not penalised
            if 'systematic search' in txt: score -= 1; sig.append('narrative review with a systematic search (hybrid)')
            else: score -= 2 if 'systematic' not in txt else 1; sig.append('narrative-review wording')
        ao = r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)
        rows.append({'study_id': s, 'evidence_score': score, 'abstract_only': ao, 'formally_rated': not r['risk_of_bias_rating'].startswith('Not ratable'),
                     'signals': '; '.join(sig) or 'none in recorded fields', 'recorded_method_text': txt.strip(' |')[:200]})
    return sorted(rows, key=lambda x: (x['evidence_score'], not x['abstract_only'], int(x['study_id'][1:])))


def year_audit():
    """publication_year in the extraction row vs the year in the full-text screening record (same paper, two sources)."""
    ed = cf.read('ed')
    ft = {r['record_id']: r for r in cf.read('ft')}
    out = []
    for r in ed:
        y, fy = r['publication_year'].strip(), ft[r['record_id']]['year'].strip()
        if y != fy:
            d = (int(y) - int(fy)) if y.isdigit() and fy.isdigit() else None
            out.append((r['study_id'], y or '(blank)', fy or '(blank)', d))
    return sorted(out, key=lambda x: int(x[0][1:]))


def certainty_audit():
    """mechanism_certainty 3/4 means quasi-experimental/experimental evidence (CODEBOOK section 9). Does the coding agree with the design/tool?"""
    ed = {r['study_id']: r for r in cf.read('ed')}
    causal = {s for s, r in ed.items() if cf.tool_of(r['risk_of_bias_tool']) in ('ROBINS-I', 'RoB 2')}
    hi = {s for s, r in ed.items() if r['mechanism_certainty'] in ('3', '4')}
    code = lambda s: ed[s]['mechanism_certainty'] if ed[s]['mechanism_certainty'] in ('0', '1', '2', '3', '4') else 'narrative'
    return {'hi_total': len(hi), 'hi_in_causal': len(hi & causal), 'hi_outside': sorted(hi - causal, key=lambda x: int(x[1:])),
            'hi_outside_tools': Counter(cf.tool_of(ed[s]['risk_of_bias_tool']) for s in hi - causal), 'causal_total': len(causal),
            'causal_by_code': Counter(code(s) for s in causal)}


def _num(s):
    m = re.search(NUM, s.replace('−', '-'))
    return float(m.group(0)) if m else None


CI_TEXT = re.compile(r'(?:95\s?%\s?)?(?:\bci\b|confidence interval)[^\d\-−]{0,14}(-?\d+(?:\.\d+)?)\s*(?:to|,|;|–|—)\s*(-?\d+(?:\.\d+)?)', re.I)


def es_scan():
    em = {r['study_id']: r for r in cf.read('em')}
    out = []
    cov = Counter()
    for r in cf.read('es'):
        s = r['study_id']
        lo, hi = r['lower_CI'].strip(), r['upper_CI'].strip()
        single = re.fullmatch(NUM + r'%?', lo.replace('−', '-')) and re.fullmatch(NUM + r'%?', hi.replace('−', '-'))
        if not single:
            cis = CI_TEXT.findall(r['effect_estimate'].replace('−', '-'))
            if len(cis) == 1:  # exactly one interval stated in the text: usable; several = several outcomes, ambiguous
                lo, hi = cis[0]
                single = True
                cov['text_interval'] += 1
        else:
            cov['structured_interval'] += 1
        cov['rows'] += 1
        d = r['direction'].lower()
        # the bare word "or" (English conjunction) used to match here and mark difference-scale rows as ratio-scale (S294, S398, S631, S780, S920); now needs a number after OR/RR/HR (2026-10-04 review)
        ratio = bool(re.search(r'\bor\b\s*[=:(]?\s*-?\d|odds|\brr\b\s*[=:(]?\s*\d|risk ratio|\bhr\b\s*[=:(]?\s*\d|hazard|\birr\b|incidence rate ratio', (r['effect_measure'] + ' ' + r['effect_estimate']).lower()))
        if single:
            l, h = _num(lo), _num(hi)
            if l > h:
                out.append((s, 'interval_reversed', f'lower {lo} > upper {hi}'))
            null = 1.0 if ratio else 0.0
            excludes = not (l <= null <= h)
            if d.startswith('null') and excludes:
                out.append((s, 'null_direction_but_interval_excludes_null', f'direction "{r["direction"][:60]}" but interval {lo} to {hi} excludes {null:g} ({"ratio" if ratio else "difference"} scale assumed)'))
            if re.match(r'(positive|negative)', d) and 'significant' in d and 'not significant' not in d and not excludes:
                out.append((s, 'significant_direction_but_interval_includes_null', f'direction "{r["direction"][:60]}" but interval {lo} to {hi} includes {null:g}'))
        if em[s]['quantitative_synthesis_eligible'] != 'TRUE':
            out.append((s, 'row_for_study_not_flagged_eligible', 'known: S589 (DECISIONS A1)' if s == 'S589' else 'new'))
        if not r['synthesis_family'].strip() and not r['exclusion_from_pooling_reason'].strip():
            out.append((s, 'blank_family_without_reason', ''))
        if not r['adjusted'].strip():
            out.append((s, 'adjusted_blank', ''))
        if not r['effect_estimate'].strip() or not r['direction'].strip():
            out.append((s, 'estimate_or_direction_blank', ''))
        if not r['exclusion_from_pooling_reason'].strip():
            out.append((s, 'no_reason_recorded_for_not_pooling', ''))
    return out, cov


def render(rows, findings, es_n, cov, am, yrs, cert):
    c = Counter(r['category'] for r in rows)
    pooled_n = sum(r_['included_in_pooled_estimate'] == 'TRUE' for r_ in cf.read('es'))
    s277_clause = ', and S277 (found descriptive-only on its full text) is one of them' if any(r['study_id'] == 'S277' and r['category'] == 'C' for r in rows) else ''
    withrow = Counter(r['category'] for r in rows if r['has_effect_size_row'])
    tools = Counter((r['category'], r['risk_of_bias_tool']) for r in rows)
    L = ["# Data-quality audit (generated — do not edit by hand)", "",
         "Generated by `code/analysis/audit_data_quality.py`. **Read-only: no flag, rating or decision was changed.** Heuristics prioritise human review; they are not verdicts.", "",
         "## 1. Is `quantitative_synthesis_eligible = TRUE` supported by the extracted results?", "",
         f"{len(rows)} studies carry the flag (a Phase 11 feasibility judgment; `EVIDENCE_MAP_README.md`). Of these, {es_n} have an `effect_sizes.csv` row. Categories:", "",
         "| Category | Meaning | Studies | of which with an effect-size row |", "|---|---|---|---|",
         f"| A | interval, SE, p-value or significance wording present | {c['A']} | {withrow['A']} |",
         f"| B | inferential model named, but no interval/SE/p-value extracted | {c['B']} | {withrow['B']} |",
         f"| C | descriptive or unclear — the flag looks overstated | {c['C']} | {withrow['C']} |", "",
         "Category C by risk-of-bias tool: " + ", ".join(f"{t} {n}" for (k, t), n in sorted(tools.items(), key=lambda kv: -kv[1]) if k == 'C') + ".", "",
         f"**Reading it:** the flag marks studies that *might* support a quantitative synthesis; {c['C']} of {len(rows)} ({100 * c['C'] / len(rows):.0f}%) show nothing inferential in the extraction{s277_clause}. "
         "Category B studies may well have estimates in the paper that the extraction did not capture — a re-extraction question, not a flag question. "
         f"Only {es_n} studies have an effect-size row and {'none is pooled' if not pooled_n else str(pooled_n) + ' are pooled'}, so **no synthesis result depends on the flag**; what it changes is the size of the pool that Phase 11 believed was available. "
         "Per-study list: `quantitative_flag_audit_2026-09-29.csv`. Whether to unflag any study is a researcher decision.", "",
         f"## 2. Consistency scan of `effect_sizes.csv` ({es_n} rows)", ""]
    if findings:
        L += ["| Study | Check | Detail |", "|---|---|---|"] + [f"| {s} | `{k}` | {d} |" for s, k, d in sorted(findings, key=lambda f: (f[1], int(f[0][1:])))]
        L += ["", "Each line is a prompt to look at the row against its paper, not proof of an error: direction wording is a synthesis judgment (sign and valence can differ — see the Family A and C documents), and interval scale (ratio vs difference) is inferred from the measure text."]
    else:
        L += ["No findings."]
    L += ["", f"**Coverage:** an interval could be checked for {cov['structured_interval']} rows (structured `lower_CI`/`upper_CI`) plus {cov['text_interval']} rows with exactly one interval stated in the estimate text, i.e. {cov['structured_interval'] + cov['text_interval']} of {es_n}; "
          "the rest have no interval, several intervals for several outcomes, or free-text intervals, so the interval checks say nothing about them.", "", "Checks run: interval order; `null` direction vs an interval excluding the null value; `significant` direction vs an interval including it; effect-size rows for studies not flagged eligible; blank family without a recorded non-pooling reason; blank `adjusted`, estimate, direction or reason. "
          "Duplicate study across families is impossible by construction (one row per study; the verifier enforces it)."]
    L += ["", f"## 3. AMSTAR 2 studies: how well do the recorded fields evidence a systematic method? ({len(am)} studies)", "",
          "Ordered least-evidenced first (see the script docstring for the score). Signals come from the AI's own recorded summary fields, not from the papers — a high score is not confirmation and a low one is not a finding; it orders which full texts to obtain first.", "",
          "| Study | Score | Abstract-only | Formally rated | Signals in recorded fields |", "|---|---|---|---|---|"] + \
         [f"| {a['study_id']} | {a['evidence_score']} | {'yes' if a['abstract_only'] else 'no'} | {'yes' if a['formally_rated'] else 'no'} | {a['signals']} |" for a in am] + \
         ["", "The weakest-evidenced studies deserve the earliest full-text check; S329 (\"narrative review with systematic search\") and S418 (\"narrative/scoping review\") are hybrids where the question is real, not just unconfirmed.", ""]
    big = [y for y in yrs if y[3] is None or abs(y[3]) > 1]
    L += ["", "## 4. `publication_year` versus the screening record's year", "",
          f"{len(yrs)} of the extraction rows have a different year from their full-text screening record; {len(yrs) - len(big)} differ by one year (usually online-first versus issue year), "
          f"and {len(big)} differ by more or are blank: " + ", ".join(f"{s} ({a} vs {b})" for s, a, b, d in big) + ". "
          "The report's recency statistics use the extraction field; a one-year difference cannot change them materially, but the larger ones should be checked against the papers. Not corrected here.", ""]
    cc = cert['causal_by_code']
    L += ["", "## 5. `mechanism_certainty` 3–4 versus study design", "",
          f"`mechanism_certainty` 3 means quasi-experimental and 4 experimental evidence (`CODEBOOK.md` §9). {cert['hi_total']} studies carry 3 or 4, but **only {cert['hi_in_causal']} of them are ROBINS-I or RoB 2 studies**; "
          f"{len(cert['hi_outside'])} sit in other designs ({', '.join(f'{t} {n}' for t, n in cert['hi_outside_tools'].most_common())}), e.g. " + ", ".join(cert['hi_outside'][:6]) + ". "
          f"Conversely, of the {cert['causal_total']} ROBINS-I/RoB 2 studies, {cc['4'] + cc['3']} are coded 3–4, {cc['2']} are coded 2, {cc['1']} are coded 1 and {cc['narrative']} carry narrative text instead of a 0–4 code. "
          "So the number of studies at certainty 3–4 is **not** a count of quasi-experimental or experimental studies, and the two figures (causal-capable designs, certainty 3–4) should not be read as the same thing. "
          "Which coding is wrong (the certainty or the design/tool) needs the papers; nothing was changed.", ""]
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    rows = flag_audit(); findings, cov = es_scan(); am = amstar_sweep(); yrs = year_audit(); cert = certainty_audit()
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(render(rows, findings, len(cf.read('es')), cov, am, yrs, cert), encoding='utf-8')
    with open(OUT_AM, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(am[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(am)
    print('wrote', OUT_MD.name, OUT_CSV.name, dict(Counter(r['category'] for r in rows)), len(findings), 'es findings')
