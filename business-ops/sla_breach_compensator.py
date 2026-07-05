def calculate_sla_compensation(client_id, monthly_retainer, downtime_minutes):
    allowed_downtime = 43.2 # 99.9% uptime per month in minutes
    
    if downtime_minutes <= allowed_downtime:
        print(f"[BizOps] SLA maintained for {client_id}. No compensation required.")
        return 0
        
    breach_minutes = downtime_minutes - allowed_downtime
    # Penalty calculation: 1% of retainer per 60 minutes of breach
    penalty_percentage = (breach_minutes / 60) * 0.01
    credit_amount = monthly_retainer * penalty_percentage
    
    print(f"[BizOps] 🚨 SLA Breach for {client_id}. Downtime: {downtime_minutes}m.")
    print(f"[BizOps] Autonomously issuing Stripe credit memo for ${credit_amount:.2f}.")
    return credit_amount

if __name__ == "__main__":
    calculate_sla_compensation("Enterprise_Logistics", 15000, downtime_minutes=120)
