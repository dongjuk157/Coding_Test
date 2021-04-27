import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
visit = [[0] * M for _ in range(N)]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = 1
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 > dx or dx >= N or 0 > dy or dy >= M: continue
            if matrix[dx][dy] == '0': continue
            if visit[dx][dy]: continue
            visit[dx][dy] = visit[x][y] + 1
            q.append((dx, dy))

bfs(0, 0)
print(visit[N-1][M-1])