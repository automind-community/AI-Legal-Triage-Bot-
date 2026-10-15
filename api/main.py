"""FastAPI application entrypoint, lifecycle management, CORS configuration, and static mount."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager to preload FAISS index and embedding models."""
    # Startup actions stub
    yield
    # Shutdown actions stub


def create_app() -> FastAPI:
    """Create, configure, and return the FastAPI application instance."""
    app = FastAPI(
        title="Legal RAG Chatbot API",
        description="FastAPI service for legal question answering over US Federal Code.",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()
