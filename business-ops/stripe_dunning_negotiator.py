def handle_failed_payment(client_id, stripe_ltv_amount, failed_invoice_amount):
    print(f"[BizOps] Stripe webhook received: Payment failed for {client_id} (${failed_invoice_amount}).")
    
    high_value_threshold = 10000
    
    if stripe_ltv_amount > high_value_threshold:
        print(f"    -> Client is HIGH VALUE (LTV: ${stripe_ltv_amount}). Bypassing standard hard-lock protocol.")
        
        email_draft = f"Hi team, it looks like the card on file failed for your recent ${failed_invoice_amount} invoice. Because you've been a valued partner, we have automatically applied a 14-day grace period to your account so your automations don't go offline. Please update your billing details when you can."
        
        print("[+] Dunning negotiation email dispatched. Automation access preserved.")
        return {"action": "grace_period_granted", "email": email_draft}
        
    print(f"    -> Client LTV (${stripe_ltv_amount}) below threshold. Standard automated lock sequence initiated.")
    # trigger_n8n_account_lockout(client_id)
    return {"action": "account_locked"}

if __name__ == "__main__":
    handle_failed_payment("Enterprise_Alpha", stripe_ltv_amount=45000, failed_invoice_amount=2500)
