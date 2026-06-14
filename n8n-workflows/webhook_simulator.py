import requests
import json
import time

def trigger_n8n_webhook(webhook_url, payload):
    headers = {'Content-Type': 'application/json'}
    print(f"[*] Sending test payload to n8n webhook...")
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    print(f"[+] Status: {response.status_code}")

if __name__ == "__main__":
    test_url = "http://localhost:5678/webhook-test/my-workflow"
    test_data = {"client": "StealthCorp", "action": "generate_lead"}
    trigger_n8n_webhook(test_url, test_data)
