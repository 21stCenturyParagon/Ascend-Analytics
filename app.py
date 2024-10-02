import os
from dotenv import load_dotenv

import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
from streamlit_gsheets import GSheetsConnection
import pandas as pd
load_dotenv(dotenv_path='venv/.env')


st.set_page_config(layout="wide")
st.title('Ascend Analytics')
df = pd.read_csv('Ascend Pro League - Leaderboard.csv')

new_dfs, code = spreadsheet(df)
code = code if code else "# Edit the spreadsheet above to generate code"
st.code(code)
# st.code(code)