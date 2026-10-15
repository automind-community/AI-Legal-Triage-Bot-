"""Pydantic schemas for request validation and response serialization with frozen signatures."""

from typing import Any
from pydantic import BaseModel, Field


class Citation(BaseModel):
    """Statutory legal citation schema corresponding to retrieved US Code sections.

    FROZEN INTERFACE SIGNATURE.
    """

    title: str = Field(..., description="US Code Title (e.g. 'Title 42 - The Public Health and Welfare')")
    section: str = Field(..., description="Section number and heading (e.g. '42 U.S.C. § 3604')")
    text: str = Field(..., description="Statutory excerpt text")
    score: float = Field(..., description="Vector similarity relevance score")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional statutory metadata")


class ChatRequest(BaseModel):
    """Incoming user chat query and session history request schema.

    FROZEN INTERFACE SIGNATURE.
    """

    query: str = Field(..., min_length=1, description="Legal question or inquiry")
    history: list[dict[str, Any]] | None = Field(default=None, description="Previous chat turns")
    top_k: int = Field(default=8, ge=1, le=32, description="Number of statutory passages to retrieve")


class ChatResponse(BaseModel):
    """Non-streaming complete response schema with answer text and citations."""

    answer: str = Field(..., description="Generated legal answer grounded in statutory context")
    citations: list[Citation] = Field(default_factory=list, description="Retrieved statutory citations")


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str = Field(default="ok", description="API operational status")
    version: str = Field(..., description="Service version")
    faiss_index_loaded: bool = Field(..., description="Indicates if vector index is ready in memory")
