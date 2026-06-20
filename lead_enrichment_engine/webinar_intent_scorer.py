def score_webinar_attendees(chat_logs):
    high_intent_keywords = ["pricing", "integrate", "implementation", "onboarding", "sla"]
    hot_leads = []
    
    for log in chat_logs:
        message = log["message"].lower()
        if any(keyword in message for keyword in high_intent_keywords):
            print(f"[Enrichment] Hot lead identified: {log['user']} asked about '{message}'")
            hot_leads.append(log["user"])
            
    return hot_leads

if __name__ == "__main__":
    mock_logs = [
        {"user": "cto@startup.io", "message": "Does this integrate with our custom AWS backend?"},
        {"user": "dev@tech.co", "message": "Will there be a recording?"}
    ]
    leads = score_webinar_attendees(mock_logs)
    print(f"[+] Total hot leads routed to CRM: {len(leads)}")
