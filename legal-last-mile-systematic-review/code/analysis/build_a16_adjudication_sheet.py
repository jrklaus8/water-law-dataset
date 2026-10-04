#!/usr/bin/env python3
"""Generate 02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.{csv,md}: one row for every full-text record on which the blind non-Claude reviewers (Codex, Gemini; see
_reviewer2_codex/) reached a different include/exclude decision from the original AI, ordered so the researcher can read the most likely mis-excludes first, with blank columns for the
researcher's own decision. READ-ONLY: it changes no screening data, and nothing in it is a decision (open item A16). The models' views are AI opinions, not evidence of eligibility.
Priority 1 = AI excluded, both models include and every criterion is 'yes' in both; 2 = AI excluded, both models include but a criterion is not 'yes'; 3 = AI excluded, only one model includes;
4 = AI included, the models exclude. Run from the project root: python3 code/analysis/build_a16_adjudication_sheet.py"""
import csv, glob, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
R2 = ROOT / '_reviewer2_codex'
OUT_CSV = ROOT / '02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.csv'
OUT_MD = ROOT / '02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md'
CODES = {'E01': 'wrong topic', 'E02': 'wrong population', 'E03': 'wrong exposure', 'E04': 'wrong outcome', 'E05': 'no empirical evidence', 'E06': 'engineering only', 'E07': 'wrong service',
         'E08': 'duplicate', 'E09': 'insufficient information', 'E10': 'inaccessible full text', 'E11': 'wrong jurisdiction / context', 'E12': 'wrong study design'}
FIELDS = ['priority', 'direction', 'record_id', 'study_id', 'year', 'authors', 'title', 'doi', 'url', 'ai_decision', 'ai_code', 'ai_code_meaning', 'ai_reasoning',
          'codex_decision', 'codex_code', 'codex_confidence', 'codex_criteria_not_yes', 'codex_design', 'codex_exposure', 'codex_outcome', 'codex_rationale', 'gemini_decision', 'gemini_code', 'gemini_confidence', 'gemini_criteria_not_yes', 'gemini_exposure', 'gemini_outcome', 'gemini_rationale',
          'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment']


def _load(sub):
    out = {}
    for f in sorted(glob.glob(str(R2 / sub / 'R*.json'))):
        if 'phase2' in f:
            continue
        j = json.load(open(f, encoding='utf-8'))
        if j.get('parsed'):
            out[j['record_id']] = j['parsed']
    return out


def _not_yes(p):
    return '; '.join(f'{k}={v}' for k, v in sorted((p.get('criteria') or {}).items()) if v != 'yes')


