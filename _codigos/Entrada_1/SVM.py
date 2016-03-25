#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SVM.py

from scipy.optimize import minimize
from numpy import dot,array,zeros,ones,tile,transpose,multiply
from Utils import MatLoad

def f(theta): return (1.0/2.0)*dot(theta,theta)
def r(theta,X,Y): return (multiply(Y,theta*X)>=1).all()

def fit(theta,X,Y):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    const = [{"type":"ineq","fun":r,"args":[X,Y]} for i in xrange(XCOLS)]
    return minimize(fun=f,x0=theta,constraints=const,bounds=[(1,99999) for i in xrange(XROWS)])

def classify(theta,X): pass
def predict(theta,X): pass

X = MatLoad("X.np"); 
Y = MatLoad("Y.np"); 
XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
theta = array([0.,0.1,-0.9])
print fit(theta,X,Y)

