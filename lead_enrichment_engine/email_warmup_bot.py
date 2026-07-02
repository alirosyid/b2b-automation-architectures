import smtplib
import imaplib
import random
import time

def send_warmup_email(smtp_server, port, sender, password, recipient, body):
    """Sends a conversational, non-spammy email to warm up the domain."""
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender, password)
        msg = f"Subject: Following up on our chat\n\n{body}"
        server.sendmail(sender, recipient, msg)
        server.quit()
        print(f"Warmup email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send: {e}")

def execute_daily_warmup_batch():
    """Ramps up email volume safely to build IP reputation."""
    warmup_pool = ["test1@domain.com", "test2@domain.com", "test3@domain.com"]
    daily_limit = random.randint(15, 30) # Varies to mimic human behavior
    
    for i in range(daily_limit):
        target = random.choice(warmup_pool)
        send_warmup_email("smtp.gmail.com", 587, "sales@mycompany.com", "my_password", target, "Just checking in on the project status!")
        time.sleep(random.randint(60, 300)) # Random delay between sends
