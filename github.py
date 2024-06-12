import os

import requests
from dotenv import load_dotenv

load_dotenv()

access_token = os.environ.get('GITHUB_ACCESS_TOKEN')

headers = None
if access_token:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {access_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

payload = {}


def get_all_user_repositories(username: str):
    """
    Uses GITHUB REST API to get all repositories for a given user.
    Retrieve information of interest
    """
    url = f"https://api.github.com/users/{username}/repos"

    repositories = []
    page = 1

    try:
        while True:
            # or requests.request(url, method='GET',.....)
            params = {"page": page, "per_page": 100}
            response = requests.get(url, headers=headers,
                                    data=payload, params=params)

            # raise exception if an error is encountered
            response.raise_for_status()

            repos = response.json()

            if not repos:
                break

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
            page += 1

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories for user {username}: \n{e}")
        return None

    return repositories
