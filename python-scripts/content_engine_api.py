import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

app = FastAPI()
model = genai.GenerativeModel("gemini-2.5-flash")

class ContentRequest(BaseModel):
    transcript: str

@app.post("/repurpose")
async def repurpose(request: ContentRequest):
    try:
        prompt = f"""You are an elite B2B Marketing Copywriter. Convert the following raw transcript into 3 different highly engaging formats. CONSTRAINT: Output MUST be pure JSON with NO markdown formatting. JSON structure: {{"blog_article": "String (SEO optimized, use HTML tags for formatting)", "twitter_thread": ["String 1", "String 2", "String 3"], "linkedin_post": "String (Professional, engaging hook)"}}. Transcript: {request.transcript}"""
        
        response = model.generate_content(prompt)
        text_output = response.text.replace("```json\n", "").replace("```json", "").replace("```", "").strip()
        
        return json.loads(text_output)
    except Exception as e:
        return {"STATUS": "ERROR", "DETAIL": str(e)}
