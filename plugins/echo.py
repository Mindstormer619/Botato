#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	altern  = ["／","＃", "＼", "ǃ"]
	normal  = ["/", "#", "\\", "!"]
	message = matches[0]
	for n,a in zip(normal, altern):
		message = message.replace(n, a)
	peer.send_msg(message)

plugin = {
	'name': "Echo",
	'tag': "echo",
	'patterns': ["^/echo (.*?)$"],
	'function': function,
	'elevated': False,
	'usage' : "/echo <text>",
	'desc' : "Repeats text"
	}

