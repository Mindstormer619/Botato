#!/usr/bin/python
#-*- coding: utf-8 -*-

from os.path import isfile, join, realpath, dirname
from multiprocessing import Pool
from BotSettings import settings
from functools import partial
from os import listdir
import threading
import datetime
import pprint
import tgl
import re

e1 = b'\xf0\x9f\x94\xb8'.decode("utf-8")
settingsData = settings.readSettings()
our_id = 103332821 # I had to manually do this as the on our id never called
curPath = dirname(realpath(__file__))
binlog_done = False
started = False
admins = [82725741]

def blockCheck(msg, command=""):
	# if msg.dest.type == tgl.PEER_CHAT:
		# print(msg.dest.user_list)
	if msg.src.id in settingsData["blocked_users"]:
		return True
	elif (msg.dest.type == tgl.PEER_CHAT) and (msg.dest.id in settingsData["blocked_chats"]):
		return True
	else:
		return False

def loadPlugins():
	pluginFiles = [curPath + "/plugins/" + f for f in listdir(curPath + "/plugins") if re.search('^.+\.py$', f)]
	global plugins
	plugins = [adminPlugin, helpPlugin]
	for file in pluginFiles:
		values = {}
		with open(file) as f:
			code = compile(f.read(), file, 'exec')
			exec(code, values)
		plugin = values['plugin']
		print("Initializing plugin: {}".format(plugin['name']))
		plugins.append(plugin)
	
	def keyfunction(item):
		return item["tag"]

	plugins.sort(key=keyfunction)

######### ADMIN TOOLS #########

def adminFunction(msg, matches, peer):
	global settingsData
	key = matches[0].lower()
	if key == "reboot":
		loadPlugins()
		msg.src.send_msg("Rebooted", reply=msg.id, preview=False)
	elif key == "sudo":
		key2 = matches[1].lower()
		if key2 == "add":
			settingsData = settings.addSudo(int(matches[2]))
		elif key2 == "remove":
			settingsData = settings.removeSudo(int(matches[2]))
	elif key == "user":
		key2 = matches[1].lower()
		if key2 == "block":
			settingsData = settings.blockUser(int(matches[2]))
		elif key2 == "unblock":
			settingsData = settings.unblockUser(int(matches[2]))
	elif key == "chat":
		key2 = matches[1].lower()
		key3 = matches[2].lower()
		if key2 == "block":
			if key3 == "this":
				settingsData = settings.blockChat(int(msg.dest.id))
			else:
				settingsData = settings.blockChat(int(matches[2]))
		elif key2 == "unblock":
			if key3 == "this":
				settingsData = settings.blockChat(int(msg.dest.id))
			else:
				settingsData = settings.unblockChat(int(matches[2]))



adminPlugin = {
	'name': "Admin",
	'tag': "admin",
	'patterns': ["^/admin (reboot)$", "^/admin (sudo) ((?:add)|(?:remove)) (\d+)$", "^/admin (user) ((?:un)?block) (\d+)$", "^/admin (chat) ((?:un)?block) ((?:\d+)|(?:this))$"],
	'function': adminFunction,
	'elevated': True, 
	'usage': "/admin [reboot|addSudo|block|unblock] [user|chat]",
	'desc': "Admin tools"
	}

######### ADMIN TOOLS #########

############# HELP ############

def helpFunction(msg, matches, peer):
	if len(matches[0]) > 1:
		for a in plugins:
			if matches[0] == a["tag"] and not a["elevated"]:
				return "{}{} : {}".format(e1, a["usage"], a["desc"])
	else:
		helpText = ""
		for a in plugins:
			if not a["elevated"] and a["usage"] and a["tag"]:
				helpText = helpText + e1 + a["usage"] + "\n"
	if msg.dest.id != our_id:
		peer.send_msg("Help was sent in a pm", reply=msg.id, preview=False)
	msg.src.send_msg(helpText, reply=msg.id, preview=False)

helpPlugin = {
	'name': "Help",
	'tag': "help",
	'patterns': ["^/help$", "^/help (.+)$"],
	'function': helpFunction,
	'elevated': False, 
	'usage': "/help [action]",
	'desc': "Display a message showing all commands or description of specific command"
	}

############# HELP ############

plugins = [adminPlugin, helpPlugin]

def on_binlog_replay_end():
	global binlog_done
	binlog_done = True;
	return "Binlog: Done!"

def on_get_difference_end():pass
def on_secret_chat_update(peer, types): return "on_secret_chat_update"
def on_user_update(peer, types): pass
def on_chat_update(peer, types): pass

def on_our_id(id):
	global our_id
	our_id = id
	return "Set ID: " + str(our_id)

HISTORY_QUERY_SIZE = 100

def history_cb(msg_list, peer, success, msgs): pass
def dialog_list_cb(success, dialog_list): pass
def contact_list_cb(success, peer_list): pass
def msg_list_cb(success, msg_list):	pass
def file_cb(success, file_path): pass
def secret_chat_cb(success, peer): pass
def str_cb(success, string): pass
def chat_cb(success, peer):	 pass
def peer_cb(success, peer):	 pass
def user_cb(success, peer): pass
def msg_cb(success, msg): pass
def empty_cb(success): pass
		
def get_receiver(msg):
	if msg.dest.id == our_id: return msg.src
	else: return msg.dest

def on_msg_receive(msg):
	nowTime = datetime.datetime.now()
	peer = get_receiver(msg)
	# peer.mark_read(empty_cb)
	if msg.out: return
	if int((nowTime - msg.date).total_seconds()) > 10: return
	if blockCheck(msg): return
	if msg.text is not None and msg.text.strip():
		for aPlugin in plugins:
			for aPattern in aPlugin['patterns']:
				if re.search(aPattern, msg.text, re.IGNORECASE) and not blockCheck(msg, aPlugin["tag"]):
					print("Found a command and will send message now")
					matches = re.search(aPattern, msg.text, re.IGNORECASE)
					if matches.groups():
						matches = matches.groups()
					else:
						matches = matches.group()
					if aPlugin['elevated']:
						if msg.src.id in admins:
							someReturnValue = aPlugin['function'](msg, matches, peer)
							if someReturnValue: 
								peer.send_msg(someReturnValue, reply=msg.id, preview=False)
						else:
							peer.send_msg('The function requires an elevated user.', reply=msg.id, preview=False)
					else:
						someReturnValue = aPlugin['function'](msg, matches, peer)
						if someReturnValue: 
							peer.send_msg(someReturnValue, reply=msg.id, preview=False)
					break

# Set callbacks
loadPlugins()
tgl.set_on_binlog_replay_end(on_binlog_replay_end)
tgl.set_on_get_difference_end(on_get_difference_end)
tgl.set_on_our_id(on_our_id)
tgl.set_on_msg_receive(on_msg_receive)
tgl.set_on_secret_chat_update(on_secret_chat_update)
tgl.set_on_user_update(on_user_update)
tgl.set_on_chat_update(on_chat_update)
