import requests

def audit_api_key_scope(test_key, target_restricted_endpoint):
    headers = {"Authorization": f"Bearer {test_key}"}
    
    response = requests.get(target_restricted_endpoint, headers=headers)
    
    if response.status_code == 200:
        print("CRITICAL SECURITY ALERT: Key has over-provisioned access!")
        # Trigger revocation logic here
        return False
    elif response.status_code in [401, 403]:
        print("Audit Passed: Key access is correctly restricted.")
        return True

if __name__ == "__main__":
    audit_api_key_scope("sk_test_123", "https://api.internal.com/admin/billing")
