#! /usr/bin/env python3
import os
import requests, json

url = "http://localhost/fruits/"

user=os.getenv('USER')

details_dir='/home/{}/supplier-data/descriptions/'.format(user)

images=[i for i in os.listdir('/home/{}/supplier-data/images/'.format(user)) if ".jpeg" in i ]
dic={}
image_iter=0
for i in os.listdir(details_dir):
	dic.clear()
	with open(details_dir+i, 'rb') as opened:
		data = opened.readlines()
		dic = {"name":data[0].decode("utf-8")[:-1] , "weight":int(data[1].decode("utf-8")[:-5]) , "description":data[2].decode("utf-8")[:-1], "image_name":images[image_iter] }
		response = requests.post(url,json=dic)
		print (response.request.url)
		print (response.status_code)
		image_iter= image_iter+1
