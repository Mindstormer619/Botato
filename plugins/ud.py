#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import re
import html as h

def function(msg, matches, peer):
	payload = {
		'term': matches[0]
	}
	r = requests.get("http://www.urbandictionary.com/define.php", params = payload)
	html = r.text

	if re.search( "id=\"not_defined_yet\"", html):
		return "{} is not defined.".format(matches[0])
	else:
		exampleRegex = '<\s*div\s*class=\\\'(example)\\\'>\s*([\s\S]*?)\s*<\/div>'
		meaningRegex = '<\s*div\s*class=\\\'(meaning)\\\'>\s*([\s\S]*?)\s*<\/div>'
		
		exampleMatches = re.search(exampleRegex, html)
		meaningMatches = re.search(meaningRegex, html)
		
		example = h.unescape(exampleMatches.group(2))
		meaning = h.unescape(meaningMatches.group(2))
		
		example = re.sub("<(.*?)>", "", example)
		meaning = re.sub("<(.*?)>", "", meaning)
		return "{}\n\nDefinition: {}\nExample: {}".format(matches[0], meaning, example)

plugin = {
	'name': "Urban Dictionary",
	'tag': "ud",
	'patterns': ["^/ud (.*?)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/ud <term>",
	'desc' : "Defines a term using Urban Dictionary"
	}

