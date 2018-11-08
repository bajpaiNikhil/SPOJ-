"""def binarySearch(arr, low, high, x):
    if (high >= low):
        mid = low + (high - low) // 2
        if x == arr[mid]:
            return (mid)
        elif (x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
    return -1
def countPairsWithDiffK(arr, n, k):
    count = 0
    arr.sort()
    for i in range(0, n - 1):
        if (binarySearch(arr, i + 1, n - 1,arr[i] + k) != -1):
            count += 1

    return count
#arr = [5,3,2,4,1]
#n = len(arr)
#k = 2
n,k=map(int,input().split())
arr=list(map(int,input().split()[:n]))
print(countPairsWithDiffK(arr, n, k))"""



"""t=int(input())
for t in range(t):
    n,m=map(int,input().split())
    c=str(n)[::-1]
    z=int(c)
    #print(z)
    d=str(m)[::-1]
    y=int(d)
    e=z+y
    f=str(e)[::-1]
    g=int(f)
    print(g)"""




"""import math
def countRect(n):
    ans = 0
    for length in range(1, int(math.sqrt(n)) + 1):
        height = length
        while (height * length <= n):
            ans += 1
            height += 1
    return ans
n = int(input())
print(countRect(n))"""
























