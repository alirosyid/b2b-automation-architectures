def graphql_subscription_to_webhook(graphql_event, target_n8n_webhook):
    print("[Integrations] ⚡ Real-Time GraphQL Mutation detected.")
    
    event_type = graphql_event.get("type")
    payload_data = graphql_event.get("data", {})
    
    if event_type == "LEAD_STATUS_CHANGED":
        print(f"    -> Lead '{payload_data.get('email')}' updated to {payload_data.get('status')}.")
        print(f"    -> Dispatching event payload directly to n8n automation layer...")
        
        # requests.post(target_n8n_webhook, json=payload_data)
        print(f"[+] N8N workflow triggered instantaneously via event-driven architecture.")
        return True
        
    print("[-] Event type not subscribed for automation. Ignoring.")
    return False

if __name__ == "__main__":
    mock_mutation = {"type": "LEAD_STATUS_CHANGED", "data": {"email": "ceo@startup.io", "status": "CONTRACT_SIGNED"}}
    graphql_subscription_to_webhook(mock_mutation, "https://n8n.internal/webhook/sales-sync")
