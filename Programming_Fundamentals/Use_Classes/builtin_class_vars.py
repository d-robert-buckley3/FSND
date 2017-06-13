# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# testing built-in class variables
# 2017-06-12 Robert Buckley
"""
	This script serves as a demonstration of the built-in class variables
	__name__ and __module__.  I also showed a test of the variable __class__
	out of curiosity.
"""

import urllib
import external_class

class MyInternalClass(object):
	"""
	This is a sample class internal to the main script
	"""
	def __init__(self, x):
		self.x = x

def main():
	my_external_object = external_class.MyExternalClass('external!')
	my_internal_object = MyInternalClass('internal!')
	connection = urllib.urlopen("http://www.google.com")

	objects = [my_external_object, my_internal_object, connection]

	print("Here are the __module__ and __class__ values of each of the 3 objects I created:")
	for my_object in objects:
		print(str(my_object))
		print("\t__module__: " + my_object.__module__)
		print("\t__class__: " + str(my_object.__class__))


if __name__ == "__main__":
	main()