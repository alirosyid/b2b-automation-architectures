def aggregate_b2b_intent_signals(lead_email, signal_events):
    print(f"[Lead Gen] Aggregating cross-channel intent telemetry for {lead_email}...")
    
    intent_score = 0
    signal_weights = {
        "pricing_page_view": 25,
        "linkedin_engagement": 10,
        "pdf_download": 40
    }
    
    for event in signal_events:
        intent_score += signal_weights.get(event["type"], 0)
        
    print(f"    -> Current Boiling Score: {intent_score}/100")
    
    if intent_score >= 70:
        print("[🔥] CRITICAL INTENT REACHED. Routing lead to SDR Priority Queue for instant dialing.")
        return {"status": "HOT", "score": intent_score}
        
    print("[+] Lead remains in automated nurture sequence.")
    return {"status": "WARM", "score": intent_score}

if __name__ == "__main__":
    events = [{"type": "pdf_download"}, {"type": "pricing_page_view"}, {"type": "linkedin_engagement"}]
    aggregate_b2b_intent_signals("vp_eng@target-saas.com", events)
