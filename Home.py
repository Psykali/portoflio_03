import streamlit as st
from pathlib import Path

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# 🧠 Intro Header
st.markdown("""
<div style='text-align: center; padding-top: 2em;'>
    <h1 style='font-size: 42px;'>👋 Hi, I'm <span style='color:#278ea5;'>S. Khalifa</span></h1>
    <h3 style='margin-top: -10px;'>Data Scientist & DevOps Engineer</h3>
    <p style='font-size: 18px; color: #aaa; max-width: 600px; margin: auto;'>I solve real-world problems using machine learning, automation, and scalable cloud infrastructure. Currently focused on AI agents, predictive systems, and DevOps engineering.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 🏷️ Badge Tags
st.markdown("""
<div style='text-align: center; font-size: 16px;'>
    🧠 AI & ML • ☁️ Azure Cloud • 🔧 FastAPI & Terraform • 📊 Streamlit Dashboards
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("""
<div style='text-align: center; margin-top: 2em;'>
    <p style='font-size:18px; color:#278ea5;'>📬 Email me directly at</p>
</div>
""", unsafe_allow_html=True)
# 🔗 Socials and CV
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-red?style=for-the-badge&logo=gmail)](mailto:siefkhalefa@gmail.com)", unsafe_allow_html=True)
with col2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sief-m-khalifa/)", unsafe_allow_html=True)
with col3:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/Psykali)", unsafe_allow_html=True)
with col4:
    st.markdown("[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium)](https://medium.com/@SKpsyktechdynamo)", unsafe_allow_html=True)
with col5:
    with open("assets/S_KHALIFA-CV.pdf", "rb") as f:
        st.download_button("📄 Download CV", f, file_name="S_KHALIFA-CV.pdf")


# 🚀 Featured Work Preview
st.markdown("## 🚀 Featured Work")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/project_imgs/jsi_stock.png", use_column_width=True)
    st.markdown(
        "[**JSI Stock Forecasting**](#projects)",
        unsafe_allow_html=True
    )

with col2:
    st.image("assets/project_imgs/revit_api.png", use_column_width=True)
    st.markdown(
        "[**Revit + FastAPI Integration**](#projects)",
        unsafe_allow_html=True
    )

with col3:
    st.image("assets/project_imgs/azure_terraform.png", use_column_width=True)
    st.markdown(
        "[**DevOps Infra Automation**](#projects)",
        unsafe_allow_html=True
    )


# CTA Footer
st.markdown("""
<div style='text-align: center; padding-top: 1.5em; color: #888; font-size: 16px;'>
    Let’s build something awesome together. 🚀
</div>
""", unsafe_allow_html=True)
