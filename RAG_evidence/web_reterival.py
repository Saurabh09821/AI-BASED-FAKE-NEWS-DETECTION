import requests
from bs4 import BeautifulSoup
import feedparser

# ======================================================
# STEP 2: SEARCH FACT-CHECK WEBSITES (RSS BASED – STABLE)
# ======================================================
def search_fact_check_sites(query):
    """
    Uses RSS feeds from trusted Indian fact-check websites.
    This avoids API limits and blocking.
    """

    rss_feeds = [
        "https://www.altnews.in/feed/",
        "https://www.boomlive.in/feed/",
        "https://factcheck.pib.gov.in/rss.xml"
    ]

    urls = []

    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            if "link" in entry:
                urls.append(entry.link)

    # remove duplicates and limit
    return list(dict.fromkeys(urls))[:5]


# ======================================================
# STEP 3: EXTRACT CLEAN ARTICLE TEXT
# ======================================================
def extract_article_text(url):
    """
    Downloads and extracts clean readable fact-check evidence.
    Works for AltNews, BoomLive, PIB.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text().strip() for p in paragraphs)

        clean_lines = [
            line for line in text.split("\n")
            if len(line.strip()) > 40
        ]

        clean_text = "\n".join(clean_lines)

        return clean_text if clean_text else "No readable content found."

    except Exception as e:
        return f"Error extracting content: {e}"


# ======================================================
# TEST (Optional)
# ======================================================
if __name__ == "__main__":
    claim = "government giving 5000 rupees to students"

    print("\n🔍 Searching fact-check websites (RSS)...")
    urls = search_fact_check_sites(claim)

    print("\nTop Fact-Check URLs Found:")
    for u in urls:
        print(" -", u)

    print("\n📄 Extracting article text...")
    for u in urls:
        print("\n===============================")
        print("URL:", u)
        text = extract_article_text(u)
        print(text[:800])
        print("===============================\n")
