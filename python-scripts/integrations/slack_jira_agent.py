import os
import requests
from slack_bolt import App

app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

def create_jira_ticket(summary, description):
    """Pushes a formatted bug ticket to Jira via REST API."""
    url = f"{os.getenv('JIRA_URL')}/rest/api/2/issue"
    headers = {
        "Authorization": f"Bearer {os.getenv('JIRA_API_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "fields": {
            "project": {"key": "ENG"},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"}
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("key")

@app.event("app_mention")
def handle_bug_report(event, say):
    """Intercepts Slack messages, parses errors, and creates Jira tickets."""
    raw_text = event['text']
    
    # LLM logic to summarize raw_text into a title and structured description goes here
    ticket_title = "Automated Bug Report from Slack" 
    ticket_key = create_jira_ticket(ticket_title, raw_text)
    
    say(f"✅ I've documented this issue. Jira Ticket created: {os.getenv('JIRA_URL')}/browse/{ticket_key}")
