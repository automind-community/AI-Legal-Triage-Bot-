"""Module containing prompt templates and citation formatting rules for legal QA."""

from typing import Any

LEGAL_SYSTEM_PROMPT = """You are a specialized US Federal Statutory Legal Assistant.
Your primary role is to answer legal inquiries strictly and accurately using the provided US Code provisions.
Rules:
1. Ground every claim directly in the cited statutory provisions.
2. Cite the exact Title and Section (e.g., 42 U.S.C. § 3604).
3. If the provided context is insufficient to answer the question, explicitly state the limitation.
4. Do not invent or extrapolate federal provisions outside the provided statutory excerpts.
"""


def format_context_passages(retrieved_docs: list[dict[str, Any]]) -> str:
    """Format retrieved statutory passages with explicit citation headers for LLM prompting.

    Args:
        retrieved_docs: List of retrieved passage dictionaries.

    Returns:
        Formatted context string with numbered citations.
    """
    raise NotImplementedError("Context formatter stub.")


def build_chat_messages(
    query: str,
    retrieved_docs: list[dict[str, Any]],
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    """Assemble system, historical context, and user query messages for the LLM.

    Args:
        query: User's legal question.
        retrieved_docs: Retrieved statutory documents.
        history: Prior conversation turns.

    Returns:
        List of message dictionaries ready for LLM consumption.
    """
    raise NotImplementedError("Message builder stub.")
