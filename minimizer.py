import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def function(X):
    "Given a scalar X, return some value"
    Y = (X - 1.5)**2 + 0.5
    print "X = {}, Y = {}".format(X,Y)
    return Y


def run_code():
    X_guess = 2.0
    min_results = spo.minimize(function, X_guess, method='SLSQP', options={'disp':True})
    print "Minima found at:"
    print "X = {}, Y = {}".format(min_results.x, min_results.fun)


if __name__ == '__main__':
    run_code()
