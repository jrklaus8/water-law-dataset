#!/usr/bin/env python3
"""Generate 05_analysis/effect_sizes/SWIM_37_SOURCE_VERIFICATION_DOSSIER.md and SWIM_37_SOURCE_PDF_MANIFEST.csv: a reading aid for the author's own verification of the 37 studies in the three SWiM families
(inclusion and scope, exposure and comparator, outcome, estimate, sample size, risk-of-bias rating, direction coding) against the source PDFs.

What it does and does not do. For every study in effect_sizes.csv with a family A, B or C it prints what the database stores, the status of any human verification, and the passages of the PDF that contain the stored
numbers or terms, verbatim, with the PDF page and the table caption. The passages are located by lexical match; the AI does not judge whether they support the stored value. It records NO confirmation of any kind
(no `human_verified`, no `reviewer_2`, no CK): every verification box in the dossier is blank for the author. Hand-picked quotes for the ten studies flagged in A28 come from swim_dossier_curated.py and are checked against the
PDF text on every build (a quote that is not found stops the build).

The PDFs are not in the repository (copyright). Give the directory of `<study_id>.pdf` files with --pdf-dir (or SWIM_PDF_DIR). A study without a PDF still gets its entry, marked as having no source file.
Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_swim_source_dossier.py --pdf-dir DIR
"""
import argparse
import csv
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import source_text_tools as T  # noqa: E402
from swim_dossier_curated import CURATED  # noqa: E402

csv.field_size_limit(sys.maxsize)
ROOT = cf.ROOT
OUT_MD = ROOT / '05_analysis/effect_sizes/SWIM_37_SOURCE_VERIFICATION_DOSSIER.md'
OUT_CSV = ROOT / '05_analysis/effect_sizes/SWIM_37_SOURCE_PDF_MANIFEST.csv'
A28 = ('S920', 'S1020', 'S1042', 'S1057', 'S294', 'S1102', 'S1144', 'S1163', 'S947', 'S1146')

