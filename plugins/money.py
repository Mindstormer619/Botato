#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import re
def function(mag, matches, peer):
	currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DEM", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FIM", "FJD", "FKP", "FRF", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "IEP", "ILS", "INR", "IQD", "IRR", "ISK", "ITL", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKG", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"]
	fromCur = matches[0].upper()
	amount = matches[1]
	toCur = matches[2].upper()

	if fromCur not in currencies:
		return "ERROR: currency \"" + fromCur + "\" is not recognized"

	if toCur not in currencies:
		return "ERROR: currency \"" + toCur + "\" is not recognized"

	returnText = "Oops, an error occurred."

	payload = {
		'a': amount,
		'from': fromCur, 
		'to': toCur
	}
	r = requests.get("https://www.google.com/finance/converter", params = payload)
	
	html = r.text
	moneyMatches = re.search("<span class=bld>([\d.]+)", html)
	if moneyMatches:
		returnText = "{} {} is {} {}".format(
			amount, fromCur, moneyMatches.group(1), toCur)

	return returnText

plugin = {
	'name': "Money",
	'tag': "money",
	'patterns': ["^/m(?:oney)? (\w+) ([\d\.]+) (\w+)$"],
	'function': function,
	'elevated': False, 
	'usage' : "/money (from currency) (amount) (to currency)",
	'desc' : "Convert money from a currency into another"
	}

