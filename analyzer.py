from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):
    loader = PyPDFLoader(path)
    documents = loader.load()
    full_text = "\n".join(doc.page_content for doc in documents)
    return full_text

def load_llm(model_path):
    return GPT4All(model=model_path, backend="gpt4all", verbose=False)

def get_insights(query, text, llm):
    prompt = PromptTemplate(
        input_variables=["query", "text"],
        template="""
You are a cancer research assistant. Answer the user's question based on the paper below.

User question: {query}

Paper content:
{text}

Answer:"""
    )
    chain = prompt | llm
    return chain.invoke({"query": query, "text": text[:5000]})  # Keep within context length
