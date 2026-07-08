def negotiate_rate_limit(vendor_name, vendor_support_email, current_limit, traffic_spike_data):
    print(f"[API Ops] 429 Rate Limit hit on {vendor_name}. Engaging Agentic Negotiator...")
    
    email_draft = f"""
    Hi {vendor_name} Support,
    
    Our infrastructure is currently hitting the {current_limit}/min rate limit threshold. Based on our current telemetry, we have sustained a {traffic_spike_data}% traffic spike due to a new enterprise deployment.
    
    To prevent webhook failures on our end, can we temporarily double this limit to {current_limit * 2}/min while we arrange an enterprise billing upgrade?
    """
    
    print("[+] Negotiation email dispatched automatically.")
    print("    -> Entering exponential backoff mode while awaiting vendor response.")
    # Mock SendGrid / Mailgun trigger
    return True

if __name__ == "__main__":
    negotiate_rate_limit("HubSpot", "api-support@hubspot.com", 100, 150)
