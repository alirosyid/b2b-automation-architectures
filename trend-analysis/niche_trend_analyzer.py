def extract_micro_trends(forum_data):
    print("[Trends] Scraping deep-web and niche forums for emerging aesthetic shifts...")
    
    emerging_keywords = []
    for post in forum_data:
        text = post.get("content", "").lower()
        if "core" in text or "wave" in text:
            # Simple mock NLP extraction
            words = text.split()
            trend = [w for w in words if "core" in w or "wave" in w]
            emerging_keywords.extend(trend)
            
    unique_trends = list(set(emerging_keywords))
    print(f"[+] Isolated high-velocity micro-trends: {unique_trends}")
    print("[+] Syncing trends to AI generation prompts for first-mover advantage.")
    return unique_trends

if __name__ == "__main__":
    mock_forums = [{"content": "I'm really getting into synthwave and hardstyle recently."}]
    extract_micro_trends(mock_forums)
