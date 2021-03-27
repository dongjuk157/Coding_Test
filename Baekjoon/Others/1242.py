N, K, M = map(int,input().split())
result = 0
tmp_m = M
while result < N:
    result += 1
    if K % (N - result + 1) == tmp_m % (N - result + 1):
        break
    if K == tmp_m:
        break
    else:
        tmp_m -= K
        while tmp_m <= 0:
            tmp_m += (N - result + 1)

print(result)


