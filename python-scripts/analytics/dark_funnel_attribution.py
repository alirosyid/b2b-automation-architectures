import datetime

def calculate_dark_funnel_source(lead_timestamp, dark_social_mentions):
    print("[Analytics] Correlating 'Direct Traffic' lead with dark funnel velocity...")
    
    probable_source = "Unknown"
    closest_delta = 999999
    
    for mention in dark_social_mentions:
        time_delta = abs((lead_timestamp - mention['timestamp']).total_seconds())
        if time_delta < closest_delta and time_delta < 86400: # Within 24 hours
            closest_delta = time_delta
            probable_source = mention['source']
            
    print(f"[+] Dark funnel attribution calculated. Probable source: {probable_source}")
    return probable_source

if __name__ == "__main__":
    now = datetime.datetime.now()
    mock_mentions = [{"source": "Private Slack Group", "timestamp": now - datetime.timedelta(hours=2)}]
    calculate_dark_funnel_source(now, mock_mentions)
