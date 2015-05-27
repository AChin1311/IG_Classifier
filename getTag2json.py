import head
import json
import requests

url = "http://api.imagga.com/v1/tagging"

querystring = {"url": "http://playground.imagga.com/static/img/example_photo.jpg"}
headers = head.headers
response = requests.request("GET", url, headers=headers, params=querystring)
j = json.loads(response.text)

# print(response.text)
json.dump(j, open("test.json", "w"), indent=2)
