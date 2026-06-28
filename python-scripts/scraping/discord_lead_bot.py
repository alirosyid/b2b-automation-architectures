def scan_discord_messages(messages, trigger_keywords):
    actionable_leads = []
    
    for msg in messages:
        content_lower = msg["content"].lower()
        if any(kw in content_lower for kw in trigger_keywords):
            print(f"[Scraping] Intent detected in Discord from @{msg['author']}: '{msg['content']}'")
            actionable_leads.append(msg["author"])
            
    return actionable_leads

def dispatch_stealth_dm(user):
    pitch = f"Hey @{user}, saw you were struggling with webhook routing. We built a custom n8n template that fixes exactly that. Happy to share it if you're interested."
    print(f"[Lead Gen] Dispatching DM to {user}...\nContent: {pitch}")

if __name__ == "__main__":
    mock_chat = [
        {"author": "StartupCTO", "content": "How do I connect Stripe to HubSpot without Zapier? It's too expensive."},
        {"author": "DevBro", "content": "Just updated my local dev environment."}
    ]
    leads = scan_discord_messages(mock_chat, ["without zapier", "automate this", "too manual"])
    
    for lead in leads:
        dispatch_stealth_dm(lead)
