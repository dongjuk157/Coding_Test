import sys
sys.stdin = open('.idea/1953_input.txt','r')

from collections import deque
tunnel = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상하좌우
    2: [(-1, 0), (1, 0)],    # 상하
    3: [(0, -1), (0, 1)],    # 좌우
    4: [(-1, 0), (0, 1)],    # 상우
    5: [(1, 0), (0, 1)],     # 하우
    6: [(1, 0), (0, -1)],    # 하좌
    7: [(-1, 0), (0, -1)],   # 상좌
}
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((R, C))
    visited[R][C] = 1
    def bfs(L):
        result = 1
        while q:
            x, y = q.popleft()
            direction = tunnel[_map[x][y]]
            for i in range(len(direction)):
                dx = x + direction[i][0]
                dy = y + direction[i][1]
                if dx < 0 or dx >= N or dy < 0 or dy >= M: continue
                if visited[dx][dy] or _map[dx][dy] == 0: continue
                if tunnel_chk(x, y, dx, dy): continue
                q.append((dx, dy))
                visited[dx][dy] = visited[x][y] + 1
                if visited[dx][dy] > L:
                    break
                result += 1
        return result

    def tunnel_chk(x, y, dx, dy):
        temp_direction = tunnel[_map[dx][dy]]
        for i in range(len(temp_direction)):
            nx = dx + temp_direction[i][0]
            ny = dy + temp_direction[i][1]
            if x == nx and y == ny: return False
        return True

    print("#{} {}".format(tc, bfs(L)))
