"""
Shared infrastructure for the court scrapers.

Standard library only (like the scrapers themselves). Provides:

* HTTP session setup (cookie jar, default headers)
* retry with exponential backoff for transient failures (timeouts, 429, 5xx,
  captcha / anti-bot interstitials)
* record schema validation and deduplication
* atomic JSON output with a dry-run mode
* a ScrapeReport that counts what was kept, rejected and failed, so a silent
  layout change shows up as numbers instead of an empty dataset.

Per-court scrapers subclass BaseScraper and only implement the parsing.
"""
import http.cookiejar
import json
import logging
import os
import re
import tempfile
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")

# Strings that mean "the server answered, but not with the data you asked for".
BLOCK_MARKERS = (
    "cf-chl-bypass",
    "cf-browser-verification",
    "Just a moment...",
    "g-recaptcha",
    "hcaptcha",
    "Attention Required! | Cloudflare",
)

RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})


class ScraperError(RuntimeError):
    """Base class for scraper failures."""


class FetchError(ScraperError):
    """A request failed permanently (after retries, or with a non-retryable status)."""


class BlockedError(FetchError):
    """The server returned a captcha / anti-bot page instead of data."""


class LayoutChangeError(ScraperError):
    """The page reports results but the parser found none: the markup probably changed."""


class ValidationError(ScraperError):
    """A record does not satisfy its schema."""


class RecordSchema:
    """Field rules for one scraped record type.

    required: must be a non-empty string; a record missing any is rejected.
    expected: should be non-empty; an empty value is kept but counted as a warning.
    optional: may be empty (e.g. fields a given court never publishes).
    date_fields: if non-empty, must match dd/mm/yyyy.
    """

    def __init__(
        self,
        required: Sequence[str],
        expected: Sequence[str] = (),
        optional: Sequence[str] = (),
        date_fields: Sequence[str] = (),
    ) -> None:
        self.required = tuple(required)
        self.expected = tuple(expected)
        self.optional = tuple(optional)
        self.date_fields = tuple(date_fields)

    @property
    def fields(self) -> Tuple[str, ...]:
        return self.required + self.expected + self.optional

    def check(self, record: Any) -> Tuple[List[str], List[str]]:
        """Return (errors, warnings) for a record without raising."""
        if not isinstance(record, Mapping):
            return ["record is not a mapping (%s)" % type(record).__name__], []

        errors: List[str] = []
        warnings: List[str] = []

        for name in self.fields:
            if name not in record:
                errors.append("missing key: %s" % name)
            elif not isinstance(record[name], str):
                errors.append("%s is not a string" % name)
        if errors:
            return errors, warnings

        for name in self.required:
            if not record[name].strip():
                errors.append("empty required field: %s" % name)
        for name in self.expected:
            if not record[name].strip():
                warnings.append("empty field: %s" % name)
        for name in self.date_fields:
            value = record[name].strip()
            if value and not DATE_RE.match(value):
                errors.append("bad date in %s: %r" % (name, value))
        return errors, warnings

    def validate(self, record: Any) -> Mapping:
        errors, _ = self.check(record)
        if errors:
            raise ValidationError("; ".join(errors))
        return record


# The record shape shared by every Brazilian court scraper in this repo.
CASE_SCHEMA = RecordSchema(
    required=("num", "ementa", "tag", "court", "state"),
    expected=("processDate", "classe", "relator", "camara"),
    optional=("publicDate", "comarca"),
    date_fields=("processDate", "publicDate"),
)


def deduplicate(records: Iterable[Mapping], key: str = "num") -> Tuple[List[Mapping], int]:
    """Drop repeated records by `key`, keeping the first. Returns (records, n_dropped)."""
    seen = set()
    kept: List[Mapping] = []
    dropped = 0
    for record in records:
        value = str(record.get(key, "")).strip()
        if not value:
            raise ValidationError("cannot deduplicate: record has no %r" % key)
        if value in seen:
            dropped += 1
            continue
        seen.add(value)
        kept.append(record)
    return kept, dropped


class ScrapeReport:
    """Counters for one scrape run, with a human-readable summary."""

    def __init__(self) -> None:
        self.kept = 0
        self.duplicates = 0
        self.rejected: Counter = Counter()
        self.warnings: Counter = Counter()
        self.failed_requests: List[str] = []
        self.failed_units: List[str] = []

    def reject(self, reasons: Iterable[str]) -> None:
        for reason in reasons:
            self.rejected[reason.split(":")[0]] += 1

    def warn(self, reasons: Iterable[str]) -> None:
        for reason in reasons:
            self.warnings[reason] += 1

    @property
    def ok(self) -> bool:
        return not self.failed_requests and not self.failed_units

    def summary(self) -> str:
        lines = ["kept=%d duplicates=%d rejected=%d" % (self.kept, self.duplicates, sum(self.rejected.values()))]
        for reason, n in self.rejected.most_common():
            lines.append("  rejected (%s): %d" % (reason, n))
        for reason, n in self.warnings.most_common():
            lines.append("  warning (%s): %d" % (reason, n))
        for unit in self.failed_units:
            lines.append("  FAILED: %s" % unit)
        for url in self.failed_requests:
            lines.append("  FAILED REQUEST: %s" % url)
        return "\n".join(lines)


