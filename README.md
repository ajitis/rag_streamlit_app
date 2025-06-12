# 📄 RAG Streamlit App with LangChain & LlamaIndex

This Streamlit app lets you upload PDF docs, index them, and ask questions using RAG (OpenAI GPT-4).

## 🛠️ Setup Locally

```bash
cd rag_streamlit_app/app
cp .env.example .env
# add OPENAI_API_KEY value
pip install -r requirements.txt

# Terminal 1
streamlit run 1_ingest_index.py

# Terminal 2
streamlit run 2_query_chat.py
```

## 🐳 Docker Deployment

```bash
cd rag_streamlit_app/app
docker build -t rag-streamlit .
docker run --env-file .env -p 8501:8501 rag-streamlit
```

Then navigate to `http://localhost:8501` to index docs.

---

## 🧠 Usage Flow

1. Upload PDFs via ingestion app.
2. Click “Build Index”.
3. Navigate to query app.
4. Ask questions—get answers + source context.
