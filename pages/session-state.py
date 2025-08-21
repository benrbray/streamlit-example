import streamlit as st

st.markdown("""# Session Variables ([Read More](https://streamlit.lewagon.ai/))""")

unpersisted_variable = 0  # here is how a normal variable behaves for comparison

if "persisted_variable" not in st.session_state:
    st.session_state.persisted_variable = 0  # initialize the session state variable

if st.button("Increment"):
    unpersisted_variable += 1
    st.session_state.persisted_variable += 1

if st.button("Decrement"):
    unpersisted_variable -= 1
    st.session_state.persisted_variable -= 1

st.markdown("""
  ### Session state
  Below, we've printed the `session_state`:
  """)


st.write(st.session_state)

st.write(f"Unpersisted variable: {unpersisted_variable} 👈 the value does not take into account previous page reruns ⛔️")
st.write(f"Persisted variable: {st.session_state.persisted_variable} 👈 the data is persisted between reruns 👌")
st.write(f'Persisted variable: {st.session_state["persisted_variable"]}')