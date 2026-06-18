import time

def monitor_sla(job_id, client_tier, execution_time, sla_limit=60):
    if execution_time > sla_limit:
        print(f"[!] SLA BREACH: Job {job_id} took {execution_time}s (Limit: {sla_limit}s).")
        
        if client_tier == "VIP":
            _trigger_pagerduty(job_id)
        else:
            _log_to_discord(job_id)
            
        return False
    
    print(f"[+] Job {job_id} completed within SLA.")
    return True

def _trigger_pagerduty(job):
    print(f"[*] PagerDuty Incident Created for VIP Job {job}. Calling on-call engineer.")

def _log_to_discord(job):
    print(f"[*] Discord Alert: Non-critical SLA breach logged for {job}.")

if __name__ == "__main__":
    monitor_sla(job_id="Workflow_992", client_tier="VIP", execution_time=120)
