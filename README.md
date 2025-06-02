# 🧬 LLM-Enhanced Cancer Literature Mining

A lightweight offline AI tool to analyze cancer research papers using local large language models (LLMs) like GPT4All.

## 🔍 Features

- Extract insights from PDFs
- Summarize findings
- Answer custom research questions
- 100% offline: no API keys, no server calls

## 🛠️ Setup Instructions

1. **Install dependencies**
pip install -r requirements.txt

2. **Download models**
- LLM (GPT4All): [Download from GPT4All.io](https://gpt4all.io/models/)
  - Place it in `models/` folder as `ggml-gpt4all-j-v1.3-groovy.bin`

3. **Add PDFs**
- Place cancer-related research PDFs in the `papers/` folder

4. **Run the app**
streamlit run app.py

## 🧠 Example Prompts

- "Summarize this paper"
- "What cancer genes are discussed?"
- "What are the main findings?"

## 💼 For Bioinformatics & Healthcare AI

- Use in academia or research teams
- Extend to include vector search or multi-PDF comparison
