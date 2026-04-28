"""
TJRR (Tribunal de Justiça de Roraima) water law case scraper.
Uses JSF form submission, year by year 2016-2026.
Small state: typically <15 cases/year, no pagination needed.
"""
import os
import urllib.request, http.cookiejar, urllib.parse, re, json, time, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://jurisprudencia.tjrr.jus.br/'
OUT = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjrr_cases_2016_2026.json')

HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}


def make_session():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(BASE, headers=HDRS)
    with opener.open(req, timeout=20) as r:
        html = r.read().decode('utf-8', errors='replace')
    vs = re.search(r'id="j_id1:javax\.faces\.ViewState:0" value="([^"]+)"', html)
    fa = re.search(r'<form id="menuinicial"[^>]+action="([^"]+)"', html)
    if not vs or not fa:
        raise RuntimeError('Could not extract ViewState or form action')
    action = 'https://jurisprudencia.tjrr.jus.br' + fa.group(1).replace('&amp;', '&')
    return opener, vs.group(1), action


def extract_cases(html, tag):
    """Extract case data from TJRR results page."""
    cases = []
    seen = set()

    # Count tabs to see how many cases
    acord_m = re.search(r'ACÓRD.{1,20}\((\d+)\)', html, re.IGNORECASE)
    mono_m  = re.search(r'DECIS.{1,30}\((\d+)\)', html, re.IGNORECASE)
    n_acordaos = int(acord_m.group(1)) if acord_m else 0
    n_mono = int(mono_m.group(1)) if mono_m else 0
    total = n_acordaos + n_mono

    # Find all result rows: id="resultadosN"
    result_divs = list(re.finditer(r'id="resultados(\d+)"', html))
    print(f'    Found {len(result_divs)} result divs (tab says {total})')

    for i, m in enumerate(result_divs):
        row_id = m.group(1)
        row_start = m.start()
        # End is next result div or end of block
        if i + 1 < len(result_divs):
            row_end = result_divs[i+1].start()
        else:
            row_end = row_start + 20000
        row_html = html[row_start:row_end]

        # Process number from extrato-processo URL or direct CNJ pattern
        proc_m = re.search(r'extrato-processo\?p=(\d+)', row_html)
        cnj_nums = re.findall(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', row_html)
        # Filter TJRR numbers (court code 8.23)
        tjrr_nums = [n for n in cnj_nums if '.8.23.' in n]

        if tjrr_nums:
            num = tjrr_nums[0]
        elif proc_m:
            # Convert internal ID to CNJ format: 90005522920198230000 -> 9000552-29.2019.8.23.0000
            raw = proc_m.group(1)
            if len(raw) == 20:
                num = f'{raw[:7]}-{raw[7:9]}.{raw[9:13]}.{raw[13]}.{raw[14:16]}.{raw[16:]}'
            else:
                num = raw
        else:
            continue

        if num in seen:
            continue
        seen.add(num)

        # Extract docTexto values (in order: classe+numproc, relator, orgao, dtjulg, dtpub)
        doc_texts = re.findall(r'class="docTexto">\s*(.*?)\s*</div>', row_html, re.DOTALL)
        doc_texts_clean = [re.sub(r'<[^>]+>', '', t).strip() for t in doc_texts]

        # First docTexto has "Classe\nNumeroProcesso"
        classe = ''
        if doc_texts_clean:
            first = doc_texts_clean[0]
            lines = [l.strip() for l in first.split('\n') if l.strip()]
            classe = lines[0] if lines else ''

        relator = doc_texts_clean[1].strip() if len(doc_texts_clean) > 1 else ''
        camara  = doc_texts_clean[2].strip() if len(doc_texts_clean) > 2 else ''
        dt_julg = doc_texts_clean[3].strip() if len(doc_texts_clean) > 3 else ''

        # Ementa: find a large continuous text block
        ementa = ''
        for tm in re.finditer(r'<div[^>]*>([^<]{80,})', row_html):
            t = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
            if len(t) > 80 and t[0].isupper():
                ementa = t[:800]
                break

        cases.append({
            'num': num,
            'processDate': dt_julg,
            'publicDate': doc_texts_clean[4].strip() if len(doc_texts_clean) > 4 else '',
            'classe': classe,
            'relator': relator,
            'camara': camara,
            'comarca': '',
            'ementa': ementa,
            'tag': tag,
            'court': 'TJRR',
            'state': 'RR',
        })

    return cases


def search_year(opener, year, query):
    d1 = f'01/01/{year}'
    d2 = f'31/12/{year}'
    tag = f'{year}-rr'

    # Refresh session for each year (JSF ViewState is page-scoped)
    req0 = urllib.request.Request(BASE, headers=HDRS)
    with opener.open(req0, timeout=20) as r0:
        html0 = r0.read().decode('utf-8', errors='replace')
    vs = re.search(r'id="j_id1:javax\.faces\.ViewState:0" value="([^"]+)"', html0)
    fa = re.search(r'<form id="menuinicial"[^>]+action="([^"]+)"', html0)
    if not vs or not fa:
        print('  Cannot extract ViewState/action, skipping')
        return []
    vs = vs.group(1)
    action = BASE.rstrip('/') + fa.group(1).replace('&amp;', '&')

    post_data = urllib.parse.urlencode([
        ('menuinicial', 'menuinicial'),
        ('menuinicial:j_idt30', query),
        ('menuinicial:numProcesso', ''),
        ('menuinicial:datainicial_input', d1),
        ('menuinicial:datafinal_input', d2),
        ('menuinicial:j_idt32', ''),
        ('javax.faces.ViewState', vs),
    ], encoding='utf-8').encode('utf-8')

    req = urllib.request.Request(action, data=post_data, headers={**HDRS,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': BASE, 'Origin': 'https://jurisprudencia.tjrr.jus.br',
    })
    try:
        with opener.open(req, timeout=30) as r:
            html = r.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'  Error: {e}')
        return []

    # Get result counts from tabs (ACÓRDÃOS (N) / DECISÃO MONOCRÁTICA (N))
    acord_m = re.search(r'ACÓRD.{1,20}\((\d+)\)', html, re.IGNORECASE)
    mono_m  = re.search(r'DECIS.{1,30}\((\d+)\)', html, re.IGNORECASE)
    n_a = int(acord_m.group(1)) if acord_m else 0
    n_m = int(mono_m.group(1)) if mono_m else 0
    print(f'  {year}: {n_a} acórdãos + {n_m} monocráticas = {n_a+n_m} total')

    return extract_cases(html, tag)


def main():
    QUERY = 'água saneamento abastecimento fornecimento'

    print('Starting TJRR scraper...')
    print(f'Query: {QUERY}')

    opener, _, _ = make_session()
    all_cases = []
    seen_global = set()

    for year in range(2016, 2027):
        print(f'\nYear {year}:')
        try:
            cases = search_year(opener, year, QUERY)
        except Exception as e:
            print(f'  FAILED: {e}')
            cases = []

        new = 0
        for c in cases:
            if c['num'] not in seen_global:
                seen_global.add(c['num'])
                all_cases.append(c)
                new += 1
        print(f'  -> {new} unique new cases (total: {len(all_cases)})')

        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, ensure_ascii=False, indent=2)

        time.sleep(3)

    print(f'\n=== DONE: {len(all_cases)} total TJRR cases ===')
    print(f'Saved to: {OUT}')

if __name__ == '__main__':
    main()
