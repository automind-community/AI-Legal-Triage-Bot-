"""Module defining the core legal RAG orchestration pipeline with frozen interface signatures."""

from collections.abc import Iterator
from typing import Any


def retrieve(query: str, top_k: int = 8) -> list[dict]:
    """Retrieve top-k relevant statutory chunks from the US Code FAISS vector store.

    FROZEN INTERFACE SIGNATURE.

    Args:
        query: User legal question or statutory inquiry string.
        top_k: Number of relevant statutory excerpts to retrieve. Defaults to 8.

    Returns:
        List of dictionaries containing statutory text, section title, citations, and scores.
    """
    raise NotImplementedError("retrieve stub.")


def answer_stream(query: str, history: list[dict] | None = None) -> Iterator[str]:
    """Generate a streamed legal answer grounded in retrieved US Code statutory provisions.

    FROZEN INTERFACE SIGNATURE.

    Args:
        query: User legal question string.
        history: Optional list of past chat turn dictionaries. Defaults to None.

    Yields:
        Streamed text token chunks from the Groq generation model.
    """
    raise NotImplementedError("answer_stream stub.")
