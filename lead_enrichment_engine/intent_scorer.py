def score_lead_intent(lead_data):
    score = 0
    company_size = lead_data.get("company_size", 0)
    message = lead_data.get("message", "").lower()
    
    if company_size > 50:
        score += 40
    elif company_size > 10:
        score += 20
        
    high_intent_keywords = ["budget", "immediately", "scaling", "bottleneck", "custom solution"]
    if any(kw in message for kw in high_intent_keywords):
        score += 35
        
    if lead_data.get("has_custom_domain", False):
        score += 25
        
    priority = "High (Direct to Closer)" if score >= 75 else "Nurture Sequence"
    
    return {"lead_email": lead_data.get("email"), "score": score, "routing": priority}

if __name__ == "__main__":
    mock_lead = {"email": "ceo@scaleup.com", "company_size": 120, "message": "Need help scaling our CRM data.", "has_custom_domain": True}
    print(score_lead_intent(mock_lead))
