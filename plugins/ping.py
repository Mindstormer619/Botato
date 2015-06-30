#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
def function(msg, matches, peer):
	output = subprocess.Popen(["ping", "-c", "3", matches[0]], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
	return output

plugin = {
	'name': "Ping",
	'tag': "ping",
	'patterns': ["^/ping (.*?)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/ping <address>",
	'desc' : "Ping an address using the linux ping command"
	}

