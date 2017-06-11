# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Check Profanity
# 2017-06-11 Robert Buckley

import urllib

def read_text():
	inputs = open("C:\\Users\\cardi\\OneDrive\\Documents\\input_text.txt")
	inputs_text = inputs.read()
	print(inputs_text)
	inputs.close()
	check_profanity(inputs_text)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	response = connection.read()
	# print(response)
	connection.close()
	if 'true' in response:
		print("[Check Profanity] Profanity detected in input text!")
	elif 'false' in response:
		print("[Check Profanity] No profanity detected in input text")
	else:
		print("[Check Profanity] Error scanning input text!")

if __name__ == "__main__":
	read_text()