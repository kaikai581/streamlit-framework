#!/usr/bin/env python
'''
My data dashboard for stock ticker with Streamlit.
Source reference:
https://github.com/jkanner/streamlit-dataview/blob/master/app.py
with the website:
https://share.streamlit.io/jkanner/streamlit-dataview/master/app.py/+/
'''

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
        * Use the menu at left to select data and set plot parameters
        * Your plots will appear below
        ''')

    def sidebar_layout(self):
        st.sidebar.markdown('# Select plot parameters:')
        #-- Set ticker
        # For a list of available tickers, here is what I find for an answer.
        # https://stackoverflow.com/questions/45447172/is-there-a-source-to-find-a-list-of-symbols
        select_event = st.sidebar.selectbox('Ticker (e.g. AAPL):',
                                            ['By event name', 'By GPS'])

if __name__ == '__main__':
    my_dashboard = MyTickerDashboard()