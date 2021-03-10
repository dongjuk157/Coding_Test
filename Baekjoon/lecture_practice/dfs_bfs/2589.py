from collections import deque
n, m = map(int, input().split())
_map = [ input() for i in range(n)]

def bfs(x, y):
    delta= [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque()
    q.append((x, y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    val = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if _map[nx][ny] == 'L':
                        q.append((nx, ny))
                        val = visited[x][y] + 1
                        visited[nx][ny] = val
    return val

dist = 0
for i in range(n):
    for j in range(m):
        if _map[i][j]=='L':
            dist = max(dist, bfs(i, j))
print(dist)