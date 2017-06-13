class MyExternalClass(object):
	"""
	This is just a sample class to demonstrate
	__name__ and __module__ variables
	generated from outside the main script
	"""
	def __init__(self, x):
		self.x = x

	def show_x(self):
		"""
		Display contents of this instance's 'x' attribute
		"""
		print(self.x)
