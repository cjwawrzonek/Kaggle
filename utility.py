##########################################################################################
# Utility functions library for repeated code
##########################################################################################
import ast
import copy
import pickle
import random
import math
import sys

import numpy as np

from pprint import pprint
from scipy.special import expit

#####################################################################
# Data Handlers
#####################################################################

def readData(file):
    pass

#####################################################################
# Stats functions
#####################################################################

# # Non-normalized (ie max of 1 at mean)
# def gaussian(x, mu, sig):
#     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

# # Normalied (ie sum over whole distribution = 1)
def gaussian(x, mu, sig):
    return 1./(math.sqrt(2.*math.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)

def mean2(x):
    y = np.sum(x) / np.size(x);
    return y

def corr2(a,b):
    a = a - mean2(a)
    b = b - mean2(b)

    r = (a*b).sum() / math.sqrt((a*a).sum() * (b*b).sum())
    return r

def corr2_coeff(A,B):
    # Rowwise mean of input arrays & subtract from input arrays themeselves
    A_mA = A - A.mean(1)[:,None]
    B_mB = B - B.mean(1)[:,None]

    # Sum of squares across rows
    ssA = (A_mA**2).sum(1);
    ssB = (B_mB**2).sum(1);

    # Finally get corr coeff
    return np.dot(A_mA,B_mB.T)/np.sqrt(np.dot(ssA[:,None],ssB[None]))

def zscore(dataSet):
    sd = np.std(dataSet)
    dataMean = np.mean(dataSet)
    zs = []

    for x in dataSet:
        zs.append((x - dataMean)/sd)

    return zs

def getJacobian(x, *args):
    rnn = args[0]
    W, b = rnn.get_layer(rnn.W, 1)

    in_0 = args[1]

    jacobian=[]

    for i in range(len(W)):
        row = []
        for j in range(len(W)):
            if i == j:
                d = 1
            else:
                d = 0
            row.append(-d + W[i][j]*dExpit(x[j]))
        jacobian.append(row)

    return np.asarray(jacobian)

def getGaussNewton(x, *args):
    rnn = args[0]
    W, b = rnn.get_layer(rnn.W, 1)

    in_0 = args[1]

    gn = []
    jac = getJacobian(x, rnn, in_0)

    for i in range(len(W)):
        row = []
        for j in range(len(W)):
            val = 0
            for k in range(len(W)):
                val += jac[k][i]*jac[k][j]
            row.append(val)
        gn.append(row)

    print np.asarray(gn).shape
    exit()
    return np.asarray(gn)

#####################################################################

def main():
    x = [1, .9, .8, 1]

    print dExpit(x)
    exit()

if __name__ == "__main__":
    main()