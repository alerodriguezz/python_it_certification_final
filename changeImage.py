#!/usr/bin/env python3
from PIL import Image
import os, sys

user=os.getenv('USER')
images_dir='/home/{}/supplier-data/images/'.format(user)

url = "http://localhost/upload/"

for image_name in os.listdir(images_dir):
	if not image_name.startswith('.') and 'tiff' in image_name:
		image_path = images_dir + image_name
		#get file name 
		file_name = os.path.splitext(image_name)[0]
		im = Image.open(image_path)
		new_path = '{}.jpeg'.format(images_dir+file_name)
		try:
			im.convert("RGB").resize((600,400)).save(new_path,"JPEG")
		except IOError:
			print("cannot convert ", image_name)
