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
          'claude_triage (N/B/X)', 'claude_triage_note', 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment']

# Claude's triage (2026-10-04) from each record's title and the models' own design/exposure/outcome summaries; the 15 priority-1 records first triaged N were then checked against their abstracts (notes say 'abstract checked'), and five of them (R2DBFA78BFB76, RB8541E7A11B9, RF104A3C9A7FE, RF8BD93786D82 full text; R4D7CD4E75E33 abstract and introduction) were read in Drive (notes say 'full text read' or 'abstract and introduction read'). A third AI opinion, of the same model family
# as the original screener, to show how much of the disagreement turns on the scope reading. N = the exposure is a rule-type mechanism of the kind the codebook flags (eligibility, documents,
# tenure, fees/tariffs, ownership, enforcement, disconnection, administrative rules or assistance) and the outcome is service access: would pass the narrow and the literal reading.
# B = a general governance factor (participation, coordination, fragmentation, project or fiscal management) with an access outcome: passes the literal reading only. X = fails both readings
# (outcome is not household/community water or sanitation service access, or the exposure is not institutional).
TRIAGE = {
    'R089ED6BEB7BE': ('B', 'abstract checked: a short descriptive agency report on coverage targets and budgets; the tariff is named as a constraint, not analysed'),
    'R08D3F4577102': ('X', 'outcome is professionals ranking hypothetical benefits of mobile payment, not measured access'),
    'R2DBFA78BFB76': ('N', 'full text read (Drive): comparative case study (document analysis, two six-month field visits, interviews) of how utilities extend water and sanitation networks into unplanned settlements in Lima and Delhi; documentation, tenure and regulatory arrangements are the exposure. Passes the narrow reading; the water case is Lima, Delhi is electricity'),
    'R3974945F7707': ('B', 'project participation and needs assessment; service availability outcome'),
    'R3F83B65D41C0': ('B', 'abstract checked: a promotion programme (trigger meetings, follow-up visits, training) and toilet uptake, n = 538; behaviour-change assistance rather than an access rule'),
    'R4FFEE7FE13E6': ('X', 'land-linked groundwater rights, but access is mostly agricultural (exclusion 7, water-resource study)'),
    'R6103D8CFE42F': ('B', 'abstract checked: descriptive survey of 420 prison inmates (crowding, toilet waiting times, hygiene); custody conditions rather than an access rule'),
    'R7E506F37F7B8': ('X', 'exposure is a dam-failure disaster; zoning appears only as a stratifier'),
    'R96A74867D7C2': ('B', 'national urban policy and legislation for informal settlements, cross-country descriptive'),
    'RAAB22A572D27': ('X', 'exposure is religiosity and social norms, not an institutional factor'),
    'RAD91FA5DFF79': ('B', 'slum zone and income with service-delivery conditions; institutional factor weak'),
    'RB8541E7A11B9': ('B', "full text read (Drive): three qualitative case studies of non-state actors and law enforcement (National Green Tribunal petitions, manual-scavenging prohibition, 'legal exceptionalism'); the exposure is legal, but the outcomes are untreated wastewater and treatment capacity, not access, so criterion 1/4 are borderline (was N on the abstract)"),
    'RB9A117B7E3E9': ('B', 'municipal finance and decentralisation (74th Amendment); coverage outcome'),
    'RBFBE0C8DD5C3': ('B', 'deficient public provision and pump operating hours; institutional factor weak'),
    'RD9AA2E70843A': ('B', 'project governance and coordination with some cost-recovery rules'),
    'RE0841B3F072D': ('X', 'groundwater purchase agreement; outcomes are farmers and resource depletion'),
    'RF104A3C9A7FE': ('B', 'full text read (Drive): pupil survey, observation and three administrator interviews in three rural schools; administrative rules (locked toilet, key access) appear as findings but the design is an infrastructure-condition survey, so criterion 2 is borderline (was N on the abstract)'),
    'RF8BD93786D82': ('B', 'full text read (Drive): choice experiment, 344 households in Nima, Accra; provider (AMA v GWCL) and connection fee are attributes, but the outcome is stated willingness to pay, not observed access, so criterion 4 is borderline (was N on the abstract)'),
    'RFE07661F24F1': ('B', 'state-civil society partnerships under decentralisation'),
    'R72919F1AC937': ('B', 'abstract checked: national tubewell census and household survey arguing for comprehensive well testing; information policy rather than an access rule'),
    'RC0409B5F0BE0': ('B', 'fragmented multilevel governance, rationing and a public-private partnership'),
    'R03DD1BAD1AD0': ('X', 'outcome is bottled-water purchase driven by trust, not access'),
    'R4D7CD4E75E33': ('B', 'abstract and introduction read (Drive): governance approach (municipal, private, community) is the exposure, but the outcome is the stated rental value of a connection, a valuation rather than observed access, so criterion 4 is borderline, as for RF8BD93786D82 (was N on the abstract snippet)'),
    'RBCDE0E7C6962': ('B', 'NGO equity-and-inclusion approach (participation, design, some tariff reform)'),
    'RDAD34E024169': ('X', 'abstract checked: ECLAC policy analysis of tariff self-financing from cost information; no empirical access data, so the original E05 looks right'),
    'R09C9177378D2': ('B', 'drought-management institutions and programmes; access outcome'),
    'R69F53378C8F2': ('N', 'abstract checked: 200-city panel 1998-2007 of private-sector participation and utility outcomes including domestic water users (ownership, Family C type). The original exclusion cites the access estimate being insignificant; non-significance is not an exclusion criterion'),
    'RA10042C12DA6': ('B', "abstract checked: master's thesis on desalination costs and residents' willingness to pay for 24-hour piped water; service arrangement, no access rule tested"),
    'RB955BA567B95': ('X', 'abstract checked: optimisation model of technology mixes and prepaid meters for a Kampala project; projections, not empirical access outcomes'),
    'RDC5BD0E41BEE': ('N', 'abstract checked: state economic regulation and household water-bill burden in the Czech Republic (affordability)'),
    'RDEA162168676': ('B', 'self-supply versus piped service costs; the regulatory element (absent permitting) is thin'),
    'R21CAA5C1809C': ('X', 'duplicate of S102 (same article, DOI 10.15847/cct.36875); the blind reviewers could not see the other record, so the original E08 stands'),
    'R2ABF896EA8EB': ('B', 'enabling environment for participation; originally E12, may be conceptual'),
    'R0A1C9E556D77': ('B', 'water concessions and private appropriation behind conflicts; access restrictions partly domestic'),
    'R0B462A3EF2D7': ('X', 'utility management tool; outcome is unbilled water'),
    'R16AB75AC4334': ('X', 'reservoir-release rules; outcomes are habitat, flows and floods'),
    'R3ADAE9AD6CD1': ('X', 'water-resource user associations; outcome is association functioning'),
    'R4D3FA2134902': ('X', 'transboundary participation; outcome is irrigation access'),
    'R79A39D631DB8': ('X', 'metering and charging, but the outcome is conservation behaviour'),
    'R8A95684C4716': ('X', 'outcome is protest participation'),
    'R9477DF8E814D': ('X', 'agrarian commons and irrigation'),
    'R9DF6B20973C6': ('X', 'groundwater rules for irrigated agriculture'),
    'RB5516429E2DC': ('X', 'exposure is household poverty'),
    'RBA18C893F671': ('X', 'outcome is willingness to drink recycled water'),
    'RD1D7FB8C4689': ('X', 'outcome is children\'s participation in planning'),
    'RD6B9F237B30D': ('X', 'irrigation water rights'),
    'RDCB899855EE9': ('X', 'prepaid meters and disconnection, but the outcome is citizenship discourse'),
    'RFA18A400F778': ('X', 'hardship-support partnership; outcome is network structure, not access'),
    'R00E98F4E387F': ('X', 'outcome is the effectiveness of participation, not access'),
    'R457A96841C7E': ('B', 'decentralised wastewater arrangements; descriptive service claims'),
    'RCFA60F99F5A8': ('X', 'seismic engineering programme; modelled post-earthquake service'),
    # priority 4: the AI included, the models would exclude (X here = the triage agrees the record fails the criteria)
    'R235E42D59F53': ('X', 'S1117: policy note scanning COVID-19 responses with no methods, search or selection described; criterion 3 doubtful (Codex E05; Gemini include)'),
    'R4BCCFE408D51': ('X', 'S1053: participatory irrigation management for 115 farming households; irrigation, not household water or sanitation service (exclusion 7)'),
    'R64A7E6073EF0': ('X', 'S397: outcome is whether a municipality formulated a sanitation policy, not access (the same outcome problem as S312 and S435); borderline'),
    'R68F11D7E3F64': ('X', 'S340: desk-based literature review with no search or selection method; criterion 3 doubtful (already on the reclassification eligibility list)'),
    'R4D3518D8ACB3': ('B', 'licensing and permissions around a bottling plant; community exclusion from groundwater partly domestic'),
}


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


