from text_embedding import get_embeddings_for_claim
from vector_db import build_faiss_index, faiss_search
import numpy as np

# ======================================================
# FINAL RAG PIPELINE (FACT-CHECK SAFE)
# ======================================================
def run_rag_fact_check(claim):

    urls, articles, query_emb, article_embs = get_embeddings_for_claim(claim)

    # safety
    if not articles:
        return [], []

    # -------------------------------
    # FAISS: get ONLY top-1 article
    # -------------------------------
    index = build_faiss_index(article_embs)
    top_evidence = faiss_search(index, query_emb, articles, top_k=1)

    # match URL to top article
    top_article = top_evidence[0]
    top_url = urls[articles.index(top_article)]

    return [top_url], [top_article]
