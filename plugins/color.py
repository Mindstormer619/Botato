#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import Image

def function(mag, matches, peer):
	_NUMERALS = '0123456789abcdefABCDEF'
	_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}

	color = matches[0]

	colors = _HEXDEC[color[0:2]], _HEXDEC[color[2:4]], _HEXDEC[color[4:6]]
	img = Image.new("RGB", (512, 512), colors)
	img.save("image.png","PNG")
	peer.send_photo("image.png")

plugin = {
	'name': "Color",
	'tag': "color",
	'patterns': ["^/color #?(.{6})$"],
	'function': function,
	'elevated': False,
	'usage' : "/color <hexamdecimal color>",
	'desc' : "Makes an image of a solid color of the color given"
	}

