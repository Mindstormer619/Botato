#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json
import re

def getMonth(number):
	if number == 1: return "January" 
	elif number == 2: return "February"
	elif number == 3: return "March"
	elif number == 4: return "April"
	elif number == 5: return "May" 
	elif number == 6: return "June"
	elif number == 7: return "July" 
	elif number == 8: return "August"
	elif number == 9: return "September" 
	elif number == 10: return "October"
	elif number == 11: return "November" 
	elif number == 12: return "December"
	else: return "what"

def getTime(city):
	payload = {
		'key': "PUT_KEY_HERE",
		'q': city, 
		'format': "json"
	}
	h = requests.get("http://api.worldweatheronline.com/free/v2/tz.ashx", params = payload)
	data = json.loads(h.text)
	if "error" in data["data"]:
		return "Could not find time for that location."
	else:
		a = re.search("(\d+)\-(\d+)\-(\d+) (\d+:\d+)", data["data"]["time_zone"][0]["localtime"])
		c = a.groups()
		d = []
		for b in range(len(c)):
			if c[b][0] == "0":
				d.append(c[b][1:])
			else:
				d.append(c[b])
		time = d[3]
		date = "{} {}, {}".format(getMonth(int(d[1])), d[2], d[0])
		return "The time in \"{}\" is currently {} on {}".format(data["data"]["request"][0]["query"], time, date)

def function(msg, matches, peer):
	return getTime(matches[0])

plugin = {
	'name': "Time",
	'tag': "time",
	'patterns': ["^/time (.+?)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/time <city>",
	'desc' : "Returns time of a city"
	}

