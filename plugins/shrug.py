#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	return "¯\_(ツ)_/¯"

plugin = {
	'name': "Shrug",
	'tag': "shrug",
	'patterns': ["^/shrug$"],
	'function': function,
	'elevated': False, 
	'usage' : "/shrug",
	'desc' : "Shrugs"
	}

