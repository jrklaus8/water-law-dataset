"""Load selected top-level definitions of a script WITHOUT running its top-level code.

Several scrapers and utilities in this repository have no ``if __name__ == "__main__"`` guard: importing them would start
a collection run, open network connections or read files from a path on the author's machine. To test their pure helper
functions offline, this module parses a script, keeps only side-effect-free top-level statements (imports of standard-library
modules with no side effects, function definitions, and plain assignments whose right-hand side calls nothing but a small
allow-list such as ``re.compile``), and executes those in a fresh namespace. Everything else (network calls, file reads,
``sys.stdout`` changes, ``pandas`` work) is skipped, never executed.

This is a testing aid, not a substitute for refactoring the scripts behind a ``main()``; see docs/audit-report.md.
Works on Python 3.8 and later.
"""
import ast
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SAFE_MODULES = {'re', 'os', 'sys', 'json', 'time', 'csv', 'math', 'datetime', 'collections', 'pathlib', 'html', 'unicodedata', 'itertools', 'string', 'typing',
                'urllib', 'ssl', 'http', 'hashlib', 'copy', 'functools'}
SAFE_CALLS = {'re.compile', 'set', 'frozenset', 'dict', 'list', 'tuple', 'str', 'int', 'float', 'len', 'sorted', 'range', 'sum', 'max', 'min',
              'Path', 'pathlib.Path', 'os.getenv', 'os.environ.get', 'os.path.join', 'Counter', 'collections.Counter'}
SAFE_METHODS = {'lower', 'upper', 'strip', 'split', 'join', 'format', 'replace', 'startswith', 'endswith', 'items', 'keys', 'values', 'get', 'title'}


def _dotted(node):
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return '.'.join(reversed(parts))
    return None


def _safe_value(node):
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            name = _dotted(n.func)
            if name in SAFE_CALLS:
                continue
            if isinstance(n.func, ast.Attribute) and n.func.attr in SAFE_METHODS:
                continue
            return False
        if isinstance(n, (ast.Await, ast.Yield, ast.YieldFrom)):
            return False
    return True


def _filter_import(node):
    """Keep only the safe names of an import statement (``import os, sys, pandas`` keeps os and sys); None if nothing is safe."""
    if isinstance(node, ast.Import):
        names = [a for a in node.names if a.name.split('.')[0] in SAFE_MODULES]
        return ast.Import(names=names) if names else None
    return node if (node.module or '').split('.')[0] in SAFE_MODULES and node.level == 0 else None


def load(relative_path):
    """Return a namespace holding the safe top-level definitions of ``relative_path`` (relative to the repository root)."""
    path = ROOT / relative_path
    tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    kept = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            node = _filter_import(node)
            if node is not None:
                kept.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            kept.append(node)
        elif isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) for t in node.targets) and _safe_value(node.value):
            kept.append(node)
    ns = {'__name__': 'safe_loaded_' + path.stem, '__file__': str(path), '__skipped__': []}
    for node in kept:
        module = ast.Module(body=[node], type_ignores=[])
        ast.fix_missing_locations(module)
        try:
            exec(compile(module, str(path), 'exec'), ns)
        except Exception as exc:  # an assignment that needs a name from skipped code (a DataFrame, an HTTP response): leave it undefined
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                raise
            ns['__skipped__'].append((getattr(node, 'lineno', 0), type(exc).__name__))
    return ns
