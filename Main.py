import streamlit as st
from pathlib import Path

st.set_page_config(page_title="S. Khalifa Portfolio", page_icon="📌", layout="wide")

st.sidebar.title("Navigate")
page = st.sidebar.radio("", ["Home", "Projects"])


if page == "Home":
    import Home
elif page == "Projects":
    import Projects
# if page == "Home":
#     exec(open("01-Home.py").read())
# elif page == "Projects":
#     exec(open("02-Projects.py").read())
