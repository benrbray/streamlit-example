import streamlit as st

import numpy as np
import pandas as pd
import random

st.markdown("""# This is a header
## This is a sub header
Updates automatically!
Be careful about long-running calculations!

```python
this is python code
live updating
```

This is text""")

st.markdown("### Images & Buttons")

st.markdown("Click the button to load an image from the `raw_data` folder!")

if st.button("Click Me!"):
    st.image("raw_data/lewagon.png")

st.markdown("### Random Number")

st.markdown("""
    The following is a random number.  It will change every time Streamlit re-executes the page!
            """)

st.write(random.random())

st.markdown("### Dataframes")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
