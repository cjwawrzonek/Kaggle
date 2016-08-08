#################################################################
# Network object
#################################################################
#!/usr/bin/python
# Filename: network.py

import json
import math
import sys
import json
from pprint import pprint

import numpy as np

class Network(object):
	'''class variables'''
	# None at the moment

	def __init__(self, layers):

		# init variables go here
		self.layers = layers
		self.W = []
		for i in range(len(layers)-1):
			self.W.append(np.zeros((self.layers[i].units,
									self.layers[i+1].units)))

	# Not important. Python object description function
	def __repr__(self):
		return None

	# To string method
	def __str__(self):
		return None

	def transform(self, inputs):
		if len(inputs) != self.layers[0].units:
			raise ValueError("Inputs length does not match input layer size.")

		acts = self.layers[0].transform(inputs)

		for i in range(len(self.layers) - 1):
			acts = self.layers[i+1].transform(np.dot(acts, W[i]))

		return acts


	def forward(self, inputs):
		if len(inputs) != self.layers[0].units:
			raise ValueError("Inputs length does not match input layer size.")

		self.layers[0].forward(inputs)

		for i in range(len(self.layers) - 1):
			acts = np.dot(self.layers[i].acts, W[i])
			self.layers[i+1].forward(acts)

		return self.layers[-1].acts

# For testing
def main():

	ann = Network([Layer(5), Layer(5)])

	output = ann.forward([1,1,0,0,1])
	
	print output


if __name__ == "__main__":
	main()