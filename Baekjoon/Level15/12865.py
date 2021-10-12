import sys; input = sys.stdin.readline
N, K = map(int, input().split())
stuff_list = [tuple(map(int, input().split())) for _ in range(N)]
memo = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1) :
    for j in range(1, K + 1):
        if stuff_list[i - 1][0] > j:
            memo[i][j] = memo[i - 1][j]
        else:
            memo[i][j] = max(memo[i - 1][j],
                             stuff_list[i - 1][1] + memo[i - 1][j - stuff_list[i - 1][0]])

print(memo[N][K])