import sys; input = sys.stdin.readline

m, n = map(int, input().split())
_map = [[-1 for _ in range(n + 2)] for _ in range(m + 2)]
for r in range(m):
    tmp = list(map(int, input().split()))
    for c in range(n):
        _map[r + 1][c + 1] = tmp[c]
memo = [[-1 for _ in range(n + 2)] for _ in range(m + 2)]
# print(*_map, sep='\n')
ans = 0
# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def dfs(y, x):
    if (y, x) == (m, n):
        return 1
    elif memo[y][x] == -1:
        memo[y][x] = 0
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if _map[yy][xx] == -1: continue
            if _map[yy][xx] < _map[y][x]:
                memo[y][x] += dfs(yy, xx)
    return memo[y][x]

print(dfs(1, 1))