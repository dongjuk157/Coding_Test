n, k, l = map(int, input().split())
cnt = 0
while k != l:
    k = (k - 1) // 2 + 1
    l = (l - 1) // 2 + 1
    cnt += 1
print(cnt)