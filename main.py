import os

from dotenv import load_dotenv

load_dotenv()

access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
print(access_token)
