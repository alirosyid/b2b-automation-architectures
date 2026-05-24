import os
import json
import requests
import io
import urllib.parse
import urllib3
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Nonaktifkan peringatan SSL (Untuk bypass pemblokiran Reddit)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =====================================================================
# INISIALISASI ENVIRONMENT & APLIKASI UTAMA
# =====================================================================
load_dotenv()

app = FastAPI(title="Ali Rosyid - Enterprise B2B AI Gateway")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# =====================================================================
# DATA SCHEMAS
# =====================================================================
class Payload(BaseModel):
    company_data: str

class JobPayload(BaseModel):
    job_description: str

class ReplyPayload(BaseModel):
    sender_email: str
    email_body: str

# =====================================================================
# CORE LLM INFERENCE HELPER
# =====================================================================
def call_llama_gateway(prompt: str) -> dict:
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY tidak ditemukan di file .env")
        
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()
        
        if content.startswith("```json"):
            content = content.replace("```json", "", 1).rstrip("```").strip()
        elif content.startswith("```"):
            content = content.replace("```", "", 1).rstrip("```").strip()
            
        return json.loads(content)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Groq API Error: {str(e)}")

# =====================================================================
# LOKET 1, 2, 3, 4 (6-Component Prompt Framework)
# =====================================================================
@app.post("/enrich")
async def enrich_lead(payload: Payload):
    prompt = f"""
    Role: You are a world-class B2B IT Automation Architect.
    Task: Analyze the raw scraped website data to extract the company name, industry, and identify exactly 3 operational bottlenecks.
    Input: {payload.company_data}
    Output: Pure JSON structure {{'status': 'success', 'ai_analysis': {{'company': 'str', 'business_category': 'str', 'bottlenecks': [{{'issue': 'str', 'business_impact': 'str'}}]}}}}
    Constraints: NO markdown formatting. Exactly 3 bottlenecks.
    Capabilities: B2B profiling and operational risk assessment.
    """
    return call_llama_gateway(prompt)

@app.post("/analyze_job")
async def analyze_job(payload: JobPayload):
    prompt = f"""
    Role: You are an expert Enterprise Sales Strategist.
    Task: Analyze the job description to extract company, category, exact systemic bottlenecks, the name of the hiring manager, and the platform origin.
    Input: {payload.job_description}
    Output: Pure JSON structure ONLY.
    Constraints: 
    1. NO markdown formatting. Ensure the JSON is structurally valid.
    2. Extract the text NATURALLY. Do NOT force lowercase. Preserve proper capitalization for acronyms like AI, LLM, AWS, etc.
    3. If the platform origin is unclear, default to "LinkedIn".
    
    EXAMPLE OUTPUT FORMAT:
    {{
      "status": "success",
      "ai_analysis": {{
        "company": "SCC",
        "business_category": "Information Technology",
        "contact_person": "Bianca Ionescu",
        "source_platform": "LinkedIn",
        "bottlenecks": [
          {{
            "issue": "Lack of experienced AI/LLM architects with expertise in AWS Bedrock",
            "business_impact": "Inability to design and deliver enterprise-scale generative AI solutions"
          }}
        ]
      }}
    }}
    
    Capabilities: Technical gap analysis, contextual interpretation, and strict data extraction.
    """
    return call_llama_gateway(prompt)

