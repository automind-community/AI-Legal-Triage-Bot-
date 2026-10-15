# Legal RAG Chatbot

A high-performance Legal Question-Answering system powered by Retrieval-Augmented Generation (RAG) over the US Code.

## Architecture
- **API:** FastAPI with Server-Sent Events (SSE) token streaming.
- **Embeddings:** `dinghy-law-0.6b-v1` specialized legal embeddings.
- **Vector Search:** FAISS (`IndexFlatIP`) with normalized inner product (cosine similarity).
- **Generation:** Groq Cloud (`llama-3.1-8b-instant`) with grounded legal citation prompting.
- **Evaluation:** Evaluated on `reglab/housing_qa` for statutory retrieval accuracy and legal correctness.

## Project Structure
```
Legal Bot/
├── .env.example
├── .gitignore
├── Makefile
├── README.md
├── pyproject.toml
│
├── api/             # FastAPI server, routing, schemas, and dependencies
├── eval/            # Benchmarking and metrics on reglab/housing_qa
├── frontend/        # Modern legal chat UI with SSE streaming
├── ingestion/       # Dataset download, statutory chunking, and FAISS indexing
├── rag/             # Retrieval pipeline, FAISS vector store, embeddings, and LLM
└── tests/           # Unit and integration test suite
```

## Quickstart

1. **Setup environment:**
   ```bash
   cp .env.example .env
   # Add your GROQ_API_KEY in .env
   make setup
   ```

2. **Ingest data & build vector index:**
   ```bash
   make ingest
   ```

3. **Start the API & Web Client:**
   ```bash
   make run
   ```
   Open `http://localhost:8000` in your browser.

4. **Run Unit Tests:**
   ```bash
   make test
   ```

5. **Run Retrieval & Answer Evaluation:**
   ```bash
   make eval
   ```
