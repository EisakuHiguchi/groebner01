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

def func_A(G):
    print('\n solve groebner: ')
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

    #w03,w13,w23,w04,w14,w24,w05,w15,w25,w36,w46,w56 = symbols('w03 w13 w23 w04 w14 w24 w05 w15 w25 w36 w46 w56')
    #W1 = Matrix([\
    #    [ w03, w04, w05] ,\
    #    [ w13, w14, w15] ,\
    #    [ w23, w24, w25]\
    #    ])
    #W2 = Matrix([\
    #    [ w36, w46, w56]\
    #    ])


    X1 = Matrix([ [x0], [x1], [x2] ])
    X2 = Matrix([ [x3], [x4], [x5] ])

    A1 = W1 * X1
    G1 = groebner(A1)
    Ga1 = groebner(activateFunc(A1))
    
    A2 = W2 * activateFunc(A1)
    G2 = groebner(A2)
    Ga2 = groebner(activateFunc(A2))
    
    #A3 = A2.subs([[x0, i0], [x1, i1], [x2, 1]])
    A3 = A2.subs([[x0, i0], [x2, 1]])
    G3 = groebner(A3)
    Ga3 = groebner(activateFunc(A3))
    

    # record
    print("\nA1 = W1 * X1\n")
    print(A1)
    print("\nG1 = groebner(A1)\n")
    print(G1)
    print("\nGa1 = groebner(activate(A1))\n")
    print(Ga1)
    print("\nA1 = W2 * activate(A1)\n")
    print(A2)
    print("\nG2 = groebner(A2)\n")
    print(G2)
    print("\nGa2 = groebner(activate(A2))\n")
    print(Ga2)
    print("\nA3 : solve A2\n")
    print(A3)
    print("\nG3 = groebner(A3)\n")
    print(G3)
    print("\nGa3 = groebner(activate(A3)\n")
    print(Ga3)
    print("\noutput = activate(A3)\n")
    print(activateFunc(A3))
    
    f = open("c:\work\Data\groebner01_" + datetime.datetime.today().strftime(("%Y%m%d%H%M%S")) + ".txt","w")

    f.write("data\n")
    f.write("W1\n")
    f.write(' , '.join(map(str, W1.tolist())))
    f.write("W2\n")
    f.write(' , '.join(map(str, W2.tolist())))
    f.write("X1\n")
    f.write(' , '.join(map(str, X1.tolist())))
    f.write("X2\n")
    f.write(' , '.join(map(str, X2.tolist())))

    f.write("\n\n\nA1 = W1 * X1\n")
    f.write(' , '.join(map(str, A1.tolist())))
    f.write("\n\nG1 = groebner(A1)\n")
    f.write(' , '.join(map(str, G1.exprs)))
    f.write("\n\nGa1 = groebner(activate(A1))\n")
    f.write(' , '.join(map(str, Ga1.exprs)))
    f.write("\n\nA1 = W2 * activate(A1)\n")
    f.write(' , '.join(map(str, A2.tolist())))
    f.write("\n\nG2 = groebner(A2)\n")
    f.write(' , '.join(map(str, G2.exprs)))
    f.write("\n\nGa2 = groebner(activate(A2))\n")
    f.write(' , '.join(map(str, Ga2.exprs)))
    f.write("\n\nA3 : solve A2\n")
    f.write(' , '.join(map(str, A3.tolist())))
    f.write("\n\nG3 = groebner(A3)\n")
    f.write(' , '.join(map(str, G3.exprs)))
    f.write("\n\nGa3 = groebner(activate(A3)\n")
    f.write(' , '.join(map(str, Ga3.exprs)))
    f.write("\n\noutput = activate(A3)\n")
    f.write(' , '.join(map(str, activateFunc(A3).tolist())))

    
if __name__ == "__main__":
    #func([x1 + x2 + 4] + [x1**2 + x2**2])
    func1(0,0)
