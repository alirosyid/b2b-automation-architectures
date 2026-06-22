import re

def validate_outreach_copy(email_body):
    dark_patterns = [
        r"(?i)buy now", r"(?i)limited time offer", r"(?i)guaranteed roi", 
        r"(?i)100% free", r"(?i)act fast"
    ]
    
    flags = []
    for pattern in dark_patterns:
        if re.search(pattern, email_body):
            flags.append(pattern)
            
    if flags:
        print(f"[SecOps] 🛑 Campaign Blocked: Dark patterns detected {flags}. Adjust copy for stealth approach.")
        return False
        
    print("[SecOps] Copy validation passed. Stealth parameters active. Ready to send.")
    return True

if __name__ == "__main__":
    mock_email = "Hey! This is a 100% FREE audit. Act fast before spots run out!"
    validate_outreach_copy(mock_email)
