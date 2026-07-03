import praw
import os

def intercept_competitor_complaints(competitor_name, subreddit_name, llm_client):
    """Scrapes Reddit for competitor complaints and scores buying intent."""
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="B2B_Intent_Scanner_1.0"
    )
    
    high_intent_leads = []
    
    for submission in reddit.subreddit(subreddit_name).search(competitor_name, limit=10, time_filter='week'):
        prompt = f"Analyze this post. Is the user expressing frustration with {competitor_name} and looking for alternatives? Reply YES or NO. Post: {submission.title} {submission.selftext}"
        
        response = llm_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        
        if "YES" in response.choices[0].message.content.upper():
            lead = {"author": submission.author.name, "url": submission.url, "intent_score": 95}
            high_intent_leads.append(lead)
            print(f"High intent signal found: {submission.url}")
            
    return high_intent_leads
