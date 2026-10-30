import json
import logging
import os
import time
import urllib.error
import urllib.request
import http.cookiejar
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional


logger = logging.getLogger(__name__)


class ScraperError(RuntimeError):
    """Base scraper exception."""


class ValidationError(ScraperError):
    """Raised when a scraped record does not meet the expected schema."""


DEFAULT_REQUIRED_FIELDS = (
    "num",
    "processDate",
    "publicDate",
    "classe",
    "relator",
    "camara",
    "comarca",
    "ementa",
    "tag",
    "court",
    "state",
)


class BaseScraper:
    """Shared scraper functionality for website-based judicial data collection."""

    def __init__(
        self,
        *,
        base_url: str,
        output_path: Optional[str] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: int = 30,
        max_retries: int = 3,
        backoff_seconds: float = 1.0,
        dry_run: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.output_path = Path(output_path) if output_path else None
        self.headers = dict(headers or {})
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_seconds = backoff_seconds
        self.dry_run = dry_run
        self.logger = logging.getLogger(self.__class__.__name__)

    def make_opener(self):
        cookie_jar = http.cookiejar.CookieJar()
        return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

    def open_url(
        self,
        url: str,
        *,
        opener=None,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[int] = None,
        method: Optional[str] = None,
    ) -> bytes:
        resolved_headers = {**self.headers, **(headers or {})}
        request_method = method or ("POST" if data is not None else "GET")
        request = urllib.request.Request(url, data=data, headers=resolved_headers, method=request_method)

        attempt = 0
        while True:
            try:
                current_opener = opener or self.make_opener()
                with current_opener.open(request, timeout=timeout or self.timeout) as response:
                    return response.read()
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt >= self.max_retries:
                    self.logger.exception("Request failed for %s after %d attempts", url, attempt + 1)
                    raise ScraperError(f"Request failed for {url}: {exc}") from exc
                wait_time = self.backoff_seconds * (attempt + 1)
                self.logger.warning(
                    "Request to %s failed (attempt %d/%d). Retrying in %.1f seconds",
                    url,
                    attempt + 1,
                    self.max_retries + 1,
                    wait_time,
                )
                time.sleep(wait_time)
                attempt += 1

    @staticmethod
    def validate_case_record(record: Mapping[str, Any], required_fields: Iterable[str] = DEFAULT_REQUIRED_FIELDS) -> MutableMapping[str, Any]:
        if not isinstance(record, Mapping):
            raise ValidationError(f"Record is not a mapping: {type(record).__name__}")

        missing = []
        for field in required_fields:
            value = record.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                missing.append(field)

        if missing:
            raise ValidationError(f"Missing required fields: {', '.join(missing)}")

        return dict(record)

    @staticmethod
    def deduplicate_records(records: Iterable[Mapping[str, Any]], key_field: str = "num") -> List[MutableMapping[str, Any]]:
        seen = set()
        deduped: List[MutableMapping[str, Any]] = []
        for record in records:
            if not isinstance(record, Mapping):
                raise ValidationError(f"Record is not a mapping: {type(record).__name__}")

            key = str(record.get(key_field, "")).strip()
            if not key:
                raise ValidationError(f"Record missing required key '{key_field}'")

            if key in seen:
                continue
            seen.add(key)
            deduped.append(dict(record))
        return deduped

    def maybe_write_json(self, records: Iterable[Mapping[str, Any]], path: Optional[str] = None) -> Path:
        target = Path(path or self.output_path)
        if target is None:
            raise ValueError("No output path provided")

        if self.dry_run:
            self.logger.info("Dry-run enabled; would write %d records to %s", len(list(records)), target)
            return target

        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8") as handle:
            json.dump(list(records), handle, ensure_ascii=False, indent=2)
        self.logger.info("Wrote %d records to %s", len(list(records)), target)
        return target

    def load_existing_records(self, path: Optional[str] = None) -> List[MutableMapping[str, Any]]:
        target = Path(path or self.output_path)
        if target is None or not target.exists():
            return []

        with target.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        if not isinstance(data, list):
            raise ScraperError(f"Expected a JSON array in {target}")
        return [dict(item) for item in data]


path: "scrapers/__init__.py",
content: """Shared scraper utilities and site-specific scrapers for the water law dataset."""

"""
},{