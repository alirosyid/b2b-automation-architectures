import requests
import os

def generate_personalized_sales_video(prospect_name, prospect_company, heygen_api_key):
    """Generates a personalized AI avatar video for B2B cold outreach."""
    url = "https://api.heygen.com/v2/video/generate"
    headers = {
        "X-Api-Key": heygen_api_key,
        "Content-Type": "application/json"
    }
    
    script_text = f"Hi {prospect_name}, I saw the recent growth at {prospect_company}. I made this quick video to show how our AI architecture can scale your operations."
    
    payload = {
        "video_inputs": [
            {
                "character": {"type": "avatar", "avatar_id": "YOUR_CUSTOM_AVATAR_ID"},
                "voice": {"type": "text", "input_text": script_text, "voice_id": "EN-US_MALE_1"}
            }
        ],
        "test": True, # Set to False for production
        "aspect_ratio": "16:9"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Video generation queued successfully:", response.json().get('data', {}).get('video_id'))
    else:
        print("HeyGen API Error:", response.text)

if __name__ == "__main__":
    generate_personalized_sales_video("Sarah", "TechFlow Inc.", os.getenv("HEYGEN_API_KEY"))
