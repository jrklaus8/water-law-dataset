"""Register a research file as a Source record without sending it anywhere.

Stages 1-4 of the ingestion pipeline: identify, checksum, detect format and
accessibility, extract cheap deterministic metadata. Deeper stages (claims,
methods) are done by the researcher or the Research Mapper agent from this record.

  python3 pipelines/ingest/register_source.py PATH --title "..." --kind chapter \
      --copyright own_work_unpublished [--id SRC-CH2-DRAFT] [--private]

--private keeps the record's location as 'private' and never copies the file.
The source file is only read. Existing records are never overwritten.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import ROOT, sha256_file, write_json  # noqa: E402

TEXT = {".md": "markdown", ".txt": "text", ".csv": "csv", ".json": "json", ".bib": "bibtex", ".py": "python"}
KNOWN = {**TEXT, ".pdf": "pdf", ".docx": "docx", ".xlsx": "xlsx", ".ipynb": "jupyter"}
KINDS = ["thesis", "chapter", "article", "dataset", "code", "report", "legal_text", "other"]
COPY = ["own_work_open_licence", "own_work_unpublished", "third_party_open", "third_party_restricted", "unknown"]


def next_id(kind: str) -> str:
    n = len(list((ROOT / "research/sources").glob("SRC-*.json"))) + 1
    return f"SRC-{kind.upper()[:4]}-{n:03d}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--title", required=True)
    ap.add_argument("--kind", choices=KINDS, required=True)
    ap.add_argument("--copyright", choices=COPY, default="unknown")
    ap.add_argument("--licence", default="")
    ap.add_argument("--id")
    ap.add_argument("--private", action="store_true")
    a = ap.parse_args(argv)

    path = Path(a.path).resolve()
    if not path.is_file():
        sys.exit(f"not a file: {path}")
    sid = a.id or next_id(a.kind)
    if not re.fullmatch(r"SRC-[A-Z0-9-]+", sid):
        sys.exit("source id must look like SRC-ABC-001")
    out = ROOT / "research/sources" / f"{sid}.json"
    if out.exists():
        sys.exit(f"{out.name} exists; refusing to overwrite. Pick another --id.")

    fmt = KNOWN.get(path.suffix.lower(), "unknown")
    status, notes = "registered", "Registered only; no text extracted."
    if path.suffix.lower() in TEXT:
        try:
            text = path.read_text(encoding="utf-8")
            status = "text_extracted"
            notes = f"Read as UTF-8 text ({len(text.splitlines())} lines)."
        except UnicodeDecodeError:
            status, notes = "failed", "File is not valid UTF-8; extraction skipped. Do not rely on any derived text."
    elif fmt in {"pdf", "docx", "xlsx"}:
        notes = f"{fmt.upper()} registered. Extraction needs a parser that is not part of the initial build; page references cannot be preserved yet."

    record = {
        "schema_version": "1.0", "id": sid, "title": a.title, "kind": a.kind,
        "location": {"type": "private", "ref": "withheld"} if a.private else {"type": "repository_path", "ref": str(path)},
        "copyright_status": a.copyright, "checksum_sha256": sha256_file(path), "size_bytes": path.stat().st_size,
        "format": fmt, "extraction_status": status, "extraction_notes": notes,
        "provenance": {"imported_by": "register_source.py", "import_mode": "reference_only", "note": "File was read, never modified or copied."},
    }
    if a.licence:
        record["licence"] = a.licence
    write_json(out, record)
    print(f"registered {sid} ({fmt}, {record['size_bytes']} bytes, sha256 {record['checksum_sha256'][:12]}...)")
    return sid


if __name__ == "__main__":
    main()
