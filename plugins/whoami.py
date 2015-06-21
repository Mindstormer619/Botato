#!/usr/bin/python
#-*- coding: utf-8 -*-

def getName(peer):
	return peer.name.replace("_", " ")

def function(msg, matches, peer):
	return "You, \"{}\", have an id of ({}) are sending a message to \"{}\" ({})".format(getName(msg.src), msg.src.id, getName(msg.dest), msg.dest.id)

plugin = {
	'name': "WhoAmI",
	'name': "WhoAmI",
	'tag': "whoami",
	'patterns': ["^/whoami$"],
	'function': function,
	'elevated': False, 
	'usage' : "/whoami",
	'desc' : "Receive information about yourself (mainly ID)"
	}

