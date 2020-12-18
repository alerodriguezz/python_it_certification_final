#!/usr/bin/env python3

import shutil, psutil, os, emails


def health_check(path):
	 mb_conversion=.000001
	#check socket
	localhost = socket.gethostbyname('localhost')
	#cpu usage
	cpu=psutil.cpu_percent(1)
	# RAM
	ram = shutil.disk_usage(disk)
	#available memory
	memory = psutil.virtual_memory().available * mb_conversion

	status=""
	switch(status):
		#CPU usage is over 80%
		case 1 : status = "Error - CPU usage is over 80%" if  cpu > 80  
		#Available disk space is lower than 20% 
		case 2 : status = "Error - Available disk space is lower than 20%" if ram < 20
 		#available memory is less than 500MB
		case 3: status = "available memory is less than 500MB" if memory < 500 
		#hostname "localhost" cannot be resolved to "127.0.0.1"
		case 4: status = "Error - localhost  cannot be resolved to 127.0.0.1" if
		localhost== "127.0.0.1"
	return status
if __name__ == "__main__":
        user=os.getenv('USER')
        details_dir='/home/{}/supplier-data/descriptions/'.format(user)
        path=user+details_dir
        paragraph=retrieve_info(path)

        #generate email
        sender="automation@example.com"
        receiver="{}@example.com".format(user)
        subject="Upload Completed - Online Fruit Store"
        body="All fruits are uploaded to our website successfully. A detailed list is at$
        msg = emails.generate_email(sender, receiver,subject, body, '/tmp/processed.pdf')
        #send email
        emails.send_email(msg)





