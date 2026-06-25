def process_support_ticket(ticket_data):
    issue = ticket_data.get("description", "").lower()
    complexity_keywords = ["database crash", "data loss", "security breach", "payment failure"]
    
    if any(kw in issue for kw in complexity_keywords):
        print(f"[Agent] 🚨 High complexity issue detected from {ticket_data['client_id']}. Routing to Tier-2 Human Support.")
        return {"action": "escalate", "priority": "High"}
        
    print(f"[Agent] Resolving Tier-1 issue autonomously for {ticket_data['client_id']}...")
    # Mock LLM generation for standard troubleshooting steps
    resolution = "We have reset your API token bucket. Please retry the webhook in 5 minutes."
    return {"action": "auto_reply", "resolution": resolution, "status": "closed"}

if __name__ == "__main__":
    mock_ticket = {"client_id": "Enterprise_X", "description": "Webhook returning 429 error continuously."}
    print(process_support_ticket(mock_ticket))
