import streamlit as st
import json
import os
from PIL import Image

PROJECT_DIR = "projects/HRD_Monitoring_Workbooks"

with open(os.path.join(PROJECT_DIR, "info.json"), encoding="utf-8") as f:
    data = json.load(f)

st.title(data["title"])

img_path = os.path.join(PROJECT_DIR, data["image"])
if os.path.exists(img_path):
    st.image(Image.open(img_path), use_container_width=True)

st.markdown(data["description"], unsafe_allow_html=True)

if data.get("link"):
    st.markdown(f"[📁 GitHub Repo]({data['link']})", unsafe_allow_html=True)

st.markdown("[⬅️ Back to Projects](Projects)")
