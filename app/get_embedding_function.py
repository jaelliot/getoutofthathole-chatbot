# get_embedding_function.py


import os
from dotenv import load_dotenv
import cohere
from langchain.embeddings.base import Embeddings

load_dotenv()

class CohereEmbeddings(Embeddings):
    def __init__(self, api_key: str, model: str = "embed-english-v3.0", input_type: str = "classification"):
        self.client = cohere.Client(api_key)
        self.model = model
        self.input_type = input_type

    def embed_documents(self, documents: list) -> list:
        # Check if the items are strings or Document objects
        if isinstance(documents[0], str):
            texts = documents
        else:
            texts = [doc.page_content for doc in documents]
        return self.embed(texts)

    def embed_query(self, query: str) -> list:
        return self.embed([query])[0]

    def embed(self, texts):
        response = self.client.embed(texts=texts, model=self.model, input_type=self.input_type)
        return response.embeddings

def get_embedding_function():
    api_key = os.getenv("COHERE_API_KEY")
    embeddings = CohereEmbeddings(api_key=api_key)
    return embeddings