def write_json_atomic(records: Sequence[Any], path: Path) -> None:
    """Write JSON via a temp file + rename, so an interrupted run cannot truncate earlier output."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(records, handle, ensure_ascii=False, indent=2)
        os.replace(tmp, str(path))
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


class BaseScraper:
    """Session, retries, logging, output and dry-run handling shared by all scrapers."""

    court = ""
    encoding = "utf-8"
    schema = CASE_SCHEMA

    def __init__(
        self,
        base_url: str,
        output_path: Optional[str] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: float = 30,
        max_retries: int = 3,
        backoff: float = 2.0,
        dry_run: bool = False,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self.base_url = base_url
        self.output_path = Path(output_path) if output_path else None
        self.headers = dict(headers or {})
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff
        self.dry_run = dry_run
        self._sleep = sleep
        self._opener: Optional[urllib.request.OpenerDirector] = None
        self.report = ScrapeReport()
        self.log = logging.getLogger(type(self).__name__)

    # --- HTTP -------------------------------------------------------------

    @property
    def opener(self) -> urllib.request.OpenerDirector:
        """Cookie-carrying opener, created lazily so constructing a scraper does no I/O."""
        if self._opener is None:
            jar = http.cookiejar.CookieJar()
            self._opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
        return self._opener

    def warm_up(self) -> None:
        """Load the landing page once so the session cookies are set."""
        self.fetch(self.base_url, headers={"X-Requested-With": None})

    def fetch(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, Optional[str]]] = None,
    ) -> str:
        """GET (or POST when `data` is given) and return decoded text.

        Retries timeouts, connection errors, HTTP 408/425/429/5xx and anti-bot
        pages with exponential backoff (honouring Retry-After). Other HTTP
        errors fail immediately. Raises FetchError when retries are exhausted.
        """
        merged = dict(self.headers)
        for key, value in (headers or {}).items():
            if value is None:
                merged.pop(key, None)
            else:
                merged[key] = value

        last: Optional[Exception] = None
        for attempt in range(self.max_retries + 1):
            delay = self.backoff * (2 ** attempt)
            try:
                request = urllib.request.Request(url, data=data, headers=merged)
                with self.opener.open(request, timeout=self.timeout) as response:
                    text = response.read().decode(self.encoding, errors="replace")
                self.check_response(text)
                return text
            except urllib.error.HTTPError as exc:
                if exc.code not in RETRYABLE_STATUS:
                    self.report.failed_requests.append("%s (HTTP %s)" % (url, exc.code))
                    raise FetchError("HTTP %s for %s" % (exc.code, url)) from exc
                last = exc
                retry_after = exc.headers.get("Retry-After") if exc.headers else None
                if retry_after and retry_after.isdigit():
                    delay = max(delay, float(retry_after))
            except BlockedError as exc:
                last = exc
            except (urllib.error.URLError, OSError) as exc:  # includes socket timeouts
                last = exc

            if attempt < self.max_retries:
                self.log.warning(
                    "attempt %d/%d failed for %s (%s); retrying in %.1fs",
                    attempt + 1, self.max_retries + 1, url, last, delay,
                )
                self._sleep(delay)

        self.report.failed_requests.append(url)
        self.log.error("giving up on %s after %d attempts: %s", url, self.max_retries + 1, last)
        raise FetchError("failed after %d attempts: %s (%s)" % (self.max_retries + 1, url, last)) from last

    def check_response(self, text: str) -> None:
        """Raise BlockedError for captcha / anti-bot pages. Subclasses may extend."""
        for marker in BLOCK_MARKERS:
            if marker in text:
                raise BlockedError("anti-bot page detected (%r)" % marker)

    # --- validation / dedup ----------------------------------------------

    def accept(self, record: Mapping) -> bool:
        """Validate a record against the schema and update the report. True if it should be kept."""
        errors, warnings = self.schema.check(record)
        if errors:
            self.report.reject(errors)
            self.log.warning("rejected %s: %s", record.get("num", "<no num>") if isinstance(record, Mapping) else "?",
                             "; ".join(errors))
            return False
        self.report.warn(warnings)
        return True

    def dedupe(self, records: Iterable[Mapping]) -> List[Mapping]:
        kept, dropped = deduplicate(records)
        self.report.duplicates += dropped
        return kept

    # --- output -----------------------------------------------------------

    def save(self, records: Sequence[Mapping]) -> None:
        """Write records to output_path, or only log what would be written in dry-run mode."""
        if self.output_path is None:
            raise ScraperError("no output path configured")
        if self.dry_run:
            self.log.info("[dry-run] would write %d records to %s", len(records), self.output_path)
            return
        write_json_atomic(list(records), self.output_path)
        self.log.info("wrote %d records to %s", len(records), self.output_path)

    def check_output_dir(self) -> None:
        """Fail before scraping (not after hours of it) if the output location is unusable."""
        if self.output_path is None or self.dry_run:
            return
        parent = self.output_path.resolve().parent
        try:
            parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise ScraperError("cannot create output directory %s: %s" % (parent, exc)) from exc
        if not os.access(str(parent), os.W_OK):
            raise ScraperError("output directory is not writable: %s" % parent)


def preview(records: Sequence[Mapping], n: int = 3) -> str:
    """Compact preview of the first n records for dry-run output."""
    shown: List[Dict[str, Any]] = []
    for record in records[:n]:
        shown.append({k: (v[:80] + "...") if isinstance(v, str) and len(v) > 80 else v for k, v in record.items()})
    return json.dumps(shown, ensure_ascii=False, indent=2)