def build():
    """Return (csv rows as dicts, markdown text)."""
    cx, gm = _load('results'), _load('results_gemini')
    queue = {r['record_id']: r for r in csv.DictReader(open(R2 / 'full_text_reviewer_2_FILLED_2026-10-03.csv', encoding='utf-8', newline=''))}
    rows = []
    for rid, q in queue.items():
        ai = q['ai_decision']; c = cx.get(rid); g = gm.get(rid)
        votes = [p['decision'] for p in (c, g) if p]
        if not votes or all(v == ai for v in votes):
            continue                                           # no model disagreed with the original AI's include/exclude decision
        if ai == 'exclude':
            both = c and g and c['decision'] == 'include' and g['decision'] == 'include'
            clean = both and not _not_yes(c) and not _not_yes(g)
            pr, direction = (1 if clean else 2 if both else 3), 'AI excluded; model(s) include'
        else:
            pr, direction = 4, 'AI included; model(s) exclude'
        def part(p, k): return p.get(k, '') if p else ''
        rows.append(dict(priority=pr, direction=direction, record_id=rid, study_id=q['study_id'], year=q['year'], authors=q['authors'][:80], title=q['title'], doi=q['doi'], url=q['url'], ai_decision=ai,
                         ai_code=q['ai_exclusion_code'], ai_code_meaning=CODES.get(q['ai_exclusion_code'], ''), ai_reasoning=q['ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT'][:500],
                         codex_decision=part(c, 'decision'), codex_code=part(c, 'exclusion_code'), codex_confidence=part(c, 'confidence'), codex_criteria_not_yes=_not_yes(c) if c else '', codex_design=part(c, 'study_design')[:200], codex_exposure=part(c, 'exposure')[:300], codex_outcome=part(c, 'outcome')[:300], codex_rationale=part(c, 'rationale')[:600],
                         gemini_decision=part(g, 'decision'), gemini_code=part(g, 'exclusion_code'), gemini_confidence=part(g, 'confidence'), gemini_criteria_not_yes=_not_yes(g) if g else '', gemini_exposure=part(g, 'exposure')[:300], gemini_outcome=part(g, 'outcome')[:300], gemini_rationale=part(g, 'rationale')[:600],
                         **{'researcher_decision (include/exclude)': '', 'researcher_exclusion_code (E01-E12)': '', 'researcher_comment': ''}))
    rows.sort(key=lambda r: (r['priority'], r['ai_code'], r['record_id']))
    n = {p: sum(1 for r in rows if r['priority'] == p) for p in (1, 2, 3, 4)}
    codes = {}
    for r in rows:
        if r['priority'] < 4:
            codes[r['ai_code']] = codes.get(r['ai_code'], 0) + 1
    L = ["# A16 adjudication sheet — AI excludes that the blind reviewers would include (2026-10-04)", "",
         "*Generated by `code/analysis/build_a16_adjudication_sheet.py` from `_reviewer2_codex/`. Read-only; no screening data changed; nothing here is a decision (open item A16 in `00_admin/DECISIONS_AND_OPEN_ITEMS.md`). "
         "The models' verdicts are AI opinions and may be too permissive: judge each paper against `INCLUSION_EXCLUSION.md` yourself. Fill the last three columns of the CSV, then send it back.*", "",
         f"**{len(rows)} records** where Codex and/or Gemini (blind to the original decision) disagreed with the original AI's include/exclude call: "
         f"priority 1 = {n[1]}, priority 2 = {n[2]}, priority 3 = {n[3]} (AI excluded, models include); priority 4 = {n[4]} (AI included, models exclude).", "",
         "AI excludes by original code among priority 1-3: " + ', '.join(f"{k} {CODES.get(k, '')} {v}" for k, v in sorted(codes.items())) + ".", "",
         "**Why they disagree may be a scope question, not only an error rate.** `INCLUSION_EXCLUSION.md` criterion 2 asks for \"a legal, administrative, institutional, regulatory or governance factor\" and states that qualitative socio-legal studies must not be dropped; the blind models read that literally. "
         "The original AI's E01 'wrong topic' exclusions (see its reasoning column) appear to apply a narrower reading closer to the project's core question: rules about eligibility, documents, cost, discretion and enforcement. "
         "Decide which reading governs before judging individual rows. If the protocol's literal breadth governs, many E01 excludes would flip and the corpus is larger than reported; if the narrower reading governs, `INCLUSION_EXCLUSION.md` should be tightened to say so and the blind check re-run with the narrow wording (this is the AI's reading of the pattern, not a finding).", "",
         "Priority 1 = both models include and every criterion is 'yes' in both; 2 = both include but some criterion is not 'yes'; 3 = only one model includes. Start with priority 1: if the researcher "
         "rejects most of those, the independent models are probably reading the criteria too loosely and the original exclusions can stand; if the researcher accepts most, widen the tier-2 sample "
         "(A16 option b) before relying on the 1,117-exclude log.", "",
         "| Pri | Record | Title | AI code | Codex | Gemini |", "|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['priority']} | {r['record_id']} | {r['title'][:90]} | {r['ai_code']} {r['ai_code_meaning']} | {r['codex_decision']} ({r['codex_confidence']}) | {r['gemini_decision']} ({r['gemini_confidence']}) |")
    return rows, "\n".join(L) + "\n"


if __name__ == '__main__':
    rows, md = build()
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(md, encoding='utf-8')
    print(f'wrote {OUT_CSV.relative_to(ROOT)} ({len(rows)} rows) and {OUT_MD.name}')
