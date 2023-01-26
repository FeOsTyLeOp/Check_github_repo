import requests
import datetime
import uvicorn
from loguru import logger
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse("http://127.0.0.3:8080/docs")


@app.get("/github/repo/{owner}/{repo}")
def get_repo_details(owner: str, repo: str):
    """
    Get repo details from GitHub.

    param owner: The owner of the GitHub repo.
    param repo: The name of the GitHub repo.
    return: A JSON object with the repo details.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    logger.info(f"Fetching details for {owner}/{repo}")
    return response.json()


@app.get("/github/repo/{owner}/{repo}/pulls")
def get_pull_requests(owner: str, repo: str):
    """
    Get a list of all pull requests from GitHub.

    param owner: The owner of the GitHub repo.
    param repo: The name of the GitHub repo.
    return: A JSON list with the pull requests.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    response = requests.get(url)
    logger.info(f"Fetching pull requests for {owner}/{repo}")
    return response.json()


@app.get("/github/repo/{owner}/{repo}/pulls/stale")
def get_stale_pull_requests(owner: str, repo: str):
    """
    Get a list of all pull requests which have not been merged for two weeks or more.

    param owner: The owner of the GitHub repo.
    param repo: The name of the GitHub repo.
    return: A JSON list with the stale pull requests.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open&sort=updated&direction=asc"
    response = requests.get(url)
    logger.info(f"Fetching stale pull requests for {owner}/{repo}")
    return [pull for pull in response.json() if
            (datetime.datetime.now() - datetime.datetime.strptime(pull['updated_at'], "%Y-%m-%dT%H:%M:%SZ")).days > 14]


@app.get("/github/repo/{owner}/{repo}/issues")
def get_issues(owner: str, repo: str):
    """
    Get a list of all issues from GitHub.

    param owner: The owner of the GitHub repo.
    param repo: The name of the GitHub repo.
    return: A JSON list with the issues.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url)
    logger.info(f"Fetching issues for {owner}/{repo}")
    return response.json()


@app.get("/github/repo/{owner}/{repo}/forks")
def get_forks(owner: str, repo: str):
    """
    Get a list of all forks from GitHub.

    param owner: The owner of the GitHub repo.
    param repo: The name of the GitHub repo.
    return: A JSON list with the forks.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    response = requests.get(url)
    logger.info(f"Fetching forks for {owner}/{repo}")
    return response.json()


## Add log in file

logger.add("logs/logs.log")

## Starting uvicorn
if __name__ == "__main__":
    uvicorn.run("Check:app", host="127.0.0.3", port=8080, reload=True)
