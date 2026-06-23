def check_usage_telemetry(client_telemetry_data):
    for client_id, data in client_telemetry_data.items():
        hours_since_last_call = data.get("hours_inactive", 0)
        
        if hours_since_last_call >= 48:
            print(f"[Analytics] ⚠️ High Churn Risk: {client_id} inactive for {hours_since_last_call} hours.")
            _dispatch_rescue_sequence(client_id)
        else:
            print(f"[Analytics] {client_id} is healthy and active.")

def _dispatch_rescue_sequence(client):
    stealth_copy = f"Hey, noticed a drop in your infrastructure traffic today. Is everything running smoothly on your end, or do you need us to run a diagnostic?"
    print(f"[Analytics] Dispatching stealth rescue email:\n'{stealth_copy}'")

if __name__ == "__main__":
    telemetry = {
        "ENT-101": {"hours_inactive": 5},
        "ENT-102": {"hours_inactive": 52} # Triggers rescue
    }
    check_usage_telemetry(telemetry)
