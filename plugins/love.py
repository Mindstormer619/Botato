#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(msg, matches, peer):
	return "I love you too {}".format(msg.src.first_name)

plugin = {
	'name': "Love",
	'tag': "",
	'patterns': ["^I? ?love you,? Botato$"],
	'function': function,
	'elevated': False, 
	'usage' : "",
	'desc' : ""
	}

