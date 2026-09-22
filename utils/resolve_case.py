#!/usr/bin/env python3
"""
resolve_case.py — stable permalinks for every decision in the dataset
=====================================================================
The `url` column captured at scrape time points at live court portals, several
of which rewrite or expire their URLs (the Brazilian ESAJ and ASP.NET portals
are the worst offenders; see the "Blocked" rows in README.md). This module maps
a decision's *identifier* to the most durable public address available for it,
so an external reviewer can still reach the text after the scraped URL rots.

Durability, by jurisdiction:

  Netherlands  PERMANENT. Every record carries an ECLI, and
               deeplink.rechtspraak.nl is the official resolver. The full XML,
               including the decision body, is at data.rechtspraak.nl.
  Canada       STABLE. CanLII citation URLs are maintained by CanLII. Where we
               only hold a style of cause we fall back to a CanLII search URL.
  Brazil       BEST EFFORT. There is no national permalink service for state
               court decisions. We normalise the CNJ process number
               (Res. CNJ 65/2008 format NNNNNNN-DD.AAAA.J.TR.OOOO) and emit the
               originating tribunal's jurisprudence search, pre-filled where the
               portal supports it. The normalised number, not the URL, is the
               durable identifier: it is what a reader types into any Brazilian
               court portal or into the CNJ consultation service.

Usage
-----
    # one case
    python utils/resolve_case.py ECLI:NL:RVS:2019:2481
    python utils/resolve_case.py 0001234-56.2022.8.26.0100 --tribunal TJSP

    # a whole dataset: adds a `permalink` and `permalink_kind` column
    python utils/resolve_case.py --csv data/water_law_global_coded.csv

Importable:
    from resolve_case import resolve
    resolve(case_id='ECLI:NL:RVS:2019:2481', country='Netherlands')
"""
import argparse
import csv
import re
import sys
import urllib.parse
from pathlib import Path

# ── Netherlands ───────────────────────────────────────────────────────────────
ECLI_RE = re.compile(r'\bECLI:[A-Z]{2}:[A-Z0-9]+:\d{4}:[A-Z0-9.\-]+', re.I)

NL_DEEPLINK = 'https://deeplink.rechtspraak.nl/uitspraak?id={ecli}'
NL_XML      = 'https://data.rechtspraak.nl/uitspraken/content?id={ecli}'

# ── Brazil ────────────────────────────────────────────────────────────────────
# CNJ unified process number: NNNNNNN-DD.AAAA.J.TR.OOOO
CNJ_RE = re.compile(r'(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})')

# Jurisprudence search entry points for the tribunals actually present in the
# dataset. Where a portal accepts a query string we pre-fill it; where it does
# not, the reviewer pastes the normalised number into the form.
BR_PORTALS = {
    'TJSP':  ('https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor={q}', True),
    'TJSC':  ('https://busca.tjsc.jus.br/jurisprudencia/buscaForm.do?q={q}', True),
    'TJRJ':  ('https://www3.tjrj.jus.br/ejuris/consultajurisprudenciaespecializada.aspx', False),
    'TJDFT': ('https://jurisdf.tjdft.jus.br/api-search/?q={q}', True),
    'TJRR':  ('https://esaj.tjrr.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor={q}', True),
    'TJAC':  ('https://esaj.tjac.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor={q}', True),
    'TJPI':  ('https://www.tjpi.jus.br/jurisprudencia/busca?q={q}', True),
    'TJTO':  ('https://jurisprudencia.tjto.jus.br/pesquisa?q={q}', True),
}
# National fallback: CNJ's public process consultation.
BR_CNJ_FALLBACK = 'https://www.cnj.jus.br/pjecnj/ConsultaPublica/DetalheProcessoConsultaPublica/listView.seam'

# Some TJSP records predate the CNJ unified numbering (Res. CNJ 65/2008) or were
# captured by the ESAJ internal acordao key rather than the process number. They
# carry a bare numeric id and, in the historical 1997-2015 subset, no URL at all.
# A 6-8 digit id is the ESAJ acordao key (cdAcordao), which addresses the PDF
# directly; longer ids are legacy process numbers and only support a search.
TJSP_ACORDAO = 'https://esaj.tjsp.jus.br/cjsg/getArquivo.do?cdAcordao={q}'
TJSP_SEARCH  = 'https://esaj.tjsp.jus.br/cjsg/resultadoCompleta.do?dados.buscaInteiroTeor={q}'
BARE_NUM_RE  = re.compile(r'^\s*(\d{6,16})\s*$')

# ── Canada ────────────────────────────────────────────────────────────────────
CANLII_URL_RE = re.compile(r'https?://(?:www\.)?canlii\.org/\S+', re.I)
CANLII_SEARCH = 'https://www.canlii.org/en/#search/text={q}'


def normalise_cnj(raw):
    """Return the canonical CNJ process number, or None if `raw` isn't one."""
    if not raw:
        return None
    m = CNJ_RE.search(str(raw))
    if not m:
        return None
    n, dd, aaaa, j, tr, oooo = m.groups()
    return f'{n}-{dd}.{aaaa}.{j}.{tr}.{oooo}'


def normalise_ecli(raw):
    """Return the canonical uppercase ECLI, or None."""
    if not raw:
        return None
    m = ECLI_RE.search(str(raw))
    return m.group(0).upper() if m else None


