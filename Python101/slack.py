import pprint
import requests
import os

url = os.getenv("SLACK_URL")

headers = {"Content-type": "application/json"}
data = '{"text": "We are awesome! - Aisana:hyper:"}'

res = requests.post(url, data, headers=headers)
print(res)