def synthesize_gtm_strategy(competitor_data):
    print(f"[Agent] Synthesizing counter-GTM strategy for competitor profile...")
    
    weaknesses = competitor_data.get("weaknesses", [])
    
    strategy = f"""
    # GTM Action Plan: Intercepting Competitor Traffic
    
    ## Positioning
    They are weak in {weaknesses[0]}. We must highlight our 99.9% uptime SLA in all outbound copy.
    
    ## Pricing Arbitrage
    Their enterprise tier starts at $5k/mo. Launch a targeted ad campaign offering a $3.5k/mo migration package.
    """
    
    print("[+] GTM Strategy drafted. Pushing to Notion leadership portal.")
    return strategy

if __name__ == "__main__":
    mock_data = {"weaknesses": ["Custom Integrations", "Customer Support Speed"]}
    synthesize_gtm_strategy(mock_data)
