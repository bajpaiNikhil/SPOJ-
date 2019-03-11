#PALIN - The Next Palindrome
t=int(input())
for t in range(t):

    def palindrome(num , n):
        mid=int(n/2)
        ls=False
        i=mid-1
        j=mid+1 if (n%2) else mid
        while(i>=0 and num[i]==num[j]):
            i-=1
            j+=1
        if(i<0 or num[i]<num[j]):
            ls=True
        while(i>=0):
            num[j]=num[i]
            j+=1
            i-=1
        if(ls==True):
            carry=1
            i=mid-1
            if(n%2==1):
                num[mid]+=carry
                carry=int(num[mid]/10)
                num[mid]%=10
                j=mid+1
            else:
                j=mid

            while(i>=0):

                num[i]+=carry
                carry=int(num[i]/10)
                num[i]%=10
                num[j]=num[i]
                j+=1
                i-=1

    def nextPalindrome(num,n):

        if (nines(num,n) ==True):
            print("1")
            for i in range(1,n):
                print("0")
            print("1")

        else:
            palindrome(num,n)
            printArray(num,n)

    def nines(num,n):
        for i in range(n):
            if(num[i]!=9):
                return 0
        return 1
    def printArray(arr,n):

        for i in range(0,n):
            print(int(arr[i]),end="")
        print()

    a=int(input())
    num=list(map(int,str(a)))
    n=len(num)
    nextPalindrome(num,n)

"""a="1234567890"
b=a*9
print(b)
c=b*9
print(c)
d=c*9
print(d)
e=d*9
print(e)
f=e*9
print(f)"""








