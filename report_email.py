#!/usr/bin/env python3
import os, reports
from datetime import datetime
import emails

def retrieve_info(path):
	paragraph=""
	for i in os.listdir(details_dir):
		with open(details_dir+i, 'r') as opened:
			data=opened.readlines()
			paragraph+="name: "+data[0][:-1]+"<br/>"+"weight: "+data[1][:-1]+"<br/><br/>"
	return paragraph


if __name__ == "__main__":
	user=os.getenv('USER')
	details_dir='/home/{}/supplier-data/descriptions/'.format(user)
	path=user+details_dir
	paragraph=retrieve_info(path)
	#get time info
	dateTimeObj = datetime.now().strftime("%b %d, %Y")
	title= "Processed on " + dateTimeObj
	#generate pdf
	reports.generate_report('/tmp/processed.pdf', title, paragraph)
	#generate email 
	sender="automation@example.com"
	receiver="{}@example.com".format(user)
	subject="Upload Completed - Online Fruit Store"
	body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	msg = emails.generate_email(sender, receiver,subject, body, '/tmp/processed.pdf')
	#send email
	emails.send_email(msg)
