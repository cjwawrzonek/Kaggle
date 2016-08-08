##########################################################################################
# Nearest Neighbor implementation of MNIST data model
##########################################################################################

import copy
import cPickle as pickle
import random
import math
import sys
import json

import utility as util
import numpy as np
import model as md

from sklearn.neighbors import KNeighborsClassifier

def NNmodel(model=None):

	print "Parsing data."

	modelpath = "models/{}".format(model)

	train = util.readData('../data/train.csv')

	## See if the data was pickled. If yes, fetch. If no, load and pickle
	# try:
	# 	train = pickle.load(open( "train.pkl", "rb" ))
	# except:
	# 	# this is potentially time intensive
	# 	train = util.readData('data/train.csv')

	# 	# pickle it
	# 	pickle.dump(train, open( "train.pkl", "wb" ))

	with open('{}/params.json'.format(modelpath)) as param_file:    
		params = json.load(param_file)

	# If we're cross validating, not yet implemented
	if params['cross_valid']:
		pass

	num_rows = len(train)

	if params['testing']:
		x = train[0:(len(train)/2), 1:]
		y = train[0:(len(train)/2), 0]

		x_test = train[(len(train)/2 + 1):, 1:]
		y_test = train[(len(train)/2 + 1): ,0]

		print "Finished parsing data. Fitting NN."

		knbrs = KNeighborsClassifier(n_neighbors=params['num_neighbors'])
		knbrs.fit(x, y)

		print "Finished fitting. Running predictions."

		y_pred = knbrs.predict(x_test)

		print "Predictions done. Calculating results."

		correct = 0
		incorrect = 0
		for i in range(len(y_pred)):
			if y_pred[i] == y_test[i]:
				correct += 1
			else:
				incorrect += 1

		percent = float(correct) / (float(correct + incorrect))

		print "Num correct = {}. Percent correct = {}".format(correct, percent)

		return

def main():
	try:
		model = sys.argv[1]
	except:
		print 'No model parameters specified, using "m1" \nTo specify parameters, use "python NN [parameter file]"'
		model = None

	NNmodel(model)

if __name__ == "__main__":
	main()