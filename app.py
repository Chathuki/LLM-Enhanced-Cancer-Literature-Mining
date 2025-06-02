import os
import streamlit as st
from analyzer import load_pdf, load_llm, get_insights

st.set_page_config(page_title="Cancer Literature Mining", page_icon="🧬", layout="centered")
st.title("🧬 LLM-Enhanced Cancer Literature Mining (Offline)")
st.markdown("Analyze cancer-related research papers using local LLMs — no API or internet required.")

PDF_PATH = "./papers/example_cancer_study.pdf"
MODEL_PATH = "./models/ggml-gpt4all-j-v1.3-groovy.bin"

# Check file existence
if not os.path.exists(PDF_PATH):
    st.error(f"❌ PDF not found at {PDF_PATH}. Please place a file in the `papers/` folder.")
    st.stop()

if not os.path.exists(MODEL_PATH):
    st.error(f"❌ LLM model not found at {MODEL_PATH}. Please download the GPT4All model and place it in `models/`.")
    st.stop()

# Load LLM and PDF
with st.spinner("Loading resources..."):
    text = load_pdf(PDF_PATH)
    llm = load_llm(MODEL_PATH)

# User prompt
st.markdown("### Enter a research question or ask for a summary:")
query = st.text_input("Ask something like 'Summarize this paper' or 'What genes are mentioned?'")

if st.button("Analyze") and query:
    with st.spinner("Analyzing..."):
        response = get_insights(query, text, llm)
        st.success("✅ Result:")
        st.markdown(response)
