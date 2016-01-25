import re
import datetime
from sympy import *

x1,x2,x3,x4,x5,x6,x7 = symbols('x1 x2 x3 x4 x5 x6 x7')

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

    

    
if __name__ == "__main__":
    func([x1 + x2 + 4] + [x1**2 + x2**2])