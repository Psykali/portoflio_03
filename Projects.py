import streamlit as st
from pathlib import Path

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

projects = [
    {
        "title": "Stock Forecasting Model (JSI Council)",
        "desc": "Improved stock accuracy by 18%, predicted peak sales and staffing periods using ML.",
        "img": "assets/project_imgs/jsi_stock.jpg"
    },
    {
        "title": "Revit + FastAPI Integration",
        "desc": "Pipeline to extract and train models on Revit data with 95–98% accuracy. Connected to FastAPI.",
        "img": "assets/project_imgs/revit_api.png"
    },
    {
        "title": "Interactive Streamlit Dashboard",
        "desc": "Streamlit dashboard for live ML model interaction (Eiffage Construction).",
        "img": "assets/project_imgs/streamlit_dash.png"
    },
    {
        "title": "Azure Infra Provisioning (Terraform & Ansible)",
        "desc": "Cut setup time by 40% across 350+ servers and optimized cloud costs by 30%.",
        "img": "assets/project_imgs/azure_terraform.png"
    }
]

st.title("📂 Projects")

for p in projects:
    st.markdown(f"""
    <div class='project-card'>
        <img src="{p['img']}" width="100%" style="border-radius: 12px; margin-bottom: 10px;" />
        <h3>{p["title"]}</h3>
        <p>{p["desc"]}</p>
    </div>
    """, unsafe_allow_html=True)
