#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json
import re

def getWeather(city):
	payload = {
		'q': city,
		'units': "metric"
	}
	h = requests.get("http://api.openweathermap.org/data/2.5/weather", params = payload)
	try:
		data = json.loads(h.text)
		cityName = "{}, {}".format(data["name"], data["sys"]["country"])
		tempInC = round(data["main"]["temp"], 2)
		tempInF = round((1.8 * tempInC) + 32, 2)
		desc = data["weather"][0]["description"]
		return "The weather in \"{}\" is currently {}C ({}F) with {}".format(cityName, tempInC, tempInF, desc)
	except ValueError:
		return "Could not find weather for that location."

def function(msg, matches, peer):
	return getWeather(matches[0])

plugin = {
	'name': "Weather",
	'tag': "weather",
	'patterns': ["^/weather (.+?)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/weather <city>",
	'desc' : "Returns weather of a city"
	}

