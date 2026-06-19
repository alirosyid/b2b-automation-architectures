import hmac
import hashlib

def verify_webhook_signature(payload_body, secret_token, signature_header):
    # Recreate the hash using the shared secret
    expected_hash = hmac.new(
        secret_token.encode('utf-8'),
        payload_body.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    expected_signature = f"sha256={expected_hash}"
    
    if hmac.compare_digest(expected_signature, signature_header):
        print("[SecOps] Signature verified. Payload is authentic and safe to process.")
        return True
    else:
        print("[SecOps] ⚠️ CRITICAL: Signature mismatch. Potential spoofing attack neutralized.")
        return False

if __name__ == "__main__":
    mock_body = '{"event": "client_update"}'
    mock_secret = "super_secure_b2b_token"
    # Generating a valid signature for testing
    valid_sig = "sha256=" + hmac.new(mock_secret.encode(), mock_body.encode(), hashlib.sha256).hexdigest()
    
    verify_webhook_signature(mock_body, mock_secret, valid_sig)
