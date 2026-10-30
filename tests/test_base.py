import io
import json
import urllib.error

import pytest

from scrapers.base import (
    CASE_SCHEMA,
    BaseScraper,
    FetchError,
    ScraperError,
    ValidationError,
    deduplicate,
    preview,
    write_json_atomic,
)


def make_record(**overrides):
    record = {
        'num': '1', 'processDate': '01/02/2024', 'publicDate': '', 'classe': 'A', 'relator': 'R',
        'camara': 'C', 'comarca': '', 'ementa': 'Ementa text', 'tag': '2024-sc', 'court': 'TJSC', 'state': 'SC',
    }
    record.update(overrides)
    return record


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


class FakeOpener:
    """Replays a scripted list of results: bytes -> response, Exception -> raised."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = 0

    def open(self, request, timeout=None):
        self.calls += 1
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        return FakeResponse(item)


def make_scraper(script, **kwargs):
    sleeps = []
    scraper = BaseScraper('http://example.test/', sleep=sleeps.append, **kwargs)
    scraper._opener = FakeOpener(script)
    return scraper, sleeps


def http_error(code, headers=None):
    return urllib.error.HTTPError('http://example.test/', code, 'err', headers or {}, None)


# --- schema ---------------------------------------------------------------

def test_valid_record_passes():
    assert CASE_SCHEMA.check(make_record()) == ([], [])


def test_empty_publicdate_and_comarca_are_allowed():
    # TJSC never publishes these; they must not cause rejection.
    errors, warnings = CASE_SCHEMA.check(make_record(publicDate='', comarca=''))
    assert errors == [] and warnings == []


def test_missing_required_field_is_error():
    errors, _ = CASE_SCHEMA.check(make_record(num='  '))
    assert errors == ['empty required field: num']


def test_empty_expected_field_is_warning_not_error():
    errors, warnings = CASE_SCHEMA.check(make_record(relator='', camara=''))
    assert errors == []
    assert warnings == ['empty field: relator', 'empty field: camara']


def test_bad_date_is_error():
    errors, _ = CASE_SCHEMA.check(make_record(processDate='2024-02-01'))
    assert errors and errors[0].startswith('bad date in processDate')


def test_missing_key_and_wrong_type():
    record = make_record()
    del record['court']
    record['tag'] = 5
    errors, _ = CASE_SCHEMA.check(record)
    assert 'missing key: court' in errors and 'tag is not a string' in errors


def test_non_mapping_record():
    errors, _ = CASE_SCHEMA.check(['x'])
    assert errors


def test_validate_raises():
    with pytest.raises(ValidationError):
        CASE_SCHEMA.validate(make_record(ementa=''))


# --- dedup ----------------------------------------------------------------

def test_deduplicate_keeps_first_and_counts():
    a, b = make_record(num='1', ementa='first'), make_record(num='1', ementa='second')
    kept, dropped = deduplicate([a, b, make_record(num='2')])
    assert [r['num'] for r in kept] == ['1', '2']
    assert kept[0]['ementa'] == 'first'
    assert dropped == 1


def test_deduplicate_rejects_keyless_record():
    with pytest.raises(ValidationError):
        deduplicate([make_record(num='')])


# --- fetch / retry --------------------------------------------------------

def test_fetch_returns_decoded_text():
    scraper, _ = make_scraper(['Órgão'.encode('utf-8')])
    assert scraper.fetch('http://example.test/') == 'Órgão'


def test_fetch_retries_transient_errors_with_exponential_backoff():
    script = [http_error(503), urllib.error.URLError('reset'), b'ok']
    scraper, sleeps = make_scraper(script, backoff=2.0)
    assert scraper.fetch('http://example.test/') == 'ok'
    assert sleeps == [2.0, 4.0]


def test_fetch_honours_retry_after_on_429():
    scraper, sleeps = make_scraper([http_error(429, {'Retry-After': '30'}), b'ok'], backoff=1.0)
    scraper.fetch('http://example.test/')
    assert sleeps == [30.0]


def test_fetch_does_not_retry_404():
    scraper, sleeps = make_scraper([http_error(404), b'never reached'])
    with pytest.raises(FetchError):
        scraper.fetch('http://example.test/')
    assert scraper._opener.calls == 1 and sleeps == []
    assert scraper.report.failed_requests == ['http://example.test/ (HTTP 404)']


def test_fetch_gives_up_after_max_retries():
    scraper, sleeps = make_scraper([TimeoutError('t')] * 3, max_retries=2)
    with pytest.raises(FetchError):
        scraper.fetch('http://example.test/')
    assert scraper._opener.calls == 3 and len(sleeps) == 2
    assert scraper.report.failed_requests == ['http://example.test/']


def test_fetch_treats_captcha_page_as_retryable_block():
    blocked = b'<title>Just a moment...</title>'
    scraper, sleeps = make_scraper([blocked, b'real data'])
    assert scraper.fetch('http://example.test/') == 'real data'
    assert len(sleeps) == 1


def test_fetch_persistent_captcha_fails():
    scraper, _ = make_scraper([b'g-recaptcha'] * 2, max_retries=1)
    with pytest.raises(FetchError):
        scraper.fetch('http://example.test/')


# --- output ---------------------------------------------------------------

def test_dry_run_writes_nothing(tmp_path):
    out = tmp_path / 'sub' / 'out.json'
    scraper = BaseScraper('http://example.test/', output_path=str(out), dry_run=True)
    scraper.save([make_record()])
    assert not out.exists() and not out.parent.exists()


def test_save_writes_utf8_json(tmp_path):
    out = tmp_path / 'sub' / 'out.json'
    scraper = BaseScraper('http://example.test/', output_path=str(out))
    scraper.save([make_record(relator='João')])
    assert json.loads(out.read_text(encoding='utf-8'))[0]['relator'] == 'João'
    assert [p.name for p in out.parent.iterdir()] == ['out.json']  # no temp file left behind


def test_atomic_write_keeps_old_file_on_failure(tmp_path):
    out = tmp_path / 'out.json'
    write_json_atomic([{'a': 1}], out)
    with pytest.raises(TypeError):
        write_json_atomic([{'a': object()}], out)
    assert json.loads(out.read_text()) == [{'a': 1}]
    assert [p.name for p in tmp_path.iterdir()] == ['out.json']


def test_save_without_output_path_raises():
    with pytest.raises(ScraperError):
        BaseScraper('http://example.test/').save([])


def test_check_output_dir_fails_loudly(tmp_path):
    blocker = tmp_path / 'file'
    blocker.write_text('x')
    scraper = BaseScraper('http://example.test/', output_path=str(blocker / 'out.json'))
    with pytest.raises(ScraperError):
        scraper.check_output_dir()


def test_preview_truncates_long_values():
    assert '...' in preview([make_record(ementa='x' * 500)])
