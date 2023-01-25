import pytest

from Check import get_repo_details, get_pull_requests, get_stale_pull_requests, get_issues, \
    get_forks


@pytest.mark.parametrize('owner, repo', [('FeOsTyLeOp', 'Hause-Price'), ('sim0nsays', 'dlcourse_ai')])
def test_get_repo_details(owner, repo):
    result = get_repo_details(owner, repo)
    assert result["name"] == repo
    assert result["owner"]["login"] == owner


def test_get_pull_requests():
    # test the get pull requests with valid owner and repo
    owner = "sim0nsays"
    repo = "dlcourse_ai"
    response = get_pull_requests(owner, repo)


    assert response is not None


def test_get_stale_pull_requests():
    # test the get stale pull requests with valid owner and repo
    owner = "sim0nsays"
    repo = "dlcourse_ai"
    response = get_stale_pull_requests(owner, repo)
    assert response is not None


def test_get_issues():
    # test the get issues with valid owner and repo
    owner = "sim0nsays"
    repo = "dlcourse_ai"
    response = get_issues(owner, repo)
    assert response is not None


def test_get_forks():
    # test the get issues with valid owner and repo
    owner = "sim0nsays"
    repo = "dlcourse_ai"
    response = get_forks(owner, repo)
    assert response is not None
