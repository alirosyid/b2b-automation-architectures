import os
from twilio.rest import Client
from openai import OpenAI

def initiate_b2b_sales_call(to_number, prospect_name, company_name):
    """Initiates an autonomous AI sales call using Twilio and OpenAI Realtime."""
    twilio_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    # Generate contextual prompt for the AI Agent
    system_prompt = f"You are a senior SDR calling {prospect_name} from {company_name}. Your goal is to qualify them for our AI automation services and book a 15-min demo."
    
    # Twilio TwiML routing to our WebSocket Server hosting the OpenAI Realtime API
    call = twilio_client.calls.create(
        url="https://api.yourdomain.com/voice/stream",
        to=to_number,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        machine_detection="Enable" # Skip voicemails
    )
    
    print(f"Initiated AI outreach to {prospect_name}. Call SID: {call.sid}")
    return call.sid

if __name__ == "__main__":
    initiate_b2b_sales_call("+1234567890", "John Doe", "TechCorp Inc.")
