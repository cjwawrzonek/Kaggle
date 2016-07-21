##########################################################################################
# Nearest Neighbor implementation of MNIST data model
##########################################################################################

import copy
import pickle
import random
import math
import sys

import utility as util
import numpy as np
import model as md

from sklearn.neighbors import KNeighborsClassifier

def NNmodel(modelpath=None):
	train = util.readData('data/train.csv')

	y = train[0:23999, 0]
	x = train[0:23999, 1:]

	y2 = train[24000: ,0]
	x2 = train[24000:, 1:]

	print "Got here"

	knbrs = KNeighborsClassifier(n_neighbors=3)
	knbrs.fit(x, y)

	print "Neighbors fit"

	y_pred = knbrs.predict(x2)

	print "Predictions made"

	print y2[0:10]
	print y_pred[0:10]

def main():
    NNmodel()

if __name__ == "__main__":
    main()