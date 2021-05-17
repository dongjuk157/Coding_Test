import sys; input = sys.stdin.readline
# from collections import deque
from heapq import heappop, heappush
M, N = map(int, input().rstrip().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visit = [[M + N] * M for _ in range(N)]
def bfs():
    q = [(0, 0, 0)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visit[0][0] = 0
    while q:
        w, r, c = heappop(q)
        if r == N and c == M: return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visit[nr][nc] > visit[r][c] + matrix[r][c]:
                visit[nr][nc] = visit[r][c] + matrix[r][c]
                heappush(q, (visit[nr][nc], nr, nc))


bfs()
print(visit[N-1][M-1])