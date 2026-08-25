import os
import time
import json
import requests
import feedparser
import gspread
from datetime import datetime, timedelta, timezone
from google.oauth2.service_account import Credentials
import html
import re

# =====================================================================
# KONFIGURASI SUMBER & PARAMETER WAKTU
# =====================================================================
RSS_FEEDS = {
    "WeWorkRemotely": "https://weworkremotely.com/remote-jobs.rss",
    "Upwork": "https://www.upwork.com/ab/feed/jobs/rss?q=python+OR+ai+OR+automation",
    "RemoteOK": "https://remoteok.com/remote-dev-jobs.rss",
    "Remotive": "https://remotive.com/remote-jobs/feed",
    "Jobspresso": "https://jobspresso.co/remote-software-jobs/feed/",
    "DailyRemote": "https://dailyremote.com/remote-jobs.rss",
    "Remote.co": "https://remote.co/remote-jobs/developer/feed/",
    "Working Nomads": "https://www.workingnomads.com/jobs/feed/development",
    "Himalayas": "https://himalayas.app/jobs/rss",
    "RemoteGlobal": "https://remoteglobal.com/jobs/feed/"
}

TIME_LIMIT_HOURS = 4

# =====================================================================
# SISTEM KATA KUNCI DUA LAPIS (THE SNIPER 2.0 FILTER)
# =====================================================================
PRIMARY_KEYWORDS = ['n8n', 'ai automation', 'ai agent', 'llm', 'langchain', 'openai', 'make.com', 'zapier', 'machine learning', 'chatgpt', 'artificial intelligence']
SECONDARY_KEYWORDS = ['python', 'api integration', 'process automation', 'workflow automation', 'chatbot', 'backend']

BLACKLIST = [
    'support', 'customer', 'marketing', 'sales', 'accounting', 'designer', 
    'copywriter', 'media', 'counsel', 'account executive', 
    'devops', 'hr', 'recruiter', 'writer', 'finance', 'product manager',
    'qa', 'ios', 'android', 'frontend', 'mobile', 'security', 'crm', 
    'specialist', 'analyst', 'battery', 'garnishment', 'offensive', 'ui/ux', 'quality assurance', 'hardware'
]

BLACKLIST_PATTERN = re.compile(r'\b(?:' + '|'.join(BLACKLIST) + r')\b', re.IGNORECASE)

def setup_google_sheets():
    gcp_service_account_json = os.environ.get('GCP_SERVICE_ACCOUNT')
    if not gcp_service_account_json:
        raise ValueError("Environment variable GCP_SERVICE_ACCOUNT belum di-set!")
    
    creds_dict = json.loads(gcp_service_account_json)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    
    # Memastikan terhubung ke sheet yang benar
    sheet = client.open("Data Job Sniper").sheet1
    return sheet

def is_recent(published_parsed):
    if not published_parsed:
        return False
    published_dt = datetime(*published_parsed[:6], tzinfo=timezone.utc)
    now_dt = datetime.now(timezone.utc)
    return (now_dt - published_dt) <= timedelta(hours=TIME_LIMIT_HOURS)

def get_existing_links(sheet):
    try:
        links = sheet.col_values(4)
        return set(links)
    except Exception as e:
        print(f"Error mengambil data dari baris/kolom Google Sheets: {e}")
        return set()

def evaluate_job(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    if BLACKLIST_PATTERN.search(title_lower):
        return False
        
    if any(kw in title_lower for kw in PRIMARY_KEYWORDS):
        return True
        
    primary_match = sum(1 for kw in PRIMARY_KEYWORDS if kw in desc_lower)
    secondary_match = sum(1 for kw in SECONDARY_KEYWORDS if kw in desc_lower)
    
    if primary_match >= 1 or secondary_match >= 2:
        return True
        
    return False

def main():
    print(f"=== Job Sniper Crawler (V2.0) Started at {datetime.now()} ===")
    
    try:
        sheet = setup_google_sheets()
        existing_links = get_existing_links(sheet)
        print(f"Berhasil terhubung ke Google Sheets. Ditemukan {len(existing_links)} link job unik.")
    except Exception as e:
        print(f"CRITICAL: Gagal menyiapkan Google Sheets - {e}")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for source_name, url in RSS_FEEDS.items():
        print(f"\n-> Memproses sumber: {source_name}")
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            new_jobs_found = 0
            
            for entry in feed.entries:
                link = entry.get('link', '')
                if not link or link in existing_links:
                    continue
                
                if not is_recent(entry.get('published_parsed')):
                    continue
                
                title = entry.get('title', '')
                description = entry.get('description', entry.get('summary', ''))
                
                if not evaluate_job(title, description):
                    continue
                
                clean_description = re.sub(r'<[^>]+>', '', html.unescape(description))[:2000]
                
                # PERBAIKAN FATAL: Memasukkan status "PENDING" agar dibaca oleh n8n
                new_row = [scrape_time, source_name, title, link, clean_description, "PENDING"]
                
                try:
                    sheet.append_row(new_row)
                    existing_links.add(link)
                    new_jobs_found += 1
                    time.sleep(2)
                except Exception as g_error:
                    print(f"   [ERROR] Gagal menyimpan '{title}': {g_error}")
            
            print(f"   Selesai: {new_jobs_found} job baru disimpan.")
            
        except Exception as e:
            print(f"   [ERROR] Gagal scrape {source_name}: {e}")

if __name__ == "__main__":
    main()
