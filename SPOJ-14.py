#LASTDIG - The last digit

t=int(input())
for t in range(t):

    def lastDigit(a,b):

        if(b==0):
            print("1")
        else:
            a = a % 10
            #print(a)
            b = b % 4
            #print(b)
            if b == 0:
                b = 4

            print(pow(a, b) % 10)

    a,b=map(int,input().split())
    lastDigit(a,b)
