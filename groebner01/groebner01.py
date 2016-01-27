import re
import datetime
from sympy import *

x0,x1,x2,x3,x4,x5,x6,x7 = symbols('x0 x1 x2 x3 x4 x5 x6 x7')

def func(g):
    f = open("c:\work\Data\groebner01_" + datetime.datetime.today().strftime(("%Y%m%d%H%M%S")) + ".txt","w")

    G = groebner(g)
    
    f.write('before: ')
    f.write(' , '.join(map(str, g)))
    f.write('\ngroebner: ')
    f.write(' , '.join(map(str, G.exprs)))
    f.write('\n\n')
    #f.write('\n'.join(map(str,solve(G.exprs))))
    for e in G.exprs:
        f.write(',\n'.join(map(str,solve(Eq(e,0)))))

    print('before: ')
    print(' , '.join(map(str, g)))
    print('\ngroebner: ')
    print(' , '.join(map(str, G.exprs)))
    #print('\n'.join(map(str,solve(G.exprs))))
    for e in G.exprs:
        print(',\n'.join(map(str,solve(Eq(e,0)))))


def genW(n):
    W1 = Matrix([ \
        [-1.6491905466464132, 2.750524819669519, 4.6341686586378925] ,\
        [3.879940487206725, -0.024429397172418453, 5.476242318746077] , \
        [0.5370499493354627, -1.141172485316484, -1.2872411534308608] \
        ])

    W2 = Matrix([ \
        [-3.587083813471922, -3.821207438213313, 5.656872762497493] ,\
        ])

    if n == 1:
        return W1
    else:
        return W2
    
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


def func1(i0 , i1):
    W1 = genW(1)
    W2 = genW(2)
    X1 = Matrix([ [x0], [x1], [x2] ])
    X2 = Matrix([ [x3], [x4], [x5] ])

    A1 = W1 * X1
    #print(A1)

    A1 = A1.subs([[x0, i0], [x1, i1], [x2, 0]])
    A2 = W2 * activateFunc(A1)
    #print(A2)

    A3 = A2.subs([[x0, i0], [x1, i1], [x2, 0]])
    #print(A3)
    print(activateFunc(A3))
    

    
if __name__ == "__main__":
    #func([x1 + x2 + 4] + [x1**2 + x2**2])
    func1(0,0)
