# import sys; input = sys.stdin.readline
N, M = map(int, input().split())
wok = list(map(int, input().split()))
wok_set = [False for _ in range(10001)]
for i in range(M):
    wok_set[wok[i]] = True
    for j in range(i + 1, M):
        if wok[i] + wok[j] > N: continue
        wok_set[wok[i] + wok[j]] = True
INF = 1234567890
memo = [INF for _ in range(10001)]
memo[0] = 0
for i in range(N + 1):
    if wok_set[i]:
        memo[i] = 1;
for i in range(N):
    for k in range(N):
        if not wok_set[k]: continue
        if i + k > N: continue
        memo[i + k] = min(memo[i] + 1, memo[i + k])

if INF == memo[N]:
    print(-1)
else:
    print(memo[N])
