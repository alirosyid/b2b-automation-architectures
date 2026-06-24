def analyze_subreddit_momentum(posts):
    viral_threshold = 50 # upvotes per hour
    
    for post in posts:
        momentum = post["upvotes"] / post["hours_live"]
        
        if momentum >= viral_threshold and "complain" in post["flair"].lower():
            print(f"[Trends] 📈 VIRAL COMPLAINT DETECTED: '{post['title']}'")
            print(f"Momentum: {momentum} upvotes/hr. Generating stealth marketing response protocol.")
            return {"target_topic": post["title"], "action": "deploy_stealth_content"}
            
    print("[Trends] No viral software complaints detected in current cycle.")
    return None

if __name__ == "__main__":
    mock_reddit_data = [
        {"title": "Is anyone else's Zapier bill out of control?", "flair": "Complaint", "upvotes": 450, "hours_live": 4}
    ]
    analyze_subreddit_momentum(mock_reddit_data)
