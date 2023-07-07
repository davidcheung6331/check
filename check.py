import streamlit as st
import pandas as pd
import streamlit_pandas as sp



file = "purchase-orders.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

df = load_data()
st.write(df)

