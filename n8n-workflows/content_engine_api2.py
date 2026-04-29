import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

app = FastAPI()

class ContentRequest(BaseModel):
    transcript: str

@app.post("/repurpose")
async def repurpose(request: ContentRequest):
    try:
        prompt = f"""ROLE: You are an Elite B2B Content Strategist and AI Automation Architect.
TASK: Analyze the provided transcript segment and engineer a comprehensive, multi-channel B2B content asset pack.
INPUT: {request.transcript}
OUTPUT: A strict JSON object containing all requested assets.
CONSTRAINTS: Do not use generic buzzwords. Tone must be authoritative, highly technical, and ROI-focused. You must escape all newline characters as \\n. Do NOT use raw line breaks. No markdown formatting in the output.
CAPABILITIES: You possess deep knowledge of B2B SaaS economics, lead generation pipelines, and algorithmic content distribution.

{{
  "seo_blog": "String (Long-form, HTML formatting for headers, highly authoritative)",
  "linkedin_post": "String (Professional, engaging hook, line breaks)",
  "x_thread": ["String 1", "String 2", "String 3"],
  "meta_title": "String",
  "meta_description": "String",
  "suggested_cta": "String",
  "email_newsletter": "String",
  "short_form_video_ideas": ["Idea 1", "Idea 2"],
  "content_calendar_suggestions": ["Suggestion 1", "Suggestion 2"],
  "client_specific_variation_example": "String (Show how the tone adapts for a specific industry like SaaS or FinTech)",
  "prompt_logic_used": "String (Briefly explain the angle used to extract the content)"
}}"""
        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        
        text_output = response.choices[0].message.content.replace("```json\n", "").replace("```json", "").replace("```", "").strip()
        
        return json.loads(text_output)
    except Exception as e:
        return {"STATUS": "ERROR", "DETAIL": str(e)}
