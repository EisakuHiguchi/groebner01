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
		[3.382219091542679, -0.8469657102458379, -0.503925721263563], \
		[4.041814394745013, 4.619087381978036, -0.6558632685417835], \
		[-2.5098945335589846, 4.22870944209639, 1.0490917396825894] \
		])

    W2 = Matrix([ \
        [-3.453323154233995, 5.376950275446613, -3.517647020953983] ,\
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
    A1 = A1.subs([[x0, i0], [x1, i1], [x2, 1]])
    
    print("sum : ")
    print(A1)
    
    print("act : ")
    print(activateFunc(A1))
    
    A2 = W2 * activateFunc(A1)
    #A2 = W2 * A1
    #print(activateFunc(A1))
    print("sum : ")
    print(A2)

    #A3 = A2.subs([[x0, i0], [x1, i1], [x2, 1]])
    #print(activateFunc(A3))
    print("act : ")
    print(activateFunc(A2))
    

    
if __name__ == "__main__":
    #func([x1 + x2 + 4] + [x1**2 + x2**2])
    func1(0,0)
