import json
import os.path

default = '{"blocked_users":[],"blocked_chats":[],"sudo_users":[],"group_disabled_commands":[],"user_disabled_commands":[]}'

# I/O functions
def writeDefault():
	if not os.path.isfile('settings.json'):
		f = open('settings.json', 'w')
		f.write(default)
		f.close()

def writeSettings(data):
	with open('settings.json', 'w') as dataF:
		json.dump(data, dataF)

def readSettings():
	writeDefault()
	with open('settings.json') as dataF:
		return json.load(dataF)

# toggling X blocked
def toggleFunction(id, list, block):
	data = readSettings()
	if block:
		if id not in data[list]:
			data[list].append(id)
			writeSettings(data)
	else:
		if id in data[list]:
			data[list].remove(id)
			writeSettings(data)
	return data

# toggling user blocked
def blockUser(id):
	return toggleFunction(id, "blocked_users", True)
		
def unblockUser(id):
	return toggleFunction(id, "blocked_users", False)

# toggling chat blocked
def blockChat(id):
	return toggleFunction(id, "blocked_chats", True)
		
def unblockChat(id):
	return toggleFunction(id, "blocked_chats", False)

# toggling sudo users
def addSudo(id):
	return toggleFunction(id, "sudo_users", True)
		
def removeSudo(id):
	return toggleFunction(id, "sudo_users", False)

# disabling commands on a per group or user basis
def addDisabledCommand(id, command, idIsGroup=False):
	data = readSettings()
	type = 'group_disabled_commands' if idIsGroup else 'user_disabled_commands'
	for i, v in enumerate(data[type]):
		if v["id"] == id:
			data[type][i]["commands"].append(command)
			writeSettings(data)
			return data
	data[type].append({"id": id, "commands": [command]})
	writeSettings(data)
	return data
			
