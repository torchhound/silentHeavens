def cli(command, username):
	"""Interprets commands and returns output"""
	output = ""
	if command == "stats":
		output = "Test output"
	else:
		output = command
	return output