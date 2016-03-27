#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NeuralNetwork.py

from scipy.optimize import minimize
import numpy as np
from Utils import MatLoad
from math import e

def lineal(z): return z
def step(z): return 1.0 if z>0 else -1.0
def ramp(z):
	if z>=1: return 1.0
	elif -1<z<1: return z
	elif z<=-1: return -1.0	
def sigmoid(z): return 1.0/(1.0+(e**(-z)))
def tanh(z): return ((e**z)-(e**-z))/((e**z)+(e**-z))
def fast(z): return z/(1+abs(z))

def get_weights_submatrices(theta,units_by_layer): 
    thetas    = []
    index     = units_by_layer[0]*(units_by_layer[1]-1)
    thetas.append((theta[0:index]).reshape(units_by_layer[1]-1,units_by_layer[0]))
    for i in xrange(2,len(units_by_layer)-1):
	thetas.append((theta[index:index+(units_by_layer[i-1]*(units_by_layer[i]-1))]).reshape(units_by_layer[i]-1,units_by_layer[i-1]))
	index += (units_by_layer[i-1]*(units_by_layer[i]-1))
    thetas.append((theta[index:]).reshape(units_by_layer[len(units_by_layer)-1],units_by_layer[len(units_by_layer)-2]))
    return thetas

def generate_theta(units_by_layer):
    n_connections = 0
    for i in xrange(1,len(units_by_layer)-1): n_connections += ((units_by_layer[i]-1)*units_by_layer[i-1])
    n_connections += (units_by_layer[len(units_by_layer)-1]*units_by_layer[len(units_by_layer)-2])
    return np.array([1 for i in xrange(n_connections)])
    
def forward_propagation(theta,X,units_by_layer,factivation):
    theta               = get_weights_submatrices(theta,units_by_layer)
    vec_factivation     = np.vectorize(factivation)
    res                 = vec_factivation(theta[0]*X)
    for i in xrange(1,len(units_by_layer)-1):
	res = np.insert(res,0,[1 for j in xrange(X.shape[1])],axis=0)
	res = vec_factivation(theta[i]*res)
    return res

def forward_propagation_transform(theta,X,units_by_layer,factivation):
    vec_factivation     = np.vectorize(factivation)
    return vec_factivation(theta*X)
    
def f(theta,X,Y,units_by_layer,factivation): 
    res_output_layer    = forward_propagation(theta,X,units_by_layer,factivation)
    mean_squared_error  = (Y-res_output_layer)
    mean_squared_error  = (1.0/(2.0*X.shape[1]))*np.multiply(mean_squared_error,mean_squared_error).sum(axis=0).sum(axis=1)
    return mean_squared_error.item(0,0)


def f_regularized(theta,X,Y,units_by_layer,factivation,l=1): return f(theta,X,Y,units_by_layer,factivation)+(l*((theta*theta).sum(axis=0)))
    
def fit(theta,X,Y,units_by_layer,factivation,params_f_solver,method="CG",max_iter=1000,verbose_convergence=True,f_solver=f): return minimize(fun=f_solver,x0=theta,args=params_f_solver,method=method,options={"maxiter":max_iter,"disp":verbose_convergence})

def classify(theta,X,units_by_layer,factivation): return forward_propagation(theta,np.matrix(X),units_by_layer,factivation).argmax(axis=0).item((0,0))
    
def predict(theta,X,units_by_layer,factivation): return forward_propagation(theta,np.matrix(X),units_by_layer,factivation)
 
if __name__ == "__main__":
    
    ## Testing classifier ##
    X = MatLoad("X.np");  # Vectores por columnas (N=|cols|, M=|rows|) # 
    Y = MatLoad("Y.np");  # Vectores por columnas (N=|cols|, M=|rows|) #
    XROWS,XCOLS = X.shape[0],X.shape[1]
    
    #### Test NN aleatoria ####
    units_by_layer = [XROWS,5,4,2] # Se cuenta la unidad BIAS en la capa oculta (la entrada se asume homogénea) en la de salida NO hay #
    theta =  generate_theta(units_by_layer)
    # res  = fit(theta,X,Y,units_by_layer,lineal,(X,Y,units_by_layer,lineal),f_solver=f,method="SLSQP") # Mean squared error
    res  = fit(theta,X,Y,units_by_layer,lineal,(X,Y,units_by_layer,lineal,0.01),f_solver=f_regularized,method="SLSQP") # Mean squared error with theta regularization #
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    print "Clase de la muestra [1,-4,-4]: ",classify(theta,np.matrix([[1],[-4],[-4]]),units_by_layer,lineal)
    print "Clase de la muestra [1,4,4]: ",classify(theta,np.matrix([[1],[4],[4]]),units_by_layer,lineal)
    print "Regresion con la muestra [1,-4,-4]: ",predict(theta,np.matrix([[1],[-4],[-4]]),units_by_layer,lineal)
    print "Regresion con la muestra [1,4,4]: ",predict(theta,np.matrix([[1],[4],[4]]),units_by_layer,lineal)
