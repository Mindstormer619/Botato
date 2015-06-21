#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET
import re

def define(phrase):
	url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" + phrase + "?key=da8b4077-583b-4788-9f5c-bf402f1c55e2"
	r = requests.get(url)
	root = ET.fromstring(r.text.encode('ascii', 'replace'))
	defs = root.findall("./entry[1]/def/dt")
	
	if defs:
		definition = phrase + " is..."
		for idx, aDef in enumerate(defs):
			oneDef = re.sub("<(.*?)>", "", str(ET.tostring(aDef))[2:-1])
			if oneDef[0] == ":":
				oneDef = oneDef[1:]
			oneDef = "{}: {}".format((idx + 1), oneDef)
			definition = definition + "\n" + oneDef
		return definition
	else:
		suggestions = root.findall("./suggestion")
		suggestion = "Did you mean: "
		for idx, sug in enumerate(suggestions):
			suggestion = suggestion + sug.text + ", "
		return suggestion[:-2]

def function(msg, matches, peer):
	return define(matches[0])

plugin = {
	'name': "Dictionary",
	'tag': "define",
	'patterns': ["^/define (.*?)$", "^define (.*?)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/define <term>",
	'desc' : "Defines a term"
	}

