def analyze_and_negotiate_billing(current_bill, market_rates):
    print("[FinOps Agent] Analyzing monthly cloud expenditure against spot market rates...")
    
    if current_bill > market_rates['average_baseline'] * 1.2:
        print("[!] Overpaying for compute by > 20%. Initiating autonomous arbitrage protocol.")
        
        draft = f"Our automated FinOps analysis indicates our current AWS compute rates are 20% above the open spot market average. We are preparing to route infrastructure to GCP unless a custom discount is applied to our enterprise tier."
        
        print("[+] Negotiation payload drafted for AWS Account Manager.")
        return draft
        
    print("[+] Cloud costs are highly optimized.")
    return "Optimized"

if __name__ == "__main__":
    analyze_and_negotiate_billing(15000, {"average_baseline": 11000})
