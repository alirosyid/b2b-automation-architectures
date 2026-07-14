def calculate_churn_probability(api_usage_delta, invoice_delay_days, support_engagement):
    print("[Analytics] Running Churn Prediction Matrix on enterprise portfolio...")
    
    risk_score = 0.0
    
    if api_usage_delta < -0.20: risk_score += 0.40 # 20% drop in usage
    if invoice_delay_days > 15: risk_score += 0.35
    if support_engagement == "zero_for_60_days": risk_score += 0.25
    
    print(f"    -> Calculated Churn Probability: {risk_score * 100}%")
    
    if risk_score >= 0.70:
        print("[!] 🚨 CRITICAL CHURN RISK. Dispatching automated retention playbook to Account Executive.")
        return "High Risk"
        
    return "Stable"

if __name__ == "__main__":
    # Client has dropped usage by 25% and is 16 days late on payment
    calculate_churn_probability(api_usage_delta=-0.25, invoice_delay_days=16, support_engagement="active")
