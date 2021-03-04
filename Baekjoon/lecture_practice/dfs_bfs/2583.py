from collections import deque


def bfs(row, col):
    q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q.append((row, col))
    matrix[row][col] = 1
    while q:
        nr, nc = q.popleft()
        for i in range(4):
            if 0 <= nr + dr[i] < m and 0 <= nc + dc[i] < n:
                if matrix[nr + dr[i]][nc + dc[i]] == 1: continue
                q.append((nr + dr[i], nc + dc[i]))
                matrix[nr + dr[i]][nc + dc[i]] = 1
                global area
                area += 1


m, n, k = map(int, input().split())
matrix = [[0] * n for _ in range(m)]
for _ in range(k):
    # r= 4, c = 6
    ld_c, ld_r, ru_c, ru_r = map(int, input().split())
    for r in range(ld_r, ru_r):
        for c in range(ld_c, ru_c):
            matrix[r][c] = 1
cnt, area = 0, 0
area_list = []

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            cnt += 1
            area = 1
            bfs(i, j)
            area_list.append(area)
print(cnt)
print(*sorted(area_list))


