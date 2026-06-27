def calculate_health_score(api_usage_trend, outstanding_tickets, invoice_days_late):
    score = 100
    
    # Deductions based on risk factors
    if api_usage_trend < 0:
        score -= (abs(api_usage_trend) * 100) # e.g., 20% drop = -20 points
        
    score -= (outstanding_tickets * 5)
    
    if invoice_days_late > 0:
        score -= (invoice_days_late * 2)
        
    score = max(0, min(100, score))
    
    print(f"[Analytics] Client Health Score calculated: {score}/100")
    
    if score < 50:
        print("[!] CRITICAL: Account at severe risk of churn. Immediate intervention required.")
        
    return score

if __name__ == "__main__":
    # 15% drop in usage, 3 open tickets, 5 days late on invoice
    calculate_health_score(api_usage_trend=-0.15, outstanding_tickets=3, invoice_days_late=5)
