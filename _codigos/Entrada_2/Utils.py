#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Utils.py
from numpy import loadtxt,matrix
from io import StringIO

def MatLoad(fname):
    res = None
    with open(fname) as fd:
	res = loadtxt(StringIO(unicode(fd.read()[:-1])))
    fd.close()
    return matrix(res)
