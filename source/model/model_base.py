import numpy

class Model :

	def __init__ (self, params) :
		self.params = params
		self.model = None
		self.mean = None
		self.std = None

	def fit (self, x, y) :
		raise

	def predict (self, x) :
		raise
