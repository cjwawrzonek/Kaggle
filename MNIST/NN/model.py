#################################################################
# This is a Nearest Neighbor model object, for reading
# and running different NN models
#################################################################
#!/usr/bin/python
# Filename: model.py

import json
import math
import sys
import json
from pprint import pprint

import numpy as np

class model:
	'''model variables'''
	# None at the moment

	def __init__(self):

		#init variables go here
		self.description = None
		self.filepath = None
		self.pickled = False
		self.params = None

	def load(self, filepath):

		self.filepath = filepath

		fparams = open("{}/params.json".format(filepath))
		self.params = json.load(fparams)
		self.description = self.params['description']

	def __repr__(self):
		return "Modle Object, Name: {}".format(self.description)

	def __str__(self):
		return "Parameter Data: \n{}\n".format(self.params)

# For testing
def main():
	mPath = sys.argv[1]

	m = model()
	m.load(mPath)

	print m.params
	print m.description
	
	exit()

if __name__ == "__main__":
	main()