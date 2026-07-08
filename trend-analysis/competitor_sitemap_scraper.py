def monitor_sitemap_velocity(competitor_domain, previous_urls, current_urls):
    print(f"[*] Analyzing sitemap velocity for: {competitor_domain}")
    
    new_pages = list(set(current_urls) - set(previous_urls))
    
    if len(new_pages) > 20:
        print(f"[Trends] 🚨 MASSIVE SEO PUSH DETECTED: {competitor_domain} published {len(new_pages)} new pages.")
        print("    -> Extracting target keywords from new URL slugs...")
        
        keywords = [url.split("/")[-1].replace("-", " ") for url in new_pages[:3]]
        print(f"    -> Competitor is targeting: {keywords}")
        return {"action": "counter_campaign", "targets": keywords}
        
    print(f"[+] Competitor SEO velocity is low. ({len(new_pages)} new pages).")
    return {"action": "monitor"}

if __name__ == "__main__":
    old_urls = ["site.com/home", "site.com/pricing"]
    new_urls = old_urls + ["site.com/automation-for-lawyers", "site.com/automation-for-cpa"]
    monitor_sitemap_velocity("rival-agency.com", old_urls, new_urls)