# Where each PDF came from (the author's Google Drive "Processed" folder, read-only downloads of 2026-10-14). None means no PDF was found there.
DRIVE = {
    'S037': ('1BolXITn0UiGV9BAvWf1qL8Ac8-74acJ1', 'S037_Espinoza_2024_paradox-production-surface-water-supply.pdf'),
    'S057': ('13TB9VVike0m2n8jwHX9Kplk4RPI8AGpM', 'S057_Kozole_2023_Impact_of_targeted_subsidies_on_access_to_resilient_sanitation_for_cli.pdf'),
    'S084': ('1gE1-2EuY52gRivTArhRaajUg1aRr9W2Y', 'S084_Lubeck_Schricker_2023_Divided_infrastructure_legal_exclusion_and_water_inequality_in_an_urb.pdf'),
    'S085': ('1OUG3pEvzFUvyEOmC3cKB9umuTeLCGhYN', 'S085_Gaikwad_2026_Getting_on_the_grid_A_field_experiment_on_bottom_up_political_pressur.pdf'),
    'S104': ('1k548crII0SPZT8VagB1qfNmNOw1Vkuo6', 'S104_ThomasPossee_2024_household-neighbourhood-service-provider-risk.pdf'),
    'S142': ('1bX785ptcsbS5fi4irjPba2tGtG6S3mnU', 'S142_Allaire_2024_water-wastewater-infrastructure.pdf'),
    'S174': ('1hVMuZqsRPzyXqBw3Qx1LQaxAL2ykinXQ', 'RF18D44C79805_de_2022.pdf'),
    'S294': ('1stu3MeOYTPEPffQrfqEd7IrepVSxedPK', 'S294_Quattrochi_2025_effects-community-driven-wash-intervention.pdf'),
    'S398': ('1Uh_yV982Yy5SB0BuC2qvrlG0BkVTMygh', 'R2B5A92453E91_dos_2025.pdf'),
    'S404': ('1Iv80KRYPN6vE4qkd-bU5S0BqSuk_9DvY', 'R9B182B30D773.pdf'),
    'S470': ('1-gEJiwruJDqK3YWryGedtc2mmls7E3n1', 'wp2025193.pdf'),
    'S526': ('19s7XKgq37R-Bdfjp7KFMtZ8UgRJq2VP4', 'Policy Studies Journal - 2025 - Switzer - Public enterprise pricing as redistributive policy.pdf'),
    'S593': ('1lJ6LTdbgc-l0aztpY0A0ue1yqS6lAqZb', 'R7A9FA4B1B749__A study on the equity and influencing factors of local water supply services in Korea.pdf'),
    'S631': ('1VZ_w3Xoc-jW33nh1Ko-dIxhsEHAMkXAs', 'R1CA3290F50A5__Does local government proliferation improve public service delivery_ Evidence from Indonesia.pdf'),
    'S749': ('1bP6zoBErgx7C5ryyYYJJw5Fg2vvSHlrY', 'RD4A74FAB9801__Governance structures and their impact on tariff levels of Brazilian water and s.pdf'),
    'S765': ('10eLEeaECPwQeri3AS2W74iZ0GksWbq0F', 'RF611C2722057__Property Rights and Water Access Evidence from Land Titling in Rural Peru.pdf'),
    'S780': ('1OTaXK1yQcOFZ1Y0od-r3N4BnZjkOZu-g', 'RE992755C7ABF__Ethnicity and government provision of drinking water infrastructure in rural Chi.pdf'),
    'S879': ('1YheYJ1naNppJFurK4RjQ_FEeDigpXmcO', 'R4D81D56EA98B__Financing Municipal Water and Sanitation Services.pdf'),
    'S882': ('1vgERrRtQtvuGTCuXdw9tVQpebWpQQ9GW', 'R59329720D787__Examining Relationships between Household Resources and Water Security in an Urb.pdf'),
    'S920': ('1iYEj8wwK6ZAckZ9skOhhFWFdVDocspZd', 'R9502CE771F1E__What Determines Access to Piped Water in Rural Areas Evidence from Small-Scale S.pdf'),
    'S930': ('1TaAyCtu8lCqTrPa6F1fuw7NVQttQRGfV', 'R7DF2A5059A76__Traditional Governance, Citizen Engagement, and Local Public Goods Evidence from.pdf'),
    'S947': ('1HRYYfkms-juJszMQy7UdfsQqwgyjVKxB', 'R7189977C3E95__Linking natural resource dependence and access to water and sanitation in Africa.pdf'),
    'S1020': ('18MkLh9WnApdUbgLbiYzh4UHgEQEsc9o_', 'R21E208560E01__Evaluating Social Impacts of Watershed Development in India.pdf'),
    'S1032': ('1Z6c4rYg7Bx8_npw4zcB9B5ClxA_Us3kz', 'R309188806D95__Exploring the Influence of Participation on Programme Satisfaction Lessons from.pdf'),
    'S1038': ('1vIH4Hed15e6KfshgF9Iv9IMwsqQ99H9h', 'R350FA2E35538__Monopoly Pricing as a Consumer Exaction in the Public Utility Sector Monopoly We.pdf'),
    'S1042': ('1-KYkhtenp-gWkzzHrfNxOE802UVOBEr0', 'R3C1D63DD65AB__Participation and Local Governance Outcomes Evidence from Ukraine.pdf'),
    'S1057': ('1Sbnk2a8GtOYbkVLaROlVa-QTOPwcAQQj', 'R4DBF12B4A327__Institutional determinants of the impact of community-based water services Evide.pdf'),
    'S1062': ('1f_b97XjX0nXDUMa9aSAxFPNx2guyYhHk', 'R54F56C59F64A__Ensuring Sustainable Access to Drinking Water in Sub Saharan Africa Conflict Bet.pdf'),
    'S1102': ('14H6QDrJrEcqfLBjFElOvXmMGLpA30FDo', 'R76BD2052C008__Determinants and Benefits of Household Level Participation in Rural Drinking Wat.pdf'),
    'S1122': ('1ljbhK1CFgpwDR1fVRvN6tfRBPeSakWfa', 'R0327EF4BAA21__Is the Tap Locked An Event History Analysis of Piped Water Access in Ouagadougou.pdf'),
    'S1144': ('1f1uaX_KrBulsBRhgTjy5Wh1hTZ5rJoRy', 'R3DB2F9D0CE7E__Civil Society in Urban Sanitation and Solid Waste Management the Role of Ngos an.pdf'),
    'S1146': ('1spQLMQj6hV6PEQ5swYvH4alaBhR4grWN', 'RD768BF81FBAA__Money down the drain Corruption and water service.pdf'),
    'S1162': ('1NC5_KYJ2XfsVbYswAxaaupNcmTVxgaXE', 'R66871E6DA5D1__A small improvement Small cities lag in expanding household water coverage acros.pdf'),
    'S1163': ('1QytgJNw_4jtZMOnMTJuuY-O-Vwamt2aT', 'R8C288AFDD095__Factors associated with water quality, sanitation, and hygiene in rural schools.pdf'),
}
NO_DRIVE_NOTE = {
    'S539': 'a PDF from an earlier retrieval round (not re-downloaded from Drive in this round)',
    'S1169': 'a PDF from an earlier retrieval round; it is a scan without a usable text layer',
    'S471': 'no PDF found in the Drive folders (searched by record id, DOI and title)',
}
FILE_NOTE = {
    'S294': 'This file is the 2021 BMJ Global Health report of the trial (catalogued as S366), not the 2025 paper catalogued as S294.',
}
LEGAL_TERMS = ('legal', 'law', 'statut', 'regulat', 'right', 'decree', 'contract', 'legislat')   # stems, so 'regulat' counts regulation, regulatory, regulated


