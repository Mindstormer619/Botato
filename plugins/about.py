#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	message = """
	A telegram bot written in python
	Made by @awkward_potato
	Running on a raspberry pi 2
	A Botato (part potato and part bot)
	v1.1 https://github.com/JuanPotato/Botato
	"""
	return message

plugin = {
	'name': "About",
	'tag': "about",
	'patterns': ["^/about$"],
	'function': function,
	'elevated': False,
	'usage' : "/about",
	'desc' : "Shows the about text"
	}

