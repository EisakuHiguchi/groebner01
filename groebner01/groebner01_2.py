

import re
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')
w03,w13,w23 = symbols('w03 w13 w23')
w04,w14,w24 = symbols('w04 w14 w24')
w05,w15,w25 = symbols('w05 w15 w25')
w36,w46,w56 = symbols('w36 w46 w56')


def getW1():
    return Matrix([\
        [w03 , w04, w05] ,\
        [w13 , w14, w15] ,\
        [w23 , w24, w25] ,\
        ])

def getW2():
    return Matrix([\
        [w36 , w46, w56]\
        ])
    
def getX1():
    return Matrix([ [x0], [x1], [x2] ])

def getX2():
    return Matrix([ [x3], [x4], [x5] ])


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


if __name__ == "__main__":
    W1 = getW1()
    W2 = getW2()

    X1 = getX1()
    X2 = getX2()

    A1 = W1 * X1
    aA1 = activateFunc(A1)
    
    A2 = W2 * A1
    aA2 = activateFunc(A2)
