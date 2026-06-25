def forecast_quarterly_revenue(active_deals, historical_win_rate):
    projected_revenue = 0
    
    for deal in active_deals:
        stage_probability = deal.get("probability", 0.1)
        deal_value = deal.get("value", 0)
        
        # Adjusted by historical agency performance
        adjusted_probability = stage_probability * historical_win_rate
        projected_revenue += (deal_value * adjusted_probability)
        
    print("--- B2B Revenue Forecast ---")
    print(f"Total Active Deals: {len(active_deals)}")
    print(f"Historical Win Rate Baseline: {historical_win_rate * 100}%")
    print(f"Projected Quarterly Revenue: ${projected_revenue:,.2f}")
    
    return projected_revenue

if __name__ == "__main__":
    deals = [
        {"client": "TechFlow", "value": 15000, "probability": 0.5},
        {"client": "DataSync", "value": 45000, "probability": 0.8}
    ]
    forecast_quarterly_revenue(deals, historical_win_rate=0.75)
