import sys; input = sys.stdin.readline
N = int(input())
INF = 2_000_000
rgb = [list(map(int, input().split())) for _ in range(N)]
memo = [[0 for _ in range(3)] for _ in range(N)]

answer = INF
for f in range(3): # 첫번째 고정
    for i in range(3):
        memo[0][i] = INF if i == f else rgb[0][i]

    for i in range(N - 1):
        memo[i + 1][0] = min(memo[i][1], memo[i][2]) + rgb[i+1][0]
        memo[i + 1][1] = min(memo[i][0], memo[i][2]) + rgb[i+1][1]
        memo[i + 1][2] = min(memo[i][1], memo[i][0]) + rgb[i+1][2]

    for i in range(3):
        if i == f:
            answer = min(answer, memo[N-1][i])

print(answer)



