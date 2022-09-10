"""
Class definition for counter object
	- keeps track of count onscreen

copyright Parker Roberts - 2022
"""


class Counter:
	"""
	Class for keeping track of count number\
	 """

	def __init__(self):
		Counter.count = 1


	def reset(self):
		"""
		Sets counter object back to one.
		"""
		self.count = 1


	def increm(self):
		"""
		Increments counter object by 1.
		"""
		self.count += 1


	def setval(self, num):
		"""
		Set counter to user-specified number. (!!! assert int?)
		"""
		self.count = num
