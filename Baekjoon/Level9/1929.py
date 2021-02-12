m, n = map(int, input().split())
#m, n = 3, 16

prime=[False,False,]+[True]*(n-1)
for i in range(2,n+1):
    if prime[i]:
        for j in range(2*i,n+1,i):
            prime[j] = False
        if i >= m:
            print(i)
