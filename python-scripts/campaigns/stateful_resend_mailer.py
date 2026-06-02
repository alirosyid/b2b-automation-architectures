import sqlite3
import logging
import resend

logger = logging.getLogger(__name__)

class StatefulResendMailer:
    """
    Automates B2B email outreach using the Resend API.
    Implements a strict stateful ledger to track outreach history, 
    preventing duplicate manual sends and protecting domain reputation.
    """
    def __init__(self, api_key: str, db_path: str = "outreach_state.db"):
        resend.api_key = api_key
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sent_emails 
                             (lead_id TEXT PRIMARY KEY, sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    def dispatch_email(self, lead_id: str, to_email: str, subject: str, html_content: str) -> bool:
        cursor = self.conn.execute("SELECT 1 FROM sent_emails WHERE lead_id = ?", (lead_id,))
        if cursor.fetchone():
            logger.warning(f"Stateful Guard: Email already sent to lead {lead_id}. Bypassing dispatch.")
            return False

        try:
            response = resend.Emails.send({
                "from": "Acme B2B <outreach@yourdomain.com>",
                "to": to_email,
                "subject": subject,
                "html": html_content
            })
            
            self.conn.execute("INSERT INTO sent_emails (lead_id) VALUES (?)", (lead_id,))
            self.conn.commit()
            logger.info(f"Email successfully dispatched and state logged for {lead_id}. ID: {response['id']}")
            return True
            
        except Exception as e:
            logger.error(f"Resend API dispatch failed for {to_email}: {e}")
            return False
