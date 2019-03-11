#EMTY2 - Can You Make It Empty
t = int(input())
for t in range(t):
    def empty(num):
        d = num.count(1)
        e = num.count(0)
        if (e / d) == 2:
            return True
        return False


    n = (input())
    num = list(map(int, str(n)))
    # print(num.con)
    if (n == 0):
        print("Case " + str(t + 1) + ":" " no")

    elif ((n[0] == "0") or (n[-1]) == "1" or (n[-1] == "0" and n[-2] == "1") or (n[0] == "0" and n[1] == "1")):

        print("Case " + str(t + 1) + ":" " no")

    elif (empty(num)):
        print("Case " + str(t + 1) + ":" " yes")

    else:
        print("Case " + str(t + 1) + ":" " no")
