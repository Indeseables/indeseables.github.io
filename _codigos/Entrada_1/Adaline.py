#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Adaline.py

from scipy.optimize import minimize
import numpy as np
from Utils import MatLoad

def f(theta,X,Y): 
    res = ((theta*X)+(-Y))
    return (1.0/2.0)*(np.multiply(res,res).sum(axis=1)[0].item((0,0)))
    

def fit(theta,X,Y):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    return minimize(fun=f,x0=theta,args=(X,Y))
    
def predict(theta,X): return np.inner(theta,X)

def classify(theta,X):
    if np.inner(theta,X)>=0: return 1
    return -1

if __name__ == "__main__":
    X = MatLoad("X.np"); 
    Y = MatLoad("Y.np"); 
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    theta = np.zeros(XROWS)
    theta = fit(theta,X,Y).x
    print predict(theta,np.array([1,2,1]))
