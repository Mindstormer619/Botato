#!/usr/bin/python
#-*- coding: utf-8 -*-

import hashlib

def function(mag, matches, peer):
	key = matches[0].lower()
	if key == "md5":
		return hashlib.md5(matches[1].encode('utf-8')).hexdigest()
	elif key == "sha1":
		return hashlib.sha1(matches[1].encode('utf-8')).hexdigest()
	elif key == "sha224":
		return hashlib.sha224(matches[1].encode('utf-8')).hexdigest()
	elif key == "sha256":
		return hashlib.sha256(matches[1].encode('utf-8')).hexdigest()
	elif key == "sha384":
		return hashlib.sha384(matches[1].encode('utf-8')).hexdigest()
	elif key == "sha512":
		return hashlib.sha512(matches[1].encode('utf-8')).hexdigest()
	else:
		return "Valid encryption modes are: md5, sha1, sha224, sha256, sha384, sha512."

plugin = {
	'name': "Encryption",
	'tag': "encrypt",
	'patterns': ["^/encrypt ((?:md5)|(?:sha1)|(?:sha224)|(?:sha256)|(?:sha384)|(?:sha512)) (.+)$", "^/(encrypt)$"],
	'function': function,
	'elevated': False, 
	'usage': "/encrypt <mode> <string>",
	'desc': "Returns encrypted version of given string"
	}

