n,k=map(int,input().split())
prime=[False,False]+[True]*(n-1)
index = 0
result = 0
#index += 1 # K번째 지우는 수
for number, val in enumerate(prime):
    if val: # number가 True이면
        for i in range(number,n+1,number):
            if prime[i]:
                prime[i]=False
                index+=1
            if index==k:
                result = i
                break
print(result)

