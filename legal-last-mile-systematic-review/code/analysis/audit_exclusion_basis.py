#!/usr/bin/env python3
"""Which full-text-stage exclusions rest on a landing-page abstract or a metadata record rather than on a read full text?

The full-text database holds 1,117 excludes. Most were decided on a read full text, but the reason text of some says the decision used only a landing-page
abstract, a paywalled abstract or a bibliographic metadata record. E10 (inaccessible) and E08 (duplicate) are expected to say so; for the other codes it
means a substantive exclusion (wrong topic, wrong design, no empirical evidence, insufficient information) was made without the full text. This lists them
so the researcher can retrieve the texts. Detection is a phrase match on exclusion_reason_detail, so it finds records whose reason SAYS the basis was thin;
it cannot find ones that do not say so. Writes 05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.{csv,md}. Run from the project root."""
import csv
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

OUT_CSV = cf.ROOT / '05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.csv'
OUT_MD = cf.ROOT / '05_analysis/descriptive/EXCLUSION_BASIS_AUDIT_2026-10-04.md'
A16 = cf.ROOT / '02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.csv'
PAT = re.compile(r'abstract[- ]only|landing[- ]page|metadata (record|only)|bibliographic metadata|paywall|no abstract|abstract text|only (the )?abstract|abstract (was|is) (available|retrieved)', re.I)
# What the copy in the researcher's Drive showed (2026-10-04; an AI reading, same model family as the screener, so not independent). Hand-entered, not derived: records not listed
# here were not checked. "portal page" = Drive holds only a repository or publisher landing page, not the article.
DRIVE_CHECK = {
    'R0B0F3925F533': 'portal page (Groningen); abstract: institutional capacity in regional water-resource cooperation, Cirebon; access outcome not stated -- borderline, E01 or E04 defensible',
    'R155FFF508359': 'portal page (Wageningen); abstract: peasant and indigenous water-user associations defending irrigation water in the Andes -- legal/governance exposure but irrigation water, so E07 (wrong service) is the better code than E01',
    'R977ECB01FA02': 'portal page (Wageningen); abstract: rules and norms of access to four natural resources (water one of them) after resettlement in Mozambique -- governance of access, water not the focus; borderline',
    'RA1F6E143593E': 'portal page (Wageningen); abstract: agribusiness and peasant irrigation water contestation, Tanzania -- agricultural water, E07 plausible',
    'RFC362FE42028': 'portal page (REIS journal); abstract: public participation in Water Framework Directive basin processes, Spain -- basin governance, not household or community service access; exclusion plausible',
    'RF5C6D981DB3B': 'portal page (Springer paywall preview); abstract: SDG interlinkages case of land-cover change and water quality in Chiapas, governance as a lever -- water quality focus; exclusion plausible',
    'RC1CB10DA729E': 'full PDF in Drive (Schiedek et al. 2021): qualitative content analysis of national SWA commitments, outcome is commitment quality, not access -- exclusion stands; status field stale',
    'RE8D979932979': 'PDF in Drive (Blanchon 2003, French): implementation of the 1998 Water Act and the environmental Reserve on the Orange River -- legal reform but environmental-flow outcome; exclusion plausible; status field stale',
    'R1A33C22EDA73': 'full PDF in Drive (Baird et al. 2013): narrative exploration of cistern safety in Canada with little empirical data -- exclusion plausible; status field stale',
    'R600CF4CBBFE7': 'full PDF in Drive (MacArthur et al. 2025): quasi-experimental evaluation of WASH programme effects on gender equality -- outcome is gender equality, not access (E04 would fit as well as E03); status field stale',
    'REA305644CBB3': 'full PDF in Drive (Chambolle 1999, French): utility-practitioner report on serving poor districts under concession contracts -- no empirical design; E05 plausible; status field stale',
    'RF22EFFAD48CC': 'PDF in Drive (Fracalanza et al. 2013, Portuguese): conceptual discussion of environmental justice and basin committees -- E05 plausible; status field stale',
    'RC9378CBDB2EE': 'portal page (Utrecht repository, abstract only): governance capacity for desalination in Antofagasta, Chile; technology and consumer perception focus, access is one step of a priority ladder -- exclusion plausible',
    'RAB6AA06D8E9D': 'not checked: no Drive text found (title: a climate-change and water-quality socio-economics study, Catalonia)',
    'R803988411D3E': 'portal page (Wageningen, book record): edited volume on socio-technical diversity in East African waste and sanitation; multi-chapter book, not a single study -- E12 defensible, though its empirical core is sanitation access',
    'R0B462A3EF2D7': 'full PDF in Drive (Leite et al. 2026): Balanced Scorecard for unbilled-water losses in a Portuguese utility -- utility management, not access; exclusion stands; status field stale',
    'R54D4AEC2087E': 'full PDF in Drive (Scruggs et al. 2020): interview study of public acceptance of direct potable reuse in five communities, governance as one influencing factor -- outcome is acceptance of reuse, not access; exclusion plausible; status field stale',
    'RAA8D967AD545': "PDF in Drive (Barnes 2006): a university utilities master's programme -- not a study of access; exclusion stands; status field stale",
    'RBEBE0BACCD18': "full PDF in Drive (Wagaba et al. 2023): survey and interviews on small NGOs' access to geological data (bureaucracy a barrier) -- the access studied is to data, not water; exclusion plausible; status field stale",
    'RD1829FC2C94A': "full PDF in Drive (Milton et al. 2012): authors' lessons from arsenic mitigation programmes, from experience rather than a defined method -- E05 would fit better than E03; status field stale",
    'R00E98F4E387F': 'full PDF in Drive (Hove et al. 2022): narrative review with a stated multi-database search (21 articles) of community participation in health and water governance in South Africa -- outcome is participation effectiveness, not access; note it is a hybrid review like S418 and S329, which were kept under AMSTAR 2; status field stale',
    'R73C7494E55DD': 'full PDF in Drive (Gidion 2025): network DEA method for ranking water utilities -- method development, no access outcome; exclusion stands; status field stale',
    'RCB78D4EF3652': 'not checked: no Drive text found',
    'R057F7388EEF4': 'full PDF in Drive (Wall 2006, Water SA technical note): investigation of franchising as a service-delivery model, concept and assessment, no empirical data -- E05 plausible; status field stale',
    'R4266AA2DF8F3': 'full PDF in Drive (Busari 2002): analysis of rural water-supply policies and institutional capacities in Swaziland with proposals -- an institutional and policy analysis that could count as documentary evidence, so E05 is borderline; status field stale',
    'R804A6CFFD1D7': 'PDF in Drive (Umunna 2010): a letter to the editor on community participation and rural health -- opinion piece; E05 stands; status field stale',
    'RF8AB3815D963': 'full PDF in Drive (Nurbaiti & Bambang 2018): non-systematic literature study of community participation in rural water and sanitation programmes -- E05 plausible; status field stale',
    'R0532032FE3BB': 'full PDF in Drive (Saraswat et al. 2017): scenario modelling of Kathmandu water demand and supply strategies -- modelling study; E06 plausible; status field stale',
    'R9167527BC9AE': 'full PDF in Drive (Alehashemi & Coulais 2021, French): hydraulic systems and urban structure in Iran with three field case studies -- infrastructure and territory focus; E06 or E01 plausible; status field stale',
    'RDEA162168676': 'full PDF in Drive (Jauhari et al. 2021): household survey of life-cycle costs of self-supply water in Metro City, Indonesia -- costs of an access route, little governance exposure; E03 would fit as well as E06; status field stale',
}
FIELDS = ['group', 'record_id', 'year', 'exclusion_code', 'title', 'basis_phrase', 'in_A16_sheet', 'reason_excerpt', 'drive_check']
STATUS_CONTRADICTS = ('not_retrievable', 'oa_pdf_candidate', 'oa_page_candidate')  # a decided record whose recorded status says no full text was obtained (or only located, not downloaded)
GROUPS = {'substantive': 'substantive exclusion (E01-E07, E09, E12) decided without a read full text', 'E10': 'E10 inaccessible (expected to say so)', 'E08': 'E08 duplicate (expected to say so)'}
CODE_NAMES = {'E01': 'wrong topic', 'E02': 'wrong population', 'E03': 'wrong exposure', 'E04': 'wrong outcome', 'E05': 'no empirical evidence', 'E06': 'engineering only',
              'E07': 'wrong service', 'E09': 'insufficient information', 'E12': 'wrong study design'}


