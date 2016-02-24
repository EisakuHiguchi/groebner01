import re
from sympy import *
import gb_module as m

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')
w1,w2,w3,w4,w5,w6,w7 = symbols('w1 w2 w3 w4 w5 w6 w7')

w14, w24, w34 = symbols('w14 w24 w34')
w15, w25, w35 = symbols('w15 w25 w35')
w1e, w2e, w3e = symbols('w1e w2e w3e')
w46, w56, we6= symbols('w46 w56 we6 ')

def getX():
    return Matrix([[x1], [x2], [x3]])

def getW():
    return Matrix([[w14, w24, w34],[w15, w25, w35]])

def getGb(t):
    X1 = Matrix([[x1], [x2], [x3]])
    W1 = Matrix([[w14, w24, w34]])
    #W2 = Matrix([[w4]])

    A = W1 * X1
    A = m.activateFunc(A)

    #A = W2 + A
    #A = m.activateFunc(A)

    r = m.inputData(A,t)
    gr = groebner(r)

    return gr
    
def getGb2(t):
    X1 = getX()
    W1 = getW()

    W2 = Matrix([[w46,w56]])

    A = W1 * X1
    A = m.activateFunc(A)

    A = W2 * A

    r = m.inputData(A,t)
    r.append(w14 + w24 + w34 -6)
    gr = groebner(r)

    return gr


def source():
    X1 = getX()
    W1 = getW()

    W2 = Matrix([[w46,w56]])

    A = W1 * X1
    A = m.activateFunc(A)

    A = W2 * A

    return A