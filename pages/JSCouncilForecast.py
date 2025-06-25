import streamlit as st
import json
import os
from PIL import Image

PROJECT_DIR = "projects/jsi_council_forecast"

# Load metadata
with open(os.path.join(PROJECT_DIR, "info.json"), encoding="utf-8") as f:
    data = json.load(f)

st.title(data["title"])

# Show image
img_path = os.path.join(PROJECT_DIR, data.get("image", "preview.png"))
if os.path.exists(img_path):
    st.image(Image.open(img_path), use_container_width=True)

# Full project description
st.markdown(data["description"], unsafe_allow_html=True)

# Link (if available)
if data.get("link"):
    st.markdown(f"[📁 GitHub Repo]({data['link']})", unsafe_allow_html=True)

# Back to projects
st.markdown("[⬅️ Back to Projects](Projects)")
