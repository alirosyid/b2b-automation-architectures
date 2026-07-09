def aggregate_comment_sentiment(comment_threads):
    print("[Scraping] Aggregating multi-channel audience sentiment...")
    
    actionable_engagements = []
    keywords = ["sponsor", "business inquiry", "collab", "license"]
    
    for comment in comment_threads:
        text = comment.get("text", "").lower()
        if any(kw in text for kw in keywords):
            print(f"[Lead Gen] 🚨 High-value inquiry detected: '{comment['text']}'")
            actionable_engagements.append(comment)
            
    print(f"[+] Swept threads. Routed {len(actionable_engagements)} business inquiries to CRM.")
    return actionable_engagements

if __name__ == "__main__":
    mock_comments = [
        {"author": "BrandX", "text": "We'd love to sponsor a collab on your next mix."},
        {"author": "User123", "text": "Great drop!"}
    ]
    aggregate_comment_sentiment(mock_comments)
