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

def inputData(A, teach):
    R1 = A.subs([ [x1,0], [x2,0], [x3,1] ])
    R2 = A.subs([ [x1,1], [x2,0], [x3,1] ])
    R3 = A.subs([ [x1,0], [x2,1], [x3,1] ])
    R4 = A.subs([ [x1,1], [x2,1], [x3,1] ])

    r1 = R1[0] - teach[0]  # 0 0 1
    r2 = R2[0] - teach[1]  # 1 0 1
    r3 = R3[0] - teach[2]  # 0 1 1
    r4 = R4[0] - teach[3]  # 1 1 1

    return [r1, r2, r3, r4]

def inputData_2(A, teach):
    R1 = A.subs([ [x1,0], [x2,0], [x3,1] ])
    R2 = A.subs([ [x1,1], [x2,0], [x3,1] ])
    R3 = A.subs([ [x1,0], [x2,1], [x3,1] ])
    R4 = A.subs([ [x1,1], [x2,1], [x3,1] ])

    r1 = R1[0] - Matrix([teach[0],teach[0]])
    r2 = R2[0] - Matrix([teach[1],teach[1]])
    r3 = R3[0] - Matrix([teach[2],teach[2]])
    r4 = R4[0] - Matrix([teach[3],teach[3]])

    return [r1, r2, r3, r4]

def define_w(gr,d):
    result = []
    for e in gr.exprs:
        t = Matrix([e])
        t = t.subs(d)
        t = t.evalf()
        result.append(t)
    return result    
