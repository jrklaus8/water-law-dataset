"""2026-10-14, open item A26 (PI instruction, reviewer CK): record the author's confirmation on the SWiM core studies that pass the narrow scope and outcome check, and flag the ones that do not.

The instruction was to confirm the remaining unconfirmed SWiM core studies (inclusion decision and two-column direction coding) unless any has a scope or outcome red flag in its extraction row. The AI read each of the 30 rows against the author's
narrow reading of criterion 2 (a legal or administrative access rule or mechanism, not project delivery, participation, attitudes or unanalysed macro-governance) and against criterion 4 (a household or community access outcome), using the same
categories the author used in the A24 recheck (Group 3: community management, participation, NGO or partnership, or programme delivery; Groups 4 and 5: macro-governance, institutional context). 20 pass and are confirmed here; 10 carry a red
flag and are NOT confirmed: they go to 02_screening/full_text/A28_SWIM_FLAGGED_CK_SHEET_2026-10-14.csv for the author's ruling (include = keep, exclude + code = reverse, applied with apply_a16_adjudications.py).
S1140 and S1136 pass by the author's own A26 ruling (kept in their families). Nine other core studies were already human-verified (S001-S200 confirmations or CK rulings) and are untouched, and their direction coding stays unchecked.

What it writes: (1) 05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv (the status of every one of the 30, which the verification-table builder merges into its ck_* columns); (2) a dated note on each full-text row ('A26 ruling 2026-10-14 by CK: confirms ...' for the 20,
'A26 scope check (AI) ...: flagged, not confirmed' for the 10) and reviewer_2 = 'CK' on the confirmed rows whose reviewer_2 is blank (S1062 keeps its Codex second-model label and the confirmation is in the note, as for the A6 tier-1 rows);
decision, code and conflict fields are untouched; (3) the A28 sheet (csv and md). Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf

FT = '02_screening/full_text/full_text_screening_database.csv'
CHK = '05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv'
SHEET = '02_screening/full_text/A28_SWIM_FLAGGED_CK_SHEET_2026-10-14'
OK_MARK = 'A26 ruling 2026-10-14 by CK'
FLAG_MARK = 'A26 scope check (AI) 2026-10-14'

CONFIRM = {   # study: why it passes
 'S404': 'exposure is membership of a statutory water-resource users association (a legal institution under the Water Act); outcome is a household water-poverty index',
 'S765': 'exposure is legal land title under a titling programme (tenure and documentation rule); outcome is use of an improved water source',
 'S780': 'exposure is the legal status of an autonomous county under administrative law; outcome is drinking-water project beneficiaries at county level (a reach measure; null result, noted)',
 'S882': 'exposure is a formal metered connection that requires a connection fee; outcomes are household water-security measures',
 'S930': 'exposure is the legal recognition of customary-law governance (the 1995 Oaxaca reform); outcome is sewerage access',
 'S1122': 'exposure is legal zoning and tenure status; outcome is the time to first piped-water access',
 'S1140': 'kept in Family B by the author (A26): application-process outcome, which the protocol lists',
 'S470': 'exposure is a regulator\'s enforcement norm on an income-eligibility social tariff; outcome is social-tariff implementation',
 'S471': 'exposure is the form of local government that owns the utility; outcome is the water bill; the primary estimate is kept in the main count by the author (A26)',
 'S526': 'exposure is utility ownership and the rate-setting regime; outcome is price progressivity',
 'S539': 'exposure is utility ownership and rate regulation; outcome is the household bill and the lowest-quintile burden',
 'S593': 'exposure is the legal administrative district class and fiscal autonomy; outcome is the equity of unit price (several outcomes are utility performance measures, noted)',
 'S631': 'exposure is the legal creation of new local governments; outcome is household protected water and sanitation access',
 'S749': 'exposure is private ownership and the regulatory regime; outcome is the water tariff',
 'S879': 'exposure is enforcement of disconnection for nonpayment (a randomised contract-enforcement rule); outcomes are payment compliance and water access; kept as Mixed by the author (A26)',
 'S1032': 'exposure is use of an administrative redress channel (municipal corporation or NGO); outcome is household water complaints',
 'S1038': 'exposure is state versus local economic regulation of the utility; outcome is welfare loss in the bill; exposure and comparator corrected by the author\'s A26 ruling',
 'S1062': 'exposure is the O&M cost-recovery policy; outcome is the change in water-supply coverage',
 'S1136': 'kept in Family C by the author (A26): distribution of public sanitation infrastructure under political capture of a mandated local-government function',
 'S1162': 'exposure is the legal administrative category of the urban local government; outcome is growth in household water coverage',
}
FLAG = {      # study: (red flag, the AI's pointer for the author)
 'S920': ('the exposure is a community-based water-user-association management model for small systems against municipal management: community management and programme delivery, with no access rule tested (the A24 Group 3 pattern)', 'E03'),
 'S1020': ('the exposure is a government watershed-development programme (programme delivery); the outcome is domestic water-collection time', 'E03'),
 'S1042': ('the exposure is establishing a community-based organisation and town-hall participation: participation, with no access rule tested (A24 Group 3)', 'E03'),
 'S1057': ('the exposure is household participation in the design of demand-responsive programmes: participation and programme delivery (A24 Group 3)', 'E03'),
 'S294': ('the exposure is a community-driven WASH intervention with committee training (programme delivery) and the effect row\'s outcomes are diarrhoea, child growth and an institutions index, not access; S366 reports the same trial, so a ruling should cover both', 'E03 (outcome E04)'),
 'S1102': ('the exposure is household capital-cost contribution and meeting attendance in community-managed projects: participation and programme delivery (a cost-sharing rule could be argued)', 'E03, or keep as a cost rule'),
 'S1144': ('the exposure is survey-measured trust in NGOs and CBOs, an attitude, and the outcome is use of NGO-supplied services (NGO partnership, A24 Group 3)', 'E03'),
 'S1163': ('the exposure is externally funded or supported WASH programmes in rural schools (programme delivery in schools; the A24 school-WASH reviews were excluded E03)', 'E03'),
 'S947': ('the exposure is the national World Bank regulation-quality index across 44 countries: macro-governance, as in S348 and S969 (excluded E03, effect rows removed)', 'E03'),
 'S1146': ('the exposure is the regional incidence of utilities-sector corruption (a governance-quality measure, cf. S348) rather than a rule or mechanism of access', 'E03, or keep'),
}
EXPECT_OK = 20
assert len(CONFIRM) == EXPECT_OK and len(FLAG) == 10 and not set(CONFIRM) & set(FLAG)


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:20000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


ed = {r['study_id']: r for r in cf.read('ed')}
es = {r['study_id']: r for r in cf.read('es')}
fam = {s: es[s]['synthesis_family'] for s in list(CONFIRM) + list(FLAG)}
assert all(fam[s] in 'ABC' and fam[s] for s in fam), 'every checked study must still be in a SWiM family'
fields, ft, eol = read(FT)
by = {r['record_id']: r for r in ft}
n_ok = n_flag = n_rev2 = 0
for s in CONFIRM:
    r = by[ed[s]['record_id']]
    assert r['final_decision'] == 'include' and not r['reviewer_2'].startswith('Human-') and OK_MARK not in r['notes'] or OK_MARK in r['notes'], s
    if OK_MARK in r['notes']:
        continue
    assert not any(m in r['notes'] for m in cf.HUMAN_RULING_MARKS), f'{s} already carries a human ruling'
    r['notes'] = (r['notes'].rstrip() + f' | {OK_MARK}: confirms the inclusion (narrow scope and outcome check passed: {CONFIRM[s]}) and the two-column direction coding (raw sign and substantive direction). The effect estimate itself was extracted and checked against the full text by the AI, not by a human.').strip(' |')
    if not r['reviewer_2'].strip():
        r['reviewer_2'] = 'CK'; n_rev2 += 1
    n_ok += 1
for s, (why, ptr) in FLAG.items():
    r = by[ed[s]['record_id']]
    assert r['final_decision'] == 'include' and not any(m in r['notes'] for m in cf.HUMAN_RULING_MARKS), s
    if FLAG_MARK in r['notes']:
        continue
    r['notes'] = (r['notes'].rstrip() + f' | {FLAG_MARK}: flagged, NOT confirmed (open item A28): {why}.').strip(' |')
    n_flag += 1
write(FT, fields, ft, eol)
# the status file the verification-table builder merges
rows = []
for s in sorted(list(CONFIRM) + list(FLAG), key=lambda x: int(x[1:])):
    ok = s in CONFIRM
    rows.append({'study_id': s, 'family': fam[s], 'scope_outcome_check': 'passed' if ok else 'flagged', 'check_note': CONFIRM[s] if ok else FLAG[s][0],
                 'ck_raw_sign_agrees (Y/N)': 'Y' if ok else '', 'ck_substantive_direction_agrees (Y/N)': 'Y' if ok else '', 'ck_comment': '' if ok else 'not confirmed: awaits the author (A28)'})
with open(CHK, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
# the A28 sheet
cols = ['record_id', 'study_id', 'citation', 'ai_decision', 'researcher_decision (include/exclude)', 'researcher_exclusion_code (E01-E12)', 'researcher_comment', 'family', 'exposure', 'outcome', 'red_flag', 'ai_pointer_not_a_decision']
sheet = []
for s, (why, ptr) in FLAG.items():
    e = es[s]
    sheet.append({'record_id': ed[s]['record_id'], 'study_id': s, 'citation': ed[s]['citation'][:200], 'ai_decision': 'include', 'researcher_decision (include/exclude)': '', 'researcher_exclusion_code (E01-E12)': '', 'researcher_comment': '',
                  'family': fam[s], 'exposure': e['exposure_definition'][:260], 'outcome': e['effect_measure'][:200], 'red_flag': why, 'ai_pointer_not_a_decision': ptr})
sheet.sort(key=lambda r: int(r['study_id'][1:]))
if not os.path.exists(SHEET + '.csv') or not any(r['researcher_decision (include/exclude)'].strip() for r in csv.DictReader(open(SHEET + '.csv', encoding='utf-8'))):
    with open(SHEET + '.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator='\n'); w.writeheader(); w.writerows(sheet)
    L = ['# A28: ten SWiM core studies the AI could not confirm on the narrow scope and outcome check (2026-10-14)', '',
         '*Generated by `code/provenance/audit_and_repair/apply_a26_swim_core_checks_2026-10-14.py`. These are the ten of the 30 unconfirmed SWiM core studies whose extraction rows show a red flag against the narrow reading of criterion 2 (a legal or administrative access rule or mechanism) '
         'or against criterion 4 (a household access outcome). The AI\'s pointers are not decisions. Fill `researcher_decision` (include = keep, exclude + code = reverse) in a copy of the CSV and apply it with `code/screening/apply_a16_adjudications.py`; a reversal needs its effect row archived first '
         '(`apply_a26_effect_row_rulings_2026-10-14.py` is the pattern) and changes the family counts.*', '',
         '| Study | Family | Red flag | AI pointer |', '|---|---|---|---|']
    for r in sheet:
        L.append(f"| {r['study_id']} | {r['family']} | {r['red_flag']} | {r['ai_pointer_not_a_decision']} |")
    open(SHEET + '.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f'confirmed {n_ok} ({n_rev2} with reviewer_2 set to CK), flagged {n_flag}; wrote {CHK} and {SHEET}.csv/.md')