def build():
    a16 = {r['record_id']: r['priority'] for r in csv.DictReader(open(A16, encoding='utf-8', newline=''))} if A16.exists() else {}
    rows = []
    for r in cf.read('ft'):
        if r['final_decision'] != 'exclude':
            continue
        m = PAT.search(r['exclusion_reason_detail'])
        if not m or 'full text read' in r['exclusion_reason_detail'].lower():  # a reason that says the full text WAS read is not a thin-basis exclusion (e.g. S356's retired abstract-only extraction)
            continue
        code = r['exclusion_reason']
        group = code if code in ('E10', 'E08') else 'substantive'
        rows.append({'group': group, 'record_id': r['record_id'], 'year': r['year'], 'exclusion_code': code, 'title': r['title'][:110], 'basis_phrase': m.group(0).lower(),
                     'in_A16_sheet': ('priority ' + a16[r['record_id']]) if r['record_id'] in a16 else 'no', 'reason_excerpt': r['exclusion_reason_detail'][:240].replace('\n', ' '), 'drive_check': DRIVE_CHECK.get(r['record_id'], 'not checked')})
    ed = {r['record_id']: r for r in cf.read('ed')}
    ed_notes = {k: v['extraction_note'] for k, v in ed.items()}
    have = {r['record_id'] for r in rows}
    for r in cf.read('ft'):
        code = r['exclusion_reason']
        if r['final_decision'] not in ('include', 'exclude') or r['full_text_status'] not in STATUS_CONTRADICTS or code in ('E10', 'E08') or r['record_id'] in have:
            continue
        e = ed.get(r['record_id'])
        basis = ('extraction note: ' + e['extraction_note'][:70].replace('\n', ' ')) if e else r['notes'][:120].replace('\n', ' ')
        rows.append({'group': 'status_include' if r['final_decision'] == 'include' else 'status_exclude', 'record_id': r['record_id'], 'year': r['year'], 'exclusion_code': code or 'include', 'title': r['title'][:110],
                     'basis_phrase': 'status ' + r['full_text_status'], 'in_A16_sheet': ('priority ' + a16[r['record_id']]) if r['record_id'] in a16 else 'no', 'reason_excerpt': basis, 'drive_check': DRIVE_CHECK.get(r['record_id'], 'not checked')})
    order = {'substantive': 0, 'status_exclude': 1, 'status_include': 2, 'E10': 3, 'E08': 4}
    rows.sort(key=lambda x: (order[x['group']], x['exclusion_code'], x['record_id']))
    n_ex = sum(1 for r in cf.read('ft') if r['final_decision'] == 'exclude')
    sub = [r for r in rows if r['group'] == 'substantive']
    st_ex = [r for r in rows if r['group'] == 'status_exclude']
    st_in = [r for r in rows if r['group'] == 'status_include']
    st_in_full = sum(1 for r in st_in if not ed_notes.get(r['record_id'], '').startswith(cf.ABSTRACT_ONLY_PREFIXES))  # extraction not marked abstract-only
    by = {}
    for r in sub:
        by[r['exclusion_code']] = by.get(r['exclusion_code'], 0) + 1
    L = ['# Decisions that rest on a landing page, abstract or metadata record rather than a read full text', '',
         f"Generated by `code/analysis/audit_exclusion_basis.py` from `full_text_screening_database.csv`. Of {n_ex:,} full-text-stage excludes, {sum(1 for r in rows if r['group'] in ('substantive', 'E10', 'E08'))} have a reason text that mentions a landing-page abstract, a paywalled abstract or a metadata record.", '',
         f"- **{len(sub)} are substantive exclusions** ({', '.join(f'{k} {CODE_NAMES[k]} {v}' for k, v in sorted(by.items()))}) made at the full-text stage without a read full text. They are the ones that matter: a topic, design or evidence judgement rests on an abstract the reviewer itself called incomplete.",
         f"- {sum(1 for r in rows if r['group'] == 'E10')} are E10 (inaccessible full text) and {sum(1 for r in rows if r['group'] == 'E08')} E08 (duplicate); a thin basis is expected for both and is listed only for completeness.", '',
         f"A second check uses the recorded `full_text_status` instead of the reason text: {len(st_ex)} further substantive excludes and {len(st_in)} includes are decided although their status says `not_retrievable` or only `oa_pdf_candidate` / `oa_page_candidate` (a PDF or landing page located, not downloaded). "
         f"For the includes the likely explanation is a stale status (the PDF arrived later through Drive: {st_in_full} of {len(st_in)} have an extraction that is not marked abstract-only); for the excludes no such trail exists, so they too are exclusions without a read full text, missed by the phrase match. Blank statuses are not counted: {sum(1 for r in cf.read('ft') if r['final_decision'] in ('include', 'exclude') and not r['full_text_status'])} decided records have none, which looks like unfilled bookkeeping rather than evidence either way.", '',
         "The phrase match finds exclusions whose reason *says* the basis was thin and the status check finds contradictions in the bookkeeping; other cases may exist that show neither. Nothing here changes a decision.", '',
         "**What would resolve it:** retrieve the full texts of the substantive and status-contradicting excludes (about 30 records) and re-screen them against `INCLUSION_EXCLUSION.md`; or relabel them as excluded at the title/abstract stage and state in the PRISMA flow that they were never read in full (`DECISIONS_AND_OPEN_ITEMS.md` A19).", '',
         "| Group | Record | Year | Code | Title | In A16 sheet |", "|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['group']} | {r['record_id']} | {r['year']} | {r['exclusion_code']} | {r['title']} | {r['in_A16_sheet']} |")
    chk = [r for r in rows if not r['drive_check'].startswith('not checked')]
    L += ['', '## What the Drive copies showed', '',
          f"An AI reading (same model family as the screener, so not independent) of the Drive copy of {len(chk)} of the {sum(1 for r in rows if r['group'] in ('substantive', 'status_exclude'))} substantive and status-contradicting excludes; the other {sum(1 for r in rows if r['group'] in ('substantive', 'status_exclude')) - len(chk)} have no Drive text. "
          f"Of the {len(chk)}, {sum(1 for r in chk if r['drive_check'].startswith('portal page'))} are only portal or landing pages (the original exclusion really was made on an abstract; on that abstract the exclusion is plausible or borderline, and for R155FFF508359 and RA1F6E143593E the code E07 would fit better) "
          f"and {sum(1 for r in chk if 'status field stale' in r['drive_check'])} are real PDFs whose recorded status was simply stale (no concern beyond the bookkeeping).", '']
    L += [f"- **{r['record_id']}** ({r['exclusion_code']}) — {r['drive_check']}" for r in chk]
    return rows, '\n'.join(L) + '\n'


if __name__ == '__main__':
    rows, md = build()
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(md, encoding='utf-8')
    print(f'wrote {OUT_CSV.relative_to(cf.ROOT)} ({len(rows)} rows) and {OUT_MD.name}')
