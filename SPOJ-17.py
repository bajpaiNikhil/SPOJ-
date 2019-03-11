##TRICOUNT - Counting Triangles
#from ctypes import c_longlong as ll

t=int(input())
for t in range(t):

    n = int(input())
    if(n%2==0):
        count= int((n*(n+2)*((2*n+1)/8)))
        print(count)
        
    else:
        """count=int((((n*(n+2))*int((2*n+1))-1)/8))
        print(count)"""
