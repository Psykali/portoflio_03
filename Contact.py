import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.title("📬 Contact Me")

st.markdown("""
<div class="contact-box">
    <p>Feel free to reach out through any of the platforms below:</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("assets/project_imgs/contact/github-logo.png", width=40)
    st.markdown("[GitHub](https://github.com/Psykali)")

with col2:
    st.image("assets/project_imgs/contact/medium-logo.png", width=40)
    st.markdown("[Medium](https://medium.com/@SKpsyktechdynamo)")

with col3:
    st.image("assets/project_imgs/contact/linkedin-logo.png", width=40)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/sief-m-khalifa/)")

with col4:
    st.image("assets/project_imgs/contact/email-logo.png", width=40)
    st.markdown("[Email](mailto:siefkhalefa@gmail.com)")
