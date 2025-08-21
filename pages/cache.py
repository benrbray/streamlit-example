import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
  print("Reading data from file....")
  data_df = pd.read_csv("raw_data/example.csv")
  st.markdown("# Loaded CSV from File!")
  return data_df

df = load_data()
st.dataframe(df)

# slider
st.markdown("# Slider")
st.markdown("This slider's only purpose is to refresh the page :)")
line_count = st.slider('Select a line count', 1, 10, 3)
st.write(f"Line Count: {line_count}")