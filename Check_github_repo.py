# import required libraries
from fastapi import FastAPI
import requests
import datetime

# set up the app
app = FastAPI()

@app.get('/repo-details/{github_repo_name}')
def get_repo_details(github_repo_name):
    """
    Get repo details such as repo name, description, language, size etc.
    """
    # make request to github api
    request_url = f"https://api.github.com/repos/{github_repo_name}"
    response = requests.get(request_url)
    # get the repo details from response
    repo_details = response.json()
    # return the repo details
    return repo_details

@app.get('/pull-requests/{github_repo_name}')
def get_pull_requests(github_repo_name):
    """
    Get a list of all pull requests for a given GitHub repo.
    """
    # make request to github api
    request_url = f"https://api.github.com/repos/{github_repo_name}/pulls"
    response = requests.get(request_url)
    # get the pull requests from response
    pull_requests = response.json()
    # return the pull requests
    return pull_requests

@app.get('/unmerged-pull-requests/{github_repo_name}')
def get_unmerged_pull_requests(github_repo_name):
    """
    get a list of all pull requests which have not been merged for two weeks or more.
    """
    # make request to github api
    request_url = f"https://api.github.com/repos/{github_repo_name}/pulls?state=open"
    response = requests.get(request_url)
    # get the pull requests from response
    unmerged_pull_requests = response.json()
#    filter out only the pull requests which have not been merged for two weeks or more
    filtered_unmerged_pull_requests = []
    for pull_request in unmerged_pull_requests:
        if datetime.datetime.strptime(pull_request['updated_at'], "%Y-%m-%dT%H:%M:%SZ") > (datetime.datetime.now() - datetime.timedelta(days=14)):
            filtered_unmerged_pull_requests.append(pull_request)
    # return the unmerged pull requests
    return filtered_unmerged_pull_requests

@app.get('/issues/{github_repo_name}')
def get_issues(github_repo_name):
    """
    Get a list of all issues for a given GitHub repo.
    """
    # make request to github api
    request_url = f"https://api.github.com/repos/{github_repo_name}/issues"
    response = requests.get(request_url)
    # get the issues from response
    issues = response.json()
    # return the issues
    return issues

@app.get('/forks/{github_repo_name}')
def get_forks(github_repo_name):
    """
    Get a list of all forks for a given GitHub repo.
    """
    # make request to github api
    request_url = f"https://api.github.com/repos/{github_repo_name}/forks"
    response = requests.get(request_url)
    # get the forks from response
    forks = response.json()
    # return the forks
    return forks


## Check
#rep = 'sim0nsays/dlcourse_ai'
#print (get_repo_details(rep))
#print(get_pull_requests(rep))
#print (get_unmerged_pull_requests(rep))
#print (get_issues(rep))
#print (get_forks(rep))