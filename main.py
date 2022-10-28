from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from gsheetsdb import connect

conn = connect()
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

for row in rows:
    st.write(f"{row.grade}")

