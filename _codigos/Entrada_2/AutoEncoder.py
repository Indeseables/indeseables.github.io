#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AutoEncoder.py

import NeuralNetwork as nn
from Utils import MatLoad
import numpy as np

if __name__ == "__main__":
    X = MatLoad("XAutoencoder.np");  # Vectores por columnas (N=|cols|, M=|rows|) # 
    XROWS,XCOLS,M1 = X.shape[0],X.shape[1],10 # Se cuenta la unidad BIAS en la capa oculta (la entrada se asume en notación homogénea) #
    units_by_layer = [XROWS,M1,XROWS-1] 
    theta = nn.generate_theta(units_by_layer)
    Y     = X[1:]
    res   = nn.fit(theta,X,Y,units_by_layer,nn.lineal,max_iter=1000000,method="SLSQP")
    print "\n Detalles de convergencia \n"
    print res
    theta = res.x
    theta = nn.get_weights_submatrices(theta,units_by_layer)
    print "Vector original: ",np.matrix([[1], [0], [1], [1], [0], [1], [0], [0], [0], [0], [1], [1], [0], [1], [1], [1],[1]])
    encoded = nn.forward_propagation_transform(theta[0],np.matrix([[1], [0], [1], [1], [0], [1], [0], [0], [0], [0], [1], [1], [0], [1], [1], [1],[1]]),units_by_layer,nn.lineal)
    encoded = np.insert(encoded,0,1,axis=0)
    print "Vector cifrado: ",encoded.tolist()
    decoded = nn.forward_propagation_transform(theta[1],encoded,units_by_layer,nn.lineal)
    print "Vector descifrado: ",decoded
