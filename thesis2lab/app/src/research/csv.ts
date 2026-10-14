import type { DatasetVariable, Row } from './types'

/** Minimal RFC 4180 parser (quoted fields, escaped quotes, CRLF). */
export function parseCsv(text: string): string[][] {
  const out: string[][] = []
  let row: string[] = []
  let field = ''
  let quoted = false
  const src = text.replace(/^﻿/, '')
  for (let i = 0; i < src.length; i++) {
    const c = src[i]
    if (quoted) {
      if (c === '"') {
        if (src[i + 1] === '"') { field += '"'; i++ } else quoted = false
      } else field += c
    } else if (c === '"') quoted = true
    else if (c === ',') { row.push(field); field = '' }
    else if (c === '\n' || c === '\r') {
      if (c === '\r' && src[i + 1] === '\n') i++
      row.push(field); field = ''
      if (row.length > 1 || row[0] !== '') out.push(row)
      row = []
    } else field += c
  }
  if (field !== '' || row.length) { row.push(field); out.push(row) }
  return out
}

/** Parse CSV into typed rows, failing loudly when the file disagrees with the dataset record. */
export function loadRows(text: string, variables: DatasetVariable[]): Row[] {
  const [header, ...body] = parseCsv(text)
  if (!header) throw new Error('CSV is empty')
  const names = variables.map((v) => v.name)
  if (header.length !== names.length || header.some((h, i) => h !== names[i])) {
    throw new Error(`CSV columns [${header.join(', ')}] do not match dataset record [${names.join(', ')}]`)
  }
  return body.map((cells, r) => {
    if (cells.length !== header.length) throw new Error(`Row ${r + 2} has ${cells.length} cells, expected ${header.length}`)
    const row: Row = {}
    variables.forEach((v, i) => {
      if (v.type === 'integer' || v.type === 'number') {
        const n = Number(cells[i])
        if (cells[i] === '' || Number.isNaN(n)) throw new Error(`Row ${r + 2}: "${cells[i]}" is not numeric for ${v.name}`)
        row[v.name] = n
      } else row[v.name] = cells[i]
    })
    return row
  })
}

export function toCsv(rows: Row[], columns: string[]): string {
  const esc = (v: string | number) => {
    const s = String(v)
    return /[",\n\r]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s
  }
  return [columns.join(','), ...rows.map((r) => columns.map((c) => esc(r[c] ?? '')).join(','))].join('\n') + '\n'
}
