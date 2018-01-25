
import json
import logging
import optparse
import os
import re
import sys
import requests
import shutil


	
def request_json(url):
	buffer =requests.get(url)
	return buffer.json()
def request_image(url):
	response = requests.get(url, stream=True)
	with open('/Users/vgpierce/Pictures/backgrounds/img.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)

def Main():
	uri = 'https://api.nasa.gov/planetary/apod?api_key=SNyPXWWXyc3xaDifZncVG9tXqK6N5LvrUQ9x2tRe'
	jsonResponse = request_json(uri)
	print jsonResponse
	image = jsonResponse["url"]
	print image
	request_image(image)

	

if __name__ == '__main__':
	print("Started")
	Main()
