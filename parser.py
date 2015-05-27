#encoding=utf-8
import jieba
import json
import config
import requests
import sys

token = config.token
tag = "明天"
jsond = []
text = []

url = "https://api.instagram.com/v1/tags/"+tag+"/media/recent?access_token="+token+"&count=1"
req = requests.get(url)
text = json.loads(req.text)["data"][0]["caption"]["text"]
print text
	
words = jieba.cut(text, cut_all=False)

for word in words:
	chinese = True
	for ch in word:
		if ord(ch) < 0x4e00 or ord(ch) > 0x9fff:
			chinese = False
	if chinese:
		print word
        