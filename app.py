import streamlit as st
from main import app


st.set_page_config(
    page_title="Company Intelligence Agent",
    layout="centered"
)

st.title("🤖 Company Intelligence Agentic System")
st.caption("Multi-agent system powered by LangGraph + Ollama")

company = st.text_input(
    "Enter company name",
    placeholder="Tesla, Google..."
)

if st.button("Generate Intelligence Report"):
    if not company.strip():
        st.warning("⚠️ Please enter a company name")
    else:
        with st.spinner("🧠 Generating report..."):
            try:
                result = app.invoke({"company": company})
            except Exception as e:
                st.error("Something went wrong.")
                st.stop()

        st.success("✅ Report Generated")

        with st.container(border=True):
            st.markdown("### 📊 Company Intelligence Report")
            st.markdown(result["analysis"])
