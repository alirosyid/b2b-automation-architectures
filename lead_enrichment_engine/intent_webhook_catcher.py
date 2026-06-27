def process_intent_webhook(payload):
    target_topics = ["business process automation", "n8n", "ai agents", "data integration"]
    
    company = payload.get("company", "Unknown")
    researched_topics = payload.get("topics", [])
    
    match_found = any(topic.lower() in target_topics for topic in researched_topics)
    
    if match_found:
        print(f"[Lead Gen] 🚨 HIGH INTENT SIGNAL: {company} is actively researching automation.")
        # Trigger push to Slack/Discord sales channel
        return {"status": "routed_to_sales", "company": company}
        
    print(f"[Lead Gen] Signal from {company} logged, but lacks automation intent.")
    return {"status": "ignored"}

if __name__ == "__main__":
    mock_webhook = {"company": "Acme Corp", "topics": ["cloud storage", "ai agents"]}
    process_intent_webhook(mock_webhook)
