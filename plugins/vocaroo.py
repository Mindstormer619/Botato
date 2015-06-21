#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	import urllib
	urllib.urlretrieve("http://vocaroo.com/media_command.php?media=" + matches[0] + "&command=download_mp3", "/home/download/mp3.mp3")
	return "¯\_(ツ)_/¯"

plugin = {
	'name': "Vocaroo",
	'tag': "",
	'patterns': ["https?:\/\/vocaroo\.com\/i\/([a-zA-Z0-9]{5,15})"],
	'function': function,
	'elevated': True, 
	'usage': "",
	'desc': ""
	}

