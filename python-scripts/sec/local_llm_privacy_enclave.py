import re

class PrivacyEnclaveRouter:
    def __init__(self):
        self.cloud_llm = "https://api.openai.com/v1/chat"
        self.local_llm = "http://internal-gpu-cluster.local/v1/chat"

    def route_prompt(self, user_prompt):
        print("[SecOps] Scanning prompt for PII and PHI markers...")
        
        # Regex for SSN, Credit Cards, or internal financial markers
        contains_sensitive_data = re.search(r'\b\d{3}-\d{2}-\d{4}\b|\b(?:\d[ -]*?){13,16}\b', user_prompt)
        
        if contains_sensitive_data:
            print("[!] 🛡️ SENSITIVE DATA DETECTED. Cloud API routing blocked.")
            print(f"[+] Re-routing payload to air-gapped Local LLM Enclave: {self.local_llm}")
            return {"target_endpoint": self.local_llm, "compliance_status": "Air-Gapped"}
            
        print("[+] Prompt cleared. Routing to high-speed Cloud LLM.")
        return {"target_endpoint": self.cloud_llm, "compliance_status": "Cloud-Cleared"}

if __name__ == "__main__":
    router = PrivacyEnclaveRouter()
    router.route_prompt("Process invoice for card 4532-1111-2222-3333.")
