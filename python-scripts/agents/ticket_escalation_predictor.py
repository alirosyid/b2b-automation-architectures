def predict_escalation_risk(ticket_text, client_tier):
    print(f"[Support Ops] Analyzing emotional trajectory of inbound {client_tier} ticket...")
    
    escalation_keywords = ["unacceptable", "cancel", "refund", "breach", "failing"]
    risk_score = 0
    
    for word in escalation_keywords:
        if word in ticket_text.lower():
            risk_score += 35
            
    if client_tier == "Enterprise":
        risk_score += 20 # Enterprise clients naturally carry higher risk
        
    print(f"    -> Calculated Escalation Risk: {risk_score}/100")
    
    if risk_score >= 50:
        print("[!] 🚨 CRITICAL ESCALATION: Bypassing Tier 1. Routing directly to VIP Retention Swarm.")
        return "VIP_Swarm"
        
    print("[+] Standard priority. Routing to Tier 1 automated resolution.")
    return "Tier_1_Queue"

if __name__ == "__main__":
    ticket = "This downtime is unacceptable, we are going to cancel our contract."
    predict_escalation_risk(ticket, "Enterprise")
