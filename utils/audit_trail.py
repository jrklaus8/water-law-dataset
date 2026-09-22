#!/usr/bin/env python3
"""
audit_trail.py — make the jurimetric coding auditable case by case
===================================================================
`jurimetric_coding.py` now emits, for every decision, the rule that assigned its
`governance_cat` and the substring that rule matched. This script turns those
columns into an audit bundle a reviewer can read without running anything:

  AUDIT_TRAIL.md            evidence sample per category, plus diagnostics
  audit_sample.csv          the same sample as data, with permalinks
  audit_rule_coverage.csv   how many decisions each individual rule decided

It also runs one diagnostic the coding engine cannot run on itself.

The Dutch compound diagnostic
-----------------------------
`_WATER_CORE_RE` gates the whole classifier: a decision with no match is
returned as `not_water_related` without any category ever being considered. Its
terms are written with `\\b` word boundaries, which is correct for Portuguese and
English but wrong for Dutch, because Dutch compounds nouns without spaces.
`\\bgrondwater\\b` does not match `grondwateronttrekking`, and `\\bwater\\b` does not
match `waterwet` or `watervergunning`.

This is not hypothetical. In `validation/second_coder_sample_raw.csv`, 65 of the
100 decisions in the `NL_broad_water` stratum contain a Dutch water compound
that the filter cannot see, and the human coder labelled 61 of them WATER. That
is the mechanism behind the 0.3579 precision recorded for that stratum in
`validation/precision_recall_results.json`.

The diagnostic reports the size of the effect. It deliberately does NOT change
any label: rewriting the filter would reclassify tens of thousands of decisions
and invalidate the deposited v0.3.0, the kappa results and the supervisor
report. That is a research decision, not a tooling decision.

Usage
-----
    python utils/audit_trail.py --csv data/water_law_global_coded.csv
    python utils/audit_trail.py --csv <coded.csv> --per-category 25 --seed 42
"""
import argparse
import csv
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from resolve_case import resolve
except ImportError:
    def resolve(**kw):
        return {'permalink': kw.get('url') or '', 'permalink_kind': 'scraped_url',
                'identifier': kw.get('case_id') or '', 'fulltext_url': ''}

# Dutch water compounds that `_WATER_CORE_RE` cannot match because of its
# word boundaries. Substring matching, because that is the point.
NL_COMPOUNDS = [
    'waterwet', 'watervergunning', 'waterschapsbelasting', 'waterschapsheffing',
    'waterhuishouding', 'waterbodem', 'waterplan', 'waterstaatswerk',
    'waterzuivering', 'waterkwaliteit', 'watervoorziening', 'waterverontreiniging',
    'wateronttrekking', 'waterstand', 'waterleidingbedrijf',
    'grondwateronttrekking', 'grondwaterstand', 'grondwaterbeheer',
    'grondwaterbescherming', 'drinkwatervoorziening', 'drinkwaterbedrijf',
    'drinkwaterleiding', 'drinkwaterwinning', 'drinkwaterwet',
    'afvalwater', 'afvalwaterzuivering', 'oppervlaktewater', 'regenwater',
    'hemelwater', 'rioolwater', 'rioolwaterzuivering', 'zwemwater',
    'koelwater', 'bluswater', 'hoogheemraadschap', 'wetterskip',
]
NL_COMPOUND_RE = re.compile('|'.join(re.escape(t) for t in NL_COMPOUNDS), re.I)

# A copy of the production water-core gate, used read-only to show which rows
# it can and cannot see. Kept in sync with jurimetric_coding._WATER_CORE_RE.
WATER_CORE_RE = re.compile(
    r'\bwater(?:schap|leiding|kering|winning|onttrekking|toets|berging|peil'
    r'|beheer|overlast|schade|staat|taak|gang|werk)?\b'
    r'|\bdrinkwater\b|\bgrondwater\b|\briolering\b|\bwateroverlast\b'
    r'|\bwaterschade\b|\bdijk\b|\bkade\b|\bpeilbesluit\b|\bwatergang\b'
    r'|\b[aáàâã]gua\b|\bfornecimento\b|\bsaneamento\b'
    r'|\bcaesb\b|\bsabesp\b|\bcasan\b|\bcaema\b|\bcagece\b'
    r'|\beau\b|\bhydraulic\b|\baquifer\b|\birrigat\b|\bwetland\b'
    r'|\bdrinkbaar\b|\bwaterkering\b', re.I)

