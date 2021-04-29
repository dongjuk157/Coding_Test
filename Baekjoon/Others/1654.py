K, N = map(int, input().split())
N_list = [int(input()) for _ in range(K)]
result = 0
s, e = 1, max(N_list)
# 1, 802 => m =401
while s <= e:
    m = (s + e) // 2
    key = sum([num // m for num in N_list]) # 5
    if key < N: # => m의 값이 큰경우 => m을 줄이는 방향
        e = m - 1
    else: # key => N
        s = m + 1
        result = max(result, m) # 랜선의 최대 길이를 찾아야 하므로
print(result)