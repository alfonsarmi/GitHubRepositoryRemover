import requests

# Replace with your GitHub username and Personal Access Token
username = "name"
token = "tokenkey"

# Get the list of all repositories
response = requests.get(f"https://api.github.com/user/repos?per_page=100", auth=(username, token))
repos = response.json()

# Iterate through and delete each repository
for repo in repos:
    repo_name = repo['name']
    delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.delete(delete_url, auth=(username, token))
    if response.status_code == 204:
        print(f"Deleted {repo_name}")
    else:
        print(f"Failed to delete {repo_name}")
