import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.title("👋 Hi, I'm S. Khalifa")
st.subheader("Data Scientist & DevOps Engineer")

st.markdown("""
I specialize in building scalable AI & ML pipelines and deploying them with Cloud/DevOps tools.

- 🧠 AI & ML | 🛠️ Azure DevOps | 🧰 FastAPI & Terraform
- 📫 Reach me: [LinkedIn](https://www.linkedin.com/in/sief-m-khalifa/) • [Mail](mailto:siefkhalefa@gmail.com)
""")

with open("assets/S_KHALIFA-CV.pdf", "rb") as file:
    btn = st.download_button("📄 Download My CV", file, file_name="S_KHALIFA-CV.pdf")
