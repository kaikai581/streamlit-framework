#!/usr/bin/env python
'''
My data dashboard for stock ticker with Streamlit.
Source reference:
https://github.com/jkanner/streamlit-dataview/blob/master/app.py
with the website:
https://share.streamlit.io/jkanner/streamlit-dataview/master/app.py/+/
'''

from datetime import date, datetime
import pandas as pd
import requests
import streamlit as st

class MyTickerDashboard:
    def __init__(self) -> None:
        self.main_layout()
        self.sidebar_layout()
    
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
                                                  list(reversed(range(2010, date.today().year))))
        
        # select month
        month_list = [datetime(1900, mint, 1).strftime('%B') for mint in range(1, 13)]
        self.selected_month = st.sidebar.selectbox('Month:',
                                                   month_list,
                                                   index=month_list.index(date.today().strftime('%B')))

if __name__ == '__main__':
    my_dashboard = MyTickerDashboard()