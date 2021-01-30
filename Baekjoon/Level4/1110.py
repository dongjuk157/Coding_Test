N = int(input())
cnt = 0
orig_N = N

while True:
    if N < 10:          
        N *= 11
    else:
        tmp = (N//10) + (N%10)    
        N = (N % 10)*10 + (tmp%10) 
    cnt += 1
    if N == orig_N:
        break

print(cnt)
