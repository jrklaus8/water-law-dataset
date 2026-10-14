import { BarList, ColumnChart, DataTable, IntervalPlot } from '../charts/Charts'
import type { ExperimentManifest, RunResult } from '../research/types'

type View = (props: { m: ExperimentManifest; result: RunResult }) => React.ReactElement

const num = (v: unknown) => (typeof v === 'number' ? v : null)

const DescriptiveView: View = ({ m, result }) => {
  const cfg = (m.runner_config ?? {}) as { category_variables?: string[] }
  const byYear = result.tables.find((t) => t.id === 'by_year')
  const total = num(result.metrics.n_selected) ?? 0
  return (
    <>
      <ColumnChart title="Records per year" xLabel="year" yLabel="records" points={(byYear?.rows ?? []).map((r) => ({ label: String(r[0]), value: Number(r[1]) }))} />
      <div className="grid-2">
        {(cfg.category_variables ?? []).map((v) => {
          const t = result.tables.find((x) => x.id === `by_${v}`)
          return <BarList key={v} title={`By ${v}`} total={total} points={(t?.rows ?? []).map((r) => ({ label: String(r[0]), value: Number(r[1]) }))} />
        })}
      </div>
    </>
  )
}

const AgreementView: View = ({ result }) => {
  const per = result.tables.find((t) => t.id === 'per_category')!
  const conf = result.tables.find((t) => t.id === 'confusion')!
  return (
    <>
      <IntervalPlot title="Cohen's kappa with 95% bootstrap interval" value={num(result.metrics.cohen_kappa)} low={num(result.metrics.ci_low)} high={num(result.metrics.ci_high)} />
      <DataTable caption={conf.title} columns={conf.columns} rows={conf.rows} />
      <DataTable caption={per.title} columns={per.columns} rows={per.rows} />
    </>
  )
}

const Generic: View = ({ result }) => <>{result.tables.map((t) => <DataTable key={t.id} caption={t.title} columns={t.columns} rows={t.rows} />)}</>

const VIEWS: Record<string, View> = { descriptive_table: DescriptiveView, coder_agreement: AgreementView }
export const viewFor = (runner: string | null): View => (runner && VIEWS[runner]) || Generic
