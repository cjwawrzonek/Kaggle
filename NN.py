import copy
import pickle
import random
import math
import sys

import utility as util
import numpy as np

from sklearn.neighbors import NearestNeighbors

def NNmodel():
	data = util.readTrainData('data/train.csv')

	y = data[:,0]
	x = data[1:, :]

	nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(data)

def main():
    NNmodel()

if __name__ == "__main__":
    main()