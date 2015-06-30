#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests

def function(msg, matches, peer):
	returnText = "Oops, an error occurred."
	exp = matches[0]
	payload = {
		'expr': exp
	}
	r = requests.get("http://api.mathjs.org/v1/", params = payload)
	if r.text:
		returnText = r.text
	
	return returnText

plugin = {
	'name': "Calculator",
	'tag': "calc",
	'patterns': ["^/calc (.+)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/calc <expression>",
	'desc' : "Evaluates a math expression"
	}

