#!/usr/bin/python
#-*- coding: utf-8 -*-

import random

def function(msg, matches, peer):
	if len(matches) == 3:
		sides = int(matches[2])
		times = int(matches[1])
		if times > 100: times = 100
		message = ""
		for i in range(times):
			message = message + str(random.randrange(1,sides)) + ", "
		return message[:-2]
	elif len(matches) == 2:
		times = int(matches[1])
		if times > 100: times = 100
		message = ""
		for i in range(times):
			message = message + str(random.randrange(1,6)) + ", "
		return message[:-2]
	elif len(matches) == 1:
		return str(random.randrange(1,6))

plugin = {
	'name': "Roll",
	'tag': "roll",
	'patterns': ["^/(roll)$", "^/(roll) (\d+)$", "^/(roll) (\d+)\s*d\s*(\d+)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/roll (times) or /roll (times)d(sides)",
	'desc' : "Receive information about yourself (mainly ID)"
	}

