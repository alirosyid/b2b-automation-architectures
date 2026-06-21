def analyze_community_sentiment(messages):
    negative_triggers = ["broken", "failed", "slow", "cancel", "frustrated"]
    positive_triggers = ["amazing", "fast", "saved", "roi", "perfect"]
    
    sentiment_score = 0
    for msg in messages:
        text = msg.lower()
        if any(word in text for word in negative_triggers):
            sentiment_score -= 1
        if any(word in text for word in positive_triggers):
            sentiment_score += 1
            
    if sentiment_score < 0:
        print("[Analytics] ⚠️ WARNING: Community sentiment trending negative. Immediate intervention required.")
    else:
        print("[Analytics] ✅ Community sentiment is positive and stable.")
        
    return sentiment_score

if __name__ == "__main__":
    recent_chat = ["The new automation saved us 10 hours!", "But the API feels a bit slow today."]
    analyze_community_sentiment(recent_chat)
