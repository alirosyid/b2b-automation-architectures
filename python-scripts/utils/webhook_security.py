import hmac
import hashlib
import os
from fastapi import HTTPException, Request

async def verify_webhook_signature(request: Request):
    """
    Validates incoming webhook payloads against a secret key.
    Prevents unauthorized execution of automation pipelines.
    """
    secret = os.getenv("WEBHOOK_SECRET", "").encode('utf-8')
    signature = request.headers.get("X-Signature")

    if not signature or not secret:
        raise HTTPException(status_code=401, detail="Missing signature or secret")

    body = await request.body()
    expected_sig = hmac.new(secret, body, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(expected_sig, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
