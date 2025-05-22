import streamlit as st
import requests
import numpy as np

st.markdown("# Giphy API")

query = st.text_input("Enter a search query for the `giphy` API:")

url = "https://api.giphy.com/v1/gifs/search"
params = { "api_key" : st.secrets.api_key, "q": query }
response = requests.get(url=url, params=params).json()

while not query:
    st.stop()
    
gif_data = response["data"][np.random.randint(0,10)]
gif_url = gif_data["images"]["original"]["url"]

# st.write(gif_data)

st.markdown(f"![]({gif_url})")