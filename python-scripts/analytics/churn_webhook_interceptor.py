def intercept_and_score_activity(client_id, activity_type, session_duration):
    print(f"[Analytics] Intercepting session telemetry for {client_id}...")
    
    # Mathematical churn vector mapping
    churn_probability = 0.0
    
    if activity_type == "export_all_data":
        churn_probability += 0.85
    elif activity_type == "delete_api_key":
        churn_probability += 0.60
        
    if churn_probability > 0.80:
        print(f"[!] 🚨 CRITICAL CHURN VECTOR: {client_id} exhibits pre-cancellation behavior.")
        print("[+] Halting standard webhook routing. Injecting emergency retention offer into UI.")
        return {"action": "trigger_retention_flow", "discount_auth": True}
        
    print("[+] Session telemetry normal. Routing to standard analytics warehouse.")
    return {"action": "log_telemetry"}

if __name__ == "__main__":
    intercept_and_score_activity("Enterprise_Logistics", "export_all_data", 45)
