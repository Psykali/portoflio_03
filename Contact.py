import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.title("📬 Contact Me")

st.markdown("""
<div class="contact-box">
    <p>Feel free to reach out through any of the platforms below:</p>
    <a href="https://github.com/Psykali" target="_blank">
        <img src="assets/project_imgs/contact/github-logo.png" alt="GitHub" width="40" style="margin-right: 10px;">
    </a>
    <a href="https://medium.com/@SKpsyktechdynamo" target="_blank">
        <img src="assets/project_imgs/contact/medium-logo.png" alt="Medium Blog" width="40" style="margin-right: 10px;">
    </a>
    <a href="https://www.linkedin.com/in/sief-m-khalifa/" target="_blank">
        <img src="assets/project_imgs/contact/linkedin-logo.png" alt="LinkedIn" width="40" style="margin-right: 10px;">
    </a>
    <a href="mailto:siefkhalefa@gmail.com" target="_blank">
        <img src="assets/project_imgs/contact/email-logo.png" alt="Email" width="40" style="margin-right: 10px;">
    </a>
</div>
""", unsafe_allow_html=True)
