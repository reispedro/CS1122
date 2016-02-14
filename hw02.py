import random
import string
import urllib2
import json
import time
import csv

from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

def createImage():
	name = raw_input("What is your name?\n")
	size = (240,280)
	color = "#%06x" % random.randint(0, 0xFFFFFF)
	font = ImageFont.truetype("Arial.ttf",20)

	im = Image.new("RGB", size, (0,0,0))

	facexy = (20,20,220,220)
	mouthxy = [(110,110),(180,125)]
	eyeLeftxy = (60,65,75,80)
	eyeRightxy = (180,65,195,80)
	draw = ImageDraw.Draw(im)

	draw.rectangle(facexy,color)
	draw.pieslice(mouthxy,10,170,(250,250,250))
	draw.ellipse(eyeLeftxy,(250,250,250))
	draw.ellipse(eyeRightxy,(250,250,250))
	draw.text((70,240),name,(250,250,250),font)

	im.save("testImage", "JPEG")
	print("Image Created")

def getVotes():
	while True:
		option = raw_input("What results do you wanna see? (Republican or Democrat)\n")
		if option.lower() == ("GOP").lower() or option.lower() == ("Republican").lower():
			request = urllib2.Request("http://elections.huffingtonpost.com/pollster/api/charts/2016-national-gop-primary")
			break
		if option.lower() == ("Democrat").lower():
			request = urllib2.Request("http://elections.huffingtonpost.com/pollster/api/charts/2016-national-democratic-primary")
			break
		else:
			print("Please answer with Republican or Democrat.\n")
	opens = urllib2.build_opener()
	dataFile = opens.open(request)
	jsonFile = json.loads(dataFile.read())
	for row in jsonFile["estimates"]:
		if row['first_name'] != None:
			print(row['first_name'] + " " + row['last_name'] + ": " + str(row['value']))
		else:
			print(row['choice'] + ": " + str(row['value']))

def getAttendance():
	csvfile = open('Attendance','w')
	infoWriter = csv.writer(csvfile)
	infoWriter.writerow(["time", "name"])
	while True:
		name = raw_input("What is your name? (enter 'exit' to quit)\n")
		now = time.strftime('%Y-%m-%d %X')
		if name == "exit":
			break
		infoWriter.writerow([now, " " + name])

def main():
	createImage()
	print('\n_______________________________________________')
	getVotes()
	print('\n_______________________________________________')
	getAttendance()


if __name__ == "__main__":
    main()