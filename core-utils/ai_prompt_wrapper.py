import os
import requests

def generate_ai_content(prompt, system_instruction="You are an expert copywriter."):
    api_key = os.getenv("AI_API_KEY", "your_api_key_here")
    url = "https://api.example.com/v1/chat/completions" # Replace with actual API endpoint
    
    payload = {
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # Mocking the response for safety
    print(f"[*] Sending prompt to AI: {prompt}")
    return "[Mock AI Output: 'Here is your high-converting stealth copy.']"

if __name__ == "__main__":
    print(generate_ai_content("Write a curiosity-driven opening sentence."))
