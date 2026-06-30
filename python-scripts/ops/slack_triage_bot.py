import os
from slack_bolt import App

app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

@app.event("app_mention")
def triage_incident(event, say):
    """Intercepts Slack mentions for PagerDuty alerts and runs initial diagnostics."""
    incident_text = event['text']
    say(f"Triage Bot activated. Analyzing incident: {incident_text}...")
    
    # Simulated Diagnostic
    diagnostic_result = "Diagnostic complete: Found 500 API errors spiking on `Ingress-Gateway`. Recommending pod restart."
    
    say(f"🚨 **Initial Triage Report:**\n{diagnostic_result}\n\nShall I execute a safe restart? (Reply YES)")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