REQUIRED = ('governance_cat', 'gov_matched_rule', 'gov_matched_span')


def load(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit(f'{path} is empty.')
    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        raise SystemExit(
            f'{path} is missing {missing}.\n'
            f'Re-run the coding engine to produce them:\n'
            f'  INPUT_CSV=<merged csv> python utils/jurimetric_coding.py')
    return rows


def text_of(row):
    return ' '.join(str(row.get(k, '') or '') for k in ('title', 'summary', 'ementa'))


def build(rows, per_category, seed):
    rnd = random.Random(seed)
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r.get('governance_cat', '') or '(blank)'].append(r)

    rule_counts = Counter(r.get('gov_matched_rule', '') for r in rows)

    sample = []
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        pool = by_cat[cat]
        # Spread the sample across the distinct rules inside a category, so a
        # reviewer sees each decision path rather than 25 hits of one pattern.
        by_rule = defaultdict(list)
        for r in pool:
            by_rule[r.get('gov_matched_rule', '')].append(r)
        picked, rules = [], sorted(by_rule, key=lambda k: -len(by_rule[k]))
        i = 0
        while len(picked) < min(per_category, len(pool)) and rules:
            rule = rules[i % len(rules)]
            bucket = by_rule[rule]
            if bucket:
                picked.append(bucket.pop(rnd.randrange(len(bucket))))
            else:
                rules.remove(rule)
                i -= 1
            i += 1
        sample.extend(picked)
    return by_cat, rule_counts, sample


