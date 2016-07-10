import copy
import pickle
import random
import math
import sys

import utility as util
import numpy as np

from sklearn.neighbors import KNeighborsClassifier

def NNmodel():
	traindata = util.readData('data/train.csv')

	y = traindata[0:23999, 0]
	x = traindata[0:23999, 1:]

	y2 = traindata[24000: ,0]
	x2 = traindata[24000:, 1:]

	print "Got here"

	knbrs = KNeighborsClassifier(n_neighbors=3)
	knbrs.fit(x, y) 

	y_pred = knbrs.predict(x2)

	print y2[0:10]
	print y_pred[0:10]

def main():
    NNmodel()

if __name__ == "__main__":
    main()