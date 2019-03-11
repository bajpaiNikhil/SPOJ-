#FCTRL2 - Small factorials
t=int(input())
for t in range(t):
    n=int(input())
    def factorial(n):
        if n==1:
            return n
        else:
            return n*factorial(n-1)
    print(factorial(n))
