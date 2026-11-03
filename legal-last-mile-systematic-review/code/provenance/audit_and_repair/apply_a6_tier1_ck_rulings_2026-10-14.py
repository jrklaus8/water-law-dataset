"""2026-10-14 (open item A6, tier 1, first batch): record the PI's rulings under reviewer CK on 16 of the 18 tier-1 rows that carry a blind second-model decision, and flag the other two.

Rows 1-8 (the eight AI excludes) are confirmed with their existing codes. Of rows 9-18 (the ten AI includes), rows 11-15 (S398, S392, S393, S389, S390) are confirmed by the PI; S394, S387 and S396 are confirmed
on the PI's rule that an include whose extracted exposure is a statutory rule, a tariff or a formal regulatory duty is confirmed (S394: the Water Resource Management Act 11 of 2013 not in force and the 1956 Act still
applying, with no regulator established; S387: enforceable minimum standards and fixture-ratio codes in a regulatory-accountability matrix; S396: the universalisation duty of Federal Laws 11.445/2007 and 14.026/2020 set
against intermittent supply). S391 and S395 are community management or operation-and-maintenance studies whose only rule-type flag is `discretion_accommodation`; they are FLAGGED for the PI and NOT changed.

What this writes: a dated note on each of the 16 rows of full_text_screening_database.csv (no decision, code, label or conflict field changes: as for the A16 confirmations, `reviewer_2` keeps the second-model label so
that the second-model counts stay true, and the human ruling is carried by the note), the ck_* columns of A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv, and a FLAG comment on S391 and S395. Idempotent.
The Pass-1 rationales of rows 1, 4 and 6 already exist in exclusion_reason_detail (an earlier sheet showed only the leading citation tag because it cut the text at the first full stop); nothing is backfilled.
Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
FT = '02_screening/full_text/full_text_screening_database.csv'
SHEET = '02_screening/full_text/A6_TIER1_SECOND_MODEL_CK_SHEET_2026-10-14.csv'
MARK = 'A6 tier-1 ruling'
DATE = '2026-10-14'
R = {  # record_id: (decision, code, comment)
    'R0B462A3EF2D7': ('exclude', 'E01', 'Corporate Balanced Scorecard case study, no household access or legal rule. The second-model split (Codex exclude E04, Gemini include) does not change it; reaffirms the A16 ruling of 2026-10-13.'),
    'R21CAA5C1809C': ('exclude', 'E08', 'Duplicate of S102 (R34A26DC79A8B, same DOI 10.15847/cct.36875). Both models read the paper as eligible but were not told of the duplicate; reaffirms the A16 ruling.'),
    'RDEA162168676': ('exclude', 'E06', 'Life-cycle-cost engineering costing exercise; the exposure is water-source type, not a legal or administrative rule. Both models read it as eligible under the plain wording of criterion 2; reaffirms the A16 ruling (narrow reading).'),
    'R057F7388EEF4': ('exclude', 'E05', 'CSIR technical note on the prospective appropriateness of franchising; no primary data and no systematic method (criterion 3).'),
    'R804A6CFFD1D7': ('exclude', 'E05', "Letter to the Editor; advocacy without primary data or method (criterion 3)."),
    'RAA8D967AD545': ('exclude', 'E01', 'Utilities engineering master\'s curriculum paper; not a study of service access (criterion 1).'),
    'RF22EFFAD48CC': ('exclude', 'E05', 'Conceptual literature review without a search or selection method (criterion 3).'),
    'RF8AB3815D963': ('exclude', 'E05', 'Narrative literature study without a systematic method (criterion 3).'),
    'R2B5A92453E91': ('include', '', 'S398: ZEIS land-use zoning rule with a census-tract difference-in-differences on water and sewer access.'),
    'R56D409CF27A6': ('include', '', 'S392: constitutional, national and provincial consumer and user-rights rules and case law, comparative legal-empirical analysis.'),
    'RA0005AC70700': ('include', '', 'S393: Clean India (Swachh Bharat) institutional rules and their implementation, interviews with programme actors.'),
    'RA1109B58A443': ('include', '', 'S389: statutory testing and reporting duties of the Tasmanian Public Health Act 1997 on rural local governments.'),
    'RA7E07382F0E4': ('include', '', 'S390: ERSAR social-tariff recommendation, all 278 Portuguese municipalities.'),
    'R03824D388779': ('include', '', 'S394: statutory framework in transition (Water Resource Management Act 11 of 2013 not in force, Water Act 1956 still applying, no regulator established); confirmed on the exposure test.'),
    'RB334FC53A1A9': ('include', '', 'S387: enforceable minimum standards and fixture-ratio codes in a regulatory-accountability matrix; confirmed on the exposure test.'),
    'RF20B9AADA984': ('include', '', 'S396: universalisation duty of Federal Laws 11.445/2007 and 14.026/2020 set against intermittent supply in nominally connected households; confirmed on the exposure test (the closest of the three to a legal frame rather than a tested rule).'),
}
FLAG = {
    'R0EED09DB6147': 'FLAGGED for CK, decision unchanged: S391 (Salatiga) scores four community-run water units on a Rapfish institutional dimension (legality of management, SOP, job descriptions, reporting). The government criteria (Permendagri, BPPSPAM) are the scoring benchmark, not a rule that varies or governs access; the only rule-type flag is discretion_accommodation. Looks like community management (A24 Group 3).',
    'RC4C6E385D8B9': 'FLAGGED for CK, decision unchanged: S395 (Jambon Village) describes one community-managed system (SPAMDes) with sustainability scores and satisfaction surveys. Government Regulation 122/2015 is the setting; the system has no written procedures and gets no government funding, the tariff is set locally, and the only rule-type flag is discretion_accommodation. Looks like community management or O&M (A24 Group 3).',
}


def rd(p):
    raw = open(p, newline='', encoding='utf-8').read()
    eol = '\r\n' if '\r\n' in raw[:20000] else '\n'
    with open(p, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r), eol


def wr(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


ff, ft, feol = rd(FT)
by = {r['record_id']: r for r in ft}
n = 0
for rid, (dec, code, com) in R.items():
    r = by[rid]
    assert r['final_decision'] == dec and r['exclusion_reason'] == code, (rid, r['final_decision'], r['exclusion_reason'])   # a confirmation: the ruling equals the standing decision
    if MARK in r['notes']:
        continue
    r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"{MARK} {DATE} by CK: confirms {dec}" + (f' ({code})' if code else '') + f'; {com}'
    n += 1
wr(FT, ff, ft, feol)
print(n, 'notes added to the full-text database')

fs, sh, seol = rd(SHEET)
for x in sh:
    rid = x['record_id']
    if rid in R:
        dec, code, com = R[rid]
        x['ck_decision (include/exclude)'], x['ck_exclusion_code (E01-E12)'], x['ck_comment'] = dec, code, com
    elif rid in FLAG:
        x['ck_comment'] = FLAG[rid]
assert sum(1 for x in sh if x['ck_decision (include/exclude)']) == 16
wr(SHEET, fs, sh, seol)
print('sheet filled: 16 rulings, 2 flags')
