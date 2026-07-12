def crawl_competitor_changelog(competitor_domain, new_release_notes):
    print(f"[Market Intel] Scanning {competitor_domain}/changelog for architectural shifts...")
    
    strategic_threats = []
    for note in new_release_notes:
        if "AI" in note or "Automated" in note or "Enterprise" in note:
            strategic_threats.append(note)
            
    if strategic_threats:
        print(f"[!] Strategic alert: {competitor_domain} shipped {len(strategic_threats)} high-impact features.")
        for threat in strategic_threats:
            print(f"    -> {threat}")
        print("[+] Compiling market intelligence report for product leadership.")
        return strategic_threats
        
    print("[+] No major architectural threats detected in current cycle.")
    return []

if __name__ == "__main__":
    mock_notes = ["Added AI Agent orchestration", "Fixed minor CSS bug in header"]
    crawl_competitor_changelog("competing-agency.io", mock_notes)
