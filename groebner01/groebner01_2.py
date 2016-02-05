import re
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')
w03,w13,w23 = symbols('w03 w13 w23')
w04,w14,w24 = symbols('w04 w14 w24')
w05,w15,w25 = symbols('w05 w15 w25')
w36,w46,w56 = symbols('w36 w46 w56')
w37,w47,w57 = symbols('w37 w47 w57')

w1,w2,w3,w4,w5,w6  = symbols('w1 w2 w3 w4 w5 w6')


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

def getW2_2():
    return Matrix([\
        [w36 , w46, w56],\
        [w37 , w47, w57],\
        ])

def getW1_3():
    return Matrix([\
        [w1, w2], \
        ])

def getW2_3():
    return Matrix([\
        [w3, w4], \
        ])

def getW1_4():
    return Matrix([\
        [w1, w2],\
        ])

def getW2_4():
    return Matrix([\
        [w3, w4, w5],\
        ])

def getW1_5():
    return Matrix([\
        [w1, w2, w3],\
        ])

def getW2_5():
    return Matrix([\
        [w4, w5, w6],\
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

def func_Solve(G):
    print(' , '.join(map(str, G.exprs)))
    for e in G.exprs:
        temp = Eq(e,0)
        temp = solve(temp)
        print(',\n'.join(map(str,temp)))

def inputData(A):
    R1 = A.subs([ [x0,0], [x1,0], [x2,1] ])
    R2 = A.subs([ [x0,1], [x1,0], [x2,1] ])
    R3 = A.subs([ [x0,0], [x1,1], [x2,1] ])
    R4 = A.subs([ [x0,1], [x1,1], [x2,1] ])

    r1 = R1[0] - 0
    r2 = R2[0] - 1
    r3 = R3[0] - 1
    r4 = R4[0] - 0

    return [r1, r2, r3, r4]


def main_1():
    W1 = getW1()
    W2 = getW2()

    X1 = getX1()
    X2 = getX2()

    A1 = W1 * X1
    aA1 = activateFunc(A1)

    A2 = W2 * aA1
    aA2 = activateFunc(A2)

    r = inputData(aA2)

    print(groebner(r))

    #func_Solve(groebner(R))


def main_2():
    W1 = getW1_3()
    W2 = getW2_3()
    X1 = getX1()

    X2 = W1.T * X1.T
    X2 = Matrix([\
        [X2[0]],[1],\
        ])

    A = W2 * X2

    r = inputData(A)
    
    print(groebner(r))
    
def main_3():
    W1 = getW1_4()
    W2 = getW2_4()
    X1 = getX1()

    X2 = W1.T * X1.T
    X2 = Matrix([\
        [x1],[X2[0]],[1],\
        ])

    A = W2 * X2
    r = inputData(A)
    print(groebner(r))

if __name__ == "__main__":
    W1 = getW1_5()
    W2 = getW2_5()
    X1 = getX1()

    X2 = W1.T * X1.T

    X2 = Matrix([\
        [x0],[X2[0]],[x2],\
        ])

    A = W2 * X2
    r = inputData(A)
    print(groebner(r))

