.PHONY: help setup ingest run test eval clean

PYTHON := python
PIP := pip
UVICORN := uvicorn

help:
	@echo "Legal RAG Bot Commands:"
	@echo "  make setup   - Install project dependencies in editable mode with dev & eval packages"
	@echo "  make ingest  - Download US Code dataset, generate embeddings, and build FAISS index"
	@echo "  make run     - Launch FastAPI server with live reload"
	@echo "  make test    - Run pytest test suite"
	@echo "  make eval    - Execute benchmark evaluation on housing_qa dataset"
	@echo "  make clean   - Remove cache files and build artifacts"

setup:
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev,eval]

ingest:
	$(PYTHON) -m ingestion.download
	$(PYTHON) -m ingestion.indexer

run:
	$(UVICORN) api.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest -v --tb=short

eval:
	$(PYTHON) -m eval.benchmark

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
