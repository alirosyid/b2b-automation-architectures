def aggregate_social_proof(client_metrics, uptime_data):
    total_hours_saved = client_metrics.get("hours_saved", 0)
    roi_percentage = client_metrics.get("roi_percentage", 0)
    uptime = uptime_data.get("system_uptime", "99.9%")
    
    # Formats raw data into curiosity-driven stealth copy
    stealth_case_study = f"""
    [Internal Metric Export]
    Recent deployment efficiency: We automated processes that recovered {total_hours_saved} hours per month, 
    achieving a {roi_percentage}% ROI within the first quarter, while maintaining {uptime} operational uptime.
    """
    
    print("[Integrations] Social proof aggregated. Ready for dynamic email injection.")
    return stealth_case_study.strip()

if __name__ == "__main__":
    metrics = {"hours_saved": 420, "roi_percentage": 315}
    uptime = {"system_uptime": "99.99%"}
    print(aggregate_social_proof(metrics, uptime))
