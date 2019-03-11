#PIR - Pyramids
from math import *
t=int(input())
for t in range(t):
    def tetrahedrons(a,b,c,d,e,f):
        a1=(pow(a,2))
        a2=(pow(b,2))
        a3=(pow(c,2))
        a4=(pow(d,2))
        a5=(pow(e,2))
        a6=(pow(f,2))
        a = (4 * (a1 * a2 * a3)
             - a1 * pow((a2 + a3 - a4), 2)
             - a2 * pow((a3 + a1 - a5), 2)
             - a3 * pow((a1 + a2 - a6), 2)
             + (a2 + a3 - a4) * (a3 + a1 - a5)
             * (a1 + a2 - a6))
        #print(a)
        v = sqrt(a)
        v =v/12
        z=str(round(v,4))
        #print(end="")
        return "".join(z)
        #print()
    a,b,c,d,e,f=map(int,input().split())
    print(tetrahedrons(a,b,c,d,e,f))


