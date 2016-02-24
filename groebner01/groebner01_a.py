import re
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')

def getW(w):
    return Matrix([w])

def getX():
    return Matrix([[x1], [x2], [x3]])

def input(A, d1, d2, d3):
    return A.subs([[x1,d1], [x2,d2], [x3,d3]]).evalf()

