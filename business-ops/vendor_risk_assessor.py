def assess_vendor_risk(vendor_domain, cve_database):
    print(f"[BizOps] Initiating automated Third-Party Risk Assessment (TPRA) for {vendor_domain}...")
    
    risk_score = 0
    threats = []
    
    if vendor_domain in cve_database:
        risk_score += 50
        threats.append("Recent unpatched CVE found.")
        
    # Mocking compliance scan
    soc2_compliant = True
    
    if not soc2_compliant:
        risk_score += 30
        threats.append("Lacks SOC2 Type II compliance.")
        
    if risk_score > 40:
        print(f"[!] Vendor rejected. Risk score ({risk_score}) exceeds enterprise thresholds: {threats}")
        return {"status": "rejected", "score": risk_score}
        
    print(f"[+] Vendor approved. Risk score ({risk_score}) is within acceptable limits.")
    return {"status": "approved", "score": risk_score}

if __name__ == "__main__":
    assess_vendor_risk("new-ai-tool.io", ["new-ai-tool.io"])
