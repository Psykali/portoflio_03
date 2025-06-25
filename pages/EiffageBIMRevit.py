import streamlit as st
import json
import os
from PIL import Image

PROJECT_DIR = "projects/eiffage_bmi_revit"

with open(os.path.join(PROJECT_DIR, "info.json"), encoding="utf-8") as f:
    data = json.load(f)

st.title(data["title"])

image_path = os.path.join(PROJECT_DIR, data.get("image", "revit_api.png"))
if os.path.exists(image_path):
    st.image(Image.open(image_path), use_container_width=True)

st.markdown(data["description"], unsafe_allow_html=True)

if data.get("link"):
    st.markdown(f"[📁 GitHub Repo]({data['link']})", unsafe_allow_html=True)

st.markdown("[⬅️ Back to Projects](Projects)")
