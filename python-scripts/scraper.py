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

# --- URL RSS Feeds Dictionary ---
RSS_FEEDS = {
    "WeWorkRemotely": "https://weworkremotely.com/remote-jobs.rss",
    "Remote.co": "https://remote.co/remote-jobs/it/rss",
    "Upwork": "https://www.upwork.com/ab/feed/jobs/rss?q=python+OR+ai+OR+automation",
    "RemoteOK": "https://remoteok.com/remote-dev-jobs.rss",
    "Remotive": "https://remotive.com/remote-jobs/feed",
    "WorkingNomads": "https://www.workingnomads.com/jobs/feed"
}

KEYWORDS = ['n8n', 'workflow automation', 'ai automation', 'make.com', 'zapier', 'chatbot', 'llm integration', 'openai api', 'process automation']
TIME_LIMIT_HOURS = 4

def setup_google_sheets():
    # Mengambil kredensial dari environment variable
    gcp_service_account_json = os.environ.get('GCP_SERVICE_ACCOUNT')
    if not gcp_service_account_json:
        raise ValueError("Environment variable GCP_SERVICE_ACCOUNT belum di-set!")
    
    # Parse JSON creds
    creds_dict = json.loads(gcp_service_account_json)
    
    # Scopes untuk akses Sheets dan Drive
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    
    # Buka Spreadsheet
    # Pastikan untuk mengganti "Data Job Sniper" dengan nama atau ID file Google Sheets yang sebenarnya
    # Service account email harus sudah diundang (Share) sebagai Editor di file tersebut
    sheet = client.open("Data Job Sniper").sheet1
    return sheet

def is_recent(published_parsed):
    if not published_parsed:
        return False
    # Konversi feedparser struct_time ke datetime object dengan timezone UTC
    published_dt = datetime(*published_parsed[:6], tzinfo=timezone.utc)
    now_dt = datetime.now(timezone.utc)
    # Bandingkan rentang waktunya (<= 4 jam)
    return (now_dt - published_dt) <= timedelta(hours=TIME_LIMIT_HOURS)

def has_keywords(text):
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in KEYWORDS)

def get_existing_links(sheet):
    try:
        # Mengambil nilai pada kolom D (Indeks 4 di gspread)
        # Menghindari duplikasi parsing, gunakan set
        links = sheet.col_values(4)
        return set(links)
    except Exception as e:
        print(f"Error mengambil data dari baris/kolom Google Sheets: {e}")
        return set()

def main():
    print(f"=== Job Sniper Crawler Started at {datetime.now()} ===")
    
    # 1. Autentikasi Google Sheets
    try:
        sheet = setup_google_sheets()
        existing_links = get_existing_links(sheet)
        print(f"Berhasil terhubung ke Google Sheets. Ditemukan {len(existing_links)} link job unik.")
    except Exception as e:
        print(f"CRITICAL: Gagal menyiapkan Google Sheets - {e}")
        return

    # 2. Custom headers (Chrome User-Agent) untuk bypass Anti-Bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 3. Looping ke setiap resource feed RSS
    for source_name, url in RSS_FEEDS.items():
        print(f"\n-> Memproses sumber: {source_name} ({url})")
        
        try:
            # Gunakan requests agar header terjamin digunakan (bukan via feedparser internal)
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            
            if feed.bozo:
                print(f"   [Peringatan] Parsing feed kurang sempurna: {feed.bozo_exception}")

            new_jobs_found = 0
            
            for entry in feed.entries:
                link = entry.get('link', '')
                
                # Lewati jika sudah ada di Google Sheets
                if not link or link in existing_links:
                    continue
                
                # Filter #1: Waktu Publikasi (4 jam terakhir)
                if not is_recent(entry.get('published_parsed')):
                    continue
                
                title = entry.get('title', '')
                # Filter beberapa feed menyertakan summary, atau description
                description = entry.get('description', entry.get('summary', ''))
                
                # Filter #2: Keyword Spesifik
                if not (has_keywords(title) or has_keywords(description)):
                    continue
                
                # Job memenuhi semua kriteria: bersihkan tag html
                clean_description = re.sub(r'<[^>]+>', '', html.unescape(description))[:2000] # Batasi ukuran teks agar API tidak error
                
                # Kolom: A(Waktu), B(Sumber), C(Posisi), D(Link), E(Deskripsi), F(Status)
                new_row = [scrape_time, source_name, title, link, clean_description, ""]
                
                try:
                    sheet.append_row(new_row)
                    existing_links.add(link)
                    new_jobs_found += 1
                    print(f"   [SUCCESS] Menyimpan Job Baru: {title}")
                    
                    # Sleep 2 detik per insert untuk menghindari rate limiter Google Sheets API
                    time.sleep(2)
                except Exception as g_error:
                    print(f"   [ERROR] Gagal menyimpan '{title}' ke sheet: {g_error}")
            
            print(f"   Selesai: {new_jobs_found} job baru disimpan dari {source_name}.")
            
        except Exception as e:
            # Robustness: Satu error di satu feed tidak akan mematikan script
            print(f"   [ERROR] Terjadi kegagalan saat scrape feed {source_name}: {e}")

    print("\n=== Proses Scraping Job Selesai ===")

if __name__ == "__main__":
    main()
