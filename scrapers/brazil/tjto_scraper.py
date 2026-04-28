"""
TJTO (Tribunal de Justiça do Tocantins) water law case scraper.
Portal: https://jurisprudencia.tjto.jus.br/
Strategy: date filter on /consulta.php doesn't work server-side.
Approach: paginate all 822 results, fetch ementa+numero_processo from /ementa.php (Solr JSON),
derive year from CNJ number (e.g. 0019045-74.2024.8.27.2700 → year 2024).
Only keep 2016-2026 cases.
"""
import os
import urllib.request, http.cookiejar, urllib.parse, re, json, time, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://jurisprudencia.tjto.jus.br/'
SEARCH = BASE + 'consulta.php'
EMENTA = BASE + 'ementa.php'
OUT = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjto_cases_2016_2026.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,*/*',
    'Referer': BASE,
}

EMENTA_HDRS = {**HEADERS, 'Accept': 'application/json,*/*'}


def make_opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    with op.open(urllib.request.Request(BASE, headers=HEADERS), timeout=20) as r:
        pass
    return op


def num20_to_cnj(raw):
    """Convert 20-char raw number to CNJ format: NNNNNNN-NN.NNNN.N.NN.NNNN"""
    if len(raw) == 20:
        return f'{raw[:7]}-{raw[7:9]}.{raw[9:13]}.{raw[13]}.{raw[14:16]}.{raw[16:]}'
    return raw


def year_from_cnj(cnj):
    """Extract year from CNJ number (chars 10-13 in raw 20-char form, or from formatted)."""
    m = re.search(r'\d{7}-\d{2}\.(\d{4})', cnj)
    return m.group(1) if m else ''


def fetch_ementa(opener, doc_id):
    """Fetch case data from Solr via /ementa.php?id=..."""
    url = EMENTA + '?id=' + urllib.parse.quote(str(doc_id))
    req = urllib.request.Request(url, headers=EMENTA_HDRS)
    try:
        with opener.open(req, timeout=15) as r:
            data = json.loads(r.read().decode('utf-8', errors='replace'))
        docs = data.get('response', {}).get('docs', [])
        if docs:
            doc = docs[0]
            num_raw = doc.get('numero_processo', '')
            num = num20_to_cnj(num_raw) if num_raw else ''
            ementa = doc.get('ementa', '')
            rodape = doc.get('rodape_ementa', '')
            full_ementa = (ementa + ('\n\n' + rodape if rodape else '')).strip()[:800]
            return num, full_ementa
    except Exception:
        pass
    return '', ''


def get_page(opener, query, start, rows=20):
    """Fetch one page of results from /consulta.php."""
    params = urllib.parse.urlencode([
        ('q', query),
        ('start', str(start)),
        ('rows', str(rows)),
    ])
    url = SEARCH + '?' + params
    req = urllib.request.Request(url, headers=HEADERS)
    with opener.open(req, timeout=30) as r:
        html = r.read().decode('utf-8', errors='replace')
    return html


def parse_page_ids_and_meta(html):
    """Extract data-id values and any available metadata from HTML."""
    results = []
    # Find all unique data-id values (on any tag — buttons, divs, etc.)
    all_ids = list(dict.fromkeys(re.findall(r'data-id=["\']([^"\']+)["\']', html)))

    # Split by result container groups (around each data-id occurrence)
    id_to_block = {}
    for doc_id in all_ids:
        # Find where this ID appears and grab surrounding context (5000 chars)
        idx = html.find(f'data-id="{doc_id}"')
        if idx < 0:
            idx = html.find(f"data-id='{doc_id}'")
        block = html[max(0, idx - 2000):idx + 3000]
        id_to_block[doc_id] = block

    for doc_id, block in id_to_block.items():
        doc_id = doc_id

        clean = re.sub(r'<[^>]+>', ' ', block)
        clean = re.sub(r'\s+', ' ', clean).strip()

        relator_m = re.search(r'Relator[^:]*:\s*([A-ZÀ-Üa-zà-ü][^;:]{3,60}?)(?:\s*[;|]|\s+Órgão|\s+Câmara|\s+Data)', clean, re.IGNORECASE)
        camara_m = re.search(r'(?:Órgão|Câmara)[^:]*:\s*([^;:]{3,80}?)(?:\s*[;|]|\s+Relator|\s+Data)', clean, re.IGNORECASE)
        classe_m = re.search(r'Classe[^:]*:\s*([^;:]{3,80}?)(?:\s*[;|]|\s+Relator|\s+Data)', clean, re.IGNORECASE)
        date_m = re.search(r'(?:Julgamento|Data)[^:]*:\s*(\d{2}/\d{2}/\d{4})', clean, re.IGNORECASE)

        results.append({
            'id': doc_id,
            'relator': relator_m.group(1).strip() if relator_m else '',
            'camara': camara_m.group(1).strip() if camara_m else '',
            'classe': classe_m.group(1).strip() if classe_m else '',
            'processDate': date_m.group(1) if date_m else '',
        })
    return results


def main():
    QUERY = 'água abastecimento saneamento fornecimento'
    TARGET_YEARS = set(str(y) for y in range(2016, 2027))

    print('Starting TJTO scraper (full sweep, year filter from CNJ)...')
    opener = make_opener()
    all_cases = []
    seen = set()

    # First, get total count
    html0 = get_page(opener, QUERY, 0, 1)
    total_m = re.search(r'(\d+)\s+(?:result|julgado|acórd)', html0, re.IGNORECASE)
    total = int(total_m.group(1)) if total_m else 0
    print(f'Total results for query: {total}')

    rows_per_page = 20
    total_pages = max(1, (total + rows_per_page - 1) // rows_per_page)
    print(f'Pages to fetch: {total_pages}')

    for page in range(total_pages):
        start = page * rows_per_page
        print(f'  Page {page+1}/{total_pages} (start={start})...', end=' ', flush=True)

        try:
            html = get_page(opener, QUERY, start, rows_per_page)
        except Exception as e:
            print(f'ERR: {e}')
            time.sleep(5)
            continue

        items = parse_page_ids_and_meta(html)
        print(f'found {len(items)} items', end=' ')

        page_new = 0
        for item in items:
            doc_id = item['id']

            # Fetch ementa to get CNJ number and ementa text
            num, ementa = fetch_ementa(opener, doc_id)
            time.sleep(0.3)

            if not num:
                continue

            # Year filter
            year = year_from_cnj(num)
            if year not in TARGET_YEARS:
                continue

            if num in seen:
                continue
            seen.add(num)

            all_cases.append({
                'num': num,
                'processDate': item['processDate'],
                'publicDate': '',
                'classe': item['classe'],
                'relator': item['relator'],
                'camara': item['camara'],
                'comarca': '',
                'ementa': ementa,
                'tag': f'{year}-to',
                'court': 'TJTO',
                'state': 'TO',
            })
            page_new += 1

        print(f'→ {page_new} new cases (total {len(all_cases)})')

        # Save incrementally every 5 pages
        if page % 5 == 0:
            with open(OUT, 'w', encoding='utf-8') as f:
                json.dump(all_cases, f, ensure_ascii=False, indent=2)

        time.sleep(1)

    # Final save
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(all_cases, f, ensure_ascii=False, indent=2)

    print(f'\n=== DONE: {len(all_cases)} TJTO cases (2016-2026) ===')


if __name__ == '__main__':
    main()
