#!/usr/bin/env python
'''
My data dashboard for stock ticker with Streamlit.
Source reference:
https://github.com/jkanner/streamlit-dataview/blob/master/app.py
with the website:
https://share.streamlit.io/jkanner/streamlit-dataview/master/app.py/+/
'''

from datetime import date, datetime
from dotenv import load_dotenv
import os
import pandas as pd
import requests
import streamlit as st

class MyTickerDashboard:
    def __init__(self) -> None:
        self.main_layout()
        self.sidebar_layout()
    
        self.render_result()

    @st.cache
    def get_data(self):
        load_dotenv()
        API_URL = 'https://www.alphavantage.co/query'
        symbol = self.selected_stock

        data = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'datatype': 'json',
        'apikey': os.getenv('APIKEY')}

        response = requests.get(API_URL, data)
        response_json = response.json() # maybe redundant

        return pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)

    def main_layout(self):
        '''
        Method to layout the main window for visualizing data.
        '''
        st.set_page_config(page_title='Shih-Kai\'s Milestone Project')
        # Title the app
        st.title('Stock Ticker in the Past Month')

        st.markdown('''
        ## Shih-Kai Lin's Milestone Project
        * Use the menu at left to select data
        * Your plots will appear below
        ''')

    def render_result(self):
        st.table(self.df)

    def sidebar_layout(self):
        st.sidebar.markdown('# Select plot parameters:')
        #-- Set ticker
        # For a list of available tickers, here is what I find for an answer.
        # https://stackoverflow.com/questions/45447172/is-there-a-source-to-find-a-list-of-symbols
        df_sym = pd.read_csv('data/nasdaq_screener_1624404893542.csv')
        stock_list = list(df_sym.Symbol)
        self.selected_stock = st.sidebar.selectbox('Ticker (e.g. AAPL):',
                                                   stock_list,
                                                   index=stock_list.index('AMZN'))
        
        # select year
        self.selected_year = st.sidebar.selectbox('Year:',
                                                  list(reversed(range(2010, date.today().year+1))))
        
        # select month
        month_list = [datetime(1900, mint, 1).strftime('%B') for mint in range(1, 13)]
        self.selected_month = st.sidebar.selectbox('Month:',
                                                   month_list,
                                                   index=month_list.index(date.today().strftime('%B')))

        # retrieve data
        self.df = self.get_data()

if __name__ == '__main__':
    my_dashboard = MyTickerDashboard()