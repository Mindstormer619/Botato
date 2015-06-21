#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json

def function(msg, matches, peer):
	req = requests.get('http://tambal.azurewebsites.net/joke/random')
	html = req.text
	jdata = json.loads(html)
	return jdata["joke"]

plugin = {
	'name': "Joke",
	'tag': "joke",
	'patterns': ["^/joke$"],
	'function': function,
	'elevated': False, 
	'usage' : "/joke",
	'desc' : "Tells a joke"
	}

