import os, streamlit as st
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores import ChromaVectorStore

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DOCS_PATH = "/app/docs"
VECTOR_PATH = "/app/chroma_store"
os.makedirs(DOCS_PATH, exist_ok=True)

st.title("📄 Document Ingestion & Indexing")
files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
if files:
    for f in files:
        with open(os.path.join(DOCS_PATH, f.name), "wb") as out:
            out.write(f.getbuffer())
    st.success("✅ Uploaded!")

if st.button("🔍 Build Index"):
    with st.spinner("Indexing..."):
        docs = SimpleDirectoryReader(DOCS_PATH).load_data()
        vs = ChromaVectorStore(persist_dir=VECTOR_PATH)
        idx = VectorStoreIndex.from_documents(docs, embed_model=OpenAIEmbedding(api_key=OPENAI_API_KEY), vector_store=vs)
        idx.storage_context.persist()
    st.success("✅ Index built!")
