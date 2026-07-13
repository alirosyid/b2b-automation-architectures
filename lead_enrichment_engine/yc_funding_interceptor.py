def intercept_funding_events(live_funding_stream):
    print("[Lead Gen] Intercepting global funding firehose for high-budget targets...")
    
    actionable_targets = []
    for event in live_funding_stream:
        if event["round"] in ["Series A", "Series B"] and event["amount_raised"] >= 5000000:
            print(f"[🔥] SCALING EVENT: {event['company']} just raised ${event['amount_raised']:,}.")
            
            enrichment_payload = {
                "company": event["company"],
                "pitch_angle": "Infrastructure scaling post-funding",
                "target_persona": "CTO / VP of Engineering"
            }
            actionable_targets.append(enrichment_payload)
            print("    -> Routing intelligence payload directly to outbound n8n orchestrator.")
            
    return actionable_targets

if __name__ == "__main__":
    stream = [{"company": "DataScale", "round": "Series A", "amount_raised": 12000000}]
    intercept_funding_events(stream)
