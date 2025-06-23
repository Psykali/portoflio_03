import streamlit as st

projects = [
    {
        "title": "Revit + FastAPI Data Pipeline",
        "desc": "Integrated BIM data into a predictive ML pipeline. Used FastAPI, trained model with 95-98% accuracy.",
    },
    {
        "title": "JSI Stock Forecasting",
        "desc": "Improved inventory and sales forecasts with a custom ML model, reducing shortages and boosting planning accuracy.",
    },
    {
        "title": "Azure DevOps Automation",
        "desc": "CI/CD pipelines and server provisioning using Terraform & Ansible. Saved 30% cost across 350+ servers.",
    }
]

st.title("📂 Projects")
for p in projects:
    st.subheader(p["title"])
    st.markdown(p["desc"])
    st.markdown("---")
