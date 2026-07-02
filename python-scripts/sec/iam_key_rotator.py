import boto3
import requests
import os
from base64 import b64encode
from nacl import encoding, public

def update_github_secret(repo_name, secret_name, unencrypted_value, github_token):
    """Encrypts and pushes a newly rotated IAM key directly to GitHub Secrets."""
    # 1. Get repo public key
    headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"}
    key_url = f"https://api.github.com/repos/{repo_name}/actions/secrets/public-key"
    pub_key_response = requests.get(key_url, headers=headers).json()
    
    # 2. Encrypt the secret using libsodium (NaCl)
    public_key = public.PublicKey(pub_key_response['key'].encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted_bytes = sealed_box.encrypt(unencrypted_value.encode("utf-8"))
    encrypted_value = b64encode(encrypted_bytes).decode("utf-8")
    
    # 3. Upload to GitHub
    put_url = f"https://api.github.com/repos/{repo_name}/actions/secrets/{secret_name}"
    payload = {"encrypted_value": encrypted_value, "key_id": pub_key_response['key_id']}
    requests.put(put_url, headers=headers, json=payload)
    print(f"Secret {secret_name} successfully rotated and pushed to GitHub.")

# IAM rotation logic goes here...
