import asyncio
import streamlit as st
from doc_generator import DocGenerator

st.set_page_config(page_title="🧠 AutoCodeDocGen App", layout="wide")
st.title("📑 Automated Code Documentation Generator (Multi-language)")

# Initialize DocGenerator
doc_generator = DocGenerator()

# File uploader
uploaded_file = st.file_uploader("📂 Upload a code file", type=["py", "java", "cpp", "js", "go", "rb", "php", "ts", "c"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    st.subheader("📜 Uploaded Code")
    st.code(code, language='auto')

    # Select language
    language = st.selectbox(
        "Select the programming language:",
        ["python", "java", "c++", "javascript", "go", "ruby", "php", "typescript", "c"]
    )

    # Button to trigger generation
    if st.button("🚀 Generate Documentation"):
        st.info("⏳ Generating documentation...please wait. This may take a minute for large files.")

        output_area = st.empty()

        async def generate_and_stream():
            documentation = ""
            async for chunk in doc_generator.generate_documentation_stream(code, language):
                documentation += chunk
                output_area.markdown(documentation, unsafe_allow_html=True)

            st.success("✅ Documentation generation completed!")

            st.download_button(
                label="📥 Download Documentation (Markdown)",
                data=documentation,
                file_name="generated_documentation.md",
                mime="text/markdown"
            )

        # Handle asyncio inside Streamlit safely
        asyncio.run(generate_and_stream())
