#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SVMSoft.py

from scipy.optimize import minimize
from numpy import dot,array,zeros,ones,tile,transpose,multiply,inner,concatenate
from Utils import MatLoad

def f(theta,C,XROWS): 
    aux_theta,tolerances  = theta[:XROWS],theta[XROWS:]
    return ((1.0/2.0)*dot(theta,theta))+(C*tolerances.sum())
    
def r1(theta,X,Y,XROWS): 
    aux_theta,tolerances  = theta[:XROWS],theta[XROWS:]
    return (multiply(Y,aux_theta*X)-1+tolerances).A1

def r2(theta,X,Y,XROWS): return theta[XROWS:]
    
def fit(theta,X,Y,C):
    XROWS,XCOLS,YROWS = X.shape[0],X.shape[1],Y.shape[0]
    return minimize(fun=f,args=(C,XROWS),x0=theta,constraints=({"type":"ineq","fun":r1,"args":[X,Y,XROWS]},
							       {"type":"ineq","fun":r2,"args":[X,Y,XROWS]}))

def generate_theta(XROWS): return array([1 for i in xrange(XROWS)])
def generate_tolerances(XCOLS): return array([0 for i in xrange(XCOLS)])
def generate_initial_guess(XROWS,XCOLS): return concatenate((generate_theta(XROWS),generate_tolerances(XCOLS)))

def classify(theta,X): return 1 if inner(theta,X)>=+0 else -1
def predict(theta,X): return inner(theta,X)

if __name__ == "__main__":
    X = MatLoad("X.np"); 
    Y = MatLoad("Y.np"); 
    XROWS,XCOLS,YROWS,C = X.shape[0],X.shape[1],Y.shape[0],0.3
    theta = generate_initial_guess(XROWS,XCOLS)
    res = fit(theta,X,Y,C)
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    theta,tolerances = res.x[0:XROWS],res.x[XROWS:]
    print classify(theta,array([1,0,5]))
    print predict(theta,array([1,0,5]))
    print classify(theta,array([1,2,1]))
    print predict(theta,array([1,2,1]))
