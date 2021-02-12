tmp = 123456*2
prime=[False,False]+[True]*(tmp)
for i in range(2,int(tmp**0.5)+1):
    if prime[i]:
        for j in range(2*i,tmp+1,i):
            prime[j]=False

while True:
    n = int(input())
    if n == 0:
        break
    print(prime[n+1:2*n+1].count(True))