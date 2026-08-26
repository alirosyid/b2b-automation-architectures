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
# KONFIGURASI SUMBER RSS (HANYA BOARD DENGAN KUALITAS REMOTE GLOBAL)
# =====================================================================
RSS_FEEDS = {
    "WeWorkRemotely": "https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss",
    "RemoteOK": "https://remoteok.com/remote-dev-jobs.rss",
    "Remotive": "https://remotive.com/remote-jobs/software-dev/feed",
    "WorkingNomads": "https://www.workingnomads.com/jobs/feed/development",
    "Jobspresso": "https://jobspresso.co/remote-software-jobs/feed/",
    "Remote.co": "https://remote.co/remote-jobs/developer/feed/",
    "Himalayas": "https://himalayas.app/jobs/rss",
    "Upwork_Tech": "https://www.upwork.com/ab/feed/jobs/rss?q=n8n+OR+fastapi+OR+python+backend"
}

TIME_LIMIT_HOURS = 24 # Disesuaikan karena cron job berjalan 1x sehari

# =====================================================================
# SISTEM KATA KUNCI (THE SNIPER 3.0 FILTER)
# =====================================================================
PRIMARY_KEYWORDS = ['n8n', 'ai automation', 'ai agent', 'llm', 'rag', 'fastapi', 'openai', 'make.com', 'zapier', 'machine learning', 'chatgpt']
SECONDARY_KEYWORDS = ['python', 'api integration', 'process automation', 'workflow', 'backend developer', 'data extraction']

# DAFTAR HITAM KETAT (Membuang peran non-teknis)
BLACKLIST = [
    'support', 'customer', 'marketing', 'sales', 'accounting', 'designer', 
    'copywriter', 'media', 'counsel', 'account executive', 
    'devops', 'hr', 'recruiter', 'writer', 'finance', 'product manager',
    'qa', 'ios', 'android', 'frontend', 'mobile', 'security', 'crm', 
    'ui/ux', 'quality assurance', 'hardware'
]

# DAFTAR HITAM GEOGRAFIS (Menendang loker yang khusus warga negara tertentu)
GEO_BLACKLIST = [
    'us only', 'usa only', 'must reside in the us', 'must reside in the united states',
    'uk only', 'europe only', 'eu only', 'clearance required', 'citizens only', 
    'must be located in', 'timezone restricted', 'north america only'
]

BLACKLIST_PATTERN = re.compile(r'\b(?:' + '|'.join(BLACKLIST) + r')\b', re.IGNORECASE)
GEO_BLACKLIST_PATTERN = re.compile(r'\b(?:' + '|'.join(GEO_BLACKLIST) + r')\b', re.IGNORECASE)

# =====================================================================
# FUNGSI UTILITAS
# =====================================================================
def setup_google_sheets():
    gcp_service_account_json = os.environ.get('GCP_SERVICE_ACCOUNT')
    if not gcp_service_account_json:
        raise ValueError("Environment variable GCP_SERVICE_ACCOUNT belum di-set!")
    
    creds_dict = json.loads(gcp_service_account_json)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    
    # GANTI STRING INI JIKA NAMA FILE GOOGLE SHEETS ANDA BERBEDA
    sheet = client.open("Data Job Sniper").sheet1
    return sheet

def is_recent(published_parsed):
    if not published_parsed:
        return True # Asumsikan baru jika tidak ada tanggal
    published_dt = datetime(*published_parsed[:6], tzinfo=timezone.utc)
    now_dt = datetime.now(timezone.utc)
    return (now_dt - published_dt) <= timedelta(hours=TIME_LIMIT_HOURS)

def get_existing_links(sheet):
    try:
        links = sheet.col_values(4) # Asumsi link ada di kolom D (indeks 4)
        return set(links)
    except Exception as e:
        print(f"Error mengambil data dari Google Sheets: {e}")
        return set()

# =====================================================================
# MESIN EVALUASI (LOGIKA PENYARINGAN KETAT)
# =====================================================================
def evaluate_job(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    # 1. Tembok Daftar Hitam Peran
    if BLACKLIST_PATTERN.search(title_lower):
        return False
        
    # 2. Tembok Daftar Hitam Geografis (Sangat Penting untuk Kandidat Global)
    if GEO_BLACKLIST_PATTERN.search(desc_lower) or GEO_BLACKLIST_PATTERN.search(title_lower):
        print(f"   [BLOCKED GEO] Terkena blokir area: {title}")
        return False
        
    # 3. Jalur VIP (Judul langsung menyebut kata kunci)
    if any(kw in title_lower for kw in PRIMARY_KEYWORDS):
        return True
        
    # 4. Evaluasi Deskripsi
    primary_match = sum(1 for kw in PRIMARY_KEYWORDS if kw in desc_lower)
    secondary_match = sum(1 for kw in SECONDARY_KEYWORDS if kw in desc_lower)
    
    if primary_match >= 1 or secondary_match >= 2:
        return True
        
    return False

# =====================================================================
# PROGRAM UTAMA
# =====================================================================
def main():
    print(f"=== Job Sniper Crawler Global B2B (V3.0) Started at {datetime.now()} ===")
    
    try:
        sheet = setup_google_sheets()
        existing_links = get_existing_links(sheet)
        print(f"Berhasil terhubung. Ditemukan {len(existing_links)} link unik di database.")
    except Exception as e:
        print(f"CRITICAL: Gagal menyiapkan Google Sheets - {e}")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for source_name, url in RSS_FEEDS.items():
        print(f"\n-> Memindai: {source_name}")
        
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
                
                # Kolom: A(Waktu), B(Sumber), C(Posisi), D(Link), E(Deskripsi), F(Status)
                # STATUS WAJIB 'PENDING' AGAR DISAMBAR OLEH n8n
                new_row = [scrape_time, source_name, title, link, clean_description, "PENDING"]
                
                try:
                    sheet.append_row(new_row)
                    existing_links.add(link)
                    new_jobs_found += 1
                    print(f"   [+] Emas ditemukan: {title}")
                    time.sleep(1.5)
                except Exception as g_error:
                    print(f"   [ERROR] Gagal menyimpan ke sheet: {g_error}")
            
            print(f"   Selesai: {new_jobs_found} lead berkualitas ditambahkan.")
            
        except Exception as e:
            print(f"   [ERROR] Gagal scrape {source_name}: {e}")

    print("\n=== Operasi Selesai ===")

if __name__ == "__main__":
    main()
