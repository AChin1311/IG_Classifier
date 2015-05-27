import json
import requests
import sys

import config
import head

tag = sys.argv[1]
n = int(sys.argv[2])

token = config.token
headers = head.headers
instagramURL = "https://api.instagram.com/v1/tags/"+tag+"/media/recent?access_token="+token
imaggaURL = "http://api.imagga.com/v1/tagging"

imagga = []
count = 0

while n > 0:
    if n < 20:
        instagramURL += "&count=" + str(n)

    req = requests.get(instagramURL)
    instagramURL = json.loads(req.text)["pagination"]["next_url"]

    for data in json.loads(req.text)["data"]:
        imageURL = data["images"]["standard_resolution"]["url"]
        querystring = {"url": str(imageURL)}
        response = requests.request("GET", imaggaURL, headers=headers, params=querystring)
        imagga += json.loads(response.text)["results"]

    n -= 20

fname = tag + ".json"
json.dump(imagga, open(fname, "w"), indent=2)