def _wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    ph = k / n; d = 1 + z * z / n; c = ph + z * z / (2 * n); h = z * ((ph * (1 - ph) / n + z * z / (4 * n * n)) ** 0.5)
    return (c - h) / d, (c + h) / d


def projection(cx, gm, queue):
    """Per exclusion code: excludes in the log, tier-2 records the models re-read, how many they would include, and the implied count if the rate held for the whole code.
    Tier 2 is a seeded random sample stratified by code (E08 and E10 not sampled), so a per-code projection is legitimate as arithmetic; it inherits every weakness of the model verdicts."""
    by_code = cf.compute()['exclusion_by_code']
    rows = []
    for code in sorted(by_code):
        if code in ('E08', 'E10'):
            continue
        rev = [q for q in queue.values() if q['priority_tier'] == '2' and q['ai_exclusion_code'] == code and (q['record_id'] in cx or q['record_id'] in gm)]
        prim = sum(1 for q in rev if q['reviewer_2_decision (include/exclude/cannot_tell)'] == 'include')
        both = sum(1 for q in rev if cx.get(q['record_id'], {}).get('decision') == 'include' and gm.get(q['record_id'], {}).get('decision') == 'include')
        nN = sum(1 for q in rev if TRIAGE.get(q['record_id'], ('',))[0] == 'N')
        nNB = sum(1 for q in rev if TRIAGE.get(q['record_id'], ('',))[0] in ('N', 'B'))
        lo, hi = _wilson(prim, len(rev))
        N = by_code[code]
        rows.append(dict(code=code, in_log=N, reread=len(rev), primary_include=prim, both_include=both,
                         projected=round(N * prim / len(rev)) if rev else None, triage_N=nN, triage_NB=nNB, proj_narrow=round(N * nN / len(rev)) if rev else None, proj_literal=round(N * nNB / len(rev)) if rev else None, lo=round(N * lo) if rev else None, hi=round(N * hi) if rev else None))
    return rows


