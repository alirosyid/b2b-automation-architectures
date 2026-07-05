def normalize_payload_schema(raw_payload):
    print("[Integrations] Intercepted unstructured inbound payload. Normalizing via LLM...")
    
    # Mock LLM dynamically mapping weird keys to standard CRM keys
    standard_schema = {
        "first_name": raw_payload.get("FirstName", raw_payload.get("fname", "Unknown")),
        "company_revenue": raw_payload.get("AnnualRev", raw_payload.get("company_size_usd", 0)),
        "source": "Normalized Webhook"
    }
    
    print("[+] Payload successfully mapped to unified B2B Hubspot schema.")
    return standard_schema

if __name__ == "__main__":
    weird_facebook_payload = {"fname": "Bruce", "company_size_usd": 5000000}
    print(normalize_payload_schema(weird_facebook_payload))
