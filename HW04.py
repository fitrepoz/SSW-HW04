import requests
import json



def view_github_repos():
    try:
        count = dict()
        username = input("Enter your github username:")

        url = "https://api.github.com/users/"+username+"/repos"

        repos = requests.get(url).json()

        for repo in repos:
            test_url = "https://api.github.com/repos/" + username + "/" + repo['name'] + "/commits"
            get = requests.get(test_urlf)
            commit = get.json()
            count[repo["name"]] = len(commit)
        for repositories, commits in count.items():
            print("Repository:", repositories, "Number of Commits:", commits)
            
    except TypeError:
        print("Invalid Username")

    return count
