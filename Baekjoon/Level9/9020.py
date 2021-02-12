#import sys
#input = sys.stdin.readline

#에라토스테네스의 체로 소수를 먼저 구함
max_number= 10000
prime=[False,False,]+[True]*(max_number - 1)
for i in range(2,int(max_number**0.5)+1):
    if prime:
        for j in range(2*i,max_number+1,i):
            prime[j] = False
prime_num = [i for i,v in enumerate(prime) if v] #1229개

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    # n을 2로 나눈 수에서 가장 큰 소수부터 2까지 확인, (n-소수) 가 소수인지확인
    for i in range(n//2,1,-1): # n=4, i=2
        if prime[i] and prime[n-i]:
            s,b = i, n-i
            break
    print(f"{s} {b}")


