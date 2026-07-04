def dispatch_interactive_slack_alert(workflow_name, error_details):
    print(f"[Ops] Critical failure in {workflow_name}. Generating interactive Slack payload...")
    
    slack_payload = {
        "text": f"🚨 *Workflow Failure:* {workflow_name}",
        "attachments": [{
            "text": f"Error: {error_details}",
            "fallback": "You are unable to interact with this alert",
            "callback_id": "n8n_incident_action",
            "actions": [
                {"name": "retry", "text": "🔄 Retry Execution", "type": "button", "value": "retry"},
                {"name": "dlq", "text": "🗑️ Dump to DLQ", "type": "button", "value": "dlq"}
            ]
        }]
    }
    
    # Mock POST request to Slack Webhook
    print("[+] Interactive incident alert dispatched to #sre-alerts.")
    return slack_payload

if __name__ == "__main__":
    dispatch_interactive_slack_alert("Stripe_To_CRM_Sync", "504 Gateway Timeout")
