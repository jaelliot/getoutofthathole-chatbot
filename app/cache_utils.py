import streamlit as st  # type: ignore
from functools import lru_cache
from app.get_embedding_function import get_embedding_function
from query_data import query_rag

@st.cache_resource
def cached_populate_database():
    from populate_database import main as populate_db
    return populate_db()

@st.cache_resource
def cached_query_rag(prompt):
    return query_rag(prompt)

@lru_cache(maxsize=32)
def lru_cached_query(prompt):
    return query_rag(prompt)
