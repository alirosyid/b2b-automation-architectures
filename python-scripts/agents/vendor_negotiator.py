import os
from openai import OpenAI

def draft_vendor_counter_offer(vendor_name, current_price, usage_utilization, llm_client):
    prompt = f"""
    You are a strict B2B procurement manager. {vendor_name} wants to renew at ${current_price}. 
    Our usage utilization was only {usage_utilization}%. 
    Draft a professional, assertive email requesting a 20% discount based on low utilization.
    """
    
    response = llm_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    email_draft = draft_vendor_counter_offer("DataCloud Inc", 5000, 45, client)
    print("Drafted Email:\n", email_draft)
