#!/usr/bin/python
#-*- coding: utf-8 -*-

from os.path import isfile, join, realpath, dirname
from multiprocessing import Pool
from functools import partial
from os import listdir
import threading
import datetime
import pprint
import tgl
import re

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

######### ADMIN TOOLS #########

def adminFunction(msg, matches, peer):
	if matches[0] == "reboot":
		loadPlugins()
		msg.src.send_msg("Rebooted", reply=msg.id, preview=False)

adminPlugin = {
	'name': "Admin",
	'tag': "admin",
	'patterns': ["^/admin (.+)(?: (.+))?$"],
	'function': adminFunction,
	'elevated': True, 
	'usage': "/admin [reboot|addAdmin|remAdmin|shutdown]",
	'desc': "Admin tools"
	}

######### ADMIN TOOLS #########

############# HELP ############

def helpFunction(msg, matches, peer):
	if msg.dest.id != our_id:
		peer.send_msg("Help was sent in a pm", reply=msg.id, preview=False)
	helpText = ""
	if len(matches[0]) > 1:
		for a in plugins:
			if matches[0] == a["tag"] and not a["elevated"]:
				helpText = "🔸{} : {}".format(a["usage"], a["desc"])
				break
	else:
		for a in plugins:
			if not a["elevated"] and a["usage"]:
				helpText = helpText + "🔸" + a["usage"] + "\n"
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

our_id = 103332821 # I had to manually do this as the on our id never called
curPath = dirname(realpath(__file__))
binlog_done = False;
started = False;
plugins = [adminPlugin, helpPlugin]
admins = [82725741]

def on_binlog_replay_end():
	print("thing 1 happened")
	binlog_done = True;

def on_get_difference_end():
	pass

def on_secret_chat_update(peer, types):
	return "on_secret_chat_update"

def on_user_update(peer, types):
	pass

def on_chat_update(peer, types):
	pass

def on_our_id(id):
	our_id = id
	return "Set ID: " + str(our_id)
	print("Set ID: " + str(our_id))

HISTORY_QUERY_SIZE = 100

def history_cb(msg_list, peer, success, msgs):
	print(len(msgs))
	msg_list.extend(msgs)
	print(len(msg_list))
	if len(msgs) == HISTORY_QUERY_SIZE:
		tgl.get_history(peer, len(msg_list), HISTORY_QUERY_SIZE, partial(history_cb, msg_list, peer));
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
	if msg.dest.id == our_id:
		return msg.src
	else:
		return msg.dest

def on_msg_receive(msg):
	# if not binlog_done: return
	peer = get_receiver(msg)
	# peer.mark_read(empty_cb)
	if msg.out: return
	if (datetime.datetime.now() - msg.date).total_seconds() > 10: return
	if msg.text is not None and msg.text.strip():
		for aPlugin in plugins:
			for aPattern in aPlugin['patterns']:
				if re.search(aPattern, msg.text):
					matches = re.search(aPattern, msg.text)
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

# def on_msg_receive(msg):
	# thr = threading.Thread(target=async_msg_receive, args=[msg])
	# thr.start()

# Set callbacks
loadPlugins()
tgl.set_on_binlog_replay_end(on_binlog_replay_end)
tgl.set_on_get_difference_end(on_get_difference_end)
tgl.set_on_our_id(on_our_id)
tgl.set_on_msg_receive(on_msg_receive)
tgl.set_on_secret_chat_update(on_secret_chat_update)
tgl.set_on_user_update(on_user_update)
tgl.set_on_chat_update(on_chat_update)
