import os
import boto3
from fastapi import Request, HTTPException

class ZeroTrustMiddleware:
    def __init__(self):
        self.secrets_client = boto3.client('secretsmanager')
        self.current_key = self._fetch_active_key()

    def _fetch_active_key(self):
        # Fetches the dynamically rotated key from AWS Secrets Manager
        print("[SecOps] Fetching current active API key from secure vault...")
        return "dynamic_secret_9942a" # Mocked key

    async def authenticate_request(self, request: Request):
        client_key = request.headers.get("X-Internal-API-Key")
        if client_key != self.current_key:
            print(f"[!] 🚨 Unauthorized access attempt detected from IP: {request.client.host}")
            raise HTTPException(status_code=403, detail="Strict Zero-Trust Enforcement: Invalid or expired API Key.")
            
        print("[+] Request authenticated via dynamic Zero-Trust protocol.")
        return True
