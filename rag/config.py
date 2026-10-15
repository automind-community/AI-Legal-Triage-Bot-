"""Configuration settings for the RAG pipeline using Pydantic Settings."""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class RAGSettings(BaseSettings):
    """Runtime configuration for embeddings, vector store, and LLM inference."""

    groq_api_key: str = ""
    groq_model: str = "llama-3.1-8b-instant"
    groq_temperature: float = 0.1
    groq_max_tokens: int = 2048

    embedding_model_name: str = "Hanno-Labs/dinghy-law-0.6b-v1"
    embedding_dimension: int = 768
    embedding_device: str = "cpu"

    faiss_index_path: str = "data/faiss_index.index"
    faiss_metadata_path: str = "data/faiss_index_metadata.npy"
    retrieval_top_k: int = 8

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_rag_settings() -> RAGSettings:
    """Return cached RAG settings. Safe to call repeatedly."""
    return RAGSettings()
