import pprint
import requests
import os

TOKEN = os.getenv("GH_TOKEN")

url = 'https://api.github.com/repos/aisana0131/Python'
headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"}
data = '{"private":false}'

res = requests.patch(url, data, headers=headers)
print(res)