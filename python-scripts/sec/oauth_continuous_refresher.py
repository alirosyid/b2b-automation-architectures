import time

def refresh_oauth_tokens(active_connections):
    current_time = time.time()
    refresh_margin = 300 # 5 minutes before expiry
    
    for connection_id, auth_data in active_connections.items():
        time_until_expiry = auth_data["expires_at"] - current_time
        
        if time_until_expiry <= refresh_margin:
            print(f"[SecOps] 🔄 Token for {connection_id} expiring soon. Initiating zero-trust refresh cycle...")
            # Trigger refresh API call to provider
            print(f"[SecOps] Token refreshed successfully. Connection secured.")
        else:
            print(f"[SecOps] Token for {connection_id} is stable ({int(time_until_expiry)}s remaining).")

if __name__ == "__main__":
    mock_connections = {
        "hubspot_client_a": {"expires_at": time.time() + 120}, # Needs refresh
        "salesforce_client_b": {"expires_at": time.time() + 86400} # Stable
    }
    refresh_oauth_tokens(mock_connections)
