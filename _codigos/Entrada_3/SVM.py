#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SVM.py

from scipy.optimize import minimize,fmin
from numpy import dot,array,zeros,ones,tile,transpose,multiply,inner
from Utils import MatLoad

def f(theta): return (1.0/2.0)*dot(theta,theta)

def r(theta,X,Y): return (multiply(Y,theta*X)-1).A1

def fit(theta,X,Y):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    return minimize(fun=f,x0=theta,constraints=({"type":"ineq","fun":r,"args":[X,Y]}),method="cobyla")

def generate_theta(XROWS): return array([1 for i in xrange(XROWS)])

def classify(theta,X): return 1 if inner(theta,X)>=+0 else -1
def predict(theta,X): return inner(theta,X)

if __name__ == "__main__":
    X = MatLoad("X.np"); 
    Y = MatLoad("Y.np"); 
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    theta = generate_theta(XROWS)
    res = fit(theta,X,Y)
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    print classify(theta,array([1,0,5]))
    print predict(theta,array([1,0,5]))
    print classify(theta,array([1,2,1]))
    print predict(theta,array([1,2,1]))
