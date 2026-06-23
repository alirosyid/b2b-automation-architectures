def scan_and_bid(job_listings):
    target_keywords = ["n8n", "api integration", "workflow automation"]
    bids_submitted = 0
    
    for job in job_listings:
        title = job.get("title", "").lower()
        budget = job.get("budget", 0)
        
        if budget >= 2000 and any(kw in title for kw in target_keywords):
            print(f"[Scraping] 🎯 High-ticket match found: '{job['title']}' (${budget})")
            print("[Scraping] Submitting stealth proposal...")
            # Mock API submission
            bids_submitted += 1
            
    return bids_submitted

if __name__ == "__main__":
    mock_jobs = [
        {"title": "Need complex n8n CRM integration", "budget": 3500},
        {"title": "Simple data entry", "budget": 50}
    ]
    scan_and_bid(mock_jobs)
