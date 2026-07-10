def track_hiring_signals(company_name, job_listings):
    print(f"[Lead Gen] Scanning hiring velocity for {company_name}...")
    
    automation_targets = ["data entry", "manual review", "operations specialist", "data processor"]
    bottleneck_score = 0
    
    for job in job_listings:
        if any(target in job.lower() for target in automation_targets):
            bottleneck_score += 1
            
    if bottleneck_score >= 3:
        print(f"[🔥] SEVERE BOTTLENECK DETECTED: {company_name} is trying to out-hire a broken process.")
        print("    -> Pushing target to hyper-personalized outbound sequence pitching n8n infrastructure.")
        return True
        
    return False

if __name__ == "__main__":
    jobs = ["Senior Dev", "Data Entry Clerk", "Operations Specialist", "Data Processor"]
    track_hiring_signals("LogisticsCorp", jobs)
