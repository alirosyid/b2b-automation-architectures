def forecast_unit_economics(ad_spend, leads_generated, predicted_close_rate, avg_retainer):
    print("[Analytics] Executing predictive LTV:CAC modeling for current cohort...")
    
    if leads_generated == 0:
        return "Insufficient data"
        
    cac = ad_spend / (leads_generated * predicted_close_rate)
    predicted_ltv = avg_retainer * 12 # Assuming 12 month retention baseline
    
    ltv_cac_ratio = predicted_ltv / cac if cac > 0 else 0
    
    print(f"    -> Predicted CAC: ${cac:,.2f}")
    print(f"    -> Predicted LTV: ${predicted_ltv:,.2f}")
    print(f"    -> Forecased LTV:CAC Ratio: {ltv_cac_ratio:.1f}x")
    
    if ltv_cac_ratio < 3.0:
        print("[!] 🛑 WARNING: Unit economics predict unprofitable scaling. Sending webhook to pause ad sets.")
        return {"status": "unprofitable", "action": "pause_ads"}
        
    print("[+] Cohort economics highly profitable. Green light to scale spend.")
    return {"status": "profitable", "action": "scale"}

if __name__ == "__main__":
    forecast_unit_economics(ad_spend=2500, leads_generated=40, predicted_close_rate=0.10, avg_retainer=3500)