def compound_diagnostic(rows):
    nwr = [r for r in rows
           if (r.get('governance_cat') == 'not_water_related'
               and (r.get('country', '') or '').strip().lower() == 'netherlands')]
    hits = []
    for r in nwr:
        t = text_of(r)
        if NL_COMPOUND_RE.search(t) and not WATER_CORE_RE.search(t):
            hits.append(r)
    terms = Counter()
    for r in hits:
        for m in NL_COMPOUND_RE.finditer(text_of(r)):
            terms[m.group(0).lower()] += 1
    return nwr, hits, terms


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--csv', required=True, help='output of jurimetric_coding.py')
    ap.add_argument('--per-category', type=int, default=20)
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--outdir', default='.')
    a = ap.parse_args()

    rows = load(a.csv)
    outdir = Path(a.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    by_cat, rule_counts, sample = build(rows, a.per_category, a.seed)
    nwr, hits, terms = compound_diagnostic(rows)

    # ── audit_sample.csv ──────────────────────────────────────────────────────
    cols = ['country', 'tribunal', 'case_id', 'date', 'governance_cat',
            'gov_matched_rule', 'gov_matched_span', 'title', 'summary',
            'permalink', 'permalink_kind', 'fulltext_url']
    with open(outdir / 'audit_sample.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for r in sample:
            res = resolve(case_id=r.get('case_id'), country=r.get('country'),
                          tribunal=r.get('tribunal'), url=r.get('url'),
                          title=r.get('title'))
            out = {c: (r.get(c, '') or '') for c in cols}
            out.update({k: res[k] for k in ('permalink', 'permalink_kind', 'fulltext_url')})
            out['summary'] = ' '.join(str(out['summary']).split())[:400]
            w.writerow(out)

    # ── audit_rule_coverage.csv ───────────────────────────────────────────────
    cat_of_rule = {}
    for r in rows:
        cat_of_rule.setdefault(r.get('gov_matched_rule', ''), r.get('governance_cat', ''))
    with open(outdir / 'audit_rule_coverage.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['rule', 'governance_cat', 'n_decisions', 'pct_of_dataset'])
        for rule, n in rule_counts.most_common():
            w.writerow([rule, cat_of_rule.get(rule, ''), n, f'{n/len(rows)*100:.4f}'])

    # ── AUDIT_TRAIL.md ────────────────────────────────────────────────────────
    L = []
    A = L.append
    A('# Coding Audit Trail\n')
    A(f'Generated from `{a.csv}` over **{len(rows):,} decisions**. '
      f'Sample seed `{a.seed}`, up to {a.per_category} decisions per category.\n')
    A('Every decision in this dataset is classified by exactly one rule. This file '
      'names that rule, shows the text it matched, and links to the decision, so the '
      'classification can be checked without re-running the pipeline.\n')
    A('Companion files: `audit_sample.csv` (this sample as data), '
      '`audit_rule_coverage.csv` (every rule and how much it decides).\n')

    A('\n## 1. Category distribution\n')
    A('| Category | n | % | distinct rules |')
    A('|---|---:|---:|---:|')
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        nrules = len({r.get('gov_matched_rule') for r in by_cat[cat]})
        A(f'| `{cat}` | {len(by_cat[cat]):,} | {len(by_cat[cat])/len(rows)*100:.2f}% | {nrules} |')

    A('\n## 2. Rule concentration\n')
    A('If one rule decides a large share of a category, that rule is doing the '
      'analytical work and deserves scrutiny first.\n')
    A('| Rule | Category | n | % of dataset |')
    A('|---|---|---:|---:|')
    for rule, n in rule_counts.most_common(20):
        A(f'| `{rule}` | `{cat_of_rule.get(rule,"")}` | {n:,} | {n/len(rows)*100:.2f}% |')

    A('\n## 3. Evidence sample\n')
    A('The `matched` line is the exact text the rule fired on. Rescue patterns '
      'bridge two terms with `.*?`, so their spans are elided in the middle.\n')
    cur = None
    for r in sample:
        if r.get('governance_cat') != cur:
            cur = r.get('governance_cat')
            A(f'\n### `{cur}`\n')
        res = resolve(case_id=r.get('case_id'), country=r.get('country'),
                      tribunal=r.get('tribunal'), url=r.get('url'), title=r.get('title'))
        span = ' '.join(str(r.get('gov_matched_span', '') or '').split()) or '(no span — gate rule)'
        link = f'[{r.get("case_id","")}]({res["permalink"]})' if res['permalink'] else r.get('case_id', '')
        A(f'- **{link}** · {r.get("country","")} · {r.get("tribunal","")} · {r.get("date","")}')
        A(f'  - rule: `{r.get("gov_matched_rule","")}`')
        A(f'  - matched: `{span}`')

    A('\n## 4. Diagnostic: Dutch compounds the water gate cannot see\n')
    A('`_WATER_CORE_RE` decides, before any category is considered, whether a '
      'decision is a water case at all. Its terms carry `\\b` word boundaries. Dutch '
      'compounds nouns without spaces, so `\\bwater\\b` does not match `waterwet` and '
      '`\\bgrondwater\\b` does not match `grondwateronttrekking`.\n')
    pct = (len(hits) / len(nwr) * 100) if nwr else 0.0
    A(f'- Netherlands decisions classified `not_water_related`: **{len(nwr):,}**')
    A(f'- of those, containing a water compound the gate cannot match: '
      f'**{len(hits):,}** ({pct:.2f}%)\n')
    if terms:
        A('| Compound | occurrences in affected decisions |')
        A('|---|---:|')
        for t, n in terms.most_common(15):
            A(f'| `{t}` | {n:,} |')
    A('\n**No label was changed by this script.** Fixing the gate would reclassify '
      'these decisions and invalidate the deposited v0.3.0, the kappa results and '
      'the supervisor report. Whether to re-run is a research decision.\n')
    A('Corroboration: in `validation/second_coder_sample_raw.csv`, 65 of the 100 '
      '`NL_broad_water` decisions carry such a compound and the human coder labelled '
      '61 of them WATER, which is the mechanism behind the 0.3579 precision recorded '
      'for that stratum in `validation/precision_recall_results.json`.\n')

    (outdir / 'AUDIT_TRAIL.md').write_text('\n'.join(L), encoding='utf-8')

    print(f'Wrote {outdir/"AUDIT_TRAIL.md"}')
    print(f'Wrote {outdir/"audit_sample.csv"}  ({len(sample):,} decisions)')
    print(f'Wrote {outdir/"audit_rule_coverage.csv"}  ({len(rule_counts):,} rules)')
    print(f'\nDutch compound diagnostic: {len(hits):,} of {len(nwr):,} NL '
          f'not_water_related decisions ({pct:.2f}%) carry an unseeable compound.')


if __name__ == '__main__':
    sys.exit(main())
