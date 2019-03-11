#CANDY3 - Candy I
n = 0
while(n > -1):
    n=int(input())
    #print('my n',n);
    if n == -1:
        break
    t=n
    a=[]
    move=0
    while(t):
        b=int(input())
        #print('my b',b);
        if b:
            a.append(b)
        t=t-1
    if(sum(a)%len(a)==0):
        avg = sum(a)/len(a)
        for i in a:
            if(i>avg):
                c=i-avg
                move=move+c
        print(int(move))
    else:
        print("-1")













