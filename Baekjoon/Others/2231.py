#N-54 ~N-1중에 만들수있는지 확인

N=int(input())
result = 0
try:
    for n in range(N-54,N):
        temp = n
        for ch in str(n):
            temp += int(ch)
        if temp == N:
            result = n
            break
    else:
        result = 0
except: 
    pass
print(result)