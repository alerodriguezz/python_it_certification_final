#!/usr/bin/env python3


import os,reports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime
from  emails import *

 
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, info):

	styles = getSampleStyleSheet()
	my_doc = SimpleDocTemplate(attachment)
	title = Paragraph(title,styles["h1"])
	info = Paragraph(info, styles["BodyText"])
	empty_line = Spacer(1,20)

	flowables=[]
	flowables.append(title)
	flowables.append(info)
	flowables.append(empty_line)

	my_doc.build(flowables)
