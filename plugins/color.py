#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import Image
import json
import re

def function(mag, matches, peer):
	with open('colors.json') as dataF:
		colors = json.load(dataF)
	_NUMERALS = '0123456789abcdefABCDEF'
	_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}

	color = matches[0]
	if color in colors:
		color = colors[color]
	elif re.search("^#?[0-9A-F]{3}$", color, re.IGNORECASE):
		color = "{}{}{}".format(color[0]*2, color[1]*2, color[2]*2)
	elif re.search("^#?[0-9A-F]{6}$", color, re.IGNORECASE) is None:
		return "could not find that color \"{}\"".format(color)

	colors = _HEXDEC[color[0:2]], _HEXDEC[color[2:4]], _HEXDEC[color[4:6]]
	img = Image.new("RGB", (128, 128), colors)
	img.save("image.jpg","JPEG")
	peer.send_photo("image.jpg")

plugin = {
	'name': "Color",
	'tag': "color",
	'patterns': ["^/color #?([0-9A-F]{6}|[0-9A-F]{3})$", "/color (.+)"],
	'function': function,
	'elevated': False,
	'usage' : "/color <hexamdecimal color>",
	'desc' : "Makes an image of a solid color of the color given"
	}

