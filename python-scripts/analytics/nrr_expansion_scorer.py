def calculate_expansion_probability(client_id, api_growth_rate, sentiment_score):
    print(f"[Analytics] Evaluating Net Retention Rate (NRR) expansion vectors for {client_id}...")
    
    expansion_score = 0
    
    # 1. Sustained infrastructure scaling
    if api_growth_rate > 0.25:  # 25% MoM API growth
        expansion_score += 45
        
    # 2. Positive support interactions
    if sentiment_score > 0.85:
        expansion_score += 35
        
    print(f"    -> Current Expansion Score: {expansion_score}/100")
    
    if expansion_score >= 80:
        print(f"[🔥] HIGH PROBABILITY UPGRADE: Routing {client_id} to Account Executive for Tier-2 upsell.")
        return {"status": "upsell_ready", "score": expansion_score}
        
    return {"status": "stable", "score": expansion_score}

if __name__ == "__main__":
    calculate_expansion_probability("FinTech_Global", api_growth_rate=0.32, sentiment_score=0.91)
