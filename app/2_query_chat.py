import os, streamlit as st
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.vector_stores import ChromaVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VECTOR_PATH = "/app/chroma_store"
st.title("💬 Ask About Your PDFs")

try:
    vs = ChromaVectorStore(persist_dir=VECTOR_PATH)
    sc = StorageContext.from_defaults(vector_store=vs)
    idx = load_index_from_storage(sc)
    retriever = idx.as_retriever(similarity_top_k=3)

    llm = ChatOpenAI(model="gpt-4", temperature=0, api_key=OPENAI_API_KEY)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

    q = st.text_input("What would you like to know?")
    if q:
        with st.spinner("Thinking..."):
            r = qa({"query": q})
        st.markdown("### 💡 Answer")
        st.write(r["result"])
        st.markdown("### 📚 Sources")
        for i, d in enumerate(r["source_documents"]):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(d.page_content)

except Exception:
    st.warning("⚠️ Run the ingestion app first to build the index.")
