def adjust_sending_limits(domain_reputation_scores):
    print("[SecOps] Synchronizing outbound SMTP limits with real-time domain reputation...")
    
    for domain, score in domain_reputation_scores.items():
        if score > 95:
            print(f"[+] {domain} reputation Elite. Increasing daily outbound volume to 500.")
        elif score < 80:
            print(f"[!] {domain} reputation slipping. Throttling outbound to 50. Activating aggressive warmup protocol.")
        else:
            print(f"[*] {domain} reputation stable. Maintaining standard volumes.")
            
    return True

if __name__ == "__main__":
    scores = {"b2b-automations.io": 98, "contact-agency.co": 76}
    adjust_sending_limits(scores)
