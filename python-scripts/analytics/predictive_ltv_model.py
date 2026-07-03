def predict_customer_ltv(stripe_data, support_ticket_sentiment, llm_client):
    """Predicts future LTV based on billing velocity and support sentiment."""
    
    prompt = f"""
    Analyze this B2B SaaS customer data. 
    MRR Growth: {stripe_data['growth_rate']}% over 6 months.
    Support Sentiment: {support_ticket_sentiment} (1-10 scale).
    Recent actions: Downgraded API tier last month.
    
    Predict their 12-month Lifetime Value risk. Will they churn or expand? 
    Output JSON with 'predicted_action', 'risk_percentage', and 'recommended_intervention'.
    """
    
    response = llm_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a predictive data scientist."},
                  {"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    return response.choices[0].message.content

# Note: Integration with Stripe/HubSpot SDKs handles data injection.
