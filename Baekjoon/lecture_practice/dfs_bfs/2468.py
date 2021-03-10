from collections import deque

n = int(input())
area = []
min_rain, max_rain = 100, 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    area.append(tmp)
    min_tmp, max_tmp = min(tmp), max(tmp)
    if max_rain < max_tmp:
        max_rain = max_tmp
    if min_rain > min_tmp:
        min_rain = min_tmp

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, rain): # x,y = r,c
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny]: continue
                if area[nx][ny] <= rain: continue
                q.append((nx, ny))
                visit[nx][ny] = 1

max_val = 1
for _rain in range(min_rain, max_rain + 1):
    visit = [[0] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j]: continue
            if area[i][j] > _rain:
                result += 1
                bfs(i, j, _rain)
                if max_val < result:
                    max_val = result

print(max_val)