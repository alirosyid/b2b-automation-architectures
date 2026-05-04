from fastapi import Request, HTTPException
import time

# Simple in-memory rate limiting dictionary for MVP deployment
_request_records = {}

def enforce_rate_limit(request: Request, limit: int = 10, window_seconds: int = 60):
    """
    Basic rate limiting utility to protect LLM budgets and server capacity.
    For production, replace with Redis-based implementation.
    """
    client_ip = request.client.host
    current_time = time.time()

    if client_ip not in _request_records:
        _request_records[client_ip] = []

    # Filter old requests
    _request_records[client_ip] = [t for t in _request_records[client_ip] if current_time - t < window_seconds]

    if len(_request_records[client_ip]) >= limit:
        raise HTTPException(status_code=429, detail="Too Many Requests")

    _request_records[client_ip].append(current_time)
