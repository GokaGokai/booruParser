#!/bin/python
import requests
import re
from bs4 import BeautifulSoup
import sys

# Input
if(len(sys.argv) != 2):
	print("Error:\nPlease enter one argument (link of safebooru) :/\n\nUsage:\npython3 safebooruParser.py 'https://safebooru.org/index.php?page=post&s=view&id=4245444'\n")
else:
	input = str(sys.argv[1])
	output = ""

	regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	if re.match(regex, input) is None:
		print("Error:\nInvalid link (Don't forget the '...' and the https://...) :p\n\nUsage:\npython3 safebooruParser.py 'https://safebooru.org/index.php?page=post&s=view&id=4245444'\n")
	else:
		# Collect and parse first page
		page = requests.get(input)
		soup = BeautifulSoup(page.text, 'html.parser')

		# Get tags
		tags = soup.find_all(class_="tag")
		for tag in tags:
			tag = tag.find("a").contents[0]
			output = output + tag + ", "
			
		# Remove the extra ,
		output = output[:-2]

		# Output
		print("\nSucess:\n"+output)
		with open("output.txt" , "w") as file:
			file.write(str(output))

