"""FastAPI dependency injection providers for configuration, vector store, and RAG pipeline."""

from rag.config import RAGSettings, get_rag_settings
from rag.vector_store import FAISSVectorStore


def get_settings() -> RAGSettings:
    """Dependency provider returning RAG configuration settings."""
    raise NotImplementedError("Settings dependency stub.")


def get_vector_store() -> FAISSVectorStore:
    """Dependency provider returning singleton FAISS vector store instance."""
    raise NotImplementedError("Vector store dependency stub.")
