def map_competitor_features(competitor_domain, latest_release_notes, internal_feature_matrix):
    print(f"[Market Intel] Mapping new features from {competitor_domain} against internal matrix...")
    
    feature_gaps = []
    
    for feature in latest_release_notes:
        if feature not in internal_feature_matrix:
            print(f"[!] 🚨 COMPETITIVE GAP DETECTED: Competitor just shipped '{feature}'.")
            feature_gaps.append(feature)
            
    if feature_gaps:
        print(f"[+] Drafting urgent Jira Epics for {len(feature_gaps)} missing features.")
        return {"status": "gaps_identified", "missing_features": feature_gaps}
        
    print("[+] Agency maintains feature parity. No immediate threats detected.")
    return {"status": "parity_maintained"}

if __name__ == "__main__":
    competitor_notes = ["SOC2 Compliance Automation", "Multi-Agent Swarms", "Basic Zapier Integration"]
    our_matrix = ["Multi-Agent Swarms", "Basic Zapier Integration"]
    map_competitor_features("RivalAutomations.io", competitor_notes, our_matrix)
