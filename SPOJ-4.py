# my_dict = dict()
# #key = input("Enter the key: ")
# #value = input("Enter the value: ")
# name, value=input()
# my_dict[name] = value
# print(my_dict)

"""n = int(input())
d = dict(input().split() for _ in range(n))
print (d)
print(sorted(d.values()))
print(d)"""

"""for _ in range(int(input())):
	a, b = map(int, input().split())
	print (a * b)"""


# test = int(input())
# for i in range(0,test):
#     n = int(input())
#     k=n+1
#     while k < 1000000 :
#         c=k
#         st=str(c)
#         if st == st[::-1]:
#             break
#         k += 1
#     print(st)

"""T=int(input())
for i in range(T):
    n=input()
    A=[]
    for i in n:
        A.append(i)
    if len(n)==1:
        print(int(n)+1)
    elif n==n[::-1]:
        if len(n)%2==1:
            int(A[(len(n)+1)//2])+=1
        else:
            int(A[len(n)//2])+=1
        print(A)
    else:
        while n!=n[::-1]:
            n=str(int(n)+1)
        print(n)"""

t,n =map(int,input().split())
for t in range(t):
    a=int(input())
    if(a<n):
        print("Bad boi")
    else:
        print("Good boi")
