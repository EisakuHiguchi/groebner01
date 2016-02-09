import re
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')
w1,w2,w3,w4,w5,w6,w7 = symbols('w1 w2 w3 w4 w5 w6 w7')

w14, w24, w34 = symbols('w14 w24 w34')
w15, w25, w35 = symbols('w15 w25 w35')
w46, w56 = symbols('w46 w56 ')

def getW():
    return Matrix([[2.2, 2.2, -6.8]])

def getX():
    return Matrix([[x1], [x2], [x3]])

def activateSub(value):
    return 1.0 / (1.0 + exp(-1 * value)) 

def activateFunc(A):
    result = []
    for e1 in A.tolist():
        r = []
        for e2 in e1:
            r.append(activateSub(e2))
        result.append(r)
    return Matrix(result)

def input(A, d1, d2, d3):
    return A.subs([[x1,d1], [x2,d2], [x3,d3]])

