#!/usr/bin/python
#-*- coding: utf-8 -*-

def function(mag, matches, peer):
	n = int(matches[0])
	if n>1000: return "I will not make a fibonacci number past 1000 (becomes spammy)"
	a,b = 0,1
	for i in range(n):
		a,b = b,a+b
	return str(a)

plugin = {
	'name': "Fibonacci",
	'tag': "fib",
	'patterns': ["^/fib (\d+)$"],
	'function': function,
	'elevated': False,
	'usage' : "/fib <n (get nth term of Fibonacci sequence)>",
	'desc' : "Fibonacci sequence calculator, get nth term of the sequence"
	}

