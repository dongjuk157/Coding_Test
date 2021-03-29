import sys
input = sys.stdin.readline

from collections import deque
delta = [(-2, -1), (-2, 1), (2, -1),(2, 1),
         (-1, -2), (-1, 2), (1, -2),(1, 2)]

for tc in range(int(input())):
    n = int(input())
    matrix = [[-1] * n for _ in range(n)]
    x, y = map(int, input().split())
    wx, wy = map(int, input().split())
    q = deque()
    q.append((x, y))
    matrix[x][y] = 0

    def bfs(queue, destination):
        if matrix[destination[0]][destination[1]] != -1:
            return
        tmp_q = deque()
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                dx = x + delta[i][0]
                dy = y + delta[i][1]
                if dx < 0 or dx >= n or dy < 0 or dy >= n: continue
                if matrix[dx][dy] != -1: continue
                tmp_q.append((dx, dy))
                matrix[dx][dy] = matrix[x][y] + 1
        bfs(tmp_q, destination)

    bfs(q, (wx,wy))
    print(matrix[wx][wy])
