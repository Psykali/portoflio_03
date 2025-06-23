import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.markdown("""
<div style='text-align: center; padding: 2em;'>
    <h1 style='color: #278ea5;'>👋 Let's Connect</h1>
    <p style='font-size: 18px; color: #aaa;'>I'm open to opportunities, collaborations, or just a good conversation.</p>
    <p style='font-size: 16px; margin-bottom: 30px;'>Feel free to reach out through any of the platforms below:</p>
</div>
""", unsafe_allow_html=True)

# Columns for icons and links
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("assets/project_imgs/contact/email-logo.png", width=50)
    st.markdown("[Email](mailto:siefkhalefa@gmail.com)")

with col2:
    st.image("assets/project_imgs/contact/github-logo.png", width=50)
    st.markdown("[GitHub](https://github.com/Psykali)")

with col3:
    st.image("assets/project_imgs/contact/linkedin-logo.png", width=50)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/sief-m-khalifa/)")

with col4:
    st.image("assets/project_imgs/contact/medium-logo.png", width=50)
    st.markdown("[Medium](https://medium.com/@SKpsyktechdynamo)")

st.markdown("---")

st.markdown("""
<div style='text-align: center; color: #aaa;'>
    <p>Prefer direct messaging? Reach out via email above or connect with me on LinkedIn.</p>
    <p>Looking forward to hearing from you!</p>
</div>
""", unsafe_allow_html=True)
