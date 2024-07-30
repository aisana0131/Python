import requests, pprint, random, os, json
# from PIL import Image
pretty = pprint.PrettyPrinter(indent=4)

def dogs():
    url = "https://dog.ceo/api/breeds/image/random"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    # print(response.json())    #{'message': 'https://images.dog.ceo/breeds/doberman/n02107142_9379.jpg', 'status': 'success'}

    json_res = response.json()
    image_url = json_res['message']
    return image_url  #https://images.dog.ceo/breeds/borzoi/n02090622_8509.jpg



def slack(data):
    url = os.getenv("SLACK_URL")
    headers = {"Content-type": "application/json"}
    data = {"text": f"Random Dog picture from Aisana: {data}"}

    # print(help(requests.post))
    res = requests.post(url, json.dumps(data), headers=headers)
    print(res)

fact = dogs()
slack(data=fact)


