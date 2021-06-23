from collections import deque
def bfs():
    q = deque()
    q.append((0, 0, 0, -1, 0))
    while q:
        x, y, oldx, oldy, dist = q.popleft()
        if (x, y) == (N - 1,N + 1):
            return dist
        if 0 > x or x >= N or 0 > y or y >= N + 2 or arr[x][y] == 0:
            continue
        if arr[x][y] <= 2:  # 직진
            q.append((2 * x - oldx, 2 * y - oldy, x, y, dist + 1))
        else:  # 회전
            q.append((x + y - oldy, y + x - oldx, x, y, dist + 1))
            q.append((x - y + oldy, y - x + oldx, x, y, dist + 1))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = N ** 2
    arr = [[0] + list(map(int, input().split()))+[0] for _ in range(N)]
    arr[0][0], arr[N - 1][N + 1] = 1, 1
    result = bfs() - 1
    print(f"#{tc} {result}")