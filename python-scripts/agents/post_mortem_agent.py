import datetime

def generate_post_mortem(incident_id, downtime_minutes, root_cause):
    print(f"[Agent] Analyzing telemetry for incident {incident_id}...")
    
    # Simulates AI generating a professional explanation
    report = f"""
    # Incident Post-Mortem: {incident_id}
    **Date:** {datetime.datetime.now().strftime('%Y-%m-%d')}
    **Total Downtime:** {downtime_minutes} minutes
    
    ## Executive Summary
    Our monitoring systems detected an anomaly that caused a temporary interruption in webhook processing.
    
    ## Root Cause Analysis
    {root_cause}
    
    ## Corrective Action Taken
    We have implemented an exponential backoff retry mechanism and deployed a dynamic connection pooler to prevent recurrence.
    """
    
    print("[Agent] Post-mortem drafted successfully. Awaiting human approval before client dispatch.")
    return report

if __name__ == "__main__":
    cause = "An upstream CRM provider enforced an undocumented API rate limit, causing a cascading timeout."
    print(generate_post_mortem("INC-9942", 14, cause))
