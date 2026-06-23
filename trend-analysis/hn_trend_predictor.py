def extract_emerging_tech(post_titles):
    print("[Trends] Analyzing HackerNews frontpage for emerging tech signatures...")
    
    emerging_keywords = []
    # Simplified NLP/Keyword extraction mock
    for title in post_titles:
        if "AI" in title or "Agent" in title or "LLM" in title:
            emerging_keywords.append(title.split()[0]) # Grabs first word as naive entity extraction
            
    print(f"[Trends] Identified high-velocity topics for SEO engine: {list(set(emerging_keywords))}")
    return emerging_keywords

if __name__ == "__main__":
    mock_titles = ["GraphRAG is changing vector search", "Why Agentic frameworks are the future"]
    extract_emerging_tech(mock_titles)
