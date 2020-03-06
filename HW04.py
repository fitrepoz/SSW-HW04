import requests


def view_repos(github_id):

    get_repo_name = requests.get(f"https://api.github.com/users/{github_id}/repos")
    r = get_repo_name.json()
    repo_list = []

    for i in range(len(r)):
        repo_list.append(r[i]["name"])

    commit_dict = {}
    for n in range(len(repo_list)):
        get_commits = requests.get(f"https://api.github.com/repos/{github_id}/{repo_list[n]}/commits")
        re = get_commits.json()
        commit_dict[repo_list[n]] = len(re)
        print(f"Repo: {repo_list[n]} Number of commits : {len(re)}")

    return commit_dict


if __name__ == "__main__":
    print(view_repos("fitrepoz"))
