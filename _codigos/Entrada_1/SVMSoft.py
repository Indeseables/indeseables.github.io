#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SVMSoft.py

from scipy.optimize import minimize
from numpy import dot,array,zeros,ones,tile,transpose,multiply,inner
from Utils import MatLoad

def f(theta,C,D): return (1.0/2.0)*dot(theta,theta) + C*(D.sum(0))
def r(theta,X,Y,D): return (multiply(Y,theta*X)>=1).all() and (D>=0).all()

def fit(theta,X,Y,C,D):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    const = [{"type":"ineq","fun":r,"args":[X,Y,D]} for i in xrange(XCOLS)]
    return minimize(fun=f,args=(C,D),x0=theta,constraints=const,bounds=[(1,99999) for i in xrange(XROWS)])
    
def classify(theta,X): return 1 if inner(theta,X)>=+0 else -1
def predict(theta,X): return inner(theta,X)

if __name__ == "__main__":
    X = MatLoad("X.np"); 
    Y = MatLoad("Y.np"); 
    XROWS,XCOLS,YROWS,C = X.shape[0],X.shape[1],Y.shape[0],0.3
    theta = array([0.,0.1,-0.9])
    D     = array([0,0,0])
    res = fit(theta,X,Y,C,D)
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    print classify(theta,array([1,0,5]))
    print predict(theta,array([1,0,5]))
    print classify(theta,array([1,2,1]))
    print predict(theta,array([1,2,1]))
