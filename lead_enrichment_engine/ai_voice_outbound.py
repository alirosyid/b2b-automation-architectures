def trigger_ai_voice_agent(lead_name, phone_number, intent_context):
    print(f"[Lead Gen] High intent detected. Booting AI Voice Agent for {lead_name}...")
    
    system_prompt = f"You are an AI SDR. Call {lead_name}. They just requested a quote for {intent_context}. Qualify their budget gently and book a Zoom meeting."
    
    # Mock API call to Vapi.ai / Bland AI
    api_payload = {
        "phone_number": phone_number,
        "prompt": system_prompt,
        "voice_id": "professional_female_1"
    }
    
    print(f"[+] Outbound call initiated to {phone_number}. Awaiting call transcript and BANT extraction.")
    return {"status": "calling", "payload": api_payload}

if __name__ == "__main__":
    trigger_ai_voice_agent("Sarah Jenkins", "+15550198472", "Custom n8n Architecture")
