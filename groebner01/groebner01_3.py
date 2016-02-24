import re
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')
w1,w2,w3,w4,w5,w6,w7 = symbols('w1 w2 w3 w4 w5 w6 w7')

w14, w24, w34 = symbols('w14 w24 w34')
w15, w25, w35 = symbols('w15 w25 w35')
w1e, w2e, w3e = symbols('w1e w2e w3e')
w46, w56, we6= symbols('w46 w56 we6 ')

def activateSub(value):
    return 1.0 / (1.0 + exp(-1 * value).evalf()) 

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
    R1 = A.subs([ [x1,0], [x2,0], [x3,1] ])
    R2 = A.subs([ [x1,1], [x2,0], [x3,1] ])
    R3 = A.subs([ [x1,0], [x2,1], [x3,1] ])
    R4 = A.subs([ [x1,1], [x2,1], [x3,1] ])

    r1 = R1[0] + 0  # 0 0 1
    r2 = R2[0] + 1  # 1 0 1
    r3 = R3[0] + 1  # 0 1 1
    r4 = R4[0] + 0  # 1 1 1

    return [r1, r2, r3, r4]

def inputData_2(A):
    R1 = A.subs([ [x1,0], [x2,0], [x3,1] ])
    R2 = A.subs([ [x1,1], [x2,0], [x3,1] ])
    R3 = A.subs([ [x1,0], [x2,1], [x3,1] ])
    R4 = A.subs([ [x1,1], [x2,1], [x3,1] ])

    r1 = R1[0] - Matrix([0,0])
    r2 = R2[0] - Matrix([1,1])
    r3 = R3[0] - Matrix([1,1])
    r4 = R4[0] - Matrix([0,0])

    return [r1, r2, r3, r4]

def define_w(gr,d):
    result = []
    for e in gr.exprs:
        t = Matrix([e])
        t = t.subs(d)
        t = t.evalf()
        result.append(t)
    return result    

def main_1():
    W1 = Matrix([[w1],[w2]])
    W2 = Matrix([[w3],[w4]])
    W3 = Matrix([[w5],[w6]])

    X1 = Matrix([[x1],[x2]])
    X2 = Matrix([[x2],[x3]])

    A1 = W1.T * X1
    A2 = W2.T * X2

    A1 = activateFunc(A1)
    A2 = activateFunc(A2)

    print(A1)
    print(A2)


    A12 = Matrix([A1[0],A2[0]])
    print(A12)

    A = W3.T * A12

    print(A)

    r1 = inputData(A)

    print(groebner(r1))

def main_2():
    W1 = Matrix([[w14, w24, w34], [w15, w25, w35]])
    W2 = Matrix([[w46, w56]])

    X1 = Matrix([[x1], [x2], [x3]])
    
    print(W1)
    print(W2)

    A1 = W1 * X1
    A1 = activateFunc(A1)

    print(A1)

    A2 = W2 * A1
    A2 = activateFunc(A2)

    print(A2)

    r = inputData(A2)
    gr = groebner(r)

    print(gr)

    return gr


def main_3():
    W1 = Matrix([[w14, w24, w34]])
    X1 = Matrix([[x1], [x2], [x3]])

    A1 = W1 * X1
    A1 = activateFunc(A1)

    print(A1)

    r = inputData(A1)

    print(r)

    gr = groebner(r)
    print(gr)

    #res = define_w(gr, [[w34, -6.8]])
    
    return gr

if __name__ == "__main__":
    gr = main_3()
    res = define_w(gr, [[w34, 10]])
    print(res)
    #res = define_w(gr,[[w34, 10],[w24, -10], [w14, -10]])
    #print(res)

