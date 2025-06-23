import streamlit as st
import os
import json
from PIL import Image

st.title("📂 My Projects ")

PROJECTS_DIR = "projects"

# Sort folders alphabetically
folders = sorted(os.listdir(PROJECTS_DIR))

for folder in folders:
    project_path = os.path.join(PROJECTS_DIR, folder)
    info_path = os.path.join(project_path, "info.json")

    if os.path.isdir(project_path) and os.path.exists(info_path):
        with open(info_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        image_path = os.path.join(project_path, data.get("image", "preview.png"))
        col1, col2 = st.columns([1, 3])

        with col1:
            if os.path.exists(image_path):
                st.image(Image.open(image_path), use_container_width=True)
            else:
                st.warning("❌ Image not found")

        with col2:
            st.subheader(data["title"])
            st.markdown(data["description"])
            if "link" in data:
                st.markdown(f"[🔗 View Project]({data['link']})", unsafe_allow_html=True)

        st.markdown("---")
