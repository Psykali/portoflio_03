import streamlit as st
from pathlib import Path

st.set_page_config(page_title="S. Khalifa Portfolio", layout="wide")

st.sidebar.title("Navigate")
page = st.sidebar.radio("", ["Home", "Projects", "About", "Contact"])

if page == "Home":
    import Home
elif page == "Projects":
    import Projects
elif page == "About":
    import About
elif page == "Contact":
    import Contact