def includes_side():
    """(tier-3 includes re-read, judged exclude by the primary model, implied count among unconfirmed includes, Wilson low, Wilson high)."""
    cx, gm = _load('results'), _load('results_gemini')
    queue = {r['record_id']: r for r in csv.DictReader(open(R2 / 'full_text_reviewer_2_FILLED_2026-10-03.csv', encoding='utf-8', newline=''))}
    t3 = [q for q in queue.values() if q['priority_tier'] == '3' and (q['record_id'] in cx or q['record_id'] in gm)]
    k3 = sum(1 for q in t3 if q['reviewer_2_decision (include/exclude/cannot_tell)'] == 'exclude')
    F = cf.compute(); pool = F['full_text_include'] - F['reviewer_2_confirmed_includes']
    lo, hi = _wilson(k3, len(t3))
    return len(t3), k3, round(pool * k3 / len(t3)), round(pool * lo), round(pool * hi)


def implied_total():
    """(model rate, narrow-reading triage, literal-reading triage) implied includes summed over estimable codes (see projection()); a sense of scale only."""
    cx, gm = _load('results'), _load('results_gemini')
    queue = {r['record_id']: r for r in csv.DictReader(open(R2 / 'full_text_reviewer_2_FILLED_2026-10-03.csv', encoding='utf-8', newline=''))}
    est = [p for p in projection(cx, gm, queue) if p['projected'] is not None]
    return sum(p['projected'] for p in est), sum(p['proj_narrow'] for p in est), sum(p['proj_literal'] for p in est)


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
                         **{'claude_triage (N/B/X)': TRIAGE.get(rid, ('', ''))[0], 'claude_triage_note': TRIAGE.get(rid, ('', ''))[1], 'researcher_decision (include/exclude)': '', 'researcher_exclusion_code (E01-E12)': '', 'researcher_comment': ''}))
    rows.sort(key=lambda r: (r['priority'], r['ai_code'], r['record_id']))
    n = {p: sum(1 for r in rows if r['priority'] == p) for p in (1, 2, 3, 4)}
    codes = {}
    for r in rows:
        if r['priority'] < 4:
            codes[r['ai_code']] = codes.get(r['ai_code'], 0) + 1
    L = ["# A16 adjudication sheet — AI excludes that the blind reviewers would include (2026-10-04)", "",
         "*Generated by `code/analysis/build_a16_adjudication_sheet.py` from `_reviewer2_codex/`. Read-only; no screening data changed; nothing here is a decision (open item A16 in `00_admin/DECISIONS_AND_OPEN_ITEMS.md`). "
         "The models' verdicts are AI opinions and may be too permissive: judge each paper against `INCLUSION_EXCLUSION.md` yourself. Fill the last three columns of a copy of the CSV; `python3 code/screening/apply_a16_adjudications.py <copy> --reviewer <initials>` then shows what would change (dry run) and `--apply` writes it — confirmations take effect at once, reversals are queued for a dated inclusion/exclusion script so the database stays consistent.*", "",
         f"**{len(rows)} records** where Codex and/or Gemini (blind to the original decision) disagreed with the original AI's include/exclude call: "
         f"priority 1 = {n[1]}, priority 2 = {n[2]}, priority 3 = {n[3]} (AI excluded, models include); priority 4 = {n[4]} (AI included, models exclude).", "",
         "AI excludes by original code among priority 1-3: " + ', '.join(f"{k} {CODES.get(k, '')} {v}" for k, v in sorted(codes.items())) + ".", "",
         "**Why they disagree may be a scope question, not only an error rate.** `INCLUSION_EXCLUSION.md` criterion 2 asks for \"a legal, administrative, institutional, regulatory or governance factor\" and states that qualitative socio-legal studies must not be dropped; the blind models read that literally. "
         "The original AI's E01 'wrong topic' exclusions (see its reasoning column) appear to apply a narrower reading closer to the project's core question: rules about eligibility, documents, cost, discretion and enforcement. "
         "Decide which reading governs before judging individual rows. If the protocol's literal breadth governs, many E01 excludes would flip and the corpus is larger than reported; if the narrower reading governs, `INCLUSION_EXCLUSION.md` should be tightened to say so and the blind check re-run with the narrow wording (this is the AI's reading of the pattern, not a finding).", "",
         "Priority 1 = both models include and every criterion is 'yes' in both; 2 = both include but some criterion is not 'yes'; 3 = only one model includes. Start with priority 1: if the researcher "
         "rejects most of those, the independent models are probably reading the criteria too loosely and the original exclusions can stand; if the researcher accepts most, widen the tier-2 sample "
         "(A16 option b) before relying on the 1,117-exclude log.", "",
         "## What the sample implies, if the models were right (arithmetic, not a finding)", "",
         "Tier 2 is a seeded random sample of the AI's full-text excludes, stratified by exclusion code (E08 duplicates and E10 inaccessible texts not sampled); the models re-read only those whose PDF was available. "
         "Scaling each code's rate to the whole exclusion log gives the order of magnitude at stake. The 95% ranges are Wilson intervals per code; they ignore the PDF-availability selection and the models' own error, so treat them as a sense of scale only.", "",
         "The last two columns use Claude's triage of the same records (column `claude_triage` in the CSV; from titles and the models' summaries, not from the papers): *narrow* counts only records whose exposure is a rule-type mechanism of the kind the codebook flags (N); *literal* adds general governance factors (N + B). Records the triage judges to fail either reading (X: outcome not service access, or exposure not institutional) count under neither.", "",
         "| Code | Excludes in log | Re-read by models | Primary model: include | Both models: include | Implied if the model rate held (95% range) | Implied, narrow reading (triage N) | Implied, literal reading (triage N + B) |", "|---|---|---|---|---|---|---|---|"]
    proj = projection(cx, gm, queue)
    t3 = [q for q in queue.values() if q['priority_tier'] == '3' and (q['record_id'] in cx or q['record_id'] in gm)]
    k3 = sum(1 for q in t3 if q['reviewer_2_decision (include/exclude/cannot_tell)'] == 'exclude')
    k3x = sum(1 for q in t3 if q['reviewer_2_decision (include/exclude/cannot_tell)'] == 'exclude' and TRIAGE.get(q['record_id'], ('',))[0] == 'X')
    pool3 = cf.compute()['full_text_include'] - cf.compute()['reviewer_2_confirmed_includes']
    lo3, hi3 = _wilson(k3, len(t3))
    inc_text = (f"Tier 3 is a seeded random sample of includes beyond the {cf.compute()['reviewer_2_confirmed_includes']} human-confirmed ones; the models re-read {len(t3)} and the primary model would exclude {k3}, "
                f"and Claude's triage agrees on {k3x} of them (three of the four priority-4 rows below; the fourth, S397, comes from tier 1). Scaled to the {pool3:,} unconfirmed includes, that is about {round(pool3 * k3 / len(t3)) if t3 else 0} "
                f"(Wilson 95% range {round(pool3 * lo3)}-{round(pool3 * hi3)}) studies that might not meet the criteria — arithmetic on {len(t3)} records, so the range is wide. It bears on precision, not on completeness, "
                "and is the strongest reason to finish the human second-screening of includes (brief, part 2).")
    for p in proj:
        L.append(f"| {p['code']} {CODES.get(p['code'], '')} | {p['in_log']} | {p['reread']} | {p['primary_include']} | {p['both_include']} | "
                 + (f"{p['projected']} ({p['lo']}-{p['hi']}) | {p['proj_narrow']} ({p['triage_N']}) | {p['proj_literal']} ({p['triage_NB']})" if p['projected'] is not None else 'not estimable (none re-read) | - | -') + " |")
    est = [p for p in proj if p['projected'] is not None]
    L += [f"| **Sum of estimable codes** | {sum(p['in_log'] for p in est)} | {sum(p['reread'] for p in est)} | {sum(p['primary_include'] for p in est)} | {sum(p['both_include'] for p in est)} | **{sum(p['projected'] for p in est)}** | **{sum(p['proj_narrow'] for p in est)}** | **{sum(p['proj_literal'] for p in est)}** |", "",
          "Two things the abstract check of the priority-1 records showed: (1) blind reviewers cannot detect duplicates, so a duplicate excluded as E08 can come back as a disagreement (R21CAA5C1809C is the same article as S102; E08 stands); "
          "(2) one original exclusion (R69F53378C8F2, a 200-city panel on private-sector participation) rests partly on the access estimate being non-significant, which is not an exclusion criterion and would bias the review against null results.", "",
          "Counts in brackets are the re-read records the triage put in each group. The triage is a third AI opinion from the same model family as the original screener, so it may share its blind spots; it is offered to show how much turns on the scope reading, not as a decision.", "",
          f"For scale: the review currently has {cf.compute()['full_text_include']:,} full-text includes. Codes with no re-read record are not estimated. A human reading of priority 1 is what turns this arithmetic into a number the review can report.", "",
          "## The other direction: AI includes the models would exclude", "",
          inc_text, "",
          "## Records", "",
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