def rows(key):
    return cf.read(key)


def trunc(s, n):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= n else s[:n].rstrip() + '...'


def status_of(s, ft_by_rec, ed, ck):
    c = ck.get(s)
    if c and c['scope_outcome_check'] == 'flagged':
        return 'A28', "FLAGGED in A28 by the AI's narrow-scope and outcome check; NOT confirmed; awaits your ruling"
    f = ft_by_rec[ed[s]['record_id']]
    if c and c['scope_outcome_check'] == 'passed':
        return 'AI-checked', ("A CK confirmation of the inclusion and of both direction codings was RECORDED on 2026-10-14 after the AI's own narrow-scope and outcome check (Round 11 instruction). "
                              "You have not yet verified this study against the paper, so treat it as AI-checked until you do")
    if f['reviewer_2'].startswith('Human-'):
        return 'earlier', "Inclusion confirmed by you earlier (the S001-S200 pass); the direction coding has not been checked"
    return 'earlier', "Inclusion decided by your own CK ruling earlier (an A6, A16, A19 or A22-A25 pass); the direction coding has not been checked"


def build(pdf_dir):
    ed = {r['study_id']: r for r in rows('ed')}
    es = {r['study_id']: r for r in rows('es')}
    em = {r['study_id']: r for r in rows('em')}
    ft = {r['record_id']: r for r in rows('ft')}
    code = {r['study_id']: r for r in csv.DictReader(open(ROOT / '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', encoding='utf-8'))}
    ck = {r['study_id']: r for r in csv.DictReader(open(ROOT / '05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv', encoding='utf-8'))}
    core = sorted((s for s in es if es[s]['synthesis_family'] in ('A', 'B', 'C')), key=lambda s: (es[s]['synthesis_family'], int(s[1:])))
    assert len(core) == 37 == len(code), (len(core), len(code))
    entries, manifest, summary = {}, [], []
    for s in core:
        e, x, c = es[s], ed[s], code[s]
        pdf = Path(pdf_dir) / f'{s}.pdf' if pdf_dir else None
        doc = T.Doc(pdf) if pdf and pdf.exists() else None
        kind, status = status_of(s, ft, ed, ck)
        est_tokens = T.number_tokens(' '.join([e['effect_estimate'], e['lower_CI'], e['upper_CI'], e['standard_error']]), 'estimate')
        n_tokens = T.number_tokens(e['sample_size'] + ' ' + x.get('extraction_sample_size', ''), 'n')
        L = [f"### {s}  ·  Family {e['synthesis_family']}  ·  {trunc(x['citation'], 330)}", '',
             f"- **Status:** {status}.",
             f"- **DOI:** {x['doi'] or 'none recorded'}  ·  **Country:** {x['country']}  ·  **Language:** {x['language']}  ·  **Design class:** {em[s]['study_design_class']}  ·  **Study design (AI):** {trunc(x['study_design'], 200)}"]
        manifest_row = {'study_id': s, 'pdf_file': f'{s}.pdf', 'drive_file_id': '', 'drive_title': '', 'pages': '', 'bytes': '', 'sha256': '', 'text_characters': '', 'text_layer': '', 'title_word_share': '', 'first_author_on_first_pages': '', 'note': ''}
        if s in DRIVE:
            manifest_row['drive_file_id'], manifest_row['drive_title'] = DRIVE[s]
        manifest_row['note'] = FILE_NOTE.get(s, '') or NO_DRIVE_NOTE.get(s, '')
        cov = None
        if doc is None:
            L.append(f"- **Source PDF:** NONE available. {NO_DRIVE_NOTE.get(s, 'No file was found')}. Nothing below can be checked against a source file; please supply the PDF.")
            manifest_row['text_layer'] = 'no pdf'
        else:
            idc = T.identity_check(doc, x['citation'])
            density = doc.chars / max(doc.n, 1)
            layer = 'ok' if density >= 1200 else 'sparse (scan or image text; machine search is unreliable)' if density >= 250 else 'none (scan; no machine search possible)'
            manifest_row.update({'pages': doc.n, 'bytes': pdf.stat().st_size, 'sha256': T.sha256(pdf), 'text_characters': doc.chars, 'text_layer': layer.split(' ')[0],
                                 'title_word_share': f"{idc['title_word_share']:.2f}", 'first_author_on_first_pages': 'yes' if idc['first_author_found'] else 'no'})
            ident = ('looks like the cited paper' if idc['title_word_share'] >= 0.5 and idc['first_author_found'] else 'DOES NOT CLEARLY MATCH the citation (check it is the right paper)')
            L.append(f"- **Source PDF:** `{s}.pdf`, {doc.n} PDF pages, text layer {layer}; identity check: {ident} (title words found {idc['title_word_share']:.0%}, first author {'found' if idc['first_author_found'] else 'not found'} on pages 1 to 2); "
                     f"SHA-256 `{manifest_row['sha256'][:16]}`; " + (f"Drive file `{DRIVE[s][1]}`. " if s in DRIVE else f"origin: {NO_DRIVE_NOTE.get(s, 'unknown')}. ") + (FILE_NOTE.get(s, '') + ' ' if s in FILE_NOTE else '') +
                     "Page numbers below are PDF page indexes, which can differ from the pages printed in the journal.")
            full = ' '.join(doc.pages + [' '.join(doc.layout_lines(p)) for p in range(1, doc.n + 1)])
            f_est, f_n = T.present(est_tokens, full), T.present(n_tokens, full)
            f_rnd = T.present_rounded([t for t in est_tokens if t not in f_est], full)
            cov = {'est': (len(f_est) + len(f_rnd), len(est_tokens)), 'est_exact': len(f_est), 'est_rounded': f_rnd, 'n': (len(f_n), len(n_tokens)),
                   'est_missing': [t for t in est_tokens if t not in f_est and t not in f_rnd], 'n_missing': [t for t in n_tokens if t not in f_n], 'layer': layer, 'ident': ident}
        L += ['', '**Stored in `effect_sizes.csv` (the AI\'s extraction; this is what you are verifying):**', '',
              '| Field | Stored value |', '|---|---|',
              f"| Exposure | {trunc(e['exposure_definition'], 420)} |", f"| Comparator | {trunc(e['comparator_definition'], 320)} |",
              f"| Effect measure | {trunc(e['effect_measure'], 260)} |", f"| Estimate | {trunc(e['effect_estimate'], 520)} |",
              f"| CI (lower, upper) / SE | {e['lower_CI'] or 'none'}, {e['upper_CI'] or 'none'} / {trunc(e['standard_error'], 160) or 'none'} |",
              f"| Sample size | {trunc(e['sample_size'], 200)} |", f"| Direction text | {trunc(e['direction'], 260)} |", f"| Adjusted | {trunc(e['adjusted'], 200)} |",
              f"| Where the AI says it looked | table: {x['table'] or 'none'}; section: {x['section'] or 'none'}; location: {trunc(x['exact_location'], 140) or 'none'} |",
              f"| Risk of bias (AI, rule-based) | {cf.tool_of(x['risk_of_bias_tool'])}: {trunc(x['risk_of_bias_rating'], 160)} |",
              f"| SWiM coding (AI) | raw sign **{c['raw_coefficient_sign']}**; outcome polarity {c['outcome_polarity']}; exposure orientation {c['exposure_orientation']}; substantive direction **{c['substantive_direction']}**"
              f"{'; adjusted alternative ' + c['alternative_substantive_direction'] if c['alternative_substantive_direction'] else ''}; note: {trunc(c['coding_note'], 240)} |", '']
        if doc is not None:
            if layer.startswith('none') or layer.startswith('sparse'):
                L += ['**This file is a scan or has too little text to search.** The AI cannot locate passages in it, so none are offered, and no quote is given. Please read the paper directly: the AI recorded its source as '
                      f"table: {x['table'] or 'none'}; location: {trunc(x['exact_location'], 140) or 'none'} (above).", '',
                      '**Your verification (blank on purpose; the AI does not fill or tick any of this):**', '',
                      '- [ ] Inclusion and scope (criteria 1 to 4)   - [ ] Exposure and comparator   - [ ] Outcome   - [ ] Estimate, SE or CI, p   - [ ] Sample size   - [ ] Risk-of-bias rating   - [ ] Raw sign and substantive direction',
                      '- **Your decision:** ____   ·   Comment: ____', '']
                entries[s] = L
                summary.append((s, e['synthesis_family'], kind, True, None, c))
                manifest.append(manifest_row)
                continue
            L += ['**Does the PDF contain the stored numbers?**', '',
                  f"- Estimate numbers found anywhere in the PDF: **{cov['est'][0]} of {cov['est'][1]}**" + (f" ({cov['est_exact']} exactly; {len(cov['est_rounded'])} only as the rounded form of a more precisely printed number: {', '.join(cov['est_rounded'][:8])})" if cov['est_rounded'] else '') +
                  (f" (not found: {', '.join(cov['est_missing'][:12])})" if cov['est_missing'] else '') + '.',
                  f"- Sample-size numbers found anywhere in the PDF: **{cov['n'][0]} of {cov['n'][1]}**" + (f" (not found: {', '.join(cov['n_missing'])})" if cov['n_missing'] else '') + '.']
            if x['language'].strip().lower() != 'english':
                L.append(f"- The paper is in {x['language']}; passages are matched mostly on numbers, because the stored terms are English.")
            L.append('')
            if s in CURATED:
                L += ['**Hand-picked passages for your A28 ruling (verbatim; each was checked against the PDF text when this file was built):**', '', f"> **What the paper's exposure is (AI summary, from the quotes below; not a ruling):** {CURATED[s]['summary']}", '']
                for lab, q in CURATED[s]['quotes']:
                    pages = doc.find(q)
                    assert pages, f'{s}: curated quote not found in the PDF: {q[:80]}'
                    cap = ''
                    if len(q) < 140 and re.search(r'\d', q):
                        capt = doc.caption_above(pages[0], q)
                        cap = f", {capt}" if capt else ''
                    L.append(f"- *{lab}* (PDF p. {pages[0]}{cap}): \"{q}\"")
                counts = Counter()
                low = ' '.join(doc.pages).lower()
                for t in LEGAL_TERMS:
                    counts[t] = len(re.findall(r'\b' + t + r'\w*', low))
                L += ['', f"- Counts of words that begin with these stems anywhere in the PDF (including the reference list): " + ', '.join(f"{t}- {counts[t]}" for t in LEGAL_TERMS) + '.', '']
            L += ['**Passages located by number or term match (verbatim; the AI has not judged whether they support the stored value):**', '']
            used = False
            for lab, ps in (('Estimate', T.estimate_passages(doc, est_tokens, limit=2)), ('Sample size', T.n_passages(doc, n_tokens, limit=1)),
                            ('Exposure and comparator', T.term_passages(doc, T.content_terms(e['exposure_definition'] + ' ' + e['comparator_definition']), limit=1)),
                            ('Outcome', T.term_passages(doc, T.content_terms(e['effect_measure'] + ' ' + e['direction'] + ' ' + e['outcome_family'].replace('_', ' ')), limit=1, extra=re.compile(r'dependent|outcome', re.I))),
                            ('Design', T.design_passages(doc, 1))):
                if not ps:
                    why = ' The stored value contains no number to search for.' if (lab == 'Sample size' and not n_tokens) or (lab == 'Estimate' and not est_tokens) else ''
                    L.append(f"- *{lab}:* no matching passage found in the text layer.{why}")
                    continue
                used = True
                for p in ps:
                    shown = T.trim(p['text'], max(p['text'].find(p['matched'][0].split(' ')[0]), 0) if p['matched'] else None, 420)
                    assert doc.contains(p['page'], shown), f"{s}: a trimmed passage is not verbatim on PDF page {p['page']}: {shown[:80]}"
                    cap = doc.caption_above(p['page'], p['text']) if p['kind'] != 'sentence' else None
                    where = f"PDF p. {p['page']}" + (f", {cap}" if cap else (f", tables on this page: {', '.join(doc.tables_on(p['page']))}" if doc.tables_on(p['page']) and lab in ('Estimate', 'Sample size') else ''))
                    L.append(f"- *{lab}* ({where}; {doc.section_label(p['page'])}; matched {', '.join(p['matched'][:8])}): \"{shown}\"")
            if not used:
                L.append('- No passage could be located; check the PDF directly.')
            L.append('')
        L += ['**Your verification (blank on purpose; the AI does not fill or tick any of this):**', '',
              '- [ ] Inclusion and scope (criteria 1 to 4)   - [ ] Exposure and comparator   - [ ] Outcome   - [ ] Estimate, SE or CI, p   - [ ] Sample size   - [ ] Risk-of-bias rating   - [ ] Raw sign and substantive direction',
              ('- **Your A28 ruling:** keep / exclude E03 / exclude other (code ____)   ·   Comment: ' if s in A28 else '- **Your decision:** ____   ·   Comment: ') + '____', '']
        entries[s] = L
        summary.append((s, e['synthesis_family'], kind, doc is not None, cov, c))
        manifest.append(manifest_row)
    return core, entries, summary, manifest


