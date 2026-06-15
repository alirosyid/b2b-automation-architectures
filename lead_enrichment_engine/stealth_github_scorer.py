import requests
import datetime

def score_b2b_lead(repo_owner, repo_name, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?per_page=100"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "Target repository unreachable or protected."}
    
    commits = response.json()
    recent_activity = sum(1 for c in commits if "2026" in c['commit']['author']['date'])
    
    business_impact_score = recent_activity * 1.5
    is_hot_lead = business_impact_score > 50
    
    return {
        "target": repo_owner,
        "score": business_impact_score,
        "actionable_lead": is_hot_lead,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