@app.post("/generate_reply")
async def generate_reply(payload: ReplyPayload):
    try:
        kb_path = "knowledge_base.txt"
        knowledge_base = open(kb_path, "r", encoding="utf-8").read() if os.path.exists(kb_path) else "Informasi tidak ditemukan."
        prompt = f"""
        Role: You are the AI Assistant for a Senior AI Automation Architect.
        Task: Draft a professional email reply to a prospective client based strictly on the provided Knowledge Base.
        Input: Email: {payload.email_body} | KB: {knowledge_base}
        Output: Pure JSON structure {{'status': 'success', 'client_intent': 'str', 'draft_reply': 'str'}}
        Constraints: NO markdown. Reject hourly rates, focus on project-based or retainer.
        Capabilities: B2B direct-response copywriting and objection handling.
        """
        return call_llama_gateway(prompt)
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/ocr")
async def process_document(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY tidak ditemukan.")
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        prompt = """
        Role: Precise Data Extraction Agent.
        Task: Extract billing data from the document into a pure JSON format.
        Input: The attached image.
        Output: Pure JSON {'Vendor_Name': 'str', 'Invoice_Number': 'str', 'Date': 'YYYY-MM-DD', 'Total_Amount': number, 'Line_Items': [{'item_name': 'str', 'price': number}]}
        Constraints: STRICTLY NO MARKDOWN. Fill missing data with null.
        Capabilities: High-fidelity OCR mapping.
        """
        response = model.generate_content([prompt, image])
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return {"status": "success", "extracted_data": json.loads(clean_text)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =====================================================================
# LOKET 5: THE PERFECTED SNIPER V10 (SSL Bypass + Money Filter)
# =====================================================================
@app.get("/scan_leads")
async def scan_urgent_leads():
    all_leads = []
    diagnostics = {"google_linkedin": "Not Run", "github": "Not Run", "reddit": "Not Run"}
    
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CX_ID = os.getenv("CX_ID")
    
    # Kumpulan kata kunci pembawa uang (Filter Target)
    TARGET_KEYWORDS = ["freelance", "hiring", "hire", "urgent", "pay", "bounty", "project", "budget", "need help", "error", "bug", "stuck", "solution", "n8n", "python", "api"]
    
    # ---------------------------------------------------------
    # MESIN A: GOOGLE API (LinkedIn & Upwork)
    # ---------------------------------------------------------
    if GOOGLE_API_KEY and CX_ID:
        google_queries = [
            'site:linkedin.com/posts/ "n8n" OR "python automation"',
            'site:upwork.com/freelance-jobs/ "n8n" OR "fastapi"'
        ]
        total_google_found = 0
        
        for q in google_queries:
            try:
                url = f"https://www.googleapis.com/customsearch/v1?q={urllib.parse.quote(q)}&key={GOOGLE_API_KEY}&cx={CX_ID}&dateRestrict=m[1]"
                res = requests.get(url, timeout=10)
                if res.status_code == 200:
                    items = res.json().get('items', [])
                    for item in items:
                        link = item.get('link', '')
                        if "linkedin.com/posts/" in link or "upwork.com/freelance-jobs/" in link:
                            all_leads.append({
                                "title": f"[VIP] {item.get('title', '')[:60]}",
                                "link": link,
                                "snippet": item.get('snippet', '')
                            })
                            total_google_found += 1
                    diagnostics["google_linkedin"] = f"SUCCESS: Ditemukan {total_google_found} data mentah."
                else:
                    diagnostics["google_linkedin"] = f"ERROR {res.status_code}: {res.json().get('error', {}).get('message', 'Unknown Error')}"
            except Exception as e:
                diagnostics["google_linkedin"] = f"EXCEPTION: {str(e)}"
    else:
        diagnostics["google_linkedin"] = "KOSONG: GOOGLE_API_KEY atau CX_ID tidak ada di .env"

    # ---------------------------------------------------------
    # MESIN B: GITHUB API (Open Issues)
    # ---------------------------------------------------------
    try:
        gh_url = "https://api.github.com/search/issues?q=n8n+state:open+(label:help-wanted OR label:bug)"
        gh_res = requests.get(gh_url, headers={"Accept": "application/vnd.github.v3+json"}, timeout=10)
        if gh_res.status_code == 200:
            items = gh_res.json().get("items", [])[:10]
            for item in items:
                all_leads.append({
                    "title": f"[GitHub] {item.get('title', '')[:60]}",
                    "link": item.get('html_url', ''),
                    "snippet": str(item.get('body', 'Tidak ada deskripsi'))[:200]
                })
            diagnostics["github"] = f"SUCCESS: Ditemukan {len(items)} data mentah."
        else:
            diagnostics["github"] = f"ERROR {gh_res.status_code}: Rate Limit GitHub."
    except Exception as e:
        diagnostics["github"] = f"EXCEPTION: {str(e)}"

    # ---------------------------------------------------------
    # MESIN C: REDDIT (Dengan SSL Bypass)
    # ---------------------------------------------------------
    try:
        reddit_queries = ["n8n", "python automation"]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ali-B2B-Scout/10.0"}
        total_reddit_found = 0
        
        for q in reddit_queries:
            url = f"https://www.reddit.com/search.json?q={urllib.parse.quote(q)}&sort=new"
            # verify=False menembus pemblokiran SSL Handshake
            red_res = requests.get(url, headers=headers, timeout=10, verify=False)
            if red_res.status_code == 200:
                items = red_res.json().get("data", {}).get("children", [])[:10]
                for child in items:
                    post = child.get("data", {})
                    all_leads.append({
                        "title": f"[Reddit] {post.get('title', '')[:60]}",
                        "link": f"https://www.reddit.com{post.get('permalink', '')}",
                        "snippet": str(post.get("selftext", "Tidak ada deskripsi"))[:200]
                    })
                    total_reddit_found += 1
                diagnostics["reddit"] = f"SUCCESS: Ditemukan {total_reddit_found} data mentah."
            else:
                diagnostics["reddit"] = f"ERROR {red_res.status_code}: Blokir Reddit."
    except Exception as e:
        diagnostics["reddit"] = f"EXCEPTION: {str(e)}"

    # ---------------------------------------------------------
    # LAYER FILTERING FINAL (B2B TARGETING)
    # ---------------------------------------------------------
    filtered_leads = []
    for lead in all_leads:
        content_to_check = (lead['title'] + " " + str(lead['snippet'])).lower()
        # Simpan hanya jika mengandung kata kunci potensial cuan
        if any(keyword in content_to_check for keyword in TARGET_KEYWORDS):
            filtered_leads.append(lead)
            
    # Hilangkan URL duplikat
    unique_leads = {lead['link']: lead for lead in filtered_leads if "http" in lead['link']}.values()
            
    if not unique_leads:
        return {
            "status": "success", 
            "DIAGNOSTICS_REPORT": diagnostics,
            "leads_found": 1, 
            "data": [{"title": "[SYSTEM STANDBY] Filter B2B Aktif", "link": "https://alirosyid.com/standby", "snippet": "Data mentah berhasil ditarik, tetapi tidak ada yang mengandung kata kunci pembayaran/proyek hari ini."}]
        }

    return {
        "status": "success", 
        "DIAGNOSTICS_REPORT": diagnostics,
        "leads_found": len(unique_leads), 
        "data": list(unique_leads)
    }
