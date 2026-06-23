def parse_slack_deal_message(message_payload):
    text = message_payload.get("text", "").lower()
    
    if "deal won" in text or "closed" in text:
        # Extremely basic extraction logic for demo purposes
        words = text.split()
        client_name = words[words.index("for") + 1] if "for" in words else "Unknown Client"
        
        print(f"[Integrations] 🎉 Deal extraction triggered! Updating CRM status for: {client_name}")
        # Call CRM API here (e.g., Hubspot deal stage update)
        return {"status": "CRM_UPDATED", "client": client_name}
        
    return {"status": "IGNORED"}

if __name__ == "__main__":
    msg = {"text": "Just closed a massive deal won for TechGlobal!"}
    parse_slack_deal_message(msg)
