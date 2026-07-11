def score_slack_mentions(messages):
    print("[Lead Gen] Parsing raw Slack community firehose for B2B intent signals...")
    hot_leads = []
    
    for msg in messages:
        score = 0
        text = msg["text"].lower()
        
        if "recommend" in text and "automation" in text: score += 40
        if "budget" in text or "hiring" in text: score += 30
        
        if score >= 50:
            print(f"[🔥] Boiling lead detected: User {msg['user']}. Routing to CRM.")
            hot_leads.append(msg["user"])
            
    return hot_leads

if __name__ == "__main__":
    chat = [{"user": "CTO_Dave", "text": "Can anyone recommend a good automation agency? We are hiring."}]
    score_slack_mentions(chat)
