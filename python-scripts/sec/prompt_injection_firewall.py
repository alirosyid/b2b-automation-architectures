import re

def sanitize_user_prompt(user_input):
    """Validates user input against known prompt injection heuristics."""
    blacklisted_phrases = [
        r"ignore previous instructions",
        r"system prompt",
        r"you are now a",
        r"bypass",
        r"output your internal rules"
    ]
    
    for pattern in blacklisted_phrases:
        if re.search(pattern, user_input, re.IGNORECASE):
            raise ValueError("SECURITY ALERT: Potential Prompt Injection Detected. Request Blocked.")
            
    return user_input

# Middleware handler integration
def handle_api_request(payload):
    clean_input = sanitize_user_prompt(payload.get("prompt", ""))
    return f"Processed safely: {clean_input[:20]}..."
