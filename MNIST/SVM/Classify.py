##########################################################################################
# Nearest Neighbor implementation of MNIST data model
##########################################################################################

import copy
import cPickle as pickle
import random
import math
import sys
import time

import utility as util
import numpy as np
# import model as md

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():

    start_time = time.time()
    train_data = util.readData('../data/train.csv')

    # y_train = train_data[0:23999, 0]
    # x_train = train_data[0:23999, 1:]

    # y_test = train_data[24000: ,0]
    # x_Test = train_data[24000:, 1:]

    y_train = train_data[0:23999, 0]
    x_train = train_data[0:23999, 1:]

    y_test = train_data[24000: ,0]
    x_test = train_data[24000:, 1:]

    print "Got here"
    print time.time() - start_time

    svc = SVC(kernel = 'poly')
    svc.fit(x_train, y_train)

    print "SVM Fit"
    print time.time() - start_time

    y_pred = svc.predict(x_test)

    print "Predictions made"
    print time.time() - start_time

    score = accuracy_score(y_test, y_pred)
    print score

    print y_pred[0:10]
    print y_test[0:10]

if __name__ == '__main__':
    main()