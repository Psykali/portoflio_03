import streamlit as st
from pathlib import Path
## import Home
## import Projects

st.set_page_config(page_title="S. Khalifa Portfolio", page_icon="📌", layout="wide")

st.sidebar.title("Navigate")
page = st.sidebar.radio("", ["Home", "Projects"])


# if page == "Home":
#     import 01-Home
# elif page == "Projects":
#     import 02-Projects
if page == "Home":
    exec(open("pages/01-Home.py").read())
elif page == "Projects":
    exec(open("pages/02-Projects.py").read())
