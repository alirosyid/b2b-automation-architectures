import requests

def dispatch_ai_voice_closer(customer_phone, visual_quote_data):
    print(f"[Integrations] Initializing Vapi.ai outbound sales agent for {customer_phone}...")
    
    issue = visual_quote_data['analysis']['identified_issue']
    max_price = visual_quote_data['estimated_quote']['max_price']
    
    system_prompt = f"You are a professional dispatcher. Tell the customer our vision AI identified a {issue}. The max cost is ${max_price}. Ask if we can send a technician today."
    
    payload = {
        "phoneNumberId": "your-vapi-phone-id",
        "customer": {"number": customer_phone},
        "assistant": {
            "firstMessage": "Hi, this is the AI dispatch team calling about the photo you just uploaded.",
            "model": {"provider": "openai", "model": "gpt-4o", "messages": [{"role": "system", "content": system_prompt}]}
        }
    }
    
    print("[+] Vapi payload structured. Outbound AI call in progress...")
    # requests.post("https://api.vapi.ai/call/phone", json=payload, headers={"Authorization": "Bearer SECRETS"})
    return True

if __name__ == "__main__":
    mock_data = {"analysis": {"identified_issue": "leak repair"}, "estimated_quote": {"max_price": 400}}
    dispatch_ai_voice_closer("+15550198372", mock_data)
