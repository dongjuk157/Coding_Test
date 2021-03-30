from collections import deque
n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 벽을 부순경우, 부수지 않은 경우
visit[0][0][0] = 1
q = deque([(0, 0, 0)])
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(q):
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m -1:
            return visit[x][y][z]
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 > dx or n <= dx or 0 > dy or m <= dy: continue
            if not matrix[dx][dy] and not visit[dx][dy][z]:
                visit[dx][dy][z] = visit[x][y][z] + 1
                q.append((dx, dy, z))
            elif not z and matrix[dx][dy] and not visit[dx][dy][1]:
                visit[dx][dy][1] = visit[x][y][z] + 1
                q.append((dx, dy, 1))
    return -1

print(bfs(q))