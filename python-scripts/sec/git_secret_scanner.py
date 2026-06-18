import re
import sys

def scan_for_secrets(file_content):
    patterns = {
        "AWS_KEY": r"(?i)aws_access_key_id\s*=\s*['\"][A-Z0-9]{20}['\"]",
        "OPENAI_KEY": r"(?i)sk-[a-zA-Z0-9]{48}",
        "STRIPE_KEY": r"(?i)sk_live_[a-zA-Z0-9]{24}"
    }
    
    for secret_type, pattern in patterns.items():
        if re.search(pattern, file_content):
            print(f"[ERROR] Commit blocked! Detected hardcoded {secret_type} in codebase.")
            return True
            
    return False

if __name__ == "__main__":
    # Mocking a file check during a git pre-commit hook
    mock_code = 'llm_client = OpenAI(api_key="sk-1234567890abcdef1234567890abcdef1234567890abcdef")'
    if scan_for_secrets(mock_code):
        sys.exit(1) # Block the commit
    print("[+] Security scan passed. No secrets detected.")
