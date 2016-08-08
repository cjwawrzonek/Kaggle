#################################################################
# layer object
#################################################################
#!/usr/bin/python
# Filename: layer.py

import json
import math
import sys
import json
from pprint import pprint

import numpy as np

class Layer(object):
	'''class variables'''
	# None at the moment

	def __init__(self, units):

		# init variables go here
		self.units = units
		self.b = np.zeros((units))
		self.acts = np.zeros((units))

	# Not important. Python object description function
	def __repr__(self):
		return None

	# To string method
	def __str__(self):
		return None

	def transform(self, inputs):
		if len(inputs) != len(self.acts):
			raise ValueError("Inputs length does not match layer size.")

		return inputs

	# update current activations
	def update(self, acts):
		self.acts = acts

	# transform inputs
	def forward(self, inputs):
		
		self.update(self.transform(inputs))


class ReLULayer(Layer):

	def __init__(self, units):
		super(ReLULayer, self).__init__(units)

	def transform(self, inputs):
		for i in range(self.units):
			self.acts[i] = max(0, inputs[i])

# For testing
def main():
	pass

if __name__ == "__main__":
	main()