def resolve(case_id=None, country=None, tribunal=None, url=None, title=None):
    """Best durable address for one decision.

    Returns a dict: {permalink, permalink_kind, identifier, fulltext_url}
      permalink_kind is one of:
        ecli_deeplink   — permanent official resolver (Netherlands)
        canlii_citation — stable CanLII decision URL
        canlii_search   — CanLII search, decision URL not held
        court_search    — tribunal jurisprudence search (Brazil), pre-filled
        court_form      — tribunal search form, number must be pasted
        scraped_url     — falls back to the URL captured at scrape time
        unresolved      — no durable address could be built
      fulltext_url is populated only where the full text is machine-retrievable.
    """
    blank = {'permalink': '', 'permalink_kind': 'unresolved',
             'identifier': '', 'fulltext_url': ''}

    # Netherlands / any ECLI-bearing record, regardless of stated country.
    ecli = normalise_ecli(case_id) or normalise_ecli(title) or normalise_ecli(url)
    if ecli:
        return {'permalink': NL_DEEPLINK.format(ecli=urllib.parse.quote(ecli, safe=':')),
                'permalink_kind': 'ecli_deeplink',
                'identifier': ecli,
                'fulltext_url': NL_XML.format(ecli=urllib.parse.quote(ecli, safe=':'))}

    # Canada.
    if (country or '').strip().lower() == 'canada':
        m = CANLII_URL_RE.search(str(url or ''))
        if m:
            return {'permalink': m.group(0), 'permalink_kind': 'canlii_citation',
                    'identifier': str(case_id or ''), 'fulltext_url': ''}
        q = str(case_id or title or '').strip()
        if q:
            return {'permalink': CANLII_SEARCH.format(q=urllib.parse.quote(q)),
                    'permalink_kind': 'canlii_search',
                    'identifier': q, 'fulltext_url': ''}

    # Brazil.
    cnj = normalise_cnj(case_id) or normalise_cnj(title) or normalise_cnj(url)
    if cnj:
        trib = (tribunal or '').strip().upper()
        entry = BR_PORTALS.get(trib)
        if entry:
            tpl, prefill = entry
            return {'permalink': tpl.format(q=urllib.parse.quote(cnj)) if prefill else tpl,
                    'permalink_kind': 'court_search' if prefill else 'court_form',
                    'identifier': cnj, 'fulltext_url': ''}
        return {'permalink': BR_CNJ_FALLBACK, 'permalink_kind': 'court_form',
                'identifier': cnj, 'fulltext_url': ''}

    # Legacy / pre-CNJ Brazilian identifiers: a bare numeric court record id.
    bare = BARE_NUM_RE.match(str(case_id or ''))
    if bare and (country or '').strip().lower() == 'brazil':
        num = bare.group(1)
        if (tribunal or '').strip().upper() == 'TJSP':
            if 6 <= len(num) <= 8:
                return {'permalink': TJSP_ACORDAO.format(q=num),
                        'permalink_kind': 'court_record_id',
                        'identifier': f'TJSP cdAcordao {num}', 'fulltext_url': ''}
            return {'permalink': TJSP_SEARCH.format(q=urllib.parse.quote(num)),
                    'permalink_kind': 'court_search',
                    'identifier': f'TJSP legacy process {num}', 'fulltext_url': ''}
        entry = BR_PORTALS.get((tribunal or '').strip().upper())
        if entry and entry[1]:
            return {'permalink': entry[0].format(q=urllib.parse.quote(num)),
                    'permalink_kind': 'court_search',
                    'identifier': num, 'fulltext_url': ''}

    # Nothing durable — keep whatever the scraper captured.
    if url:
        return {'permalink': str(url), 'permalink_kind': 'scraped_url',
                'identifier': str(case_id or ''), 'fulltext_url': ''}
    return blank


def annotate_csv(in_path, out_path=None):
    """Add permalink columns to a dataset CSV. Returns the output path."""
    in_path = Path(in_path)
    out_path = Path(out_path) if out_path else in_path.with_name(
        in_path.stem + '_resolved.csv')

    with open(in_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = list(reader.fieldnames or [])

    for c in ('permalink', 'permalink_kind', 'identifier', 'fulltext_url'):
        if c not in fields:
            fields.append(c)

    kinds = {}
    for r in rows:
        res = resolve(case_id=r.get('case_id'), country=r.get('country'),
                      tribunal=r.get('tribunal'), url=r.get('url'),
                      title=r.get('title'))
        r.update(res)
        kinds[res['permalink_kind']] = kinds.get(res['permalink_kind'], 0) + 1

    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f'Resolved {len(rows):,} records -> {out_path}')
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        print(f'  {k:16} {v:>7,}  ({v/len(rows)*100:.1f}%)')
    unresolved = kinds.get('unresolved', 0) + kinds.get('scraped_url', 0)
    if unresolved:
        print(f'\n  {unresolved:,} records have no permanent resolver and depend on '
              f'the scraped URL. See DATA_ACCESS.md.')
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('case_id', nargs='?', help='ECLI, CNJ process number, or CanLII citation')
    ap.add_argument('--country')
    ap.add_argument('--tribunal')
    ap.add_argument('--url')
    ap.add_argument('--csv', help='annotate a whole dataset CSV instead')
    ap.add_argument('--out', help='output path for --csv')
    a = ap.parse_args()

    if a.csv:
        annotate_csv(a.csv, a.out)
        return
    if not a.case_id:
        ap.error('give a case_id or --csv')
    res = resolve(case_id=a.case_id, country=a.country,
                  tribunal=a.tribunal, url=a.url)
    for k, v in res.items():
        print(f'{k:16} {v}')


if __name__ == '__main__':
    sys.exit(main())
