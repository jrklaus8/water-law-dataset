"""
TJPI (Tribunal de Justiça do Piauí) water law case scraper.
Portal: https://jurisprudencia.tjpi.jus.br/
System: Ruby on Rails app, HTML results, 25/page, date via data_min/data_max (YYYY-MM-DD).
"""
import os
import urllib.request, http.cookiejar, urllib.parse, re, json, time, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://jurisprudencia.tjpi.jus.br/'
SEARCH = BASE + 'jurisprudences/search'
OUT = os.path.join(os.getenv('OUTPUT_DIR', '.'), 'tjpi_cases_2016_2026.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,*/*',
    'Referer': BASE,
}


def make_opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(BASE, headers=HEADERS)
    with op.open(req, timeout=20) as r:
        pass
    return op


def extract_cases(html, tag):
    cases = []
    seen = set()

    # Each result card: look for card/result blocks with process number
    # Format: "Exibindo 1 - 25 de um total de 191 jurisprudência(s)"
    total_m = re.search(r'de um total de\s*<b>(\d+)</b>', html, re.IGNORECASE)
    if not total_m:
        total_m = re.search(r'total de\s+(\d+)\s+jurisprud', html, re.IGNORECASE)
    total = int(total_m.group(1)) if total_m else 0

    # CNJ case numbers
    cnj_all = re.findall(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', html)

    # Split by result cards — look for card divs
    # Typical: <div class="card ..."> or <tr> containing CNJ number
    blocks = re.split(r'(?=<(?:div|article|tr)[^>]*(?:card|result|jurisprud)[^>]*>)', html, flags=re.IGNORECASE)

    for block in blocks:
        cnj_nums = re.findall(r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', block)
        if not cnj_nums:
            continue
        num = cnj_nums[0]
        if num in seen:
            continue
        seen.add(num)

        clean = re.sub(r'<[^>]+>', ' ', block)
        clean = re.sub(r'\s+', ' ', clean).strip()

        # Extract fields from clean text
        relator_m = re.search(r'Relator[^:]*:\s*([A-ZÀ-Üa-zà-ü][^\n<]{3,60}?)(?:\s+(?:Órgão|Câmara|Data|Classe|Processo|\d))', clean, re.IGNORECASE)
        camara_m = re.search(r'(?:Órgão|Câmara)[^:]*:\s*([^\n<]{3,80}?)(?:\s+(?:Relator|Data|Classe|Processo|\d))', clean, re.IGNORECASE)
        classe_m = re.search(r'Classe[^:]*:\s*([^\n<]{3,80}?)(?:\s+(?:Relator|Data|Câmara|Órgão|Processo|\d))', clean, re.IGNORECASE)
        date_m = re.search(r'(?:Data|Julgamento|Publicação)[^:]*:\s*(\d{2}/\d{2}/\d{4})', clean, re.IGNORECASE)

        # Ementa: largest text block
        ementa = ''
        for em_m in re.finditer(r'<(?:div|p|span)[^>]*>([^<]{80,})', block):
            t = re.sub(r'<[^>]+>', '', em_m.group(1)).strip()
            if len(t) > len(ementa):
                ementa = t[:800]

        if not ementa:
            ementa = clean[:500]

        cases.append({
            'num': num,
            'processDate': date_m.group(1) if date_m else '',
            'publicDate': '',
            'classe': classe_m.group(1).strip() if classe_m else '',
            'relator': relator_m.group(1).strip() if relator_m else '',
            'camara': camara_m.group(1).strip() if camara_m else '',
            'comarca': '',
            'ementa': ementa,
            'tag': tag,
            'court': 'TJPI',
            'state': 'PI',
        })

    return cases, total


def search_year(opener, year, query, max_pages=20):
    d1 = f'{year}-01-01'
    d2 = f'{year}-12-31'
    tag = f'{year}-pi'
    all_cases = []
    seen = set()

    # Page 1
    params = urllib.parse.urlencode([
        ('q', query),
        ('data_min', d1),
        ('data_max', d2),
    ])
    url = SEARCH + '?' + params
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with opener.open(req, timeout=30) as r:
            html = r.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'  Error page 1: {e}')
        return []

    cases, total = extract_cases(html, tag)
    # Count pages from pagination
    pages_m = re.search(r'page=(\d+)[^"]*"\s*>(?:&raquo;|Última|&rsaquo;|[>»])', html, re.IGNORECASE)
    if not pages_m:
        # Find highest page number in pagination links
        page_nums = [int(x) for x in re.findall(r'[?&]page=(\d+)', html)]
        total_pages = max(page_nums) if page_nums else 1
    else:
        total_pages = int(pages_m.group(1))
    # Estimate from total if pagination not found
    if total_pages == 1 and total > 25:
        total_pages = (total + 24) // 25

    print(f'  {year}: {total} results, ~{total_pages} pages')

    for c in cases:
        if c['num'] not in seen:
            seen.add(c['num'])
            all_cases.append(c)

    # Pages 2+
    pages_to_fetch = min(total_pages, max_pages)
    for pg in range(2, pages_to_fetch + 1):
        time.sleep(2)
        params = urllib.parse.urlencode([
            ('q', query),
            ('data_min', d1),
            ('data_max', d2),
            ('page', str(pg)),
        ])
        url = SEARCH + '?' + params
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with opener.open(req, timeout=30) as r:
                page_html = r.read().decode('utf-8', errors='replace')
        except Exception as e:
            print(f'  Error page {pg}: {e}')
            break
        page_cases, _ = extract_cases(page_html, tag)
        new = 0
        for c in page_cases:
            if c['num'] not in seen:
                seen.add(c['num'])
                all_cases.append(c)
                new += 1
        print(f'    Page {pg}: {new} new (total {len(all_cases)})')

    return all_cases


def main():
    QUERY = 'água abastecimento saneamento fornecimento'
    print('Starting TJPI scraper...')
    opener = make_opener()
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
        print(f'  -> {new} new (total: {len(all_cases)})')
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(all_cases, f, ensure_ascii=False, indent=2)
        time.sleep(5)

    print(f'\n=== DONE: {len(all_cases)} TJPI cases ===')


if __name__ == '__main__':
    main()
