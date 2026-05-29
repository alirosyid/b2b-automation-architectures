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

# DAFTAR HITAM SUPER KETAT (Mencegah job sampah masuk ke Llama-3)
BLACKLIST = [
    'support', 'customer', 'marketing', 'sales', 'accounting', 'designer', 
    'copywriter', 'media', 'counsel', 'account executive', 
    'devops', 'hr', 'recruiter', 'writer', 'finance', 'product manager',
    'qa', 'ios', 'android', 'frontend', 'mobile', 'security', 'crm', 
    'specialist', 'analyst', 'battery', 'garnishment', 'offensive', 'ui/ux', 'quality assurance', 'hardware'
]

# Kompilasi Regex di luar loop untuk performa maksimal
BLACKLIST_PATTERN = re.compile(r'\b(?:' + '|'.join(BLACKLIST) + r')\b', re.IGNORECASE)

# =====================================================================
# FUNGSI UTILITAS
# =====================================================================
def setup_google_sheets():
    # Mengambil kredensial dari environment variable
    gcp_service_account_json = os.environ.get('GCP_SERVICE_ACCOUNT')
    if not gcp_service_account_json:
        raise ValueError("Environment variable GCP_SERVICE_ACCOUNT belum di-set!")
    
    creds_dict = json.loads(gcp_service_account_json)
    
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    
    # Buka Spreadsheet
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

# =====================================================================
# MESIN EVALUASI (LOGIKA PENYARINGAN KETAT)
# =====================================================================
def evaluate_job(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    # FILTER 1: Tembok Daftar Hitam (Blokir instan dari Judul)
    if BLACKLIST_PATTERN.search(title_lower):
        print(f"   [BLOCKED] Judul masuk daftar hitam: {title}")
        return False
        
    # FILTER 2: Jalur VIP (Jika judul langsung menyebut kata kunci utama)
    if any(kw in title_lower for kw in PRIMARY_KEYWORDS):
        return True
        
    # FILTER 3: Kepadatan Kata Kunci di Deskripsi
    primary_match = sum(1 for kw in PRIMARY_KEYWORDS if kw in desc_lower)
    secondary_match = sum(1 for kw in SECONDARY_KEYWORDS if kw in desc_lower)
    
    # Lolos jika minimal ada 1 keyword utama ATAU 2 keyword pendukung di deskripsi
    if primary_match >= 1 or secondary_match >= 2:
        return True
        
    return False

# =====================================================================
# PROGRAM UTAMA
# =====================================================================
def main():
    print(f"=== Job Sniper Crawler (V2.0) Started at {datetime.now()} ===")
    
    try:
        sheet = setup_google_sheets()
        existing_links = get_existing_links(sheet)
        print(f"Berhasil terhubung ke Google Sheets. Ditemukan {len(existing_links)} link job unik.")
    except Exception as e:
        print(f"CRITICAL: Gagal menyiapkan Google Sheets - {e}")
        return

    # Custom headers untuk bypass Anti-Bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for source_name, url in RSS_FEEDS.items():
        print(f"\n-> Memproses sumber: {source_name} ({url})")
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            
            if feed.bozo:
                print(f"   [Peringatan] Parsing feed kurang sempurna: {feed.bozo_exception}")

            new_jobs_found = 0
            
            for entry in feed.entries:
                link = entry.get('link', '')
                
                if not link or link in existing_links:
                    continue
                
                if not is_recent(entry.get('published_parsed')):
                    continue
                
                title = entry.get('title', '')
                description = entry.get('description', entry.get('summary', ''))
                
                # Eksekusi Mesin Evaluasi "Sniper 2.0"
                if not evaluate_job(title, description):
                    continue
                
                # Bersihkan tag HTML
                clean_description = re.sub(r'<[^>]+>', '', html.unescape(description))[:2000]
                
                # Kolom: A(Waktu), B(Sumber), C(Posisi), D(Link), E(Deskripsi), F(Status)
                new_row = [scrape_time, source_name, title, link, clean_description, ""]
                
                try:
                    sheet.append_row(new_row)
                    existing_links.add(link)
                    new_jobs_found += 1
                    print(f"   [SUCCESS] Menyimpan Job Baru: {title}")
                    
                    # Jeda agar tidak terkena rate limit Google API
                    time.sleep(2)
                except Exception as g_error:
                    print(f"   [ERROR] Gagal menyimpan '{title}' ke sheet: {g_error}")
            
            print(f"   Selesai: {new_jobs_found} job baru disimpan dari {source_name}.")
            
        except Exception as e:
            print(f"   [ERROR] Terjadi kegagalan saat scrape feed {source_name}: {e}")

    print("\n=== Proses Scraping Job Selesai ===")

if __name__ == "__main__":
    main()
