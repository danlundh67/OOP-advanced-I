import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px

def read_data():
    data_path=Path(__file__).parents[1] / "data"
    df=pd.read_csv(data_path / "cleaned_yh_region.csv", index_col=0, parse_dates=[0])
    df.index=df.index.year
    return df

#print(read_data()) 

def layout():
    df=read_data()
    st.markdown("# YH dashboard")
    st.dataframe(df)

# __name__ is a special variable, which is equal to __main__ when we run this script
#  when we import this somewhere else, __name__ is the script name

if __name__ == '__main__':
    layout()