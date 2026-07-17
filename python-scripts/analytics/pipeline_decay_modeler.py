def analyze_pipeline_decay(deals_in_pipeline):
    print("[Analytics] Running predictive decay modeling on active sales pipeline...")
    
    decaying_deals = []
    
    for deal in deals_in_pipeline:
        # Complex heuristic mocked as a simple decay score
        decay_score = (deal["days_since_last_contact"] * 1.5) - (deal["stakeholder_sentiment"] * 10)
        
        if decay_score > 50:
            print(f"[!] 📉 DECAY DETECTED: {deal['company']} deal momentum is crashing (Score: {decay_score}).")
            decaying_deals.append(deal["company"])
            
    if decaying_deals:
        print(f"[+] Pushing {len(decaying_deals)} decaying deals to n8n for autonomous re-engagement sequencing.")
        return decaying_deals
        
    print("[+] Pipeline momentum is universally healthy.")
    return []

if __name__ == "__main__":
    mock_pipeline = [
        {"company": "Acme Corp", "days_since_last_contact": 14, "stakeholder_sentiment": 0.2},
        {"company": "Beta Inc", "days_since_last_contact": 2, "stakeholder_sentiment": 0.9}
    ]
    analyze_pipeline_decay(mock_pipeline)
