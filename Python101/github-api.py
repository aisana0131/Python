import requests
import pprint

pretty = pprint.PrettyPrinter(indent=4)

# url = 'https://api.github.com/repos/aisana0131/python'
url = 'https://api.github.com/users/aisana0131/repos'
header = {"Accept": "application/vnd.github+json"}
response = requests.get(url, header)

# pretty.pprint(response.json())
# pretty.pprint(response.json())

all_repos = response.json()
# print(len(all_repos))
# pretty.pprint(response.json()['full_name'])                     - This will only print a full_name

all_repos = response.json()

for repo in all_repos:
    print("clone url: ", repo['clone_url'])
    print("private: ", repo['private'])
    print("Username: ", repo['owner']['login'])
    print("-----------------------------------------------------")


