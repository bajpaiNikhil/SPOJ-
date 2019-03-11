#NSTEPS - Number Steps
t=int(input())
for t in range(t):
    a, b = map(int, input().split())
    if(a!=b and (a-b)!=2):
        print("No Number")
    elif(a%2==0 and b%2==0):
        print(a+b)
    else:
        print(a+b-1)


