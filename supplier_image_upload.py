#!/usr/bin/env python3
import requests,os,sys

user=os.getenv('USER')
images_dir='/home/{}/supplier-data/images/'.format(user)
url = "http://localhost/upload/"
for image in os.listdir(images_dir):
	if ".jpeg" in image:
		with open(images_dir+image, 'rb') as opened:
			r = requests.post(url, files={'file': opened})
