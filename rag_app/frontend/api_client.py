import streamlit as st
import pandas as pd
import requests

base_url = "http://rag_backend:8000/api"

def upload_document(file) -> dict:
    url = f"{base_url}/upload"
    files = {"file": file}
    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()


def query_llm(query_text: str, top_k: int = 5) -> dict:
    url = f"{base_url}/query"
    params = {"q": query_text, "top_k": top_k}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
