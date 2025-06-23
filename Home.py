import streamlit as st
from pathlib import Path

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# 1. HEADLINE SECTION
st.markdown("""
<div style='text-align: center; padding-top: 2em;'>
    <h1 style='font-size: 42px;'>👋 Hi, I'm <span style='color:#278ea5;'>S. Khalifa</span></h1>
    <h3 style='margin-top: -10px;'>Data Scientist & DevOps Engineer</h3>
    <p style='font-size: 18px; color: #aaa; max-width: 600px; margin: auto;'>I solve real-world problems using machine learning, automation, and scalable cloud infrastructure. Currently focused on AI agents, predictive systems, and DevOps engineering.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# 2. BADGES & TAGLINE
st.markdown("""
<div style='text-align: center; font-size: 16px;'>
    🧠 AI & ML • ☁️ Azure Cloud • 🔧 FastAPI & Terraform • 📊 Streamlit Dashboards
</div>
""", unsafe_allow_html=True)

st.write("")

# 3. ACTION LINKS (GITHUB, MEDIUM, LINKEDIN, CV)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/Psykali)", unsafe_allow_html=True)
with col2:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sief-m-khalifa/)", unsafe_allow_html=True)
with col3:
    st.markdown("[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium)](https://medium.com/@SKpsyktechdynamo)", unsafe_allow_html=True)
with col4:
    with open("assets/S_KHALIFA-CV.pdf", "rb") as f:
        st.download_button("📄 Download CV", f, file_name="S_KHALIFA-CV.pdf")

# 4. FEATURED PROJECTS PREVIEW
st.markdown("---")
st.subheader("🚀 Featured Work")

st.markdown("""
✅ **JSI Stock Forecasting**: ML model improved inventory accuracy by 18%
✅ **Revit + FastAPI**: Integrated BIM data into a prediction platform
✅ **DevOps Automation**: Cut server setup time by 40% using Terraform
""")

# 5. CALL TO ACTION
st.markdown("""
<div style='text-align: center; padding-top: 1.5em; color: #888; font-size: 16px;'>
    Want to collaborate, hire, or just say hi? 👉 Check out the [Contact] page!
</div>
""", unsafe_allow_html=True)
