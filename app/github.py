import httpx

GITHUB_API_URL = "https://api.github.com"

async def fetch_pr_diff(owner: str, repo: str, pr: int, token: str = None):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls/{pr}"
    
    headers = {
        "Accept": "application/vnd.github.v3.diff"
    }
    
    if token:
        headers["Authorization"] = f"token {token}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.text
