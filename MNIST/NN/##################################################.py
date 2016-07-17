#################################################################
# This is a Nearest Neighbor model object, for reading
# and running different NN models
#################################################################
#!/usr/bin/python
# Filename: model.py

import numpy as np
import math
import sys
import json

class model:
	'''experiment variables'''
	# None at the moment

	def __init__(self, name="Default"):

		#init variables go here
		self.name = None
		self.var = None
		self.pickled = False

	def read(self, filepath):

		self.filepath = filepath

		# some sort of json.loads(filename) line here?

		# maybe a pickle line here?

	def __repr__(self):
		return "Experiment Object, Name: {}".format(self.name)

	def __str__(self):
		return "\nExperiment Data: \n\n{}\n".format(self.exp)

# For testing
def main():
	if len(sys.argv) < 2:
		raise Exception("Usage: python experiment.py [exp name] [optional: exp path]")
	expName = sys.argv[1]
	if len(sys.argv) > 2:
		expPath = sys.argv[2]
		if not expPath.endswith('/'):
			expPath += "/"
		expPath += "{}.exp".format(expName)
	else:
		expPath = "{}/{}.exp".format(expName, expName)

	e = experiment()
	e.read(expPath)

	print e

	e.createTrainSet()
	e.train()

if __name__ == "__main__":
	main()