import faiss
import numpy as np


# ======================================================
# Step 5A: Build FAISS vector DB
# ======================================================
def build_faiss_index(article_embs):
    """
    Builds a FAISS in-memory vector store using article embeddings.
    """
    if article_embs is None or len(article_embs) == 0:
        raise ValueError("No article embeddings found. Search returned no results.")

    if len(article_embs.shape) == 1:
        article_embs = article_embs.reshape(1, -1)

    dim = article_embs.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(article_embs)
    return index



# ======================================================
# Step 5B: Search FAISS for Top Evidence
# ======================================================
def faiss_search(index, query_emb, articles, top_k=3):
    """
    Returns the top_k most relevant article texts.
    """
    distances, ids = index.search(np.array([query_emb]), top_k)

    result_texts = []
    for i in ids[0]:
        result_texts.append(articles[i])

    return result_texts
