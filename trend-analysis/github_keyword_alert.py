import requests
import datetime

def scan_github_trends(target_keywords):
    url = "https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc".format(
        (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    )
    
    response = requests.get(url)
    if response.status_code != 200:
        return []
        
    trending_repos = response.json().get("items", [])[:20]
    opportunities = []
    
    for repo in trending_repos:
        description = str(repo.get("description", "")).lower()
        if any(keyword in description for keyword in target_keywords):
            opportunities.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"]
            })
            
    return opportunities

if __name__ == "__main__":
    keywords = ["agentic", "n8n", "b2b automation", "rag"]
    leads = scan_github_trends(keywords)
    print(f"[Trends] Found {len(leads)} trending repos matching business criteria.")
