import streamlit as st
import os
import json
from PIL import Image

st.title("📂 Projects")

PROJECTS_DIR = "projects"

folders = sorted(os.listdir(PROJECTS_DIR))

for folder in folders:
    path = os.path.join(PROJECTS_DIR, folder)
    info_file = os.path.join(path, "info.json")

    if os.path.exists(info_file):
        with open(info_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        slug = data.get("slug", folder)
        summary = data.get("summary", "No summary provided")
        image_path = os.path.join(path, data.get("image", "preview.png"))

        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(image_path):
                st.image(Image.open(image_path), use_container_width=True)
        with col2:
            st.subheader(data["title"])
            st.markdown(summary)
            st.page_link(f"pages/{slug.replace('_', ' ').title()}.py", label="🔍 View Full Project")

        st.markdown("---")