def render(core, entries, summary):
    F = cf.compute()
    kinds = Counter(k for _, _, k, _, _, _ in summary)
    have = sum(1 for *_, d, _, _ in summary if d)
    L = ['# SWiM source-verification dossier: the 37 studies in Families A, B and C (generated, 2026-10-14)', '',
         "*Generated by `code/analysis/build_swim_source_dossier.py` from the databases and the source PDFs. This file is a reading aid for **your** verification. It records no confirmation of any kind: no `human_verified`, no `reviewer_2`, no CK entry. "
         "Every box is blank for you. The AI located the passages below by matching the stored numbers and terms; it did not decide whether a passage supports a stored value.*", '',
         '## How to use it', '',
         "1. Start with the ten **A28** entries (section 1). Each has hand-picked, verbatim quotes, checked against the PDF text, and a neutral description of the paper's own exposure, so you can rule keep (a formal rule or mechanism) or exclude E03.",
         "2. For each other study, open the PDF, read the quoted passages in context, and compare the stored values in the table with the paper. The dossier says how many of the stored numbers it could find in the PDF at all.",
         "3. If you want a study recorded as verified, say so in your own words and the AI will record exactly that, under your initials, and nothing more.", '',
         "**Conventions.** Quotes are verbatim apart from three mechanical clean-ups: ligature glyphs expanded (ﬁ to fi), a hyphen at a line break inside a word joined, and runs of whitespace collapsed to one space. `[...]` marks text cut from a long passage. "
         "Table rows are copied from the PDF's layout text and can lose their column alignment. Page numbers are PDF page indexes. The files themselves are listed, with hashes, in `SWIM_37_SOURCE_PDF_MANIFEST.csv`; the PDFs are not in the repository.", '',
         '## Status of the 37 studies', '',
         f"- **{kinds['A28']} flagged (A28)**, not confirmed, awaiting your ruling.",
         f"- **{kinds['AI-checked']} AI-checked**: a CK confirmation was recorded on 2026-10-14 after the AI's own scope and outcome check, under your Round 11 instruction. You have not verified them against the papers. They are shown as AI-checked here because the standard for this dossier is your own reading.",
         f"- **{kinds['earlier']} confirmed earlier by you** for inclusion (the S001-S200 pass or your own CK rulings); their direction codings have not been checked.",
         f"- Source PDFs: {have} of 37 available to this build.", '',
         '| Study | Fam | Status | PDF | Estimate numbers found | Sample numbers found | Text layer | Raw sign | Substantive |', '|---|---|---|---|---|---|---|---|---|']
    for s, fam, kind, d, cov, c in summary:
        L.append(f"| {s} | {fam} | {kind} | {'yes' if d else '**none**'} | " + (f"{cov['est'][0]}/{cov['est'][1]}" if cov else 'n/a') + ' | ' + (f"{cov['n'][0]}/{cov['n'][1]}" if cov else 'n/a') + ' | ' + (cov['layer'].split(' ')[0] if cov else 'n/a') + f" | {c['raw_coefficient_sign']} | {c['substantive_direction']} |")
    L += ['', "*The numbers-found columns count how many of the numbers stored in `effect_sizes.csv` appear anywhere in the PDF's text layer. A low count means a possible extraction error, a different version of the paper, or a text layer that lost its tables, not a finding; a high count is not proof either, because a short decimal can match unrelated text.*", '',
          '## 1. The A28 studies awaiting your ruling', '']
    for s in A28:
        L += entries[s]
    for fam, title in (('A', 'Family A: legal status, tenure, recognition and governance arrangements'), ('B', 'Family B: assistance, participation, trust and external support'), ('C', 'Family C: ownership, regulation, institutional capacity and administrative structure')):
        L += [f'## {"234"["ABC".index(fam)]}. {title}', '']
        for s in core:
            if s in entries and next(x[1] for x in summary if x[0] == s) == fam and s not in A28:
                L += entries[s]
    return '\n'.join(L).rstrip() + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf-dir', default=os.environ.get('SWIM_PDF_DIR'))
    a = ap.parse_args()
    core, entries, summary, manifest = build(a.pdf_dir)
    OUT_MD.write_text(render(core, entries, summary), encoding='utf-8')
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(manifest[0]), lineterminator='\r\n')
        w.writeheader()
        w.writerows(manifest)
    print(f'wrote {OUT_MD.relative_to(ROOT)} ({len(core)} studies) and {OUT_CSV.name}')


if __name__ == '__main__':
    main()
