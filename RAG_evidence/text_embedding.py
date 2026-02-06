from sentence_transformers import SentenceTransformer
from web_reterival import search_fact_check_sites, extract_article_text


# ======================================================
# Load embedding model
# ======================================================
model = SentenceTransformer("all-MiniLM-L6-v2")


# ======================================================
# Step 4A: Convert text → embeddings
# ======================================================
def embed_text(text):
    """
    Converts a single text string into a numerical embedding vector.
    """
    return model.encode(text, convert_to_numpy=True)


def embed_multiple(text_list):
    """
    Converts a list of article texts into embedding matrix.
    """
    return model.encode(text_list, convert_to_numpy=True)


# ======================================================
# Step 4B: Combined wrapper
# (Step 3 → Step 4)
# ======================================================
def get_embeddings_for_claim(claim):
    """
    1. Search fact-check websites (Step 2)
    2. Extract article text (Step 3)
    3. Embed query + articles (Step 4)
    
    Returns:
        urls       → list of URLs found
        articles   → list of extracted article texts
        query_emb  → embedding for claim
        article_embs → embeddings for all fact-check articles
    """

    print("\n🔍 Step 2: Searching fact-check websites...")
    urls = search_fact_check_sites(claim)

    print("\n📄 Step 3: Extracting article text...")
    articles = []
    for u in urls:
        print(f" - Extracting from: {u}")
        text = extract_article_text(u)
        articles.append(text)

    print("\n🔢 Step 4: Generating embeddings...")
    query_emb = embed_text(claim)
    article_embs = embed_multiple(articles)

    return urls, articles, query_emb, article_embs


# ======================================================
# Execute only for debugging (not used in final pipeline)
# ======================================================
if __name__ == "__main__":
    claim = "government giving 5000 rupees to students"
    urls, articles, query_emb, article_embs = get_embeddings_for_claim(claim)

    print("\nEmbedding Shapes:")
    print("Query:", query_emb.shape)
    print("Articles:", article_embs.shape)
