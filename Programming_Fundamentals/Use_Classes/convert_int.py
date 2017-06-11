# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Convert Int
# 2017-06-11 Robert Buckley
# An exercise to become more familiar with some built-in functions

def convert_int(n):
	"""
	Convert an int to hex, octal and binary forms
	"""
	print("Hex: " + str(hex(n)))
	print("Oct: " + str(oct(n)))
	print("Bin: " + str(bin(n)))

if __name__ == "__main__":
	while(True):
		n = raw_input("Please enter only an integer (enter Q to quit): ")
		if n == 'Q':
			break
		if n.isdigit():
			convert_int(int(n))
	

