"""
Document Q&A engine backed by LlamaIndex + OpenAI embeddings.

The index is built lazily on the first /doc-chat request so that the
FastAPI server starts immediately even when no API key is configured.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Lazy globals — populated on first call to query_documents()
_query_engine = None


def _get_query_engine():
    """Build (or return cached) query engine.

    FIX: Previously built index at module import time, which caused
    the server to crash on startup if the OpenAI key was missing or
    the network was unreachable. Now deferred to first request.
    """
    global _query_engine
    if _query_engine is not None:
        return _query_engine

    # Import here so module-level import doesn't trigger network calls
    # FIX: `VectorStroreIndex` was a typo → VectorStoreIndex
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
    from llama_index.llms.openai import OpenAI as LlamaOpenAI

    # FIX: model name was "get-3.5-turbo" (typo) → "gpt-3.5-turbo"
    llama_llm = LlamaOpenAI(
        model="gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Resolve docs path relative to this file
    docs_dir = os.path.join(os.path.dirname(__file__), "docs")
    documents = SimpleDirectoryReader(docs_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    _query_engine = index.as_query_engine(llm=llama_llm)
    return _query_engine


def query_documents(query: str) -> str:
    """Query the document index and return a string answer.

    FIX: was named query_docs() but main.py called query_documents().
    FIX: query_engine.query() takes a positional arg, not keyword `user_query=`.
    """
    engine = _get_query_engine()
    return str(engine.query(query))
