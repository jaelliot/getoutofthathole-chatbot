import streamlit as st  # type: ignore
from functools import lru_cache
from app.get_embedding_function import get_embedding_function
from query_data import query_rag
from app.context_manager import ContextManager

context_manager = ContextManager()

@st.cache_resource
def cached_populate_database():
    from populate_database import main as populate_db
    return populate_db()

@st.cache_resource
def cached_query_rag(prompt, user_id, conversation_history):
    context = context_manager.get_context(user_id, conversation_history)
    return query_rag(prompt, context)

@lru_cache(maxsize=32)
def lru_cached_query(prompt, user_id, conversation_history):
    context = context_manager.get_context(user_id, conversation_history)
    return query_rag(prompt, context)
