import os

import requests
from dotenv import load_dotenv

load_dotenv()

access_token = os.environ.get('GITHUB_ACCESS_TOKEN')

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {access_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

url = "https://api.github.com/users/urekmazth/repos"

payload = {}

# or requests.request(url, method='GET',.....)
response = requests.get(url, headers=headers, data=payload)

repos = response.json()
repositories = []

for repo in repos:
    info = {
        "id": repo.get("id"),
        "name": repo.get("name"),
        "url": repo.get("html_url"),
        "description": repo.get("description"),
        "language": repo.get("language"),
        "stars": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "fork": str(repo.get("fork")),
        "created_at": repo.get("created_at"),
    }

    repositories.append(info)

print(repositories[0])
