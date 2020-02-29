import json
import requests


def view_repos(user_input):

    rep = []
    result = []
    GitHubID = user_input
    initial_request = 'https://api.github.com/users/' + GitHubID + '/repos'
    response = requests.get(initial_request)
    answer = response.json()

    for r in answer:
        rep.append(r['name'])

    for k in rep:
        second_request = 'https://api.github.com/repos/' + GitHubID + '/' + k + '/commits'
        res = requests.get(second_request)
        commit_num = res.json()
        result.append('Repo:' + k + ' Number of commits: ' + str(len(commit_num)))
    return result


if __name__ == '__main__':
    for item in view_repos('fitrepoz'):
        print(item)