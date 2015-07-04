#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import ImageDraw, ImageFont, Image
import random

def function(mag, matches, peer):
	palette = ["#000BAB", "#40E0D0", "#DC143C", "#4B0082", "#00DD00", "#00DDDD", "#DD0000", "#DD00FF", "#DDDD00", "#0112fe", "#ff4e00", "#741478", "#01870e"]
	im = Image.open("doge.jpg")
	texts = matches[0].split("/")
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("dogeFont.ttf",35)
	
	def typeText(text, color="#ff00ff"):
		size = font.getsize(text)
		x = random.randint(10, (500-size[0]-10))
		y = random.randint(10, (375-size[1]-10))
		draw.text((x, y), text, font=font, fill=color)

	a = 0
	for t in texts:
		if a >= len(palette):
			a = 0
		typeText(t, palette[a])
		a = a + 1

	im.save("image.jpg","JPEG")
	peer.send_photo("image.jpg")

plugin = {
	'name': "Dogify",
	'tag': "dogify",
	'patterns': ["^/dogify (.+)$"],
	'function': function,
	'elevated': False,
	'usage' : "/dogify words/or phrases seperated/by/slashes",
	'desc' : "Makes a doge meme from given phrases"
	}

