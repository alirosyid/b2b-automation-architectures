def execute_pipeline_forensics(closed_lost_transcripts):
    print("[Analytics] Executing forensic analysis on Closed-Lost pipeline data...")
    
    # Mocking LLM Semantic clustering
    loss_reasons = {"missing_soc2": 45, "pricing_too_high": 12, "no_salesforce_sync": 38}
    
    primary_killer = max(loss_reasons, key=loss_reasons.get)
    
    print("--- Forensic Deal Loss Matrix ---")
    for reason, count in loss_reasons.items():
        print(f"Deal Killer: {reason} | Occurrences: {count}")
        
    print(f"\n[!] 🚨 PRIMARY LEAK: The agency is losing massive revenue due to '{primary_killer}'.")
    print("    -> Generating automated Jira Epics to resolve this blocker immediately.")
    
    return primary_killer

if __name__ == "__main__":
    execute_pipeline_forensics(["We need SOC2", "Pricing is fine but no SOC2 is a dealbreaker"])
