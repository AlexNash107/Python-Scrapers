from datetime import datetime
import pandas as pd
import numpy as np
import traceback
import sys


FLOAT_COLUMNS = [
    'Service Fee',
    'State Fee',
]


def convert_pivot_to_df(pivot):
    return pd.DataFrame(pivot.to_records())


def clean_values_to_expected_float(df):

    def convert_values(x):
        try:
            return float(x)
        except:
            return 0.0

    for col in FLOAT_COLUMNS:
        df[col] = df[col].apply(convert_values).astype(float)
    return df


class DMVAnalyzer:

    def __init__(self, df):
        self.raw_df = clean_values_to_expected_float(df)
        self.analysis_types = [
            'dmv_summary',
            'dmv_analysis',
            'dmv_nohit_orders'
        ]

    def dmv_summary(self):
        try:
            df = self.raw_df
            df['hits'] = df.result == 'hit'
            df['combined_cost'] = df['State Fee'] + df['Service Fee']
            pivot = df.pivot_table(
                index='state',
                values=['hits', 'combined_cost'],
                aggfunc={
                    'hits': [len, sum],
                    'combined_cost': sum
                }
            )
            df = convert_pivot_to_df(pivot)
            df.columns = ['state', 'total', 'hits', 'cost']
            df['cost_per_hit'] = (df.cost / df.hits).replace(np.inf, 0).apply(lambda x: round(x, 2))
            df['hit_rate'] = (df.hits / df.total).apply(lambda x: round(x, 2))
            df.hits = df.hits.astype(int)
            df.sort_values('state')
            return df
        except:
            traceback.print_exc()


    def dmv_analysis(self):
        try:
            df = self.raw_df
            df['state_charged'] = df['State Fee'] > 0
            pivot = df.pivot_table(
                index='reference',
                values=['state_charged', 'State Fee', 'Service Fee',],
                aggfunc={
                    'state_charged': [len, sum],
                    'State Fee': sum,
                    'Service Fee': sum,
                }
            )
            df = convert_pivot_to_df(pivot)
            df.columns = ['reference', 'adr_fee_paid', 'state_fee_paid', 'run_count', 'state_charged_count']
            df['state_fee_overcharge'] = ((df.state_fee_paid / df.state_charged_count) * (df.state_charged_count - 1)).fillna(0).apply(lambda x: round(x, 2))
            df.state_charged_count = df.state_charged_count.astype(int)
            df = df[['reference', 'run_count', 'state_charged_count', 'state_fee_paid', 'adr_fee_paid', 'state_fee_overcharge']]
        except:
            traceback.print_exc()
        return df


    def dmv_nohit_orders(self):
        try:
            df = self.raw_df
            df = df[df.result == 'nohit']
            pivot = df.pivot_table(
                index=['number', 'last name', 'reference'],
                values=['State Fee', 'Service Fee'],
                aggfunc={
                    'State Fee': [len, sum],
                    'Service Fee': sum,
                }
            )
            df = convert_pivot_to_df(pivot)
            df.columns = ['number', 'last name', 'reference', 'service_fee_total', 'times_run', 'state_fee_total']
            df = df[['number', 'last name', 'reference', 'times_run', 'state_fee_total', 'service_fee_total']]
        except:
            traceback.print_exc()
        return df


def run(filename):
    today = datetime.today().strftime('%m_%d')
    df = pd.read_csv(filename)
    Analyzer = DMVAnalyzer(df)
    for run in Analyzer.analysis_types:
        analyzed = getattr(Analyzer, run)()
        analyzed.to_csv(
            '{}_{}.csv'.format(run, today),
            index=False
        )


if __name__ == '__main__':
    args = sys.argv
    filename = args[1]
    run(filename)
