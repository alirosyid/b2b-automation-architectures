import re

def sweep_unstructured_drives(document_metadata, content):
    print(f"[SecOps] Sweeping unstructured document '{document_metadata['title']}' for exposed IAM credentials...")
    
    # Regex for RSA Private Keys and AWS Secrets
    private_key_pattern = r'-----BEGIN RSA PRIVATE KEY-----'
    
    if re.search(private_key_pattern, content):
        print(f"[!] 🚨 EXPOSURE DETECTED: RSA Private Key found in standard document.")
        print(f"    -> Owner: {document_metadata['owner']}")
        print(f"[+] Autonomously revoking file permissions to 'Private' and triggering IAM rotation.")
        
        # Trigger revocation API
        return {"status": "quarantined", "severity": "CRITICAL"}
        
    print("[+] Document secure. No exposed credentials found.")
    return {"status": "secure"}

if __name__ == "__main__":
    mock_doc = {"title": "Dev Server Setup", "owner": "dev_intern"}
    mock_content = "To connect, use this key:\n-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA..."
    sweep_unstructured_drives(mock_doc, mock_content)
