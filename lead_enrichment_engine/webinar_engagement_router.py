def route_webinar_leads(attendee_metrics):
    hot_leads = []
    
    for attendee in attendee_metrics:
        score = 0
        if attendee["watch_time_minutes"] > 45: score += 30
        if attendee["questions_asked"] > 0: score += 40
        if attendee["poll_participated"]: score += 20
        
        if score >= 70:
            print(f"[Enrichment] 🔥 HOT LEAD: {attendee['email']} (Score: {score}). Routing to closing sequence.")
            hot_leads.append(attendee["email"])
        else:
            print(f"[Enrichment] Warm lead: {attendee['email']}. Routing to long-term nurture.")
            
    return hot_leads

if __name__ == "__main__":
    metrics = [
        {"email": "ceo@b2b.com", "watch_time_minutes": 50, "questions_asked": 2, "poll_participated": True},
        {"email": "intern@startup.com", "watch_time_minutes": 15, "questions_asked": 0, "poll_participated": False}
    ]
    route_webinar_leads(metrics)
