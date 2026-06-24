def calculate_unit_economics(total_ad_spend, new_customers, avg_monthly_retainer, avg_lifespan_months):
    if new_customers == 0:
        return "Insufficient data."
        
    cac = total_ad_spend / new_customers
    ltv = avg_monthly_retainer * avg_lifespan_months
    
    ratio = ltv / cac
    
    print("--- B2B Unit Economics Dashboard ---")
    print(f"Customer Acquisition Cost (CAC): ${cac:.2f}")
    print(f"Lifetime Value (LTV): ${ltv:.2f}")
    print(f"LTV:CAC Ratio: {ratio:.1f}x")
    
    if ratio < 3.0:
        print("[!] Warning: Ratio below 3.0x. Marketing spend is inefficient.")
    else:
        print("[+] Ratio healthy. Green light to scale ad campaigns.")
        
    return ratio

if __name__ == "__main__":
    calculate_unit_economics(total_ad_spend=5000, new_customers=4, avg_monthly_retainer=3500, avg_lifespan_months=12)
