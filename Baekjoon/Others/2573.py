import sys; input = sys.stdin.readline;
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for dt in delta:
            dr = r + dt[0]
            dc = c + dt[1]
            if 0 <= dr < H and 0 <= dc < W:
                if glacier[dr][dc] and not visit[dr][dc]:
                    q.append((dr, dc))
                    visit[dr][dc] = 1


H, W = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(H)]

delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
answer = 0
while True:
    answer += 1
    visit = [[0 for _ in range(W)] for _ in range(H)]
    mass = 0
    # 녹는 값 저장
    for r in range(H):
        for c in range(W):
            if not visit[r][c] and glacier[r][c]:
                for dt in delta:
                    dr = r + dt[0]
                    dc = c + dt[1]
                    if 0 <= dr < H and 0 <= dc < W:
                        if not glacier[dr][dc]:
                            visit[r][c] += 1
    # 빙하 녹이기
    for r in range(H):
        for c in range(W):
            if visit[r][c] > 0:
                glacier[r][c] -= visit[r][c]
                if glacier[r][c] < 0:
                    glacier[r][c] = 0
    # 덩어리 개수
    visit = [[0 for _ in range(W)] for _ in range(H)]
    for r in range(H):
        for c in range(W):
            # 같은 덩어리 탐색
            if glacier[r][c] and not visit[r][c]:
                visit[r][c] = 1
                mass += 1
                bfs(r, c)

    if mass > 1:
        # answer -= 1
        break
    elif mass == 0:
        answer = 0
        break
print(answer)