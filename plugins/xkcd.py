#!/usr/bin/python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import requests

def function(mag, matches, peer):
	a = requests.get("http://dynamic.xkcd.com/random/comic/")
	soup = BeautifulSoup(a.text)
	title = soup.find(id="ctitle").text
	comic = soup.find(id="comic").find_all('img')[0]
	comicUrl = comic.get('src')
	comicAlt = comic.get('title')
	filetype = comicUrl.split('.')
	filetype = filetype[len(filetype) - 1]
	urllib.request.urlretrieve("http:" + comicUrl, "image." + filetype)
	peer.send_photo("image." + filetype)
	return "{}\n\n{}".format(title, comicAlt)

plugin = {
	'name': "Xkcd",
	'tag': "xkcd",
	'patterns': ["^/xkcd$"],
	'function': function,
	'elevated': False, 
	'usage': "/xkcd",
	'desc': "Returns a random xkcd comic"
	}

