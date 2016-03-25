#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  svm.py

from scipy.optimize import minimize
from numpy import dot,array,zeros,ones,tile,transpose
from Utils import MatLoad

def f(theta): return (1.0/2.0)*dot(theta,theta)
def r(theta,c,x): 
    aux = tile(theta,(x.shape[1],1))
    print c*(dot(aux,x))
    return c*(dot(aux,x))

def fit(X,Y,theta):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    const = [{"type":"ineq","fun":r,"args":[Y,X]} for i in xrange(XROWS)]
    return minimize(fun=f,x0=theta,constraints=const,bounds=[(1,99999) for i in xrange(XROWS)])

X = MatLoad("X.np"); 
Y = MatLoad("Y.np"); 
XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
theta = zeros(XROWS)
print fit(X,Y,theta)

