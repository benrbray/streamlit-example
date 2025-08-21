import streamlit as st
import requests
import numpy as np

st.markdown("# Giphy API")

query = st.text_input("Enter a search query for the `giphy` API:")

url = "https://api.giphy.com/v1/gifs/search"
params = {
    "api_key" : st.secrets.api_key,
    "q": query
}
response = requests.get(url=url, params=params).json()

while not query:
    st.stop()
    
gif_data = response["data"][np.random.randint(0,10)]
gif_url = gif_data["images"]["original"]["url"]

st.markdown("### Method 1")
st.markdown(f"![]({gif_url})")

st.markdown("### Method 2")
st.write(f'<img height=600 src="{gif_url}"/>', unsafe_allow_html=True)

st.markdown("### JSON Data")
with st.expander(label="Expand Me!"):
    st.write(gif_data)