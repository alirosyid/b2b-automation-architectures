def trigger_trial_conversion_sequence(user_email, trial_days_remaining, usage_metrics):
    if trial_days_remaining == 2:
        print(f"[Lead Gen] Trial expiring in 48 hours for {user_email}. Generating custom ROI report...")
        
        workflows_run = usage_metrics.get("workflows_executed", 0)
        time_saved = workflows_run * 0.5 # Assuming 30 mins saved per workflow
        
        conversion_pitch = f"Your trial ends soon. During this period, our system executed {workflows_run} automations, saving your team approximately {time_saved} hours. Click here to upgrade to a dedicated enterprise node."
        
        print(f"[+] High-conversion logic drafted. Routing payload to email dispatch server.")
        return conversion_pitch
        
    print(f"[-] {user_email} trial not in critical conversion window. Ignoring.")
    return None

if __name__ == "__main__":
    trigger_trial_conversion_sequence("founder@startup.io", 2, {"workflows_executed": 45})
