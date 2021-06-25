#!/usr/bin/env python

from datetime import date, datetime
import pandas as pd

def get_all_ticker_symbols(infpn):
    df_sym = pd.read_csv(infpn)
    print(list(df_sym.Symbol))

if __name__ == '__main__':
    # get_all_ticker_symbols('../data/nasdaq_screener_1624404893542.csv')
    # print([datetime(1900, mint, 1).strftime('%B') for mint in range(1, 13)])
    print(date.today().strftime('%B'))
