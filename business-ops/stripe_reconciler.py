def process_stripe_webhook(webhook_payload):
    event_type = webhook_payload.get("type")
    data = webhook_payload.get("data", {}).get("object", {})
    
    if event_type == "invoice.payment_succeeded":
        customer_id = data.get("customer")
        amount = data.get("amount_paid", 0) / 100
        print(f"[BizOps] Payment of ${amount} cleared for {customer_id}.")
        _update_crm(customer_id, "Paid")
        return {"status": "success", "action": "crm_updated"}
        
    elif event_type == "invoice.payment_failed":
        customer_id = data.get("customer")
        print(f"[BizOps] Payment FAILED for {customer_id}. Initiating automated follow-up sequence.")
        _trigger_dunning_automation(customer_id)
        return {"status": "failed", "action": "dunning_started"}
        
    return {"status": "ignored"}

def _update_crm(customer, status):
    pass # Placeholder for CRM API call

def _trigger_dunning_automation(customer):
    pass # Placeholder for n8n trigger

if __name__ == "__main__":
    mock_payload = {"type": "invoice.payment_succeeded", "data": {"object": {"customer": "cus_123", "amount_paid": 500000}}}
    process_stripe_webhook(mock_payload)
