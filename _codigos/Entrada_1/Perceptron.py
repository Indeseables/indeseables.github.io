#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Perceptron.py
from scipy.optimize import minimize
import numpy as np
from Utils import MatLoad

def f(theta,X,Y): 
    res = np.multiply(theta*X,Y)
    if np.array_equal(res>=+0,Y>=+0): return -9999999
    else: return (-res[res<0]).sum(1).item((0,0))

def fit(theta,X,Y):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    return minimize(fun=f,x0=theta,args=(X,Y),method="CG")

def classify(theta,X): return 1 if np.inner(theta,X)>=+0 else -1
def predict(theta,X): return np.inner(theta,X)

if __name__ == "__main__":
    X = MatLoad("X.np"); 
    Y = MatLoad("Y.np"); 
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    theta = np.array([-0.0003,-1.54,-3.78])
    res  = fit(theta,X,Y)
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    print "\nClase de [1,0,5]:",classify(theta,np.array([1,0,5]))
