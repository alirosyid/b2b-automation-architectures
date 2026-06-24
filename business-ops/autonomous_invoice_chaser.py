def generate_chaser_email(client_name, amount, days_overdue):
    if days_overdue <= 7:
        tone = "polite reminder"
        template = f"Hi {client_name}, just a quick reminder that invoice #4092 for ${amount} is slightly overdue. Let us know if you need another copy!"
    elif days_overdue <= 30:
        tone = "firm follow-up"
        template = f"Hello {client_name}, we have not received payment for ${amount} (overdue by {days_overdue} days). Please process this immediately to avoid service interruptions."
    else:
        tone = "service suspension warning"
        template = f"URGENT: {client_name}, your account is {days_overdue} days past due. SLA services will be suspended in 24 hours if ${amount} is not cleared."
        
    print(f"[BizOps] Generating {tone} for {client_name}.")
    return template

if __name__ == "__main__":
    print(generate_chaser_email("Globex Corp", 15000, 14))
